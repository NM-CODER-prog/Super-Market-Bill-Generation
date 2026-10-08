#SUPER MARKET MINI PROJECT.

print("=="*10,"","PYTHONLIFE MARKET","","=="*10)

name=input("enter your name: ")

#LIST OF ITEAMS
lists = """
Rice       Rs 10/kg
Sugar       Rs 8/kg
oil         Rs 30/liter
salt        Rs 25/kg
Paneer      RS 40/kg
Maigge      Rs  12/kg
Boost       Rs 200/bottles
"""



#Declaration
price=0
pricelist=[]
totalprice=[]
finalprice=[]
list=[]
qlist=[]
plist=[]

#rate for each iteam.

iteams = {'rice':10,'sugar':8,'oil':30,'salt':25,'paneer': 40,'maggie':12,'boost':200}
while True:
    option =input("press 1 for list 2 to exit: ")
    if option =="2":
        break
    elif option=="1":
        print(lists)

    while True:
        inp1=input("To buy press 1 or press 2 to exit: ")
        if inp1 =='2':
            print("Thank you for shopping")
            break
        elif inp1== '1':
            iteam= input("choose your iteams: ").lower()
            while True:
                quantity_input=input("enter quantity: ")
                if quantity_input.isdigit():
                    quantity=int(quantity_input)
                    break
                else:
                    print("please enter a valid quantity: ")
                if iteam in iteams:
                    price=quantity * iteams[iteam]
                    pricelist.append((iteam,quantity,iteams(iteam),price))
                    totalprice=+price
                    list.append(iteam)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("selected iteam is not available.sorry for the inconvenience.")
                if totalprice>0:
                    tax=(totalprice*18)/100
                    finalamount=tax*totalprice
                    print(25 * "=" , "pythonlife Supermarket", 25 * "=")
                    print(28 * " ", "hyderabad")
                    print("Name",name,30* " ","August 21 2026")
                    print(75 * "=")
                    print("sno",10*" ","iteams",8*" ","quality",8*" ","price")
                    for i in range(len(pricelist)):
                        print(i,13 *" ",list[i],8* " ",qlist[i],8*" ",plist[i])
                    print(75 * "=")
                    print(50*" ",'Final amount','RS',finalamount)
                    print(20*" ","Thank you & visit Again")
                    print(75 * "=")












