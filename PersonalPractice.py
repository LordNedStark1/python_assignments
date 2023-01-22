amount = float(input("Enter amount in decimal: "))
amount_by_hundred = amount *100

dollar = amount_by_hundred // 100
cent = amount_by_hundred % 100

quarters =cent //25
cent_two = cent % 25

dimes = cent_two // 10
cent_three = cent_two % 10

nickel = cent_three// 5
pennies = cent_three % 5


print("Your amount", amount, "consists of\n",
 "\t", dollar, "dollars\n",
 "\t", quarters, "quarters\n",
 "\t", dimes, "dimes\n",
 "\t", nickel, "nickels\n",
 "\t", pennies, "pennies")
