from django.shortcuts import (get_object_or_404,
                               render,
                               HttpResponseRedirect)
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

def detail_view(request, id):
    context = {}

    context["data"] = Contact.objects.get(id=id)

    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(Contact, id=id)

    form = ContactForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    
    context["form"] = form

    return render(request, "update_view.html", context)

def delete_view(request, id):
    pass