from haystack import indexes
from recipes.models import Recipe


class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr='category')
    name = indexes.CharField(model_attr='name')
    ingredients = indexes.CharField(model_attr='ingredients')
    slug = indexes.CharField(model_attr='slug')

    def get_model(self):
        return Recipe

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
