from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def procesar(request):
    #recuperar datos de la página index
    n1=float(request.GET['num1'])
    n2=float(request.GET['num2'])
    ope=request.GET.get('operador')
    res=0
    match ope:
        case '+':
            res= n1+n2
        case '-':
            res= n1-n2
        case 'X':
            res= n1*n2
        case '/':
            if n2==0:
                sw=True
                return render(request, 'app/resultado.html', {'msg':'No se puede dividir entre Cero!','sw':sw})
            else:
                res= n1/n2
        case _:
            res= 0
    return render(request,'app/resultado.html',{'result':res}) 


