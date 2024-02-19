amount= int(input("Enter Your Amount: "))
currency=input("Enter Currency To Convert From PKR: ")

if currency == "usd":
    print("PKR to USD" , amount*279)

elif currency =="eur":
    print("PKR TO EUR", amount*301)


elif currency =="gbp":
    print("PKR TO GBP" ,amount*348)

elif currency == "sar":
    print("PKR TO SAR" , amount*73)

elif currency == "inr":
    print("PKR TO INR" , amount*3.33)

elif currency == "aud":
    print("PKR TO AUD" , amount*180)

elif amount == "end":
    print("Thankyou")

else:
    print("currency not supported")


