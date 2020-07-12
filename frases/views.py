from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'author': 'Jorge Rojas',
    'title': 'Primera Frase',
    'content': 'Esta es la primera frase',
    'datePosted': '11/07/2020'
},
{
    'author': 'Brawcito Rojas',
    'title': 'Segunda Frase',
    'content': 'Esta es la segunda frase',
    'datePosted': '11/07/2020'
}
]


def home(request):
    context = {'posts': posts,
    'title': 'Jorge Rojas'}
    return render(request,'frases/home.html', context)

def about(request):
    return render(request,'frases/about.html',{'title': 'Jorge Rojas About'})