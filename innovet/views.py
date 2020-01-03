from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def blood(request):
    return render(request,'blooddonation.html')
def gallary(request):
    return render(request,'gallary.html')
def money(request):
    return render(request,'Moneydonation1.html')
def payment(request):
    return render(request,'payment.html')
def contact(request):
    return render(request,'contact.html')