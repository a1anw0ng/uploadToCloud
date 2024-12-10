#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"
export PGPASSWORD=$DB_PASSWORD


TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_23-562210a', 'O1', 'self', 'qa7', 'MGM2327A1US0030', 34, 6, 6, 1, 1, 0, '~2hrs', 30, '', false, '', false, '', false, './O1_ota_self_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 194, 211, 196, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="POWER_DURING_OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_06_23-562210a', 'O1', 'qa7', 'MG52306A1US002C', 34, 6, 6, 20, 20, 0, '~2hrs', 1, '', false, '', false, '', false, './O1_ota_power_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_23-562210a', 'O1', 'intFTUG', 'qa7', 'MGM2327A1US0030', 34, 6, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O1_ota_int_upgrade_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 168, 246, 207, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_23-562210a', 'O1', 'extFTUG', 'qa7', 'MGM2327A1US0030', 34, 6, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O1_ota_ext_upgrade_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 168, 246, 207, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_23-562210a', 'O1', 'prodUG', 'qa7', 'MGM2327A1US0030', 34, 6, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O1_ota_prod_upgrade_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 168, 246, 207, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'idle', 'qa7', 'MG22332A2US0019', 34, 6, 6, 26, 26, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_idle_op_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'lip', 'qa7', 'MG22332A2US0019', 34, 6, 6, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_lip_op_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'hip', 'qa7', 'MG22332A2US0019', 34, 6, 6, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_hip_op_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'cooldown', 'qa7', 'MG22332A2US0019', 34, 6, 6, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_cooldown_op_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'fluff', 'qa7', 'MG22332A2US0019', 34, 6, 6, 47, 47, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_dgo_fluff_op_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'idle', 'qa7', 'MG22332A2US0019', 34, 6, 6, 15, 15, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_idle_mass_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'lip', 'qa7', 'MG22332A2US0019', 34, 6, 6, 15, 15, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_dgo_lip_mass_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'hip', 'qa7', 'MG22332A2US0019', 34, 6, 6, 15, 15, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_dgo_hip_mass_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'cooldown', 'qa7', 'MG22332A2US0019', 34, 6, 6, 15, 15, 0, '~1hrs', 1, '', false, '', false, '', false, './O1_dgo_cooldown_mass_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'fluff', 'qa7', 'MG22332A2US0019', 34, 6, 6, 15, 15, 0, '~1.5hrs', 1, '', false, '', false, '', false, './O1_dgo_fluff_mass_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="EEPROM_STRESS_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'qa7', 'MG22332A2US0019', 34, 6, 6, 8, 8, 0, '~1hrs', 100, '', false, '', false, '', false, './O1_eeprom_stress_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="PAIRING_WITHOUT_BLE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'qa7', 'MG22332A2US0019', 34, 6, 6, 98, 98, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_pairing_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'normal', 'qa7', 'MG22332A2US0019', 34, 6, 6, 36, 36, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_start_via_bin_B_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'stress', 'qa7', 'MG22332A2US0019', 34, 6, 6, 19, 19, 0, '~1hrs', 30, '', false, '', false, '', false, './O1_start_via_bin_A_stress_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="CHILD_LOCK_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'normal', 'qa7', 'MG22332A2US0019', 34, 6, 6, 80, 80, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_child_lock_B_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="CHILD_LOCK_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'stress', 'qa7', 'MG22332A2US0019', 34, 6, 6, 17, 17, 0, '~0.5hrs', 30, '', false, '', false, '', false, './O1_child_lock_A_stress_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="SAFETY_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'qa7', 'MG22332A2US0019', 34, 6, 6, 37, 37, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O1_safety_test_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BOOT_CYCLE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_23-562210a', 'O1', 'stress', 'qa7', 'MG22332A2US0019', 34, 6, 6, 17, 17, 0, '~5hrs', 30, '', false, '', false, '', false, './O1_boot_cycle_A_stress_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/more/testsuites/boot_cycle_stress_A_O1.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="LID_OPEN_CLOSE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_23-562210a', 'O1', 'qa7', 'MG22332A2US0019', 34, 6, 6, 14, 14, 0, '~1hrs', 30, '', false, '', false, '', false, './O1_lid_open_close_results_v01_06_23.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/lid_open_close_stress.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"



unset PGPASSWORD