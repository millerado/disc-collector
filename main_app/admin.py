from django.contrib import admin
from .models import Disc, Throws, User

# Register your models here.
admin.site.register(Disc)
admin.site.register(Throws)
admin.site.register(User)