import csv
from datetime import datetime

with open("restaurant_sales_dataset.csv", encoding="utf-8-sig", newline="") as src, \
     open("restaurant_sales.txt", "w", encoding="utf-8", newline="") as dst:

    reader = csv.DictReader(src)
    writer = csv.writer(dst, delimiter="\t", lineterminator="\n")

    for row in reader:
        dt = datetime.strptime(row["Date"].strip(), "%Y-%m-%d %H:%M:%S")

        writer.writerow([
            dt.strftime("%Y-%m-%d"),
            dt.strftime("%H:%M:%S"),
            row["Restaurant_Location"].strip(),
            row["Menu_Item_Name"].strip(),
            row["Total_Price"].strip(),
            row["Payment_Method"].strip()
        ])