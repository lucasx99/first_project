from django.shortcuts import render
from first_app.models import RegistroAcesso
from .forms import FormName, ModelForm,FiveModelForm


# Create your views here.
def index(request):
    dict_lista2 = {"lista_acessos": RegistroAcesso.objects.order_by('data')}
    return render(request, 'index.html', dict_lista2)


def calculadora(request):
    return render(request, 'calculadora.html')


def site(request):
    return render(request, 'site.html')

def links(request):
    return render(request, 'links.html')

def help(request):
    var = {"variavel": '<p>O bala é muito mala<p>'}
    return render(request, 'help.html', var)


def form_name(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Os campos estão corretos")
            print("Nome: ", form.cleaned_data['nome'])
            print("Email: ", form.cleaned_data['email'])
            print("Texto: ", form.cleaned_data['texto'])

    return render(request, 'form.html', {"form": form})


def modelform(request):
    form = ModelForm()

    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'modelform.html', context={'modelform': form})

def fivemodelform(request):
    form = FiveModelForm()

    if request.method == 'POST':
        form = FiveModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'fivemodelform.html', context={'fivemodelform': form})