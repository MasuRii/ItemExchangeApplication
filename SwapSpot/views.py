from django.shortcuts import render
from .models import Item

def homepage(request):
    query = request.GET.get('q', '')
    if query:
        # Search for items based on the query
        items = Item.objects.filter(title__icontains=query).order_by('date_listed')  # Ascending order (oldest to newest)
    else:
        # Retrieve the 10 most recent items, ordered from newest to oldest
        items = Item.objects.all().order_by('-date_listed')[:10]  # Descending order (newest first)

    context = {
        'items': items,
        'query': query,
    }
    return render(request, 'exchange/homepage.html', context)
