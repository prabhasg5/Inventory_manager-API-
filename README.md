# Inventory_manager-API-
# 📦 Inventory Manager API

A backend API project for managing inventory items using **FastAPI** and **Couchbase**. This RESTful API allows users to perform CRUD operations on items such as products or tools, each with properties like `name`, `category`, `price`, and `stock status`.

---

## Live Demo

- **API Base URL:** [https://inventory-manager-api-qkd9.onrender.com](https://inventory-manager-api-qkd9.onrender.com)
- **Swagger Docs:** [https://inventory-manager-api-qkd9.onrender.com/docs](https://inventory-manager-api-qkd9.onrender.com/docs)

---

## Features

- Built with FastAPI for high-performance backend
-  Swagger UI for interactive API testing
-  Asynchronous endpoints using `async`/`await`
-  Full CRUD (Create, Read, Update, Delete) support
-  Basic error handling (404 Not Found, 500 Server Error)
-  JSON data modeling via Pydantic
-  UUID-based item ID generation
-  Couchbase NoSQL integration for scalable storage
-  Docker support for simple and consistent deployment

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI
- **Database:** Couchbase
- **Language:** Python 3.x
- **Others:** Uvicorn, Pydantic, Docker

---

##  Installation & Setup

### 🖥️ Run Locally
# 1. Clone the repository
git clone https://github.com/prabhasg5/Inventory_manager-API-.git
cd Inventory_manager-API-

# 2. (Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add environment variables
# Create a `.env` file in the root directory with:
COUCHBASE_HOST=localhost
COUCHBASE_USERNAME=Administrator
COUCHBASE_PASSWORD=password
COUCHBASE_BUCKET=inventory

# 5. Run the application
uvicorn main:app --reload
