from django.contrib import admin

# Register your models here.

# Superuser login:
# ---------------
# username: cp317
# email: cp317@gmail.com
# password: davidbrown

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)