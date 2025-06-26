# 📦 SQLAlchemy SQLite Store Database

This is a simple Python project demonstrating how to use **SQLAlchemy (a Python ORM)** with a **SQLite3 database**.  
It creates two related tables:
- `categories` (category_id, category_name)
- `products` (product_id, product_name, price, category_id)

The project inserts sample data into these tables and retrieves product details along with their associated category names.

---

## 📌 Project Structure

```

.
├── store.db               # SQLite database file (auto-created)
├── store\_script.py        # Main Python script
└── README.md              # This README file

````

---

## 📚 Technologies Used

- **Python 3**
- **SQLAlchemy ORM**
- **SQLite3 (via SQLAlchemy engine)**

---

## 📖 How It Works

1. **Connects to a SQLite database (`store.db`)**
2. **Creates two tables (`categories` and `products`)**
3. **Inserts sample category and product records**
4. **Fetches all products along with their category names**
5. **Displays the results in the terminal console**

---

## 📥 Installation & Setup

1. **Install SQLAlchemy**
   ```bash
   pip install SQLAlchemy
````

2. **Run the Python script**

   ```bash
   python store_script.py
   ```

---

## 📸 Screenshot — Terminal Output

*Add your terminal screenshot here after running the script*

> 📌 Example:

```
Product: Laptop, Price: ₹50000.0, Category: Electronics
Product: Smartphone, Price: ₹25000.0, Category: Electronics
Product: Rice, Price: ₹500.0, Category: Groceries
```

📷 **\[Insert your screenshot image here if hosting on GitHub or report]**

---

## ✅ Features

* Simple and clean SQLAlchemy ORM model definitions
* One-to-many relationship between `Category` and `Product`
* Automatic SQLite database file creation
* Console output of product and category information

---

## 📌 Notes

* The `category_id` is auto-generated as it is declared `Integer, primary_key=True`
* `store.db` file is created automatically on first run

---

## 📑 License

This project is free to use and learn from ✌️

````

---

## 📸 Screenshot Example  
After you run:
```bash
python store_script.py
````

The terminal will display:

![image](https://github.com/user-attachments/assets/37c11202-2362-4da6-a2d3-776713a166dc)

![image](https://github.com/user-attachments/assets/35b049ae-16cd-4de6-9568-1fbe194ce685)

![image](https://github.com/user-attachments/assets/b4a3be3a-0ffd-420a-8354-63deb0538ade)






