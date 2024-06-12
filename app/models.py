from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class SeasonalFlavor(Base):
    __tablename__ = 'seasonal_flavors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

class CustomerSuggestion(Base):
    __tablename__ = 'customer_suggestions'
    id = Column(Integer, primary_key=True)
    flavor_name = Column(String, nullable=False)
    allergy_concern = Column(String)

class Allergen(Base):
    __tablename__ = 'allergens'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
