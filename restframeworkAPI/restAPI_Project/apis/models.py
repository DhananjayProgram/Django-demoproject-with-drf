from django.db import models


class StreamPlatform(models.Model):
    
    name = models.CharField(max_length = 50)
    about = models.CharField(max_length = 100)
    website = models.URLField(max_length = 100)
    def __str__(self) -> str:
        return self.name

class WatchList(models.Model):
    
    title = models.CharField(max_length = 50)
    storyline = models.CharField(max_length = 100)
    platform = models.ForeignKey(StreamPlatform , on_delete = models.CASCADE , related_name = "watch_list")
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'WatchList'
        verbose_name_plural = 'WatchLists'

