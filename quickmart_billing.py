# quickmart_billing.py - QuickMart Billing System
cart = [
{"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
{"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
{"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
{"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
{"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]

from quickmart_billing_fns import line_total, subtotal, apply_discount, gst, category_totals, top_items, print_bill

def main():
    print("TASK 1: Line total")
    print(line_total(cart[0]))

    print("\nTASK 2: Subtotal")
    print(subtotal(cart))

    print("\nTASK 3: Discount")
    print(apply_discount(500))
    print(apply_discount(500, 10))

    print("\nTASK 4: GST")
    print(gst(100))
    print(gst(100, 5))

    print("\nTASK 5: Category totals")
    for key, val in category_totals(cart).items():
        print(f"{key:<12}{val}")

    print("\nTASK 6: Top items")
    print(top_items(cart))
    print(top_items(cart, n=3))

    print("\nTASK 7: Bill")
    print_bill(cart, 10)      
main()