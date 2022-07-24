#TODO: Create a letter using starting_letter.txt
#jsg
PLACEHOLDER="[name]"
with open("..\Mail Merge Project Start\input\Letters\starting_letter.txt") as file:
    letter = file.read()
    print(letter)
    print("my")
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
letters=[]
#here first we have to create a letters list which have total letter as many invited student are given in list
with open("D:\Programc,c++,java\Python program\day24mail\Mail Merge Project Start\Input\\Names\invited_names.txt") as file:
    list_name=file.readlines()#it return list of lines from the file
    for i in range(0,len(list_name)):
      letters[i]=letters[i].strip("\n")
      with open("..\Mail Merge Project Start\input\Letters\starting_letter.txt") as file:
            letters.append(file.read())
      letters[i]=letters[i].replace(PLACEHOLDER,list_name[i])#return a string with changes so that we have to again modified our list
      print(letters[i])
#Save the letters in the folder "ReadyToSend".
with open("..\\Mail Merge Project Start\Output\ReadyToSend\example.txt",mode="a") as file:
      for letter in letters:
        file.write(letter+"\n")
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
print("jd")