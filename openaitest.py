import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email that I will finish the project",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)

