a = int(input("1 chi sonni kiriting"))
b = int(input("2 chi sonni kiriting"))
arifmetic = input("Hisoblash amalini kiriting:")

if arifmetic == "+":
    print(a+b)

elif arifmetic == "*":
    print(a*b)

elif arifmetic == "/":
    if a != 0 and b !=0:
        print(a/b)

    else:
        print("Amal noto'g'ri")

else: arifmetic == "-"
print(a-b)
