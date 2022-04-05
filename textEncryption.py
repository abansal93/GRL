import base64
import os
import binascii

def encode_string():
    data = input("Please enter the text for encryption:- ")
    if not data:
        print("\n\nExiting !!! .. Please enter a string for encryption!!")
        exit()

    reverse_data = data[::-1]
    encoded_string = reverse_data.encode("ascii")
    base64_encoded = base64.b64encode(encoded_string)

    try:
        with open("output.txt", 'wb' ) as Wfile:
            Wfile.write(base64_encoded)
    except:
        print("Error in encryption .. Exiting")
    else:
        print("\n\nFile encoded successfully. output.txt .")


def decode_file():
    file = input("Please enter the file name:-")
    if os.path.exists(file):
        with open (file,'rb') as FR:
            data = FR.read()
        # print(data.decode('ascii'))
        try:
            base64decodedata = base64.b64decode(data)
            print(base64decodedata.decode('ascii')[::-1])
        except binascii.Error as err:
            print("\n\nError in file content, Please validate the file")
    else:
        print("\n\nFile does not exist. Please retry . Exiting .. ")
        exit()


## take an input from CLI

print("Welcome to encode/decode CLI . Please select your option. 1 or 2 !!")
print("1. Encode a string")
print("2. Decode a File")
try:
    option = int(input("Please enter 1 or 2:- "))
except ValueError:
    print("\n\nInvalid entry, Please retry!")
    exit()
if option == 1 or option == 2:
    if option == 1:
        encode_string()
    else:
        decode_file()
else:
    print("\n\nWrong option selected. Please select 1 or 2. Exiting...")


