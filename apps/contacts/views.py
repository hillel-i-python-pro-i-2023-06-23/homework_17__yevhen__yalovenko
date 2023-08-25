from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.contacts.models import Contact


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
