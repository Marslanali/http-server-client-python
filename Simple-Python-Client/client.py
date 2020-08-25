import requests
url='http://127.0.0.1:8080/'

while True:

    for x in range(100000000000):
        try:
            r = requests.get(url,timeout=3)
            r.raise_for_status()
            print(r)
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:\n",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:\n",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:\n",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else\n",err)


