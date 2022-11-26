import aiopg.sa
import sqlalchemy as sa

__all__ = ['store', 'item', 'sales']

meta = sa.MetaData()

store = sa.Table(
    'store', meta,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('adress', sa.String(200), nullable=False)
)

item = sa.Table(
    'item', meta,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(200), nullable=False),
    sa.Column('price', sa.Float, server_default="0", nullable=False)

)

sales = sa.Table(
    'sales', meta,

    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('sale_time' , sa.Date, server_default="now()", nullable=False),

    sa.Column('item_id',
           sa.Integer,
           sa.ForeignKey('item.id', ondelete='CASCADE')),
    
    sa.Column('store_id',
           sa.Integer,
           sa.ForeignKey('store.id', ondelete='CASCADE'))
)

async def pg_context(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()