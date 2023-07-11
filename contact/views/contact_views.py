from django.shortcuts import render, get_object_or_404, redirect
#https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')#[:2]
    # contact = Contact.objects.all

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
        'site_title': 'Contatos - '
    }

    # print(contact.query)

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()
    print('Search Value:',search_value)
    
    if search_value == '':
        return redirect('contact:index')
        

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) | 
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
        ).order_by('-id')

    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(contacts.query)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value
    }

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
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    print(single_contact)
    # contact = Contact.objects.all
    context = {
        'contact':single_contact,
        'site_title':site_title
    }

    # print(contact.query)

    return render(
        request,
        'contact/contact.html',
        context
    )