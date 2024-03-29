def difference(string1, string2):
  # Split both strings into list items
  string1 = string1.split()
  string2 = string2.split()

  # A = set(string1) # Store all string1 list items in set A
  # B = set(string2) # Store all string2 list items in set B
 
  # str_diff = A.symmetric_difference(B)
  
  # iterate through the string to find the result
  if len(string1) < len(string2):
    iterate = len(string1)
  else:
    iterate = len(string2)
  
  diff = []
  changes = ""
  
  for i in range(iterate):
    # start pointer at both strings
    if string1[i] != string2[i]:
      changes += string2[i] + " "
    else:
      if changes != "":
        diff.append(changes)
        changes = ""
    
  print(diff)
  
if __name__ == "__main__":
  
  string1 = "Unfortunately, after much deliberation, I am unable to provide you with a spot on the 2024 Spring Banquet committee. There were a large number of applicants for banquet committee this semester, so please do not feel discouraged. "
  string2 = "Regrettably, after careful consideration, I am unable to offer you a position on the 2024 Spring Banquet committee. There were a high number of applicants for the banquet committee this semester, so please do not be disheartened."
  difference(string1, string2)