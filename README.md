# ☕ Coffee Shop Terminal Application

A clean, object-oriented command-line coffee ordering system built in Python. This application allows users to browse a dynamic coffee menu, manage order quantities, calculate totals, securely handle checkouts, and automatically archive transaction receipts locally.

---

## 🚀 Features

* **Object-Oriented Design:** Clean separation of concerns across `Coffee`, `Menu`, `Order`, and `CoffeeShopApp` classes.
* **Smart Cart Management:** Add multiple quantities of items, update existing selections automatically, and view detailed order breakdowns.
* **Transaction Archiving:** Automatically logs completed orders and timestamps into a local `receipts.json` file.
* **Robust Input Validation:** Bulletproof error handling to ensure smooth user navigation and prevent crashes on invalid inputs.

---

## 🛠️ Prerequisites

* Python 3.8 or higher installed on your machine.

---

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/temesgen-teka4/CoffeeShopApp.git](https://github.com/temesgen-teka4/CoffeeShopApp.git)
   cd CoffeeShopApp


 ## Usage Guide
   when u run the Application You will see
 ================================
          COFFEE MENU          
================================
[1] Espresso     | $30.00
[2] Latte        | $35.00
[3] Cappuccino   | $40.00
[4] Mocha        | $45.00
================================
5. View Order
6. Checkout
7. Exit

Select an item (1-4): Enter the menu number and specify the desired quantity.

View Order (5): Display all items currently in your cart along with the running total.

Checkout (6): Review your order summary, confirm purchase, and generate an archived transaction record.

Exit (7): Quit the application.



## Project Structure

CoffeeShopApp/
│
├── CoffeeMenu.py     # Main application runtime and classes
├── receipts.json     # Automatically generated transaction logs
└── README.md         # Project documentation


👨‍💻 Author
Temesgen Teka

GitHub: @temesgen-teka4