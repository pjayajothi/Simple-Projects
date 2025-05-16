#Write a program that receives three inputs (given):
  #A list of prices
  #A list of item names
  #A budget per item
#The program should print:
  #A list of items that you can afford within your budget
  #How much budget would you need if you bought all of the affordable items
  #How many items you couldn't afford


prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = [item for item, price in zip(items, prices) if price <= budget_per_item]
cant_afford = sum(1 for price in prices if price > budget_per_item)
total_needed = sum(price for price in prices if price <= budget_per_item)

# Write your code below




print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
