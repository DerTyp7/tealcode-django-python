from django.shortcuts import redirect, render

from .forms import EntryForm

def index(req):    
    if req.method == "POST":
        form = EntryForm(req.POST)
        if form.is_valid:
            entry = form.save()
            entry.ip = ip=get_ip(req)
            entry.save()
            form = False
    else:
        form = EntryForm()

    context = {
            'current': 'contact',
            'form': form,
        }
    return render(req, "contact/index.html", context)


def get_ip(req):
    ip = req.META.get('HTTP_X_REAL_IP') 
    if ip is None:
        return "x.x.x.x"
    else:
        # We got the client's IP address
        return ip
    