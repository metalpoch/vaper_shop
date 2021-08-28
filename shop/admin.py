from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Client, SalesRecord, Product


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
admin.site.register(SalesRecord)
admin.site.register(Product)
