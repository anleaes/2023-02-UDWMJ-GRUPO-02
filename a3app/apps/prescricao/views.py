from django.shortcuts import render, get_object_or_404, redirect
from .forms import PrescricaoForm
from .models import Prescricao, Medico

# Create your views here.
def add_prescricao(request, id_medico):
    template_name = 'prescricao/add_prescricao.html'
    context = {}
    if request.method == 'POST':
        form = PrescricaoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.medico = Medico.objects.get(id=id_medico)
            f.save()
            form.save_m2m()
            return redirect('precricao:list_prescricao')
    form = PrescricaoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_prescricao(request):
    template_name = 'prescricao/list_prescricao.html'
    prescricao = Prescricao.objects.filter()
    medico = Medico.objects.filter()
    context = {
        'prescricao': prescricao,
        'medico': medico
    }
    return render(request, template_name, context)

def delete_prescricao(request, id_prescricao):
    prescricao = Prescricao.objects.get(id=id_prescricao)
    prescricao.delete()
    return redirect('prescricao:list_prescricao')