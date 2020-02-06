from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from splash.models import Signature

import secrets
import os
import requests
import json

def home(request):
    context = {'n' : 18324, 'signatures':[
        {'name':'News T. Boomer', 'department':"Department of The Built Environment", "level":"Undergraduate Student"},
        {'name':'Irish O\'Texan', 'department':"Psychology", "level":"Postgraduate Student"},
        {'name':'Beniamino Green', 'department':"Department of Political Science", "level":"Undergraduate Student"}
        ]}
    return render(request, 'splash/strike_splash.html', context)

def login(request):
    state = secrets.token_urlsafe(20)
    request.session["state"] = state
    client_id=os.environ.get("UCL_OAUTH_ID")

    url = f"https://uclapi.com/oauth/authorise/?client_id={client_id}&state={state}"
    return redirect(url)

def callback(request):
    try:
        result = request.GET.get("result")
    except KeyError:
        return JsonResponse({
            "error": "No result parameter passed."
        })

    if result == "allowed":
        return allowed(request)
    elif result == "denied":
        return denied(request)

def allowed(request):
    code = request.GET.get("code")
    params = {
            'client_id':os.environ.get('UCL_OAUTH_ID'),
            'code': code,
            'client_secret': os.environ.get("UCL_OAUTH_SECRET")
        }

    r = requests.get("https://uclapi.com/oauth/authorise/oauth/token", params=params)
    token_response = r.json()

    params = {'token': token_response["token"],
            'client_secret': os.environ.get("UCL_OAUTH_SECRET")}

    r = requests.get("https://uclapi.com/oauth/user/data",params=params)
    sig_data=r.json()
    signature = Signature(id_hash= hash(sig_data["cn"]),
            department = "POLISCI",
            level = "UG")
    return JsonResponse(r.json())

def denied(request):
    return render(request, 'splash/strike_not_authorised.html')

def test_token(request):
    pass
