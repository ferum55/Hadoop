import sys

for line in sys.stdin:
    fields = line.strip().split("\t")

    if len(fields) != 6:
        continue

    product = fields[3]

    try:
        amount = float(fields[4])
    except ValueError:
        continue

    print(f"{product}\t{amount}")