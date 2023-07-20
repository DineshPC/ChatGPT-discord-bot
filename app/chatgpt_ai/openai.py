# import necessary modules
from dotenv import load_dotenv
import openai
import os

# initialize dotenv or load dotenv
load_dotenv()

# getting chatgpt api key token from environment 
openai.api_key = os.getenv('CHATGPT_API_KEY')

# function to get the AI response from GPT-3
def chatgpt_response(prompt):
    response_text = ""  # initialize the response text variable
    response = openai.Completion.create(
        model="text-davinci-003",  # specify the GPT-3 model to use
        prompt=prompt,  # the prompt to send to the model
        temperature=0.8,  # the "creativity" of the response
        max_tokens=20  # the maximum length of the response
    )
    response_choices = response.get("choices")  # get the response choices
    if response_choices and len(response_choices) > 0:
        response_text = response_choices[0]["text"]  # select the first choice
    return response_text  # return the response text
