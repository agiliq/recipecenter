import datetime
from haystack import indexes
from haystack import site
from recipes.models import Recipe


class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr='category')
    name = indexes.CharField(model_attr='name')
    ingredients = indexes.CharField(model_attr='ingredients')
    slug = indexes.CharField(model_attr='slug')

    def index_queryset(self):
        return RecipeIndex.objects.filter(pub_date_lte=datetime.datetime.now())

site.register(Recipe, RecipeIndex)
