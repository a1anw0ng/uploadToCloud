#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

#### OTA ####
TABLE_NAME="REPORT_TABLE" 
COLUMN_NAMES="(Oscar, BuildDate, TemplateN, BuildN, CodeN, BuildType, ProdRelTemplate, ProdRelversion, ExtFTRelTemplate, ExtFTRelVersion, IntFTRelTemplate, IntFTRelVersion, BuildId, StatusId, JiraId, BuildStatus, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, BuildNotes, ClsStatus, BuildLink)"


# -- For v01_07_05
VALUES="('O2', '5_2_2024', 'rls-v01_07_04-f463d98', 'rls-v01.07.04-f463d98', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'id_build_38', 'id_status_38', 'id_jira_38', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2



# 'PENDING',  'pending'    './asset/under_construction.html'

#  'PASS',   'passed',    './rls-v01.06.21-e1529df/dashboard_v01_06_21.html