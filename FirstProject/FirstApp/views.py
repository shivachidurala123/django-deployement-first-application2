from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
    ss='''
        <h2>Hello user!!</h2>
        <hr/>
        <h2>Welcome to django</h2>
        <hr/>
        <h2>All the best</h2>
        <hr/>
    
    '''
    return HttpResponse(ss);
