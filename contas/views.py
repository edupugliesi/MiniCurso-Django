from django.shortcuts import redirect, render
from .models import Transacao
import datetime
from .forms import TransacaoForm



def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')
    return render(request, 'contas/form.html', {'form': form})

