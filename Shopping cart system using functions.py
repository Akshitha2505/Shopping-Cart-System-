user = {}

products = {
    1: {"name": "laptop", "price": 50000, "stock": 5},
    2: {"name": "mobile", "price": 20000, "stock": 10},
    3: {"name": "headphones", "price": 2000, "stock": 15}
}

cart = {}
orders = []

#----------------MAIN MENU------------------

def main_menu():
    while True:
        print('----WELCOME TO SHOPPING CART SYSTEM----')
        print('---MAIN MENU---')
        print('1.ADMIN LOGIN')
        print('2.USER REGISTRATION')
        print('3.USER LOGIN')
        print('4.EXIT')
        
        choice=input('ENTER YOUR CHOICE:')
        if choice=='1':
            admin_login()
        elif choice=='2':
            user_register()
        elif choice=='3':
            user_login()
        elif choice=='4':
            print('---Shop Closed---')
            break
        else:
            print('Please choose the correct option')

#----------ADMIN LOGIN---------------------

def admin_login():
    username=input('username:')
    password=input('password:')
    if username=='admin' and password=='1234':
        print('login succuess')
        admin_dashboard()
    else:
        print('invalid login credentials')
        
#---------------ADMIN MENU-----------------

def admin_dashboard():
    while True:
        print('---ADMIN DASHBOARD---')
        print('1.ADD PRODUCT')
        print('2.VIEW PRODUCT')
        print('3.UPDATE PRODUCT')
        print('4.DELETE PRODUCT')
        print('5.SEARCH PRODUCT')
        print('6.VIEW USERS')
        print('7.VIEW ORDERS')
        print('8.LOGOUT')
        
        ch=int(input('Enter your operation:'))
        if ch==1:#add product
            add_product()     
        elif ch==2:#veiw product
            view_product()
        elif ch==3:#update product
            update_product()
        elif ch==4:#delete product
            delete_product()
        elif ch==5:#search product
            search_product()
        elif ch==6:#view user
            view_user()
        elif ch==7:#view orders
            view_orders()
        elif ch==8:#logout-----need to get the main menu but it is asking again username and passsword
            print('---Admin Logged out---')
            return
        else:#invaild
            print('Invalid choice')
            
#----------ADD PRODUCT------------------
            
def add_product():#DONE
    n=int(input('Enter how many number of products u want to add:'))
    for i in range(0,n):
        product_id=len(products)+1
        name=input('Enter Product Name:')
        price=float(input('Enter Product Price:'))
        stock=int(input('Enter Stock:'))

        products[product_id]={'name':name,'price':price,'stock':stock}
    print('Products added successsfully')
    #admin_dashboard()
    
#-------------VEIW PRODUCTS-------------
    
def view_product():#DONE
    print('----PRODUCTS----')
    if len(products)==0:
        print('No Products Available')
        return
    for product_id,product in products.items():
        print("ID:", product_id,
              "Name:", product["name"],
              "Price:", product["price"],
              "Stock:", product["stock"])
    #admin_dashboard()
        
#-------------UPDATE PRODUCTS-----------
        
def update_product():#DONE
    view_product()
    n=int(input('Enter how many products u want to update:'))
    for i in range(0,n):
        product_id=int(input('Enter product ID:'))
        if product_id in products:
            products[product_id]['name']=input('Enter Product Name:')
            products[product_id]['price']=input('Enter Product price:')
            products[product_id]['stock']=input('Enter Product stock:')

            print('Products updated successfully')
        else:
            print('Product Not Found')
    #admin_dashboard()

#--------------DELETE PRODUCT--------------
            
def delete_product():
    view_product()
    n=int(input('Enter how many products u want to delete:'))
    for i in range(0,n):
        product_id=int(input('Enter Product Id:'))
        if product_id in products:
            del products[product_id]
            print('products deleted Successfully')
            admin_dashboard()
        else:
            print('product id not found')
            view_product()
            
#------------SEARCH PRODUCT---------------
            
def search_product():#getting not found anii 3 times vasthundhii
    product_name=input('Enter product name:')
    for product_id, product in products.items():
        if product_name.lower() in product["name"].lower():
            print('product ID:',product_id)
            print('product Name:',product["name"])
            print('price:',product["price"])
            print('Stock:',product["stock"])
            return
    else:
        print('Product Not Found')
    #admin_dashboard()

#-----------VEIW USER----------------------
            
def view_user():
    if len(user)==0:
        print('No registered User')
        return
    else:
        print('Name:',user['name'])
        print('Email:',user['mail'])
        print('Mobile No:',user['mbl']) 
    #admin_dashboard()

#-----------VEIW ORDERS----------------------
        
def view_orders():
    if len(orders)==0:
        print('No Orders Available')  
        return
    for i in orders:
        print(i)        
    #admin_dashboard()

#-----------USER REGISTER---------------------

def user_register():
    global user
    user['name']=input('Name:')#registration
    user['mail']=input('Email:')
    user['password']=input('password:')
    user['mbl']=input('phone:')
    
    if len(user['password'])<6:
        print('password must contain atleast 6 characters:')
        return
    elif len(user['mbl'])!=10 or not user['mbl'].isdigit():
        print('phone no must contain exactly 10 digits')
        return
    else:
        print('Registration Successful')   
    #main_menu()

#-----------USER LOGIN----------------------

def user_login():
    if len(user)==0:
        print('please Rigister ')
        return
        user_register()
    email=input('Email:')
    password=input('password:')
    if email ==user['mail'] and password==user['password']:
        print('login successful')
        print('Welcome',user['name'])
        user_dashboard()
    else:
        print('Incorrect Email/password')
    #main_menu()

#-----------USER MENU----------------------
        
def user_dashboard():
    while True:
        print('---USER DASHBOARD---')
        print('1.VIEW PRODUCTS')
        print('2.SEARCH PRODUCTS')
        print('3.ADD TO CART')
        print('4.VIEW CART')
        print('5.REMOVE PRODUCT')
        print('6.UPDATE QUANTITY')
        print('7.CHECKOUT')
        print('8.ORDER HISTORY')
        print('9.LOGOUT')
        ch=int(input('Select your operation:'))
        if ch==1:#view product
            view_product()
        elif ch==2:#search product
            search_product()
        elif ch==3:#add to cart
            add_to_cart()
        elif ch==4:#view cart
            view_cart()
        elif ch==5:#remove product
            remove_product_from_cart()
        elif ch==6:#update quantity
            update_quantity()
        elif ch==7:#checkout
            checkout()
        elif ch==8:#order history
            order_history()
        elif ch==9:#logout--------------need to get the main menu but it is asking again email and passsword
            print('---User Logged Out--')
            return
        else:#invalid operation
            print('Invalid Selection')
            
#-----------ADD TO CART----------------------

def add_to_cart():
    view_product()
    n=int(input('Enter how many products u want to Add:'))
    for i in range(0,n):
        product_id=int(input('Enter the Product ID:'))
        if product_id not in products:
            print('Product Not Available')
            return
        quantity=int(input('Enter the quantity u want:'))
        if quantity<=0:
            print('Invalid Quantity')
            return
        if quantity > products[product_id]['stock']:
            print('Out off Stock')
            return
        if product_id in cart:
            cart[product_id]+=quantity
        else:
            cart[product_id]=quantity   
        print(products[product_id]['name'] ,'added to cart' )          
    #user_dashboard()
    
#-----------VEIW CART----------------------

def view_cart():
    if len(cart)==0:
        print('cart is empty')
        return
    total=0
    for product_id,quantity in cart.items():
        product=products[product_id]
        amount=product['price']*quantity

        print(product['name'],'X',quantity,'=',amount)
        
        total+=amount
        print('='*20)
    print('Total amount:',total)
    #user_dashboard()
    
#-----------REMOVE PRODUCT FROM CART----------------------

def remove_product_from_cart():
    if len(cart)==0:
        print('cart is Empty')
        return
    view_cart()
    n= int(input('Enter how many u want to remove from cart:'))
    view_product()
    for i in range(0,n):
        product_id=int(input('Enter Product ID:'))
        if product_id in cart:
            del cart[product_id]
            print('product Removed from cart ')
        else:
            print('product not found in cart')
            
#-----------UPDATE QUANTITY---------------------

def update_quantity():
    if len(cart)==0:
        print('No products in cart')
        return
    view_product()
    product_id=int(input('Enter Product ID:'))
    if product_id not in products:
        print('Product Not found')
        return
    quantity=int(input('Enter the Quantity:'))
    if quantity<=0:
        print('Invalid quantity')
        return
    if quantity>products[product_id]['stock']:
        print('Not Enough stock ')
        return
    cart[product_id]=quantity
    print('quantity updated succesfully')
    #user_dashboard()
    
#-----------CHECK OUT-------------------------

def checkout():
    if len(cart)==0:
        print('cart is Empty')
        return
    total=0
    
    for product_id,quantity in cart.items():
        product=products[product_id]
        amount=product['price']*quantity
        
        print(product['name'],'X',quantity,'=',amount)
        
        total+=amount
    print('-'*20)
    print('Total Bill:',total)
    #view_cart()
    
    payment=input('Confirm your payment yes/no:')
    if payment.lower()=='yes':
        for product_id, quantity in cart.items():
            products[product_id]["stock"] -= quantity
            
        order = {
            "customer": user["name"],
            "items": cart.copy(),
            "total": total
        }
        orders.append(order)
        
        cart.clear()
        
        print("\nPayment Successful")
        print("Order Placed Successfully")        
    else:
        print('Order Cancelled')
        
#-----------ORDER HISTORY----------------------

def order_history():
    print('----Order History----')
    for order in orders:
        if order["customer"] == user["name"]:
            print("\nCustomer:", order["customer"])
            print("Items:", order["items"])
            print("Total:", order["total"])
            return
        else:
            print("No Orders Found")
            
#-----------Program start from here------------

main_menu()
