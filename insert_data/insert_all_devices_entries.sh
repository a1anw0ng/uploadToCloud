#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


TABLE_NAME="DEVICES_TABLE" 
COLUMN_NAMES="(Thing, ThingGroup, Ipaddr, MacAddr, Ssid, WifiPW, Advertisement, Oscartype, Platform, Tests, Server, Runner, PoolName, Interfaces)"

VALUES="('MGM2327A1US0030', 'qa_ota_test_14', '10.1.100.214', '70:b8:f6:2e:73:3a', 'CheWiFi', 'thingsarehappening', 'Mill_MGM2327A1US0030', 'O1', 'pvt', 'otastress', 'dgo1', 'dgo1', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG32401A2US100099', 'qa_ota_23', '10.1.101.14', 'e0:5a:1b:e9:19:ba', 'CheWiFi', 'thingsarehappening', 'Mill_MG32401A2US100099', 'O2', 'dvt', 'otastress', 'qa1', 'qa1', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG62311A1US0028', 'qa_ota_test_17', '10.1.100.149', 'e8:31:cd:19:e4:be', 'CheWiFi', 'thingsarehappening', 'Mill_MG62311A1US0028', 'O1', 'pvt', 'otastress', 'qa5', 'qa5', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG52306A1US002C', 'qa_ota_test5', '', '', 'CheWiFi', 'thingsarehappening', 'Mill_MG52306A1US002C', 'O1', 'prepvt', 'otastress', 'qa6_O1', 'qa6_O1', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('guo_sn_14_o2', 'qa_ota_test11', '', '', 'CheWiFi', 'thingsarehappening', 'Mill_guo_sn_14_o2', 'O2', 'p2', 'otastress', 'qa6_O2', 'qa6_O2', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG22332A2US0019', 'qa_ota_test_15', '10.1.101.11', '64:b7:08:64:36:b2', 'CheWiFi', 'thingsarehappening', 'Mill_MG22332A2US0019', 'O2', 'evt', 'otastress', 'qa7', 'qa7', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG52306A1US002E', 'qa_ota_test_9', '192.168.0.34', 'e8:31:cd:19:f2:b6', 'CheWiFi', 'thingsarehappening', 'Mill_MG52306A1US002E', 'O1', 'prepvt', 'otastress', 'home_O1', 'home_O1', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG22335A2US0024', 'qa_ota_test9', '192.168.0.29', '64:b7:08:d1:14:7e', 'CheWiFi', 'thingsarehappening', 'Mill_MG22335A2US0024', 'O2', 'evt', 'otastress', 'home_O2', 'home_O2', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2



VALUES="('MG32401A2US100202', 'qa_test_ota_19', '10.1.101.15', '64:b7:08:d5:1d:ca', 'CheWiFi', 'thingsarehappening', 'Mill_MG32401A2US100202', 'O2', 'evt', 'otastress', 'qa8', 'qa8', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG32401A2US100204', 'qa_test_ota_20', '10.1.101.10', '64:b7:08:d5:1a:72', 'CheWiFi', 'thingsarehappening', 'Mill_MG32401A2US100204', 'O2', 'evt', 'otastress', 'qa9', 'qa9', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MG22337A2US0056', 'RemoteShellAccess', '10.1.100.193', '64:b7:08:d1:14:9e', 'CheWiFi', 'thingsarehappening', 'Mill_MG22337A2US0056', 'O2', 'evt', 'otastress', 'qa10', 'qa10', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('MGM2318A1US003D', 'qa_ota_test_21', '10.1.100.148', '0c:dc:7e:da:fd:1a', 'CheWiFi', 'thingsarehappening', 'Mill_MGM2318A1US003D', 'O1', 'evt', 'otastress', 'qa14', 'qa14', '', 'uart, dev_shadow');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2





