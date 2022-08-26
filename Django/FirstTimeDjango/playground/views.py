from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hell_world(request):
    #return HttpResponse("Hello world")
    return render(request, 'hello.html', {'name': 'Abel'})