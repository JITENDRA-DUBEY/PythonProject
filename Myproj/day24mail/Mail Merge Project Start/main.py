#TODO: Create a letter using starting_letter.txt
#jsg
PLACEHOLDER="[name]"
with open("..\Mail Merge Project Start\input\Letters\starting_letter.txt") as file:
    letter = file.read()
    print(letter)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.

#here we store names list form starting_letter to list name
with open("D:\Programc,c++,java\Python program\day24mail\Mail Merge Project Start\Input\\Names\invited_names.txt") as file:
    list_name=file.readlines()#it return list of lines from the file
    #loop through the whole list_name list
    for i in range(0,len(list_name)):
      list_name[i]=list_name[i].strip()#removing /n from each name
      my_mes=letter.replace(PLACEHOLDER,list_name[i])#here we replace [name ] with actural name from list from the lette
      #for generating new txt files corresponding to each name
      with open(f"./Output/ReadyToSend/letter_for_{list_name[i]}.txt",mode="w") as complet_letter:
           complet_letter.write(my_mes)#add content to in each files
      print(my_mes)
#Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
print("jd")