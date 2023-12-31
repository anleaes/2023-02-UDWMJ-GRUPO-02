from django.shortcuts import render, get_object_or_404, redirect
from .forms import PacienteForm
from .models import Paciente
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_paciente(request):
    template_name = 'paciente/add_paciente.html'
    context = {}
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('paciente:list_paciente')
    form = PacienteForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_paciente(request):
    template_name = 'paciente/list_paciente.html'
    paciente = Paciente.objects.filter()
    context = {
        'paciente': paciente,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_paciente(request, id_paciente):
    template_name = 'paciente/add_paciente.html'
    context ={}
    paciente = get_object_or_404(Paciente, id=id_paciente)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente:list_paciente')
    form = PacienteForm(instance=paciente)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    paciente.delete()
    return redirect('paciente:list_paciente')

#============= Buscar
def search_paciente(request):
    template_condicao = 'paciente/list_paciente.html'
    query = request.GET.get('query')
    paciente = Paciente.objects.filter(condicao__icontains=query)
    context = {
        'paciente': paciente,
    }
    return render(request,template_condicao, context)