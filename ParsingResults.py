from datetime import datetime
from millPostDB import millPostDB
import re
import argparse
import os
from sqlsDash import sqlsDash
import os
import time

GH_OTA_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/'
GH_DGO_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/'
GH_PAIR_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/'
GH_MORE_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/more/testsuites/'

class TSLink:
    OTA = GH_OTA_PATH + 'run_ota_3D.py'
    OTA_POWER = GH_OTA_PATH + 'testsuites/ota_power_cycles.json'
    O1_DGO_OP_IDLE = GH_DGO_PATH + 'dgo_testsuite_IDLE_5hr.json'
    O1_DGO_OP_LIP = GH_DGO_PATH + 'dgo_testsuite_LIP_5hr.json'
    O1_DGO_OP_HIP = GH_DGO_PATH + 'dgo_testsuite_HIP_5hr.json'
    O1_DGO_OP_COOLDOWN = GH_DGO_PATH + 'dgo_testsuite_COOLDOWN_5hr.json'
    O1_DGO_OP_FLUFF = GH_DGO_PATH + 'dgo_testsuite_FLUFF_5hr.json'
    O2_DGO_OP_IDLE = GH_DGO_PATH + 'dgo_testsuite_IDLE_5hr_O2.json'
    O2_DGO_OP_LIP = GH_DGO_PATH + 'dgo_testsuite_LIP_5hr_O2.json'
    O2_DGO_OP_HIP = GH_DGO_PATH + 'dgo_testsuite_HIP_5hr_O2.json'
    O2_DGO_OP_COOLDOWN = GH_DGO_PATH + 'dgo_testsuite_COOLDOWN_5hr_O2.json'
    O2_DGO_OP_FLUFF = GH_DGO_PATH + 'dgo_testsuite_FLUFF_5hr_O2.json'
    O1_DGO_MASS_IDLE = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_IDLE.json'
    O1_DGO_MASS_LIP = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_LIP.json'
    O1_DGO_MASS_HIP = GH_DGO_PATH +'dgo_mass_add_5hr_min_runtime_HIP.json'
    O1_DGO_MASS_COOLDOWN = GH_DGO_PATH +'dgo_mass_add_5hr_min_runtime_COOLDOWN.json'
    O1_DGO_MASS_FLUFF = GH_DGO_PATH +'dgo_mass_add_5hr_min_runtime_FLUFF.json'
    O2_DGO_MASS_IDLE = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_IDLE_O2.json'
    O2_DGO_MASS_LIP = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_LIP_O2.json'
    O2_DGO_MASS_HIP = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_HIP_O2.json'
    O2_DGO_MASS_COOLDOWN = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_COOLDOWN_O2.json'
    O2_DGO_MASS_FLUFF = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_FLUFF_O2.json'
    O1_SAFETY = GH_DGO_PATH + 'safety_test.json'
    O2_SAFETY = GH_DGO_PATH + 'safety_test_O2.json'
    O1_PAIRING = GH_PAIR_PATH + 'pairing.json'
    O2_PAIRING = GH_PAIR_PATH + 'pairing_O2.json'    
    O1_LID = GH_DGO_PATH + 'lid_open_close_stress.json'
    O1_STARTA = GH_DGO_PATH + 'dgo_start_via_bin_stress_A.json'
    O1_STARTB = GH_DGO_PATH + 'dgo_start_via_bin_B.json'
    O2_STARTA = GH_DGO_PATH + 'dgo_start_via_bin_stress_A_O2.json'
    O2_STARTB = GH_DGO_PATH + 'dgo_start_via_bin_B_O2.json'
    EEPROM = GH_DGO_PATH + 'eeprom_stress_test.json'
    O1_CHILDA = GH_DGO_PATH + 'child_lock_stress_A.json'
    O1_CHILDB = GH_DGO_PATH + 'child_lock_B.json'
    O2_CHILDA = GH_DGO_PATH + 'child_lock_stress_A_O2.json'
    O2_CHILDB = GH_DGO_PATH + 'child_lock_B_O2.json'
    O1_BOOTA = GH_MORE_PATH + 'boot_cycle_stress_A_O1.json'
    O1_BOOTB = GH_MORE_PATH + 'boot_cycle_B_O1.json'
    O2_BOOTA = GH_MORE_PATH + 'dgo_test_boot_cycle.json'
    O2_BOOTB = GH_MORE_PATH + 'boot_cycle_B_O2.json'
    O2_BAT_D_A_M_H = GH_DGO_PATH + 'bat_dgo_add_mass_hip.json'
    O2_BAT_D_R_H = GH_DGO_PATH + 'bat_dgo_reset_hip.json'
    O2_BAT_D_S_C_S_W_H = GH_DGO_PATH + 'bat_dgo_sht40_cal_skip_when_hot.json'
    O2_BAT_S_C = GH_DGO_PATH + 'bat_dgo_sht40_calibration.json'
    O2_BAT_D_S_S_N_V = GH_DGO_PATH + 'bat_dgo_start_stop_no_vacation.json'
    O2_SMOKE_PAIRING = GH_PAIR_PATH + 'wifi_test_O2_automation.json'
    O2_BAT_D_J_E = GH_DGO_PATH + 'bat_dgo_jam_error.json'
    O2_BAT_D_J_I = GH_DGO_PATH + 'bat_dgo_jam_inactive.json'
    O2_BAT_D_H_M_F_A = GH_DGO_PATH + 'bat_dgo_hip_moisture_food_add.json'
    O2_BAT_D_H_W_S = GH_DGO_PATH + 'bat_dgo_heat_warning_status.json'
    O2_BAT_D_E_B = GH_DGO_PATH + 'bat_dgo_empty_bucket.json'
    O2_BAT_COOLDOWN_TEMP = GH_DGO_PATH + 'bat_dgo_cooldown_temp.json'
    O2_BAT_HEAT_LED = GH_DGO_PATH + 'bat_dgo_heat_led.json'    
    O2_BAT_PREMATURE_MASS_NO_RESET = GH_DGO_PATH + 'bat_dgo_premature_mass_no_reset.json'
    O2_BAT_LOCKED_WHEN_HOT_SHADOWS = GH_DGO_PATH + 'bat_dgo_locked_when_hot_shadows.json'
    O2_SMOKE_DGO_INACTIVE = GH_DGO_PATH + 'dgo_inactive.json'
    O2_SMOKE_TEST_LID = GH_DGO_PATH + 'lid_lock_smoke.json'
    
    #GUO_ADDED
    O2_BAT_VACATION_CLEAN_MODE = GH_DGO_PATH + 'bat_vacation_clean_mode.json'
    O2_BAT_VACATION_ECO_MODE = GH_DGO_PATH + 'bat_vacation_eco_mode.json'   
    O2_BAT_VACATION_ADD_MASS_COOLDOWN = GH_DGO_PATH + 'bat_dgo_vacation_add_mass_cooldown.json'
    O2_BAT_VACATION_RESET = GH_DGO_PATH + 'bat_dgo_vacation_reset.json'
    O2_BAT_D_GRINDER_SOFT_STALL_RETRY = GH_DGO_PATH + 'bat_grinder_soft_stall_retry.json'
    O2_BAT_D_GRINDER_STATE_LID = GH_DGO_PATH + 'bat_dgo_grinder_state_lid.json'
    O2_BAT_D_GRINDER_HIGH_TEMP_JAM = GH_DGO_PATH + 'bat_dgo_grinder_high_temp_jam.json'
    O2_BAT_D_GRINDER_JAM_AUTO_RETRY = GH_DGO_PATH + 'bat_dgo_grinder_jam_auto_retry.json'
    O2_BAT_D_FLUFF_NOT_RUN = GH_DGO_PATH + 'bat_dgo_fluff_not_run.json'
    O2_BAT_SET_START_TIME_DURING_HIP = GH_DGO_PATH + 'dgo_set_cycle_start_time_HIP_O2.json'
    O2_BAT_RESUME_FROM_LIP = GH_DGO_PATH + 'bat_dgo_resume_lip.json'
    O2_BAT_D_ALWAYS_LOCKED = GH_DGO_PATH + 'bat_dgo_always_locked.json'
    O2_BAT_D_ALWAYS_UNLOCKED = GH_DGO_PATH + 'bat_dgo_always_unlocked.json'
    O2_BAT_D_BUCKET_FULLNESS_LOW = GH_DGO_PATH + 'bat_dgo_bucket_fullness_low.json'
    O2_BAT_DELTA_MR_HIP_MASS_BUCKET = GH_DGO_PATH + 'bat_dgo_hip_mass_bucket.json'
    O2_BAT_D_LOCKED_WHEN_RUNNING = GH_DGO_PATH + 'bat_dgo_locked_when_running.json'
    O2_BAT_D_FR_HEAT_WARNING_STATUS = GH_DGO_PATH + 'bat_dgo_fr_heat_warning_status.json'
    O2_BAT_D_MASS_NO_CHANGE_RESET = GH_DGO_PATH + 'bat_dgo_mass_no_change_reset.json'
    O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS = GH_DGO_PATH + 'bat_dgo_lastDgoCycle_energy_shadows.json'
    O2_BAT_D_CYCLEENDTIME_LID_OPEN = GH_DGO_PATH + 'bat_dgo_cycleEndTime_lid_open.json'
    O2_BAT_D_UNPROCESSED_MASS_ZERO = GH_DGO_PATH + 'bat_dgo_unprocessed_mass_zero.json'
    O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE = GH_DGO_PATH + 'bat_dgo_mass_add_lid_open_close.json'
    O2_BAT_D_LIP_SKIPPED_HOT = GH_DGO_PATH + 'bat_dgo_lip_skipped_hot.json'

    # 8/12/2024
    O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE = GH_DGO_PATH + 'bat_dgo_hip_extension_lid_open_close.json'
    O2_BAT_START_DISCONNECTED = GH_DGO_PATH + 'bat_dgo_start_disconnected.json'
    O2_BAT_RESUME_DISCONNECTED = GH_DGO_PATH + 'bat_dgo_resume_disconnected.json'
    O2_BAT_HEAT_LED_INTERRUPTIONS = GH_DGO_PATH + 'bat_dgo_heat_led_interruptions.json'
    O2_BAT_VACATION_AFTER_EMPTY = GH_DGO_PATH + 'bat_dgo_vacation_after_empty.json'
    O2_BAT_RESUME_COOLDOWN = GH_DGO_PATH + 'bat_dgo_resume_cooldown.json'

    # 9/4/2024
    O2_BAT_VACATION_OTA_PRE = GH_DGO_PATH + 'bat_vacation_ota_pre.json'
    O2_BAT_VACATION_OTA_POST = GH_DGO_PATH + 'bat_vacation_ota_post.json'
    O2_BAT_BUCKET_CRASH_OTA_PRE = GH_DGO_PATH + 'bat_bucket_crash_ota_pre.json'
    O2_BAT_BUCKET_CRASH_OTA_POST = GH_DGO_PATH + 'bat_bucket_crash_ota_post.json'

class DBT:
    OTA_TABLE = 'OTA_TABLE'
    POWER_DURING_OTA_TABLE = 'POWER_DURING_OTA_TABLE'
    DGO_OP_PR_TABLE = 'DGO_OP_PR_TABLE'
    DGO_ADD_MASS_TABLE = 'DGO_ADD_MASS_TABLE'
    SAFETY_TEST_TABLE = 'SAFETY_TEST_TABLE'
    PAIRING_WITHOUT_BLE_TABLE = 'PAIRING_WITHOUT_BLE_TABLE'
    LID_OPEN_CLOSE_TABLE = 'LID_OPEN_CLOSE_TABLE'
    START_VIA_BIN_TABLE = 'START_VIA_BIN_TABLE'
    EEPROM_STRESS_TEST_TABLE = 'EEPROM_STRESS_TEST_TABLE'
    CHILD_LOCK_TABLE = 'CHILD_LOCK_TABLE'
    BOOT_CYCLE_TABLE = 'BOOT_CYCLE_TABLE'
    BAT_TABLE = 'BAT_TABLE'
    SMOKE_TEST_TABLE = 'SMOKE_TEST_TABLE'

class Suites:
    OTA_SELF = 'OTA_SELF'
    OTA_PROD_UPGRADE = 'OTA_PROD_UPGRADE'
    OTA_EXT_FT_UPGRADE = 'OTA_EXT_FT_UPGRADE'
    OTA_INT_FT_UPGRADE = 'OTA_INT_FT_UPGRADE'
    POWER_DURING_OTA = 'POWER_DURING_OTA'
    DGO_IDLE_OP_PR = 'DGO_IDLE_OP_PR'
    DGO_LIP_OP_PR = 'DGO_LIP_OP_PR'
    DGO_HIP_OP_PR = 'DGO_HIP_OP_PR'
    DGO_COOLDOWN_OP_PR = 'DGO_COOLDOWN_OP_PR'
    DGO_FLUFF_OP_PR = 'DGO_FLUFF_OP_PR'
    DGO_IDLE_ADD_MASS = 'DGO_IDLE_ADD_MASS'
    DGO_LIP_ADD_MASS = 'DGO_LIP_ADD_MASS'
    DGO_HIP_ADD_MASS = 'DGO_HIP_ADD_MASS'
    DGO_COOLDOWN_ADD_MASS = 'DGO_COOLDOWN_ADD_MASS'
    DGO_FLUFF_ADD_MASS = 'DGO_FLUFF_ADD_MASS'
    SAFETY_TEST = 'SAFETY_TEST'
    PAIRING_WITHOUT_BLE = 'PAIRING_WITHOUT_BLE'
    START_VIA_BIN_STRESS_A = 'START_VIA_BIN_STRESS_A'
    START_VIA_BIN_B = 'START_VIA_BIN_B'
    EEPROM_STRESS_TEST = 'EEPROM_STRESS_TEST'
    CHILD_LOCK_STRESS_TEST = 'CHILD_LOCK_STRESS_TEST'
    CHILD_LOCK_TEST = 'CHILD_LOCK_TEST'
    LID_OPEN_CLOSE = 'LID_OPEN_CLOSE'
    BOOT_CYCLE_STRESS_TEST = 'BOOT_CYCLE_STRESS_TEST'
    BOOT_CYCLE_TEST = 'BOOT_CYCLE_TEST'
    BAT_D_A_M_H_TEST = 'BAT_D_A_M_H_TEST'
    BAT_D_R_H_TEST = 'BAT_D_R_H_TEST'
    BAT_S_C_TEST = 'BAT_S_C_TEST'
    BAT_D_S_C_S_W_H_TEST = 'BAT_D_S_C_S_W_H_TEST'
    BAT_D_S_S_N_V_TEST = 'BAT_D_S_S_N_V_TEST'
    SMOKE_PAIRING_TEST = 'SMOKE_PAIRING_TEST'
    BAT_D_J_E_TEST = 'BAT_D_J_E_TEST'
    BAT_D_J_I_TEST = 'BAT_D_J_I_TEST'
    BAT_D_H_M_F_A_TEST = 'BAT_D_H_M_F_A_TEST'
    BAT_D_H_W_S_TEST = 'BAT_D_H_W_S_TEST'
    BAT_D_E_B_TEST = 'BAT_D_E_B_TEST'
    BAT_COOLDOWN_TEMP_TEST = 'BAT_COOLDOWN_TEMP_TEST'
    BAT_HEAT_LED_TEST = 'BAT_HEAT_LED_TEST'
    BAT_PREMATURE_MASS_NO_RESET_TEST = 'BAT_PREMATURE_MASS_NO_RESET_TEST'
    BAT_LOCKED_WHEN_HOT_SHADOWS_TEST = 'BAT_LOCKED_WHEN_HOT_SHADOWS_TEST'
    SMOKE_DGO_INACTIVE_TEST = 'SMOKE_DGO_INACTIVE_TEST'
    SMOKE_TEST_LID_TEST = 'SMOKE_TEST_LID_TEST'

    #GUO_ADDED
    BAT_VACATION_CLEAN_MODE_TEST = 'BAT_VACATION_CLEAN_MODE_TEST'
    BAT_VACATION_ECO_MODE_TEST = 'BAT_VACATION_ECO_MODE_TEST' 
    BAT_VACATION_ADD_MASS_COOLDOWN_TEST = 'BAT_VACATION_ADD_MASS_COOLDOWN_TEST'
    BAT_VACATION_RESET_TEST = 'BAT_VACATION_RESET_TEST'
    BAT_D_GRINDER_SOFT_STALL_RETRY_TEST = 'BAT_D_GRINDER_SOFT_STALL_RETRY_TEST'
    BAT_D_GRINDER_STATE_LID_TEST = 'BAT_D_GRINDER_STATE_LID_TEST'
    BAT_D_GRINDER_HIGH_TEMP_JAM_TEST = 'BAT_D_GRINDER_HIGH_TEMP_JAM_TEST'
    BAT_D_GRINDER_JAM_AUTO_RETRY_TEST = 'BAT_D_GRINDER_JAM_AUTO_RETRY_TEST'
    BAT_D_FLUFF_NOT_RUN_TEST = 'BAT_D_FLUFF_NOT_RUN_TEST'
    BAT_SET_START_TIME_DURING_HIP_TEST = 'BAT_SET_START_TIME_DURING_HIP_TEST'
    BAT_RESUME_FROM_LIP_TEST = 'BAT_RESUME_FROM_LIP_TEST'
    BAT_D_ALWAYS_LOCKED_TEST = 'BAT_D_ALWAYS_LOCKED_TEST'
    BAT_D_ALWAYS_UNLOCKED_TEST = 'BAT_D_ALWAYS_UNLOCKED_TEST'
    BAT_D_BUCKET_FULLNESS_LOW_TEST = 'BAT_D_BUCKET_FULLNESS_LOW_TEST'
    BAT_DELTA_MR_HIP_MASS_BUCKET_TEST = 'BAT_DELTA_MR_HIP_MASS_BUCKET_TEST'
    BAT_D_LOCKED_WHEN_RUNNING_TEST = 'BAT_D_LOCKED_WHEN_RUNNING_TEST'
    BAT_D_FR_HEAT_WARNING_STATUS_TEST = 'BAT_D_FR_HEAT_WARNING_STATUS_TEST'
    BAT_D_MASS_NO_CHANGE_RESET_TEST = 'BAT_D_MASS_NO_CHANGE_RESET_TEST'
    BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST = 'BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST'
    BAT_D_CYCLEENDTIME_LID_OPEN_TEST = 'BAT_D_CYCLEENDTIME_LID_OPEN_TEST'
    BAT_D_UNPROCESSED_MASS_ZERO_TEST = 'BAT_D_UNPROCESSED_MASS_ZERO_TEST'
    BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST = 'BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST'
    BAT_D_LIP_SKIPPED_HOT_TEST = 'BAT_D_LIP_SKIPPED_HOT_TEST'

    # 8/12/2024
    BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST = 'BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST'
    BAT_START_DISCONNECTED_TEST = 'BAT_START_DISCONNECTED_TEST'
    BAT_RESUME_DISCONNECTED_TEST = 'BAT_RESUME_DISCONNECTED_TEST'
    BAT_HEAT_LED_INTERRUPTIONS_TEST = 'BAT_HEAT_LED_INTERRUPTIONS_TEST'
    BAT_VACATION_AFTER_EMPTY_TEST = 'BAT_VACATION_AFTER_EMPTY_TEST'
    BAT_RESUME_COOLDOWN_TEST = 'BAT_RESUME_COOLDOWN_TEST'

    # 9/4/2024
    BAT_VACATION_OTA_PRE_TEST = 'BAT_VACATION_OTA_PRE_TEST'
    BAT_VACATION_OTA_POST_TEST = 'BAT_VACATION_OTA_POST_TEST'  
    BAT_BUCKET_CRASH_OTA_PRE_TEST = 'BAT_BUCKET_CRASH_OTA_PRE_TEST'
    BAT_BUCKET_CRASH_OTA_POST_TEST = 'BAT_BUCKET_CRASH_OTA_POST_TEST'  


class LogFiles:
    O1_patterns = [
        'O1_ota_self_results_{version}.txt',
        'O1_ota_prod_upgrade_results_{version}.txt',
        'O1_ota_ft_upgrade_results_{version}.txt',
        'O1_ota_int_upgrade_results_{version}.txt',
        'O1_ota_ext_upgrade_results_{version}.txt',
        'O1_ota_power_results_{version}.txt',
        'O1_dgo_idle_mass_results_{version}.txt',
        'O1_dgo_idle_op_results_{version}.txt',
        'O1_dgo_lip_mass_results_{version}.txt',
        'O1_dgo_lip_op_results_{version}.txt',
        'O1_dgo_hip_mass_results_{version}.txt',
        'O1_dgo_hip_op_results_{version}.txt',
        'O1_dgo_cooldown_mass_results_{version}.txt',
        'O1_dgo_cooldown_op_results_{version}.txt',
        'O1_dgo_fluff_mass_results_{version}.txt',
        'O1_dgo_fluff_op_results_{version}.txt',
        'O1_child_lock_A_stress_results_{version}.txt',
        'O1_child_lock_B_results_{version}.txt',
        'O1_start_via_bin_A_stress_results_{version}.txt',
        'O1_start_via_bin_B_results_{version}.txt',
        'O1_eeprom_stress_results_{version}.txt',
        'O1_pairing_results_{version}.txt',
        'O1_safety_test_results_{version}.txt',
        'O1_lid_open_close_results_{version}.txt',
        'O1_boot_cycle_A_stress_results_{version}.txt'
    ]

    O2_patterns = [
        'O2_ota_self_results_{version}.txt',
        'O2_ota_ft_upgrade_results_{version}.txt',
        'O2_ota_prod_upgrade_results_{version}.txt',
        'O2_ota_int_upgrade_results_{version}.txt',
        'O2_ota_ext_upgrade_results_{version}.txt',
        'O2_ota_power_results_{version}.txt',
        'O2_dgo_idle_mass_results_{version}.txt',
        'O2_dgo_idle_op_results_{version}.txt',
        'O2_dgo_lip_mass_results_{version}.txt',
        'O2_dgo_lip_op_results_{version}.txt',
        'O2_dgo_hip_mass_results_{version}.txt',
        'O2_dgo_hip_op_results_{version}.txt',
        'O2_dgo_cooldown_mass_results_{version}.txt',
        'O2_dgo_cooldown_op_results_{version}.txt',
        'O2_dgo_fluff_mass_results_{version}.txt',
        'O2_dgo_fluff_op_results_{version}.txt',
        'O2_child_lock_A_stress_results_{version}.txt',
        'O2_child_lock_B_results_{version}.txt',
        'O2_start_via_bin_A_stress_results_{version}.txt',
        'O2_start_via_bin_B_results_{version}.txt',
        'O2_eeprom_stress_results_{version}.txt',
        'O2_safety_test_results_{version}.txt',
        'O2_pairing_results_{version}.txt',
        'O2_boot_cycle_A_stress_results_{version}.txt',
        'O2_bat_dgo_add_mass_hip_results_{version}.txt',
        'O2_bat_dgo_reset_hip_results_{version}.txt',
        'O2_bat_dgo_sht40_calibration_results_{version}.txt',
        'O2_bat_dgo_sht40_cal_skip_when_hot_results_{version}.txt',
        'O2_bat_dgo_start_stop_no_vacation_results_{version}.txt',
        'O2_smoke_pairing_results_{version}.txt',
        'O2_bat_dgo_jam_error_results_{version}.txt',
        'O2_bat_dgo_jam_inactive_results_{version}.txt',
        'O2_bat_dgo_hip_moisture_food_add_results_{version}.txt',
        'O2_bat_dgo_heat_warning_status_results_{version}.txt',
        'O2_bat_dgo_empty_bucket_results_{version}.txt',
        'O2_bat_cooldown_temp_results_{version}.txt',
        'O2_bat_premature_mass_no_reset_results_{version}.txt',
        'O2_bat_heat_led_results_{version}.txt',
        'O2_bat_locked_when_hot_shadows_results_{version}.txt',
        'O2_smoke_dgo_inactive_results_{version}.txt',
        'O2_smoke_test_lid_results_{version}.txt',

        #GUO_ADDED
        'O2_bat_vacation_clean_mode_results_{version}.txt',
        'O2_bat_vacation_eco_mode_results_{version}.txt',
        'O2_bat_vacation_add_mass_cooldown_results_{version}.txt',
        'O2_bat_vacation_reset_results_{version}.txt',
        'O2_bat_grinder_soft_stall_retry_same_dir_results_{version}.txt',
        'O2_bat_grinder_state_lid_results_{version}.txt',
        'O2_bat_grinder_high_temp_jam_results_{version}.txt',
        'O2_bat_grinder_jam_auto_retry_results_{version}.txt',
        'O2_bat_fluff_not_run_results_{version}.txt',
        'O2_bat_set_dgo_start_time_during_hip_results_{version}.txt',
        'O2_bat_resume_from_lip_results_{version}.txt',
        'O2_bat_always_locked_results_{version}.txt',
        'O2_bat_always_unlocked_results_{version}.txt',
        'O2_bat_bucket_fullness_detection_results_{version}.txt',
        'O2_bat_delta_mr_mass_bucket_results_{version}.txt',
        'O2_bat_locked_when_running_results_{version}.txt',
        'O2_bat_fr_heat_warning_status_results_{version}.txt',
        'O2_bat_mass_no_change_reset_results_{version}.txt',
        'O2_bat_lastDgoCycle_energy_shadows_results_{version}.txt',
        'O2_bat_cycleEndTime_lid_open_results_{version}.txt',
        'O2_bat_unprocessed_mass_zero_results_{version}.txt',
        'O2_bat_mass_add_lid_open_close_results_{version}.txt',
        'O2_bat_lip_skipped_hot_results_{version}.txt',

        # 8/12/2024
        'O2_bat_hip_extension_lid_open_close_results_{version}.txt',
        'O2_bat_start_disconnected_results_{version}.txt',
        'O2_bat_resume_disconnected_results_{version}.txt',
        'O2_bat_heat_led_interruptions_results_{version}.txt',
        'O2_bat_vacation_after_empty_results_{version}.txt',
        'O2_bat_resume_cooldown_results_{version}.txt',

        # 9/4/2024
        'O2_bat_vacation_ota_pre_results_{version}.txt',
        'O2_bat_vacation_ota_post_results_{version}.txt',
        'O2_bat_bucket_crash_ota_pre_results_{version}.txt',
        'O2_bat_bucket_crash_ota_post_results_{version}.txt'

    ]

class stagesN:
    idle = 'idle'
    lip = 'lip'
    hip = 'hip'
    cooldown = 'cooldown'
    fluff = 'fluff'  

class TestMGrp:
    ota = 'ota'
    dgo = 'dgo'
    more = 'more'
    mon = 'mon'
    stress = 'stress'
    normal = 'normal'

class TestParts:
    op = 'op'
    mass = 'mass'
    eeprom = 'eeprom'
    pairing = 'pairing'
    start = 'start'
    child = 'child'
    lid = 'lid'
    safety = 'safety'
    boot = 'boot'
    bat = 'bat'
    smoke = 'smoke'

    prod = 'prod'

    int = 'int'
    ext = 'ext'
    
    A = 'A'
    B = 'B'

    dgo = 'dgo'
    add = 'add'

    hip = 'hip'
    stop = 'stop'
    sht40 = 'sht40'
    calibration = 'calibration'
    skip = 'skip'
    jam = 'jam'
    error = 'error'
    inactive = 'inactive'
    heat = 'heat'
    empty = 'empty'
    bucket = 'bucket'
    cooldown = "cooldown"
    temp = 'temp'
    led = 'led'

    self = 'self'

class otaType:
    self = 'self'
    prodUG = 'prodUG'
    intFTUG = 'intFTUG'
    extFTUG = 'extFTUG'
    power = 'power'

class batType:
    cooldown_temp = 'cooldown_temp'
    empty_bucket = 'empty_bucket'
    jam_inactive = 'jam_inactive'
    hip_moisture_food_add = 'hip_moisture_food_add'
    jam_error = 'jam_error'
    sht40_calibration = 'sht40_calibration'
    sht40_cal_skip_when_hot = 'sht40_cal_skip_when_hot'
    start_stop_no_vacation = 'start_stop_no_vacation'
    add_mass_hip = 'add_mass_hip'
    reset_hip = 'reset_hip'
    heat_warning_status = 'heat_warning_status'
    heat_led = 'heat_led'
    premature_mass_no_reset = 'premature_mass_no_reset' 
    locked_when_hot_shadows = 'locked_when_hot_shadows'

    #GUO_ADDED
    vacation_clean_mode = 'vacation_clean_mode'
    vacation_eco_mode = 'vacation_eco_mode'
    vacation_add_mass_cooldown = 'vacation_add_mass_cooldown'
    vacation_reset = 'vacation_reset'
    grinder_soft_stall_retry = 'grinder_soft_stall_retry'
    grinder_state_lid = 'grinder_state_lid'
    grinder_high_temp_jam = 'grinder_high_temp_jam'
    grinder_jam_auto_retry = 'grinder_jam_auto_retry'
    fluff_not_run = 'fluff_not_run'
    cycle_start_time_HIP = 'cycle_start_time_HIP'
    resume_lip = 'resume_lip'
    always_locked = 'always_locked'
    always_unlocked = 'always_unlocked'
    bucket_fullness_low = 'bucket_fullness_low'
    dgo_hip_mass_bucket = 'dgo_hip_mass_bucket'
    locked_when_running = 'locked_when_running'
    fr_heat_warning_status = 'fr_heat_warning_status'
    mass_no_change_reset = 'mass_no_change_reset'
    lastDgoCycle_energy_shadows = 'lastdgocycle_energy_shadows'
    cycleEndTime_lid_open = 'cycleendtime_lid_open'
    unprocessed_mass_zero = 'unprocessed_mass_zero'
    mass_add_lid_open_close = 'mass_add_lid_open_close'
    lip_skipped_hot = 'lip_skipped_hot'

    # 8/12/2024
    hip_extension_lid_open_close = 'hip_extension_lid_open_close'
    start_disconnected = 'start_disconnected'
    resume_disconnected = 'resume_disconnected'
    heat_led_interruptions = 'heat_led_interruptions'
    vacation_after_empty = 'vacation_after_empty'
    resume_cooldown = 'resume_cooldown'

    # 9/4/2024
    bat_vacation_ota_pre = 'bat_vacation_ota_pre'
    bat_vacation_ota_post = 'bat_vacation_ota_post'
    bat_bucket_crash_ota_pre = 'bat_bucket_crash_ota_pre'
    bat_bucket_crash_ota_post = 'bat_bucket_crash_ota_post'



class smokeType:
    pairing = 'pairing'
    dgo_inactive = 'dgo_inactive'
    test_lid = 'test_lid'

class OscarType:
    O1 = 'O1'
    O2 = 'O2'

class pattern:
    quote_open = "s ("
    quote_close = ") ============"
    sline = "s ================="
    runcount = "RUN COUNT:"
    linerun = "================= Run:"
    passed = "-- Passed! ***"
    failed = "-- Failed! ***"
    endtimestamp = "End timestamp"
    takesecondtocomplete = "Takes seconds to complete:"
    invalidtype = "Invalid Type: "
    invalidoscartype = "Invalid Oscar Type"
    invalidtestsuite = "invalid test suite!"
    invalidparts = "Invalid parts!"
    allversionfiles = "All specified version files are present."
    metadata_O1 = "_metadata_O1.sh"
    metadata_O2 = "_metadata.sh"


class startwith:
    passed = "PASSED"
    failed = "FAILED"
    rls = "rls-"
    dbg = "dbg-"

class ParseData(millPostDB):
    def __init__(self, database, host, user, password, port, sysLogF):
        super().__init__(database, host, user, password, port, sysLogF)
        self.run_details = {}  
        self.tests_passed = 0
        self.tests_failed = 0
        self.total_duration_seconds = 0
        self.datetime_format = "%m-%d %H:%M"
        self.start_times = {}
        self.end_times = {}
        self.test_durations = []  
        self.first_line = None
        self.second_line = None
        self.total_collected = None
        self.dgo_passed = 0
        self.dgo_failed = 0
        self.total_tests = 0
        self.dgo_total_time = 0
        self.dgo_run_count = 0
        self.results = {}

    def extract_timestamp_with_format_detection(self, date_time_string):
        formats = [
            {"format": "%Y-%m-%d %H:%M:%S,%f", "has_year": True},
            {"format": "%Y-%m-%d %H:%M:%S", "has_year": True},
            {"format": "%m-%d %H:%M", "has_year": False}
        ]

        current_year = datetime.now().year
        for fmt in formats:
            try:
                if fmt["format"].endswith(",%f"): 
                    datetime_part, milliseconds = date_time_string.split(',')
                    datetime_object = datetime.strptime(datetime_part, fmt["format"].rstrip(",%f"))
                    timestamp = datetime_object.timestamp() + int(milliseconds) / 1000
                else:
                    datetime_object = datetime.strptime(date_time_string, fmt["format"])
                    timestamp = datetime_object.timestamp()
                    
                if not fmt["has_year"]:
                    datetime_object = datetime_object.replace(year=current_year)
                    timestamp = datetime_object.timestamp()
                
                return timestamp
            except ValueError:
                continue
        return None

    def detect_invalid_timestamps(self, parts):
        formats = [
            "%Y-%m-%d %H:%M:%S,%f",
            "%Y-%m-%d %H:%M:%S",
            "%m-%d %H:%M",
            "%Y-%m-%d",
            "%H:%M:%S",
            "%m-%d",
            "%H:%M"
        ]
        
        def is_valid_datetime(part):
            for fmt in formats:
                try:
                    datetime.strptime(part, fmt)
                    return True 
                except ValueError:
                    continue 
            return False 

        is_first_part_valid = is_valid_datetime(parts[0])
        is_second_part_valid = is_valid_datetime(parts[1])
        
        return not (is_first_part_valid or is_second_part_valid)

    def estimate_hours(self, x):
        hours = x // 3600
        estimate = f"~{hours}"
        if x % 3600 > 1800:
            hours += 1
            estimate = f"~{hours}"
        elif x % 3600 > 0:
            if hours > 0:
                estimate += ".5"
            else:
                estimate = "~0.5"
        estimate += "hrs"
        return estimate


    def extract_filename(self, path):
        return path.split('/')[-1]

    def parseOTAFile(self, file_path):
        with open(file_path, 'r') as file:
            self.first_line = file.readline().strip()  
            self.second_line = file.readline().strip()  

            for line in file:
                parts = line.split()
                if not parts:
                    continue

                if len(parts) < 2:
                    continue

                if self.detect_invalid_timestamps(parts):
                    continue

                timestamp_str = parts[0] + " " + parts[1]
                timestamp = self.extract_timestamp_with_format_detection(timestamp_str)

                if pattern.linerun in line:
                    try:
                        run_part = line.split(pattern.linerun)[1].strip()
                        if '->' in run_part:
                            run_id, sub_run_id = run_part.split('->')
                            run_id = run_id.strip()
                            sub_run_id = sub_run_id.strip()

                            if run_id in self.run_details:
                                self.run_details[run_id].add(sub_run_id)
                            else:
                                self.run_details[run_id] = {sub_run_id}

                            run_key = f"{run_id}->{sub_run_id}"
                            self.start_times[run_key] = timestamp
                        else:
                            print(f"Line does not contain expected '->': {line.strip()}")
                    except ValueError as e:
                        print(f"Error processing line: {line.strip()}. Error: {e}")
                        
                elif pattern.endtimestamp in line:
                    for run_key in self.start_times.keys():
                        if run_key not in self.end_times:
                            self.end_times[run_key] = timestamp
                            break

                elif pattern.passed in line:
                    self.tests_passed += 1

                elif pattern.failed in line:
                    self.tests_failed += 1        

                elif pattern.takesecondtocomplete in line:
                    try:
                        duration_str = line.split(pattern.takesecondtocomplete)[1].strip()
                        duration_seconds = int(duration_str)
                        self.test_durations.append(duration_seconds)
                    except ValueError as e:
                        print(f"Error processing line for duration: '{line.strip()}'. Error: {e}")


    def getSerialNum(self):
        return self.first_line[self.first_line.find("['")+2:self.first_line.find("']")]
    
    def getThingGrp(self):
        return self.second_line[self.second_line.find("['")+2:self.second_line.find("']")]

    def getPassed(self):
        return self.tests_passed
    
    def getFailed(self):
        return self.tests_failed

    def getMin(self):
        return min(self.test_durations)
    
    def getMax(self):
        return max(self.test_durations)

    def getAvg(self):
        total = sum(self.test_durations)
        return total // len(self.test_durations)

    def calculateRunTotals(self):
        total_runs = len(self.run_details)
        total_sub_runs = sum(len(sub_runs) for sub_runs in self.run_details.values())
        return total_runs, total_sub_runs

    def calculateDuration(self):
        for run_key, start_time in self.start_times.items():
            if run_key in self.end_times:
                self.total_duration_seconds += (self.end_times[run_key] - start_time)
                self.total_duration_seconds += 60

        return self.total_duration_seconds
    
    def convertSQL(self, line, placeholder, replacement):
        try:
            pattern = re.escape(placeholder)
            line = re.sub(pattern, replacement, line)
        except Exception as e:
            print(f"Exception in converting SQL: {e}")    
        return line

    def queryServerName(self, sn):
        pass

    def queryFKeyReportT(self, oscarT, buildN): 
        vSql = self.convertSQL(sqlsDash.report_fk_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)[0][0]

    def queryFKeyServerT(self, serverN, runnerN):
        vSql = self.convertSQL(sqlsDash.server_fk_q, '[serverN]', serverN)
        vSql = self.convertSQL(vSql, '[runnerN]', runnerN)
        return  self.queryData(vSql)[0][0]

    def queryFKeyDeviceT(self, sn):
        vSql = self.convertSQL(sqlsDash.device_fk_q, '[SN]', sn)
        return  self.queryData(vSql)[0][0]

    def queryJira(self, oscarT, buildN):
        vSql = self.convertSQL(sqlsDash.jiras_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)

    def queryBlocker(self, oscarT, buildN):
        vSql = self.convertSQL(sqlsDash.blockers_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)

    def queryNotes(self, oscarT, buildN):
        vSql = self.convertSQL(sqlsDash.build_notes_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)[0][0]

    def fetchFailedNum(self, sn, grp):
        # temparary hard-codes the failed number
        # TODO: fetch AWS API for it
        return 0
        
    def fetchRetryPassNum(self, sn, grp):
        # temparary hard-codes the Retries Pass number
        # TODO: fetch AWS API for it
        return 0

    def convert_version(self, version_str):
        if version_str.startswith(startwith.dbg):
            return startwith.rls + version_str[4:]
        elif version_str.startswith(startwith.rls):
            return startwith.dbg + version_str[4:]
        else:
            return version_str

    def extractFilename(self, path):
        filename = os.path.basename(path)
        return filename

    def fillStaticResultsOTA(self, parts, results):
        if parts[2] == TestParts.self:
            results["TestExecuted"] = 1
            results["TestType"] = TestParts.self
            results["TCLink"] = TSLink.OTA
            results["Tbl"] = DBT.OTA_TABLE
            results["Suite"] = Suites.OTA_SELF
        elif parts[2] == TestParts.prod:
            results["TestExecuted"] = 2
            results["TestType"] = otaType.prodUG
            results["TCLink"] = TSLink.OTA
            results["Tbl"] = DBT.OTA_TABLE
            results["Suite"] = Suites.OTA_PROD_UPGRADE
        elif parts[2] == TestParts.int:
            results["TestExecuted"] = 2
            results["TestType"] = otaType.intFTUG
            results["TCLink"] = TSLink.OTA
            results["Tbl"] = DBT.OTA_TABLE
            results["Suite"] = Suites.OTA_INT_FT_UPGRADE
        elif parts[2] == TestParts.ext:
            results["TestExecuted"] = 2
            results["TestType"] = otaType.extFTUG
            results["TCLink"] = TSLink.OTA
            results["Tbl"] = DBT.OTA_TABLE
            results["Suite"] = Suites.OTA_EXT_FT_UPGRADE
        elif parts[2] == otaType.power:
            results["TestExecuted"] = 20
            results["TestType"] = otaType.power    
            results["TCLink"] = TSLink.OTA_POWER
            results["Tbl"] = DBT.POWER_DURING_OTA_TABLE    
            results["Suite"] = Suites.POWER_DURING_OTA
        else:
            print(pattern.invalidtype, parts[2])
        return results

    def fillStaticResultsDGO(self, parts, results):
        if parts[1] == TestMGrp.dgo:
            self.DGOParts(parts, results)
        elif parts[1] == TestParts.eeprom:
            results["TestType"] = None
            results["TCLink"] = TSLink.EEPROM
            results["Tbl"] = DBT.EEPROM_STRESS_TEST_TABLE
            results["Suite"] = Suites.EEPROM_STRESS_TEST
        elif parts[1] == TestParts.pairing:
            results["TestType"] = None
            if parts[0] == OscarType.O1:
                results["TCLink"] = TSLink.O1_PAIRING
            elif parts[0] == OscarType.O2:
                results["TCLink"] = TSLink.O2_PAIRING
            else:
                print(pattern.invalidoscartype)

            results["Tbl"] = DBT.PAIRING_WITHOUT_BLE_TABLE    
            results["Suite"] = Suites.PAIRING_WITHOUT_BLE 
        elif parts[1] == TestParts.start:
            self.StartViaBinParts(parts, results)

        elif parts[1] == TestParts.child:
            self.ChildLockParts(parts, results)

        elif parts[1] == TestParts.lid:
            results["TestType"] = None
            results["TCLink"] = TSLink.O1_LID
            results["Tbl"] = DBT.LID_OPEN_CLOSE_TABLE   
            results["Suite"] = Suites.LID_OPEN_CLOSE

        elif parts[1] == TestParts.safety:
            results["TestType"] = None
            results["TCLink"] = TSLink.O1_SAFETY
            results["Tbl"] = DBT.SAFETY_TEST_TABLE   
            results["Suite"] = Suites.SAFETY_TEST

        elif parts[1] == TestParts.boot:
            if parts[3] == TestParts.A:
                results["TestType"] = TestMGrp.stress
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_BOOTA
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_BOOTA
                else:
                    print(pattern.invalidoscartype)                    
                
                results["Tbl"] = DBT.BOOT_CYCLE_TABLE     
                results["Suite"] = Suites.BOOT_CYCLE_STRESS_TEST 
            elif parts[3] == TestParts.B:    
                results["TestType"] = TestMGrp.normal
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_BOOTB
                elif parts[0] == OscarType:
                    results["TCLink"] = TSLink.O2_BOOTB
                else:
                    print(pattern.invalidoscartype)                      
                
                results["Tbl"] = DBT.BOOT_CYCLE_TABLE     
                results["Suite"] = Suites.BOOT_CYCLE_TEST
            else:
                print(pattern.invalidtype, parts[3])

        elif parts[1] == TestParts.bat:
            results["TestType"] = None
            results["Tbl"] = DBT.BAT_TABLE   
            results["Stage"] = ''
            if parts[2] == TestParts.dgo:
                if parts[3] == TestParts.add and parts[4] == TestParts.mass:
                    results["TCLink"] = TSLink.O2_BAT_D_A_M_H
                    results["Suite"] = Suites.BAT_D_A_M_H_TEST
                    results["Stage"] = TestParts.hip
                    results["Type"] = batType.add_mass_hip
                elif parts[3] == 'reset' and parts[4] == TestParts.hip:
                    results["TCLink"] = TSLink.O2_BAT_D_R_H
                    results["Suite"] = Suites.BAT_D_R_H_TEST
                    results["Stage"] = TestParts.hip
                    results["Type"] = batType.reset_hip
                elif parts[3] == 'start' and parts[4] == TestParts.stop:
                    results["TCLink"] = TSLink.O2_BAT_D_S_S_N_V
                    results["Suite"] = Suites.BAT_D_S_S_N_V_TEST
                    results["Type"] = batType.start_stop_no_vacation
                elif parts[3] == 'sht40':
                    if parts[4] == 'calibration':
                        results["TCLink"] = TSLink.O2_BAT_S_C
                        results["Suite"] = Suites.BAT_S_C_TEST
                        results["Type"] = batType.sht40_calibration
                    elif parts[4] == 'cal' and parts[5] == 'skip':
                        results["TCLink"] = TSLink.O2_BAT_D_S_C_S_W_H
                        results["Suite"] = Suites.BAT_D_S_C_S_W_H_TEST
                        results["Type"] = batType.sht40_cal_skip_when_hot

                elif parts[3] == 'jam':
                    if parts[4] == 'error':
                        results["TCLink"] = TSLink.O2_BAT_D_J_E
                        results["Suite"] = Suites.BAT_D_J_E_TEST
                        results["Type"] = batType.jam_error
                    elif parts[4] == 'inactive':
                        results["TCLink"] = TSLink.O2_BAT_D_J_I
                        results["Suite"] = Suites.BAT_D_J_I_TEST
                        results["Type"] = batType.jam_inactive
                elif parts[3] == TestParts.hip and parts[4] == 'moisture':
                    results["TCLink"] = TSLink.O2_BAT_D_H_M_F_A
                    results["Suite"] = Suites.BAT_D_H_M_F_A_TEST
                    results["Stage"] = TestParts.hip
                    results["Type"] = batType.hip_moisture_food_add

                elif parts[3] == 'heat':
                    results["TCLink"] = TSLink.O2_BAT_D_H_W_S
                    results["Suite"] = Suites.BAT_D_H_W_S_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.heat_warning_status
                elif parts[3] == 'empty' and parts[4] == 'bucket':
                    results["TCLink"] = TSLink.O2_BAT_D_E_B
                    results["Suite"] = Suites.BAT_D_E_B_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.empty_bucket
            



            elif parts[2] == "cooldown":
                if parts[3] == 'temp':
                    results["TCLink"] = TSLink.O2_BAT_COOLDOWN_TEMP
                    results["Suite"] = Suites.BAT_COOLDOWN_TEMP_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.cooldown_temp                  
            elif parts[2] == "heat":

                if parts[3] == 'led' and parts[4] == 'interruptions':
                    results["TCLink"] = TSLink.O2_BAT_HEAT_LED_INTERRUPTIONS
                    results["Suite"] = Suites.BAT_HEAT_LED_INTERRUPTIONS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.heat_led_interruptions   

                elif parts[3] == 'led':   
                    results["TCLink"] = TSLink.O2_BAT_HEAT_LED
                    results["Suite"] = Suites.BAT_HEAT_LED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.heat_led   


            elif parts[2] == "premature":
                if parts[3] == TestParts.mass:
                    results["TCLink"] = TSLink.O2_BAT_PREMATURE_MASS_NO_RESET
                    results["Suite"] = Suites.BAT_PREMATURE_MASS_NO_RESET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.premature_mass_no_reset  



            #GUO_ADDED
            elif parts[2] == "locked":
                if parts[4] == 'hot' and parts[5] == 'shadows':
                    results["TCLink"] = TSLink.O2_BAT_LOCKED_WHEN_HOT_SHADOWS
                    results["Suite"] = Suites.BAT_LOCKED_WHEN_HOT_SHADOWS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.locked_when_hot_shadows 
                elif parts[3] == 'when':
                    results["TCLink"] = TSLink.O2_BAT_D_LOCKED_WHEN_RUNNING
                    results["Suite"] = Suites.BAT_D_LOCKED_WHEN_RUNNING_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.locked_when_running 

            elif parts[2] == "fluff":
                if parts[3] == 'not':
                    results["TCLink"] = TSLink.O2_BAT_D_FLUFF_NOT_RUN
                    results["Suite"] = Suites.BAT_D_FLUFF_NOT_RUN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.fluff_not_run  
            elif parts[2] == "set":
                if parts[3] == 'dgo':
                    results["TCLink"] = TSLink.O2_BAT_SET_START_TIME_DURING_HIP
                    results["Suite"] = Suites.BAT_SET_START_TIME_DURING_HIP_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.cycle_start_time_HIP  


            elif parts[2] == "resume":
                if parts[3] == 'from':
                    results["TCLink"] = TSLink.O2_BAT_RESUME_FROM_LIP
                    results["Suite"] = Suites.BAT_RESUME_FROM_LIP_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.resume_lip  
                elif parts[3] == 'disconnected':
                    results["TCLink"] = TSLink.O2_BAT_RESUME_DISCONNECTED
                    results["Suite"] = Suites.BAT_RESUME_DISCONNECTED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.resume_disconnected    
                elif parts[3] == 'cooldown':
                    results["TCLink"] = TSLink.O2_BAT_RESUME_COOLDOWN
                    results["Suite"] = Suites.BAT_RESUME_COOLDOWN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.resume_cooldown    

            elif parts[2] == "bucket":
                if parts[3] == 'fullness':
                    results["TCLink"] = TSLink.O2_BAT_D_BUCKET_FULLNESS_LOW
                    results["Suite"] = Suites.BAT_D_BUCKET_FULLNESS_LOW_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bucket_fullness_low  


                elif parts[3] == 'crash' and parts[4] == 'ota' and parts[5] == 'pre':
                    results["TCLink"] = TSLink.O2_BAT_BUCKET_CRASH_OTA_PRE
                    results["Suite"] = Suites.BAT_BUCKET_CRASH_OTA_PRE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_bucket_crash_ota_pre    

                elif parts[3] == 'crash' and parts[4] == 'ota' and parts[5] == 'post':
                    results["TCLink"] = TSLink.O2_BAT_BUCKET_CRASH_OTA_POST
                    results["Suite"] = Suites.BAT_BUCKET_CRASH_OTA_POST_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_bucket_crash_ota_post    




            elif parts[2] == "fr":
                if parts[3] == 'heat':
                    results["TCLink"] = TSLink.O2_BAT_D_FR_HEAT_WARNING_STATUS
                    results["Suite"] = Suites.BAT_D_FR_HEAT_WARNING_STATUS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.fr_heat_warning_status  

            elif parts[2] == "lastDgoCycle":
                if parts[3] == 'energy':
                    results["TCLink"] = TSLink.O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS
                    results["Suite"] = Suites.BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.lastDgoCycle_energy_shadows 

            elif parts[2] == "cycleEndTime":
                if parts[3] == 'lid':
                    results["TCLink"] = TSLink.O2_BAT_D_CYCLEENDTIME_LID_OPEN
                    results["Suite"] = Suites.BAT_D_CYCLEENDTIME_LID_OPEN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.cycleEndTime_lid_open 

            elif parts[2] == "unprocessed":
                if parts[3] == 'mass':
                    results["TCLink"] = TSLink.O2_BAT_D_UNPROCESSED_MASS_ZERO
                    results["Suite"] = Suites.BAT_D_UNPROCESSED_MASS_ZERO_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.unprocessed_mass_zero 

            elif parts[2] == "lip":
                if parts[3] == 'skipped':
                    results["TCLink"] = TSLink.O2_BAT_D_LIP_SKIPPED_HOT
                    results["Suite"] = Suites.BAT_D_LIP_SKIPPED_HOT_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.lip_skipped_hot 

            elif parts[2] == "delta":
                if parts[3] == 'mr':
                    results["TCLink"] = TSLink.O2_BAT_DELTA_MR_HIP_MASS_BUCKET
                    results["Suite"] = Suites.BAT_DELTA_MR_HIP_MASS_BUCKET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.dgo_hip_mass_bucket


            elif parts[2] == "vacation":
                if parts[3] == 'clean':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_CLEAN_MODE
                    results["Suite"] = Suites.BAT_VACATION_CLEAN_MODE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_clean_mode    
                elif parts[3] == 'eco':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_ECO_MODE
                    results["Suite"] = Suites.BAT_VACATION_ECO_MODE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_eco_mode    
                elif parts[3] == 'add':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_ADD_MASS_COOLDOWN
                    results["Suite"] = Suites.BAT_VACATION_ADD_MASS_COOLDOWN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_add_mass_cooldown    
                elif parts[3] == 'reset':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_RESET
                    results["Suite"] = Suites.BAT_VACATION_RESET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_reset    

                elif parts[3] == 'after':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_AFTER_EMPTY
                    results["Suite"] = Suites.BAT_VACATION_AFTER_EMPTY_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_after_empty  


                elif parts[3] == 'ota' and parts[4] == 'pre':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_OTA_PRE
                    results["Suite"] = Suites.BAT_VACATION_OTA_PRE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_vacation_ota_pre  

                elif parts[3] == 'ota' and parts[4] == 'post':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_OTA_POST
                    results["Suite"] = Suites.BAT_VACATION_OTA_POST_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_vacation_ota_post  





            elif parts[2] == "grinder":
                if parts[3] == 'soft':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_SOFT_STALL_RETRY
                    results["Suite"] = Suites.BAT_D_GRINDER_SOFT_STALL_RETRY_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_soft_stall_retry    
                elif parts[3] == 'state':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_STATE_LID
                    results["Suite"] = Suites.BAT_D_GRINDER_STATE_LID_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_state_lid    
                elif parts[3] == 'high':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_HIGH_TEMP_JAM
                    results["Suite"] = Suites.BAT_D_GRINDER_HIGH_TEMP_JAM_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_high_temp_jam    
                elif parts[3] == 'jam':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_JAM_AUTO_RETRY
                    results["Suite"] = Suites.BAT_D_GRINDER_JAM_AUTO_RETRY_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_jam_auto_retry    

            elif parts[2] == "always":
                if parts[3] == 'locked':
                    results["TCLink"] = TSLink.O2_BAT_D_ALWAYS_LOCKED
                    results["Suite"] = Suites.BAT_D_ALWAYS_LOCKED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.always_locked   
                elif parts[3] == 'unlocked':
                    results["TCLink"] = TSLink.O2_BAT_D_ALWAYS_UNLOCKED
                    results["Suite"] = Suites.BAT_D_ALWAYS_UNLOCKED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.always_unlocked   

            elif parts[2] == "mass":
                if parts[3] == 'no':
                    results["TCLink"] = TSLink.O2_BAT_D_MASS_NO_CHANGE_RESET
                    results["Suite"] = Suites.BAT_D_MASS_NO_CHANGE_RESET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.mass_no_change_reset   
                elif parts[3] == 'add':
                    results["TCLink"] = TSLink.O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE
                    results["Suite"] = Suites.BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.mass_add_lid_open_close   



            # 8/12/2024

            elif parts[2] == "hip":
                if parts[3] == 'extension':
                    results["TCLink"] = TSLink.O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE
                    results["Suite"] = Suites.BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.hip_extension_lid_open_close   

            elif parts[2] == "start":
                if parts[3] == 'disconnected':
                    results["TCLink"] = TSLink.O2_BAT_START_DISCONNECTED
                    results["Suite"] = Suites.BAT_START_DISCONNECTED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.start_disconnected   



            else:
                print("Invalid Inputs for bat!")


        elif parts[1] == TestParts.smoke:
            if parts[2] == TestParts.pairing: 
                results["TestType"] = None
                results["Tbl"] = DBT.SMOKE_TEST_TABLE
                results["Suite"] = Suites.SMOKE_PAIRING_TEST
                results["Type"] = smokeType.pairing
                results["TCLink"] = TSLink.O2_SMOKE_PAIRING
            elif parts[2] == TestParts.dgo and parts[3] == 'inactive': 
                results["TestType"] = None
                results["Tbl"] = DBT.SMOKE_TEST_TABLE
                results["Suite"] = Suites.SMOKE_DGO_INACTIVE_TEST
                results["Type"] = smokeType.dgo_inactive
                results["TCLink"] = TSLink.O2_SMOKE_DGO_INACTIVE
            elif parts[2] == 'test' and parts[3] == 'lid': 
                results["TestType"] = None
                results["Tbl"] = DBT.SMOKE_TEST_TABLE
                results["Suite"] = Suites.SMOKE_TEST_LID_TEST
                results["Type"] = smokeType.test_lid
                results["TCLink"] = TSLink.O2_SMOKE_TEST_LID
            else:
                print("Invalid Inputs for smoke!")

        else:
            print("Invalid Inputs!")

        return results

    def mockingResults(self, vFile, vBuild, vSVR, vSN, vRunr):
        fileName = self.extractFilename(vFile)
        parts = fileName.split('_')
        results = {}

        results["Oscar"] = parts[0]
        results["ThingSN"] = vSN
        results["ThingGroup"] = ""
        results["Server"] =  vSVR

        results["RLink"] = ''
        results["DebugLink"] = ''
        results["Notes"] = self.queryNotes(parts[0], vBuild)

        results["ReportId"] = self.queryFKeyReportT(parts[0], vBuild)
        results["SvrId"] = self.queryFKeyServerT(vSVR, vRunr)
        results["DevId"] = self.queryFKeyDeviceT(vSN)

        if False:
            jiras = self.queryJira(parts[0], vBuild)
            results["Jira1"] = jiras[0][0]
            results["Jira2"] = jiras[0][1]
            results["Jira3"] = jiras[0][2]
            blockerF = self.queryBlocker(parts[0], vBuild)
            results["JiraF1"] = str(blockerF[0][1]).lower()
            results["JiraF2"] = str(blockerF[0][3]).lower()
            results["JiraF3"] = str(blockerF[0][5]).lower()
        else:
            results["Jira1"] = ''
            results["Jira2"] = ''
            results["Jira3"] = ''
            results["JiraF1"] = 'false'
            results["JiraF2"] = 'false'
            results["JiraF3"] = 'false'  

        if parts[1] == TestMGrp.ota:
            results["Build"] = vBuild
            results = self.fillStaticResultsOTA(parts, results)

            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0

            results["MinT"] = 0
            results["MaxT"] = 0
            results["AvgT"] = 0
            results["failedNum"] = 0
            results["repPass"] = 0

        elif parts[1] == 'safety':
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["TestExecuted"] = 42
            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TCLink"] = TSLink.O2_SAFETY
            results["Tbl"] = DBT.SAFETY_TEST_TABLE
            results["Suite"] = Suites.SAFETY_TEST
            results["TestType"] = ''

        elif parts[1] == TestMGrp.dgo:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TestType"] = ''

            if parts[2] == stagesN.idle:
                results["TestType"] = 'idle'
                if parts[3] == TestParts.op:
                    results["TestExecuted"] = 26
                    results["TCLink"] = TSLink.O2_DGO_OP_IDLE
                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_IDLE_OP_PR
                elif parts[3] == TestParts.mass:
                    results["TestExecuted"] = 15
                    results["TCLink"] = TSLink.O2_DGO_MASS_IDLE
                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_IDLE_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])   

            elif parts[2] == stagesN.lip:
                results["TestType"] = 'lip'
                if parts[3] == TestParts.op:
                    results["TestExecuted"] = 28
                    results["TCLink"] = TSLink.O2_DGO_OP_LIP
                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_LIP_OP_PR
                elif parts[3] == TestParts.mass:
                    results["TestExecuted"] = 15
                    results["TCLink"] = TSLink.O2_DGO_MASS_LIP
                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_LIP_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])    

            elif parts[2] == stagesN.hip:
                results["TestType"] = TestParts.hip
                if parts[3] == TestParts.op:
                    results["TestExecuted"] = 28
                    results["TCLink"] = TSLink.O2_DGO_OP_HIP
                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_HIP_OP_PR
                elif parts[3] == TestParts.mass:
                    results["TestExecuted"] = 15
                    results["TCLink"] = TSLink.O2_DGO_MASS_HIP
                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_HIP_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])    

            elif parts[2] == stagesN.cooldown:
                results["TestType"] = 'cooldown'
                if parts[3] == TestParts.op:
                    results["TestExecuted"] = 28
                    results["TCLink"] = TSLink.O2_DGO_OP_COOLDOWN
                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_COOLDOWN_OP_PR
                elif parts[3] == TestParts.mass:
                    results["TestExecuted"] = 15
                    results["TCLink"] = TSLink.O2_DGO_MASS_COOLDOWN
                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_COOLDOWN_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])    

            elif parts[2] == stagesN.fluff:
                results["TestType"] = 'fluff'
                if parts[3] == TestParts.op:
                    results["TestExecuted"] = 28
                    results["TCLink"] = TSLink.O2_DGO_OP_FLUFF
                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_FLUFF_OP_PR
                elif parts[3] == TestParts.mass:
                    results["TestExecuted"] = 15
                    results["TCLink"] = TSLink.O2_DGO_MASS_FLUFF
                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_FLUFF_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])     

        elif parts[1] == TestParts.child:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TestType"] = ''

            if parts[3] == TestParts.A:
                results["TestType"] = TestMGrp.stress
                if parts[0] == OscarType.O1:
                    results["TestExecuted"] = 19
                    results["TCLink"] = TSLink.O1_CHILDA
                elif parts[0] == OscarType.O2:
                    results["TestExecuted"] = 19
                    results["TCLink"] = TSLink.O2_CHILDA
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.CHILD_LOCK_TABLE          
                results["Suite"] = Suites.CHILD_LOCK_STRESS_TEST
            elif parts[3] == TestParts.B:    
                results["TestType"] = TestMGrp.normal
                if parts[0] == OscarType.O1:
                    results["TestExecuted"] = 89
                    results["TCLink"] = TSLink.O1_CHILDB
                elif parts[0] == OscarType.O2:
                    results["TestExecuted"] = 91
                    results["TCLink"] = TSLink.O2_CHILDB
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.CHILD_LOCK_TABLE   
                results["Suite"] = Suites.CHILD_LOCK_TEST
            else:
                print(pattern.invalidtype, parts[2])

        elif parts[1] == TestParts.start:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TestType"] = ''

            if parts[4] == TestParts.A:
                results["TestType"] = TestMGrp.stress
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_STARTA
                    results["TestExecuted"] = 19
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_STARTA
                    results["TestExecuted"] = 36
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.START_VIA_BIN_TABLE   
                results["Suite"] = Suites.START_VIA_BIN_STRESS_A    
            elif parts[4] == TestParts.B:    
                results["TestType"] = TestMGrp.normal
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_STARTB
                    results["TestExecuted"] = 21
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_STARTB
                    results["TestExecuted"] = 46
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.START_VIA_BIN_TABLE     
                results["Suite"] = Suites.START_VIA_BIN_B
            else:
                print(pattern.invalidtype, parts[4])

        elif parts[1] == TestParts.pairing:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["TestExecuted"] = 104
            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TCLink"] = TSLink.O2_PAIRING
            results["Tbl"] = DBT.PAIRING_WITHOUT_BLE_TABLE
            results["Suite"] = Suites.PAIRING_WITHOUT_BLE
            results["TestType"] = ''

        elif parts[1] == TestParts.boot:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["TestExecuted"] = 17
            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TCLink"] = TSLink.O2_BOOTA
            results["Tbl"] = DBT.BOOT_CYCLE_TABLE
            results["Suite"] = Suites.BOOT_CYCLE_TEST
            results["TestType"] = TestMGrp.stress

        elif parts[1] == TestParts.eeprom:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["TestExecuted"] = 8
            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            results["TCLink"] = TSLink.EEPROM
            results["Tbl"] = DBT.EEPROM_STRESS_TEST_TABLE
            results["Suite"] = Suites.EEPROM_STRESS_TEST
            results["TestType"] = ''

        elif parts[1] == TestParts.smoke:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0
            if parts[2] == TestParts.pairing:
                results["TestType"] = None
                results["Tbl"] = DBT.SMOKE_TEST_TABLE
                results["Suite"] = Suites.SMOKE_PAIRING_TEST
                results["Type"] = smokeType.pairing
                results["TCLink"] = TSLink.O2_SMOKE_PAIRING
                results["TestExecuted"] = 11
            elif parts[2] == TestParts.dgo and parts[3] == 'inactive': 
                results["TestType"] = None
                results["Tbl"] = DBT.SMOKE_TEST_TABLE
                results["Suite"] = Suites.SMOKE_DGO_INACTIVE_TEST
                results["Type"] = smokeType.dgo_inactive
                results["TCLink"] = TSLink.O2_SMOKE_DGO_INACTIVE
                results["TestExecuted"] = 8
            elif parts[2] == 'test' and parts[3] == 'lid': 
                results["TestType"] = None
                results["Tbl"] = DBT.SMOKE_TEST_TABLE
                results["Suite"] = Suites.SMOKE_TEST_LID_TEST
                results["Type"] = smokeType.test_lid
                results["TCLink"] = TSLink.O2_SMOKE_TEST_LID
                results["TestExecuted"] = 18
            else:
                print("Invalid Inputs for smoke!")

        elif parts[1] == TestParts.bat:
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["TestType"] = ''
            results["Tbl"] = DBT.BAT_TABLE   
            results["Stage"] = ''
            results["Passed"] = 0
            results["Failed"] = 0
            results["ExeTime"] = 0
            results["Repeats"] = 0

            if parts[2] == TestParts.dgo:
                if parts[3] == TestParts.add and parts[4] == TestParts.mass:
                    results["TCLink"] = TSLink.O2_BAT_D_A_M_H
                    results["Suite"] = Suites.BAT_D_A_M_H_TEST
                    results["Stage"] = TestParts.hip
                    results["Type"] = batType.add_mass_hip
                    results["TestExecuted"] = 9
                elif parts[3] == 'reset' and parts[4] == TestParts.hip:
                    results["TCLink"] = TSLink.O2_BAT_D_R_H
                    results["Suite"] = Suites.BAT_D_R_H_TEST
                    results["Stage"] = TestParts.hip
                    results["Type"] = batType.reset_hip
                    results["TestExecuted"] = 9
                elif parts[3] == 'start' and parts[4] == TestParts.stop:
                    results["TCLink"] = TSLink.O2_BAT_D_S_S_N_V
                    results["Suite"] = Suites.BAT_D_S_S_N_V_TEST
                    results["Type"] = batType.start_stop_no_vacation
                    results["TestExecuted"] = 8
                elif parts[3] == 'sht40':
                    if parts[4] == 'calibration':
                        results["TCLink"] = TSLink.O2_BAT_S_C
                        results["Suite"] = Suites.BAT_S_C_TEST
                        results["Type"] = batType.sht40_calibration
                        results["TestExecuted"] = 7
                    elif parts[4] == 'cal' and parts[5] == 'skip':
                        results["TCLink"] = TSLink.O2_BAT_D_S_C_S_W_H
                        results["Suite"] = Suites.BAT_D_S_C_S_W_H_TEST
                        results["Type"] = batType.sht40_cal_skip_when_hot
                        results["TestExecuted"] = 9
                elif parts[3] == 'jam':
                    if parts[4] == 'error':
                        results["TCLink"] = TSLink.O2_BAT_D_J_E
                        results["Suite"] = Suites.BAT_D_J_E_TEST
                        results["Type"] = batType.jam_error
                        results["TestExecuted"] = 9
                    elif parts[4] == 'inactive':
                        results["TCLink"] = TSLink.O2_BAT_D_J_I
                        results["Suite"] = Suites.BAT_D_J_I_TEST
                        results["Type"] = batType.empty_bucket
                        results["TestExecuted"] = 9
                elif parts[3] == TestParts.hip and parts[4] == 'moisture':
                    results["TCLink"] = TSLink.O2_BAT_D_H_M_F_A
                    results["Suite"] = Suites.BAT_D_H_M_F_A_TEST
                    results["Stage"] = TestParts.hip
                    results["Type"] = batType.hip_moisture_food_add
                    results["TestExecuted"] = 10
                elif parts[3] == 'heat':
                    results["TCLink"] = TSLink.O2_BAT_D_H_W_S
                    results["Suite"] = Suites.BAT_D_H_W_S_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.heat_warning_status
                    results["TestExecuted"] = 8
                elif parts[3] == 'empty' and parts[4] == 'bucket':
                    results["TCLink"] = TSLink.O2_BAT_D_E_B
                    results["Suite"] = Suites.BAT_D_E_B_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.empty_bucket
                    results["TestExecuted"] = 9

            elif parts[2] == "cooldown":
                if parts[3] == 'temp':
                    results["TCLink"] = TSLink.O2_BAT_COOLDOWN_TEMP
                    results["Suite"] = Suites.BAT_COOLDOWN_TEMP_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.cooldown_temp   
                    results["TestExecuted"] = 11               
            elif parts[2] == "heat":

                if parts[3] == 'led' and parts[4] == 'interruptions':
                    results["TCLink"] = TSLink.O2_BAT_HEAT_LED_INTERRUPTIONS
                    results["Suite"] = Suites.BAT_HEAT_LED_INTERRUPTIONS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.heat_led_interruptions 
                    results["TestExecuted"] = 18
                elif parts[3] == 'led':   
                    results["TCLink"] = TSLink.O2_BAT_HEAT_LED
                    results["Suite"] = Suites.BAT_HEAT_LED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.heat_led   
                    results["TestExecuted"] = 22



            elif parts[2] == "premature":
                if parts[3] == TestParts.mass:
                    results["TCLink"] = TSLink.O2_BAT_PREMATURE_MASS_NO_RESET
                    results["Suite"] = Suites.BAT_PREMATURE_MASS_NO_RESET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.premature_mass_no_reset  
                    results["TestExecuted"] = 8





            #GUO_ADDED
            elif parts[2] == "locked":
                if parts[4] == 'hot' and parts[5] == 'shadows':
                    results["TCLink"] = TSLink.O2_BAT_LOCKED_WHEN_HOT_SHADOWS
                    results["Suite"] = Suites.BAT_LOCKED_WHEN_HOT_SHADOWS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.locked_when_hot_shadows 
                    results["TestExecuted"] = 11

                elif parts[3] == 'when':
                    results["TCLink"] = TSLink.O2_BAT_D_LOCKED_WHEN_RUNNING
                    results["Suite"] = Suites.BAT_D_LOCKED_WHEN_RUNNING_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.locked_when_running 
                    results["TestExecuted"] = 16

            elif parts[2] == "fluff":
                if parts[3] == 'not':
                    results["TCLink"] = TSLink.O2_BAT_D_FLUFF_NOT_RUN
                    results["Suite"] = Suites.BAT_D_FLUFF_NOT_RUN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.fluff_not_run  
                    results["TestExecuted"] = 8
            elif parts[2] == "set":
                if parts[3] == 'dgo':
                    results["TCLink"] = TSLink.O2_BAT_SET_START_TIME_DURING_HIP
                    results["Suite"] = Suites.BAT_SET_START_TIME_DURING_HIP_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.cycle_start_time_HIP  
                    results["TestExecuted"] = 11
            elif parts[2] == "resume":
                if parts[3] == 'from':
                    results["TCLink"] = TSLink.O2_BAT_RESUME_FROM_LIP
                    results["Suite"] = Suites.BAT_RESUME_FROM_LIP_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.resume_lip  
                    results["TestExecuted"] = 7

                elif parts[3] == 'disconnected':
                    results["TCLink"] = TSLink.O2_BAT_RESUME_DISCONNECTED
                    results["Suite"] = Suites.BAT_RESUME_DISCONNECTED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.resume_disconnected  
                    results["TestExecuted"] = 13  
                elif parts[3] == 'cooldown':
                    results["TCLink"] = TSLink.O2_BAT_RESUME_COOLDOWN
                    results["Suite"] = Suites.BAT_RESUME_COOLDOWN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.resume_cooldown    
                    results["TestExecuted"] = 22

            elif parts[2] == "bucket":
                if parts[3] == 'fullness':
                    results["TCLink"] = TSLink.O2_BAT_D_BUCKET_FULLNESS_LOW
                    results["Suite"] = Suites.BAT_D_BUCKET_FULLNESS_LOW_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bucket_fullness_low  
                    results["TestExecuted"] = 4


                elif parts[3] == 'crash' and parts[4] == 'ota' and parts[5] == 'pre':
                    results["TCLink"] = TSLink.O2_BAT_BUCKET_CRASH_OTA_PRE
                    results["Suite"] = Suites.BAT_BUCKET_CRASH_OTA_PRE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_bucket_crash_ota_pre    
                    results["TestExecuted"] = 99

                elif parts[3] == 'crash' and parts[4] == 'ota' and parts[5] == 'post':
                    results["TCLink"] = TSLink.O2_BAT_BUCKET_CRASH_OTA_POST
                    results["Suite"] = Suites.BAT_BUCKET_CRASH_OTA_POST_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_bucket_crash_ota_post    
                    results["TestExecuted"] = 99


            elif parts[2] == "fr":
                if parts[3] == 'heat':
                    results["TCLink"] = TSLink.O2_BAT_D_FR_HEAT_WARNING_STATUS
                    results["Suite"] = Suites.BAT_D_FR_HEAT_WARNING_STATUS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.fr_heat_warning_status  
                    results["TestExecuted"] = 17
            elif parts[2] == "lastDgoCycle":
                if parts[3] == 'energy':
                    results["TCLink"] = TSLink.O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS
                    results["Suite"] = Suites.BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.lastDgoCycle_energy_shadows 
                    results["TestExecuted"] = 14

            elif parts[2] == "cycleEndTime":
                if parts[3] == 'lid':
                    results["TCLink"] = TSLink.O2_BAT_D_CYCLEENDTIME_LID_OPEN
                    results["Suite"] = Suites.BAT_D_CYCLEENDTIME_LID_OPEN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.cycleEndTime_lid_open 
                    results["TestExecuted"] = 9
            elif parts[2] == "unprocessed":
                if parts[3] == 'mass':
                    results["TCLink"] = TSLink.O2_BAT_D_UNPROCESSED_MASS_ZERO
                    results["Suite"] = Suites.BAT_D_UNPROCESSED_MASS_ZERO_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.unprocessed_mass_zero 
                    results["TestExecuted"] = 13
            elif parts[2] == "lip":
                if parts[3] == 'skipped':
                    results["TCLink"] = TSLink.O2_BAT_D_LIP_SKIPPED_HOT
                    results["Suite"] = Suites.BAT_D_LIP_SKIPPED_HOT_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.lip_skipped_hot 
                    results["TestExecuted"] = 14
            elif parts[2] == "delta":
                if parts[3] == 'mr':
                    results["TCLink"] = TSLink.O2_BAT_DELTA_MR_HIP_MASS_BUCKET
                    results["Suite"] = Suites.BAT_DELTA_MR_HIP_MASS_BUCKET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.dgo_hip_mass_bucket
                    results["TestExecuted"] = 13

            elif parts[2] == "vacation":
                if parts[3] == 'clean':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_CLEAN_MODE
                    results["Suite"] = Suites.BAT_VACATION_CLEAN_MODE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_clean_mode    
                    results["TestExecuted"] = 8
                elif parts[3] == 'eco':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_ECO_MODE
                    results["Suite"] = Suites.BAT_VACATION_ECO_MODE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_eco_mode    
                    results["TestExecuted"] = 8
                elif parts[3] == 'add':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_ADD_MASS_COOLDOWN
                    results["Suite"] = Suites.BAT_VACATION_ADD_MASS_COOLDOWN_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_add_mass_cooldown    
                    results["TestExecuted"] = 13
                elif parts[3] == 'reset':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_RESET
                    results["Suite"] = Suites.BAT_VACATION_RESET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_reset    
                    results["TestExecuted"] = 13

                elif parts[3] == 'after':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_AFTER_EMPTY
                    results["Suite"] = Suites.BAT_VACATION_AFTER_EMPTY_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.vacation_after_empty  
                    results["TestExecuted"] = 6


                elif parts[3] == 'ota' and parts[4] == 'pre':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_OTA_PRE
                    results["Suite"] = Suites.BAT_VACATION_OTA_PRE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_vacation_ota_pre  
                    results["TestExecuted"] = 10

                elif parts[3] == 'ota' and parts[4] == 'post':
                    results["TCLink"] = TSLink.O2_BAT_VACATION_OTA_POST
                    results["Suite"] = Suites.BAT_VACATION_OTA_POST_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.bat_vacation_ota_post  
                    results["TestExecuted"] = 2



            elif parts[2] == "grinder":
                if parts[3] == 'soft':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_SOFT_STALL_RETRY
                    results["Suite"] = Suites.BAT_D_GRINDER_SOFT_STALL_RETRY_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_soft_stall_retry    
                    results["TestExecuted"] = 11
                elif parts[3] == 'state':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_STATE_LID
                    results["Suite"] = Suites.BAT_D_GRINDER_STATE_LID_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_state_lid    
                    results["TestExecuted"] = 9
                elif parts[3] == 'high':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_HIGH_TEMP_JAM
                    results["Suite"] = Suites.BAT_D_GRINDER_HIGH_TEMP_JAM_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_high_temp_jam    
                    results["TestExecuted"] = 14
                elif parts[3] == 'jam':
                    results["TCLink"] = TSLink.O2_BAT_D_GRINDER_JAM_AUTO_RETRY
                    results["Suite"] = Suites.BAT_D_GRINDER_JAM_AUTO_RETRY_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.grinder_jam_auto_retry    
                    results["TestExecuted"] = 11

            elif parts[2] == "always":
                if parts[3] == 'locked':
                    results["TCLink"] = TSLink.O2_BAT_D_ALWAYS_LOCKED
                    results["Suite"] = Suites.BAT_D_ALWAYS_LOCKED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.always_locked   
                    results["TestExecuted"] = 10                  
                elif parts[3] == 'unlocked':
                    results["TCLink"] = TSLink.O2_BAT_D_ALWAYS_UNLOCKED
                    results["Suite"] = Suites.BAT_D_ALWAYS_UNLOCKED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.always_unlocked   
                    results["TestExecuted"] = 15
            elif parts[2] == "mass":
                if parts[3] == 'no':
                    results["TCLink"] = TSLink.O2_BAT_D_MASS_NO_CHANGE_RESET
                    results["Suite"] = Suites.BAT_D_MASS_NO_CHANGE_RESET_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.mass_no_change_reset   
                    results["TestExecuted"] = 9                  
                elif parts[3] == 'add':
                    results["TCLink"] = TSLink.O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE
                    results["Suite"] = Suites.BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.mass_add_lid_open_close   
                    results["TestExecuted"] = 9

            # 8/12/2024

            elif parts[2] == "hip":
                if parts[3] == 'extension':
                    results["TCLink"] = TSLink.O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE
                    results["Suite"] = Suites.BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.hip_extension_lid_open_close   
                    results["TestExecuted"] = 18
            elif parts[2] == "start":
                if parts[3] == 'disconnected':
                    results["TCLink"] = TSLink.O2_BAT_START_DISCONNECTED
                    results["Suite"] = Suites.BAT_START_DISCONNECTED_TEST
                    results["Stage"] = ''
                    results["Type"] = batType.start_disconnected   
                    results["TestExecuted"] = 13


            else:
                print("Invalid Inputs for bat!")

        else:
            print(pattern.invalidtestsuite)
            results = None

        return results

    def getDGOPassedFailed(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith(pattern.runcount):
                    self.dgo_run_count += 1
                elif line.startswith(startwith.passed):
                    self.dgo_passed += 1
                elif line.startswith(startwith.failed):
                    self.dgo_failed += 1
                elif "in" in line and pattern.quote_open in line and pattern.quote_close in line:
                    time_str = line.split("in")[1].split("s")[0].strip()
                    self.dgo_total_time += float(time_str)

        return self.dgo_passed, self.dgo_failed    

    def getRepeatedCount(self):
        return self.dgo_run_count

    def getTotalTime(self):
        return self.dgo_total_time 
    
    def getPassedFailed(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith(pattern.runcount):
                    self.dgo_run_count += 1
                elif line.startswith(startwith.passed):
                    self.dgo_passed += 1
                elif line.startswith(startwith.failed):
                    self.dgo_failed += 1
                elif "in" in line and pattern.quote_open in line and pattern.quote_close in line:
                    time_str = line.split(" in ")[1].split("s")[0].strip()
                    self.dgo_total_time += float(time_str)
                elif "in" in line and pattern.sline in line:
                    time_match = re.search(r"in (\d+\.?\d*)s", line)
                    if time_match:
                        self.dgo_total_time += float(time_match.group(1))

        return self.dgo_passed, self.dgo_failed    

    def is_file_empty(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return len(content) == 0
        except IOError:
            print(f"Error: File {file_path} not accessible.")
            return False  

    def ChildLockParts(self, parts, results):
        if parts[1] == TestParts.child:
            if parts[3] == TestParts.A:
                results["TestType"] = TestMGrp.stress
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_CHILDA
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_CHILDA
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.CHILD_LOCK_TABLE          
                results["Suite"] = Suites.CHILD_LOCK_STRESS_TEST
            elif parts[3] == TestParts.B:    
                results["TestType"] = TestMGrp.normal
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_CHILDB
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_CHILDB
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.CHILD_LOCK_TABLE   
                results["Suite"] = Suites.CHILD_LOCK_TEST
            else:
                print(pattern.invalidtype, parts[3])
        else:
            print(pattern.invalidparts)

    def DGOParts(self, parts, results):
        if parts[1] == TestMGrp.dgo:
            if parts[2] == stagesN.idle:
                results["TestType"] = stagesN.idle
                if parts[3] == TestParts.op:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_OP_IDLE
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_OP_IDLE
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_IDLE_OP_PR
                elif parts[3] == TestParts.mass:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_MASS_IDLE
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_MASS_IDLE
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_IDLE_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])

            elif parts[2] == stagesN.lip:
                results["TestType"] = stagesN.lip
                if parts[3] == TestParts.op:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_OP_LIP
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_OP_LIP
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_LIP_OP_PR
                elif parts[3] == TestParts.mass:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_MASS_LIP
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_MASS_LIP
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_LIP_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])

            elif parts[2] == stagesN.hip:
                results["TestType"] = stagesN.hip
                if parts[3] == TestParts.op:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_OP_HIP
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_OP_HIP
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_HIP_OP_PR
                elif parts[3] == TestParts.mass:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_MASS_HIP
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_MASS_HIP
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_HIP_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])

            elif parts[2] == stagesN.cooldown:
                results["TestType"] = stagesN.cooldown
                if parts[3] == TestParts.op:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_OP_COOLDOWN
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_OP_COOLDOWN
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_COOLDOWN_OP_PR
                elif parts[3] == TestParts.mass:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_MASS_COOLDOWN
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_MASS_COOLDOWN
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_COOLDOWN_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])

            elif parts[2] == stagesN.fluff:
                results["TestType"] = stagesN.fluff
                if parts[3] == TestParts.op:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_OP_FLUFF
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_OP_FLUFF
                    else:
                        print(pattern.invalidoscartype)
                
                    results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    results["Suite"] = Suites.DGO_FLUFF_OP_PR
                elif parts[3] == TestParts.mass:
                    if parts[0] == OscarType.O1:
                        results["TCLink"] = TSLink.O1_DGO_MASS_FLUFF
                    elif parts[0] == OscarType.O2:
                        results["TCLink"] = TSLink.O2_DGO_MASS_FLUFF
                    else:
                        print(pattern.invalidoscartype)

                    results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    results["Suite"] = Suites.DGO_FLUFF_ADD_MASS
                else:
                    print(pattern.invalidtype, parts[3])
            else:
                print(pattern.invalidtype, parts[2])
        else:
            print(pattern.invalidparts)

    def StartViaBinParts(self, parts, results):
        if parts[1] == 'start':
            if parts[4] == TestParts.A:
                results["TestType"] = TestMGrp.stress
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_STARTA
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_STARTA
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.START_VIA_BIN_TABLE   
                results["Suite"] = Suites.START_VIA_BIN_STRESS_A    
            elif parts[4] == TestParts.B:    
                results["TestType"] = TestMGrp.normal
                if parts[0] == OscarType.O1:
                    results["TCLink"] = TSLink.O1_STARTB
                elif parts[0] == OscarType.O2:
                    results["TCLink"] = TSLink.O2_STARTB
                else:
                    print(pattern.invalidoscartype)

                results["Tbl"] = DBT.START_VIA_BIN_TABLE     
                results["Suite"] = Suites.START_VIA_BIN_B
            else:
                print(pattern.invalidtype, parts[4])
        else:
            print(pattern.invalidparts)

    def ProcessOTA(self, vFile, vBuild, vSVR, vSN, vRunr):
        fileName = self.extractFilename(vFile)
        parts = fileName.split('_')

        if parts[1] == TestMGrp.ota:

            if self.is_file_empty(vFile):
                results = self.mockingResults(vFile, vBuild, vSVR, vSN, vRunr)
                return results, vFile 

            self.parseOTAFile(vFile)
            total_runs, total_sub_runs = self.calculateRunTotals()
            total_duration_seconds = self.calculateDuration()
            tests_passed = self.getPassed()
            tests_failed = self.getFailed()
            min_duration_seconds = self.getMin()
            max_duration_seconds = self.getMax()
            average_duration_seconds = self.getAvg()
            sn = self.getSerialNum()
            thingGrp = self.getThingGrp()


            # print("tests_passed= ", tests_passed)
            # print("tests_failed= ", tests_failed)

            results = {}
            results["Build"] = vBuild
            results["Oscar"] = parts[0]
            results["ThingSN"] = sn
            results["ThingGroup"] = thingGrp
            results["Server"] =  vSVR
            results["TestExecuted"] = (tests_passed + tests_failed) // total_runs // 2

            if parts[2] == otaType.power:
                results["Passed"] = tests_passed // 2
                results["Repeats"] = total_runs // total_sub_runs
            else:
                results["Passed"] = tests_passed // total_runs // 2
                results["Repeats"] = total_runs


            results["Failed"] = tests_failed
            results["ExeTime"] = self.estimate_hours(int(average_duration_seconds * total_sub_runs))
        
            results["MinT"] = min_duration_seconds
            results["MaxT"] = max_duration_seconds
            results["AvgT"] = average_duration_seconds

            results = self.fillStaticResultsOTA(parts, results)
            #print("results= ", results)

            results["RLink"] = './' + self.extract_filename(vFile)
            results["DebugLink"] = ''
            results["Notes"] = self.queryNotes(parts[0], vBuild)

            results["ReportId"] = self.queryFKeyReportT(parts[0], vBuild)
            results["SvrId"] = self.queryFKeyServerT(vSVR, vRunr)
            results["DevId"] = self.queryFKeyDeviceT(vSN)

            if False:
                jiras = self.queryJira(parts[0], vBuild)
                results["Jira1"] = jiras[0][0]
                results["Jira2"] = jiras[0][1]
                results["Jira3"] = jiras[0][2]
                blockerF = self.queryBlocker(parts[0], vBuild)
                results["JiraF1"] = str(blockerF[0][1]).lower()
                results["JiraF2"] = str(blockerF[0][3]).lower()
                results["JiraF3"] = str(blockerF[0][5]).lower()
            else:
                results["Jira1"] = ''
                results["Jira2"] = ''
                results["Jira3"] = ''
                results["JiraF1"] = 'false'
                results["JiraF2"] = 'false'
                results["JiraF3"] = 'false' 

            results["failedNum"] = self.fetchFailedNum(sn, thingGrp)
            results["repPass"] = self.fetchRetryPassNum(sn, thingGrp)
            return results, vFile
        else:
            return None, vFile

    def ProcessDGO(self, vFile, vBuild, vSVR, vSN, vRunr):
        fileName = self.extractFilename(vFile)
        parts = fileName.split('_')

        if parts[1] == TestMGrp.dgo or parts[1] == TestParts.eeprom or parts[1] == TestParts.pairing or parts[1] == TestParts.start \
                or parts[1] == TestParts.child or parts[1] == TestParts.lid or parts[1] == TestParts.safety \
                or parts[1] == TestParts.boot or parts[1] == TestParts.bat or parts[1] == TestParts.smoke:
        
            if self.is_file_empty(vFile):
                results = self.mockingResults(vFile, vBuild, vSVR, vSN, vRunr)
                return results, vFile 

            passed, failed = self.getPassedFailed(vFile)
            runs = self.getRepeatedCount()
            totalT = self.getTotalTime()

            results = {}
            if vBuild.startswith(startwith.rls):
                results["Build"] = self.convert_version(vBuild)
            else:
                results["Build"] = vBuild

            results["Oscar"] = parts[0]
            results["ThingSN"] = vSN
            results["ThingGroup"] = ""
            results["Server"] =  vSVR
            results["TestExecuted"] = (passed // runs) + (failed // runs)
            results["Passed"] = passed // runs
            results["Failed"] = failed // runs
            results["ExeTime"] = self.estimate_hours(int(totalT))
            results["Repeats"] = runs

            results = self.fillStaticResultsDGO(parts, results)

            results["RLink"] = './' + self.extract_filename(vFile)
            results["DebugLink"] = ''
            results["Notes"] = self.queryNotes(parts[0], vBuild)
            results["ReportId"] = self.queryFKeyReportT(parts[0], vBuild)
            results["SvrId"] = self.queryFKeyServerT(vSVR, vRunr)
            results["DevId"] = self.queryFKeyDeviceT(vSN)

            if False:
                jiras = self.queryJira(parts[0], vBuild)
                results["Jira1"] = jiras[0][0]
                results["Jira2"] = jiras[0][1]
                results["Jira3"] = jiras[0][2]
                blockerF = self.queryBlocker(parts[0], vBuild)
                results["JiraF1"] = str(blockerF[0][1]).lower()
                results["JiraF2"] = str(blockerF[0][3]).lower()
                results["JiraF3"] = str(blockerF[0][5]).lower()
            else:
                results["Jira1"] = ''
                results["Jira2"] = ''
                results["Jira3"] = ''
                results["JiraF1"] = 'false'
                results["JiraF2"] = 'false'
                results["JiraF3"] = 'false'

            return results, vFile
        else:
            return None, vFile

    def toTmpl(self, vBuild):
        firstIndex = vBuild.find('.')
        prefix = vBuild[:firstIndex]
        verSuffix = vBuild[firstIndex:].replace('.', '_')
        return prefix + verSuffix

    def verify_specific_version_exists(self, folder_path, version, oscar):
        existing_files = os.listdir(folder_path)
        missing_files = []

        if oscar == OscarType.O1:
            patterns = LogFiles.O1_patterns 
        else:
            patterns = LogFiles.O2_patterns

        for pattern in patterns:
            expected_filename = pattern.format(version=version)
            if expected_filename not in existing_files:
                missing_files.append(expected_filename)

        if missing_files:
            print("Missing files:")
            for file in missing_files:
                print(f"  - {file}")
        else:
            print(pattern.allversionfiles)

    def generate_insert_query(self, results, vFile, vBuild, dbF=True):
        if results == None:
            return

        insert_q = None
        data = None
        if dbF:
            if results["Suite"] == Suites.OTA_SELF or results["Suite"] == Suites.OTA_PROD_UPGRADE or \
               results["Suite"] == Suites.OTA_INT_FT_UPGRADE or results["Suite"] == Suites.OTA_EXT_FT_UPGRADE :
                insert_q = sqlsDash.insert_q_ota.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["TestType"]}',
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}', results["MinT"], 
                        results["MaxT"], results["AvgT"], results["failedNum"],
                        results["repPass"]
                        )
                
            elif results["Suite"] == Suites.POWER_DURING_OTA:
                insert_q = sqlsDash.insert_q_power.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', 
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.DGO_IDLE_OP_PR or results["Suite"] == Suites.DGO_LIP_OP_PR or \
                 results["Suite"] == Suites.DGO_HIP_OP_PR or results["Suite"] == Suites.DGO_COOLDOWN_OP_PR or \
                 results["Suite"] == Suites.DGO_FLUFF_OP_PR:
                insert_q = sqlsDash.insert_q_dgo_op.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["TestType"]}',
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.DGO_IDLE_ADD_MASS or results["Suite"] == Suites.DGO_LIP_ADD_MASS or \
                 results["Suite"] == Suites.DGO_HIP_ADD_MASS or results["Suite"] == Suites.DGO_COOLDOWN_ADD_MASS or \
                 results["Suite"] == Suites.DGO_FLUFF_ADD_MASS:
                insert_q = sqlsDash.insert_q_dgo_mass.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["TestType"]}',
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.PAIRING_WITHOUT_BLE:
                insert_q = sqlsDash.insert_q_pairing.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', 
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.EEPROM_STRESS_TEST:
                insert_q = sqlsDash.insert_q_eeprom.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', 
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.SAFETY_TEST:
                insert_q = sqlsDash.insert_q_safety.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', 
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.LID_OPEN_CLOSE:
                insert_q = sqlsDash.insert_q_lid.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', 
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.START_VIA_BIN_STRESS_A or results["Suite"] == Suites.START_VIA_BIN_B:
                insert_q = sqlsDash.insert_q_start_via_bin.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["TestType"]}',
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.CHILD_LOCK_STRESS_TEST or results["Suite"] == Suites.CHILD_LOCK_TEST:
                insert_q = sqlsDash.insert_q_child.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["TestType"]}',
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )

            elif results["Suite"] == Suites.BOOT_CYCLE_STRESS_TEST or results["Suite"] == Suites.BOOT_CYCLE_TEST:
                insert_q = sqlsDash.insert_q_boot.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["TestType"]}',
                        f'{results["Server"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )               
                
            elif results["Suite"] in [Suites.BAT_D_A_M_H_TEST, Suites.BAT_D_R_H_TEST, Suites.BAT_S_C_TEST, \
            Suites.BAT_D_S_C_S_W_H_TEST, Suites.BAT_D_S_S_N_V_TEST, Suites.BAT_D_J_E_TEST, Suites.BAT_D_J_I_TEST, \
            Suites.BAT_D_H_M_F_A_TEST, Suites.BAT_D_H_W_S_TEST, Suites.BAT_D_E_B_TEST, Suites.BAT_COOLDOWN_TEMP_TEST, \
            Suites.BAT_HEAT_LED_TEST, Suites.BAT_PREMATURE_MASS_NO_RESET_TEST, Suites.BAT_LOCKED_WHEN_HOT_SHADOWS_TEST, \
            Suites.BAT_VACATION_CLEAN_MODE_TEST, Suites.BAT_VACATION_ECO_MODE_TEST, Suites.BAT_VACATION_ADD_MASS_COOLDOWN_TEST, \
            Suites.BAT_VACATION_RESET_TEST, Suites.BAT_D_GRINDER_SOFT_STALL_RETRY_TEST, Suites.BAT_D_GRINDER_STATE_LID_TEST, \
            Suites.BAT_D_GRINDER_HIGH_TEMP_JAM_TEST, Suites.BAT_D_GRINDER_JAM_AUTO_RETRY_TEST, Suites.BAT_D_FLUFF_NOT_RUN_TEST, \
            Suites.BAT_SET_START_TIME_DURING_HIP_TEST, Suites.BAT_RESUME_FROM_LIP_TEST, Suites.BAT_D_ALWAYS_LOCKED_TEST, \
            Suites.BAT_D_ALWAYS_UNLOCKED_TEST, Suites.BAT_D_BUCKET_FULLNESS_LOW_TEST, Suites.BAT_DELTA_MR_HIP_MASS_BUCKET_TEST, \
            Suites.BAT_D_LOCKED_WHEN_RUNNING_TEST, Suites.BAT_D_FR_HEAT_WARNING_STATUS_TEST, Suites.BAT_D_MASS_NO_CHANGE_RESET_TEST, \
            Suites.BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST, Suites.BAT_D_CYCLEENDTIME_LID_OPEN_TEST, Suites.BAT_D_UNPROCESSED_MASS_ZERO_TEST, \
            Suites.BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST, Suites.BAT_D_LIP_SKIPPED_HOT_TEST, Suites.BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST, \
            Suites.BAT_START_DISCONNECTED_TEST, Suites.BAT_RESUME_DISCONNECTED_TEST, Suites.BAT_HEAT_LED_INTERRUPTIONS_TEST, \
            Suites.BAT_VACATION_AFTER_EMPTY_TEST, Suites.BAT_RESUME_COOLDOWN_TEST, Suites.BAT_VACATION_OTA_PRE_TEST, \
            Suites.BAT_VACATION_OTA_POST_TEST, Suites.BAT_BUCKET_CRASH_OTA_PRE_TEST, Suites.BAT_BUCKET_CRASH_OTA_POST_TEST ]:
                insert_q = sqlsDash.insert_q_bat.format(f'{results["Tbl"]}')
                #print("insert_q", insert_q)
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}', f'{results["Stage"]}',
                        f'{results["Server"]}', f'{results["Type"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )   
                #print("data", data)

            elif results["Suite"] in [Suites.SMOKE_PAIRING_TEST, Suites.SMOKE_TEST_LID_TEST, Suites.SMOKE_DGO_INACTIVE_TEST]:
                insert_q = sqlsDash.insert_q_smoke.format(f'{results["Tbl"]}')
                data = (f'{self.toTmpl(results["Build"])}', f'{results["Oscar"]}',
                        f'{results["Server"]}', f'{results["Type"]}', f'{results["ThingSN"]}', results["ReportId"], 
                        results['SvrId'], results['DevId'], results['TestExecuted'],
                        results["Passed"], results["Failed"], f'{results["ExeTime"]}',
                        results["Repeats"], f'{results["Jira1"]}', results["JiraF1"], 
                        f'{results["Jira2"]}', results["JiraF2"], f'{results["Jira3"]}',
                        results["JiraF3"], f'{results["RLink"]}', f'{results["TCLink"]}', 
                        f'{results["DebugLink"]}', f'{results["Notes"]}' 
                        )      
            else:
                print(pattern.invalidtestsuite)

            results["Tbl"]
            if self.insertRowData(insert_q, data):
                print(f"""insert tabele: {results["Tbl"]} ==> '{self.toTmpl(results["Build"])}' and '{results["Oscar"]}' and data successful!""")
            else:
                print(f"""insert tabele: {results["Tbl"]} ==> '{self.toTmpl(results["Build"])}' and '{results["Oscar"]}' and data failed!""")
            time.sleep(3)

            print("%%%%%%%%%%%%%% Direct Insert %%%%%%%%%%%%%%")

        else:
            table_name = ''
            value_line = ''

            #print(results)
            #print(results["Suite"])


            if results["Suite"] == Suites.OTA_SELF or results["Suite"] == Suites.OTA_PROD_UPGRADE or \
               results["Suite"] == Suites.OTA_INT_FT_UPGRADE or results["Suite"] == Suites.OTA_EXT_FT_UPGRADE :

                table_name = sqlsDash.q_table_ota
                column_name = sqlsDash.q_column_ota
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["TestType"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\', {results["MinT"]}, '
                    f'{results["MaxT"]}, {results["AvgT"]}, {results["failedNum"]}, '
                    f'{results["repPass"]})"'
                )

            elif results["Suite"] == Suites.POWER_DURING_OTA:
                table_name = sqlsDash.q_table_power
                column_name = sqlsDash.q_column_power
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.DGO_IDLE_OP_PR or results["Suite"] == Suites.DGO_LIP_OP_PR or \
                 results["Suite"] == Suites.DGO_HIP_OP_PR or results["Suite"] == Suites.DGO_COOLDOWN_OP_PR or \
                 results["Suite"] == Suites.DGO_FLUFF_OP_PR:
                table_name = sqlsDash.q_table_dgo_op
                column_name = sqlsDash.q_column_dgo_op
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["TestType"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.DGO_IDLE_ADD_MASS or results["Suite"] == Suites.DGO_LIP_ADD_MASS or \
                 results["Suite"] == Suites.DGO_HIP_ADD_MASS or results["Suite"] == Suites.DGO_COOLDOWN_ADD_MASS or \
                 results["Suite"] == Suites.DGO_FLUFF_ADD_MASS:
                table_name = sqlsDash.q_table_dgo_mass
                column_name = sqlsDash.q_column_dgo_mass
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["TestType"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.PAIRING_WITHOUT_BLE:
                table_name = sqlsDash.q_table_pairing
                column_name = sqlsDash.q_column_pairing
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.EEPROM_STRESS_TEST:
                table_name = sqlsDash.q_table_eeprom
                column_name = sqlsDash.q_column_eeprom
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.SAFETY_TEST:
                table_name = sqlsDash.q_table_safety
                column_name = sqlsDash.q_column_safety
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.LID_OPEN_CLOSE:
                table_name = sqlsDash.q_table_lid
                column_name = sqlsDash.q_column_lid
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.START_VIA_BIN_STRESS_A or results["Suite"] == Suites.START_VIA_BIN_B:
                table_name = sqlsDash.q_table_start_via_bin
                column_name = sqlsDash.q_column_start_via_bin
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["TestType"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.CHILD_LOCK_STRESS_TEST or results["Suite"] == Suites.CHILD_LOCK_TEST:
                table_name = sqlsDash.q_table_child
                column_name = sqlsDash.q_column_child
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["TestType"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] == Suites.BOOT_CYCLE_STRESS_TEST or results["Suite"] == Suites.BOOT_CYCLE_TEST:
                table_name = sqlsDash.q_table_boot
                column_name = sqlsDash.q_column_boot
                value_line = (
                    f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["TestType"]}\', '
                    f'\'{results["Server"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                    f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                    f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                    f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                    f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                    f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                    f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                )

            elif results["Suite"] in [Suites.BAT_D_A_M_H_TEST, Suites.BAT_D_R_H_TEST, Suites.BAT_S_C_TEST, \
            Suites.BAT_D_S_C_S_W_H_TEST, Suites.BAT_D_S_S_N_V_TEST, Suites.BAT_D_J_E_TEST, Suites.BAT_D_J_I_TEST, \
            Suites.BAT_D_H_M_F_A_TEST, Suites.BAT_D_H_W_S_TEST, Suites.BAT_D_E_B_TEST, Suites.BAT_COOLDOWN_TEMP_TEST, \
            Suites.BAT_HEAT_LED_TEST, Suites.BAT_PREMATURE_MASS_NO_RESET_TEST, Suites.BAT_LOCKED_WHEN_HOT_SHADOWS_TEST, \
            Suites.BAT_VACATION_CLEAN_MODE_TEST, Suites.BAT_VACATION_ECO_MODE_TEST, Suites.BAT_VACATION_ADD_MASS_COOLDOWN_TEST, \
            Suites.BAT_VACATION_RESET_TEST, Suites.BAT_D_GRINDER_SOFT_STALL_RETRY_TEST, Suites.BAT_D_GRINDER_STATE_LID_TEST, \
            Suites.BAT_D_GRINDER_HIGH_TEMP_JAM_TEST, Suites.BAT_D_GRINDER_JAM_AUTO_RETRY_TEST, Suites.BAT_D_FLUFF_NOT_RUN_TEST, \
            Suites.BAT_SET_START_TIME_DURING_HIP_TEST, Suites.BAT_RESUME_FROM_LIP_TEST, Suites.BAT_D_ALWAYS_LOCKED_TEST, \
            Suites.BAT_D_ALWAYS_UNLOCKED_TEST, Suites.BAT_D_BUCKET_FULLNESS_LOW_TEST, Suites.BAT_DELTA_MR_HIP_MASS_BUCKET_TEST, \
            Suites.BAT_D_LOCKED_WHEN_RUNNING_TEST, Suites.BAT_D_FR_HEAT_WARNING_STATUS_TEST, Suites.BAT_D_MASS_NO_CHANGE_RESET_TEST, \
            Suites.BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST, Suites.BAT_D_CYCLEENDTIME_LID_OPEN_TEST, Suites.BAT_D_UNPROCESSED_MASS_ZERO_TEST, \
            Suites.BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST, Suites.BAT_D_LIP_SKIPPED_HOT_TEST, Suites.BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST, \
            Suites.BAT_START_DISCONNECTED_TEST, Suites.BAT_RESUME_DISCONNECTED_TEST, Suites.BAT_HEAT_LED_INTERRUPTIONS_TEST, \
		    Suites.BAT_VACATION_AFTER_EMPTY_TEST, Suites.BAT_RESUME_COOLDOWN_TEST, Suites.BAT_VACATION_OTA_PRE_TEST, \
		    Suites.BAT_VACATION_OTA_POST_TEST, Suites.BAT_BUCKET_CRASH_OTA_PRE_TEST, Suites.BAT_BUCKET_CRASH_OTA_POST_TEST ]:
                    table_name = sqlsDash.q_table_bat
                    column_name = sqlsDash.q_column_bat
                    value_line = (
                        f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', \'{results["Stage"]}\', '
                        f'\'{results["Server"]}\', \'{results["Type"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                        f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                        f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                        f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                        f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                        f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                        f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                    )

            elif results["Suite"] in [Suites.SMOKE_PAIRING_TEST, Suites.SMOKE_TEST_LID_TEST, Suites.SMOKE_DGO_INACTIVE_TEST]:
                    table_name = sqlsDash.q_table_smoke
                    column_name = sqlsDash.q_column_smoke
                    value_line = (
                        f'VALUES="(\'{self.toTmpl(results["Build"])}\', \'{results["Oscar"]}\', '
                        f'\'{results["Server"]}\', \'{results["Type"]}\', \'{results["ThingSN"]}\', {results["ReportId"]}, '
                        f'{results["SvrId"]}, {results["DevId"]}, {results["TestExecuted"]}, '
                        f'{results["Passed"]}, {results["Failed"]}, \'{results["ExeTime"]}\', '
                        f'{results["Repeats"]}, \'{results["Jira1"]}\', {results["JiraF1"]}, '
                        f'\'{results["Jira2"]}\', {results["JiraF2"]}, \'{results["Jira3"]}\', '
                        f'{results["JiraF3"]}, \'{results["RLink"] }\', \'{results["TCLink"]}\', '
                        f'\'{results["DebugLink"]}\', \'{results["Notes"]}\')"'
                    )
            else:
                print(pattern.invalidtestsuite)

            fName = self.extractFilename(vFile)
            mataName = None
            if fName.startswith("O1_"):
                mataName = self.toTmpl(vBuild) + pattern.metadata_O1
            else:
                mataName = self.toTmpl(vBuild) + pattern.metadata_O2

            print("mataName= ", mataName)
            with open(mataName, 'a') as f:
                print (table_name, file=f)
                print (column_name, file=f)
                print(value_line, file=f)
                print (sqlsDash.q_query, file=f)
                print (sqlsDash.q_executes, file=f)
                print(file=f)

    def insertReportEntry(self, vTable, data, vOscar, vTemplateN):
        insert_query = sqlsDash.ins_report_entry_q.format(vTable)
        if self.insertRowData(insert_query, data):
            print(f"insert tabele: '{vTable}' => '{vOscar}' and '{vTemplateN}' data successful!")
        else:
            print(f"insert tabele: '{vTable}' => '{vOscar}' and '{vTemplateN}' data failed!")

    def updateReportEntry(self, vTable, values, vOscar, vTemplateN):
        update_query = sqlsDash.upd_report_entry_q.format(vTable)
        if self.updateRowData2(update_query, values):
            print(f"update tabele: '{vTable}' => '{vOscar}' and '{vTemplateN}' data successful!")
        else:
            print(f"update tabele: '{vTable}' => '{vOscar}' and '{vTemplateN}' data failed!")

    def selectReportEntry(self, vTable, vOscar, vTemplateN):
        vSql = self.convertSQL(sqlsDash.sel_report_entry_q, '[vTable]', vTable)
        vSql = self.convertSQL(vSql, '[vOscar]', vOscar)
        vSql = self.convertSQL(vSql, '[vTemplateN]', vTemplateN)
        ret = self.queryData(vSql)
        if ret:
            print(f"tabele: '{vTable}' => '{vOscar}' and '{vTemplateN}' ", ret)            

    def insertCurShippedEntry(self, vTable, data, vOscar):
        insert_query = sqlsDash.ins_cur_shipped_q.format(vTable)
        if self.insertRowData(insert_query, data):
            print(f"insert tabele: '{vTable}' => '{vOscar}' data successful!")
        else:
            print(f"insert tabele: '{vTable}' => '{vOscar}' data failed!")

    def updateCurShippedEntry(self, vTable, values, vOscar):
        update_query = sqlsDash.upd_cur_shipped_q
        if self.updateRowData2(update_query, values):
            print(f"update tabele: '{vTable}' => '{vOscar}' data successful!")
        else:
            print(f"update tabele: '{vTable}' => '{vOscar}' data failed!")

    def selectCurShippedEntry(self, vTable, vOscar):
        vSql = self.convertSQL(sqlsDash.sel_cur_shipped_q, '[vTable]', vTable)
        vSql = self.convertSQL(vSql, '[vOscar]', vOscar)
        ret = self.queryData(vSql)
        if ret:
            print(f"tabele: '{vTable}' => '{vOscar}' ", ret)    

    def insertDevicesEntry(self, vTable, data):
        insert_query = sqlsDash.ins_devices_q.format(vTable)
        if self.insertRowData(insert_query, data):
            print(f"insert tabele: '{vTable}' => data successful!")
        else:
            print(f"insert tabele: '{vTable}' => data failed!")

    def updateDevicesEntry(self, vTable, values):
        update_query = sqlsDash.upd_devices_q
        if self.updateRowData2(update_query, values):
            print(f"update tabele: '{vTable}' => data successful!")
        else:
            print(f"update tabele: '{vTable}' => data failed!")

    def selectDevicesEntry(self, vTable, vThing):
        vSql = self.convertSQL(sqlsDash.sel_devices_q, '[vThing]', vThing)
        ret = self.queryData(vSql)
        if ret:
            print(f"tabele: '{vTable}' => '{vThing}' ", ret)   