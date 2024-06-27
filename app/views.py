from django.shortcuts import render

# Create your views here.
def sinchan(request):
    d={'name':'chandu','age':13}
    return render(request,'sinchan.html',context=d)