network = input("Enter  Network(Airtel/jio/Bsnl/Data packs): ")
amount = int(input("Enter Amount: "))
coupon = input("Enter coupon Code: ")
plan_available = False
if network == "jio":
#Recharge plans jio    
    if amount == 199:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 3GB/")
        print("Voice : Unlimited")
        print("SMS : 100 SMS")
        plan_available = True 
    elif amount == 249:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 1GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True 
    elif amount == 299:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 1.5GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True                
    elif amount == 349:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 2GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
    elif amount == 399:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 2.5GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True          
    elif amount == 599:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 84Days")
        print("Data: 2GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
    elif amount == 799:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 84Days")
        print("Data: 3GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True       
    elif amount == 999:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 98Days")
        print("Data: 2.5GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
#Jio data packs
    elif amount == 11:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  1 Hour")
        print("Data: Unlimited Data") 
    elif amount == 19:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  1 Day")
        print("Data: 1 GB")                 
    elif amount == 29:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  2 Day")
        print("Data: 2 GB")  
    elif amount == 39:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  3 Day")
        print("Data: 3 GB/Day")  
    elif amount == 69:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  7 Day")
        print("Data: 6 GB")    
    elif amount == 139:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: Existing Plan Validity")
        print("Data: 12 GB")  
    elif amount == 359:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 30 Days")
        print("Data: 50 GB")                              
    else:
        print("Pack Not Available")           
elif network == "airtel":
#Recharge plans airtel    
    if amount == 199:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 2GB Total")
        print("Voice : Unlimited")
        print("SMS : 100 SMS")
        plan_available = True 
    elif amount == 249:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 24Days")
        print("Data: 1GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True 
    elif amount == 249:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 1 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True                
    elif amount == 299:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 1.5 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
    elif amount == 349:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28Days")
        print("Data: 2 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True          
    elif amount == 549:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:56 Days")
        print("Data: 2 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
    elif amount == 859:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 84 Days")
        print("Data: 3 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True       
    elif amount == 1199:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 84 Days")
        print("Data: 2.5GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
#airtel data packs
    elif amount == 59:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  1 Day")
        print("Data: Unlimited Data") 
               
    elif amount == 33:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  1 Day")
        print("Data: 2 GB")  
    elif amount == 49:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  1 Day")
        print("Data: 6 GB")  
    elif amount == 99:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  2 DayS")
        print("Data: 20 GB")    
    elif amount == 181:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 30 Days")
        print("Data: 15 GB")  
    elif amount == 361:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 30 Days")
        print("Data: 50 GB")                              
    else:
        print("Pack Not Available")   
if network == "bsnl":
#Recharge plans bsnl    
    if amount == 107:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 35Days")
        print("Data: 3 GB Total")
        print("Voice : Unlimited")
        print("SMS : 100 SMS")
        plan_available = True 
    elif amount == 139:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28 Days")
        print("Data: 1.5 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True 
    elif amount == 187:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 28 Days")
        print("Data: 2 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True                
    elif amount == 199:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 30 Days")
        print("Data: 2 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
    elif amount == 247:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 30 Days")
        print("Data: 100 GB Total")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True          
    elif amount == 347:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 54 Days")
        print("Data: 2 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
    elif amount == 797:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 300 Days")
        print("Data: 2GB/Day(60Days)")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True       
    elif amount == 997:
        print("----- Recharge Receipt -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 160 Days")
        print("Data: 2 GB/Day")
        print("Voice : Unlimited")
        print("SMS : 100 SMS/Day")
        plan_available = True   
#Bsnl data packs
    elif amount == 16:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  1 Day")
        print("Data: 2 GB") 
    elif amount == 105:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  7 Days")
        print("Data: 20 GB")                 
    elif amount == 58:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  7 Days")
        print("Data: 8 GB")  
    elif amount == 49:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  30 Days")
        print("Data: 10 GB")  
    elif amount == 94:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity:  30 Days")
        print("Data: 3 GB")    
    elif amount == 151:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 30 Days")
        print("Data: 40 GB")  
    elif amount == 198:
        print("----- Recharge Receipt -----")
        print("----- Data Pack -----")
        print(f"Recharge Amount: ₹{amount}")
        print("Pack Validity: 40 Days")
        print("Data: 2 GB/Day")                              
    else:
        print("Pack Not Available")  
else:
    print("Invalid Network")  
            
if plan_available:

    if coupon == "SAVE50":
        amount = amount - 50
        print("Coupon Applied ")

    elif coupon == "SAVE100":
        amount = amount - 100
        print("Coupon Applied ")

    else:
        print("No Coupon Applied")
else:
    print("Recharge Not Success")        

print("Final Amount: ₹",amount)                    