# Online Shop — Backend

Django backend (SQLite). Kosmetika/online do'kon uchun skelet.

## Apps
- `products` — to'liq modellar: `Banner`, `Category`, `Brand`, `Product`, `ProductImage`
- `users`, `orders`, `cart`, `delivery` — bo'sh skeletlar (modellar keyinroq qo'shiladi)

## Ishga tushirish

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin panel: http://127.0.0.1:8000/admin/
