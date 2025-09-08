"""
THIS IS A CONVERTER
"""

#convert C to F
def convertCtoF():
    C = float(input("Ievadi temperatūru: "))
    F = (C * 9/5) + 32
    print(F)

# convert kms to miles
def convertKilometersToMiles():
    kms = float(input("Ievadi attālumu: "))
    if kms > 0:
        miles = round(kms/1.6, 2)
        print(f"Rezultāts ir: {miles}")
    else:
        print("Vērtība nederīga!")

#convertKilometersToMiles()

#convert Euro to $$$
def convertEuroToUsd():
    Eur = float(input("Ievadi summu: "))
    if Eur > 0:
        usd = round(Eur * 1.17 , 2)
        print(f"Summa: {usd}")
    else:
        print("Nepareiza summa!")

#convertEuroToUsd()

#platības convert
def convertArea():
    square_m = int(input("Kvadrātmetri: "))
    ha = square_m / 10000
    print(f"{square_m} kvadrātmetri ir: {ha} hektāri!")

convertArea()