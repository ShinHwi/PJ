# from django.shortcuts import render
#
# # Create your views here.
#
# def index(req):
#     return render(req,'index.html')


from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

# Create your views here.


today_day = datetime.today().strftime("%m-%d")


url1 = "http://www.wedarak.net"
image_link = ""

with urlopen('http://www.wedarak.net/shop/rtjournal.asp') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("p.journaltit a"):
        url1004 = anchor.get('href')[26:64]
        url10 = url1+url1004


        if (url10[-5:] == today_day):


            with urlopen(url10) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor1 in soup.select('table p img'):
                    url2 = str(anchor1)[17:]


            indexNo = url2.find("jpg")
            image_link = url1 + url2[:indexNo + 3]


def index(req):
    context = {
        "image_link" : image_link,
    }
    return render(req, "index.html", context=context)