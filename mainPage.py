

sayi1 = 3
sayi2 = 11
sayi3 = 10
if sayi1>sayi2 & sayi2>sayi3:
    print("Büyük sayı : ", sayi1, "Küçük sayı : ", sayi3)
elif sayi2>sayi1 & sayi1>sayi3:
    print("Büyük sayı :", sayi2, "Küçük Sayı : ", sayi3)
elif sayi3>sayi2 & sayi2>sayi1:
    print("Büyük sayı :", sayi3, "Küçük Sayı : ", sayi1)
elif sayi1>sayi3 & sayi3>sayi2:
    print("Büyük sayı :", sayi1, "Küçük Sayı : ", sayi2)
elif sayi2>sayi3 & sayi3>sayi1:
    print("Büyük sayı :", sayi2, "Küçük Sayı : ", sayi1)
elif sayi3>sayi1 & sayi1>sayi2:
    print("Büyük sayı :", sayi3, "Küçük Sayı : ", sayi2)
else:
    print("")