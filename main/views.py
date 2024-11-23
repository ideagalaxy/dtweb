from django.shortcuts import render,redirect
import random
from .models import *

def first_page(request):
    print("this is first_page")
    print(request.POST)
    if "click" in request.POST:
        length  = len(Store.objects.all())
        print(length)
        get_id = random.randint(1,length)
        print(get_id)
        return redirect(f'/{get_id}/')



    return render(request, 'first_page.html')

def store_page(request, pk):
    store  = Store.objects.get(id = pk)
    print(store)
    
    context={}
    context["store"] = store.name
    context["desc"] = store.desc

    
    return render(request, 'store_page.html',context)

def store_list(request):
    store_list = Store.objects.all()
    print(store_list)
    context = {}
    context["store_list"] = store_list

    if "click" in request.POST:
        return redirect(f'add')


    return render(request, 'store_list.html',context)

def change(request,pk):
    store  = Store.objects.get(id = pk)
    print(store)
    
    context={}
    context["store"] = store.name
    context["desc"] = store.desc

    match store.dist:
        case 1:
            dist = "가까운 거리"
        case 2:
            dist = "적당한 거리"
        case 3:
            dist = "살짝 먼 거리"
    context["dist"] = dist

    if request.method == "POST":
        if 'change' in request.POST:
            print(request.POST)
            new_name = request.POST.get("name")
            new_dist = request.POST.get("distance")
            match new_dist:
                case "min":
                    new_dist = 1
                case "mid":
                    new_dist = 2
                case "max":
                    new_dist = 3

            new_desc = request.POST.get("desc")
            Store.objects.filter(id = pk).update(name = new_name)
            Store.objects.filter(id = pk).update(dist = new_dist)
            Store.objects.filter(id = pk).update(desc = new_desc)
            
            return redirect(f'/store_list')
        
        if 'delete' in request.POST:
            Store.objects.filter(id = pk).delete()
            return redirect(f'/store_list')
    
    return render(request, 'change.html',context)

def add(request):
    context={}
    print(request.POST)
    if request.method == "POST":
        if 'add' in request.POST:
            print(request.POST)
            new_name = request.POST.get("name")
            if new_name == "":
                return redirect(f'/add')
            new_dist = request.POST.get("distance")
            if new_dist == "":
                return redirect(f'/add')
            new_type = request.POST.get("type")
            if new_type == "":
                return redirect(f'/add')
            match new_dist:
                case "min":
                    new_dist = 1
                case "mid":
                    new_dist = 2
                case "max":
                    new_dist = 3
            new_desc = request.POST.get("desc")
            
            Store.objects.create(name = new_name, type = new_type, dist=new_dist, desc = new_desc)
            return redirect(f'/store_list')
    
    return render(request, 'add.html',context)