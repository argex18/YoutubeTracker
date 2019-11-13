import os
from traceback import print_exc

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from creds import creds

def subscriptions():
    subs = []
    try:
        # Set the necessary scopes for performing the task
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        # Get credentials and create an API client
        youtube = creds(scopes)
        # Return a list of all my subscriptions
        request = youtube.subscriptions().list(
            part='snippet,contentDetails',
            mine=True
        )
        response = request.execute()
        # For every subscription
        for channel in response.get("items"):
            title = channel.get("snippet").get("title")
            channel_id = channel.get("snippet").get("resourceId").get("channelId")
            # Append a dictionary with name and id of the subscription to the list
            subs.append(
                {
                    "name": title,
                    "id": channel_id
                }
            )
    except googleapiclient.errors.Error as err:
        print_exc()
    finally:
        return subs

if __name__ == "__main__":
    for channel in subscriptions():
        name = channel.get("name")
        channel_id = channel.get("id")
        print("{}:{}".format(name, channel_id))