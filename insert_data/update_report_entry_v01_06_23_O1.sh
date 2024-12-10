#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


QUERY="
UPDATE REPORT_TABLE
SET 
	Oscar = 'O1',
	BuildDate = '4_3_2024',
    TemplateN = 'rls-v01_06_23-562210a',
    BuildN = 'rls-v01.06.23-562210a',
    CodeN = 'Hamburgh',
    BuildType = 'release',
    ProdRelTemplate = 'rls-v01_06_19-8cafe27',
    ProdRelversion = 'rls-v01.06.19-8cafe27',
    ExtFTRelTemplate = 'rls-v01_06_22-c356fff',
    ExtFTRelVersion = 'rls-v01.06.22-c356fff',
    IntFTRelTemplate = 'rls-v01_06_22-c356fff',
    IntFTRelVersion = 'rls-v01.06.22-c356fff',
    BuildId = 'id_build_30',
    StatusId = 'id_status_30',
    JiraId = 'id_jira_30',
    BuildStatus = 'pass - no blocker',
    Jira1 = '',
    JiraF1 = false,
    Jira2 = '',
    JiraF2 = false,
    Jira3 = '',
    JiraF3 = false,
    BuildNotes = '',
    ClsStatus = 'passnoblocker',
    BuildLink = './rls-v01.06.23-562210a_O1/dashboard_v01_06_23_O1.html'
WHERE Oscar = 'O1' and TemplateN = 'rls-v01_06_23-562210a';
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