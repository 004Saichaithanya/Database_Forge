from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine=create_engine('sqlite:///store.db',echo=True)


Base=declarative_base()


class Category(Base):
    __tablename__='categories'
    category_id=Column(Integer,primary_key=True)
    category_name=Column(String,nullable=False)

    products=relationship("Product",back_populates="category")


class Product(Base):
    __tablename__='products'
    product_id=Column(Integer,primary_key=True)
    product_name=Column(String,nullable=False)
    price=Column(Float,nullable=False)
    category_id=Column(Integer,ForeignKey('categories.category_id'))

    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

# Add categories
category1 = Category(category_name='Electronics')
category2 = Category(category_name='Groceries')

session.add_all([category1, category2])
session.commit()

# Add products
product1 = Product(product_name='Laptop', price=50000.00, category=category1)
product2 = Product(product_name='Smartphone', price=25000.00, category=category1)
product3 = Product(product_name='Rice', price=500.00, category=category2)

session.add_all([product1, product2, product3])
session.commit()

# Retrieve and display products with their categories
products = session.query(Product).all()

for product in products:
    print(f"Product: {product.product_name}, Price: ₹{product.price}, Category: {product.category.category_name}")





