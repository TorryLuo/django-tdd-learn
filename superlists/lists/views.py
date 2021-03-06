from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    data = Item.objects.all()
    return render(request, 'home.html', {"items": data})
