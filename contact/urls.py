from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [

    # contact (CRUD)
    path('', views.index, name='index'),
    path('contact/<int:contact_id>/', views.contact, name='contactt'),
    path('search/', views.search, name='search'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
]
