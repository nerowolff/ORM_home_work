import sqlalchemy as sq
from sqlalchemy.orm import declarative_base,relationship

Base=declarative_base()



def drop_create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class publisher(Base):
    __tablename__= "publisher"
    id = sq.Column(sq.Integer, primary_key= True)
    name = sq.Column(sq.String(length=40), unique=True)
    def __str__(self):
        return f'ID {self.id}, Name: {self.name}'

class book(Base):
    __tablename__= "book"
    id = sq.Column(sq.Integer, primary_key= True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher=sq.Column(sq.Integer,sq.ForeignKey('publisher.id'))
    publisher=relationship(publisher, backref='books')
    def __str__(self):
        return f'Издатель: {self.publisher}, Описание : {self.title}'

class shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer,primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}'

class stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer,primary_key=True)
    id_book = sq.Column(sq.Integer,sq.ForeignKey('book.id'))
    book = relationship(book, backref='book_stocks')
    id_shop = sq.Column(sq.Integer,sq.ForeignKey('shop.id'))
    shop = relationship(shop, backref='shop_stocks')
    count=sq.Column(sq.Integer,unique=False)
    def __str__(self):
        return f'в магазине: {self.shop}, продаж: {self.count}'

class sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer,primary_key = True)
    price = sq.Column(sq.Numeric(10, 2))
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer,sq.ForeignKey('stock.id'))
    stock = relationship(stock,backref = 'sales')
    count = sq.Column(sq.Integer,nullable=False)
    def __str__(self):
        return f'{self.date_sale} : {self.count} по цене : {self.price}'