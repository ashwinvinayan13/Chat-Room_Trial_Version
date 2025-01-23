from django.shortcuts import render

def lobby(request):
    return render(request, 'chat/lobby.html')


def home(reqeust):
    return render(reqeust, 'chat/home.html')