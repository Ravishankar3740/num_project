from django.shortcuts import render,render
from django.views.decorators.csrf import csrf_exempt

def addition(n):
    if len(str(n))==1:
        return n
    else:
        temp = 0
        for i in str(n):
            temp = temp + int(i)
        return addition(temp)


# Create your views here.
@csrf_exempt
def homepage(request):
    return render(request,"algorithms/home.html")

@csrf_exempt
def take_data(request):
    print(request.POST)
    date_of_birth = request.POST.get('birth_date')
    a = date_of_birth.split('-')
    strings = [str(integer) for integer in a]
    a_string = "".join(strings)
    an_integer = a_string
    total = addition(an_integer)
    d = addition(int(a[0]))
    if request.POST.get('gender')=='Male':
        c = 11-addition(int(a[1]))
    else:
        c = 4+addition(int(a[1]))
    k = addition(int(a[-1]))
    dd = {"name":request.POST.get('name'),"birth_date":request.POST.get('birth_date'),"gender":request.POST.get('gender'),"total":total,"driver":d,"cund":c,"kuber":k}
    return render(request,"algorithms/data.html",{"data":dd})