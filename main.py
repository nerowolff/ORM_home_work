from models import Base, publisher, book, shop, stock, sale,drop_create_table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
import json
from user import username,password
url='https://raw.githubusercontent.com/netology-code/py-homeworks-db/SQLPY-76/06-orm/fixtures/tests_data.json'
try:
    response = requests.get(url)
    with open('tests_data.json', 'w', encoding = 'UTF-8') as f:
        f.write(response.text)
except Exception as err:
    print(err)
if response.status_code == 200:
    try:
        DNS=f'postgresql://{username}:{password}@localhost:5432/HWdb'

        engine=create_engine(DNS)

        Session=sessionmaker(bind=engine)

        session=Session()

        drop_create_table(engine)

        with open('tests_data.json', 'r', encoding = 'UTF-8') as f:
            file=json.load(f)
            for item in file:
                if item['model'] ==  'publisher':
                    pub= publisher(
                        name=item["fields"]["name"], 
                        id =item["pk"]
                    )
                    session.add(pub)

                elif item['model'] == 'shop':
                    sp= shop(
                        id = item["pk"],
                        name = item["fields"]["name"]
                    )
                    session.add(sp) 

                elif item['model'] == "book":
                    bk=book(
                        title=item["fields"]["title"], 
                        id =item["pk"],
                        id_publisher= item["fields"]["id_publisher"]
                        )
                    session.add(bk)
                    
                elif item['model'] == "stock":
                    sk= stock(
                        id = item["pk"],
                        id_shop = item ["fields"]["id_shop"],
                        id_book = item ["fields"]["id_book"],
                        count = item ["fields"]["count"]
                    )
                    session.add(sk)
                elif item["model"] == "sale":
                    se= sale(
                        id = item["pk"],
                        price = item ["fields"]["price"],
                        date_sale = item ["fields"]["date_sale"],
                        count = item ["fields"]["count"],
                        id_stock = item ["fields"]["id_stock"]
                        )
                    session.add(se)
            session.commit()
            session.close()
        
    except Exception as err:
        session.rollback()
        print(f'Ошибка про добавлении данных {err}')

else:
    print(f'код ошибки {response.status_code}')