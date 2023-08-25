from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contact_list"),
    path("create/", views.ContactCreateView.as_view(), name="contact_create"),
    path("update/<int:pk>/", views.ContactUpdateView.as_view(), name="contacts_update"),
    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="contacts_delete"),
]
