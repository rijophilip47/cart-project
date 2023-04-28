from django.shortcuts import render,redirect
from .models import *
from userapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    category = Category.objects.all().count()
    product  = Product.objects.all().count()
    user     = Register.objects.all().count()
    orders   = CheckoutDB.objects.all().count()
    message  = ContactDB.objects.all().count()
    return render(request,'adminindex.html',{'category':category,'product':product,'user':user,'orders':orders,'message':message})

def categoryform(request):
    return render(request,'categoryform.html')

def categorytable(request):
    data = Category.objects.all()
    return render(request,'categorytable.html',{'data':data})

def category(request):
    if request.method == 'POST':
        name1 = request.POST['name2']
        desc   = request.POST['description2']
        image1 = request.FILES['image2']
        
        data = Category(name = name1,description = desc,image = image1)
        
        data.save()
        
        return redirect('categorytable') 
    
def editcategoryform(request,id):
    data = Category.objects.filter(id = id)
    return render(request,'categoryedit.html',{'data':data})

def editcategory(request,id):
    if request.method == 'POST':
        name1 = request.POST['name2']
        desc   = request.POST['description2']
        try:
            img_c = request.FILES['image2']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).image
        Category.objects.filter(id=id).update(name = name1,description = desc,image = file)
        return redirect('categorytable')


def deletecategory(request,id):
    Category.objects.filter(id = id).delete()
    return redirect('categorytable')

def productform(request):
    data = Category.objects.all()
    return render(request,'productform.html',{'data':data})

def product(request):
    if request.method == 'POST':
        name1 = request.POST['name2']
        desc   = request.POST['description2']
        price1   = request.POST['price2']
        category1 = request.POST['category2']
        image1 = request.FILES['image2']
        
        data = Product(name = name1,description = desc,price = price1,image = image1,category = category1)
        
        data.save()
        
        return redirect('producttable') 
    
    
def producttable(request):
    data = Product.objects.all()
    return render(request,'producttable.html',{'data':data})

def editproductform(request,id):
    data      = Product.objects.filter(id = id)
    datacateg = Category.objects.all()
    return render(request,'productedit.html',{'data':data,'categ':datacateg})

def editproduct(request,id):
    if request.method == 'POST':
        name1 = request.POST['name2']
        price1 = request.POST['price2']
        desc   = request.POST['description2']
        category1   = request.POST['category2']
        try:
            img_c = request.FILES['image2']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).image
        Product.objects.filter(id=id).update(name = name1,description = desc,price = price1,category = category1, image = file)
        return redirect('producttable')
    
def deleteproduct(request,id):
    Product.objects.filter(id = id).delete()
    return redirect('producttable')

def loginuser(request):
    return render(request,'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})

def messages(request):
    data = ContactDB.objects.all()
    return render(request,'messages.html',{'data':data})
    
    
    