from django.shortcuts import render,redirect
from adminapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Sum
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('loginusers')

@login_required
def userindex(request):
    data = Product.objects.all()
    return render(request,'index.html',{'data':data})

@login_required
def products(request):
    categ = Category.objects.all()
    data = Product.objects.all()
    return render(request,'product.html',{'data':data,'categ':categ})

@login_required
def sortprod(request,cat):
    categ = Category.objects.all()
    data = Product.objects.filter(category = cat)
    return render(request,'product.html',{'data':data,'categ':categ})

@login_required
def contact(request):
    categ = Category.objects.all()
    return render(request,'contact.html',{'categ':categ})

def loginusers(request):
    return render(request,'loginuser.html')


def register(request):
    return render(request,'register.html')

def create_user(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password2 = request.POST['password']
        email2    = request.POST['email']
        phone2    = request.POST['phone']
        new_user  = Register.objects.create(username=username1, password=password2, email=email2, phone=phone2)
        new_user.save()
    return redirect('loginusers')
    


def login_view_user(request):
    username1 = request.POST.get('username')
    password1 = request.POST.get('password')
    if Register.objects.filter(username=username1,password=password1).exists():
        data = Register.objects.filter(username=username1,password=password1).values('email','phone','id').first()
        request.session['name'] = username1
        request.session['email'] = data['email']
        request.session['mobile'] = data['phone']
        request.session['password1'] = password1
        request.session['id'] = data['id']
        return redirect('userindex')
    else:
        error_message = ''
        return redirect('loginusers')
    
    
def userlogout(request):
    del request.session['name']
    del request.session['email']
    del request.session['mobile']
    del request.session['password1']
    del request.session['id']
    return redirect('loginusers')

def productdetails(request,id):
    categ = Category.objects.all()
    allprod = Product.objects.all()
    data    = Product.objects.filter(id = id)
    return render(request,'detail.html',{'data':data,'allprod':allprod,'categ':categ})
    
def cart(request):
    categ = Category.objects.all()
    return render(request,'cart.html',{'categ':categ})

def cart1(request):
    u=request.session.get('id')
    data=CartDB.objects.filter(user_id=u,status=0)
    s=CartDB.objects.filter(user_id=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'s':s})

def cartdata(request,id):
    if request.method=="POST":
        userid=request.session.get('id')
        quantity1=request.POST['amount']
        total1=request.POST['total']
        data = CartDB(user_id=Register.objects.get(id=userid),product_id=Product.objects.get(id=id),quantity=quantity1,total=total1)
        data.save()
    return redirect('cart1')

def cartremove(request,id):
    CartDB.objects.filter(id = id).delete()
    return redirect('cart1')

def checkout(request):
    u = request.session.get('id')
    data=CartDB.objects.filter(user_id=u,status=0)
    s = CartDB.objects.filter(user_id=u,status=0).aggregate(Sum('total'))
    return render(request,'checkout.html',{'data':data,'s':s})

def checkoutdata(request):
    if request.method=="POST":
        address1 = request.POST['address']
        city1    = request.POST['city']
        state1   = request.POST['state']
        country1 = request.POST['country']
        postal_zip1 = request.POST['zip']
        userid   = request.session.get('id')
        data=CartDB.objects.filter(user_id=userid,status=0)
        for i in data:
            checkout = CheckoutDB(user_id=Register.objects.get(id=userid),cart_id=CartDB.objects.get(id=i.id),address=address1,city=city1,state=state1,country=country1,postal_zip = postal_zip1)
            checkout.save()
        CartDB.objects.filter(user_id=userid,status=0).update(status = 1) 
        return redirect('userindex')
        

@csrf_exempt
def my_ajax_view(request):
    if request.method == "POST":
        id1 = request.POST.get("id")
        quantity1 = request.POST.get("quantity")
        total1 = request.POST.get("total")
        CartDB.objects.filter(id=id1).update(quantity = quantity1,total = total1)
        # Do something with the data
        response_data = {"message": "Received your data!"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "Invalid request."})
    

def contactform(request):
    if request.method=="POST":
        name1       = request.POST['name']
        email1    = request.POST['email']
        comment1   = request.POST['comment']  
        contact = ContactDB(name=name1,email=email1,comment=comment1)
        contact.save()
        return redirect('userindex')
 
@csrf_exempt    
def search(request):
    if request.method == "GET":
        value1 = request.POST.get("value")
        data = Product.objects.filter(Q(name__startswith=value1) | Q(category__startswith=value1))
        categ = Category.objects.all()
        # return redirect('products')
        return render(request,'product.html',{'data':data,'categ':categ})