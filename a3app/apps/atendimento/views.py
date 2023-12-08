from django.shortcuts import render, get_object_or_404, redirect
from .forms import AtendimentoForm
from .models import Atendimento , Paciente

def add_atendimento(request, id_paciente):
    template_name = 'atendimento/add_atendimento.html'
    context = {}
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.paciente = Paciente.objects.get(id=id_paciente)
            f.save()
            form.save_m2m()
            return redirect('atendimento:list_atendimento')
    form = AtendimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_atendimento(request):
    template_name = 'atendimento/list_atendimento.html'
    atendimento = Atendimento.objects.filter()
    paciente = Paciente.objects.filter()
    context = {
        'atendimento': atendimento,
        'paciente': paciente
    }
    return render(request, template_name, context)

def delete_atendimento(request, id_atendimento):
    atendimento = Atendimento.objects.get(id=id_atendimento)
    atendimento.delete()
    return redirect('atendimento:list_atendimento')
