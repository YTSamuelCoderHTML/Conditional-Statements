print("Let's see if you are a dumb business man or a smart business man!")

costprice = int(input("Tell the Cost:"))

sellingprice = int(input("Tell how much to sell for:"))

if sellingprice < costprice:
    print("You are selling the things less than price of cost! You.... are... a.... DUMB BUSINESS MANNNN!!!!")

elif sellingprice == costprice:
    print("You are selling the things at the same price of cost! - This is rare but - You.... are... a.... MID BUSINESS MANNNN!!!!")

if sellingprice > costprice:
     print("You are selling the things at a bigger price than cost! - You.... are... a.... SMART BUSINESS MANNNN!!!!")