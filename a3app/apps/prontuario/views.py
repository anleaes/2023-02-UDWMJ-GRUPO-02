from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProntuarioForm
from .models import Prontuario
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_prontuario(request):
    template_name = 'prontuario/add_prontuario.html'
    context = {}
    if request.method == 'POST':
        form = ProntuarioForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('prontuario:list_prontuario')
    form = ProntuarioForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_prontuario(request):
    template_name = 'prontuario/list_prontuario.html'
    prontuario = Prontuario.objects.filter()
    context = {
        'prontuario': prontuario
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_prontuario(request, id_prontuario):
    template_name = 'prontuario/add_prontuario.html'
    context ={}
    prontuario = get_object_or_404(Prontuario, id=id_prontuario)
    if request.method == 'POST':
        form = ProntuarioForm(request.POST, request.FILES,  instance=prontuario)
        if form.is_valid():
            form.save()
            return redirect('prontuario:list_prontuario')
    form = ProntuarioForm(instance=prontuario)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_prontuario(request, id_prontuario):
    prontuario = Prontuario.objects.get(id=id_prontuario)
    prontuario.delete()
    return redirect('prontuario:list_prontuario')