import re
text = input()
pattern = r'\b\w+\.\b'
found_words = re.findall(text,pattern)
for word in found_words:
  print(word)
