from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Mid_level_User)
admin.site.register(Low_level_User)
admin.site.register(High_level_User)
admin.site.register(Form)
admin.site.register(Input)
admin.site.register(Action)
admin.site.register(FormStructure)
admin.site.register(FormValues)