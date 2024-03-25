import os
API_KEY = os.environ.get('OPENAI_API_KEY')
from openai import OpenAI
client = OpenAI(api_key = API_KEY)

while True:
  content = input()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": content},
    ]
  )

  print(completion.choices[0].message)
