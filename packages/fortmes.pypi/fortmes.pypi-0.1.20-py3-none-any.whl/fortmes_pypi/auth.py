import aiohttp
import asyncio

import logging

LOGGER = logging.getLogger(__name__)


class Auth0Client:
    def __init__(self, auth0_domain, client_id):
        self.auth0_domain = auth0_domain
        self.client_id = client_id

    async def device_authorization(self):
        # Step 1: Request device code and user code
        # Device code needs to be displayed on the intergation
        device_authorization_url = f"https://{self.auth0_domain}/oauth/device/code"
        data = {
            "client_id": self.client_id,
            "scope": "openid profile",  # Define required scopes
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(device_authorization_url, json=data) as response:
                response_data = await response.json()

        self.device_code = response_data["device_code"]
        self.user_code = response_data["user_code"]
        verification_uri = response_data["verification_uri"]
        return [self.device_code, self.user_code, verification_uri]

    ## Seperate Class
    async def token_validation(self):
        # Step 2: Poll for user authentication
        authorization_endpoint = f"https://{self.auth0_domain}/oauth/token"
        data = {
            "client_id": self.client_id,
            "device_code": self.device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        }
        LOGGER.info("The while cycle starts.")
        while True:
            LOGGER.info("Next or First cycle.")
            async with aiohttp.ClientSession() as session:
                LOGGER.info(
                    f"POST sent to Auth0 service with authorization_endpoint: {authorization_endpoint} and json-data: {data}."
                )
                async with session.post(authorization_endpoint, json=data) as response:
                    LOGGER.info(
                        f"waiting for response from server. Response is: {response}"
                    )
                    if response.status == 200:
                        auth_response = await response.json()
                        return auth_response["access_token"]
                    elif response.status == 400:
                        error_data = await response.json()
                        # _LOGGER.error("Module Error: %s", error_data)
                        if error_data["error"] == "authorization_pending":
                            await asyncio.sleep(5)  # Wait and retry
                        else:
                            raise Exception(
                                f"Authorization error: {error_data['error_description']} {self.auth0_domain} {self.client_id} {self.device_code}"
                            )
                    else:
                        raise Exception(
                            f"Unexpected response: {response.status} - {await response.text()} {self.auth0_domain} {self.client_id} {self.device_code} {self.user_code}"
                        )
