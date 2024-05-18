alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
h=1
print(logo)
# Direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# Text = input("Type your message:\n").lower()
# Shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(direction, text, shift):
  Encoded=''
  n=len(text)
  New_text=[]
  for i in range(n):
    if text[i] not in alphabet:
      New_text.insert(i, text[i])
    else:  
      p=alphabet.index(text[i])
      if direction=="encode":
        np=p+shift
        word="encoded"
      elif direction=="decode":
        np=p-shift
        word="decoded"
      if np>25 and np<51:
        INDEX=np-26
      elif np>51:
        INDEX=np-52
      elif np<-25:
        INDEX=np+26      
      else:
        INDEX=np
      New_text.insert(i, alphabet[INDEX])     
  for i in range(n):
    Encoded+=New_text[i]
  print(f"The {word} text is {Encoded}")
while h==1:
  Direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  Text = input("Type your message:\n").lower()
  Shift = int(input("Type the shift number:\n"))
  
  caesar(Direction, Text, Shift)
  response=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if response=="yes":
    continue
  else:
    print("Goodbye sweetheart, thank you for your time")
    h-=1
  


#COMPLETED THIS ENTIRE THING ON MY OWN,FELT GREAT
#THIS IS THE COMPLETED VERSION OF THE ENCODER/DECODER CODE

