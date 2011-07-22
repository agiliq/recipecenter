from django.db import models
from djangoratings.fields import RatingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
   # slug = models.SlugField(max_length=100)
    
    def get_absolute_url(self):
        return "/category/%s/" % self.name
   
   

class RecipeDump(models.Model):
    class Meta:
        db_table = "addrecipe"
        ordering = ['name']
    def __unicode__(self):
        return self.name

    #imported_pk = models.IntegerField()
   # category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,null=True,blank=True)
    something = models.CharField(max_length = 100, null=True, blank=True)
    name =  models.CharField(max_length = 100)
    ingredients =  models.TextField()
    instructions = models.TextField()
    image = models.CharField(max_length=100, null=True, blank=True)
    blah = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    foo = models.CharField(max_length=100)
    bar = models.CharField(max_length=100)
    baz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    rating = RatingField(range=5)

    def title(self):
        return self.name
   
    def get_absolute_url(self):
        return "/details/%s/" % self.slug
    


    
   
    
