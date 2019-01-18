import urllib.request
import sys
import getpass
from html.parser import HTMLParser
from amazonloginparser import AmazonLoginParser


''' Test basics of doing MTurk via python '''
def test_mturk():
    #login='jacobmas@gmail.com'
    #password=getpass.getpass()
    #print('{0},{1}'.format(login,password))
    req=urllib.request.Request(url='https://worker.mturk.com/',data=None)
    with urllib.request.urlopen(req) as f:
        try_stuff(f)

def try_stuff(f):
    x=f.read().decode('utf-8')
   # print(type(x.toString()))
    parser=AmazonLoginParser()
    parser.feed(x)


                                   




if __name__ == "__main__":
    import sys
    test_mturk()
