from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.contacts.forms import GenerateForm
from apps.contacts.models import Contact
from apps.contacts.services.aggregation_info import (
    show_contact_data_types_counts,
    show_contacts_data_count,
    show_average_age,
    show_contact_info,
)
from apps.contacts.services.delete_contacts import delete_contacts
from apps.contacts.services.generate_and_save_contacts import generate_and_save_contacts


class ContactsListView(ListView):
    model = Contact

    def get_queryset(self):
        return show_contacts_data_count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_info = show_contact_info()

        context["contact_data_types_counts"] = show_contact_data_types_counts()
        context["youngest_age"] = contact_info.youngest_age
        context["youngest_birthdate"] = contact_info.youngest_birthdate
        context["oldest_age"] = contact_info.oldest_age
        context["oldest_birthdate"] = contact_info.oldest_birthdate
        context["average_age"] = show_average_age()
        return context


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "birthday",
    )

    success_url = reverse_lazy("contacts:contact_list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "name",
        "birthday",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context

    success_url = reverse_lazy("contacts:contact_list")


class UserDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:contact_list")


def generate_contacts_view(request):
    if request.method == "POST":
        form = GenerateForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data["amount"]

            generate_and_save_contacts(amount=amount)
    else:
        form = GenerateForm()

    contact_list = show_contacts_data_count()
    return render(
        request=request,
        template_name="contacts/contacts_generate.html",
        context=dict(
            contacts_list=contact_list,
            form=form,
        ),
    )


def delete_contacts_view(request):
    delete_contacts()

    return redirect(reverse_lazy("contacts:contact_list"))
