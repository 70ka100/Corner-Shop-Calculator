Bubblegum = 202
Toffee = 118
Ice_cream = 2250
Milk_chocolate = 1680
Doughnut = 1075
Pancake = 80
Income = Bubblegum + Toffee + Ice_cream + Milk_chocolate + Doughnut + Pancake
print("Earned amount:")
print("Bubblegum: $", Bubblegum, sep='')
print("Toffee: $", Toffee, sep='')
print("Ice cream: $", Ice_cream, sep='')
print("Milk chocolate: $", Milk_chocolate, sep='')
print("Doughnut: $", Doughnut, sep='')
print("Pancake: $", Pancake, sep='')
print()
print("Income: $", Income, sep='')
print("Staff expenses:")
Staff = int(input())
print("Other expenses:")
Other = int(input())
print("Net income: $", Income - (Staff + Other), sep='')

# Earned amount:
# Bubblegum: $202
# Toffee: $118
# Ice cream: $2250
# Milk chocolate: $1680
# Doughnut: $1075
# Pancake: $80
#
# Income: $5405
# Staff expenses:
# > 2000
# Other expenses:
# > 205
# Net income: $3200

# Earned amount:
# Bubblegum: $202
# Toffee: $118
# Ice cream: $2250
# Milk chocolate: $1680
# Doughnut: $1075
# Pancake: $80
#
# Income: $5405
# Staff expenses:
# > 5203
# Other expenses:
# > 400
# Net income: $-198
