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
	BuildDate = '5_2_2024',
    TemplateN = 'rls-v01_07_04-f463d98',
    BuildN = 'rls-v01.07.04-f463d98',
    CodeN = 'Lxworth',
    BuildType = 'release',
    ProdRelTemplate = 'N/A',
    ProdRelversion = 'N/A',
    ExtFTRelTemplate = 'rls-v01_06_27-3a12001',
    ExtFTRelVersion = 'rls-v01.06.27-3a12001',
    IntFTRelTemplate = 'rls-v01_06_27-3a12001',
    IntFTRelVersion = 'rls-v01.06.27-3a12001',
    BuildId = 'id_build_38',
    StatusId = 'id_status_38',
    JiraId = 'id_jira_38',
    BuildStatus = 'PASS',
    Jira1 = '',
    Jira2 = '',
    Jira3 = '',
    BuildNotes = '',
    ClsStatus = 'passed',
    BuildLink = './rls-v01.07.04-f463d98/dashboard_v01_07_04.html'
WHERE Oscar = 'O2' and TemplateN = 'rls-v01_07_04-f463d98' 
AND CreatedAt = (SELECT MAX(CreatedAt) FROM REPORT_TABLE WHERE Oscar = 'O2' and TemplateN = 'rls-v01_07_04-f463d98');
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