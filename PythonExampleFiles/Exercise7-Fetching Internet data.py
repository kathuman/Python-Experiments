import urllib.request as urllib2
import json

def main():
    webUrl = urllib2.urlopen("http://joemarini.com")
    
    ## plain Internet data##
    print("result code: " + str(webUrl.getcode()))
    
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()