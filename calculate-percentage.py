print("Enter your marks: ")
english1 = int(input("english paper 1: "))
english2 = int(input("english paper 2: "))
sindhi = int(input("sindhi: "))
urdu = int(input("urdu: "))
pakstd = int(input("pakistan studies: "))
islamiat = int(input("islamiat:"))
chem = int(input("chemistry: "))
bio = int(input("bioogy: "))
phy = int(input("physics: "))
maths = int(input("mathematics: "))

a = english1 + english2 + sindhi + urdu + pakstd + islamiat + chem + bio + phy + maths
prin("obtained marks:", a)
totalmarks = 850
prin("total marks:", totalmarks)
percentage = (a / totalmarks) * 100
prin("percentage:", percentage)

#i have removed "t" from 4 "print"
