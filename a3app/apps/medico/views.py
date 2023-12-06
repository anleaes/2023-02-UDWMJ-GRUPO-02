from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicoForm
from .models import Medico


# Create your views here.
def add_medico(request):
    template_name = 'medico/add_medico.html'
    context = {}
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medico:list_medico')
    form = MedicoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_medicos(request):
    template_name = 'medico/list_medico.html'
    medicos = Medico.objects.filter()
    context = {
        'medicos': medicos,
    }
    return render(request, template_name, context)

def edit_medicos(request, id_medico):
    template_name = 'medico/add_medico.html'
    context ={}
    medico = get_object_or_404(Medico, id=id_medico)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico:list_medico')
    form = MedicoForm(instance=medico)
    context['form'] = form
    return render(request, template_name, context)

def delete_medico(request, id_medico):
    medico = Medico.objects.get(id=id_medico)
    medico.delete()
    return redirect('medico:list_medico')