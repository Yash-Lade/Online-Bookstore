<h1>📚 Online Book Store API (Django REST Framework) </h1>

<h4> A fully functional RESTful backend for an Online Book Store built using Django and Django REST Framework. </h4>

<h4>This project demonstrates production-grade backend architecture including authentication, cart management, order processing with transactions, and review aggregation. </h4>

<h3>🚀 Features <br> 🔐 Authentication (JWT-Based)</h3>

- User Registration
- User Login
- User Logout (Token Blacklisting)
- User Profile
- JWT Access & Refresh Tokens
- Protected Endpoints

<h3>📖 Book Catalog </h3>

- Browse all books
- View book details
- Search by title & author
- Filter by genre
- Sort by price and date
- Pagination support

<h3>🛒 Shopping Cart </h3>

- Add books to cart
- Update quantity
- Remove books
- View cart
- Auto-create cart per user

<h3>📦 Order Management </h3>

- Place order (atomic transaction)
- Automatic stock validation
- Stock deduction on purchase
- Order history
- Order status management

<h3>⭐ Reviews & Ratings </h3>

- One-user-one-review rule
- 1–5 rating validation
- Average rating aggregation
- View all reviews for a book

<h3>🏗 Tech Stack </h3>

- Python
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- PostgreSQL (Development DB)
- Vercel (Deployment)

```
📂 Project Structure
bookstore/
│
├── users/      # Authentication & user management
├── books/      # Book catalog
├── cart/       # Shopping cart logic
├── orders/     # Order management & transactions
├── reviews/    # Reviews & ratings
│
└── bookstore/  # Project settings & root configuration

```
Each app follows separation of concerns and modular architecture.

<h3>⚙️ Installation & Setup </h3>
<h3>1️⃣ Clone the Repository </h3>

```
git clone <your-repo-url>
cd bookstore
```
<h3>2️⃣ Create Virtual Environment</h3>
  
```
python -m venv venv
.venv\Scripts\activate  # Windows
```
<h3>3️⃣ Install Dependencies</h3>
  
```
pip install -r requirements.txt
```

If no requirements file:
```
pip install django djangorestframework djangorestframework-simplejwt django-filter
```
<h3>4️⃣ Apply Migrations</h3>

```
python manage.py makemigrations
python manage.py migrate
```
<h3>5️⃣ Create Superuser</h3>

```
python manage.py createsuperuser
```
<h3>6️⃣ Run Server</h3>

```
python manage.py runserver
```

Server runs at:
```
http://127.0.0.1:8000/
```

Admin panel:
```
http://127.0.0.1:8000/admin/
```
<h3>🔑 Authentication Flow </h3>
<h3>Register </h3>

```
POST /api/users/register/
```
<h3>Login </h3>

```
POST /api/users/login/
```

Returns:
- Access Token
- Refresh Token

<h3>Use Token </h3>

Attach header:

Authorization: Bearer <access_token>

<h3>Logout </h3>

```
POST /api/users/logout/
```
<h3>📖 Book APIs </h3>
<h3>List Books</h3>

```
GET /api/books/
```
<h3>Search</h3>

```
GET /api/books/?search=harry
```
<h3>Filter</h3>

```
GET /api/books/?genre=fiction
```
<h3>Sort</h3>

```
GET /api/books/?ordering=price
```
<h3>Pagination</h3>

```
GET /api/books/?page=2
```
<h3>🛒 Cart APIs</h3>
<h3>View Cart</h3>

```
GET /api/cart/
```
<h3>Add to Cart</h3>

```
POST /api/cart/add/
```

Body:
```
{
  "book_id": 1,
  "quantity": 2
}
```
<h3>Remove from Cart</h3>

```
POST /api/cart/remove/
```
<h3>📦 Order APIs</h3>
Place Order</h3>

```
POST /api/orders/place/
```

- Validates stock
- Deducts stock
- Clears cart
- Uses database transaction

<h3>Order History </h3>

```
GET /api/orders/history/
```
<h3>⭐ Review APIs </h3>
Create Review </h3>

```
POST /api/reviews/create/
```
```
{
  "book": 1,
  "rating": 5,
  "comment": "Excellent book"
}
```
<h3>View Reviews for Book </h3>

```
GET /api/reviews/<book_id>/
```

Returns:
- Average rating
- List of reviews

<h3>🧠 Key Backend Concepts Demonstrated </h3>

- Custom User Model
- JWT Authentication (Access + Refresh)
- Token Blacklisting
- One-to-One & ForeignKey relationships
- Unique Constraints
- Aggregation (Average rating)
- Database Transactions (@transaction.atomic)
- Query filtering & search
- Pagination
- Clean app modularization

<h3>🔒 Security Features </h3>

- Protected endpoints using IsAuthenticated
- JWT-based stateless authentication
- Refresh token blacklisting
- Stock validation before order placement
- One-review-per-user-per-book constraint

<h3>📌 Future Improvements </h3>

- API documentation using Swagger / DRF Spectacular
- Role-based permissions (Admin vs User)
- Review allowed only after purchase
- Payment gateway integration
- Production database (PostgreSQL)
- Docker deployment
- CI/CD integration

<h3>📄 License </h3>

This project is for educational and portfolio purposes.

<h3>👨‍💻 Author </h3>

Developed by Yash Lade
Backend API built using Django REST Framework
