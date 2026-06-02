mid=input("Enter the Member ID.")
reg=input("Enter bike Registration Number. ")
mob=input("Enter Mobile Number. ")
d=int(input("Enter number of days bike was taken on rent."))
if d<=5:
	r=550.0
if d<=10:
	r=550+(d-5)*400.0
if d>10:
	r=550.0+400.0+(d-10)*250.0
print("========Slip========")
print("Member ID: ",mid)
print("Bike Registration Number: ",reg)
print("Mobile Number: ",mob)
print("Number if days bike was taken on rent: ",d)
print("Amount to be paid: ",r)
print("====================")