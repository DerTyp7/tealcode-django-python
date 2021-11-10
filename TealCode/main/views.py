from django.shortcuts import render, redirect
from .models import Category, Topic

def index(req):
    return render(req, "main/index.html")

def topic(req, category, topic):

    if topic and category:
        category_obj = Category.objects.filter(title = category).first()
        if category_obj:
            topic_obj = Topic.objects.filter(title=topic, category = category_obj).first()
            if topic_obj:
                context = {
                    'title': topic_obj.title,
                    'code': topic_obj.code_text,
                    'category_title': category_obj.title,
                }

                return render(req, "main/topic.html", context)

    return redirect("main-index")

    

def category(req, category):
    
    if category:
        category_obj = Category.objects.filter(title = category).first()
        if category_obj:
            return render(req, "main/category.html", {'category_obj': category_obj})
        
    
    return redirect("main-index")


