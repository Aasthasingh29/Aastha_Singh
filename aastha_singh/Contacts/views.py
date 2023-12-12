from django.shortcuts import render

from .forms import ContactForm

def index(request):
    return create_contact_view(request)

def create_contact_view(request):

    context = {}

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "create_contact_view.html", context)