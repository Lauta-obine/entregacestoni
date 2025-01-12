from django.shortcuts import render,redirect

from .models import Tractor, Semi, Chofer
from .forms import TractorFormulario, SemiFormulario, ChoferFormulario


# Create your views here.

def index (request):
    return render (request,"index.html")

def tractores(request):
    
    
    
    tractores=Tractor.objects.all()


    contexto={"tractores": tractores}
    


    return render(request,"tractores.html", contexto)

def tractor_formulario(request):
    print(f"metodo: {request.method}")
    if request.method=='POST':
        form=TractorFormulario(request.POST)
        print(f"patente: {form['patente'].value()}")
        print(f"marca: {form['marca'].value()}")
        print(f"ano: {form['ano'].value()}")
        if form.is_valid():
            print("El formulario es valido")
            print(f"patente: {form.cleaned_data['patente']}")
            print(f"marca: {form.cleaned_data['marca']}")
            print(f"ano: {form.cleaned_data['ano']}")

            tractor=Tractor(patente=form.cleaned_data['patente'], marca=form.cleaned_data['marca'], ano=form.cleaned_data['ano'])

            tractor.save()
            return redirect ('tractores')


    form= TractorFormulario()
    return render(request, 'tractor_formulario.html', {'form': form})

def buscar_tractor(request):
    query = request.GET.get('busquedatmarca', '') 
    mtractores= Tractor.objects.filter(marca__icontains=query) 
    
    return render(request, 'buscar_tractor.html', {'tractores': mtractores, 'query': query})

def semis(request):
    
    
    
    semis=Semi.objects.all()


    contexto={"semis": semis}
    
    return render(request,"semis.html", contexto)

def semi_formulario(request):
    print(f"metodo: {request.method}")
    if request.method=='POST':
        form=SemiFormulario(request.POST)
        print(f"patente: {form['patente'].value()}")
        print(f"marca: {form['marca'].value()}")
        print(f"tipo: {form['tipo'].value()}")
        print(f"ano: {form['ano'].value()}")
        if form.is_valid():
            print("El formulario es valido")
            print(f"patente: {form.cleaned_data['patente']}")
            print(f"marca: {form.cleaned_data['marca']}")
            print(f"tipo: {form.cleaned_data['tipo']}")
            print(f"ano: {form.cleaned_data['ano']}")

            semi=Semi(patente=form.cleaned_data['patente'], marca=form.cleaned_data['marca'], tipo=form.cleaned_data['tipo'], ano=form.cleaned_data['ano'])

            semi.save()
            return redirect ('semis')


    form= SemiFormulario()
    return render(request, 'semi_formulario.html', {'form': form})

def buscar_semi(request):
    query = request.GET.get('busquedastipo', '') 
    tsemis= Semi.objects.filter(tipo__icontains=query) 
    
    return render(request, 'buscar_semi.html', {'semis': tsemis, 'query': query})

def choferes(request):
      
    choferes=Chofer.objects.all()

    contexto={"choferes": choferes}
    
    return render(request,"choferes.html", contexto)

def chofer_formulario(request):
    print(f"metodo: {request.method}")
    if request.method=='POST':
        form=ChoferFormulario(request.POST)
        print(f"dni: {form['dni'].value()}")
        print(f"nombre: {form['nombre'].value()}")
       
        if form.is_valid():
            print("El formulario es valido")
            print(f"dni: {form.cleaned_data['dni']}")
            print(f"nombre: {form.cleaned_data['nombre']}")
           

            chofer=Chofer(dni=form.cleaned_data['dni'], nombre=form.cleaned_data['nombre'])

            chofer.save()
            return redirect ('choferes')


    form= ChoferFormulario()
    return render(request, 'chofer_formulario.html', {'form': form})