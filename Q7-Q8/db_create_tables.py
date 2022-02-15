import mysql.connector
from mysql.connector import errorcode

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'my-secret-pw'
DB_NAME = 'db'
DB_PORT = '3306'


TABLES = {}
TABLES['Person'] = (
    "CREATE TABLE `Person` ("
    "  `person_id` INT AUTO_INCREMENT,"
    "  `first_name` VARCHAR(50) NOT NULL,"
    "  `last_name` VARCHAR(50) NOT NULL,"
    "  `birth_date` DATE NOT NULL,"
    "  `mother_id_info` INT DEFAULT NULL,"
    "  `father_id_info` INT DEFAULT NULL,"
    "  PRIMARY KEY (`person_id`),"
    "  CONSTRAINT `fk_mother_id_info`FOREIGN KEY (`mother_id_info`) REFERENCES Person(`person_id`),"
    "  CONSTRAINT `fk_father_id_info` FOREIGN KEY (`father_id_info`) REFERENCES Person(`person_id`)"
    ") ENGINE=InnoDB")

TABLES['PersonAddress'] = (
    "CREATE TABLE `PersonAddress` ("
    "  `person_address_id` INT AUTO_INCREMENT,"
    "  `person_id_pk_person_address` INT,"
    "  `address1` VARCHAR(255),"
    "  `address2` VARCHAR(255),"
    "  `city` VARCHAR(255),"
    "  `state` VARCHAR(255),"
    "  `zip` INT(12),"
    "  PRIMARY KEY (`person_address_id`),"
    "  CONSTRAINT `fk_person_address` FOREIGN KEY (`person_id_pk_person_address`) REFERENCES Person(`person_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['PersonEmail'] = (
    "CREATE TABLE `PersonEmail` ("
    "  `person_email_id` INT AUTO_INCREMENT,"
    "  `person_id_pk_person_email` INT,"
    "  `email_address` VARCHAR(255),"
    "  `primary_email` TINYINT(1),"
    "  PRIMARY KEY (`person_email_id`),"
    "  CONSTRAINT `fk_person_email` FOREIGN KEY (`person_id_pk_person_email`) "
    "     REFERENCES `Person` (`person_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


cnx = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST,port=DB_PORT, database=DB_NAME)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()