from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Use MySQL with root user
DATABASE_URL = "mysql+pymysql://root:root@localhost/sentimentdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)  # ADDED LENGTH (255)
    password = Column(String(255))  # ADDED LENGTH (255)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    review_text = Column(String(1000))  # ADDED LENGTH (1000)
    sentiment = Column(String(50))  # ADDED LENGTH (50)
    explanation = Column(String(2000))  # ADDED LENGTH (2000)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)
