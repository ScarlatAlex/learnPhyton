# Calculator

what = input("Ce facem? (+ ; - ; * ; /): ")

a = float(input("Introdu primul numar: "))
b = float(input("Introdu al doilea numar: "))

if what == "+":
    c = a + b
    print("Rezultat: " + str(c))
elif what == "-":
    c = a - b
    print("Rezultat: " + str(c))
elif what == "*":
    c = a * b
    print("Rezultat: " + str(c))
elif what == "/":
    c = a / b
    print("Rezultat: " + str(c))
else:
    print("Ati facut ceva gresit...")
