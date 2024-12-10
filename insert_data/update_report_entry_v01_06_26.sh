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
	BuildDate = '4_25_2024',
    TemplateN = 'rls-v01_06_26-f09d1ae',
    BuildN = 'rls-v01.06.26-f09d1ae',
    CodeN = 'Hamburgh',
    BuildType = 'release',
    ProdRelTemplate = 'N/A',
    ProdRelversion = 'N/A',
    ExtFTRelTemplate = 'rls-v01_06_24-b0df8e4',
    ExtFTRelVersion = 'rls-v01.06.24-b0df8e4',
    IntFTRelTemplate = 'rls-v01_06_24-b0df8e4',
    IntFTRelVersion = 'rls-v01.06.24-b0df8e4',
    BuildId = 'id_build_36',
    StatusId = 'id_status_36',
    JiraId = 'id_jira_36',
    BuildStatus = 'PASS',
    Jira1 = '',
    Jira2 = '',
    Jira3 = '',
    BuildNotes = '',
    ClsStatus = 'passed',
    BuildLink = './rls-v01.06.26-f09d1ae/dashboard_v01_06_26.html'
WHERE Oscar = 'O2' and TemplateN = 'rls-v01_06_26-f09d1ae';
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