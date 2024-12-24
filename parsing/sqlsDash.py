class sqlsDash:
    report_q = f'''
        select * from REPORT_TABLE ORDER BY CreatedAt ASC;
        '''
    
    report2_q = f'''
        select * from REPORT_TABLE where Oscar = '[Oscar]' and templateN = '[templateN]';
    '''

    ota_o1_self_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'self';
    '''

    ota_o1_prod_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'prodUG';
    '''

    ota_o1_ext_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'extFTUG';
    '''

    ota_o1_int_q = f'''
        select * from OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]' and TestType = 'intFTUG';
    '''

    power_o1_q = f'''
        select * from POWER_DURING_OTA_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1]';
    '''

    dgo_op_idle_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'idle';
    '''

    dgo_op_lip_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'lip';
    '''

    dgo_op_hip_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'hip';
    '''

    dgo_op_cool_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'cooldown';
    '''

    dgo_op_fluff_o1_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'fluff';
    '''

    dgo_mass_idle_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'idle';
    '''

    dgo_mass_lip_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'lip';
    '''

    dgo_mass_hip_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'hip';
    '''

    dgo_mass_cool_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'cooldown';
    '''

    dgo_mass_fluff_o1_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]' and Stage = 'fluff';
    '''

    safety_o1_q = f'''
        select * from SAFETY_TEST_TABLE where OscarType = 'O1' and TemplateN = '" + curBuild_O1_B + "';
    '''

    pairing_o1_q = f'''
        select * from PAIRING_WITHOUT_BLE_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]';
    '''

    lid_o1_q = f'''
        select * from LID_OPEN_CLOSE_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]';
    '''

    start_a_o1_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O1' and TestType = 'stress' and TemplateN = '[curBuild_O1_B]';
    '''

    start_b_o1_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O1' and TestType = 'normal' and TemplateN = '[curBuild_O1_B]';
    '''

    eeprom_o1_q = f'''
        select * from EEPROM_STRESS_TEST_TABLE where OscarType = 'O1' and TemplateN = '[curBuild_O1_B]';
    '''

    child_a_o1_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O1' and TestType = 'stress' and TemplateN = '[curBuild_O1_B]';
    '''

    child_b_o1_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O1' and TestType = 'normal' and TemplateN = '[curBuild_O1_B]';
    '''






    ota_o2_self_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'self';
    '''

    ota_o2_prod_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'prodUG';
    '''

    ota_o2_ext_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'extFTUG';
    '''

    ota_o2_int_q = f'''
        select * from OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]' and TestType = 'intFTUG';
    '''

    power_o2_q = f'''
        select * from POWER_DURING_OTA_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2]';
    '''

    dgo_op_idle_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'idle';
    '''

    dgo_op_lip_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'lip';
    '''

    dgo_op_hip_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'hip';
    '''

    dgo_op_cool_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'cooldown';
    '''

    dgo_op_fluff_o2_q = f'''
        select * from DGO_OP_PR_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'fluff';
    '''

    dgo_mass_idle_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'idle';
    '''

    dgo_mass_lip_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'lip';
    '''

    dgo_mass_hip_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'hip';
    '''

    dgo_mass_cool_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'cooldown';
    '''

    dgo_mass_fluff_o2_q = f'''
        select * from DGO_ADD_MASS_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]' and Stage = 'fluff';
    '''

    safety_o2_q = f'''
        select * from SAFETY_TEST_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]';
    '''

    pairing_o2_q = f'''
        select * from PAIRING_WITHOUT_BLE_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]';
    '''

    lid_o2_q = f'''
        select * from LID_OPEN_CLOSE_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]';
    '''

    start_a_o2_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O2' and TestType = 'stress' and TemplateN = '[curBuild_O2_B]';
    '''

    start_b_o2_q = f'''
        select * from START_VIA_BIN_TABLE where OscarType = 'O2' and TestType = 'normal' and TemplateN = '[curBuild_O2_B]';
    '''

    eeprom_o2_q = f'''
        select * from EEPROM_STRESS_TEST_TABLE where OscarType = 'O2' and TemplateN = '[curBuild_O2_B]';
    '''

    child_a_o2_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O2' and TestType = 'stress' and TemplateN = '[curBuild_O2_B]';
    '''

    child_b_o2_q = f'''
        select * from CHILD_LOCK_TABLE where OscarType = 'O2' and TestType = 'normal' and TemplateN = '[curBuild_O2_B]';
    '''

    boot_a_o2_q = f'''
        select * from BOOT_CYCLE_TABLE where OscarType = 'O2' and TestType = 'stress' and TemplateN = '[curBuild_O2_B]';
    '''




    report_fk_q = f'''
        select id FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]';
    '''


    server_fk_q = f'''
        select id FROM SERVERS_TABLE where ServerName = '[serverN]';
    '''

    device_fk_q = f'''
        select id FROM DEVICES_TABLE where Thing = '[SN]';
    '''


    build_notes_q = f'''
        select BuildNotes FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]';
    '''

    jiras_q = f'''
        select Jira1, Jira2, Jira3 FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]';
    '''

    blockers_q = f'''
        select Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3 FROM REPORT_TABLE where Oscar = '[oscarT]' and BuildN = '[buildN]';
    '''


    svr_name_q = f'''
        
    '''
