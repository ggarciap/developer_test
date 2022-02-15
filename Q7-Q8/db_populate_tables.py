
from datetime import date
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'my-secret-pw'
DB_NAME = 'db'
DB_PORT = '3306'

# Connect with the MySQL Server
cnx = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST,port=DB_PORT, database=DB_NAME)

# Buffered cursor
cur = cnx.cursor(buffered=True)

dict_person =  {
    0:['Joe', 'Borrow', date(9999, 1, 1,), None, None],
    1:['Ana', 'Haskel', date(9999, 1, 1,), None, None],
    2:['Trevor', 'Jackson', date(9999, 1, 1,), 2, 1],
    3:['Julia', 'Roberts', date(9999, 1, 1,), 2, 1],
    4:['James', 'Bond', date(9999, 1, 1,), 4, 1],
    5:['Robert', 'Craft', date(9999, 1, 1,), 2, 1],
    6:['Genaro', 'Garcia', date(9999, 1, 1,), 4, 6]
}

dict_address = {
    0:[1,'123th', 'Apt. 221', 'Alexandria', 'FL', '33160'],
    1:[2,'parkway 12th', 'Apt. 323', 'Golden Beach', 'FL', '33160'],
    2:[3,'Test av. ', 'Apt. 121', 'Arlington', 'VA', '22312'],
    3:[4,'Test St', 'Bldg. 2212', 'Baquita', 'CA', '33160'],
    4:[5,'343th', 'Apt. AB', 'Royal', 'IN', '33160'],
    5:[6,'parkway 76th', 'Apt. 2', 'Rue', 'AK', '22122'],
    6:[7,'test final av.', 'Apt. 213', 'Clarito', 'CA', '33161']
}

dict_email = {
    0:[1,'joe@gmail.com', 1],
    1:[2,'ana@gmail.com', 1],
    2:[3,'tevee@gmail.com', 1],
    3:[4,'juls@gmail.com', 0],
    4:[5,'jbond@gmail.com', 0],
    5:[6,'robcraft@gmail.com', 1],
    6:[7,'genarogp@gmail.com', 0]
}

try:
    # Inserting rows to Person Table
    for key in dict_person:
        new_person = (
    "INSERT INTO Person (first_name, last_name, birth_date, mother_id_info, father_id_info) "
    "VALUES (%s, %s, %s, %s, %s)")
        cur.execute(new_person,
                (dict_person[key][0], dict_person[key][1], dict_person[key][2], dict_person[key][3], dict_person[key][4]))
        cnx.commit()

    # Inserting rows to PersonAddress Table
    for key in dict_address:
        new_address = (
    "INSERT INTO PersonAddress (person_id_pk_person_address, address1, address2, city, state, zip) "
    "VALUES (%s, %s, %s, %s, %s, %s)")
        cur.execute(new_address,
                (dict_address[key][0], dict_address[key][1], dict_address[key][2], dict_address[key][3], dict_address[key][4], dict_address[key][5]))
        cnx.commit()


    # Inserting rows to PersonEmail Table
    for key in dict_email:
        new_email = (
    "INSERT INTO PersonEmail (person_id_pk_person_email, email_address, primary_email) "
    "VALUES (%s, %s, %s)")
        cur.execute(new_email,
                (dict_email[key][0], dict_email[key][1], dict_email[key][2]))
        cnx.commit()
    
    print('All rows inserted successfully.')

except mysql.connector.Error as err:
    print(err)
    exit(1)
cur.close()
cnx.close()