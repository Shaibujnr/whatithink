from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.

def home(request):
    if request.method == 'GET':
        test_var = os.environ["MY_TEST_VARIABLE"] if "MY_TEST_VARIABLE" in os.environ else "Development mode"
        http = "Welcome to HOME page and the test variable is %s" % test_var
        return HttpResponse(http, status=200)
