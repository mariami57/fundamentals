import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
n = int(input())

for _ in range(n):
    barcode = input()
    product_group = ""
    match = re.findall(pattern, barcode)
    if match:
        for current_barcode in match:
            for char in current_barcode:
                if char.isdigit():
                    product_group += char
        if len(product_group) == 0:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
