from django.shortcuts import render

# Create your views here.
def if_condition(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditions.html',d)
def for_loops(request):
    d={'name':'pravee'}
    return render(request,'loop.html',d)

