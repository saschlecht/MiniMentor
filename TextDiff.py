import os
from openai import OpenAI

API_KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

def calculate_difference(string1, string2):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that finds the difference between two paragraphs and outputs what is different about them in a list format. example: 'word1 / word2.'"},
        {"role": "user", "content": "Find the difference between these two pieces of text, and output only the changed words and phrases in the format 'word1 / word2'. MAKE SURE it is in that format every single time, or else i will be mad: \n Paragraph 1:" + string1 + "\n Paragraph 2: " + string2},
    ]
  )
  diff = completion.choices[0].message.content
  
  # trim the data and put into a list 
  # split by new line
  trimData = diff.split('\n')
  outputString = ""
  
  for i in range(len(trimData)):
    outputString += trimData[i][trimData[i].index("/") + 2:] + "****"
  
  print(outputString)
  return outputString
  