from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish


def optimal_menu(request):
    clients = int(request.GET['clients'])
    max_weight = clients*100
    q = Dish.objects.filter(rations__gt=0, weight__lte=max_weight)

    options = {}

    for dish in q:
        req_dishes = max_weight // dish.weight
        if req_dishes > dish.rations:
            avai_dishes = dish.rations
        else:
            avai_dishes = req_dishes

        for ind in range(1, avai_dishes+1):
            options[(ind, dish)] = max_weight - ind*dish.weight


    for elem 

    breakpoint()
    return HttpResponse('Hello')
