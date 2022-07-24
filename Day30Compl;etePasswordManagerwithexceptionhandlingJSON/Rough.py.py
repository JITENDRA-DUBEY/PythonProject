#jsg Exceptions and handle them
# try:
#   file = open("a.txt")
#   my_dic={"key":"value"}
#   print(my_dic["sdjs"])
# except FileNotFoundError:# here we have to give perticular exception name
#
#     file= open("a.txt","w")
#     print("File not found")
# except KeyError as error_message:
#     print(f"This key is {error_message} not found")
#
# else:
#     print("This else executed ehrn there is no exception occour in try block")
# finally:
#     file.close()
#     print("This is always executed either exception occur or not")
#     # lets raise your own exception
#     raise TypeError("this exception raised by me")

# lets make na bmi with exceptions
heigth= int(input("Height? "))#meters
weight=float(input("Weigth? "))#kg
if heigth>3 or weight> 500:
    raise ValueError("That given heigth and weigth can't be possible for human")
print(round(weight/heigth**2,2))

