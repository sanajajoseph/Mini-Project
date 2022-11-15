#project week 3#
from mimetypes import init





from xml.sax.saxutils import prepare_input_source

#Reading data's from txt file#

product_file = open("product.txt","r")
product_list = product_file.readlines()
for i, product in enumerate (product_list):
    product_list[i] = product[:-1]
product_file.close()


courier_file = open("couriers.txt","r")
courier_list = courier_file.readlines()
for i, courier in enumerate (courier_list):
    courier_list[i] = courier[:-1]
courier_file.close()


order_dic = [{"order_no": 1,    
    "customer_name":"Max", 
    "customer_address":"1 New street, LS00xx, Leeds",   
    "customer_phone": 1111111110,
    "ord_status":"preparing"}]

order_status =['Order Rejected','Preparing','Ready','On the way','Delivered'] 


option = ""
while option !="0":
    
#Displaying Main Menu#
    

    print("\n Welcome to Our Caffe")
    print("\n *********************")
    print("\n")
    print("MAIN MENU")
    print("==========")
    print("[1]. Products Menu ")
    print("[2]. Orders Menu")
    print("[3]. Courier Menu")
    print("[0]. Exit")
    option = input("\n Please enter your option:")
    if option == "0":

        #Saving the data to product list#

        product_file = open("product.txt",'w')
        for product in product_list:           
            product_file.writelines(product + "\n")
        product_file.close()

        #Saving the data to courier list#

        courier_file = open("couriers.txt",'w')
        for courier in courier_list:           
            courier_file.writelines(courier + "\n")
        courier_file.close()
        print("\n Your Data is Automatically Saved")
        print("\n Thanks for using our caffe ")

#Product Menu#
    elif option == "1":
        option1 = ""
        while option1 !="0":
            print("\n PRODUCT MENU")
            print("=================")
            print("[1] Display the product list")  
            print("[2] Add the product to list")
            print("[3] Update the product")
            print("[4] Delete product")
            print("[0] Back") 
            option1 = input("\nPlease enter your option:")
            if option1 == "0":
                print("\n Back to Main menu")

        #Display Product list#
                
            elif option1 == "1":    
                print("The product list is:")
                for product in product_list:
                    print(product)
                input("\nPress ENTER to return menu. ")  

        #Add product into database#
                  
            elif option1 == "2":
                print(f'\n Current product List is: {product_list}')
            
                new_product = str(input("\n Please enter new product to add to list:\n"))                
                product_list.append(new_product)
                print("\n Added",new_product)
                print(f'\n New product List is {product_list}')


        #Update product#
                
            elif option1 =="3":
                print("\n Product List:")
                for idx, product in enumerate(product_list):
                    print("\t", idx, product)
                product_number = input("\n Which product would you like to update?: ")
                
                product_number = int(product_number)
                existing_name = product_list[product_number]

                new_name = input(f"Enter a new name for {existing_name}: ")
                product_list[product_number] = new_name
                print("\n New updated list is:")
                print(product_list)


        #Delete product#        
            elif option1 == "4":
                print("\n The product list is:")
                for idx, product in enumerate(product_list):
                    print("\t", idx, product)
               
                del_item = input("\nwhich product would you like to Delete:? Please enter the number:")
                del_item = int(del_item)
                product_list.pop(del_item)
                print(del_item,"Deleted from database")
                print("\n New product list is:")
                print(product_list)    

            else:
                print("Invalid option. Please enter 0 to 4.")

#Orders Menu# 

    elif option == "2":
        option_ord=""
        while option_ord !="0":

            #Displaying submenus of orders menu#
            print("\n ORDERS MENU")
            print("================")
            print("\n1.Display order dictionary")
            print("2.Add Customer details")
            print("3.Update existing order status")
            print("4.Update existing order")
            print("5.Delete order")
            print("0.Back") 
            option_ord = input("\n Please enter your option:") 

        #Displaying orders list#    
            if option_ord =="1":
                print("\n The existing orders are")
                for order in order_dic:
                    print(order)

                input("\nPress ENTER to return menu. ")

        #Creating new customers#

            elif option_ord == "2":
                print("\n Please enter the following details")
                cus_name= str(input("\n Name:\t"))
                cus_addr= str(input("\n Address:\t" ))
                cus_ph = int(input("\n Phone Number:\t"))
                new_ord_dic ={"order_no": len(order_dic) + 1,    
                            "customer_name":cus_name, 
                            "customer_address":cus_addr,   
                            "customer_phone": cus_ph,
                            "ord_status":"preparing"}
                order_dic.insert(len(order_dic) + 1,new_ord_dic)
                print("\n The order has been placed\n your order number is:\t",len(order_dic)) 
                input("\nPress ENTER to return menu. ")

        #Updating Existing order#

            elif option_ord =="3":
                for idx, ord in enumerate(order_dic):

                    print("\t", idx ,"\torder number :",ord["order_no"], "\tstatus:" ,ord["ord_status"])
                ord_index = int(input("\n Which order would you like to update?: "))
                existing_status = order_dic[ord_index]["ord_status"]
                print("The current status is:\t",existing_status)
                print("Choose an option to update:")
                print("[1]. Ready ")
                print("[2]. Deliverd")
                status_ip = int(input("\n"))
                if status_ip == 1:
                    order_dic[ord_index]["ord_status"] = "Ready"
                    print("\nStatus updated")
                elif status_ip == 2:
                    order_dic[ord_index]["ord_status"] = "Deliverd"
                    print("\nStatus updated")
                else:
                    print("\n status is not updated") 

                input("\n Press ENTER to return menu.")
            elif option_ord =="4":
                for idx, ord in enumerate(order_dic):

                    print("\n", idx ,ord)
                ord_index = int(input("\n Which order would you like to update?: "))
                selt_ord = order_dic[ord_index]
                
                for idx, up_dic in enumerate(selt_ord):
                    print("\nEnter the new",up_dic)
                    new_value = input()
                    if new_value != "":
                        order_dic[ord_index][up_dic] = new_value
                        print(up_dic," is updated")
                    else:
                        print(up_dic," is not updated")    
                print("The updated order list is:\n", order_dic)   
                input("\nENTER to return")    

        #Deleting Order#

            elif option_ord == "5":
                
                print("\n The orderd list is:")
                for idx, delete in enumerate(order_dic):
                    print("\t", idx, delete)
                
                del_order = int(input("\nwhich order would you like to Delete:? Please enter the number:"))
                
                order_dic.pop(del_order)
                print("\n Order Deleted from database")
                print("\n New Order list is:")
                print(order_dic)    
                input("\nENTER to return")


            else:
                print("\n Invalid option. Please enter the correct option:")    

#courier menu#
    elif option == "3":
        option_cour =""

    #Displaying submenus of courier menu#

        while option_cour !="0":
            print("\nCOURIERS MENU")
            print("=================")
            print("\n1.Display Courier List")
            print("2.Create new Courier")
            print("3.Update existing Courier")
            print("4.Delete Courier")            
            print("0.Back") 
            option_cour = input("\n Please enter your option:") 

        #Displaying Courier list#

            if option_cour =="1":
                print("\n The existing Courier list is:")
                for courier in courier_list:                
                    print(courier)

                input("\nPress ENTER to return menu. ")

        # Create new courier list#
                
            elif option_cour == "2":
                print(f'\n Current Courier List is: {courier_list}')
            
                new_courier = str(input("\n Please enter new courier to add to list:\n"))
                courier_list.append(new_courier)
                print("\n Added",new_courier)
                print(f'\n New Courier List is {courier_list}')
                
                input("\nPress ENTER to return menu. ")

        # Update Courier list#
                
            elif option_cour =="3":
                print("\n Courier List:")
                for idx, courier in enumerate(courier_list):
                    print("\t", idx, courier)
                courier_number = input("\n Which courier would you like to update?: ")
                
                courier_number = int(courier_number)
                existing_courier = courier_list[courier_number]

                new_cou_name = input(f"Enter a new name for {existing_courier}: ")
                courier_list[courier_number] = new_cou_name
                print("\n New updated list is:")
                print(courier_list)

                input("\n Press ENTER to return menu.")

        #Delete Courier list#

            elif option_cour =="4":   
                print("\n Courier List:")
                for idx, courier in enumerate(courier_list):
                    print("\t", idx, courier)        
                
                del_cour = int(input("\nwhich order would you like to Delete:? Please enter the number:"))
                
                courier_list.pop(del_cour)
                print("\n Courier Deleted from database")
                print("\n New Courier list is:")
                print(courier_list)    
                input("\nENTER to return")


            else:
                print("\n Invalid option. Please enter the correct option:")    
            







    else:
        print("\n Invalid option. Please Press valid number.\n")    


            
            
        

        
    
        
    
    


    
