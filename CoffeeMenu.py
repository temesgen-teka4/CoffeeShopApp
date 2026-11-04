import json
from datetime import datetime

class Coffee:
    """Represents an individual coffee item on the menu."""
    def __init__(self, item_id: int, name: str, price: float):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f}"


class Menu:
    """Manages the catalog of available coffee products."""
    def __init__(self):
        self._items: list[Coffee] = [
            Coffee(1, "Espresso", 30.00),
            Coffee(2, "Latte", 35.00),
            Coffee(3, "Cappuccino", 40.00),
            Coffee(4, "Mocha", 45.00)
        ]

    def display(self):
        print("\n" + "=" * 32)
        print("          COFFEE MENU          ")
        print("=" * 32)
        for item in self._items:
            print(f"[{item.item_id}] {item.name:<12} | ${item.price:.2f}")
        print("=" * 32)

    def get_item(self, item_id: int) -> Coffee | None:
        for item in self._items:
            if item.item_id == item_id:
                return item
        return None


class Order:
    """Manages customer cart items, totals, checkout, and persistence."""
    def __init__(self):
        self._items: list[tuple[Coffee, int]] = []  # Stores tuples of (Coffee object, quantity)

    def add_item(self, coffee: Coffee, quantity: int = 1):
        for i, (item, qty) in enumerate(self._items):
            if item.item_id == coffee.item_id:
                self._items[i] = (item, qty + quantity)
                print(f"Updated {coffee.name} quantity to {qty + quantity}.")
                return
        self._items.append((coffee, quantity))
        print(f"Added {quantity}x {coffee.name} to your order.")

    @property
    def total(self) -> float:
        return sum(item.price * qty for item, qty in self._items)

    def show_summary(self):
        if not self._items:
            print("\nYour order cart is currently empty.")
            return
        print("\n" + "-" * 36)
        print("            ORDER SUMMARY           ")
        print("-" * 36)
        for i, (item, qty) in enumerate(self._items, 1):
            subtotal = item.price * qty
            print(f"{i}. {item.name} x{qty} — ${subtotal:.2f}")
        print("-" * 36)
        print(f"Total Amount Due: ${self.total:.2f}")
        print("-" * 36)

    def checkout(self) -> bool:
        if not self._items:
            print("\nYour cart is empty. Add items before checking out.")
            return False
        
        self.show_summary()
        confirm = input("\nProceed to checkout? (yes/no): ").strip().lower()
        if confirm in ['y', 'yes']:
            print("\nOrder confirmed! Thank you for your purchase.")
            self._save_receipt()
            self._items.clear()
            return True
        else:
            print("\nCheckout cancelled.")
            return False

    def _save_receipt(self):
        """Logs completed transaction records to a local JSON file."""
        receipt_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": [{"name": item.name, "quantity": qty, "price": item.price} for item, qty in self._items],
            "total": self.total
        }
        try:
            with open("receipts.json", "a") as f:
                f.write(json.dumps(receipt_data) + "\n")
            print("Transaction receipt successfully archived.")
        except Exception as e:
            print(f"Warning: Could not save receipt log ({e})")


class CoffeeShopApp:
    """Main application controller managing the runtime lifecycle."""
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def run(self):
        print("☕ Welcome to the Professional Coffee Shop System! ☕")
        while True:
            self.menu.display()
            print("5. View Order")
            print("6. Checkout")
            print("7. Exit")
            
            choice = input("\nSelect an option (1-7): ").strip()
            
            if choice in ['1', '2', '3', '4']:
                coffee = self.menu.get_item(int(choice))
                if coffee:
                    qty_input = input(f"Enter quantity for {coffee.name} [default 1]: ").strip()
                    qty = int(qty_input) if qty_input.isdigit() and int(qty_input) > 0 else 1
                    self.order.add_item(coffee, qty)
            elif choice == '5':
                self.order.show_summary()
            elif choice == '6':
                self.order.checkout()
            elif choice == '7':
                print("\nThank you for visiting. Have a wonderful day!")
                break
            else:
                print("\nInvalid choice. Please enter a valid number between 1 and 7.")


if __name__ == "__main__":
    app = CoffeeShopApp()
    app.run()