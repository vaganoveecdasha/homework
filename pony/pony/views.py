from django.http import HttpResponse
from django.shortcuts import render

MENU = {"HOME": "/", "About": "/about", "Comments": "/form"}
Pony = {"Apple Jack": "/appleJack", "Rarity": "/rarity", "Rainbow Dash": "/rainbowDash"}
def main_page(request):
    title = "Pony"
    data = {"menu": MENU, "Pony": Pony, "title": title}
    return render(request, "./index.html", context=data)

def jack_page(request):
    title = "Apple Jack"
    data = {"menu":MENU, "title": title}
    return render(request, "./jack.html", context=data)

def rarity_page(request):
    title = "Rarity"
    data = {"menu": MENU, "title": title}
    return render(request, "./rarity.html", context=data)

def dash_page(request):
    title = "Rainbow Dash"
    data = {"menu":MENU, "title": title}
    return render(request, "./dash.html", context=data)

def about_page(request):
    title = "BLOG"
    data = {"menu":MENU, "title": title}
    return render(request, "./about.html", context=data)


