
class Product:
    def __init__(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.pid}. {self.name} - ₹{self.price} (Stock: {self.stock})"p


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.items.append(CartItem(product, quantity))
            print(f"✅ Added {quantity} x {product.name} to cart.")
        else:
            print("❌ Not enough stock!")

    def view_cart(self):
        if not self.items:
            print("🛒 Cart is empty.")
            return
        print("\n🛒 Your Cart:")
        total = 0
        for item in self.items:
            print(f"- {item.product.name} x {item.quantity} = ₹{item.total_price()}")
            total += item.total_price()
        print(f"Total: ₹{total}\n")

    def checkout(self):
        if not self.items:
            print("❌ Cart is empty! Add items first.")
        else:
            total = sum(item.total_price() for item in self.items)
            print(f"\n💳 Checkout successful! Total amount: ₹{total}")
            self.items.clear()


# ===============================
# App Simulation
# ===============================
def main():
    # Create some products
    products = [
        Product(1, "Laptop", 50000, 5),
        Product(2, "Headphones", 1500, 10),
        Product(3, "Smartphone", 20000, 8),
        Product(4, "Keyboard", 1200, 6)
    ]

    cart = ShoppingCart()

    while True:
        print("\n=== Online Shopping App ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n📦 Available Products:")
            for p in products:
                print(p)

        elif choice == "2":
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            product = next((p for p in products if p.pid == pid), None)
            if product:
                cart.add_item(product, qty)
            else:
                print("❌ Invalid product ID.")

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            cart.checkout()

        elif choice == "5":
            print("👋 Thank you for shopping with us!")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
