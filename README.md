# Rasa Stack

This is AI chatbot based on Rasa Stack.

## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt

```

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```


### Files for training the Rasa NLU model

- **data/nlu_data.json** file contains training examples of six intents: 
	- greet
	- goodbye
	- thanks
	- deny
	- joke
	- name (examples of this intent contain an entity called 'name')
	
- **nlu_cofing.yml** file contains the configuration of the Rasa NLU pipeline:  
```text
language: "en"

pipeline: spacy_sklearn
```	

### Files for training the Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action which retrieves a Chuck Norris joke by making an external API call.
- **endpoints.yml** file contains the webhook configuration for custom action.

## How to use this project?
1. You can train the Rasa NLU model by running:  
```
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose
```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml
```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. Start the server for the custom action by running:  
```
python -m rasa_core_sdk.endpoint --actions actions
```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```
python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --endpoints endpoints.yml --credentials credentials.yml
```  
```
python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --credentials credentials.yml
```
```
ngrok http 5005
```
This will load the assistant in your terminal for you to chat.


## Conversation Examples
### Example 1 of conversation
```
User: Hi bot
Bot: Hey There! Tell me your name!
User: My name is Tatiana
Bot: Nice to meet you Tatiana. How can I help?
User: I want to buy a laptop
Bot: Which brand of laptop fo you want to buy?
User: I have identified MacBook
Bot: Order was placed for MacBook laptop
User: Thank you so much
Bot: My pleasure
User: Bye bot
Bot: Have a nice day Tatiana!
```
