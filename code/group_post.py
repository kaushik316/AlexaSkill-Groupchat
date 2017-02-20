from flask import Flask 
from flask_ask import Ask, statement, question, session
import json
import requests
from api_keys import *
from random import randint
import logging 


app = Flask(__name__)
ask = Ask(app, "/groupme_reader")
log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def get_messages(limit):
	req = requests.get('https://api.groupme.com/v3/groups/'+ group_id +'/messages?token=' + api_key3 + '&limit=' + limit)
	decoded = json.loads(req.text)
	group_posts = decoded["response"]["messages"]
	messages_to_read = []
	for message in group_posts:
		if message['text'] is not None:
			decoded_msg = message['text'].encode("utf-8")
			speaker = friend_dict[message['user_id']]['name']
			messages_to_read.append(speaker + " says " + decoded_msg)
	messages_to_read = (list(reversed(messages_to_read)))
	print messages_to_read
	return messages_to_read


def make_post(content): # Function to post something in the groupme
	random_guid = str(randint(0,100))
	print random_guid
	poster = {"message": {"source_guid": random_guid, "text": content}}
	r = requests.post("https://api.groupme.com/v3/groups/" + group_id + "/messages?token=" + api_key3,  json = poster)
	print r.text


# use ask to reference flask-ask
@ask.launch
def start_skill():
	welcome_message = "Hello, would you like to read or post messages?"
	return question(welcome_message)


@ask.intent("ReadIntent", default={"messagenumber":"5"})
def read_messages(messagenumber):
	messages = get_messages(messagenumber)
	alexa_msg = "The last {} messages from the group are {}".format(messagenumber, messages)
	return statement(alexa_msg)


@ask.intent("PostIntent", default= {"message": "This is Kash's Echo"})
def no_intent(message):
	make_post(message)
	post = "You said" + message
	return statement(post)


if __name__ == "__main__":
	app.run(debug=True)
