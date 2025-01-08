from django.shortcuts import render, redirect
from AdminApp.models import CategoryDB, ProductDB
from WebApp.models import ContactDB, RegisterDB, CartDb, OrderDB
from django.contrib import messages
import razorpay

# Create your views here.



def HomePage(reqeust):
    category = CategoryDB.objects.all()
    cou = CartDb.objects.filter(Username=reqeust.session['Name'])
    x = cou.count()
    return render(reqeust, 'home.html', {'category': category, 'x': x})


def About(request):
    category = CategoryDB.objects.all()
    return render(request, 'About.html', {'category': category})

def Contact(request):
    category = CategoryDB.objects.all()
    return render(request, 'Contact.html', {'category': category})


def Save_Contact(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        ema = request.POST.get('email')
        sub = request.POST.get('subject')
        tex = request.POST.get('text')
        obj = ContactDB(Name=nam, Email=ema, Subject=sub, Message=tex)
        obj.save()
        return redirect(Contact)


def All_Products(request):
    products = ProductDB.objects.all()
    category = CategoryDB.objects.all()
    return render(request, 'All_Products.html', {'products': products}, {'category': category})


def Filter_Products(request, ct_name):
    pro = ProductDB.objects.filter(Name=ct_name)
    return render(request, 'Filtered_Products.html', {'pro': pro})

def Single_Product(request, p_id):
    eta = ProductDB.objects.get(id=p_id)
    return render(request, 'Single_Products.html', {'eta': eta})

def User_registration(request):
    return render(request, 'User_Registration.html')


def User_Login(request):
    return render(request, 'User_Login.html')


def Save_User(request):
    if request.method=="POST":
        nam = request.POST.get("user")
        ema = request.POST.get("email")
        mob = request.POST.get("mobile")
        pas = request.POST.get("password")
        cpa = request.POST.get("passwo")
        obj = RegisterDB(Name=nam, Email=ema, Phone=mob, Password=pas, CPassword=cpa)
        obj.save()
        return redirect(User_registration)

def user_login(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        psw = request.POST.get("upass")
        if RegisterDB.objects.filter(Name=un, Password=psw).exists():
            request.session['Name'] = un
            request.session['Password'] = psw
            messages.success(request, "Welcome")
            return redirect(HomePage)
        else:
            return redirect(User_Login)
    else:
        return redirect(User_Login)


def User_Logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "logged Out Succesfully")
    return redirect(User_Login)

def Cart(request):
    sub_total = 0
    shipping = 0
    cat = CategoryDB.objects.all()
    data = CartDb.objects.filter(Username=request.session['Name'])
    for i in data:
        sub_total += i.TotalPrice
        if sub_total > 750:
            shipping = 100
        else:
            shipping = 300
        total = sub_total + shipping
    return render(request, "cart.html", {'category': cat, 'data': data, 'sub_total': sub_total, 'total': total, 'shipping': shipping})
def SaveCart(request):
    if request.method == 'POST':
        use = request.POST.get('uname')
        pna = request.POST.get('pname')
        tot = request.POST.get('total')
        pri = request.POST.get('price')
        qua = request.POST.get('quantity')

        try:
            x = ProductDB.objects.get(Product=pna)
            img = x.Image
        except ProductDB.DoesNotExist:
            img = None
        obj = CartDb(Username=use, ProductName=pna, Quantity=qua, Price=pri, TotalPrice=tot, Pro_Image=img)
        obj.save()
        return redirect(HomePage)


def Delete_cart(request, cr_id):
    x = CartDb.objects.filter(id=cr_id)
    x.delete()
    return redirect(Cart)


def Checkout(request):
    sub_total = 0
    shipping = 0
    cat = CategoryDB.objects.all()
    data = CartDb.objects.filter(Username=request.session['Name'])
    for i in data:
        sub_total += i.TotalPrice
        if sub_total > 750:
            shipping = 100
        else:
            shipping = 300
        total = sub_total + shipping
    return render(request, 'Checkout.html', {'data': data, 'cat': cat, 'total': total, 'sub_total': sub_total, 'shipping': shipping})


def Save_order(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        ema = request.POST.get('email')
        pla = request.POST.get('place')
        add = request.POST.get('address')
        mob = request.POST.get('mobile')
        sta = request.POST.get('state')
        pin = request.POST.get('pin')
        tot = request.POST.get('total')
        mes = request.POST.get('text')
        obj = OrderDB(Name=nam, Email=ema, Place=pla, Address=add, Mobile=mob, State=sta, Pin=pin, TotalPrice=tot, Message=mes)
        obj.save()
        return redirect(Getaway)


def Getaway(request):
    customer = OrderDB.objects.order_by('-id').first()
    payy = customer.TotalPrice
    amount = int(payy*100)
    payy_str = str(amount)

    if request.method == 'POST':
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_bXPA97UanCNNtB', 'uaPIIR1QDGt9zmco69tRe1DZ'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request, 'payment_getaway.html', {'customer': customer, 'payy_str': payy_str})
