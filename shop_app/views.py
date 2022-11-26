from aiohttp import web
import db
import datetime

async def stores(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.store.select())
        records = await cursor.fetchall()
        stores = [dict(s) for s in records]
        return web.Response(text=str(stores))


async def items(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.item.select())
        records = await cursor.fetchall()
        items = [dict(s) for s in records]
        return web.Response(text=str(items))


async def top_stores(request):
    async with request.app['db'].acquire() as conn:
        stmt = db.sa.select(db.store.c.id, db.store.c.adress, db.sa.func.sum(db.item.c.price).label("total_sum")). \
            select_from(db.sales).join(db.store).join(db.item).group_by(db.store.c.id, db.store.c.adress).\
                order_by(db.sa.func.sum(db.item.c.price).desc()).limit(10)

        cursor = await conn.execute(stmt)
        records = await cursor.fetchall()
        result = [dict(i) for i in records]
        return web.Response(text=str(result))

async def top_sold(request):
    async with request.app['db'].acquire() as conn:
        stmt = db.sa.select(db.item.c.id, db.item.c.name, db.sa.func.count(db.sales.c.id).label("total_count")). \
                    join(db.sales).group_by(db.item.c.id, db.item.c.name).order_by(db.sa.func.count(db.sales.c.id).desc()).limit(10)

        cursor = await conn.execute(stmt)
        records = await cursor.fetchall()
        result = [dict(i) for i in records]
        return web.Response(text=str(result))

async def sales(request):
    async with request.app['db'].acquire() as conn:
        data = await request.json()

        try:
            item_id = int(data['item_id'])
            store_id = int(data['store_id'])
        except (KeyError, TypeError, ValueError) as e:
            raise web.HTTPBadRequest(text='You have not specified coreect value') from e
        
        stmt = db.sa.insert(db.sales).values(item_id=item_id, store_id=store_id)

        await conn.execute(stmt)

        return web.Response(text="Ok")



 