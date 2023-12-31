from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExameForm
from .models import Exame
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_exame(request):
    template_name = 'exame/add_exame.html'
    context = {}
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('exame:list_exame')
    form = ExameForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_exame(request):
    template_name = 'exame/list_exame.html'
    exame = Exame.objects.filter()
    context = {
        'exame': exame,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_exame(request, id_exame):
    template_name = 'exame/add_exame.html'
    context ={}
    exame = get_object_or_404(Exame, id=id_exame)
    if request.method == 'POST':
        form = ExameForm(request.POST, instance=exame)
        if form.is_valid():
            form.save()
            return redirect('exame:list_exame')
    form = ExameForm(instance=exame)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_exame(request, id_exame):
    exame = Exame.objects.get(id=id_exame)
    exame.delete()
    return redirect('exame:list_exame')