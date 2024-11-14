from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path("create_ticket/",views.create_ticket, name="create_ticket"),
    path("list_ticket/",views.list_ticket, name="list_ticket"),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/add_comment/<int:ticket_id>/', views.add_comment, name='add_comment'),
    path('tickets/update_ticket_status/<int:ticket_id>/', views.update_ticket_status, name='update_ticket_status')
]