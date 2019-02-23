import web
        
urls = (
    '/', 'application.controllers.clientes.index.Index',
    '/insert', 'application.controllers.clientes.insert.Insert',
    '/update/(.*)', 'application.controllers.clientes.update.Update',
    '/delete/(.*)', 'application.controllers.clientes.delete.Delete',
    '/view/(.*)', 'application.controllers.clientes.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
