import json
from google.cloud import secretmanager
import jwt

# Need to change to accept request and attach user oauth id to request.oauth_id
# object = TokenManager(project_id=xxxxxx, secret=xxxxxx, oauth_id=xxxxxx)


class TokenManager:


    def __init__(self, *arg, **kwargs):
        self.project_id = kwargs.get('project_id', None)
        self.secret_title = kwargs.get('secret_title', None)
        self.oauth_id = kwargs.get('oauth_id', None)
    
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, new_project_id):
        # You can add custom logic here, if needed
        self._project_id = new_project_id

    @property
    def secret_id(self):
        return self._secret_id

    @secret_id.setter
    def secret_id(self, new_secret_id):
        # You can add custom logic here, if needed
        self._secret_id = new_secret_id

    @project_id.deleter
    def project_id(self):
        del self._project_id

    @secret_id.deleter
    def secret_id(self):
        del self._secret_id

    def validate_token(self, token, audience):
        secret_key_list = self.get_token_secret()

        for secret_key in secret_key_list:
            try:
                decoded_payload = jwt.decode(
                    token, secret_key, audience=audience, algorithms=['HS256'])

                self.oauth_id = self.get_oauth_id(token=token)
                return True

            except jwt.ExpiredSignatureError:
                print("Token has expired")
                return False

            except jwt.InvalidTokenError as e:
                print("Token is invalid, error: ", e)

            except Exception as e:
                print(f"An error occurred: {str(e)}")

        return False

    def get_oauth_id(self, token):

        try:
            # Decode the JWT without validation
            decoded_token = jwt.decode(
                token, options={"verify_signature": False})

            return decoded_token['user']
        except Exception as e:
            print("Error: ", e)

    # This function will return a list with 2 values, first is the latest token secret, and
    # the second latest token secret

    def get_token_secret(self):

        secret_name = f"projects/{self.project_id}/secrets/{self.secret_title}"

        client = secretmanager.SecretManagerServiceClient()

        versions = list(client.list_secret_versions(
            request={"parent": secret_name}))

        sorted_versions = sorted(
            versions, key=lambda x: x.create_time, reverse=True)

        version_list = []

        for version in sorted_versions:
            if version.state == 1:
                if len(version_list) == 0:
                    version_list.append(version.name.split("/")[-1])
                elif len(version_list) == 1:
                    version_list.append(version.name.split("/")[-1])
                    break

        token_secret_list = []

        for version in version_list:
            response = client.access_secret_version(
                request={"name": f"{secret_name}/versions/{version}"})

            secret_data = response.payload.data.decode("UTF-8")

            lines = secret_data.split('\n')

            for line in lines:
                if line.startswith('TOKEN_SECRET='):
                    token_secret_list.append(line[len('TOKEN_SECRET='):])

        return token_secret_list
