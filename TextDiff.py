import os
from openai import OpenAI

API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

def calculate_difference(string1, string2):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that finds the difference between two paragraphs and outputs what is different about them in a numbered list format. Uses as little text as possible to accomplish this"},
        {"role": "user", "content": "Find the difference between these two pieces of text: \n Text 1:" + string1 + "\n Text 2: " + string2},
        {"role": "user", "content": "Replace the changed to in the output to a /. MAKE SURE you do this"},
    ]
  )
  diff = completion.choices[0].message.content
    
  return diff
  
if __name__ == "__main__":
  
  string1 = "Unfortunately, after much deliberation, I am unable to provide you with a spot on the 2024 Spring Banquet committee. There were a large number of applicants for banquet committee this semester, so please do not feel discouraged. "
  string2 = "Regrettably, after careful consideration, I am unable to offer you a position on the 2024 Spring Banquet committee. There were a high number of applicants for the banquet committee this semester, so please do not be disheartened."
  calculate_difference(string1, string2)