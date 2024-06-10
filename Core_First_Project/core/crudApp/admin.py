from django.contrib import admin
from .models import userDetail
# Register your models here.
class userDetailAdmin(admin.ModelAdmin):
    list_display=("name","age")
    
admin.site.register(userDetail,userDetailAdmin)