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
    [0, 15, 16, 17, 18, 19, 20, 21, 22, 23],  
    [15, 0, 15, 16, 17, 18, 19, 20, 21, 22],  
    [16, 15, 0, 15, 16, 17, 18, 19, 20, 21],  
    [17, 16, 15, 0, 15, 16, 17, 18, 19, 20],  
    [18, 17, 16, 15, 0, 16, 17, 18, 19, 20], 
    [19, 18, 17, 16, 15, 0, 15, 16, 17, 18], 
    [20, 19, 18, 17, 16, 15, 0 ,15, 16, 17],  
    [21, 20, 19, 18, 17, 16, 15, 0, 15, 16],  
    [22, 21, 20, 19, 18, 17, 16, 15, 0, 15],  
    [23, 22, 21, 20, 19, 18, 17, 16, 15, 0]   
    ]
Discounts = [
    "Student", "Senior Citizen", "PWD", "Regular"
    ]

boundary = []
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
        if From == 0:
            MoneyCollected = sum(boundary)
            print("You Choose to end journey...")
            print(f"Total money collected: {MoneyCollected:.2f}")
        To = int(input("Choose drop-off point: "))
        Quantity = int(input("Enter Quantity: "))
        print("===================================")
        print("             DISCOUNT")
        print("===================================")
        print("1. Student \n2. Senior Citizen \n3. PWD \n4. Regular")
        Discount = int(input("Enter Discount: "))
        if Discount in (1, 2, 3):
            Total = fare[From-1][To-1] * 0.80
            DiscountFee = fare[From-1][To-1] / 0.80
            print("\n\n              GOORPU")
            print("===================================")
            print(f"From: {starmall_sampol[From -1]}")
            print(f"To: {starmall_sampol[To -1]}")
            print(f"Discount: {Discounts[Discount-1]}")
            print(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * 5:.2f}")
            print(f"Discount Amount: P{DiscountFee}")
            print(f"Total: P{Total * Quantity:.2f}")
            boundary.append(Total * Quantity)
            continue
        elif Discount == 4:
            DiscountFee = 0
            Total = fare[From-1]
            print("\n\n              GOORPU")
            print("===================================")
            print(f"From: {starmall_sampol[From -1]}")
            print(f"To: {starmall_sampol[To -1]}")
            print(f"Discount: {Discounts[Discount-1]}")
            print(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * 5:.2f}")
            print(f"Discount Amount: P{DiscountFee}")
            print(f"Total: P{Total * Quantity}")
            boundary.append(Total * Quantity)
            continue
        else:
            print("Invalid Input...")
            break
        
    
    
elif route == 2:
    while route == 2:
        print("===================================")
        print("           Pick-Up Point")
        print("==================================")
        for index, locations in enumerate(sampol_starmall):
            print(f"{index+1}. {locations} ")
        print("==================================")
        From = int(input("Choose pick-up point: "))
        if From == 0:
            MoneyCollected = sum(boundary)
            print("You Choose to end journey...")
            print(f"Total money collected: {MoneyCollected:.2f}")
        To = int(input("Choose drop-off point: "))
        Quantity = int(input("Enter Quantity: "))
        print("===================================")
        print("             DISCOUNT")
        print("===================================")
        for index, discounts in enumerate(Discounts):
            print(f"{index+1}. {discounts}")
        Discount = int(input("Enter Discount: "))
        if Discount in (1, 2, 3):
            Total = fare[From-1][To-1] * 0.80
            DiscountFee = Total / 0.80
            print("\n\n              GOORPU")
            print("===================================\n")
            print(f"From: {sampol_starmall[From -1]}")
            print(f"To: {sampol_starmall[To -1]}")
            print(f"Discount: {Discounts[Discount-1]}")
            print(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * 5:.2f}")
            print(f"Discount Amount: P{DiscountFee}")
            print(f"Total: P{Total * Quantity:.2f}")
            boundary.append(Total * Quantity)
            continue
        elif Discount == 4: 
            DiscountFee = 0
            Total = fare[From-1][To-1]
            print("\n\n              GOORPU")
            print("===================================\n")
            print(f"From: {sampol_starmall[From -1]}")
            print(f"To: {sampol_starmall[To -1]}")
            print(f"Discount: {Discounts[Discount-1]}")
            print(f"Fare: P {fare[From-1][To-1]}.00 x {Quantity} = {fare[From-1][To-1] * 5:.2f}")
            print(f"Discount Amount: P{DiscountFee}")
            print(f"Total: P{Total * Quantity:.2f}")
            boundary.append(Total * Quantity)
            continue
        else:
            print("Invalid Input...")
            continue
        
else:
    print("Invalid Input...")
