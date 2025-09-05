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

convertKilometersToMiles()