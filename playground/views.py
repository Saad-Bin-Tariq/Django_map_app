from django.shortcuts import render

from django.http import HttpResponse
x=1
def say_hello(request):
    return render(request, 'hello.html', {'name':'Pak'})

def hi(request):
    return HttpResponse('second pg')
