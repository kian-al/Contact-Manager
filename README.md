# 📇 Contact Manager (Python + Click + PostgreSQL + CSV)

A simple yet powerful CLI-based Contact Manager built with **Python**, **Click**, and **SQLAlchemy**, supporting both **PostgreSQL database storage** and **CSV import/export**.

This project allows you to create, search, update, delete and list contacts directly from the terminal.

---

## 🚀 Features

- ✔ Add new contacts  
- ✔ List all contacts  
- ✔ Search contacts by keyword  
- ✔ Get a contact by ID  
- ✔ Update fields of any contact  
- ✔ Delete a contact  
- ✔ Import contacts from CSV  
- ✔ Export contacts to CSV  
- ✔ Initialize PostgreSQL database  

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/contact-manager.git
cd contact-manager
2️⃣ Create virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
🗄️ Setting up PostgreSQL
Make sure PostgreSQL is installed and running.

Create database:
sql
Copy code
CREATE DATABASE contactdb;
Configure DB connection
In src/contact_manager/db.py, update this:

python
Copy code
DATABASE_URL = "postgresql://username:password@localhost:5432/contactdb"
🔧 Initialize Database
Before using the CLI, run:

bash
Copy code
python -m contact_manager init
You should see:

nginx
Copy code
DB initialized
🖥️ CLI Usage
Run any command like this:

bash
Copy code
python -m contact_manager <command>
📌 Available Commands
➕ Add a contact
bash
Copy code
python -m contact_manager add --first John --last Doe --email j@doe.com
📃 List contacts
bash
Copy code
python -m contact_manager list
🔍 Search contacts
bash
Copy code
python -m contact_manager search john
🔎 Get contact by ID
bash
Copy code
python -m contact_manager get 1
✏️ Update contact
bash
Copy code
python -m contact_manager update 1 --phone 0912000000 --notes "Friend"
🗑️ Delete contact
bash
Copy code
python -m contact_manager delete 1
📥 Import from CSV
CSV must contain columns such as:
first_name,last_name,email,phone,address,notes

bash
Copy code
python -m contact_manager import_csv contacts.csv
📤 Export to CSV
bash
Copy code
python -m contact_manager export_csv backup.csv
📁 Project Structure
css
Copy code
contact-manager/
│
├── src/
│   └── contact_manager/
│       ├── cli.py
│       ├── db.py
│       ├── repository.py
│       └── __init__.py
│
├── venv/
│
└── README.md
🧩 TODO (Future Improvements)
Add unit tests

Add validation for phone numbers

Add JSON export

Add colored output using Rich

Add Dockerfile

📜 License
MIT License
Feel free to use this project for learning or building your own CLI tools.

🧑‍💻 Author
Kian Almasi

