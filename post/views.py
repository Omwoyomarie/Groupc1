from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from .models import ItemList  # Replace with your app's model if needed

@login_required()
def index(request):
    people = ItemList.objects.all()
    return render(request, 'index.html' ,{'people':people})

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
            return redirect('index')  # this name must match your urls.py

    return render(request, 'item.html')
def delete(request, id):
    person = get_object_or_404(ItemList, id=id)
    try:
        person.delete()
        messages.success(request, 'Person deleted successfully')
    except Exception as e:
        messages.error(request, "person not deleted")

    return redirect('index')
def edit(request,id):
    person = get_object_or_404(ItemList, id=id)

    if request.method == 'POST':
        person.sample_item = request.POST.get('sample_item')
        person.category= request.POST.get('category')
        person.date = request.POST.get('date')
        person.save()

        return redirect('index')
    return render(request, 'edit.html',{'person':person})


def login_one(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username OR password is incorrect')
            return redirect('index')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


