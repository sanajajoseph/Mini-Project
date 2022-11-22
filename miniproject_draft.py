
                            #for communicating with Database
import pymysql
import os
from dotenv import load_dotenv



                                #for defining the main menu
mn_menu = ["MAIN MENU","==========", "[1]. Products Menu ","[2]. Orders Menu",\
    "[3]. Courier Menu","[0]. Exit"] 

                                #for defining the Product menu    
prd_menu = ["\n PRODUCT MENU","=================","[1] Display the product list",\
    "[2] Add the product to list","[3] Update the product","[4] Delete product","[0] Back" ]

                                #for defining the Orders menu    
ord_menu = ["\n ORDERS MENU","================","[1].Display order dictionary","[2].Add Customer details",\
            "[3].Update existing order status","[4].Update existing order","[5].Delete order","[0].Back" ] 

                                #for defining the Couriers menu             
cour_menu = ["\nCOURIERS MENU","=================","[1].Display Courier List","[2].Create new Courier",\
            "[3].Update existing Courier","[4].Delete Courier","[0].Back" ]        
                   
product_keys = ['id','Item','price']
ord_stat_keys = ['id','order_status']
ord_keys = ['id','customer_name','customer_address','customer_phone','items','courier','status']
cour_keys =['id','cour_name','cour_phone']


                                #Function for displaying both menus and list of product, order, courier
def display_fn(curs,keys,tbl,ls_idfr):
    if keys != 0:
        curs.execute('SELECT * FROM ' + tbl)
        curs = curs.fetchall()
    for i in curs:
        print(i)
    if ls_idfr != 0:
        input("\nPress ENTER to return menu. ") 


                                #Function for adding list of product, order, courier        
def add_fn(curs,keys):
    value = []
    for k in keys:
        if k == 'items':
            display_fn(curs,product_keys,'product_list',0)
            optn = ''
            prd_ids = []
            while optn !='0':
                prd_id = input('Please enter the product id for ordering, 0 for checkout:')
                optn = str(prd_id)
                if optn != '0':
                    prd_ids.append(prd_id)
            str_ids = ''
            for i,id in enumerate(prd_ids):
                if i == 0:
                    str_ids = str_ids + str(id)
                else:
                    str_ids = str_ids+ ',' + str(id)
            value.append(str_ids)
            
        elif k == 'courier':
             display_fn(curs,cour_keys,'courier_list',0)
             print('\n\nPlease select a courier id from the list:')
             value.append(input())
        elif k == 'status':
            value.append(1)
        elif k != 'id':
            print("\n Please enter the new",k,":")
            value.append(str(input()) )
        else :
            print("Invalid option. please enter valid value")    
    print("\n Added",value)
    if keys[1] == 'Item':
        curs.execute("INSERT INTO product_list (Item,price)" "VALUES (%s, %s)", (value[0],value[1]))
    elif keys[1] == 'customer_name':
        curs.execute("INSERT INTO order_list (customer_name,customer_address,customer_phone,items,courier,status)" "VALUES (%s,%s,%s,%s,%s,%s)", (value[0],value[1],value[2],value[3],value[4],value[5]))
    elif keys[1] == 'cour_name':
        curs.execute("INSERT INTO courier_list (cour_name,cour_phone)" "VALUES (%s, %s)", (value[0],value[1]))    


                                    #Function for updating list of product, order, courier
def update_fn(curs,keys,tbl):
    product_id = str(input("\n Please enter the  id to be updated?: "))
    for k in keys:
        if k == 'status':
             display_fn(curs,ord_stat_keys,'order_status',0)
             print('Please enter the new satus id:')
             new_value = str(input())
             if new_value != "":
                sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                curs.execute(sql_cmd,(new_value,product_id)) 
        elif k == 'items':
            display_fn(curs,product_keys,'product_list',0)
            optn = ''
            prd_ids = []
            while optn !='0':
                prd_id = input('Please enter the product id for ordering, 0 for checkout:')
                optn = str(prd_id)
                if optn != '0':
                    prd_ids.append(prd_id)
            str_ids = ''
            for i,id in enumerate(prd_ids):
                if i == 0:
                    str_ids = str_ids + str(id)
                else:
                    str_ids = str_ids+ ',' + str(id)
            if str_ids != "":
                sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                curs.execute(sql_cmd,(str_ids,product_id))
        elif k == 'courier':
             display_fn(curs,cour_keys,'courier_list',0)
             print('\n\nPlease select a courier id from the list:')
             new_value = str(input())
             if new_value != "":
                sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                curs.execute(sql_cmd,(new_value,product_id))
        elif k != 'id':
            print("\n Please enter the new ",k,":")
            new_value = str(input())
            if new_value != "":
                sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                curs.execute(sql_cmd,(new_value,product_id))   


                                            #Function for deleting list of product, order, courier                                
def delete_fn(curs,tbl): 
    product_id = str(input("\n Please enter the  id to be deleted?: "))
    sql_cmd = "Delete from " + tbl +  " where id =%s"
    curs.execute(sql_cmd,product_id)


                                            # Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


                                            # Establish a database connection
db_connection = pymysql.connect(host,user,password,database)


                                            # A cursor is an object that represents a DB cursor,
                                            # which is used to manage the context of a fetch operation.
cursor = db_connection.cursor(pymysql.cursors.DictCursor)

                                            #Main Body
option_m = ""
while option_m !="0":
    print("\n Welcome to Our Caffe\n\n")
    display_fn(mn_menu,0,0,0)
    option_m = input("\n Please enter your option:")

                                            #Save and exit option
    if option_m == "0":
        print("\n Thanks for using our caffe ")
        db_connection.commit()
        cursor.close()
        db_connection.close()

                                            #Product menu option
    elif option_m == "1": 
        option_p = ""
        while option_p !="0":
            display_fn(prd_menu,0,0,0)
            option_p = input("\nPlease enter your option:")
            if option_p == "0":
                print("\n Back to Main menu")
            elif option_p == "1":    
                print("The product list is:")
                display_fn(cursor,product_keys,'product_list',1)   
            elif option_p == "2":
                display_fn(cursor,product_keys,'product_list',0)
                add_fn(cursor,product_keys)
                print('New product list is\n')
                display_fn(cursor,product_keys,'product_list',1)    
            elif option_p =="3":
                print("\n Product List:")
                display_fn(cursor,product_keys,'product_list',0)                   
                update_fn(cursor,product_keys,"product_list")  
                print("\n New updated list is:")
                display_fn(cursor,product_keys,'product_list',1)     
            elif option_p == "4":  
                print("\n The product list is:")
                display_fn(cursor,product_keys,'product_list',0)  
                delete_fn(cursor,"product_list")
                print("\n New product list is:")
                display_fn(cursor,product_keys,'product_list',1) 
            else:
                print("Invalid option. Please enter valid option:")

                                            #Orders Menu option 
    elif option_m == "2":
        option_ord=""
        while option_ord !="0":
            display_fn(ord_menu,0,0,0)
            option_ord = input("\n Please enter your option:") 
            #Displaying orders list#    
            if option_ord =="1":
                print("\n The existing orders are")
                display_fn(cursor,ord_keys,'order_list',1)                
                
                                            #Creating new order#
            elif option_ord == "2":
                print("\n Please enter the following details")
                add_fn(cursor,ord_keys)
                print('New product list is\n')
                display_fn(cursor,ord_keys,'order_list',1) 
        
                                        #Updating Existing order status#
            elif option_ord =="3":
                print("\n The existing orders are")
                display_fn(cursor,ord_keys,'order_list',0)
                update_fn(cursor,['status'],"order_list") 
                print('New product list is\n')
                display_fn(cursor,ord_keys,'order_list',1) 
        
                                        #update existing order#
            elif option_ord =="4":
                print("\n The existing orders are")
                display_fn(cursor,ord_keys,'order_list',0)
                update_fn(cursor,ord_keys[:-1],"order_list") 
                print('New product list is\n')
                display_fn(cursor,ord_keys,'order_list',1) 

                                        #Deleting Order#
            elif option_ord == "5":
                print("\n The orderd list is:")
                display_fn(cursor,ord_keys,'order_list',0)  
                delete_fn(cursor,"order_list")
                print("\n New order list is:")
                display_fn(cursor,ord_keys,'order_list',1)   
            else:
                print("\n Invalid option. Please enter the correct option:")

                                        #courier menu#
    elif option_m == "3":
        option_cour =""

                                     #Displaying submenus of courier menu#

        while option_cour !="0":
            display_fn(cour_menu,0,0,0)            
            option_cour = input("\n Please enter your option:") 

                                     #Displaying Courier list#
            if option_cour =="1":
                print("\n The existing Courier list is:")                
                display_fn(cursor,cour_keys,'courier_list',1)              

                                    # Create new courier list# 
            elif option_cour == "2":
                print(f'\n Current Courier List is:')
                display_fn(cursor,cour_keys,'courier_list',0)
                add_fn(cursor,cour_keys)
                print('New courier list is\n')
                display_fn(cursor,cour_keys,'courier_list',1)            

                                    # Update Courier list#   
            elif option_cour =="3":
                print("\n Courier List:")
                display_fn(cursor,cour_keys,'courier_list',0)                   
                update_fn(cursor,cour_keys,"courier_list")  
                print("\n New updated list is:")
                display_fn(cursor,cour_keys,'courier_list',1)                  

                                    #Delete Courier list#
            elif option_cour =="4":   
                print("\n Courier List:")
                display_fn(cursor,cour_keys,'courier_list',0)  
                delete_fn(cursor,"courier_list")
                print("\n New courier list is:")
                display_fn(cursor,cour_keys,'courier_list',1)                   
            else:
                print("\n Invalid option. Please enter the correct option:")    
    else:
                print("Invalid option. Please enter valid option:")
