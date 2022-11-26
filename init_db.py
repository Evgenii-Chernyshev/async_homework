from sqlalchemy import create_engine, MetaData

from shop_app.settings import config
from shop_app.db import store, item, sales 


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[store, item, sales])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(store.insert(), [
        {'adress': 'adress 1'},
        {'adress': 'adress 2'},
        {'adress': 'adress 3'},
        {'adress': 'adress 4'},
        {'adress': 'adress 5'},
        {'adress': 'adress 6'},
        {'adress': 'adress 7'},
        {'adress': 'adress 8'},
        {'adress': 'adress 9'},
        {'adress': 'adress 10'},
        {'adress': 'adress 11'},

    ])

    conn.execute(item.insert(), [
        {'name': 'name 1', 'price': 100},
        {'name': 'name 2', 'price': 150},
        {'name': 'name 3', 'price': 50.5},
        {'name': 'name 4', 'price': 80},
        {'name': 'name 5', 'price': 70},
        {'name': 'name 6', 'price': 90},
        {'name': 'name 7', 'price': 110},
        {'name': 'name 8', 'price': 120.5},
        {'name': 'name 9', 'price': 130,},
        {'name': 'name 10', 'price': 140},
        {'name': 'name 11', 'price': 200},
        {'name': 'name 12', 'price': 10000},

    ])

    conn.execute(sales.insert(), [
        {'item_id': 1, 'store_id': 1},
        {'item_id': 1, 'store_id': 2},
        {'item_id': 3, 'store_id': 1},
        {'item_id': 3, 'store_id': 3},
        {'item_id': 3, 'store_id': 3},
        {'item_id': 3, 'store_id': 4},
        {'item_id': 3, 'store_id': 5},
        {'item_id': 3, 'store_id': 6},
        {'item_id': 3, 'store_id': 7},
        {'item_id': 3, 'store_id': 8},
        {'item_id': 3, 'store_id': 9},
        {'item_id': 3, 'store_id': 10},
        {'item_id': 3, 'store_id': 11},
    ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)