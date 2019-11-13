"""
Created by: Argex
Last update of this file: 13/11/2019
Free code distribution granted 
"""
from time import sleep
import json

from subscriptions import subscriptions
from tracker import tracker
from like import getLiked, like

def main():
	while True:
		try:
			# List of channel IDs
			ids = []
			liked = getLiked()
			channels = subscriptions()
			# Check if videos have been liked during these 10 minutes
			if len(liked) != 0:
				f = open("liked.json", "w")
				f.close()
				# Write them to like.json file
				for like in liked:
					with open("liked.json", "a") as data:
						json.dump(like, data, indent=2)

			# For every subscription
			for channel in channels:
				channel_id = channel.get("id")
				ids.append(channel_id) # Fill the list with the IDs
			# Print all the channels with their relative id
			for channel in channels:
				name = channel.get("name")
				channel_id = channel.get("id")
				print("{}:{}".format(name, channel_id))
			# Start the tracker on the current subscriptions
			tracker(ids)
			print("Sleeping 10 minutes...")
			print("\n", end='')
			
			# Sleep 10 minutes and then repeat the control
			sleep(600)
		except KeyboardInterrupt:
			break
	
if __name__ == "__main__":
	main()
	