TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_07_05-1b8bb0d', 'O2', 'self', 'qa7', 'MG22332A2US0019', 38, 8, 6, 1, 1, 0, '~2hrs', 30, '', false, '', false, '', false, './O2_ota_self_results_v01_07_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 205, 347, 220, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="POWER_DURING_OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"
VALUES="('rls-v01_07_05-1b8bb0d', 'O2', 'qa6', 'guo_sn_14_o2', 38, 7, 5, 20, 20, 0, '~2hrs', 1, '', false, '', false, '', false, './O2_ota_power_results_v01_07_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json', '', '')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_07_05-1b8bb0d', 'O2', 'intFTUG', 'qa7', 'MG22332A2US0019', 38, 8, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O2_ota_int_upgrade_results_v01_07_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 199, 337, 210, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

TABLE_NAME="OTA_TABLE"
COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"
VALUES="('rls-v01_07_05-1b8bb0d', 'O2', 'extFTUG', 'qa7', 'MG22332A2US0019', 38, 8, 6, 2, 2, 0, '~3.5hrs', 30, '', false, '', false, '', false, './O2_ota_ext_upgrade_results_v01_07_05.txt', 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py', '', '', 199, 337, 210, 0, 0)"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"

