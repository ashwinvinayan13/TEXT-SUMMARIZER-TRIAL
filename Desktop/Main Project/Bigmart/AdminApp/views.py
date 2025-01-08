from django.shortcuts import render, redirect
from AdminApp.models import CategoryDB, ProductDB
from WebApp.models import ContactDB, RegisterDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib import messages



def index(request):
    caategories = CategoryDB.objects.count()
    products = ProductDB.objects.count()
    date = datetime.now()
    return render(request, 'index.html', {'categories': caategories, 'products':products, 'date':date})

def AddCategory(request):
    return render(request, 'AddCategory.html')


def Save_Category(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        des = request.POST.get('description')
        ima = request.FILES['image']
        obj = CategoryDB(Name=nam, Description=des, Image=ima)
        obj.save()
        messages.success(request, "Category Saved succesfully...")
        return redirect(AddCategory)

def Display_Category(request):
    data = CategoryDB.objects.all()
    return render(request, 'DisplayCategory.html', {'data': data})


def Edit_Category(request, pro_id):
    data = CategoryDB.objects.get(id=pro_id)
    return render(request, 'EditCategory.html', {'data': data})

def Update_Category(request, pro_id):
    if request.method == 'POST':
        nam = request.POST.get('name')
        des = request.POST.get('description')
        try:
            ima = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(ima.name, ima)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=pro_id).Image
        CategoryDB.objects.filter(id=pro_id).update(Name=nam, Description=des, Image=file)
        messages.success(request, "Category Updated Succesfully....")
        return redirect(Display_Category)

def Delete_Category(request, pro_id):
    x = CategoryDB.objects.filter(id=pro_id)
    x.delete()
    messages.error(request, "Category deleted Succesfully")
    return redirect(Display_Category)



def AddProducts(request):
    name = CategoryDB.objects.all
    return render(request, 'AddProducts.html', {'name': name})


def Save_Products(request):
    if request.method == 'POST':
        nam = request.POST.get('category_name')
        pro = request.POST.get('product_name')
        pri = request.POST.get('price')
        des = request.POST.get('description')
        qua = request.POST.get('quantity')
        ima = request.FILES['image']
        obj1 = ProductDB(Name=nam, Product=pro, Price=pri, Description=des, Quantity=qua, Image=ima)
        obj1.save()
        return redirect(AddProducts)


def Display_Products(request):
    data = ProductDB.objects.all()
    return render(request, 'Display_Products.html', {'data': data})



def EditProduct(request, pro_id):
    data = ProductDB.objects.get(id=pro_id)
    Name = CategoryDB.objects.all()
    return render(request, 'EditProduct.html', {'data': data, 'Name': Name})

def UpdateProduct(request, pro_id):
    if request.method == 'POST':
        nam = request.POST.get('category_name')
        pro = request.POST.get('product_name')
        pri = request.POST.get('price')
        des = request.POST.get('description')
        qua = request.POST.get('quantity')
        try:
            ima = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(ima.name, ima)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=pro_id).Image
        ProductDB.objects.filter(id=pro_id).update(Name=nam, Product=pro, Price=pri, Description=des, Quantity=qua,
                                                   Image=file)
        messages.success(request, "Product Updated Succesfully......")
        return redirect(Display_Products)


def DeleteProduct(reqeust, pro_id):
    x = ProductDB.objects.filter(id=pro_id)
    x.delete()
    return redirect(Display_Products)


def Admin_login_page(request):
    return render(request, 'Admin_login_page.html')

def Admin_login(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        pas = request.POST.get('pass')
        if User.objects.filter(username__contains=nam).exists():
            x = authenticate(username=nam, password=pas)
            if x is not None:
                login(request, x)
                request.session['username'] = nam
                request.session['password'] = pas
                messages.success(request, "Welcome to Bigmart admin dashboard.....!")
                return redirect(index)
            else:
                messages.warning(request, "Invalid Password")
                return redirect(Admin_login_page)
        else:
            messages.warning(request, "Invalid Username")
            return redirect(Admin_login_page)


def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Admin_login_page)

def View_Contact(request):
    contact = ContactDB.objects.all()
    return render(request, 'View_Contact.html', {'contact':contact})


def Delete_Contact(request, p_id):
    x = ContactDB.objects.filter(id=p_id)
    x.delete()
    return redirect(View_Contact)


def View_Message(request):
    data = RegisterDB.objects.all()
    return render(request, 'View_Message.html', {'data':data})


def Delete_Message(request, p_id):
    x = RegisterDB.objects.filter(id=p_id)
    x.delete()
    return redirect(View_Message)
