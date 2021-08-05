from os import system, name
from time import sleep
def inventory():
    data= [
        {"id": 1001, "Info":"1001    Plain Ol' Cheese Pizza    Price   "+str(870), "Name":"Plain Ol' Cheese Pizza","Price":870},
        {"id": 1008, "Info":"1008    Veggie Pizza              Price   "+str(800), "Name":"Veggie Pizza","Price":800},
        {"id": 1003, "Info":"1003    Pepperoni Pizza           Price   "+str(900), "Name":"Pepperoni Pizza","Price":900},
        {"id": 1004, "Info":"1004    Meat-Lovers Pizza         Price   "+str(1200),"Name":"Meat-Lovers Pizza","Price":1200},
        {"id": 1009, "Info":"1009    Margherita Pizza          Price   "+str(850), "Name":"Margherita Pizza","Price":850},
        {"id": 1005, "Info":"1005    BBQ Chicken Pizza         Price   "+str(950), "Name":"BBQ Chicken Pizza","Price":950},
        {"id": 1002, "Info":"1002    Hawaiian Pizza            Price   "+str(850), "Name":"Hawaiian Pizza","Price":850},
        {"id": 1006, "Info":"1006    Chicken Ranch Pizza       Price   "+str(975), "Name":"Chicken Ranch Pizza","Price":975},
        {"id": 1007, "Info":"1007    Chicken Fajita Pizza      Price   "+str(950), "Name":"Chicken Fajita Pizza","Price":950}
        ]
    return data

# function that displays the inventory to the user

def userMenu(x):
    for each in x:
        print(each["Info"])

# function that clears the screen

def clear():
    if name == 'nt':
        _ = system('cls')

def quicksort(lst,check2):
    if len(lst)<=1:
        return lst
    # if check is l then it sorts from low to high 
    if check2=="l":
        p=lst.pop()
        gi,li=[],[]
        # get each item's dict from our inventory's list  
        for c in lst:
            # comparing the Price values of items
            if c["Price"]>p["Price"]:
                gi.append(c)
            else:
                li.append(c)
        # recursion returning the sorted list 
        return quicksort(li,check2)+[p]+quicksort(gi,check2)
    # if check is h then it sorts from high to low
    elif check2=="h":
        p=lst.pop()
        gi,li=[],[]
        # get each item's dict from our inventory's list  
        for c in lst:
            # comparing the Price values of items
            if c["Price"]<p["Price"]:
                gi.append(c)
            else:
                li.append(c)
        # recursion returning the sorted list 
        return quicksort(li,check2)+[p]+quicksort(gi,check2)

# linear search returns the index of dictionary of the item present in our inventory 

def linear_search(lst,item):
    for c in range(len(lst)):
        if lst[c]["id"]==item:
            return c
    return -1 

# dijkstra gives us the delivery path and time taken from our store to the user's area

def dijsktra(graph,start,end):
    lst_nodes=list(graph.keys())
    short_dist,visited,infinity={},[],9999
    for each_node in lst_nodes:
        if each_node==start:
            short_dist[each_node]=("", 0)
        else:
            short_dist[each_node]=("", infinity)                
    while len(visited)!=len(lst_nodes):
        lst=[]
        for value in short_dist.items(): 
            if value[0] not in visited:
                lst.append(value[1][1])
        min_d=min(lst)
        for key, value in short_dist.items():
            if min_d==value[1] and key not in visited:
                visited.append(key)
                for val in graph[key]:
                    temp=short_dist[key][1] + (val[1])
                    if temp<short_dist[val[0]][1]:
                        short_dist[val[0]]=(key,temp)
    path=[]
    x=""
    y=end
    while x!=start:
        x=short_dist[y][0]
        path.insert(0,(x,y))
        y=x
    time=0
    # calculates the total time taken that the rider will take to get the products to the user
    for each in path:
        time+=(short_dist[each[1]])[1]
    final=""
    # makes the path that the rider will take to get from DHA to the selected delivery area
    for tuple in path:
        for each in tuple:
            if each not in final:
                final+=each+" --> "
    print()
    print("==> The path from our store to your area is ",final[:-4],".")
    print()
    print("==> The time taken to reach your area will be  "+str(time)+" mins.")
    print()

# function that filters the inventory data, by either high or low using bubble sort

def filter():
    # print() statement for spacing
    print()
    # asks user if they would like to filter the prices
    check=input("Would you like to filter the prices? Y or N? ") 
    if check.lower()=="y":
        print()
        # if yes, then we ask if they would like to filter from low to high or high to low
        check2=input("To filter from low to high Enter L, Else H. ")
        if check2=="l":
            clear()
            # using bubble sort we will sort our inventory from low to high 
            x=quicksort(inventory(),check2)
            # display inventory 
            print("Prices filtered from low to high")
            print("ID      Model                   Price   PKR")
            userMenu(x)
        elif check2.lower()=="h":
            clear()
            # using bubble sort we will sort our inventory from low to high 
            x=quicksort(inventory(),check2)
            # display inventory 
            print("Prices filtered from high to low")
            print("ID      Model                   Price   PKR")
            userMenu(x)
    elif check.lower()=="n":
        # if they do not want to filter we pass
        pass

# function that adds selected items to cart 

def add(cart):
    # asks user for the item that they would like to add to cart
    item=int(input("Enter the id of the item you would like to add: "))
    # we get the index of our dictionary from the list 
    position=linear_search(inventory(),item)
    # check for if index in list 
    if position!=-1:
        # ask for the required quantity of the item
        qnty=int(input("Kindly enter the quantity of the item: "))
        if qnty>0:
       
            #it adds the to the cart with the set quantity and their total price
            price=(inventory()[position])["Price"]*qnty
            name=(inventory()[position])["Name"]
            cart[(inventory()[position])["id"]]=[name,qnty,price]
            print("Item added to cart!")
        else:
            print('Invalid quantity entered!')
    else:
        # if id not in inventory then it outputs an error msg
        print("Enter a valid id to add!")

# function deletes the selected item from the cart 

def remove(cart):
    # displays cart to user 
    viewcart(cart)
    # inputs for the item id to be removed  
    item=int(input("Enter the item id that you would like to remove: "))
    # checks if item is present in cart
    if item in cart.keys():
        # inputs the quantity of that item to be removed
        qnty=int(input("Also enter the quantity that you would like to remove: "))
        # if the cart quantity matches the entered quantity 
        if cart[item][1]==qnty or cart[item][1]==1:
            # deletes that item from cart  
            del(cart[item])
        # else if quantitiy does not match the items quantity in cart then it tells the user to enter a valid quantity  
        elif cart[item][1]<qnty:
            print("Entered quantity doesn't exist, enter a valid quantity to remove!")
        # else, then it removes the set quantity from the cart 
        else:
            # removing item from cart
            intial=cart[item][1]
            cart[item][1]=(cart[item][1])-qnty
            cart[item][2]=(cart[item][2])-((cart[item][2]/intial)*qnty)
        print("Item removed from cart!")
    else:
        # if id not present in cart prompts the user to enter a valid id 
        print("Enter a valid id to remove!") 

# fucnion that displays the cart to the user 
   
def viewcart(cart):
    print("ID   Name                       Quantity    Price")
    for key, value in cart.items():
        print(str(key)+" "+value[0]+"         "+str(value[1])+"           "+str(value[2]))

# fucntion that displays the total bill 
def checkout(cart):
    total=0
    # sums up all the prices of items present in our cart 
    for key, value in cart.items():
        total+=value[2]
    viewcart(cart)
    print()
    # displays the receipt
    print("===================================================")
    print("Total:                                      ",total)
    print("===================================================")
    # if the total is < or =  0 it means that there is no item in cart, so it prompts the user that they can not proceed to checkout 
    if total<=0:
        print()
        print("Your cart is empty, you can not proceed to checkout!")
        print()

# funciton that displays the delivery time and the fastest route that the rider will take   
def location():
    # dicionary of areas that we deliver to 
    areas={
            1:"DHA",
            2:"Bahadrabad",
            3:"Clifton",
            4:"Cantt",
            5:"Saddar",
            6:"Nazimabad",
            7:"Saki Hassan",
            8:"Garden",
            9:"North Nazimabad",
            10:"North Karachi"
    }
    # connnections of our delivery areas
    links={
          "DHA" : [("Bahadurabad",22), ("Clifton",12),("Cantt",12)],
          "Bahadurabad" : [("Sakhi Hassan",19), ("Saddar",9),("DHA",20)],
          "Clifton" : [("Saddar",12), ("Cantt",10), ("Garden",20), ("DHA",11)],
          "Cantt" : [("DHA",14), ("Clifton",11), ("Saddar",8)],
          "Saddar" : [("Clifton", 14), ("Cantt",7), ("Bahadurabad",14), ("North Nazimabad",25), ("Nazimabad",18), ("Garden",9)],
          "Nazimabad" : [("North Nazimabad",10), ("North Karachi",17),("Saddar",20)],
          "Sakhi Hassan":[("Bahadurabad",21)],
          "Garden":[("Clifton",18),("Saddar",9)],
          "North Nazimabad":[("Nazimabad",11)],
          "North Karachi":[("Nazimabad",18)]
    }
    # asks the user to select their delivery area
    print("""
    Our Store is located in DHA and below are the available delivery options
    Delivery options
    ================================
    1:"DHA",
    2:"Bahadurabad",
    3:"Clifton",
    4:"Cantt",
    5:"Saddar",
    6:"Nazimabad",
    7:"Sakhi Hassan",
    8:"Garden",
    9:"North Nazimabad",
    10:"North Karachi"
    """)
    choice=int(input("Kindly choose your residential area : "))
    print("-----------------------------------")
    # checks if the selected choice is present in our areas
    if choice in areas.keys():
        # if areas is no.1 then it is the same area as our store
        if choice==1:
            print("==> Our Store is located in your area.")
            print() 
            print("==> The time taken to reach your area will be  "+str(5)+" mins.")
            print()
        else:
            # calls the dijkstra function to display rider path and time taken 
            dijsktra(links,"DHA",areas[choice])
        print("-----------------------------------")
    else:
        # if area not present in dict then it prompts the user and calls the location function again
        print("You have entered an invalid choice, kindly enter again!")
        location()  

# function that has all the commands that we can make to our shopping cart

def shoppingCart():
    # displays the available options to the user 
    print("""
    Shopping basket options
    ================================
    1: Add item 
    2: Remove item
    3: View cart
    0: Proceed to checkout
    """)
    cart={}
    # inputs the choice from the user 
    choice=int(input("Kindly choose your choice: "))
    print("----------------------------")
    # calls the function according to the set choice 
    while True:
        if choice==1:
            add(cart)
        elif choice==2:
            remove(cart)
        elif choice==3:
            viewcart(cart)
        elif choice==0:
            clear()
            location()
            print("==> This is the final receipt")
            print("-----------------------------------")
            checkout(cart)
            # breaks this loop once checkout is called 
            break
        print()
        choice=int(input("Kindly choose your choice: "))
        print("----------------------------")

# main funciton that runs the whole code 
            
def main():
    # displays welcome msg
    print("""
    ==================================================
        
          Welcome to Habib Pizzeria Terminal     
        
    ==================================================
    """)
    sleep(2)
    clear()
    # displays the available products
    print("These are the available products.")
    print()
    print("****************")
    print()
    print("ID      Flavours                   Price   PKR")
    userMenu(inventory())
    print()
    print("****************")
    filter()
    # after displaying it calls the shopping cart function
    shoppingCart()
    # asks if there is a new user or would they like to exit
    OK=input("TYPE Enter for a new user or End to end program: ")
    if OK.lower()=="enter":
        # if enter then it clears the screen and run the main() function again
        clear()
        main()
    elif OK.lower()=="exit":
        # if exit() it exits the code
        exit()
    else:
        print ('Enter a valid input')
        OK=input("TYPE Enter for a new user or End to end program: ")
    

# call the main function    
main()