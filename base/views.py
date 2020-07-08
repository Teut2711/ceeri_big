from django.shortcuts import render
from django.views.generic import TemplateView
from abc import ABC, abstractmethod
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView
from base.views_general_views import *
# Create your views here.


class MainView(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["requests_views_list"] = [(class_.self_text(), class_.self_name())
                                          for class_ in ALL_REQUEST_VIEWS]
        return context


class ProjectRequestView(GeneralRequestView):
    @staticmethod
    def self_name():
        return "base-Project"

    @staticmethod
    def self_text():
        return "Project Request View"


class ToTRequestView(GeneralRequestView):
    @staticmethod
    def self_name():
        return "base-ToT"

    @staticmethod
    def self_text():
        return "ToT Request View"


class NDARequestView(GeneralRequestView):
    @staticmethod
    def self_name():
        return "base-NDA"

    @staticmethod
    def self_text():
        return "NDA Request View"


class MoURequestView(GeneralRequestView):
    @staticmethod
    def self_name():
        return "base-MoU"

    @staticmethod
    def self_text():
        return "MoU Request View"


class TechServiceRequestView(GeneralRequestView):
    @staticmethod
    def self_name():
        return "base-TechService"

    @staticmethod
    def self_text():
        return "Tech Service Request View"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


################################################################################################

class InternationalView(GeneralFormTypeView):
    @staticmethod
    def self_name():
        return "international"

    @staticmethod
    def self_text():
        return "International"

class NationalView(GeneralFormTypeView):
    @staticmethod
    def self_name():
        return "national"

    @staticmethod
    def self_text():
        return "National"

#####################################################################################


class SponseredView(GeneralFormView):
    template_name = "base/sponsered.html"
    form_class = SponseredForm

    @staticmethod
    def self_name():
        return "sponsered"

    @staticmethod
    def self_text():
        return "Sponsered"


class CollaborativeView(GeneralFormView):
    template_name = "base/collaborative.html"
    form_class = CollaborativeForm

    @staticmethod
    def self_name():
        return "collaborative"

    @staticmethod
    def self_text():
        return "Collaborative"


class ConsultancyView(GeneralFormView):
    template_name = "base/consultancy.html"

    form_class = ConsultancyForm

    @staticmethod
    def self_name():
        return "consultancy"

    @staticmethod
    def self_text():
        return "Consultancy"


ALL_REQUEST_VIEWS = [ProjectRequestView, ToTRequestView,
                     MoURequestView, TechServiceRequestView]
