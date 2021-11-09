from django.shortcuts import render

def index(req):
    return render(req, "main/index.html")

def list(req):
    return render(req, "main/list.html")