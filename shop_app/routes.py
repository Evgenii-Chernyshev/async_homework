from views import stores, items, top_stores, top_sold, sales

def setup_routes(app):
    app.router.add_get('/stores', stores)
    app.router.add_get('/items', items)
    app.router.add_get('/top_stores', top_stores)
    app.router.add_get('/top_sold', top_sold)
    app.router.add_post('/sales', sales)