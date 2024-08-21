year=int(input("Enter year:"))
if year%4==0:
    if year%100==10:
        if year%4==0:
            print(f"{year} is leap year")
        else:
             print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
        
