from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(type__icontains=search_query)
        )
    
    # Category filtering
    category = request.GET.get('category', '')
    if category:
        products = products.filter(type=category)
    
    # Sorting
    sort = request.GET.get('sort', '')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'rating':
        products = products.order_by('-rating')
    
    # Get unique categories for the filter dropdown
    categories = Product.objects.values_list('type', flat=True).distinct()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
        'current_sort': sort
    }
    return render(request, 'main/index.html', context)
