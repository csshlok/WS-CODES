eng = int(input("Enter marks of the english subject: "))
maths = int(input("Enter marks of the maths subject: "))
phy = int(input("Enter marks of the Phyiscs subject: "))
chem = int(input("Enter marks of the Chemistry subject: "))
comp = int(input("Enter marks of the Computer subject: "))
avg = (eng + maths + phy + chem + comp) / 5
if (avg >= 85):

    print("GRADE A")
elif (avg >= 40 and avg < 60):
    print("NEED TO WORK HARDER")
elif (avg < 40):
    print("CAN YOU BETTER")