import datetime
from haystack.indexes import *
from haystack import site
from recipes.models import Recipe


class RecipeIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    category = CharField(model_attr='category')
    name = CharField(model_attr='name')
    ingredients = CharField(model_attr='ingredients')
    slug = CharField(model_attr='slug')

    def index_queryset(self):
        return RecipeIndex.objects.filter(pub_date_lte=datetime.datetime.now())

site.register(Recipe, RecipeIndex)
