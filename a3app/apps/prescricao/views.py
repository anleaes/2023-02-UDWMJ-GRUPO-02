from django.shortcuts import render, get_object_or_404, redirect
from .forms import PrescricaoForm
from .models import Prescricao
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_prescricao(request):
    template_name = 'prescricao/add_prescricao.html'
    context = {}
    if request.method == 'POST':
        form = PrescricaoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('prescricao:list_prescricao')
    form = PrescricaoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_prescricao(request):
    template_name = 'prescricao/list_prescricao.html'
    prescricao = Prescricao.objects.filter()
    context = {
        'prescricao': prescricao
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_prescricao(request, id_prescricao):
    template_name = 'prescricao/add_prescricao.html'
    context ={}
    prescricao = get_object_or_404(Prescricao, id=id_prescricao)
    if request.method == 'POST':
        form = PrescricaoForm(request.POST, request.FILES,  instance=prescricao)
        if form.is_valid():
            form.save()
            return redirect('prescricao:list_prescricao')
    form = PrescricaoForm(instance=prescricao)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_prescricao(request, id_prescricao):
    prescricao = Prescricao.objects.get(id=id_prescricao)
    prescricao.delete()
    return redirect('prescricao:list_prescricao')
