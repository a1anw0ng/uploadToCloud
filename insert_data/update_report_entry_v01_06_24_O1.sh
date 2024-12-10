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
	BuildDate = '4_12_2024',
    TemplateN = 'rls-v01_06_24-b0df8e4',
    BuildN = 'rls-v01.06.24-b0df8e4',
    CodeN = 'Hamburgh',
    BuildType = 'release',
    ProdRelTemplate = 'rls-v01_06_19-8cafe27',
    ProdRelversion = 'rls-v01.06.19-8cafe27',
    ExtFTRelTemplate = 'rls-v01_06_23-562210a',
    ExtFTRelVersion = 'rls-v01.06.23-562210a',
    IntFTRelTemplate = 'rls-v01_06_23-562210a',
    IntFTRelVersion = 'rls-v01.06.23-562210a',
    BuildId = 'id_build_32',
    StatusId = 'id_status_32',
    JiraId = 'id_jira_32',
    BuildStatus = 'PASS',
    Jira1 = '',
    Jira2 = '',
    Jira3 = '',
    BuildNotes = '',
    ClsStatus = 'passed',
    BuildLink = './rls-v01.06.24-b0df8e4_O1/dashboard_v01_06_24_O1.html'
WHERE Oscar = 'O1' and TemplateN = 'rls-v01_06_24-b0df8e4';
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