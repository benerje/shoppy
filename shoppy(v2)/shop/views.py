from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact, Ordercheckout, Order
from math import ceil
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .filters import OrderFilter
from django.contrib.auth.models import User


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ShopHome')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'shop/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('ShopHome')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('Login')

    context = {'form': form}
    return render(request, 'shop/register.html', context)


def index(request):
    products = Product.objects.all()
    allProds = []
    # retrive category and id values in all items(array)
    catProds = Product.objects.values('category', 'id')
    cats = {item['category']
            for item in catProds}  # give the values of categories

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 * ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thanks = True
        return render(request, 'shop/contact.html', {'thanks': thanks})
    return render(request, 'shop/contact.html')


def searchMatch(query, item):
    if query.lower() in item.product_name.lower() or query.lower() in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":

        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        username = request.POST.get('username', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " "+request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Ordercheckout(items_json=items_json, amount=amount, username=username, name=name, email=email, address=address,
                              city=city, state=state, zip_code=zip_code, phone=phone)

        order.save()
        thank = True
        id = order.order_id

        username = request.user.username
        return render(request, "shop/checkout.html", {'thank': thank, 'id': id, 'username': username})

    return render(request, 'shop/checkout.html')


def orders(request):
    username1 = request.user.username
    catProds = Ordercheckout.objects.filter(username=username1)

    x = catProds.values('items_json', 'amount', 'date_created')
    import datetime
    orders = []
    for orderitem in x:
        orders.append(orderitem)
    orders.reverse()
    context = {'orders': orders}
    return render(request, 'shop/orders.html', context)

# dashboard views


def dashboard(request):
    order_status = Order.objects.all()
    order_count = order_status.count()
    order_delivered_count = order_status.filter(status="Delivered").count()
    order_pending_count = order_status.filter(status="Pending").count()
    order_delivered = order_status.filter(status="Delivered")

    details = Ordercheckout.objects.all()
    users = User.objects.values('username', 'email')

    prods = Ordercheckout.objects.values("items_json", "date_created",)

    user = Order.objects.values('ordercheckout__username')

    myFilter = OrderFilter(request.GET, queryset=users)
    myFilter1 = OrderFilter(request.GET, queryset=details)
    users = myFilter.qs
    details = myFilter1.qs

    context = {'myFilter': myFilter, 'users': users, 'details': details, 'order_count': order_count, 'order_delivered_count':
               order_delivered_count, 'order_pending_count': order_pending_count}

    return render(request, 'dashboard/dashboard.html', context)
