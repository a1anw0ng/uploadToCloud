# To query data from different tables
# python insert_entry_details.py OTA_PROD_UPGRADE_TABLE query 'rls-v01_05_09-ff78838' 'O1'

# To update a build's entry
# python insert_entry_details.py OTA_SELF_TABLE update 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 1 1 0 '~2hrs' 30 'ZZZZZZ' true 'zzz222' false 'zz33333' true './O1_ota_self_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'




# # OTA_SELF_TABLE
# python insert_entry_details.py OTA_SELF_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 1 1 0 '~2hrs' 30 '' false '' false '' false './O1_ota_self_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# python insert_entry_details.py OTA_SELF_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa1' 'CLS32245A1US0002' 2 5 5 1 1 0 '~2hrs' 30 '' false '' false '' false './O2_ota_self_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'


# # OTA_PROD_UPGRADE_TABLE
# python insert_entry_details.py OTA_PROD_UPGRADE_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa6' 'MGM2327A1US0030' 1 3 3 2 2 0 '~4hrs' 30 '' false '' false '' false './O1_ota_prod_upgrade_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# python insert_entry_details.py OTA_PROD_UPGRADE_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa1' 'CLS32245A1US0002' 2 5 5 2 0 0 '0' 0 '' false '' false '' false '' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# # OTA_EXT_FT_UPGRADE_TABLE
# python insert_entry_details.py OTA_PROD_UPGRADE_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa6' 'MGM2327A1US0030' 1 3 3 2 2 0 '~4hrs' 30 '' false '' false '' false './O1_ota_ext_ft_upgrade_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# python insert_entry_details.py OTA_PROD_UPGRADE_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa1' 'CLS32245A1US0002' 2 5 5 2 2 0 '~4hrs' 30 '' false '' false '' false './O2_ota_ext_ft_upgrade_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# # OTA_INT_FT_UPGRADE_TABLE
# python insert_entry_details.py OTA_INT_FT_UPGRADE_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa6' 'MGM2327A1US0030' 1 3 3 2 2 0 '~4hrs' 30 '' false '' false '' false './O1_ota_int_ft_upgrade_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# python insert_entry_details.py OTA_INT_FT_UPGRADE_TABLE insert  'dbg-v01_05_09-ff78838' 'O2' 'qa1' 'CLS32245A1US0002' 2 5 5 2 2 0 '~4hrs' 30 '' false '' false '' false './O2_ota_int_ft_upgrade_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

# # POWER_DURING_OTA_TABLE
# python insert_entry_details.py POWER_DURING_OTA_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa6' 'MGM2327A1US0030' 1 3 3 20 20 0 '~2.5hrs' 1 '' false '' false '' false './O1_ota_power_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json'

# python insert_entry_details.py POWER_DURING_OTA_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa6b' 'guo_sn_14_o2' 2 9 9 20 20 0 '~3hrs' 1 '' false '' false '' false './O2_ota_power_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/testsuites/ota_power_cycles.json'


# # DGO_IDLE_OP_PR_TABLE
# python insert_entry_details.py DGO_IDLE_OP_PR_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 26 26 0 '~3m' 1 '' false '' false '' false './O1_dgo_idle_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr.json'

# python insert_entry_details.py DGO_IDLE_OP_PR_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 26 26 0 '~4m' 1 '' false '' false '' false './O2_dgo_idle_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_IDLE_5hr_O2.json'


# # DGO_LIP_OP_PR_TABLE
# python insert_entry_details.py DGO_LIP_OP_PR_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 28 28 0 '~6m' 1 '' false '' false '' false './O1_dgo_lip_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr.json'

# python insert_entry_details.py DGO_LIP_OP_PR_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 28 28 0 '~8m' 1 '' false '' false '' false './O2_dgo_lip_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_LIP_5hr_O2.json'


# # DGO_HIP_OP_PR_TABLE
# python insert_entry_details.py DGO_HIP_OP_PR_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 28 28 0 '~6m' 1 '' false '' false '' false './O1_dgo_hip_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr.json'

# python insert_entry_details.py DGO_HIP_OP_PR_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 28 28 0 '~8m' 1 '' false '' false '' false './O2_dgo_hip_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_HIP_5hr_O2.json'


# # DGO_COOLDOWN_OP_PR_TABLE
# python insert_entry_details.py DGO_COOLDOWN_OP_PR_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 28 28 0 '~6m' 1 '' false '' false '' false './O1_dgo_cooldown_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr.json'

# python insert_entry_details.py DGO_COOLDOWN_OP_PR_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 28 28 0 '~9m' 1 '' false '' false '' false './O2_dgo_cooldown_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_COOLDOWN_5hr_O2.json'


# # DGO_FLUFF_OP_PR_TABLE
# python insert_entry_details.py DGO_FLUFF_OP_PR_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 47 47 0 '~35m' 1 '' false '' false '' false './O1_dgo_fluff_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr.json'

# python insert_entry_details.py DGO_FLUFF_OP_PR_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 47 47 0 '~36m' 1 '' false '' false '' false './O2_dgo_fluff_op_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_testsuite_FLUFF_5hr_O2.json'


# # DGO_IDLE_ADD_MASS_TABLE
# python insert_entry_details.py DGO_IDLE_ADD_MASS_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 15 15 0 '~24m' 1 '' false '' false '' false './O1_dgo_Idle_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE.json'

# python insert_entry_details.py DGO_IDLE_ADD_MASS_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 15 15 0 '~24m' 1 '' false '' false '' false './O2_dgo_Idle_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_IDLE_O2.json'

# # DGO_LIP_ADD_MASS_TABLE
# python insert_entry_details.py DGO_LIP_ADD_MASS_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 15 15 0 '~26m' 1 '' false '' false '' false './O1_dgo_lip_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP.json'

# python insert_entry_details.py DGO_LIP_ADD_MASS_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 15 15 0 '~26m' 1 '' false '' false '' false './O2_dgo_lip_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_LIP_O2.json'

# # DGO_HIP_ADD_MASS_TABLE
# python insert_entry_details.py DGO_HIP_ADD_MASS_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 15 15 0 '~46m' 1 '' false '' false '' false './O1_dgo_hip_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP.json'

# python insert_entry_details.py DGO_HIP_ADD_MASS_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 15 15 0 '~46m' 1 '' false '' false '' false './O2_dgo_hip_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_HIP_O2.json'

# # DGO_COOLDOWN_ADD_MASS_TABLE
# python insert_entry_details.py DGO_COOLDOWN_ADD_MASS_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 15 15 0 '~53m' 1 '' false '' false '' false './O1_dgo_cooldown_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN.json'

# python insert_entry_details.py DGO_COOLDOWN_ADD_MASS_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 15 15 0 '~53m' 1 '' false '' false '' false './O2_dgo_cooldown_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_COOLDOWN_O2.json'

# # DGO_FLUFF_ADD_MASS_TABLE
# python insert_entry_details.py DGO_FLUFF_ADD_MASS_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 15 15 0 '~71m' 1 '' false '' false '' false './O1_dgo_fluff_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF.json'

# python insert_entry_details.py DGO_FLUFF_ADD_MASS_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 15 15 0 '~72m' 1 '' false '' false '' false './O2_dgo_fluff_mass_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_mass_add_5hr_min_runtime_FLUFF_O2.json'



# # SAFETY_TEST_TABLE
# python insert_entry_details.py SAFETY_TEST_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 42 42 0 '~18m' 1 '' false '' false '' false './O1_safety_test_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/safety_test.json'

# python insert_entry_details.py SAFETY_TEST_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'qa7' 'MG22332A2US0019' 2 6 6 42 0 0 '0' 1 '' false '' false '' false '' ''

# # PAIRING_WITHOUT_BLE_TABLE
# python insert_entry_details.py PAIRING_WITHOUT_BLE_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 95 95 0 '~16m' 1 '' false '' false '' false './O1_pairing_without_BLE_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing.json'

# python insert_entry_details.py PAIRING_WITHOUT_BLE_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'home_O2' 'MG22335A2US0024' 2 7 7 104 104 0 '~17m' 1 '' false '' false '' false './O2_pairing_without_BLE_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/pairing_O2.json'

# # LID_OPEN_CLOSE_TABLE
# python insert_entry_details.py LID_OPEN_CLOSE_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 14 14 0 '~63m' 30 '' false '' false '' false './O1_lid_open_close_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/lid_open_close_stress.json'

# # START_VIA_BIN_STRESS_A_TABLE
# python insert_entry_details.py START_VIA_BIN_STRESS_A_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 19 19 0 '~67m' 30 '' false '' false '' false './O1_start_via_bin_stress_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A.json'

# python insert_entry_details.py START_VIA_BIN_STRESS_A_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'home_O2' 'MG22335A2US0024' 2 7 7 19 19 0 '~110m' 30 '' false '' false '' false './O2_start_via_bin_stress_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_stress_A_O2.json'

# # START_VIA_BIN_B_TABLE
# python insert_entry_details.py START_VIA_BIN_B_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 35 35 0 '~19m' 1 '' false '' false '' false './O1_start_via_bin_B_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B.json'
 
# python insert_entry_details.py START_VIA_BIN_B_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'home_O2' 'MG22335A2US0024' 2 7 7 36 36 0 '~7m' 1 '' false '' false '' false './O2_start_via_bin_B_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/dgo_start_via_bin_B_O2.json'






# # # EEPROM_STRESS_TEST_TABLE
# python insert_entry_details.py EEPROM_STRESS_TEST_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 8 8 0 '~34m' 100 '' false '' false '' false './O1_eeprom_stress_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json'

# python insert_entry_details.py EEPROM_STRESS_TEST_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'home_O2' 'MG22335A2US0024' 2 7 7 8 8 0 '~34m' 100 '' false '' false '' false './O2_eeprom_stress_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/eeprom_stress_test.json'

# # # CHILD_LOCK_STRESS_TEST_TABLE
# python insert_entry_details.py CHILD_LOCK_STRESS_TEST_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 19 19 0 '~39m' 30 '' false '' false '' false './O1_child_lock_stress_A_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A.json'

# python insert_entry_details.py CHILD_LOCK_STRESS_TEST_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'home_O2' 'MG22335A2US0024' 2 7 7 17 17 0 '~39m' 30 '' false '' false '' false './O2_child_lock_stress_A_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_stress_A_O2.json'

# # # CHILD_LOCK_TEST_TABLE
# python insert_entry_details.py CHILD_LOCK_TEST_TABLE insert 'rls-v01_05_09-ff78838' 'O1' 'home_O1' 'MG52306A1US002E' 1 4 4 89 89 0 '~24m' 1 '' false '' false '' false './O1_child_lock_B_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B.json'

# python insert_entry_details.py CHILD_LOCK_TEST_TABLE insert 'dbg-v01_05_09-ff78838' 'O2' 'home_O2' 'MG22335A2US0024' 2 7 7 76 76 0 '~17m' 1 '' false '' false '' false './O2_child_lock_B_results_v01_05_09.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/child_lock_B_O2.json'









        # UPDATE OTA_SELF_TABLE
        # SET 
        #     TemplateN = 'rls-v01_05_09-ff78838',
        #     OscarType = 'O1',
        #     SvrName = 'qa3',
        #     ThingSN = 'MG52306A1US002C',
        #     OscarId = 1, 
        #     SvrId = 2, 
        #     DeviceId = 2,
        #     TestExecuted = 1, 
        #     Passed = 1, 
        #     Failed = 0,
        #     ExeTime = '~2hrs', 
        #     Repeats = 30,
        #     Jira1 = 'ADDDD',
        #     JiraF1 = false,
        #     Jira2 = 'BCCCC',
        #     JiraF2 = false,
        #     Jira3 = 'EEEEE',
        #     JiraF3 = false,
        #     ResultLink = './O1_ota_self_results_v01_05_09.txt', 
        #     TestCasesLink = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'
        # WHERE OscarType = 'O1' and TemplateN = 'rls-v01_05_09-ff78838';
        