from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room, Category


def room_list(request):
    rooms = Room.objects.all()

    return render(request, 'room_list.html', {'rooms': rooms})



def add_room(request):
    if request.method == 'POST':
        numbers = request.POST.get('numbers')
        capacity = request.POST.get('capacity')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)
        room = Room.objects.create(
            numbers=numbers,
            capacity=capacity,
            description=description,
            category=category,
            price=price,
            image=image
        )
        return redirect(reverse('room_list'))

    categories = Category.objects.all()
    return render(request, 'add_room.html', {'categories': categories})
