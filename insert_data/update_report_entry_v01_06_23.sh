#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


QUERY="
UPDATE REPORT_TABLE
SET 
	Oscar = 'O2',
	BuildDate = '4_3_2024',
    TemplateN = 'rls-v01_06_23-562210a',
    BuildN = 'rls-v01.06.23-562210a',
    CodeN = 'Hamburgh',
    BuildType = 'release',
    ProdRelTemplate = 'N/A',
    ProdRelversion = 'N/A',
    ExtFTRelTemplate = 'rls-v01_06_22-c356fff',
    ExtFTRelVersion = 'rls-v01.06.22-c356fff',
    IntFTRelTemplate = 'rls-v01_06_22-c356fff',
    IntFTRelVersion = 'rls-v01.06.22-c356fff',
    BuildId = 'id_build_27',
    StatusId = 'id_status_27',
    JiraId = 'id_jira_27',
    BuildStatus = 'PASS',
    Jira1 = '',
    Jira2 = '',
    Jira3 = '',
    BuildNotes = '',
    ClsStatus = 'passed',
    BuildLink = './rls-v01.06.23-562210a/dashboard_v01_06_23.html'
WHERE Oscar = 'O2' and TemplateN = 'rls-v01_06_23-562210a';
"

export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -c "$QUERY"

unset PGPASSWORD


# # To update the following:

# BuildStatus = 'PENDING',
# ClsStatus = 'pending',
# BuildLink = './asset/under_construction.html'

# BuildStatus = 'PASS',
# ClsStatus = 'passed',
# BuildLink = './rls-v01.06.19-8cafe27/dashboard_v01_06_19.html'