from django.shortcuts import render

# Create your views here.
def looping (request):
    d={'name':'ashu','num':[20,40]}
    return render(request,'looping.html',d)

