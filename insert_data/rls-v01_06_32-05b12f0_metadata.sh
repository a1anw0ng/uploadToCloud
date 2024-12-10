#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_32-05b12f0', 'O2', 'self', 'qa7', 'MG22332A2US0019', 61, 8, 6, 1, 1, 0, '~2hrs', 30, '', false, '', false, '', false, './O2_ota_self_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 199, 215, 204, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="POWER_DURING_OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_06_32-05b12f0', 'O2', 'qa6', 'MG32401A2US100199', 61, 7, 5, 20, 20, 0, '~1.5hrs', 1, '', false, '', false, '', false, './O2_ota_power_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_32-05b12f0', 'O2', 'intFTUG', 'qa7', 'MG22332A2US0019', 61, 8, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O2_ota_int_upgrade_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 199, 321, 204, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_32-05b12f0', 'O2', 'extFTUG', 'qa7', 'MG22332A2US0019', 61, 8, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O2_ota_ext_upgrade_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 199, 321, 204, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_06_32-05b12f0', 'O2', 'prodUG', 'qa7', 'MG22332A2US0019', 61, 8, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O2_ota_prod_upgrade_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 193, 361, 206, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'idle', 'qa9', 'MG32401A2US100204', 61, 12, 10, 26, 26, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_dgo_idle_op_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'lip', 'qa9', 'MG32401A2US100204', 61, 12, 10, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_dgo_lip_op_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'hip', 'qa9', 'MG32401A2US100204', 61, 12, 10, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_dgo_hip_op_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'cooldown', 'qa9', 'MG32401A2US100204', 61, 12, 10, 28, 28, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_dgo_cooldown_op_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_OP_PR_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'fluff', 'qa9', 'MG32401A2US100204', 61, 12, 10, 47, 47, 0, '~1hrs', 1, '', false, '', false, '', false, './O2_dgo_fluff_op_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'idle', 'qa9', 'MG32401A2US100204', 61, 12, 10, 15, 15, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_dgo_idle_mass_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'lip', 'qa9', 'MG32401A2US100204', 61, 12, 10, 15, 15, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_dgo_lip_mass_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'hip', 'qa9', 'MG32401A2US100204', 61, 12, 10, 15, 15, 0, '~1hrs', 1, '', false, '', false, '', false, './O2_dgo_hip_mass_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'cooldown', 'qa9', 'MG32401A2US100204', 61, 12, 10, 15, 15, 0, '~1hrs', 1, '', false, '', false, '', false, './O2_dgo_cooldown_mass_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="DGO_ADD_MASS_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'fluff', 'qa9', 'MG32401A2US100204', 61, 12, 10, 15, 15, 0, '~1.5hrs', 1, '', false, '', false, '', false, './O2_dgo_fluff_mass_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="EEPROM_STRESS_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'qa9', 'MG32401A2US100204', 61, 12, 10, 8, 8, 0, '~1hrs', 100, '', false, '', false, '', false, './O2_eeprom_stress_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="PAIRING_WITHOUT_BLE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'home_O2', 'MG22335A2US0024', 61, 10, 8, 104, 104, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_pairing_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'normal', 'qa9', 'MG32401A2US100204', 61, 12, 10, 46, 46, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_start_via_bin_B_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="START_VIA_BIN_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'stress', 'qa9', 'MG32401A2US100204', 61, 12, 10, 21, 21, 0, '~1.5hrs', 30, '', false, '', false, '', false, './O2_start_via_bin_A_stress_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="CHILD_LOCK_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'normal', 'qa9', 'MG32401A2US100204', 61, 12, 10, 91, 91, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_child_lock_B_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="CHILD_LOCK_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'stress', 'qa9', 'MG32401A2US100204', 61, 12, 10, 19, 19, 0, '~1hrs', 30, '', false, '', false, '', false, './O2_child_lock_A_stress_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="SAFETY_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'qa9', 'MG32401A2US100204', 61, 12, 10, 42, 0, 0, '0', 0, '', false, '', false, '', false, '', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test_O2.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BOOT_CYCLE_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'stress', 'qa9', 'MG32401A2US100204', 61, 12, 10, 17, 17, 0, '~5hrs', 30, '', false, '', false, '', false, './O2_boot_cycle_A_stress_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/more/testsuites/dgo_test_boot_cycle.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'hip', 'qa9', 'add_mass_hip', 'MG32401A2US100204', 61, 12, 10, 9, 9, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_add_mass_hip_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_add_mass_hip.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'hip', 'qa9', 'reset_hip', 'MG32401A2US100204', 61, 12, 10, 9, 9, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_reset_hip_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_reset_hip.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'sht40_calibration', 'MG32401A2US100204', 61, 12, 10, 7, 7, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_sht40_calibration_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_sht40_calibration.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'sht40_cal_skip_when_hot', 'MG32401A2US100204', 61, 12, 10, 9, 9, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_sht40_cal_skip_when_hot_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_sht40_cal_skip_when_hot.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'start_stop_no_vacation', 'MG32401A2US100204', 61, 12, 10, 8, 8, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_start_stop_no_vacation_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_start_stop_no_vacation.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="SMOKE_TEST_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'qa9', 'pairing', 'MG32401A2US100204', 61, 12, 10, 11, 11, 0, '~0.5hrs', 3, '', false, '', false, '', false, './O2_smoke_pairing_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/wifi_test_O2_automation.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'jam_error', 'MG32401A2US100204', 61, 12, 10, 9, 9, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_jam_error_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_jam_error.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'jam_inactive', 'MG32401A2US100204', 61, 12, 10, 12, 12, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_jam_inactive_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_jam_inactive.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'empty_bucket', 'MG32401A2US100204', 61, 12, 10, 9, 9, 0, '~3hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_empty_bucket_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_empty_bucket.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', '', 'qa9', 'heat_warning_status', 'MG32401A2US100204', 61, 12, 10, 8, 8, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_heat_warning_status_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_heat_warning_status.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="BAT_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" 
VALUES="('dbg-v01_06_32-05b12f0', 'O2', 'hip', 'qa9', 'hip_moisture_food_add', 'MG32401A2US100204', 61, 12, 10, 10, 10, 0, '~0.5hrs', 1, '', false, '', false, '', false, './O2_bat_dgo_hip_moisture_food_add_results_v01_06_32.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/bat_dgo_hip_moisture_food_add.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

unset PGPASSWORD
