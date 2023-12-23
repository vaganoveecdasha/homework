from django.shortcuts import render
from .models import Form

MENU = {"HOME": "/", "About": "/about", "Comments": "/form"}

def form_page(request):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    text = request.POST.get('text')
    if firstName and lastName and email and text:
        Form.objects.create(firstName=firstName, lastName=lastName, email=email, text=text)
    forms = Form.objects.filter(checked=True)
    data = {"menu": MENU, "forms": forms}
    return render(request, './form.html', context=data)
