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
	BuildDate = '3_27_2024',
    TemplateN = 'rls-v01_06_22-c356fff',
    BuildN = 'rls-v01.06.22-c356fff',
    CodeN = 'Hamburgh',
    BuildType = 'release',
    ProdRelTemplate = 'N/A',
    ProdRelversion = 'N/A',
    ExtFTRelTemplate = 'rls-v01_06_21-e1529df',
    ExtFTRelVersion = 'rls-v01.06.21-e1529df',
    IntFTRelTemplate = 'rls-v01_06_21-e1529df',
    IntFTRelVersion = 'rls-v01.06.21-e1529df',
    BuildId = 'id_build_26',
    StatusId = 'id_status_26',
    JiraId = 'id_jira_26',
    BuildStatus = 'PASS',
    Jira1 = '',
    Jira2 = '',
    Jira3 = '',
    BuildNotes = '',
    ClsStatus = 'passed',
    BuildLink = './rls-v01.06.22-c356fff/dashboard_v01_06_22.html'
WHERE Oscar = 'O2' and TemplateN = 'rls-v01_06_22-c356fff';
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