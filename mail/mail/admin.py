from curses.ascii import EM
import django
from django.contrib import admin
from .models import User, Email
# Register your models here.
admin.site.register(User)
admin.site.register(Email)