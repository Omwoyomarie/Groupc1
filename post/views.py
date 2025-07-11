from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import ItemList  # Replace with your app's model if needed


def index(request):
    return render(request, 'index.html')

def item(request):
    if request.method == "POST":
        sample_item = request.POST.get('sample_item')
        category = request.POST.get('category')
        date = request.POST.get('date')

        if sample_item and category and date:
            ItemList.objects.create(
                sample_item=sample_item,
                category=category,
                date=date
            )
            return redirect('item')  # this name must match your urls.py

    return render(request, 'item.html')

