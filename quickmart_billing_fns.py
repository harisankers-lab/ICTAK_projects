cart = [
{"name": "Notebook", "category": "Stationery", "price": 40, "qty": 5},
{"name": "Pen", "category": "Stationery", "price": 10, "qty": 11},
{"name": "Biscuits", "category": "Snacks", "price": 25, "qty": 4},
{"name": "Juice", "category": "Drinks", "price": 45, "qty": 3},
{"name": "Chips", "category": "Snacks", "price": 20, "qty": 6},
]

def line_total(item):
  return item["price"]*item["qty"]

def subtotal(cart):
  return sum(line_total(item) for item in cart)

def apply_discount(amount, percent=0):
  return amount - amount*(percent/100)

def gst(amount, rate=18):
  return amount*(rate/100)

def category_totals(cart):
  total_values = {}
  for item in cart:
    cat = item["category"]
    total_values[cat] = total_values.get(cat, 0) + line_total(item)
  return total_values

def top_items(cart, n=2):
  sorted_list = sorted(cart, key=line_total, reverse=True)
  return [item["name"] for item in sorted_list[:n]]


def print_bill(cart, discount_percent=0):
  print(f"{"Item":<10}{"Price":>6}{"Qty":>5}{"Total":>8}")
  print(f"{"-"*29}")
  for item in cart:
    print(f"{item["name"]:<10}{item["price"]:>6}{item["qty"]:>5}{line_total(item):>8}")
  print(f"{"-"*29}")
  print(f"{"Subtotal":<10}{subtotal(cart):>19.2f}")
  after_dis = apply_discount(subtotal(cart), 10)
  discount = subtotal(cart) - after_dis
  print(f"{"Discount 10%":<10}{discount:>17.2f}")
  print(f"{"GST 18%":<10}{gst(after_dis):>19.2f}")
  grand = after_dis + gst(after_dis)
  print(f"{"Grand Total":<10}{grand:>18.2f}")

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