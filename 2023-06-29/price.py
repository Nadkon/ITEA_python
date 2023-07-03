price = int(input('enter the price '))
qty = int(input('enter tyhe qty '))

total = price * qty
if qty > 10:
    total = total - (total * 0.1)

print(total)