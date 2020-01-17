from django.shortcuts import render, redirect, get_object_or_404



from .models import Ideia
from .forms import IdeiaForm


# Funções dos CRUDS

# CRUD IDEIA
#Alterar isso aqui para:

def IdeiaUpdatea(request, pk):
    ideia = get_object_or_404(Ideia, pk=pk)
    form = IdeiaForm(request.POST or None, instance=ideia)
    if form.is_valid():
        form.save()
        return redirect('ideialista')
    return render(request, 'ideiaupdate.html', {'form':form})



'''def IdeiaUpdate(UpdateView):
    model = Ideia
    form_class = IdeiaForm()
    template_name = 'Ideiaupdate.html'
    success_url = reverse_lazy('Ideialista')
'''

def ideialista(request):
    ideias = Ideia.objects.all()

    return render(request, 'lista.html', {'ideias': ideias})


def ideia_create(request):
    form = IdeiaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('ideialista')
    return render(request, 'index.html', {'form': form})


def ideia_delete(request, pk):
    ideia = get_object_or_404(Ideia, pk=pk)
    form = IdeiaForm(request.POST or None, request.FILES or None, instance=ideia)

    if request.method == 'POST':
        ideia.delete()
        return redirect('ideialista')

    return render(request, 'ideiadelete.html', {'form': form})
