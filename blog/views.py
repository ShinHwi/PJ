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

link_eng = "http://www.wedarak.net/shop/rtjournal_e.asp"

link_jp = "http://www.wedarak.net/shop/rtjournal_j.asp"

link_cn = "http://www.wedarak.net/shop/rtjournal_c.asp"

linkarr = [link_eng, link_jp, link_cn]

total_arr = []

image_link = ""
image_link_eng = ""
image_link_jp = ""
image_link_cn = ""

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



for i in range(3):
    with urlopen(linkarr[i]) as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.select("p.journaltit a"):
            url1004 = anchor.get('href')[26:66]


            url10 = url1 + url1004

            if (url10[-5:] == today_day):


                with urlopen(url10) as response:
                    soup = BeautifulSoup(response, 'html.parser')
                    for anchor1 in soup.select('table p img'):
                        url2 = str(anchor1)[17:]


                indexNo = url2.find("jpg")

                url3 = url1 + url2[:indexNo + 3]
                total_arr.append(url3)

image_link_eng = total_arr[0]
image_link_jp = total_arr[1]
image_link_cn = total_arr[2]

def index(req):
    context = {
        "image_link" : image_link,
    }
    return render(req, "index.html", context=context)

def english(req):
    context = {
        "image_link_eng" : image_link_eng,
    }
    return render(req, "english.html", context=context)

def japanese(req):
    context = {
        "image_link_jp" : image_link_jp,
    }
    return render(req, "japanese.html", context=context)

def chinese(req):
    context = {
        "image_link_cn" : image_link_cn,
    }
    return render(req, "chinese.html", context=context)