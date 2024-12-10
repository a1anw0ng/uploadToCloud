#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


QUERY="
UPDATE OTA_TABLE
SET 
    TemplateN = 'rls-v01_06_31-aaaa605',
	OscarType = 'O1',
	TestType = 'prodUG',
	SvrName = 'qa5',
    ThingSN = 'MGM2327A1US0030',
	OscarId = 54, 
	SvrId = 1, 
	DeviceId = 1,
	TestExecuted = 2, 
	Passed = 0, 
	Failed = 2,
	ExeTime = '~0.5hrs', 
	Repeats = 1,
	Jira1 = 'FW-4444',
	JiraF1 = true,
    Jira2 = '',
	JiraF2 = false,
    Jira3 = '',
	JiraF3 = false,
	ResultLink = './O1_ota_prod_upgrade_results_v01_06_31.txt', 
	TestCasesLink = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py',
    DebugLink = '',
    Notes = 'stuck in "QUEUED" state'

WHERE OscarType = 'O1' and TemplateN = 'rls-v01_06_31-aaaa605'
AND LOGTIME = (SELECT MAX(LOGTIME) FROM OTA_TABLE WHERE OscarType = 'O1' and TemplateN = 'rls-v01_06_31-aaaa605');
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