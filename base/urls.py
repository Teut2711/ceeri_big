from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name="base-main"),

    path('project/',
         ProjectRequestView.as_view(), name="base-Project"),

    path('tot/',
         ToTRequestView.as_view(), name="base-ToT"),

    path('nda/',
         NDARequestView.as_view(), name="base-NDA"),

    path('mou/',
         MoURequestView.as_view(), name="base-MoU"),

    path('techservice/',
         TechServiceRequestView.as_view(), name="base-TechService"),

    path('<str:form_request_type>/international/',
         InternationalView.as_view(), name="base-International"),

    path('<str:form_request_type>/national/',
         NationalView.as_view(), name="base-National"),

    path('<str:form_request_type>/<str:form_type>/sponsered/',
         SponseredView.as_view(), name="base-Sponsered"),

    path('<str:form_request_type>/<str:form_type>/collaborative/',
         CollaborativeView.as_view(), name="base-Collaborative"),
    
    path('<str:form_request_type>/<str:form_type>/consultancy/',
         ConsultancyView.as_view(), name="base-Consultancy"),
]
