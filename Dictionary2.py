d2={}
#printing menu
while True:
  print("MENU\n 1. Insert Sports and their Countries\n 2. Display Countries\n 3. Display Sports\n 4. Get Countries\n 5. Delete")
  inp=int(input("Enter your choice: "))
  if inp == 1:
    sports=input("Enter a Sport: ")
    countries=input("Enter a Country: ")
    d2[sports]=countries
    print(d2)
  elif inp == 2:
    print(d2.values())
  elif inp == 3:
    print(d2.keys())
  elif inp == 4:
    sport=input("Enter a Sport: ")
    print(d2[sport])
  elif inp == 5:
    delete=input("Which Sport are you going to delete?: ")
    del(d2[delete])
  else:
    print("Whoops, try again")