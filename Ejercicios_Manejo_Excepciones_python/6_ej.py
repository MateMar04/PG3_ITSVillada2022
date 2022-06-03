import mysql.connector

cnx = mysql.connector.connect(user='bdi', password='pepe1234', host='127.0.0.1', database='PALADINI')

cursor = cnx.cursor()

try:
    add_medic = ("INSERT INTO MEDICOS "
                 "(dni, nombre, apellido)"
                 "VALUES (%s, %s, %s)")

    data_medic = (45934473, 'Mateo', 'Marchisone')  # Ya hay un dato con esta primary key

    cursor.execute(add_medic, data_medic)
    cnx.commit()
except mysql.connector.Error:
    print("No se pudo ingresar este dato en la base de datos")

cursor.close()
cnx.close()
