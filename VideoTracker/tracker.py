from os import path, system
from traceback import print_exc
from itertools import zip_longest
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from creds import creds

def tracker(ids):
    try:
        # Raise an exception if the argument is not of list type
        if not isinstance(ids, list):
            raise TypeError("The argument must be a list of channel ids")
        # Dict with my subscriptions and the number of videos of those channels 
        subscriptions = {
            "channels": [],
            "number_of_videos": []
        }
        # Set the necessary scopes for performing the task
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        # Get credentials and create an API client
        youtube = creds(scopes)
        # For every id in the IDs list
        for id in list(ids):
            # Set a request for that channel
            request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=id
            )
            response = request.execute()
            # For every channel in the response
            for channel in response.get("items"):
                # Update channels and number of videos keys in the dict
                subscriptions["channels"].append(channel.get("snippet").get("title"))
                subscriptions["number_of_videos"].append(channel.get("statistics").get("videoCount"))
        # If subscriptions.json does not exist
        if not path.exists("subscriptions.json"):
            with open("subscriptions.json", "w") as data:
                json.dump(subscriptions, data)
        # Otherwise if it exists
        else:
            # Read its content and convert it to a dict
            with open("subscriptions.json", "r") as data:
                content = json.load(data)
                channels = content.get("channels")
                number_of_videos = content.get("number_of_videos")
            
            for fchannel, fnumber, channel, number in zip_longest(
                    channels,
                    number_of_videos,
                    subscriptions.get("channels"),
                    subscriptions.get("number_of_videos")
            ):
                # Update the json file if it's necessary
                if fchannel == channel and fnumber != number:
                    system('echo "New video posted by ' + channel + '"')
                elif fchannel != channel and channel != None:
                    system('echo "New channel added: ' + channel + '"')
                    with open("subscriptions.json", "w") as data:
                        json.dump(subscriptions, data)   
    except TypeError:
        print_exc()
    except googleapiclient.errors.Error as err:
        print(err)
    except Exception:
        print_exc()

if __name__ == "__main__":
	print("This is a private module which cannot be run directly")