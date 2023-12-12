from django.shortcuts import render

from .models import Contact

from .forms import ContactForm

def index(request):
    return list_view(request)

def create_contact_view(request):

    context = {}

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "create_contact_view.html", context)

def list_view(request):
   
   context = {}

   context['dataset'] = Contact.objects.all()

   return render(request, "list_view.html", context)