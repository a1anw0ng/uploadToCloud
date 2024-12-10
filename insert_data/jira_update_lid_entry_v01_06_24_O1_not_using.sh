#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


QUERY="
UPDATE LID_OPEN_CLOSE_TABLE
SET 
    TemplateN = 'dbg-v01_06_24-b0df8e4',
	OscarType = 'O1',
	SvrName = 'qa7',
    ThingSN = 'MG22332A2US0019',
	OscarId = 33, 
	SvrId = 6, 
	DeviceId = 6,
	TestExecuted = 14, 
	Passed = 14, 
	Failed = 0,
	ExeTime = '~1hrs', 
	Repeats = 30,
	Jira1 = 'fw-4301',
	JiraF1 = false,
    Jira2 = '',
	JiraF2 = false,
    Jira3 = '',
	JiraF3 = false,
	ResultLink = './O1_lid_open_close_results_v01_06_24.txt', 
	TestCasesLink = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/lid_open_close_stress.json',
    DebugLink = '',
    Notes = 'skipped test cases'

WHERE OscarType = 'O1' and TemplateN = 'dbg-v01_06_24-b0df8e4';
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