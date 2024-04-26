from django.db import models
from django.conf import settings
from froala_editor.fields import FroalaField


from .utils import generate_slug

# Create your models here.



class PostModel(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    content = FroalaField(theme='dark')
    image = models.ImageField(upload_to='blogPost/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        
        super(PostModel, self).save(*args, **kwargs)
    
   
    def get_image_url(self):
        image_url = self.image.url
        print("Image URL", image_url)
        return image_url

    