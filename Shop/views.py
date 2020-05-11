from django.shortcuts import render
from .models import Product,Contact_us,Order,OrderUpdated
from math import ceil
from django.http import HttpResponse
import json
# Create your views here.
def Index(request):
    DBproducts = Product.objects.all()
    allpdc = []
    pdc = Product.objects.values('product_subcatagory','id')
    sub_ctgry = {item['product_subcatagory'] for item in pdc}
    for ctgy in sub_ctgry:
        pdcs = Product.objects.filter(product_subcatagory=ctgy)
        allpdc.append([pdcs,ctgy])    
    
    Dictionary = {"allpdc":allpdc}
    return render(request,'shop/index.html',Dictionary)
def About(request):
    return render(request,'shop/about.html')
def Contact(request):
   if request.method == 'POST':
       name = request.POST.get('name','')
       email = request.POST.get('email','')
       phone = request.POST.get('phone','')
       desc = request.POST.get('message','')
       conatct = Contact_us(contacter_name=name,contacter_mail=email,contacter_phone=phone,contacter_desc=desc)
       conatct.save()
       username = {'user':name,'thank':'True'}
       return render(request,'shop/contact.html',username)   
   return render(request,'shop/contact.html')
def Tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdated.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('error')
        except Exception as e:
            return HttpResponse(str(e)) 
    return render(request,'shop/tracker.html')
def Products(request,pid):
    #Handling id
    pdc = Product.objects.filter(id=pid)   
    
    return render(request,'shop/products.html',{'product':pdc[0]})
def Search(request):
    query = request.GET.get('search')
    products = Product.objects.filter()
    searched_pdt = []
    for DB in products:
        if query.lower() in DB.product_name.lower() or query.lower() in DB.product_catagory.lower():
            searched_pdt.append(DB)
    if searched_pdt  == 0:
        # result = {'allprods':searched_pdt}
        return HttpResponse('No Item with "'+query+'"')
    send_dict = {'searched_item':searched_pdt} 
    return render(request, 'shop/search.html',send_dict)
def Checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('addressline1', '') + " " + request.POST.get('addressline2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        
        thank = True
        id = order.order_id
        
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request,'shop/checkout.html')
