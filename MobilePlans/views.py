from django.shortcuts import render
from .rechargeplans.api import MobileRecharge


# Create your views here.

def index(request):
    obj = MobileRecharge()
    if request.method == 'POST':
        circle = request.POST['circle']
        operator = request.POST['operator']
        plan = request.POST['plan']
        data = obj.get_data(circle=obj.circle[circle], operator=obj.operator[operator], plan=obj.plans[plan])
    else:
        data = obj.get_data()
        circle = 'Andhra Pradesh'
        operator = 'Airtel'
        plan = 'All'
    return render(request, 'MobilePlans/index.html',
                  context={'data': data, 'circle': circle, 'operator': operator, 'plan': plan})
