## ML Project
Retail-Management-System/
│
├── app.py      # Main Streamlit app
│
├── database/
│   ├── db_connection.py
│   ├── product_db.py
│   ├── supplier_db.py
│   ├── sales_db.py
│   └── customer_db.py
│
├── pages/
│   ├── 1_Billing.py
│   ├── 2_Inventory.py
│   ├── 3_Suppliers.py
│   ├── 4_Sales_Dashboard.py
│   ├── 5_Recommendations.py
│   └── 6_Forecasting.py
│
├── ml/
│   ├── recommendation.py
│   ├── demand_forecasting.py
│   └── train_model.py
│
├── services/
│   ├── billing_service.py
│   ├── inventory_service.py
│   ├── supplier_service.py
│   └── analytics_service.py
│
├── utils/
│   ├── pdf_generator.py
│   ├── charts.py
│   └── helpers.py
│
├── models/
│   ├── product.py
│   ├── supplier.py
│   ├── customer.py
│   └── sale.py
│
├── data/
│   ├── products.csv
│   ├── sales.csv
│   └── suppliers.csv
│
├── assets/
│   ├── logo.png
│   └── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore
└── config.py