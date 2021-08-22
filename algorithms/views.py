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

def addition1(n):
    temp = 0
    for i in str(n):
        temp = temp + int(i)
    return temp
    # return addition(temp)

# Create your views here.
@csrf_exempt
def homepage(request):
    return render(request,"algorithms/home.html")

@csrf_exempt
def take_data(request):
    print(request.POST)
    date_of_birth = request.POST.get('birth_date')
    a = date_of_birth.split('-')
    print(a)
    strings = [str(integer) for integer in a]
    a_string = "".join(strings)
    an_integer = a_string
    conductor = addition(an_integer)
    driver = addition(int(a[-1]))

    if request.POST.get('gender')=='Male':
        kua = 11-addition(int(a[0]))
        kua = addition(kua)
    else:
        kua = 4+addition(int(a[0]))
        kua = addition(kua)


    if request.POST.get('mobile1') and request.POST.get('mobile2'):
        d = [request.POST.get('mobile1'),request.POST.get('mobile2')]
        print(d)
        daa = {}
        for i in range(0,2):
            mob_add = addition(d[i])
            daa['mob'+str(i)] = mob_add
            # mob_two_dig = addition1(d[i])
            daa['mob_two'+str(i)] = addition1(d[i])
        dd = {"name":request.POST.get('name'),"birth_date":request.POST.get('birth_date'),"gender":request.POST.get('gender'),"driver":driver,"cund":conductor,"kuber":kua,'mob1':daa['mob0'],'mob2':daa['mob1'],"num1":request.POST.get('mobile1'),"num2":request.POST.get('mobile2'),"two_mob1":daa['mob_two0'],"two_mob2":daa['mob_two1']}

    else:
        daa = {}
        mob_add = addition(request.POST.get('mobile1'))
        daa['mob'+str(1)] = mob_add
        daa['mob_two'+str(1)] = addition1(request.POST.get('mobile1'))
        dd = {"name":request.POST.get('name'),"birth_date":request.POST.get('birth_date'),"gender":request.POST.get('gender'),"driver":driver,"cund":conductor,"kuber":kua,'mob1':daa['mob1'],"num1":request.POST.get('mobile1'),"two_mob1":daa['mob_two1']}
    print(dd)
    
    return render(request,"algorithms/data.html",{"data":dd})