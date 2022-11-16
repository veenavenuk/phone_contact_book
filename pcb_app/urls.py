from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from pcb_app.views import *

urlpatterns=[
   path('',views.list,name='list'),
   path('view_dtls/<int:id>',views.view_dtls,name='view_dtls'),
   path('edit/<int:id>',views.edit,name='edit'),
   path('delete/<int:id>',views.delete,name='delete'),
   path('view_contact_dtls/',views.view_contact_dtls,name='view_contact_dtls'),
   path('contact_add_sv/',views.contact_add_sv,name='contact_add_sv'),
  
]


