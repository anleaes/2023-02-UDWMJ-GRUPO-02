from django.shortcuts import render, get_object_or_404, redirect
from .forms import AtendimentoForm
from .models import Atendimento
from django.contrib.auth.decorators import login_required

@login_required(login_url='/contas/login/')
def add_atendimento(request):
    template_name = 'atendimento/add_atendimento.html'
    context = {}
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('atendimento:list_atendimento')
    form = AtendimentoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_atendimento(request):
    template_name = 'atendimento/list_atendimento.html'
    atendimento = Atendimento.objects.filter()
    context = {
        'atendimento': atendimento,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_atendimento(request, id_atendimento):
    template_name = 'atendimento/add_atendimento.html'
    context ={}
    atendimento = get_object_or_404(Atendimento, id=id_atendimento)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, request.FILES,  instance=atendimento)
        if form.is_valid():
            form.save()
            return redirect('atendimento:list_atendimento')
    form = AtendimentoForm(instance=atendimento)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_atendimento(request, id_atendimento):
    atendimento = Atendimento.objects.get(id=id_atendimento)
    atendimento.delete()
    return redirect('atendimento:list_atendimento')
