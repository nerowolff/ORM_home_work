from models import Base, publisher, book, shop, stock, sale,drop_create_table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import username,password


DNS=f'postgresql://{username}:{password}@localhost:5432/HWdb'

engine=create_engine(DNS)

Session=sessionmaker(bind=engine)

session=Session()
for i in session.query(sale).all():
    print(i)
session.close()