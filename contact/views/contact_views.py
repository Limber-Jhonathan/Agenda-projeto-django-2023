from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

# Create your views here.
def index(request):
    contact = Contact.objects.filter(show=True).order_by('id')#[:2]
    # contact = Contact.objects.all
    context = {
        'contacts':contact,
    }

    # print(contact.query)

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.get(pk=contact_id)#[:2]
    # O get retorna um objeto. O filter retorna uma lista.
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    print(single_contact)
    # contact = Contact.objects.all
    context = {
        'contact':single_contact,
    }

    # print(contact.query)

    return render(
        request,
        'contact/contact.html',
        context
    )