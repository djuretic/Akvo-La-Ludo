import random
forto = 100
sano = 100

def Komenco():
    print("")
    print("     A            K   K        V     V       O O")
    print("    A  A          K K           V   V      O     O")
    print("   A    A         K K            V V       O     O")
    print("  A      A        K   K           V          O O")
    print("")
    print("Kreis de Ethan Hansen")
    print("")
    print("-------------------------------------------------------------------")
    print("\n\n")
    print("Vi estas en dezerto insulo, kusxas sur la tero. La suno estas tre varma kaj ondoj tusxas viajn piedojn. Ne estas malgranda insulo, cxar ne povas vidi la alia flanko")
    print("Norde estas gxangalo, kaj la resto de la insulo")
    print("Sude estas nur oceano")
    print("Okcidente estas parto de sxipo")
    print("Oriente estas pli strando")
    print("")
    forto = 100
    sano = 100
    response = str(input("> "))
    while (response != "norde" and response != "sude" and response != "okcidente" and response != "oriente"):
        if (response == "sano"):
            print("Via sano estas: ", sano)
        elif (response == "forto"):
            print("Via forto estas: ", forto)
        response = str(input("> "))
    if (response == "sude"):
        Oceano()
    elif (response == "norde"):
        Gxangalo()
        

def Oceano():
    if (random.randint(0,10) == 5):
        print("La maro prenis vin, kaj vi mortis")
    else:
        print("Vi estas en la oceano, nagxado. Vi povas nagxi, cxu ne?")
        print("Vi ne povas vidi alia lando. Kaj ne estas io utila")

def Gxangalo():
    print("Vi estas en la gxangalo. Arboj kaj plantoj estas cxie. Vi auxdas bestojn, sed vi ne povas vidi ilin.")
    print("FIX THIS")

Komenco()
