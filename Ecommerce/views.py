from django.shortcuts import render, redirect
from commE.models import Profile,Product,Cart,Order,OrderItem
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import random
from django.contrib import messages

def home(request):
    return render(request,'home.html') 

def main(request):
    return render(request,'main.html')


def login_call(request): 
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        Currentuser = authenticate(username=username,password=password)
        if Currentuser:
            login(request, Currentuser)
            return redirect('/main')
        else:
            return redirect('/signup')
    return render(request,'loginpage.html')



def logout_call(request):
    logout(request)
    return redirect('/login')

def signup(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        mobile=request.POST['mobile']
        email=request.POST['email']
        psw=request.POST['psw']
        pswrepeat=request.POST['pswrepeat']

        u = User(first_name=fullname, username=email, email=email, password=pswrepeat)
        u.save()
        p = Profile(user=u, mobile=mobile)
        p.save()
        
        print("SAVED!!!")
        return redirect('/login')

    return render(request,'register.html')

def productdetail(request,id):
    obj = Product.objects.filter(pk=id).first()
    if obj==None:
        return redirect('/home')
    return render(request,'productdetail.html',{"data":obj})



def testimonial(request):
    return render(request,'testimonial.html')

def about(request):
    return render(request,'about.html')

def blog_list(request):
    return render(request,'blog_list.html')

def contact(request):
    return render(request,'contact.html')

def checkout(request):
    return render(request,'checkout.html')


def products(request):
    if(request.method=="POST"):
        search = request.POST.get("search","")
        obj = Product.objects.filter(name__icontains=search).all()
    else:
        obj = Product.objects.all()
    
    return render(request,'products.html',{"data":obj})

@login_required(login_url='/login/')
def add_to_cart(request,pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    cart = Cart()
    cart.product = product
    cart.user = user
    cart.save()

    return redirect('/viewcart/')


@login_required(login_url='/login/')
def viewcart(request):
    user = request.user
    cart_item = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_item})


@login_required(login_url='/login/')
def editcart(request,id):
    cart_item = Cart.objects.get(id=id)
    action = request.GET.get("action",'')
    quantity = int(cart_item.quantity)
    if(action=='increase'):
        cart_item.quantity = quantity+1
        cart_item.save()
    elif(action=='decrease'):
        if(quantity==1):
            cart_item.delete()
        else:
            cart_item.quantity = quantity-1
            cart_item.save()
    # cart_item.quantity = str(int(cart_item.quantity)+1)
    # print(id,action)
    return redirect('/viewcart/')


@login_required(login_url='/login/')
def checkout(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    total = 0
    for x in cart:
        total += (int(x.product.price)*(x.quantity))
        
    
    return render(request,'checkout.html',{"data":cart,"total":total})

def placeorder(request):
    if request.method =='POST':
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.price*item.quantity


        neworder = Order()
        neworder.fname=request.POST.get('fname','')
        neworder.lname=request.POST.get('lname','')
        neworder.username=request.POST.get('username','')
        neworder.email=request.POST.get('email','')
        neworder.address=request.POST.get('address','')
        neworder.country=request.POST.get('country','')
        neworder.state=request.POST.get('state','')
        neworder.zip=request.POST.get('zip','')
        neworder.card_holder_name=request.POST.get('card_holder_name','')
        neworder.card_number = request.POST.get("card_number",'')
        neworder.card_expiration_date=request.POST.get('card_expiration_date','')
        neworder.card_cvv=request.POST.get('card_cvv','')
        neworder.total_price=request.POST.get('total_price','')
        neworder.payment_mode=request.POST.get('paymentMethod','')
        neworder.payment_id=request.POST.get('payment_id','123456')
        

        neworder.total_price = cart_total_price
        trackno = 'nayra'+str(random.randint(1111111,9999999))
        
        neworder.tracking_no=trackno    
        neworder.save()

        print(neworder,"neworder")

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            x = OrderItem.objects.create(order=neworder, product=item.product, price=item.product.price, quantity = item.quantity)
            x.save()
            

        # to dec the qtty
        # orderproduct = Product.objects.filter(id=item.product.id).first()
        # orderproduct.quantity = orderproduct.quantity - item.quantity
        # orderproduct.save()

        #to clear cart 
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, "your order has been placed successfully")

        # return render(request,'checkout.html',{"orderitems":neworderitems})
    return redirect("/home")

    
    
    
    
    
    

