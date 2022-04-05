import sys
import json
import os
import yaml
import requests



if __name__ == '__main__':

## check if the file was added as a parameter  or not.  
# if not then take an input from user

    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            print(f"Please enter a valid file name as script parameter. \n{os.path.basename(sys.argv[0])} fileName")
            print("Or Run the script independently and add the file name on the go.")
            exit()
        fileName = sys.argv[1]
    else:
        fileName = input("Please enter the file name:- ")


    #####check if the file extemsion is correct or not

    if not fileName.lower().endswith('.json'):
        print("Please enter the correct file name. Exiting ...")
        exit()
    else:
        if os.path.exists(fileName):
            try:
                FH = open(fileName,'r')
                data = json.load(FH)
            # print(type(data))
                for key,value in data.items():                
                    resp = requests.get('http://validate.jsontest.com/?json={%22key%22:%22value%22}')
                    if json.loads(resp.text)['validate'] == False:
                        print("File is not Json , Please validate the file")
                        break
                ### dunp the content as YAML     
                print(yaml.dump(data))
            except json.decoder.JSONDecodeError:
                print("File is not a json file")
            else:
                FH.close()
        else:
            print("File does not exist. Please check and run again")
