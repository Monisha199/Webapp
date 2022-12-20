from django.contrib import admin
from .models import User,Group,Group_member
# Register your models here.
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Group_member)
