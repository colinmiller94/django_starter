from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'website/home.html', context={'title': 'Home'})


def about(request):
    return render(request, 'website/about.html', context={'title': 'About'})