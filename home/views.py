from django.shortcuts import render
from home.models import BusSystem
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        dt = request.POST["date"]
        die = request.POST["diesel"]
        bus = request.POST["bus"]
        qty = request.POST["qty"]
        num = request.POST["num"]
        result = int(qty) * int(die)
        li = [bus,dt,die,qty,result]
        BusSystem.objects.create(date=dt,diesel=die,bus=bus,qty=qty)
        return render(request, "result.html",{'li': li,'num': range(int(num))})
    else:
        return render(request, "home.html")
