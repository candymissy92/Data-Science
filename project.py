# ---------------- Product Classes ----------------
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ₹{self.price}"


class ClothingProduct(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def __str__(self):
        return f"[{self.product_id}] {self.name} (Size: {self.size}) - ₹{self.price}"


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, file_size):
        super().__init__(product_id, name, price)
        self.file_size = file_size

    def __str__(self):
        return f"[{self.product_id}] {self.name} (Digital, {self.file_size}MB) - ₹{self.price}"


# ---------------- Cart Classes ----------------
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ₹{self.get_total_price()}"


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def apply_discount(self, code):
        discounts = {"WELCOME10": 10, "SAVE20": 20}
        if code in discounts:
            self.discount = discounts[code]
            print(f"✅ Discount code applied: {self.discount}% off")
        else:
            print("❌ Invalid discount code.")

    def get_total(self):
        total = sum(item.get_total_price() for item in self.items)
        if self.discount > 0:
            total -= total * self.discount / 100
        return total

    def view_cart(self):
        if not self.items:
            print("🛒 Your cart is empty.")
        else:
            print("\n🛍️ Items in your cart:")
            for item in self.items:
                print(item)
            print(f"Total (after discount) = ₹{self.get_total()}")


# ---------------- User & Admin ----------------
class User:
    def __init__(self, username):
        self.username = username
        self.cart = ShoppingCart()


class Admin:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("\n📦 Available Products:")
        for p in self.products:
            print(p)


# ---------------- Payment ----------------
class PaymentGateway:
    def process_payment(self, amount):
        print(f"\nProcessing payment of ₹{amount}...")
        print("💳 Payment Successful! 🎉")


# ---------------- Main App ----------------
def shopping_app():
    # Admin setup
    admin = Admin()
    admin.add_product(Product(1, "Laptop", 55000))
    admin.add_product(ClothingProduct(2, "T-Shirt", 999, "M"))
    admin.add_product(DigitalProduct(3, "E-Book", 299, 5))
    admin.add_product(Product(4, "Headphones", 2500))

    username = input("Enter your name: ")
    user = User(username)
    print(f"\n👋 Welcome {user.username} to the Online Shop!")

    while True:
        print("\n========= MENU =========")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Apply Discount Code")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            admin.list_products()

        elif choice == "2":
            admin.list_products()
            try:
                pid = int(input("Enter Product ID to add: "))
                qty = int(input("Enter quantity: "))
                product = next((p for p in admin.products if p.product_id == pid), None)
                if product:
                    user.cart.add_item(product, qty)
                    print("✅ Item added to cart.")
                else:
                    print("❌ Invalid Product ID.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "3":
            try:
                pid = int(input("Enter Product ID to remove: "))
                user.cart.remove_item(pid)
                print("❌ Item removed.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "4":
            user.cart.view_cart()

        elif choice == "5":
            code = input("Enter discount code: ")
            user.cart.apply_discount(code)

        elif choice == "6":
            if not user.cart.items:
                print("🛒 Cart is empty. Add items before checkout.")
            else:
                total = user.cart.get_total()
                payment = PaymentGateway()
                payment.process_payment(total)
                print("🎉 Thank you for shopping with us!")
                break  # Exit after checkout

        elif choice == "7":
            print("👋 Goodbye! Visit again.")
            break

        else:
            print("❌ Invalid option. Please try again.")


# Run App
if __name__ == "__main__":
    shopping_app()
django-admin startproject shop_project
cd shop_project
python manage.py startapp shop_app

