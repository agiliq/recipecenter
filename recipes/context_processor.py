from recipes.models import Category


def call_category(request):
    return {'categobj': Category.objects.all()}
