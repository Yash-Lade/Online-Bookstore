
<h1> Online Book Store </h1>

<h1> File Structure </h1>

```
bookstore/
├── config/              # project settings
├── apps/
│   ├── users/           # auth & profiles
│   ├── books/           # catalog
│   ├── cart/            # shopping cart
│   ├── orders/          # order lifecycle
│   ├── reviews/         # ratings & reviews
├── common/              # shared utilities
└── manage.py
```

<h2> Standard Cart Stucture </h2>s


User
  └── Cart (OneToOne)
         └── CartItem (Many)
                └── Book (ForeignKey)
