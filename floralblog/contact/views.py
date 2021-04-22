from django.shortcuts import render
from django.http import HttpResponse


def contact_form(request):
    return render(request, 'contact/contact_form.html')


def success_view(request):
    return render(request, 'contact/success.html')
