kanelbulle = 35
day_old_kanelbulle = kanelbulle * 0.6

print(day_old_kanelbulle)
print("How many day-old kanelbullar do you want to buy?")
amount = int(input())

price = amount * kanelbulle
print("The original price for {} fresh kanelbullar would have been {:.2f} SEK.".format(amount, price))

discountedPrice = amount * day_old_kanelbulle
discount = price - discountedPrice
print("You saved {:.2f} SEK for buying {} day-old kanelbullar instead of {} fresh kanelbullar.".format(discount, amount, amount))
print("The total price for {} day-old kanelbullar is {:.2f} SEK.".format(amount, discountedPrice))