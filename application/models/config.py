import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''
db = web.database(
    dbn='mysql', 
    host='localhost', 
    db='ria_edr', 
    user='ria', 
    pw='ria.2019', 
    port = 3306 
    )