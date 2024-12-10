#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"
export PGPASSWORD=$DB_PASSWORD


# SQL_COMMANDS="delete from SAFETY_TEST_TABLE; ALTER SEQUENCE safety_test_table_id_seq RESTART WITH 1;"
# PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "$SQL_COMMANDS"



TABLE_NAME="SAFETY_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_24-b0df8e4', 'O1', 'qa7', 'MG22332A2US0019', 33, 6, 6, 37, 37, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_safety_test_results_v01_06_24.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

#TABLE_NAME="LID_OPEN_CLOSE_TABLE"
#COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
#VALUES="('dbg-v01_06_24-b0df8e4', 'O1', 'qa7', 'MG22332A2US0019', 33, 6, 6, 14, 14, 0, '~1hrs', 30, '', false, '', false, '', false, './O1_lid_open_close_results_v01_06_24.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/lid_open_close_stress.json', '', '')"
#QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
#psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

unset PGPASSWORD