import pickle

from os import path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import googleapiclient.errors

CLIENT_SECRETS = None
if not path.exists("token.pickle"):
    CLIENT_SECRETS = input("Insert the path of your client secret file: ")

def creds(scopes):
    credentials = None
    youtube = None
    try:
        # If token file already exists
        if path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                credentials = pickle.load(token)
        # Otherwise it must be created
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                credentials = CLIENT_SECRETS

                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials, scopes)
                credentials = flow.run_local_server(port=0)

                # Write credentials to the token file
                with open("token.pickle", "wb") as token:
                    pickle.dump(credentials, token)
        #Build API Client
        youtube = build('youtube', 'v3', credentials=credentials)

    except googleapiclient.errors.Error as err:
        print(err)
    finally:
        #Return the API Client built
        return youtube

if __name__ == "__main__":
    print("This is a private module which cannot be run directly")