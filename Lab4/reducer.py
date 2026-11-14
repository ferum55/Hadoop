import sys

current_product = None
total = 0.0

for line in sys.stdin:
    fields = line.strip().split("\t")

    if len(fields) != 2:
        continue

    product = fields[0]

    try:
        amount = float(fields[1])
    except ValueError:
        continue

    if product == current_product:
        total += amount
    else:
        if current_product is not None:
            print(f"{current_product}\t{total:.2f}")

        current_product = product
        total = amount

if current_product is not None:
    print(f"{current_product}\t{total:.2f}")