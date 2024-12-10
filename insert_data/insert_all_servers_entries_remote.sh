#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


TABLE_NAME="SERVERS_TABLE" 
COLUMN_NAMES="(ServerName, Ipaddr1, Ipaddr2, Ipaddr3, Fqdn, PortIndex, RaspPort, Switchport, Runner, RunnerGrp, Labels)"

VALUES="('dgo1', '100.104.30.118', '192.168.0.112', '10.1.100.153', 'dgo1', 5, 1, 13, 'dgo1', 'otaGrp', 'self-hosted, Linux, ARM64, dgo1');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


VALUES="('qa1', '100.85.75.33', '192.168.0.118', '10.1.100.211', 'qa1', 4, 0, 12, 'qa1', 'otaGrp', 'self-hosted, Linux, ARM64, qa1');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa3', '100.117.244.108', '192.168.0.135', '192.168.130.122', 'qa3', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


VALUES="('qa5', '100.126.212.16', '192.168.0.55', '192.168.129.123', 'qa5', null, 2, null, 'qa5', 'dgoGrp', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa6', '100.100.77.113', '192.168.0.106', '10.1.101.8', 'qa6', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa6', '100.100.77.113', '192.168.0.106', '10.1.101.8', 'qa6', 7, 2, 3, 'qa6_O1', 'powerGrp', 'self-hosted, Linux, ARM64, qa6_O1');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa6', '100.100.77.113', '192.168.0.106', '10.1.101.8', 'qa6', 6, 2, 3, 'qa6_O2', 'powerGrp', 'self-hosted, Linux, ARM64, qa6_O2');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa7', '100.121.150.100', '192.168.0.37', '10.1.101.7', 'qa7', 4, 0, 1, 'qa7', 'otaGrp', 'self-hosted, Linux, ARM64, qa7');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('home_O1', '100.92.225.35', '192.168.0.116', '', 'home_O1', 0, 0, null, 'home_O1', 'otaGrp', 'self-hosted, Linux, ARM64, home_O1');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('home_O2', '100.92.225.35', '192.168.0.116', '', 'home_O2', 0, 0, null, 'home_O2', 'otaGrp', 'self-hosted, Linux, ARM64, home_O2');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa8', '100.121.181.69', '192.168.0.18', '10.1.101.16', 'qa8', 7, 3, 4, 'qa8', 'otaGrp', 'self-hosted, Linux, ARM64, qa8');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa9', '100.65.125.23', '192.168.0.19', '10.1.101.12', 'qa9', 5, 1, 2, 'qa9', 'otaGrp', 'self-hosted, Linux, ARM64, qa9');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa10', '100.113.56.34', '', '10.1.100.195', 'qa10', null, null, null, 'qa10', 'otaGrp', 'self-hosted, Linux, ARM64, qa10');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa11', '', '', '', 'qa11', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa12', '100.102.33.103', '192.168.0.12', '10.1.101.17', 'qa12', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa13', '100.119.4.24', '192.168.0.13', '10.1.101.42', 'qa13', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa14', '100.84.19.12', '192.168.0.14', '10.1.101.43', 'qa14', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('qa15', '', '', '', 'qa14', null, null, null, '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2
