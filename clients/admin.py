from django.contrib import admin
from clients.models import Client


class PreviewClient(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'gender',
        'birth_date',
        'address',
        'credits',
    ]


admin.site.register(Client, PreviewClient)
