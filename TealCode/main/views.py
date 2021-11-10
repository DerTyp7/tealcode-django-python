from django.shortcuts import render

def index(req):
    return render(req, "main/index.html")

def topic(req, category, topic):
    return render(req, "main/topic.html")

def category(req, category):
    return render(req, "main/category.html")