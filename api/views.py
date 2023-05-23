from django.http import HttpResponse




def add(request,num1,num2):
    return HttpResponse(num1+num2)

def sub(request,num1,num2):
    return HttpResponse(num1-num2)

def mult(request,num1,num2):
    return HttpResponse(num1*num2)

def div(request,num1,num2):
    if num2 != 0:
        return HttpResponse(num1/num2)
    else:
        return HttpResponse("Can't divide by zero")

