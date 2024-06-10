from django.contrib import admin
from .models import StreamPlatform , WatchList
# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    
    list_display = ("title","platform","active","created")
    
class StreamPlatformAdmin(admin.ModelAdmin):
    
    list_display = ("name","about","website")

admin.site.register(StreamPlatform,StreamPlatformAdmin)
admin.site.register(WatchList,WatchListAdmin)
