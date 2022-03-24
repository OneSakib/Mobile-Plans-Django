from django.shortcuts import render
from .rechargeplans.api import MobileRecharge


# Create your views here.

def index(request):
    obj = MobileRecharge()
    if request.method == 'POST':
        circle = request.POST['circle']
        operator = request.POST['operator']
        plan = request.POST['plan']
        if plan == '--ALL--':
            plan = ''
        data = obj.get_data(circle=circle, operator=operator, plan=plan)
    else:
        data = obj.get_data()
        circle='andhra-pradesh'
        operator='airtel'
        plan='all'
    return render(request, 'MobilePlans/index.html', context={'data': data,'circle':circle,'operator':operator,'plan':plan})
