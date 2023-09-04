import logging
import time
import boto3 # 07/12 : make sure you have boto 3 installed ( pip install boto3 )

LOGGER = logging.getLogger(__name__)

class AWSCognitoTokenizer():


    def _generate_token(self, region, client_app_id, username, password, ttl):
        try:
            client = boto3.client('cognito-idp', region_name=region)
            resp = client.initiate_auth(ClientId=client_app_id, AuthFlow='USER_PASSWORD_AUTH', AuthParameters={"USERNAME": username, "PASSWORD": password})
            expiration_time = time.time() + ttl
            return True, resp['AuthenticationResult']['AccessToken'], expiration_time
        except Exception as e:
            LOGGER.error('Error encountered when trying to generate token: {}'.format(e))
            return False, None, None

    def _refresh_token(self):
        success, token, expiration = self._generate_token(self.region, self.client_app_id, self.username, self.password, self.ttl)
        if success:
            self.cognito_access_token = token
            self.token_expiration = expiration

    def get_cognito_access_token(self, request_form):
        token = request_form.api_token
        if token:
            return token

        # Check if token has expired, and refresh if needed
        if self.token_expiration and time.time() > self.token_expiration:
            self._refresh_token()

        return self.cognito_access_token