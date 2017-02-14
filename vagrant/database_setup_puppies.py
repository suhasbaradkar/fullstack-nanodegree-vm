import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String , Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Shelter(Base):
	__tablename__ = 'shelter'
	id = Column(Integer, primary_key=True)
	name = Column(String(250))
	address = Column(String(250))
	city = Column(String(80))
	state = Column(String(80))
	zipCode = Column(String(10))
	website = Column(String)
	
    
 
class Puppy(Base):
	__tablename__ = 'puppy'
	id = Column(Integer, primary_key = True)
	name =Column(String(80), nullable = False)
	dateOfBirth = Column(Date)
	gender = Column(String(6),nullable = False)
	weight = Column(Integer,nullable = False)
	picture = Column(String(80),nullable = True)
	shelter_id = Column(Numeric(10),ForeignKey('shelter.id'))
	shelter = relationship(Shelter) 
	
    
 

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)