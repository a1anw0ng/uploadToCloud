#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"


# O1
TABLE_NAME="OTA_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"  # Example column names

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'self', 'qa3', 'MG52306A1US002C', 1, 2, 2, 1, 1, 0, '~2hrs', 30, '', false, '', false, '', false, './O1_ota_self_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', 'change to MG52306A1US002C', 179, 361, 194, 0, 0)"  
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'prodUG', 'qa6', 'MGM2327A1US0030', 1, 3, 3, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O1_ota_prod_ft_results_v01_05_05_N_v01_05_04_N_v01_04_07.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', 'MGM2327A1US0030', 159, 367, 196, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'extFTUG', 'qa6', 'MGM2327A1US0030', 1, 3, 3, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O1_ota_prod_ft_results_v01_05_05_N_v01_05_04_N_v01_04_07.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', 'MGM2327A1US0030', 159, 367, 196, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'intFTUG', 'qa6', 'MGM2327A1US0030', 1, 3, 3, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O1_ota_prod_ft_results_v01_05_05_N_v01_05_04_N_v01_04_07.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', 'MGM2327A1US0030', 159, 367, 196, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2  
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'self', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 1, 1, 0, '~2hrs', 30, '', false, '', false, '', false, './O2_ota_self_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 204, 235, 210, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'prodUG', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 2, 0, 0, '0', 0, '', false, '', false, '', false, '', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 0, 0, 0, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'extFTUG', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O2_ota_ext_int_ft_results_v01_05_05_N_v01_05_04.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 204, 3603, 277, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'intFTUG', 'qa1', 'CLS32245A1US0002', 2, 5, 5, 2, 2, 0, '~4hrs', 30, '', false, '', false, '', false, './O2_ota_ext_int_ft_results_v01_05_05_N_v01_05_04.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 204, 3603, 277, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="POWER_DURING_OTA_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'qa6', 'MGM2327A1US0030', 1, 3, 3, 20, 20, 0, '~2.5hrs', 1, '', false, '', false, '', false, './O1_ota_power_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2  
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'qa6b', 'guo_sn_14_o2', 2, 9, 9, 20, 20, 0, '~3hrs', 1, '', false, '', false, '', false, './O2_ota_power_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="DGO_OP_PR_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'idle', 'qa3', 'MG52306A1US002C', 1, 2, 2, 26, 26, 0, '~3m', 1, '', false, '', false, '', false, './O1_dgo_idle_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'lip', 'qa3', 'MG52306A1US002C', 1, 2, 2, 28, 28, 0, '~6m', 1, '', false, '', false, '', false, './O1_dgo_lip_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'hip', 'qa3', 'MG52306A1US002C', 1, 2, 2, 28, 28, 0, '~6m', 1, '', false, '', false, '', false, './O1_dgo_hip_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'cooldown', 'qa3', 'MG52306A1US002C', 1, 2, 2, 28, 28, 0, '~6m', 1, '', false, '', false, '', false, './O1_dgo_cooldown_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'fluff', 'qa3', 'MG52306A1US002C', 1, 2, 2, 47, 47, 0, '~35m', 1, '', false, '', false, '', false, './O1_dgo_fluff_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'idle', 'qa7', 'MG22332A2US0019', 2, 6, 6, 26, 26, 0, '~4m', 1, '', false, '', false, '', false, './O2_dgo_idle_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'lip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 28, 28, 0, '~8m', 1, '', false, '', false, '', false, './O2_dgo_lip_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'hip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 28, 28, 0, '~8m', 1, '', false, '', false, '', false, './O2_dgo_hip_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'cooldown', 'qa7', 'MG22332A2US0019', 2, 6, 6, 28, 28, 0, '~9m', 1, '', false, '', false, '', false, './O2_dgo_cooldown_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'fluff', 'qa7', 'MG22332A2US0019', 2, 6, 6, 47, 47, 0, '~36m', 1, '', false, '', false, '', false, './O2_dgo_fluff_op_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="DGO_ADD_MASS_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'idle', 'qa3', 'MG52306A1US002C', 1, 2, 2, 15, 15, 0, '~24m', 1, '', false, '', false, '', false, './O1_dgo_Idle_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'lip', 'qa3', 'MG52306A1US002C', 1, 2, 2, 15, 15, 0, '~26m', 1, '', false, '', false, '', false, './O1_dgo_lip_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'hip', 'qa3', 'MG52306A1US002C', 1, 2, 2, 15, 15, 0, '~46m', 1, '', false, '', false, '', false, './O1_dgo_hip_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'cooldown', 'qa3', 'MG52306A1US002C', 1, 2, 2, 15, 15, 0, '~53m', 1, '', false, '', false, '', false, './O1_dgo_cooldown_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'fluff', 'qa3', 'MG52306A1US002C', 1, 2, 2, 15, 15, 0, '~71m', 1, '', false, '', false, '', false, './O1_dgo_fluff_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'idle', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~24m', 1, '', false, '', false, '', false, './O2_dgo_Idle_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'lip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~26m', 1, '', false, '', false, '', false, './O2_dgo_lip_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'hip', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~46m', 1, '', false, '', false, '', false, './O2_dgo_hip_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'cooldown', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~53m', 1, '', false, '', false, '', false, './O2_dgo_cooldown_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'fluff', 'qa7', 'MG22332A2US0019', 2, 6, 6, 15, 15, 0, '~72m', 1, '', false, '', false, '', false, './O2_dgo_fluff_mass_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O1
TABLE_NAME="SAFETY_TEST_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'qa3', 'MG52306A1US002C', 1, 2, 2, 42, 42, 0, '~18m', 1, '', false, '', false, '', false, './O1_safety_test_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'qa7', 'MG22332A2US0019', 2, 6, 6, 42, 0, 0, '0', 1, '', false, '', false, '', false, '', '', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="PAIRING_WITHOUT_BLE_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 95, 95, 0, '~16m', 1, '', false, '', false, '', false, './O1_pairing_without_BLE_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2 
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 104, 104, 0, '~17m', 1, '', false, '', false, '', false, './O2_pairing_without_BLE_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="LID_OPEN_CLOSE_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 14, 14, 0, '~63m', 30, '', false, '', false, '', false, './O1_lid_open_close_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/lid_open_close_stress.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="START_VIA_BIN_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'stress', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 19, 19, 0, '~67m', 30, '', false, '', false, '', false, './O1_start_via_bin_stress_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'normal', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 35, 35, 0, '~19m', 1, '', false, '', false, '', false, './O1_start_via_bin_B_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'stress', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 19, 19, 0, '~110m', 30, '', false, '', false, '', false, './O2_start_via_bin_stress_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'normal', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 36, 36, 0, '~7m', 1, '', false, '', false, '', false, './O2_start_via_bin_B_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="EEPROM_STRESS_TEST_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 8, 8, 0, '~34m', 100, '', false, '', false, '', false, './O1_eeprom_stress_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 8, 8, 0, '~34m', 100, '', false, '', false, '', false, './O2_eeprom_stress_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


# O1
TABLE_NAME="CHILD_LOCK_TABLE" 
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_05_05-19dc16c', 'O1', 'stress', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 19, 19, 0, '~39m', 30, '', false, '', false, '', false, './O1_child_lock_stress_A_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A.json', '', '')"

QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('rls-v01_05_05-19dc16c', 'O1', 'normal', 'home_O1', 'MG52306A1US002E', 1, 4, 4, 89, 89, 0, '~24m', 1, '', false, '', false, '', false, './O1_child_lock_B_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

# O2
VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'stress', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 17, 17, 0, '~39m', 30, '', false, '', false, '', false, './O2_child_lock_stress_A_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

VALUES="('dbg-v01_05_05-19dc16c', 'O2', 'normal', 'home_O2', 'MG22335A2US0024', 2, 7, 7, 76, 76, 0, '~17m', 1, '', false, '', false, '', false, './O2_child_lock_B_results_v01_05_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"


unset PGPASSWORD








