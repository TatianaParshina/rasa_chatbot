## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 
## story_joke_01
* joke
 - action_joke
 
## story_short_product
* order_product
 - utter_ask_product_name
* order_product[product=router]
 - utter_ask_model_name
* order_product[model=123]
 - slot{"model": "123"}
 - action_order_product
* thanks
 - utter_thanks 