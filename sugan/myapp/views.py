
from django.shortcuts import render

def calculate_rate(request):
    
    lost=float(request.POST.get("CustLost",'0'))
    init=float(request.POST.get("InitCust",'0'))
    ChurnRate = ((lost)*100)/init if request.method == 'POST' else 0
    print(f"Initial Customer: {init}numbers \n Lost Customer: {lost}numbers \n Churn Rate: {ChurnRate}")
    return render(request, "myapp/math.html",{"init": init, "lost": lost, "ChurnRate": ChurnRate})