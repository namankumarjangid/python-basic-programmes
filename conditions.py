weight=int(input("Weight:"))
unit=input("pound or kg")
if unit=="pound":
    converter=weight*0.45
    print(f"your weight is {converter} in pounds")
else:
    converted==weight/0.45
    print(f"your weight is {converted} in kilos")