from django.shortcuts import render
from .models import Socio
from .models import Importe
from .models import Pago
from .forms import SocioForm
from .forms import PagoForm
from .forms import ImporteForm
from django.shortcuts import redirect
# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response

from django.shortcuts import get_object_or_404

def search(request):
    query =request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(documento__icontains=query)
        )
        results = Socio.objects.filter(qset).distinct()
    else:
        return redirect('aplicacionSociosCooperativa.views.socio_list')
        #results = []
    return render(request, 'aplicacionSociosCooperativa/buscador.html',{"results":results,"query":query})

def socio_list(request):
    socios = Socio.objects.all().order_by('documento')
    #pagos = Pago.objects.all()#.order_by('socio.documento')
    #return render(request, 'aplicacionSociosCooperativa/socio_list.html',{{'socios':socios},{'pagos':pagos}})
    return render(request, 'aplicacionSociosCooperativa/socio_list.html',{'socios':socios})

#def buscador_socios(reques,busqueda):
#    soios = Socio.objects.filter(nombre = busqueda).order_by('documento')
#    return render(request, 'aplicacionSociosCooperativa/socio_list.html',{'socios':socios})

def importe_list(request):
    importes = Importe.objects.all().order_by('-fechaInicio')
    return render(request, 'aplicacionSociosCooperativa/importe_list.html', {'importes':importes})

def pago_list(request):
    pagos = Pago.objects.all()
    return render(request, 'aplicacionSociosCooperativa/pago_list.html', {'pagos':pagos})

def actualizarTipoSocioPago(pk):
    socioActualizar = get_object_or_404(Socio, pk=pk)
    pagos = Pago.objects.filter(socio=socioActualizar)
    pagado = 0
    for pago in pagos:
        pagado = pagado + pago.pago
    #importeVigente = Importe.objects.filter(socio.fechaInscripcion__gt=fechaInicio, socio.fechaInscripcion__lt=fechaFin)
    importeVigente = Importe.objects.get(fechaInicio__lte = socioActualizar.fechaInscripcion, fechaFin__gte = socioActualizar.fechaInscripcion)
    #if importeVigente.coste <= pagos.pago__sum :
    if importeVigente.coste <= pagado :
        socioActualizar.socioCompleto = 1
        socioActualizar.save()

'''
def actualizarTipoSocioImporte():
    socios = Socio.objects.filter()
    for socio in socios :
'''

def nuevoSocio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save(commit=False)
            socio.save()
            return redirect('aplicacionSociosCooperativa.views.socio_list')
    else:
        form = SocioForm()
    return render(request, 'aplicacionSociosCooperativa/socioNuevo.html', {'form': form})

def socioEditar (request, pk):
	socio = get_object_or_404(Socio, pk=pk)
	if request.method == "POST":
		form = SocioForm(request.POST, instance=socio)
		if form.is_valid():
			socio = form.save(commit=False)
			socio.save()
			return redirect('aplicacionSociosCooperativa.views.socio_list')
	else:
		form = SocioForm(instance=socio)
	return render(request, 'aplicacionSociosCooperativa/socioEditar.html', {'form':form})

def socioEliminar (request, pk):
	Socio.objects.filter(pk=pk).delete()
	return redirect('aplicacionSociosCooperativa.views.socio_list')

def importeNuevo(request):
    if request.method == "POST":
        form = ImporteForm(request.POST)
        if form.is_valid():
            importe = form.save(commit=False)
            importe.save()
            return redirect('aplicacionSociosCooperativa.views.importe_list')
    else:
        form = ImporteForm()
    return render(request, 'aplicacionSociosCooperativa/importeNuevo.html', {'form': form})



def pagoNuevo(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.save()
            actualizarTipoSocioPago(pago.socio.pk)
            return redirect('aplicacionSociosCooperativa.views.pago_list')
    else:
        form = PagoForm()
    return render(request, 'aplicacionSociosCooperativa/pagoNuevo.html', {'form': form})



def pagoEditar (request, pk):
	pago = get_object_or_404(Pago, pk=pk)
	if request.method == "POST":
		form = PagoForm(request.POST, instance=pago)
		if form.is_valid():
			pago = form.save(commit=False)
			pago.save()
			return redirect('aplicacionSociosCooperativa.views.pago_list')
	else:
		form = PagoForm(instance=pago)
	return render(request, 'aplicacionSociosCooperativa/pagoEditar.html', {'form':form})

def pagoEliminar (request, pk):
	Pago.objects.filter(pk=pk).delete()
	return redirect('aplicacionSociosCooperativa.views.pago_list')

def importeEditar (request, pk):
	importe = get_object_or_404(Importe, pk=pk)
	if request.method == "POST":
		form = ImporteForm(request.POST, instance=importe)
		if form.is_valid():
			importe = form.save(commit=False)
			importe.save()
			return redirect('aplicacionSociosCooperativa.views.importe_list')
	else:
		form = ImporteForm(instance=importe)
	return render(request, 'aplicacionSociosCooperativa/importeEditar.html', {'form':form})

def importeEliminar (request, pk):
	Importe.objects.filter(pk=pk).delete()
	return redirect('aplicacionSociosCooperativa.views.importe_list')

'''
def socio_nuevo(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save(commit=False)
            socio.save()
            return redirect('aplicacionSociosCooperativa.views.socio_list')
    else:
        form = SocioForm()
    return render(request, 'aplicacionSociosCooperativa/socioEdit.html', {'form':form})
'''
