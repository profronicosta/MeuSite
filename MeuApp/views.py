from django.shortcuts import render

# Create your views here.
def home(request):
    # variáveis que vou enviar para o template
    context = {
        'nome': 'Ronivaldo',
        'sobrenome': 'Pereira'
    }

    #o segundo parametro é o caminho do html
    return render(request, 'home.html', context)

def contato(request):
    return render(request, 'contato.html')

def exibir_produtos(request):
    
    produtos = ['Bonés', 'Camisetas', 'Agasalhos']
    context = {
        'produtos': produtos
    }

    return render(request, 'produtos.html', context)