import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from creds import creds

def getLiked():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    youtube = creds(scopes)
    likes = []

    try:
        request = youtube.channels().list(
            part='contentDetails',
            mine=True
        )
        response = request.execute()

        for item in response.get("items"):
            likes_id = item.get("contentDetails").get("relatedPlaylists").get("likes")
        
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=likes_id
        )
        response = request.execute()

        if len(response.get("items")) != 0:
            for item in response.get("items"):
                title = item.get("snippet").get("title")
                video_id = item.get("snippet").get("resourceId").get("videoId")
                likes.append(
                    {
                        "title": title,
                        "id": video_id
                    }
                )
    except googleapiclient.errors.Error as err:
        print(err)
    finally:
        return likes

    return likes

def like(time=60):
    scopes = ["https://www.googleapis.com/auth/youtube"]
    youtube = creds(scopes)
    """
    This function is scheduled to be implemented
    It will like the video you are currently watching after a certain amount of time
    The default value for the time parameter is: 60 seconds
    """

if __name__ == "__main__":
    likes = getLiked()
    print(likes)