"""
FreshKart 1 - SQLAlchemy Database Models
"""
import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, default="customer") # 'admin', 'supplier', 'customer'
    supplier_company_name = Column(String, nullable=True) # e.g. 'Ramesh Kirana Wholesale Co.'
    phone = Column(String, nullable=True)
    street_address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    pincode = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    products = relationship("Product", back_populates="supplier_user")

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_person = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    city = Column(String, nullable=True)

    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    original_price = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    rating = Column(Float, default=4.8)
    reviews_count = Column(Integer, default=100)
    image = Column(String, nullable=False)
    badge = Column(String, default="Fresh")
    discount = Column(String, default="10% OFF")
    description = Column(Text, nullable=True)
    nutrition = Column(Text, nullable=True)
    supplier_name = Column(String, default="FreshKart Direct Mandi") # e.g. 'Ramesh Kirana Wholesale Co.'
    
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    supplier_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    supplier = relationship("Supplier", back_populates="products")
    supplier_user = relationship("User", back_populates="products")

class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=True)
    date = Column(String, nullable=False)
    status = Column(String, default="Placed")
    total = Column(Float, nullable=False)
    delivery_json = Column(Text, nullable=True)
    items_json = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    product_id = Column(String, index=True, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class WishlistItem(Base):
    __tablename__ = "wishlist_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    product_id = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    discount_percent = Column(Float, nullable=False)
    min_order = Column(Float, default=0.0)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

class Location(Base):
    __tablename__ = "serviceable_locations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    pincode = Column(String, unique=True, index=True, nullable=False)
    delivery_time = Column(String, default="15 Mins")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    icon = Column(String, default="fa-solid fa-layer-group")

class RefundClaim(Base):
    __tablename__ = "refund_claims"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False)
    order_id = Column(String, index=True, nullable=False)
    reason = Column(String, nullable=False)
    upi_id = Column(String, nullable=True)
    details = Column(Text, nullable=False)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
