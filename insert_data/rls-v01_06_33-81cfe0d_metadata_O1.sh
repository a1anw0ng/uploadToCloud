#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"
export PGPASSWORD=$DB_PASSWORD

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_33-81cfe0d', 'O1', 'self', 'dgo1', 'MGM2327A1US0030', 59, 1, 1, 1, 1, 0, '~3hrs', 30, '', false, '', false, '', false, './O1_ota_self_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 341, 382, 349, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="POWER_DURING_OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_06_33-81cfe0d', 'O1', 'qa6', 'MG52306A1US002C', 59, 6, 4, 20, 20, 0, '~2.5hrs', 1, '', false, '', false, '', false, './O1_ota_power_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_33-81cfe0d', 'O1', 'intFTUG', 'dgo1', 'MGM2327A1US0030', 59, 1, 1, 2, 2, 0, '~6hrs', 30, '', false, '', false, '', false, './O1_ota_int_upgrade_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 342, 382, 350, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_33-81cfe0d', 'O1', 'extFTUG', 'dgo1', 'MGM2327A1US0030', 59, 1, 1, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O1_ota_ext_upgrade_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 210, 463, 237, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_33-81cfe0d', 'O1', 'prodUG', 'dgo1', 'MGM2327A1US0030', 59, 1, 1, 2, 0, 0, '0', 0, '', false, '', false, '', false, '', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 0, 0, 0, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'idle', 'qa5', 'MG62311A1US0028', 59, 4, 3, 26, 26, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_idle_op_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'lip', 'qa5', 'MG62311A1US0028', 59, 4, 3, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_lip_op_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'hip', 'qa5', 'MG62311A1US0028', 59, 4, 3, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_hip_op_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'cooldown', 'qa5', 'MG62311A1US0028', 59, 4, 3, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_cooldown_op_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'fluff', 'qa5', 'MG62311A1US0028', 59, 4, 3, 47, 47, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_dgo_fluff_op_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'idle', 'qa5', 'MG62311A1US0028', 59, 4, 3, 15, 15, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_idle_mass_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'lip', 'qa5', 'MG62311A1US0028', 59, 4, 3, 15, 15, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_lip_mass_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'hip', 'qa5', 'MG62311A1US0028', 59, 4, 3, 15, 15, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_dgo_hip_mass_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'cooldown', 'qa5', 'MG62311A1US0028', 59, 4, 3, 15, 15, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_dgo_cooldown_mass_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'fluff', 'qa5', 'MG62311A1US0028', 59, 4, 3, 15, 15, 0, '~1.5hrs', 1, '', false, '', false, '', false, './O1_dgo_fluff_mass_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="EEPROM_STRESS_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'qa5', 'MG62311A1US0028', 59, 4, 3, 8, 8, 0, '~1hrs', 100, '', false, '', false, '', false, './O1_eeprom_stress_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="PAIRING_WITHOUT_BLE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'home_O1', 'MG52306A1US002E', 59, 9, 7, 98, 98, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_pairing_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'normal', 'qa5', 'MG62311A1US0028', 59, 4, 3, 36, 36, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_start_via_bin_B_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'stress', 'qa5', 'MG62311A1US0028', 59, 4, 3, 19, 19, 0, '~1hrs', 30, '', false, '', false, '', false, './O1_start_via_bin_A_stress_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="CHILD_LOCK_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'normal', 'qa5', 'MG62311A1US0028', 59, 4, 3, 89, 89, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_child_lock_B_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="CHILD_LOCK_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'stress', 'qa5', 'MG62311A1US0028', 59, 4, 3, 19, 19, 0, '~1hrs', 30, '', false, '', false, '', false, './O1_child_lock_A_stress_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="SAFETY_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'qa5', 'MG62311A1US0028', 59, 4, 3, 42, 42, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_safety_test_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="LID_OPEN_CLOSE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_33-81cfe0d', 'O1', 'qa5', 'MG62311A1US0028', 59, 4, 3, 14, 14, 0, '~1hrs', 30, '', false, '', false, '', false, './O1_lid_open_close_results_v01_06_33.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/lid_open_close_stress.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

unset PGPASSWORD
