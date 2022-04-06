import requests
import json
from bs4 import BeautifulSoup
import os
import shutil

def checkURL(url):
    url_list = url.split("/")
    # print(url_list)
    if len(url_list) > 3:
        user = url_list[-2]
        repo = url_list[-1]
        # print(user)
        # print(repo)

        git_api  = "https://api.github.com/repos/" + user + "/" + repo
        resp = requests.get(git_api)
        resp_json = json.loads(resp.text)
        try:
            if resp_json['private'] == False:
                download_data  = resp_json['clone_url']
                newfolder = input("Please enter a specific folder :- ")
                # newfolder =  os.getcwd() + newfolder 
                # print(newfolder)
                if os.path.exists(newfolder):
                    os.system('rmdir /S /Q "{}"'.format(newfolder))
                try:
                    os.system("git clone " + download_data + " " + newfolder)
                except:
                    print("Unable to copy, Please verify if the directory already exist.")
                # print(download_data)
                # resp1 = requests.get(download_data)
                # print(resp1)
                # print("repo is public and we can access it.")
            else:
                print("repo is private!!")
        except KeyError:
            print("Invalid GIT URL, Please verify ! ")
    else:
            print("Wrong git URL, Please enter correct url . Exiting .. ")



url = input("Please enter a git URL:- ")
if url:
    checkURL(url)
else:
    print("Please input the url to be cloned!!! Exiting...")