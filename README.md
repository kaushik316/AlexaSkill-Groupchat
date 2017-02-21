# AlexaSkill-Groupchat
A skill created for Amazon's Alexa system to read and post messages into your GroupMe

### Features
The skill allows you to read the last few messages from a groupchat or post a message that you dictate to Alexa into the chat. You can also tell Alexa how many messages from the chat you want her to read. 

### Setup and Deployment
Your api_keys file should look something like this:
```python
api_key = "123abc"
group_id = 12345678
```
You'll receive this information when you create an account and register your bot on the GroupMe developer [portal] (https://dev.groupme.com/). 

The schema.json file includes the configuration setup for the skill, which can be copied and pasted into the model setup page in the Alexa developer portal. Deployment of the skill can be performed with [zappa](https://github.com/Miserlou/Zappa)

### Usage
See sample_utterances.txt. The Alexa schema allows for custom slots - i.e variables (message and messagenumber in this case) that can be 
changed each time you invoke the skill. 

E.g 
```
# Launch skill
"Alexa, start groupchat"

# messagenumber 
"Alexa, tell groupchat to read the last 5 messages" 
Returns "The last 5 messages are..."

# message 
"Alexa, tell groupchat to post 'Where should I eat?'"
returns "You said..."
```



