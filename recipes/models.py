from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/category/%s/" % self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    something = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.CharField(max_length=100, null=True, blank=True)
    blah = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100)
    foo = models.CharField(max_length=100)
    bar = models.CharField(max_length=100)
    baz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_featured = models.BooleanField('Featured',
                                      default=False,
                                      help_text='Designates whether this\
                                      recipe should be treated as featured.')

    def __unicode__(self):
        return self.name

    def title(self):
        return self.name

    def get_absolute_url(self):
        return "/detail/%s/" % self.slug

    def get_image(self):
        try:
            #temp = open(self.image)
            import os
            import settings

            image_url = os.path.join(settings.STATIC_ROOT,
                                     'images/%s' % self.image)
            print "image_url", image_url
            #temp.close()

        except IOError:
            image_url = None
        print image_url
        return image_url
