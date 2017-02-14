from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem
#from flask.ext.sqlalchemy import SQLAlchemy
#import datetime
#from datetime import date , timedelta
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_all():
	result = session.query(Restaurant.name,Restaurant.id).order_by(Restaurant.name.asc()).all()
	return result
    # Returns list of restautant names alphbatically 
def add_restaurant(Name):
	restaurant1 = Restaurant(name=Name)
	session.add(restaurant1)
	session.commit()

def return_restaurantName(num):
	result = session.query(Restaurant).get(num)
	print result.name
	return result.name

def rename_restaurantName(Name1,id1):
	result = session.query(Restaurant).get(id1)
	#print(result.name)
	result.name = Name1
	session.add(result)
	session.commit()

def delete_restaurant(id1):
	result = session.query(Restaurant).get(id1)
	#print(result.name)
	session.delete(result)
	session.commit()

#rename_restaurantName("Suhas' Desi Tadka",10)
#return_restaurantName(10)
#delete_restaurantName(10)