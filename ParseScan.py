import requests
import sys
import getopt

def parsescan(argv):

    serverURL = ""
    applicationID = ""
    
    try:
        (opts, args) = getopt.getopt(argv, 'u:i:')
    except getopt.GetoptError:
        print('parsescan.py -u <url> -i <Application ID>')
        sys.exit(2)
    for (opt, arg) in opts:
        if opt == '-h':
            print('parsescan.py -u <url> -i <Application ID>')
            sys.exit()
        elif opt in '-u':
            serverURL = arg
        elif opt in '-i':
            applicationID = arg
            
    headers = {
       'X-Parse-Application-Id': applicationID
   }
    if serverURL[-1] != "/":
        serverURL = serverURL + "/"
    response = requests.get(serverURL+"parse/users/",headers=headers)
    if (response.text).find("results") != -1:
        print(serverURL + " is vulnerable to anonymous class read. Checking for anonymous file upload...")
    else:
        print(serverURL + " is NOT vulnerable to anonymous class read. Checking for anonymous file upload...")
    data = "test"
    response = requests.post(serverURL+"parse/files/test.txt",headers=headers, data=data)
    if (response.text).find("url") != -1:
        print(serverURL + " is vulnerable to anonymous file upload.")
    else:
        print(serverURL + " is NOT vulnerable to anonymous file upload.")
if __name__ == '__main__':
    parsescan(sys.argv[1:])

