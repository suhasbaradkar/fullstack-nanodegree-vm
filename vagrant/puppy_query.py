from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from database_setup_puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
import datetime
#from datetime import date , timedelta
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_one():
	result = session.query(Puppy.name).order_by(Puppy.name.asc()).all()

    # print the result with puppy name only
    # print len(result)
	for item in result:
		print item[0]
#query_one()

def query_two():
	today = datetime.date.today()
	if passesLeapDay(today):
		sixMonthsAgo = today - datetime.timedelta(days = 183)
	else:
		sixMonthsAgo = today - datetime.timedelta(days = 182)
	result = session.query(Puppy.name,Puppy.dateOfBirth)\
	.filter(Puppy.dateOfBirth >= sixMonthsAgo)\
	.order_by(Puppy.dateOfBirth.desc())
	for item in result:
		print "{name} : {dob}".format(name = item[0],dob = item[1])

def query_three():
	
	result = session.query(Puppy.name,Puppy.weight)\
	.order_by(Puppy.weight.asc())\
	.all()
	for item in result:
		print "{name} : {weight}".format(name = item[0],weight = item[1])		
		
def query_four():
	result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
	for item in result:
		print item[0].id,item[0].name, item[1]

def passesLeapDay(today):
    """
    Returns true if most recent February 29th occured after or exactly 183 days ago (366 / 2)
    """
    thisYear = today.timetuple()[0]
    if isLeapYear(thisYear):
        sixMonthsAgo = today - datetime.timedelta(days = 183)
        leapDay = datetime.date(thisYear, 2, 29)
        return leapDay >= sixMonthsAgo
    else:
        return False
        
def isLeapYear(thisYear):
    """
    Returns true iff the current year is a leap year.
    Implemented according to logic at https://en.wikipedia.org/wiki/Leap_year#Algorithm
    """
    if thisYear % 4 != 0:
        return False
    elif thisYear % 100 != 0:
        return True
    elif thisYear % 400 != 0:
        return False
    else:
        return True

#query_one()		
#query_two()
#query_three()
query_four()