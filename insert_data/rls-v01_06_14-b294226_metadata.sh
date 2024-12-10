#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

#### OTA ####
TABLE_NAME="OTA_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"

# O2_ota_self_results_v01_06_14.txt
VALUES="('rls-v01_06_14-b294226', 'O2', 'self', 'qa1', 'MG32401A2US100099', 2, 5, 10, 1, 1, 0, '~2hrs', 30, '', false, '', false, '', false, './O2_ota_self_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 224, 245, 233, 0, 0)"  
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_ota_upgrade_results_v01_06_14.txt
VALUES="('rls-v01_06_14-b294226', 'O2', 'prodUG', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 2, 0, 0, '0', 0, '', false, '', false, '', false, '', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 0, 0, 0, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_06_14-b294226', 'O2', 'extFTUG', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O2_ota_upgrade_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 174, 207, 190, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_06_14-b294226', 'O2', 'intFTUG', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O2_ota_upgrade_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 174, 207, 190, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2  
TABLE_NAME="POWER_DURING_OTA_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('rls-v01_06_14-b294226', 'O2', 'qa6b', 'guo_sn_14_o2', 2, 9, 9, 20, 20, 0, '~3hrs', 1, '', false, '', false, '', false, './O2_ota_power_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


##### DGO OP PR, testing the whole DGO cycle FSM ####
TABLE_NAME="DGO_OP_PR_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"

# O2_dgo_idle_op_results_v01_06_14.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'idle', 'qa7', 'MG22332A2US0019', 2, 6, 6, 26, 26, 0, '~3m', 1, '', false, '', false, '', false, './O2_dgo_idle_op_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_lip_op_results_v01_06_14.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'lip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 28, 28, 0, '~7m', 1, '', false, '', false, '', false, './O2_dgo_lip_op_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_hip_op_results_v01_06_14_.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'hip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 28, 28, 0, '~7.5m', 1, '', false, '', false, '', false, './O2_dgo_hip_op_results_v01_06_14_.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_cooldown_op_results_v01_06_14_B2.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'cooldown', 'qa7', 'MG22332A2US0019', 2, 6, 6, 28, 28, 0, '~8m', 1, '', false, '', false, '', false, './O2_dgo_cooldown_op_results_v01_06_14_B2.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_fluff_op_results_v01_06_14_B.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'fluff', 'qa7', 'MG22332A2US0019', 2, 6, 6, 47, 47, 0, '~35m', 1, '', false, '', false, '', false, './O2_dgo_fluff_op_results_v01_06_14_B.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


##### DGO adding mass logically ####
TABLE_NAME="DGO_ADD_MASS_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"

# O2_dgo_Idle_mass_results_v01_06_14_3.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'idle', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~23m', 1, '', false, '', false, '', false, './O2_dgo_Idle_mass_results_v01_06_14_3.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_lip_mass_results_v01_06_14_B.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'lip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~25m', 1, '', false, '', false, '', false, './O2_dgo_lip_mass_results_v01_06_14_B.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_hip_mass_results_v01_06_14_B.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'hip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~45m', 1, '', false, '', false, '', false, './O2_dgo_hip_mass_results_v01_06_14_B.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_cooldown_mass_results_v01_06_14_B.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'cooldown', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~52.5m', 1, '', false, '', false, '', false, './O2_dgo_cooldown_mass_results_v01_06_14_B.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_dgo_fluff_mass_results_v01_06_14_C1.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'fluff', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~71m', 1, '', false, '', false, '', false, './O2_dgo_fluff_mass_results_v01_06_14_C1.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


#### Start via bin table ####
TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"

# O2_start_via_bin_stress_results_v01_06_14_C.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'stress', 'qa7', 'MG22332A2US0019', 2, 6, 6, 21, 21, 0, '~53m', 30, '', false, '', false, '', false, './O2_start_via_bin_stress_results_v01_06_14_C.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_start_via_bin_B_results_v01_06_14_b1.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'normal', 'qa7', 'MG22332A2US0019', 2, 6, 6, 46, 46, 0, '~9.4m', 1, '', false, '', false, '', false, './O2_start_via_bin_B_results_v01_06_14_b1.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


#### EEPROM ####
TABLE_NAME="EEPROM_STRESS_TEST_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"

# O2_eeprom_stress_results_v01_06_14.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'qa7', 'MG22332A2US0019', 2, 6, 6, 8, 8, 0, '~33m', 100, '', false, '', false, '', false, './O2_eeprom_stress_results_v01_06_14.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2 Pairing
TABLE_NAME="PAIRING_WITHOUT_BLE_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_14-b294226', 'O2', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 104, 104, 0, '~17m', 1, '', false, '', false, '', false, './O2_pairing_results_O2_v01_06_14_C1.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O2
TABLE_NAME="SAFETY_TEST_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_14-b294226', 'O2', 'qa7', 'MG22332A2US0019', 2, 6, 6, 42, 0, 0, '0', 0, '', false, '', false, '', false, '', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


#### Child/pet lock ####
TABLE_NAME="CHILD_LOCK_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"

# O2_child_lock_stress_A_results_v01_06_14_D_1.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'stress', 'qa7', 'MG22332A2US0019', 2, 6, 6, 19, 19, 0, '~40m', 30, '', false, '', false, '', false, './O2_child_lock_stress_A_results_v01_06_14_D_1.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2_child_lock_B_results_v01_06_14_B_1.txt
VALUES="('dbg-v01_06_14-b294226', 'O2', 'normal', 'qa7', 'MG22332A2US0019', 2, 6, 6, 91, 91, 0, '~29m', 1, '', false, '', false, '', false, './O2_child_lock_B_results_v01_06_14_B_1.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

unset PGPASSWORD