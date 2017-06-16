from django.http import HttpResponse
from django.template.loader import get_template
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render
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
    form_class = ContactForm()
    if request.method == "GET":
        return render(request,"contact-us.html",{"form":form_class},status=200)
    if request.method == "POST":
        #contact form submitted
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            template = get_template('contact_tmp.txt')
            content = template.render({'contact_name':contact_name,
                                    'contact_email':contact_email,
                                    'message':message})
            send_mail(subject,content,'no-reply@shaibu.me',['s.shaibu.jnr@gmail.com'])
            response = redirect('/thankyou/')
            response.set_cookie('contact_me',contact_name)
            return response



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

def thankyou(request):
    if request.method == "GET":
        if 'contact_me' in request.COOKIES:
            contact_name = request.COOKIES.get('contact_me')
            t = get_template('thank.html')
            html = t.render({'name': contact_name})
            response = HttpResponse(html,status=200)
            response.delete_cookie('contact_me')
            return response
        else:
            return redirect('/')
