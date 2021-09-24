
# To make the categories available in all templates
# we have created context_processor from the settings django.contrib.messages.context_processors.messages

from .models import Category


def categories(request):
    return {
        # 'categories': Category.objects.all()
        ##for mptt to remove the django model under django
        'categories' : Category.objects.filter(level=0) #for the parent(root which is django), 1 is djaango model 

    }
