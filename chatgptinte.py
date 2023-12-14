
from openai import OpenAI

client = OpenAI(api_key = 'Your API key')

user_prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": user_prompt}
  ]
)
print(response.choices[0].message.content)





