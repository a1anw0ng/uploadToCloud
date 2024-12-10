#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

# -- Clear all report tables and reset the index to 1

SQL_COMMANDS="delete from OTA_TABLE; ALTER SEQUENCE ota_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from POWER_DURING_OTA_TABLE; ALTER SEQUENCE power_during_ota_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from DGO_OP_PR_TABLE; ALTER SEQUENCE dgo_op_pr_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from DGO_ADD_MASS_TABLE; ALTER SEQUENCE dgo_add_mass_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from SAFETY_TEST_TABLE; ALTER SEQUENCE safety_test_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from PAIRING_WITHOUT_BLE_TABLE; ALTER SEQUENCE pairing_without_ble_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from LID_OPEN_CLOSE_TABLE; ALTER SEQUENCE lid_open_close_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from START_VIA_BIN_TABLE; ALTER SEQUENCE start_via_bin_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from EEPROM_STRESS_TEST_TABLE; ALTER SEQUENCE eeprom_stress_test_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

SQL_COMMANDS="delete from CHILD_LOCK_TABLE; ALTER SEQUENCE child_lock_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"


SQL_COMMANDS="delete from BOOT_CYCLE_TABLE; ALTER SEQUENCE boot_cycle_table_id_seq RESTART WITH 1;"
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"

echo "Commands executed successfully."


# delete from OTA_TABLE;
# ALTER SEQUENCE ota_table_id_seq RESTART WITH 1;


# delete from POWER_DURING_OTA_TABLE;
# ALTER SEQUENCE power_during_ota_table_id_seq RESTART WITH 1;

# delete from DGO_OP_PR_TABLE;
# ALTER SEQUENCE dgo_op_pr_table_id_seq RESTART WITH 1;

# delete from DGO_ADD_MASS_TABLE;
# ALTER SEQUENCE dgo_add_mass_table_id_seq RESTART WITH 1;

# delete from SAFETY_TEST_TABLE;
# ALTER SEQUENCE safety_test_table_id_seq RESTART WITH 1;

# delete from PAIRING_WITHOUT_BLE_TABLE;
# ALTER SEQUENCE pairing_without_ble_table_id_seq RESTART WITH 1;

# delete from LID_OPEN_CLOSE_TABLE;
# ALTER SEQUENCE lid_open_close_table_id_seq RESTART WITH 1;


# delete from START_VIA_BIN_TABLE;
# ALTER SEQUENCE start_via_bin_table_id_seq RESTART WITH 1;


# delete from EEPROM_STRESS_TEST_TABLE;
# ALTER SEQUENCE eeprom_stress_test_table_id_seq RESTART WITH 1;


# delete from CHILD_LOCK_TABLE;
# ALTER SEQUENCE child_lock_table_id_seq RESTART WITH 1;