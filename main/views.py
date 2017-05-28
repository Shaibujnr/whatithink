from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def home(request):
    if request.method == "GET":
        t = get_template("home.html")
        html = t.render()
        return HttpResponse(html,status=200)

def about(request):
    if request.method == "GET":
        t = get_template("about-us.html")
        html = t.render()
        return HttpResponse(html,status=200)

def contact(request):
    if request.method == "GET":
        t = get_template("contact-us.html")
        html = t.render()
        return HttpResponse(html,status=200)

def portfolio(request):
    if request.method == "GET":
        t = get_template('portfolio.html')
        html = t.render()
        return HttpResponse(html,status=200)

def services(request):
    if request.method == "GET":
        t = get_template('services.html')
        html = t.render()
        return HttpResponse(html,status=200)