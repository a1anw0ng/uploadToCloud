#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

# Please noted, all the tables have to deleted first, else, 
# it will have error of "violates foreign key constraint "power_during_ota_table_oscarid_fkey""

# -- Clear the table and reset the index to 1

SQL_COMMANDS="delete from CUR_SHIPPED_TABLE; ALTER SEQUENCE cur_shipped_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

