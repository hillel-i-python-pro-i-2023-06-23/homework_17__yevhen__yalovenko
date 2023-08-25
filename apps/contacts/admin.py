from django.contrib import admin

from apps.contacts.models.contact import Contact, ContactDataType, ContactData
from apps.contacts.models.group import Group


class ContactDataInline(admin.TabularInline):
    model = ContactData
    extra = 0


class GroupInline(admin.StackedInline):
    model = Group.contacts.through
    extra = 0


class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactDataInline, GroupInline]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Group)
admin.site.register(ContactDataType)
