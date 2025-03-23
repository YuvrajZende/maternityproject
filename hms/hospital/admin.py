from django.contrib import admin
from .models import CustomUser, Hospital

admin.site.register(CustomUser)
admin.site.register(Hospital)
