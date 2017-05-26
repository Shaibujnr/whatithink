from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def home(request):
    if request.method == "GET":
        t = get_template("home.html")
        html = t.render()
        return HttpResponse(html,status=200)
