# default parameter
# adalah sebuah istilah untuk parameter yang memiliki nilai awal
# atau nilai default.

def penjumlahan(nilai1 = 5, nilai2 = 10, nilai3 = 20):
    return nilai1 + nilai2 + nilai3

print(penjumlahan()) # outputnya 15
print(penjumlahan(29)) # outputnya 39
print(penjumlahan(10,20,19))

def hello(a,b):
    print(a+b)

hello(10,8)

def hello_bro(town = "Jakarta"):
    print('i am from '+ town)

hello_bro()
hello_bro("Bandung")
hello_bro("Bekasi")

def say_hi(age = 17, name ="Jono"):
    print("My Name is", name, "My Age,", age)

say_hi()

def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
         hasil = hasil * angka
    return hasil

print(pangkat(3))
print(pangkat(5))
print(pangkat(10))
print(pangkat(6))
print(pangkat(3,3))
print(pangkat(5,4))
print(pangkat(10,4))
print(pangkat(6,6))

def nama(*names):

    for name in names:
        print("Hello", name)

nama("Alfian", "Bejo","Doel", "Jhony")
