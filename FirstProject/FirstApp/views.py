from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
    ss='''
        <h2>This is the sample view</h2>
        <hr/>
    
    '''
    return HttpResponse(ss);
