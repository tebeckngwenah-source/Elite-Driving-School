from django.contrib import admin
from .models import Contact_user
admin.site.site_header = 'Welcome to Elilte Driving School Dashboard'
admin.site.index_title = 'NOVATECH Innovations'
admin.site.register(Contact_user)
