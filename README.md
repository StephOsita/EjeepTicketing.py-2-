# EjeepTicketing.py-2-
This python code project is for Public Electronic Jeepney Ticketing System generating ride information and receipt. It is built to help electronic jeepney driver and conductors and render fair service to passengers. This code solve problems such as real-time computing and determine appropriate distance of a passenger.


# Route
This is a list for where a passenger destined to go or to stop.


```python
starmall_sampol = [
    "Starmall",
    "Bulacan State University", 
    "Carissa 4B",
    "Kaypian Elementary School",
    "Petron Karyapay",
    "SJDM City Hall",
    "Motorpol", 
    "Area E",
    "SJDM National Trade School",
    "Sampol"
    ]

sampol_starmall = [
    "Sampol",
    "SJDM National Trade School",
    "Area E",
    "Motorpol", 
    "SJDM City Hall",
    "Petron (Karyapay)",
    "Kaypian Elementary School",
    "Carissa 4B",
    "Bulacan State University",
    "Starmall",
    ]

fare = [
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 23],  # Starmall
    [15, 0, 15, 16, 17, 18, 19, 20, 21, 22],  # BSU
    [16, 15, 0, 15, 16, 17, 18, 19, 20, 21],  # Carissa
    [17, 16, 15, 0, 15, 16, 17, 18, 19, 20],  # Kaypian Elem
    [18, 17, 16, 15, 0, 16, 17, 18, 19, 20],  # Petron Karyapay
    [19, 18, 17, 16, 15, 0, 15, 16, 17, 18],  # SJDM City Hall
    [20, 19, 18, 17, 16, 15, 0 ,15, 16, 17],  # Motorpol
    [21, 20, 19, 18, 17, 16, 15, 0, 15, 16],  # Area E
    [22, 21, 20, 19, 18, 17, 16, 15, 0, 15],  
    [23, 22, 21, 20, 19, 18, 17, 16, 15, 0]   
    ]

Discounts = [
    "Student", "Senior Citizen", "PWD", "Regular"
    ]
```


print("===================================")
print("              ROUTE")
print("===================================")
print("1. Starmall -> Sampol")
print("2. Sampol -> Starmall")
route = int(input("Choose route: "))
if route == 1:
    while route == 1:
        print("===================================")
        print("           Pick-Up Point")
        print("==================================")
        for index, locations in enumerate(starmall_sampol):
            print(f"{index+1}. {locations} ")
        print("==================================")
        From = int(input("Choose pick-up point: "))
        To = int(input("Choose drop-off point: "))
        print("===================================")
        print("             DISCOUNT")
        print("===================================")
        print("1. Student \n2. Senior Citizen \n3. PWD \n4. Regular")
        Discount = int(input("Enter Discount: "))
        if Discount in (1, 2, 3):
            DiscountFee = 0.20
            Total = fare[From-1][To-1] * 0.80
            break
        elif Discount == 4:
            Total = fare[From-1][To-1]
            break
        else:
            print("Invalid Input...")
            break
    
    print("\n\n              GOORPU")
    print("===================================")
    print(f"From: {starmall_sampol[From -1]}")
    print(f"To: {starmall_sampol[To -1]}")
    print(f"Fare: P{fare[From-1][To-1]}.00")
    print(f"Discount: {Discounts[Discount-1]}")
    print(f"Total: P{int(Total)}.00")
elif route == 2:
    while route == 2:
        print("===================================")
        print("           Pick-Up Point")
        print("==================================")
        for index, locations in enumerate(sampol_starmall):
            print(f"{index+1}. {locations} ")
        print("==================================")
        From = int(input("Choose pick-up point: "))
        To = int(input("Choose drop-off point: "))
        print("===================================")
        print("             DISCOUNT")
        print("===================================")
        for index, discounts in enumerate(Discounts):
            print(f"{index+1}. {discounts}")
        Discount = int(input("Enter Discount: "))
        if Discount in (1, 2, 3):
            Total = fare[From-1][To-1] * 0.80
            break
        elif discount == 4: 
            Total = fare[From-1][To-1]
            break
        else:
            print("Invalid Input...")
            break
    
    print("\n\n              GOORPU")
    print("===================================\n")
    print(f"From: {sampol_starmall[From -1]}")
    print(f"To: {sampol_starmall[To -1]}")
    print(f"Fare: P {fare[From-1][To-1]}.00")
    print(f"Discount: {Discounts[Discount-1]}")
    print(f"Total: P{int(Total)}.00")
else:
    print("Invalid Input...")
