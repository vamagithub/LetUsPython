'''
Distance between two cities is input through keyboard (in  Km)

convert - in m , ft , inches , cm

'''
print("Welcome to conversion startup.We are happy to help you with all your conversions.")

print("Enter name of the cities below(*OPTIONAL- PRESS ENTER TO SKIP*)")

a = input("City1:")
b = input("City2:")

km = int(input("Enter Distance in kilometers:\t>>"))

m = km * 1000
cm = m* 100
inch = cm/2.54
ft = inch/12


print("meters:%d\ncentimeters:%d\ninches:%d\nfeet:%d\n"
      %(m,cm,inch,ft))

print("Happy Journey")
