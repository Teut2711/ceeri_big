from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from abc import ABC, abstractmethod


class GeneralRequestView(TemplateView, ABC):
    template_name = "base/requests.html"

    @staticmethod
    @abstractmethod
    def self_name():
        pass

    @staticmethod
    @abstractmethod
    def self_text():
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_types"] = [(class_.self_text(), class_.self_name())
                                 for class_ in GeneralFormTypeView.__subclasses__()]

        return context


class GeneralFormTypeView(TemplateView, ABC):
    template_name = "base/formtype.html"

    @staticmethod
    @abstractmethod
    def self_name():
        pass

    @staticmethod
    @abstractmethod
    def self_text():
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_types"] = [(class_.self_text(), class_.self_name())
                                 for class_ in GeneralFormView.__subclasses__()]

        return context

class GeneralFormView(FormView, ABC):

    @staticmethod
    @abstractmethod
    def self_name():
        pass

    @staticmethod
    @abstractmethod
    def self_text():
        pass
    