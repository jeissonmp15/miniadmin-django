import sqlite3
con = sqlite3.connect('db.sqlite3')

print(con)

cur = con.cursor()
query = """INSERT INTO "clientes_clientes" (nombre, nit, nombre_contacto, telefono, direccion, correo)
VALUES ('OSP', '21315254', 'Jeisson Manrique', 1241253, 'Calle 1', 'jeissonmp15@gmail.com')"""
cur.execute(query)

con.commit()

con.close()