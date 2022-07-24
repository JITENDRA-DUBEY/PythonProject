#jsg
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
char_list=[random.choice(letters) for _ in range(2,random.randint(4,8))]
print (char_list)
num_list=[random.choice(numbers) for _ in range(2,random.randint(3,7))]
print(num_list)
symbool_list=[random.choice(symbols) for _  in range(2,random.randint(3,5))]
print(symbool_list)
password_list=char_list+num_list+symbool_list
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print(password)
#using list comprehenssion generate a random pass

