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
        result = int(qty) * int(die)
        li = [bus,dt,die,qty,result]
        num = request.POST["num"]
        BusSystem.objects.create(date=dt,diesel=die,bus=bus,qty=qty)
        if num == '':
            return render(request, "result.html",{'li': li,'num': range(1)})
        else:    
        	return render(request, "result.html",{'li': li,'num': range(int(num))})
    else:
        return render(request, "home.html")
