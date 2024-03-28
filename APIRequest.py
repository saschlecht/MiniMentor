import os
API_KEY = os.environ.get('OPENAI_API_KEY')
from openai import OpenAI
client = OpenAI(api_key = API_KEY)

def APIRequest(content):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a friendly and helpful professional assistant. You take paragraphs as inputs and change a few words to make the input sound more professional."},
      {"role": "user", "content": content},
    ]
  )
  print("\n")
  return completion.choices[0].message.content
  
# find the difference in the text of the input and output, return a vector of those differences 
def textDiff(str1, str2):
  print("hello") # not functional yet 


if __name__ == "__main__":
  
  while True:
    content = input("Enter a paragraph you need help revising! (enter q to quit) \n")
    
    if content == "q":
      break
    
    # get the output of the second string 
    output = APIRequest(content)
    print(output + "\n")
    
    difference = textDiff(content, output)
    
    print(difference)
    

  
  
  
