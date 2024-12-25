temp = float(input("What is the temperature{in celcius}? "))
rain = bool(input("Is it raining (type 1 for yes and 0 for no)?"))
if (10<temp>=30)and(rain == 0):
    print("Wear a shirt and shorts")
elif (10<temp>=30)and(rain == 1):
    print("Please wear shorts and shirt and bring jacket or unbrella")
elif(10<temp<30)and(rain == 1):
    print("Please bring an unbrella or a jacket and some warm clothes(wear trousers)")
elif (10<temp<30)and(rain == 0):
    print("Be in warm clothes")
elif (temp ==10)and(rain == 0):
    print("Be in extremely warm clothes")
elif (temp==10)and(rain == 1):
    print("Be in extremely warm clothes and bring an umbrella")
elif (-12>=temp)and(rain == 0):
    print("Be in extremely warm clothes and stay inside inside unless you have to (make sure you have heating and essentials)")
elif(-12>=temp)and(rain == 1):
    print("Be in extremely warm clothes and stay inside unless you have to(make sure you have heating and essentials)")
