# from django.shortcuts import render
from django.shortcuts import redirect, render
import requests
import http.client
import random
import json


def view_list(request):
    fact = getfact()
    print(fact)
    return render(request, 'home.html', {'user': fact})


def getfact():
    RndPage = random.randint(1, 626)
    conn = http.client.HTTPConnection("www.catfact.info")
    StrRequest = "/api/v1/facts.json?page=" + str(RndPage) + "&per_page=1"
    conn.request("GET", StrRequest)
    r1 = conn.getresponse()
    print(r1.status)
    data1 = r1.read()

    dict = json.loads(data1)
    dict2 = dict['facts']
    dict3 = dict2[0]
    responsedict = dict3['details']

    conn.close()
    return responsedict
