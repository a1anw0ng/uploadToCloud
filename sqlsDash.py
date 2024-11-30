class sqlsDash:
    report_q = f'''
        select * from REPORT_TABLE ORDER BY CreatedAt ASC;
        '''
    
    report2_q = f'''
        select * from REPORT_TABLE where Oscar = '[Oscar]' and templateN = '[templateN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''

    ota_o1_self_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'self' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    ota_o1_prod_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'prodUG' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    ota_o1_ext_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'extFTUG' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    ota_o1_int_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'intFTUG' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    power_o1_q = f'''
        select * from POWER_DURING_OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_idle_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'idle' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_lip_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'lip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_hip_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'hip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_cool_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'cooldown' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_fluff_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'fluff' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_idle_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'idle' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_lip_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'lip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_hip_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'hip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_cool_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'cooldown' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_fluff_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'fluff' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    safety_o1_q = f'''
        select * from SAFETY_TEST_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    pairing_o1_q = f'''
        select * from PAIRING_WITHOUT_BLE_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    lid_o1_q = f'''
        select * from LID_OPEN_CLOSE_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    start_a_o1_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O1' and TestType = 'stress' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    start_b_o1_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O1' and TestType = 'normal' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    eeprom_o1_q = f'''
        select * from EEPROM_STRESS_TEST_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    child_a_o1_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O1' and TestType = 'stress' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    child_b_o1_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O1' and TestType = 'normal' and TemplateN = '[curBuild_O1_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''






    ota_o2_self_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'self' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    ota_o2_prod_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'prodUG' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    ota_o2_ext_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'extFTUG' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    ota_o2_int_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'intFTUG' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    power_o2_q = f'''
        select * from POWER_DURING_OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_idle_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'idle' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_lip_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'lip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_hip_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'hip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_cool_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'cooldown' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_op_fluff_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'fluff' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_idle_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'idle' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_lip_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'lip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_hip_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'hip' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_cool_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'cooldown' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    dgo_mass_fluff_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'fluff' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    safety_o2_q = f'''
        select * from SAFETY_TEST_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    pairing_o2_q = f'''
        select * from PAIRING_WITHOUT_BLE_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    lid_o2_q = f'''
        select * from LID_OPEN_CLOSE_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    start_a_o2_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O2' and TestType = 'stress' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    start_b_o2_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O2' and TestType = 'normal' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    eeprom_o2_q = f'''
        select * from EEPROM_STRESS_TEST_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    child_a_o2_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O2' and TestType = 'stress' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    child_b_o2_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O2' and TestType = 'normal' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    boot_a_o2_q = f'''
        select * from BOOT_CYCLE_TABLE where OscarType = 'O2' and TestType = 'stress' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    smoke_pairing_o2_q = f'''
        select * from SMOKE_TEST_TABLE where OscarType = 'O2' and Type = 'pairing' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''



    bat_d_a_m_h_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = 'hip' and Type = 'add_mass_hip' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_r_h_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = 'hip' and Type = 'reset_hip' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''
    bat_d_s_c_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'sht40_calibration' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''
    bat_d_s_c_s_w_h_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'sht40_cal_skip_when_hot' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''
    bat_d_s_s_n_v_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'start_stop_no_vacation' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''



    bat_d_j_e_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'jam_error' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_j_i_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'jam_inactive' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_h_m_f_a_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = 'hip' and Type = 'hip_moisture_food_add' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_h_w_s_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'heat_warning_status' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_e_b_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'empty_bucket' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''




    bat_cooldown_temp_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'cooldown_temp' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_heat_led_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'heat_led' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_premature_mass_no_reset_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'premature_mass_no_reset' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_locked_when_hot_shadows_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'locked_when_hot_shadows' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    smoke_dgo_inactive_o2_q = f'''
        select * from SMOKE_TEST_TABLE where OscarType = 'O2' and Type = 'dgo_inactive' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    smoke_test_lid_o2_q = f'''
        select * from SMOKE_TEST_TABLE where OscarType = 'O2' and Type = 'test_lid' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''



    #GUO_ADDED

    bat_vacation_clean_mode_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'vacation_clean_mode' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_vacation_eco_mode_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'vacation_eco_mode' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_vacation_add_mass_cooldown_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'vacation_add_mass_cooldown' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_vacation_reset_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'vacation_reset' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_grinder_soft_stall_retry_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'grinder_soft_stall_retry' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''
    
    bat_d_grinder_state_lid_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'grinder_state_lid' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_grinder_high_temp_jam_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'grinder_high_temp_jam' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_grinder_jam_auto_retry_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'grinder_jam_auto_retry' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_fluff_not_run_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'fluff_not_run' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_set_start_time_during_hip_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'cycle_start_time_HIP' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_resume_from_lip_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'resume_lip' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_always_locked_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'always_locked' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_always_unlocked_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'always_unlocked' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_bucket_fullness_low_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'bucket_fullness_low' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_delta_mr_hip_mass_bucket_o2_q = f'''
            select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'dgo_hip_mass_bucket' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_locked_when_running_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'locked_when_running' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_fr_heat_warning_status_o2_q = f'''
            select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'fr_heat_warning_status' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_mass_no_change_reset_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'mass_no_change_reset' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_lastdgocycle_energy_shadows_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'lastdgocycle_energy_shadows' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_cycleendtime_lid_open_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'cycleendtime_lid_open' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_unprocessed_mass_zero_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'unprocessed_mass_zero' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_mass_add_lid_open_close_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'mass_add_lid_open_close' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_d_lip_skipped_hot_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'lip_skipped_hot' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''



    # 8/12/2024
    bat_hip_extension_lid_skipped_hot_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'hip_extension_lid_open_close' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_start_disconnected_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'start_disconnected' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_resume_disconnected_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'resume_disconnected' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_heat_led_interruptions_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'heat_led_interruptions' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_vacation_after_empty_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'vacation_after_empty' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_resume_cooldown_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'resume_cooldown' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''


    # 9/4/2024
    bat_vacation_ota_pre_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'bat_vacation_ota_pre' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_vacation_ota_post_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'bat_vacation_ota_post' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_bucket_crash_ota_pre_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'bat_bucket_crash_ota_pre' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

    bat_bucket_crash_ota_post_o2_q = f'''
        select * from BAT_TABLE where OscarType = 'O2' and Stage = '' and Type = 'bat_bucket_crash_ota_post' and TemplateN = '[curBuild_O2_B]' ORDER BY LOGTIME DESC LIMIT 1;
    '''

















    report_fk_q = f'''
        select id FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''


    server_fk_q = f'''
        select id FROM SERVERS_TABLE where ServerName = '[serverN]' and Runner = '[runnerN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''

    device_fk_q = f'''
        select id FROM DEVICES_TABLE where Thing = '[SN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''


    build_notes_q = f'''
        select BuildNotes FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''

    jiras_q = f'''
        select Jira1, Jira2, Jira3 FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''

    blockers_q = f'''
        select Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3 FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''


    insert_q_ota = """INSERT INTO {} (TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    insert_q_power = """INSERT INTO {} (TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    insert_q_dgo_op = """INSERT INTO {} (TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    insert_q_dgo_mass = """INSERT INTO {} (TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    


    insert_q_pairing = """INSERT INTO {} (TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    insert_q_eeprom = """INSERT INTO {} (TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""



    insert_q_safety = """INSERT INTO {} (TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""



    insert_q_lid = """INSERT INTO {} (TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    insert_q_start_via_bin = """INSERT INTO {} (TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    insert_q_child = """INSERT INTO {} (TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    insert_q_boot = """INSERT INTO {} (TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    insert_q_bat = """INSERT INTO {} (TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    insert_q_smoke = """INSERT INTO {} (TemplateN, OscarType, SvrName, Type, ThingSN, OscarId, SvrId,  
                            DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                            Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""



    q_query = f'''QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"'''

    q_executes = f'''psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"'''

    q_table_ota = '''TABLE_NAME="OTA_TABLE"'''
    
    q_column_ota = '''COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats,  
                        Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes, MinT, MaxT, AvgT, FailedNum, RecvrNum)"'''


    q_table_power = '''TABLE_NAME="POWER_DURING_OTA_TABLE"'''
    q_column_power = '''COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''
                

    q_table_dgo_op = '''TABLE_NAME="DGO_OP_PR_TABLE"''' 
    q_column_dgo_op = '''COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''
                

    q_table_dgo_mass = '''TABLE_NAME="DGO_ADD_MASS_TABLE"'''
    q_column_dgo_mass = '''COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''
    
    q_table_pairing = '''TABLE_NAME="PAIRING_WITHOUT_BLE_TABLE"'''
    q_column_pairing = '''COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''
            

    q_table_eeprom = '''TABLE_NAME="EEPROM_STRESS_TEST_TABLE"'''
    q_column_eeprom = '''COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''
    
    q_table_safety = '''TABLE_NAME="SAFETY_TEST_TABLE"'''
    q_column_safety = '''COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''


    q_table_lid = '''TABLE_NAME="LID_OPEN_CLOSE_TABLE"'''
    q_column_lid = '''COLUMN_NAMES="(TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''


    q_table_start_via_bin = '''TABLE_NAME="START_VIA_BIN_TABLE"'''
    q_column_start_via_bin = '''COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''


    q_table_child = '''TABLE_NAME="CHILD_LOCK_TABLE"'''
    q_column_child = '''COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)"'''

    q_table_boot = '''TABLE_NAME="BOOT_CYCLE_TABLE"'''
    q_column_boot = '''COLUMN_NAMES="(TemplateN, OscarType, TestType, SvrName, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" '''



    q_table_bat = '''TABLE_NAME="BAT_TABLE"'''
    q_column_bat = '''COLUMN_NAMES="(TemplateN, OscarType, Stage, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" '''


    q_table_smoke = '''TABLE_NAME="SMOKE_TEST_TABLE"'''
    q_column_smoke = '''COLUMN_NAMES="(TemplateN, OscarType, SvrName, Type, ThingSN, OscarId, SvrId, DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, ResultLink, TestCasesLink, DebugLink, Notes)" '''









    ins_report_entry_q = """INSERT INTO {} (Oscar, BuildDate, TemplateN, BuildN, CodeN, BuildType, ProdRelTemplate, ProdRelversion, ExtFTRelTemplate, ExtFTRelVersion, IntFTRelTemplate,  
                        IntFTRelVersion, BuildId, StatusId, JiraId, BuildStatus, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, BuildNotes, ClsStatus, BuildLink)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    upd_report_entry_q = """UPDATE {}
                SET Oscar = %s, BuildDate = %s, TemplateN = %s, BuildN = %s, CodeN = %s, BuildType = %s, 
                ProdRelTemplate = %s, ProdRelversion = %s, ExtFTRelTemplate = %s, ExtFTRelVersion = %s, 
                IntFTRelTemplate = %s, IntFTRelVersion = %s, BuildId = %s, StatusId = %s, JiraId = %s, 
                BuildStatus = %s, Jira1 = %s, JiraF1 = %s, Jira2 = %s, JiraF2 = %s, Jira3 = %s, 
                JiraF3 = %s, BuildNotes = %s, ClsStatus = %s, BuildLink = %s 
                WHERE id = (SELECT MAX(id) FROM REPORT_TABLE WHERE Oscar = %s AND TemplateN = %s);"""



    sel_report_entry_q = '''
        select * from [vTable] where Oscar = '[vOscar]' and TemplateN = '[vTemplateN]' ORDER BY CreatedAt DESC LIMIT 1;
    '''



    ins_cur_shipped_q = """INSERT INTO {} (Oscar, CodeN, BuildType, ProdRelT, ProdRelV, ExtFTRelT, ExtFTRelV, IntFTRelT, IntFTRelV, DayOImgT, DayOImgV, FFUImgT, FFUImgV, 
                        AutoOTAT, AutoOTAV, FactoryImg, DiagImg, UserGrp1T, UserGrp1V, UserGrp2T, UserGrp2V, UserGrp3T, UserGrp3V)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    upd_cur_shipped_q = """
            WITH sorted_rows AS (
                SELECT id
                FROM CUR_SHIPPED_TABLE
                WHERE Oscar = %s
                ORDER BY CreatedAt DESC
                LIMIT 1
            )
            UPDATE CUR_SHIPPED_TABLE
            SET 
                Oscar = %s,
                CodeN = %s,
                BuildType = %s,
                ProdRelT = %s,
                ProdRelV = %s,
                ExtFTRelT = %s,
                ExtFTRelV = %s,
                IntFTRelT = %s,
                IntFTRelV = %s,
                DayOImgT = %s,
                DayOImgV = %s,    
                FFUImgT = %s,
                FFUImgV = %s,
                AutoOTAT = %s,
                AutoOTAV = %s,    
                FactoryImg = %s,
                DiagImg = %s,
                UserGrp1T = %s,
                UserGrp1V = %s,
                UserGrp2T = %s,
                UserGrp2V = %s,
                UserGrp3T = %s,
                UserGrp3V = %s
            FROM sorted_rows
            WHERE CUR_SHIPPED_TABLE.id = sorted_rows.id;
        """
    










    ins_devices_q = """INSERT INTO {} (Thing, ThingGroup, Ipaddr, MacAddr, Ssid, WifiPW, Advertisement, Oscartype, Platform, Tests, Server,  
                        Runner, PoolName, Interfaces)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    upd_devices_q = """UPDATE DEVICES_TABLE
        SET 
            Thing = %s,
            ThingGroup = %s,
            Ipaddr = %s,
            MacAddr = %s,
            Ssid = %s,
            WifiPW = %s,
            Advertisement = %s,
            Oscartype = %s,
            Platform = %s,
            Tests = %s,
            Server = %s,
            Runner = %s,
            PoolName = %s,
            Interfaces = %s,
        WHERE id = (SELECT MAX(id) FROM DEVICES_TABLE WHERE Thing = %s);"""


    sel_devices_q = f"""select * from DEVICES_TABLE where thing = '[vThing]' ORDER BY CreatedAt DESC LIMIT 1;"""




    ins_servers_q = """INSERT INTO {} (ServerName, Ipaddr1, Ipaddr2, Ipaddr3, Fqdn, PortIndex, RaspPort, Switchport, Runner, RunnerGrp, Labels)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""


    upd_servers_q = """UPDATE SERVERS_TABLE
        SET 
            ServerName = %s,
            Ipaddr1 = %s,
            Ipaddr2 = %s,
            Ipaddr3 = %s,
            Fqdn = %s,
            PortIndex = %s,
            RaspPort = %s,
            Switchport = %s,
            Runner = %s,
            RunnerGrp = %s,
            Labels = %s,
        WHERE id = (SELECT MAX(id) FROM SERVERS_TABLE WHERE ServerName = %s AND Runner = %s);"""

    sel_devices_q1 = """select * from SERVERS_TABLE where ServerName = '[vServer]' ORDER BY CreatedAt DESC LIMIT 1;"""
    
    sel_devices_q2 = """select * from SERVERS_TABLE where ServerName = '[vServer]' and Runner = '[vRunner]' ORDER BY CreatedAt DESC LIMIT 1;"""
