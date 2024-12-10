#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


TABLE_NAME="CUR_SHIPPED_TABLE" 
COLUMN_NAMES="(Oscar, CodeN, BuildType, ProdRelT, ProdRelV, ExtFTRelT, ExtFTRelV, IntFTRelT, IntFTRelV, DayOImgT, DayOImgV, FFUImgT, FFUImgV, AutoOTAT, AutoOTAV, FactoryImg, DiagImg, UserGrp1T, UserGrp1V, UserGrp2T, UserGrp2V, UserGrp3T, UserGrp3V)"

VALUES="('O1', 'Gournay', 'release', 'rls-v01_05_09-ff78838', 'rls-v01.05.09-ff78838', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O1', 'Hamburgh', 'release', 'rls-v01_05_09-ff78838', 'rls-v01.05.09-ff78838', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O1', 'Hamburgh', 'release', 'rls-v01_05_09-ff78838', 'rls-v01.05.09-ff78838', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_26-f09d1ae', 'rls-v01.06.26-f09d1ae', 'rls-v01_06_26-f09d1ae', 'rls-v01.06.26-f09d1ae', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', '', '', '', '', '', '', '', '', '', '', '', '', '', '');"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2
