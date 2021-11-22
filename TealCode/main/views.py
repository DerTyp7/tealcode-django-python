from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Topic
from analytics.models import View

def index(req):
    view = View(ip=get_client_ip(req), home=True)
    view.save()
    categorys_obj = Category.objects.all()
    return render(req, "main/index.html", {'categorys': categorys_obj})

def topic(req, category, topic):

    if topic and category:
        category_obj = Category.objects.filter(title = category).first()
        if category_obj:
            topic_obj = Topic.objects.filter(title=topic, category = category_obj).first()
            previous_obj = Topic.objects.filter(id = topic_obj.id-1, category = category_obj).first()
            next_obj = Topic.objects.filter(id = topic_obj.id+1, category = category_obj).first()

            if topic_obj:
                context = {
                    'title': topic_obj.title,
                    'code': topic_obj.code_text,
                    'category_title': category_obj.title,
                    'version': topic_obj.version,
                    'previous': previous_obj,
                    'next': next_obj,
                    'output': topic_obj.output,
                    'current': category_obj.title,
                    'helpful_count': 2,
                    'notHelpful_count': 2,
                }


                view = View(ip=get_client_ip(req), topic=topic_obj)
                view.save()
                return render(req, "main/topic.html", context)

    return redirect("main-index")

    

def category(req, category):
    
    if category:
        category_obj = Category.objects.filter(title = category).first()
        if category_obj:
            topics_obj = Topic.objects.filter(category=category_obj)

            view = View(ip=get_client_ip(req), category=category_obj)
            view.save()

            context = {
                'category_obj': category_obj,
                'topics': topics_obj,
                'current': category_obj.title,
                'title': category_obj.display_name,
            }

            return render(req, "main/category.html", context)
        
    
    return redirect("main-index")


def search(req, value): # https://django-taggit.readthedocs.io/en/latest/getting_started.html        
    
    return HttpResponse("<h1>moin</h1>")




def sitemap(req):
    topics = Topic.objects.all()
    categories = Category.objects.all()
    #REPLACE ALL BLANKS WITH %20


    context = {
        'topics': topics,
        'categories': categories
    }
    return render(req, 'sitemap.xml', context, 'text/xml')

def about(req):
    return render(req, "main/about.html", {'current': 'about'})


def privacy(req):
    return render(req, "main/privacy.html", {'current': 'privacy'})

def rating(req, topic, is_positive):
    return HttpResponse("<h1>HALLO</h1>")

def get_client_ip(req):
    x_forwarded_for = req.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split[","][0]
    else:
        ip = req.META.get("REMOTE_ADDR")
    return ip
