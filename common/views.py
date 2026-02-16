from django.shortcuts import render


def home_page(request):
    return render(request, "common/home.html")


def about_page(request):
    return render(request, "common/about.html")
