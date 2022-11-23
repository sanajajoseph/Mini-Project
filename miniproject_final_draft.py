
                            #for communicating with Database
import pymysql
import os
from dotenv import load_dotenv

                                #for defining the main menu
mn_menu = ["\nWelcome to Our Caffe\n\n","MAIN MENU","==========", "[1]. Products Menu ","[2]. Orders Menu",\
    "[3]. Courier Menu","[0]. Exit"] 

                                #for defining the Product menu    
prd_menu = ["\nPRODUCT MENU","=================","[1] Display the product list",\
    "[2] Add the product to list","[3] Update the product","[4] Delete product","[0] Back" ]

                                #for defining the Orders menu    
ord_menu = ["\nORDERS MENU","================","[1].Display order dictionary","[2].Add new order details",\
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
    if ls_idfr != 0:
        os.system("cls")
    if keys != 0:
        print('\nThe current ' + tbl.replace('_',' ') + ' is:\n')
        curs.execute('SELECT * FROM ' + tbl)
        curs = curs.fetchall()
    for i in curs:
        print(i)
    if ls_idfr != 0:
        input("\nPress ENTER to return menu.")
        os.system("cls")
    return curs 


                                #Function for adding list of product, order, courier        
def add_fn(curs,keys):
    while True:
        value = []
        for k in keys:
            if k == 'items':
                prd_list = display_fn(curs,product_keys,'product_list',0)
                optn = ''
                prd_ids = []
                while optn !='0':
                    vld_ip = False
                    prd_id = input('\nPlease enter the product id for ordering, 0 for checkout:')
                    if prd_id != '':
                        for prd in prd_list:
                            if prd_id == str(prd['id']) or prd_id == '0':
                                vld_ip = True
                                break
                        if vld_ip == True:
                            optn = str(prd_id)
                            if optn != '0':
                                prd_ids.append(prd_id)
                        else:
                            input("\nInvalid option. Press ENTER to continue")
                            continue
                        str_ids = ''
                        for i,id in enumerate(prd_ids):
                            if i == 0:
                                str_ids = str_ids + str(id)
                            else:
                                str_ids = str_ids+ ',' + str(id)
                        if str_ids != '':
                            value.append(str_ids)
                        else:
                            input("\nAtleast one item necessary for checkout. Press ENTER to continue")
                            optn = ''
                            continue
            
            elif k == 'courier':
                cor_list = display_fn(curs,cour_keys,'courier_list',0)
                while True:
                    print('\n\nPlease select a courier id from the list:')
                    vld_ip = False
                    cor_id = input()
                    if cor_id != '':
                        for cor in cor_list:
                            if cor_id == str(cor['id']):
                                vld_ip = True
                                break
                        if vld_ip == True:
                            value.append(int(cor_id))
                            break
                        else:
                            input("\nInvalid option. Press ENTER to continue")
                            continue
            elif k == 'status':
                value.append(1)
            elif k != 'id':
                while True:
                    print("\nPlease enter the new",k,":")
                    n_val = input()
                    if n_val != '':
                        value.append(n_val)
                        break
                    else:
                        input("\nInvalid input. Press ENTER to continue")
                        continue  
        try:
            if keys[1] == 'Item':
                curs.execute("INSERT INTO product_list (Item,price)" "VALUES (%s, %s)", (value[0],value[1]))
            elif keys[1] == 'customer_name':
                curs.execute("INSERT INTO order_list (customer_name,customer_address,customer_phone,items,courier,status)" "VALUES (%s,%s,%s,%s,%s,%s)", (value[0],value[1],value[2],value[3],value[4],value[5]))
            elif keys[1] == 'cour_name':
                curs.execute("INSERT INTO courier_list (cour_name,cour_phone)" "VALUES (%s, %s)", (value[0],value[1]))    
            print("\n Added",value)
            input("\nPress ENTER to continue.")
            break
        except Exception as error:
            print(f"Invalid input\n{error}")
            input("\nPress ENTER to continue.")
            continue
    os.system("cls")   

                                    #Function for updating list of product, order, courier
def update_fn(curs,keys,tbl):
    list = display_fn(curs,keys,tbl,0)
    while True:
        print("\nPlease enter the " + tbl.split('_')[0] + " id to be updated?: ")
        id = input()
        vld_ip = False
        if id != '':
            for itm in list:
                if id == str(itm['id']):
                    vld_ip = True
                    break
        if vld_ip == True:
            for k in keys:
                try:
                    if k == 'status':
                        stat_list = display_fn(curs,ord_stat_keys,'order_status',0)
                        while True:
                            print('\nPlease enter the new satus id:')
                            stat_id = str(input())
                            vld_ip = False
                            if stat_id != '':
                                for stat in stat_list:
                                    if stat_id == str(stat['id']):
                                        vld_ip = True
                                        break
                                if vld_ip == True:
                                    sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                                    curs.execute(sql_cmd,(int(stat_id),id))
                                    break
                                else:
                                    input("\nInvalid option. Press ENTER to continue")
                                    continue 
                    elif k == 'items':
                        print(curs)
                        prd_list = display_fn(curs,product_keys,'product_list',0)
                        optn = ''
                        prd_ids = []
                        while optn !='0':
                            vld_ip = False
                            prd_id = input('\nPlease enter the product id for ordering, 0 for checkout:')
                            if prd_id != '':
                                for prd in prd_list:
                                    if prd_id == str(prd['id']) or prd_id == '0':
                                        vld_ip = True
                                        break
                                if vld_ip == True:
                                    optn = str(prd_id)
                                    if optn != '0':
                                        prd_ids.append(prd_id)
                                else:
                                    input("\nInvalid option. Press ENTER to continue")
                                    continue
                                str_ids = ''
                                for i, p_id in enumerate(prd_ids):
                                    if i == 0:
                                        str_ids = str_ids + str(p_id)
                                    else:
                                        str_ids = str_ids+ ',' + str(p_id)
                        if str_ids != "":
                            sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                            curs.execute(sql_cmd,(str_ids,id))
                    elif k == 'courier':
                        cor_list = display_fn(curs,cour_keys,'courier_list',0)
                        while True:
                            print('\n\nPlease select a courier id from the list:')
                            vld_ip = False
                            cor_id = input()
                            if cor_id == '':
                                break
                            else:
                                for cor in cor_list:
                                    if cor_id == str(cor['id']):
                                        vld_ip = True
                                        break
                                if vld_ip == True:
                                    sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                                    curs.execute(sql_cmd,(int(cor_id),id))
                                    break
                                else:
                                    input("\nInvalid option. Press ENTER to continue")
                                    continue
                    elif k != 'id':
                        print("\nPlease enter the new ",k,":")
                        new_value = str(input())
                        if new_value != "":
                            sql_cmd = "UPDATE " + tbl + " set " + k + " = %s where id =%s"
                            curs.execute(sql_cmd,(new_value,id))   
                except Exception as error:
                    print(f"Invalid input\n{error}")
                    input("\nPress ENTER to continue.")
                    continue
            break
        else:
            input("\nInvalid option. Press ENTER to continue")
            continue  
    
        

                                            #Function for deleting list of product, order, courier                                
def delete_fn(curs,keys,tbl):
    list = display_fn(curs,keys,tbl,0)
    while True:
        id = input("\nPlease enter the " + tbl.split('_')[0] + " id to be deleted?: ")
        vld_ip = False
        if id != '':
            for itm in list:
                if id == str(itm['id']):
                    vld_ip = True
                    break
            if vld_ip == True:
                sql_cmd = "Delete from " + tbl +  " where id =%s"
                curs.execute(sql_cmd,id)
                print("\nThe " + tbl.split('_')[0] + " with id " + str(id) + " deleted")
                input("\nPress ENTER to continue.")
                break
            else:
                input("\nInvalid option. Press ENTER to continue")
                continue
        else:
            input("\nInvalid option. Press ENTER to continue")
            continue


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
    os.system("cls")
    display_fn(mn_menu,0,0,0)
    option_m = input("\nPlease enter your option:")

                                            #Save and exit option
    if option_m == "0":
        os.system("cls")
        print("\nThanks for using our caffe\n\n")
        db_connection.commit()
        cursor.close()
        db_connection.close()

                                            #Product menu option
    elif option_m == "1":
        os.system("cls") 
        option_p = ""
        while option_p !="0":
            display_fn(prd_menu,0,0,0)
            option_p = input("\nPlease enter your option:")
            if option_p == "0":
                print("\nBack to Main menu")
            elif option_p == "1":    
                display_fn(cursor,product_keys,'product_list',1)   
            elif option_p == "2":
                add_fn(cursor,product_keys)
                display_fn(cursor,product_keys,'product_list',1)    
            elif option_p =="3":                   
                update_fn(cursor,product_keys,"product_list")  
                display_fn(cursor,product_keys,'product_list',1)     
            elif option_p == "4":  
                delete_fn(cursor,product_keys,"product_list")
                display_fn(cursor,product_keys,'product_list',1) 
            else:
                input("Invalid option. Press ENTER to continue")

                                            #Orders Menu option 
    elif option_m == "2":
        os.system("cls")
        option_ord=""
        while option_ord !="0":
            display_fn(ord_menu,0,0,0)
            option_ord = input("\nPlease enter your option:") 
            if option_ord == "0":
                print("\nBack to Main menu")
            #Displaying orders list#    
            elif option_ord =="1":
                display_fn(cursor,ord_keys,'order_list',1)                
                
                                            #Creating new order#
            elif option_ord == "2":
                add_fn(cursor,ord_keys)
                display_fn(cursor,ord_keys,'order_list',1) 
        
                                        #Updating Existing order status#
            elif option_ord =="3":
                update_fn(cursor,['status'],"order_list") 
                display_fn(cursor,ord_keys,'order_list',1) 
        
                                        #update existing order
            elif option_ord =="4":
                update_fn(cursor,ord_keys[:-1],"order_list") 
                display_fn(cursor,ord_keys,'order_list',1) 

                                        #Deleting Order#
            elif option_ord == "5":
                delete_fn(cursor,ord_keys,"order_list")
                display_fn(cursor,ord_keys,'order_list',1)   
            else:
                input("\nInvalid option. Press ENTER to continue")

                                        #courier menu#
    elif option_m == "3":
        os.system("cls")
        option_cour =""

                                     #Displaying submenus of courier menu#

        while option_cour !="0":
            display_fn(cour_menu,0,0,0)            
            option_cour = input("\nPlease enter your option:")
            if option_cour == "0":
                print("\nBack to Main menu") 

                                     #Displaying Courier list#
            elif option_cour =="1":              
                display_fn(cursor,cour_keys,'courier_list',1)              

                                    # Create new courier list# 
            elif option_cour == "2":
                add_fn(cursor,cour_keys)
                display_fn(cursor,cour_keys,'courier_list',1)            

                                    # Update Courier list#   
            elif option_cour =="3":                
                update_fn(cursor,cour_keys,"courier_list")  
                display_fn(cursor,cour_keys,'courier_list',1)                  

                                    #Delete Courier list#
            elif option_cour =="4":   
                delete_fn(cursor,cour_keys,"courier_list")
                display_fn(cursor,cour_keys,'courier_list',1)                   
            else:
                input("\nInvalid option. Press ENTER to continue")    
    else:
                input("\nInvalid option. Press ENTER to continue")

#end