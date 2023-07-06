from django.shortcuts import render
from contact.models import Contact

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