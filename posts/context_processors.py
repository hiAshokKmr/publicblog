from .models import Category, Language

def language_category_context(request):
    return {
        'categories': Category.objects.all(),
        'languages': Language.objects.all(),
    }
