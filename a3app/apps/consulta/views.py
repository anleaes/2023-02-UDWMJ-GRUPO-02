from django.shortcuts import render, get_object_or_404, redirect
from .forms import ConsultaForm
from .models import Consulta
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_consulta(request):
    template_name = 'consulta/add_consulta.html'
    context = {}
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('consulta:list_consulta')
    form = ConsultaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_consulta(request):
    template_name = 'consulta/list_consulta.html'
    consultas = Consulta.objects.filter()
    context = {
        'consultas': consultas,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_consulta(request, id_consulta):
    template_name = 'consulta/add_consulta.html'
    context ={}
    consulta = get_object_or_404(Consulta, id=id_consulta)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta:list_consulta')
    form = ConsultaForm(instance=consulta)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    consulta.delete()
    return redirect('consulta:list_consulta')
