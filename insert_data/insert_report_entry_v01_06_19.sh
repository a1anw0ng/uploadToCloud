#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

#### OTA ####
TABLE_NAME="REPORT_TABLE" 
COLUMN_NAMES="(Oscar, BuildDate, TemplateN, BuildN, CodeN, BuildType, ProdRelTemplate, ProdRelversion, ExtFTRelTemplate, ExtFTRelVersion, IntFTRelTemplate, IntFTRelVersion, BuildId, StatusId, JiraId, BuildStatus, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, BuildNotes, ClsStatus, BuildLink)"


# -- For v01_06_19
VALUES="('O2', '3_13_2024', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_17-8b85b9b', 'rls-v01.06.17-8b85b9b', 'rls-v01_06_17-8b85b9b', 'rls-v01.06.17-8b85b9b', 'id_build_23', 'id_status_23', 'id_jira_23', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.19-8cafe27/dashboard_v01_06_19.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2



