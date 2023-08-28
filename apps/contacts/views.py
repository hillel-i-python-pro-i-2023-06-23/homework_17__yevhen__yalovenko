from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.contacts.forms import GenerateForm
from apps.contacts.models import Contact
from apps.contacts.services.delete_contacts import delete_contacts
from apps.contacts.services.generate_and_save_contacts import generate_and_save_contacts


class ContactsListView(ListView):
    model = Contact


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

    return render(
        request=request,
        template_name="contacts/contacts_generate.html",
        context=dict(
            contacts_list=Contact.objects.all(),
            form=form,
        ),
    )


def delete_contacts_view(request):
    delete_contacts()

    return redirect(reverse_lazy("contacts:contact_list"))
