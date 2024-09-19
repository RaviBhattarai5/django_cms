from django.db import models

class Menu(models.Model):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.menu'
    
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    url = models.URLField(max_length=255)
    icon = models.TextField(default='<path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>')

    position = models.IntegerField(unique=True, blank=True, null=True)
    publish = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Automatically set position to increment based on the highest position
        if self.position is None:
            last_position = Menu.objects.aggregate(max_position=models.Max('position'))['max_position']
            self.position = 1 if last_position is None else last_position + 1
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
