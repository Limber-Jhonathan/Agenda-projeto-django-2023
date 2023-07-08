from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def create(request):

    if request.method == 'POST':
        print(request.method) 
        search = request.POST.get('first_name')
        search2 = request.POST.get('last_name')
        print(search)
        print(search2)

    # post = request.POST
    context = {

    }

    print(request.method) 

    return render(
        request,
        'contact/create.html',
        context
    )