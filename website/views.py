from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'website/home.html', context={'title': 'Home'})


def resume(request):
    return render(request, 'website/resume.html', context={'title': 'Resume'})


def contact(request):
    return render(request, 'website/contact.html', context={'title': 'Contact'})

def calculator(request):
    return render(request, 'website/calculator.html', context={'title': 'Calculator'})
