from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base , Restaurant , MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
#connection with DB 
# for session commands 
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "bhukkad")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()

cheesepizza = MenuItem(name = "Cheese Pizza", description ="Most boring pizza in world", course = "Entree",price = "$9.95",restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()

