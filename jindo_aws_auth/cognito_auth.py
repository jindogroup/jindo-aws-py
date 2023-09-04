import logging
import time
import boto3 # 07/12 : make sure you have boto 3 installed ( pip install boto3 )

LOGGER = logging.getLogger(__name__)


def generate_aws_cognito_token(region, client_app_id, username, password, ttl):
    try:
        client = boto3.client('cognito-idp', region_name=region)
        resp = client.initiate_auth(ClientId=client_app_id, AuthFlow='USER_PASSWORD_AUTH', AuthParameters={"USERNAME": username, "PASSWORD": password})
        expiration_time = time.time() + ttl
        return True, resp['AuthenticationResult']['AccessToken'], expiration_time
    except Exception as e:
        LOGGER.error('Error encountered when trying to generate token: {}'.format(e))
        return False, None, None


class AWSCognitoTokenizer():
    """
        username (str, optional): The username for token generation.
        password (str, optional): The password for token generation.
        region (str, optional): The AWS region for token generation.
        client_app_id (str, optional): The client application ID for token generation.
        ttl (int, optional): Time to live for the token in seconds. Defaults to 1800.
        token_expiration (int): The expiration time of the cognito token in seconds since the epoch. None if no token generated.
    """

    def __init__(self, username=None, password=None, region=None, client_app_id=None, ttl=1800):
        self.username = username
        self.password = password
        self.region = region
        self.client_app_id = client_app_id
        self.ttl = ttl
        self.token_expiration = None

        self._refresh_token()

    def _refresh_token(self):
        success, token, expiration = generate_aws_cognito_token(self.region, self.client_app_id, self.username, self.password, self.ttl)
        if success:
            self.cognito_access_token = token
            self.token_expiration = expiration

    def get_cognito_access_token(self):

        # Check if token has expired, and refresh if needed
        if self.token_expiration and time.time() > self.token_expiration:
            self._refresh_token()

        return self.cognito_access_token