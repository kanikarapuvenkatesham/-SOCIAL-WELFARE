from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'About.html')
def team(request):
    return render(request,'department.html')   
def blood(request):
    return render(request,'blooddonation.html')
def gallery(request):
    return render(request,'gallary.html')
def money(request):
    return render(request,'Moneydonation1.html')
def payment(request):
    return render(request,'payment.html')
def contact(request):
    return render(request,'contact.html')