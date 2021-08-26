from .models import Category


# add context_processor under template so these category will reflect in all pages
# They come in handy when you need to make something available globally to all templates.

def category(request):
    return{
        'categories':Category.objects.all() 
    }