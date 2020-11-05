from django.contrib import admin
from backend.models import *

admin.site.register(User)
admin.site.register(Client)

# class InnerCircleAdmin(admin.ModelAdmin):
#     filter_horizontal = ('contacts',)

admin.site.register(Profile)
admin.site.register(InnerCircle)
admin.site.register(Mowiki)
admin.site.register(Interest)
admin.site.register(Level)
admin.site.register(Community)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(SubComment)