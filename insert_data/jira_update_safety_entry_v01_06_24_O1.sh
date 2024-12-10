#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


QUERY="
UPDATE SAFETY_TEST_TABLE
SET 
    TemplateN = 'dbg-v01_06_24-b0df8e4',
	OscarType = 'O1',
	SvrName = 'qa5',
    ThingSN = 'MG62311A1US0028',
	OscarId = 33, 
	SvrId = 6, 
	DeviceId = 6,
	TestExecuted = 37, 
	Passed = 37, 
	Failed = 0,
	ExeTime = '~0.5hrs', 
	Repeats = 1,
	Jira1 = 'fw-4301',
	JiraF1 = false,
    Jira2 = '',
	JiraF2 = false,
    Jira3 = '',
	JiraF3 = false,
	ResultLink = './O1_safety_test_results_v01_06_24.txt', 
	TestCasesLink = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test.json',
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