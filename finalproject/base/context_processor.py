from base.models import categories

def get_categories(request):
    d={
        'categories':categories.objects.all()
    }

    return d
    
    