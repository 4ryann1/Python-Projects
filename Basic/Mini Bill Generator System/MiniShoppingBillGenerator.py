# Product database
products = {
    "Rice": 60,
    "Wheat": 45,
    "Sugar": 50,
    "Milk": 30,
    "Oil": 180,
    "Tea": 250,
    "Biscuits": 40,
    "Coffee": 180
}


# Display products
def display_products():
    print("\n====== AVAILABLE PRODUCTS ======")

    for product, price in products.items():
        print(f"{product:<15} ₹{price}")


# Take shopping input
def take_order():
    cart = {}

    while True:
        display_products()

        product = input("\nEnter product name (or 'done' to finish): ").title()

        if product == "Done":
            break

        if product not in products:
            print("❌ Product not available!")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        # Add product to cart
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity

    return cart


# Calculate bill
def calculate_bill(cart):
    subtotal = 0

    for product, quantity in cart.items():
        price = products[product]
        subtotal += price * quantity

    # Discount
    if subtotal >= 5000:
        discount_rate = 20
    elif subtotal >= 2000:
        discount_rate = 15
    elif subtotal >= 1000:
        discount_rate = 10
    else:
        discount_rate = 0

    discount = subtotal * discount_rate / 100

    # Amount after discount
    discounted_amount = subtotal - discount

    # GST
    gst = discounted_amount * 5 / 100

    # Final amount
    final_amount = discounted_amount + gst

    return subtotal, discount, gst, final_amount


# Display final bill
def display_bill(cart, subtotal, discount, gst, final_amount):

    print("\n")
    print("=" * 55)
    print("                 🛒 GROCERY BILL")
    print("=" * 55)

    print(f"{'Product':<15}{'Qty':<8}{'Price':<12}{'Total':<12}")
    print("-" * 55)

    for product, quantity in cart.items():
        price = products[product]
        total = price * quantity

        print(f"{product:<15}{quantity:<8}₹{price:<11}₹{total}")

    print("-" * 55)

    print(f"{'Subtotal':<40} ₹{subtotal:.2f}")
    print(f"{'Discount':<40} ₹{discount:.2f}")
    print(f"{'GST (5%)':<40} ₹{gst:.2f}")

    print("-" * 55)
    print(f"{'FINAL AMOUNT':<40} ₹{final_amount:.2f}")

    print("=" * 55)
    print("          Thank you for shopping! 🛍️")
    print("=" * 55)


# Main program
cart = take_order()

if len(cart) == 0:
    print("\n❌ No products were purchased.")

else:
    subtotal, discount, gst, final_amount = calculate_bill(cart)

    display_bill(
        cart,
        subtotal,
        discount,
        gst,
        final_amount
    )