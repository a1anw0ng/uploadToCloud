import yaml
import psycopg2
import json
import copy
import os
import shutil
from bs4 import BeautifulSoup
import re
import io
from sqlsDash import sqlsDash
from millPostDB import millPostDB
from configparser import ConfigParser


class AutoGeneratePages(millPostDB):
    def __init__(self, db=None, usr=None, pw=None, host=None):
        self.port = 5432
        self.sysLogF = False

        if db is not None and usr is not None and pw is not None and host is not None:
            super().__init__(db, host, usr, pw, self.port, self.sysLogF)
        else:
            CONFIGFILE = "../conf/config"
            config_object = ConfigParser()
            config_object.read(CONFIGFILE)
            postConf = config_object["postdb"]

            database = postConf["database"] 
            host = postConf["host"] 
            user = postConf["user"] 
            password = postConf["password"] 
            port = postConf["port"] 

        self.cursor = None
        self.m_nodes = []
        self.json_data = None
        self.cur_builds_row = {}
        self.rel_info_rows = None
        self.ota_self_data = {}
        self.ota_prod_data = {}
        self.ota_ext_ft_data = {}
        self.ota_int_ft_data = {}
        self.ota_power_data = {}
        self.dgo_idle_op_data = {}
        self.dgo_lip_op_data = {}
        self.dgo_hip_op_data = {}
        self.dgo_cooldown_op_data = {}
        self.dgo_fluff_op_data = {}
        self.dgo_idle_mass_data = {}
        self.dgo_lip_mass_data = {}
        self.dgo_hip_mass_data = {}
        self.dgo_cooldown_mass_data = {}
        self.dgo_fluff_mass_data = {}
        self.dgo_safety_data = {}
        self.dgo_pair_data = {}
        self.dgo_lid_data = {}
        self.dgo_start_bin_A_data = {}
        self.dgo_start_bin_B_data = {}
        self.dgo_eeprom_data = {}
        self.dgo_lock_A_data = {}
        self.dgo_lock_B_data = {}
        self.boot_cycle_A_data = {}
        self.bat_dgo_add_mass_hip_data = {}
        self.bat_dgo_reset_hip_data = {}
        self.bat_dgo_sht40_calibration_data = {}
        self.bat_dgo_sht40_cal_skip_when_hot_data = {}
        self.bat_dgo_start_stop_no_vacation_data = {}
        self.smoke_pairing_data = {}
        self.bat_dgo_jam_error = {}
        self.bat_dgo_jam_inactive = {}
        self.bat_dgo_hip_moisture_food_add = {}
        self.bat_dgo_heat_warning_status = {}
        self.bat_dgo_empty_bucket = {}
        self.cur_builds_row_O2 = {}
        self.rel_info_rows_O2 = None
        self.ota_self_data_O2 = {}
        self.ota_prod_data_O2 = {}
        self.ota_ext_ft_data_O2 = {}
        self.ota_int_ft_data_O2 = {}
        self.ota_power_data_O2 = {}
        self.dgo_idle_op_data_O2 = {}
        self.dgo_lip_op_data_O2 = {}
        self.dgo_hip_op_data_O2 = {}
        self.dgo_cooldown_op_data_O2 = {}
        self.dgo_fluff_op_data_O2 = {}
        self.dgo_idle_mass_data_O2 = {}
        self.dgo_lip_mass_data_O2 = {}
        self.dgo_hip_mass_data_O2 = {}
        self.dgo_cooldown_mass_data_O2 = {}
        self.dgo_fluff_mass_data_O2 = {}
        self.dgo_safety_data_O2 = {}
        self.dgo_pair_data_O2 = {}
        self.dgo_start_bin_A_data_O2 = {}
        self.dgo_start_bin_B_data_O2 = {}
        self.dgo_eeprom_data_O2 = {}
        self.dgo_lock_A_data_O2 = {}
        self.dgo_lock_B_data_O2 = {}
        self.boot_cycle_A_data_O2 = {}
        self.bat_dgo_add_mass_hip_data_O2 = {}
        self.bat_dgo_reset_hip_data_O2 = {}
        self.bat_dgo_sht40_calibration_data_O2 = {}
        self.bat_dgo_sht40_cal_skip_when_hot_data_O2 = {}
        self.bat_dgo_start_stop_no_vacation_data_O2 = {}
        self.smoke_pairing_data_O2 = {}
        self.bat_dgo_jam_error_data_O2 = {}
        self.bat_dgo_jam_inactive_data_O2 = {}
        self.bat_dgo_hip_moisture_food_add_data_O2 = {}
        self.bat_dgo_heat_warning_status_data_O2 = {}
        self.bat_dgo_empty_bucket_data_O2 = {}
        self.bat_dgo_empty_bucket_data_O2 = {}

        self.bat_cooldown_temp_data_O2 = {}
        self.bat_heat_led_data_O2 = {}
        self.bat_premature_mass_no_reset_data_O2 = {}
        self.bat_locked_when_hot_shadows_data_O2 = {}
        self.smoke_dgo_inactive_data_O2 = {}
        self.smoke_test_lid_data_O2 = {}

        #GUO_ADDED
        self.bat_vacation_clean_mode_data_O2 = {}
        self.bat_vacation_eco_mode_data_O2 = {}
        self.bat_dgo_vacation_add_mass_cooldown_data_O2 = {}
        self.bat_dgo_vacation_reset_data_O2 = {}
        self.bat_grinder_soft_stall_retry_data_O2 = {}
        self.bat_dgo_grinder_state_lid_data_O2 = {}
        self.bat_dgo_grinder_high_temp_jam_data_O2 = {}
        self.bat_dgo_grinder_jam_auto_retry_data_O2 = {}
        self.bat_dgo_fluff_not_run_data_O2 = {}
        self.dgo_set_cycle_start_time_HIP_data_O2 = {}
        self.bat_dgo_resume_lip_data_O2 = {}
        self.bat_dgo_always_locked_data_O2 = {}
        self.bat_dgo_always_unlocked_data_O2 = {}
        self.bat_dgo_bucket_fullness_low_data_O2 = {}
        self.bat_dgo_hip_mass_bucket_data_O2 = {}
        self.bat_dgo_locked_when_running_data_O2 = {}
        self.bat_dgo_fr_heat_warning_status_data_O2 = {}
        self.bat_dgo_mass_no_change_reset_data_O2 = {}
        self.bat_dgo_lastDgoCycle_energy_shadows_data_O2 = {}
        self.bat_dgo_cycleEndTime_lid_open_data_O2 = {}
        self.bat_dgo_unprocessed_mass_zero_data_O2 = {}
        self.bat_dgo_mass_add_lid_open_close_data_O2 = {}
        self.bat_dgo_lip_skipped_hot_data_O2 = {}

        # 8/12/2024
        self.bat_hip_extension_lid_open_close_data_O2 = {}
        self.bat_start_disconnected_data_O2 = {}
        self.bat_resume_disconnected_data_O2 = {}
        self.bat_heat_led_interruptions_data_O2 = {}
        self.bat_vacation_after_empty_data_O2 = {}
        self.bat_resume_cooldown_data_O2 = {}

        # 9/4/2024 
        self.bat_vacation_ota_pre_data_O2 = {}
        self.bat_vacation_ota_post_data_O2 = {}
        self.bat_bucket_crash_ota_pre_data_O2 = {}
        self.bat_bucket_crash_ota_post_data_O2 = {}


    def __del__(self):
        self.cursor.close()
        self.cursor = None

    def replace_file(self, targetF, templF):
        if os.path.isfile(targetF):
            try:
                os.remove(targetF)
            except OSError as e:
                print(f"Error: {e.strerror}")
                return
        else:
            print(f"No old file found at '{targetF}'. No need to delete.")

        try:
            shutil.copy2(templF, targetF)
        except shutil.Error as e:
            print(f"Error: {e}")


    def getCursor(self):
        self.cursor = super().getCursor()


    def queryReportTable(self, sqlQuery):
        self.cursor.execute(sqlQuery)
        rows = self.cursor.fetchall()
        for i, v in enumerate(rows):
            node = {
                    "index": int(rows[i][0]),
                    "buildId": str(rows[i][13]),
                    "Build": str(rows[i][4]),
                    "Oscar": str(rows[i][1]),
                    "buildLink": str(rows[i][25]),
                    "CodeName": str(rows[i][5]),
                    "BuildDate": str(rows[i][2]),
                    "statusId": str(rows[i][14]),
                    "clsStatus": str(rows[i][24]),
                    "Status": str(rows[i][16]),
                    "jiraId": str(rows[i][15]),
                    "Jira1": str(rows[i][17]),
                    "JiraF1": "0" if rows[i][18] == False else "1",   
                    "Jira2": str(rows[i][19]),
                    "JiraF2": "0" if rows[i][20] == False else "1",     
                    "Jira3": str(rows[i][21]),
                    "JiraF3": "0" if rows[i][22] == False else "1",    
                    "Notes": str(rows[i][23])
            }
            self.m_nodes.append(node)

    def update_and_get_forms(self, rows, newK):
        forms = {
                newK: {'TestExecuted': str(rows[0][8]), 
                            'Passed': str(rows[0][9]), 
                            'Failed': str(rows[0][10]), 
                            'ExeTime': str(rows[0][11]),               
                            'Repeats': str(rows[0][12]),
                            'Jira1': rows[0][13], 
                            'JiraF1': "0" if rows[0][14] == False else "1",
                            'Jira2': rows[0][15], 
                            'JiraF2':  "0" if rows[0][16] == False else "1",    
                            'Jira3': rows[0][17], 
                            'JiraF3': "0" if rows[0][18] == False else "1",     
                            'ResultLink': rows[0][19],
                            'TestCasesLink': rows[0][20]
                            }}
        return forms

    def update_and_get_forms2(self, rows, newK):
        forms = {
                newK: {'TestExecuted': str(rows[0][9]), 
                            'Passed': str(rows[0][10]), 
                            'Failed': str(rows[0][11]), 
                            'ExeTime': str(rows[0][12]),               
                            'Repeats': str(rows[0][13]),
                            'Jira1': rows[0][14], 
                            'JiraF1': "0" if rows[0][15] == False else "1",
                            'Jira2': rows[0][16], 
                            'JiraF2':  "0" if rows[0][17] == False else "1",    
                            'Jira3': rows[0][18], 
                            'JiraF3': "0" if rows[0][19] == False else "1",     
                            'ResultLink': rows[0][20],
                            'TestCasesLink': rows[0][21]
                            }}
        return forms



    def update_and_get_forms3(self, rows, newK):
        forms = {
                newK: {'TestExecuted': str(rows[0][10]), 
                            'Passed': str(rows[0][11]), 
                            'Failed': str(rows[0][12]), 
                            'ExeTime': str(rows[0][13]),               
                            'Repeats': str(rows[0][14]),
                            'Jira1': rows[0][15], 
                            'JiraF1': "0" if rows[0][16] == False else "1",
                            'Jira2': rows[0][17], 
                            'JiraF2':  "0" if rows[0][18] == False else "1",    
                            'Jira3': rows[0][19], 
                            'JiraF3': "0" if rows[0][20] == False else "1",     
                            'ResultLink': rows[0][21],
                            'TestCasesLink': rows[0][22]
                            }}
        return forms



    def query_release_info_by_build(self, templateN, Oscar):

        sqlQuery = self.convertSQL(sqlsDash.report2_q, '[Oscar]', Oscar)
        sqlQuery = self.convertSQL(sqlQuery, '[templateN]', templateN)

        self.cursor.execute(sqlQuery)
        if Oscar == "O1":
            self.rel_info_rows = self.cursor.fetchall()
        else:
            self.rel_info_rows_O2 = self.cursor.fetchall()

    def queryCurShippedBuilds(self, qCurBuilds, fO1=True):
        self.cursor.execute(qCurBuilds)
        if fO1:
            self.cur_builds_row = self.cursor.fetchall()
        else:
            self.cur_builds_row_O2 = self.cursor.fetchall()


    def queryOTASelfTable(self, qOtaSelf, fO1=True):
        self.cursor.execute(qOtaSelf)
        rows = self.cursor.fetchall()
        forms = {
                'OTA_SELF': {'TestExecuted': str(rows[0][8]), 
                            'Passed': str(rows[0][9]), 
                            'Failed': str(rows[0][10]), 
                            'ExeTime': str(rows[0][11]),               
                            'Repeats': str(rows[0][12]),
                            'Jira1': rows[0][13], 
                            'JiraF1': "0" if rows[0][14] == False else "1",
                            'Jira2': rows[0][15], 
                            'JiraF2':  "0" if rows[0][16] == False else "1",    
                            'Jira3': rows[0][17], 
                            'JiraF3': "0" if rows[0][18] == False else "1",     
                            'ResultLink': rows[0][19],
                            'TestCasesLink': rows[0][20]
                            }}
        if fO1:
            self.ota_self_data = copy.deepcopy(forms)
        else:
            self.ota_self_data_O2 = copy.deepcopy(forms)

    def queryOTASelfTable2(self, qOtaSelf, fO1=True):
        #print("qOtaSelf= ", qOtaSelf)
        self.cursor.execute(qOtaSelf)
        rows = self.cursor.fetchall()
        #print("rows= ", rows)

        forms = {
                'OTA_SELF': {'TestExecuted': str(rows[0][9]), 
                            'Passed': str(rows[0][10]), 
                            'Failed': str(rows[0][11]), 
                            'ExeTime': str(rows[0][12]),               
                            'Repeats': str(rows[0][13]),
                            'Jira1': rows[0][14], 
                            'JiraF1': "0" if rows[0][15] == False else "1",
                            'Jira2': rows[0][16], 
                            'JiraF2':  "0" if rows[0][17] == False else "1",    
                            'Jira3': rows[0][18], 
                            'JiraF3': "0" if rows[0][19] == False else "1",     
                            'ResultLink': rows[0][20],
                            'TestCasesLink': rows[0][21]
                            }}
        if fO1:
            self.ota_self_data = copy.deepcopy(forms)
        else:
            self.ota_self_data_O2 = copy.deepcopy(forms)

    def queryTable(self, q, newK, fO1=True):
        #print("q", q)
        self.cursor.execute(q)
        rows = self.cursor.fetchall()
        #print("rows", rows)
        if len(rows) == 0:
            return

        if newK == "OTA_PROD_UPGRADE":
            if fO1:
                self.ota_prod_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.ota_prod_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "OTA_EXT_FT_UPGRADE" :
            if fO1:
                self.ota_ext_ft_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.ota_ext_ft_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "OTA_INT_FT_UPGRADE" :
            if fO1:
                self.ota_int_ft_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.ota_int_ft_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "POWER_DURING_OTA" :
            if fO1:
                self.ota_power_data = copy.deepcopy(self.update_and_get_forms(rows, newK))
            else:
                self.ota_power_data_O2 = copy.deepcopy(self.update_and_get_forms(rows, newK))
        elif newK == "DGO_IDLE_OP_PR" :
            if fO1:
                self.dgo_idle_op_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_idle_op_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_LIP_OP_PR" :
            if fO1:
                self.dgo_lip_op_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_lip_op_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_HIP_OP_PR" :
            if fO1:
                self.dgo_hip_op_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_hip_op_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_COOLDOWN_OP_PR" :
            if fO1:
                self.dgo_cooldown_op_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_cooldown_op_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_FLUFF_OP_PR" :
            if fO1:
                self.dgo_fluff_op_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_fluff_op_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_IDLE_ADD_MASS" :
            if fO1:
                self.dgo_idle_mass_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_idle_mass_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_LIP_ADD_MASS" :
            if fO1:
                self.dgo_lip_mass_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_lip_mass_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_HIP_ADD_MASS" :
            if fO1:
                self.dgo_hip_mass_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_hip_mass_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_COOLDOWN_ADD_MASS" :
            if fO1:
                self.dgo_cooldown_mass_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_cooldown_mass_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "DGO_FLUFF_ADD_MASS" :
            if fO1:
                self.dgo_fluff_mass_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_fluff_mass_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "SAFETY_TEST" :
            if fO1:
                self.dgo_safety_data = copy.deepcopy(self.update_and_get_forms(rows, newK))
            else:
                self.dgo_safety_data_O2 = copy.deepcopy(self.update_and_get_forms(rows, newK))

        elif newK == "PAIRING_WITHOUT_BLE" :
            if fO1:
                self.dgo_pair_data = copy.deepcopy(self.update_and_get_forms(rows, newK))
            else:
                self.dgo_pair_data_O2 = copy.deepcopy(self.update_and_get_forms(rows, newK))
        elif newK == "LID_OPEN_CLOSE" :
            if fO1:
                self.dgo_lid_data = copy.deepcopy(self.update_and_get_forms(rows, newK))
        elif newK == "START_VIA_BIN_STRESS_A" :
            if fO1:
                self.dgo_start_bin_A_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_start_bin_A_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "START_VIA_BIN_B" :
            if fO1:
                self.dgo_start_bin_B_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_start_bin_B_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "EEPROM_STRESS_TEST" :
            if fO1:
                self.dgo_eeprom_data = copy.deepcopy(self.update_and_get_forms(rows, newK))
            else:
                self.dgo_eeprom_data_O2 = copy.deepcopy(self.update_and_get_forms(rows, newK))
        elif newK == "CHILD_LOCK_STRESS_TEST" :
            if fO1:
                self.dgo_lock_A_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_lock_A_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))
        elif newK == "CHILD_LOCK_TEST" :
            if fO1:
                self.dgo_lock_B_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.dgo_lock_B_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))

        elif newK == "BOOT_CYCLE_STRESS_TEST" :
            if fO1:
                self.boot_cycle_A_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.boot_cycle_A_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))



        elif newK == "BAT_DGO_ADD_MASS_HIP_TEST" :
            if fO1:
                self.bat_dgo_add_mass_hip_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_add_mass_hip_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_RESET_HIP_TEST" :
            if fO1:
                self.bat_dgo_reset_hip_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_reset_hip_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_SHT40_CALIBRATION_TEST" :
            if fO1:
                self.bat_dgo_sht40_calibration_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_sht40_calibration_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST" :
            if fO1:
                self.bat_dgo_sht40_cal_skip_when_hot_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_sht40_cal_skip_when_hot_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_START_STOP_NO_VACATION_TEST" :
            if fO1:
                self.bat_dgo_start_stop_no_vacation_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_start_stop_no_vacation_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "SMOKE_PAIRING_TEST" :
            if fO1:
                self.smoke_pairing_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.smoke_pairing_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))

        elif newK == "BAT_DGO_JAM_ERROR_TEST" :
            if fO1:
                self.bat_dgo_jam_error_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_jam_error_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_JAM_INACTIVE_TEST" :
            if fO1:
                self.bat_dgo_jam_inactive_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_jam_inactive_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST" :
            if fO1:
                self.bat_dgo_hip_moisture_food_add_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_hip_moisture_food_add_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_HEAT_WARNING_STATUS_TEST" :
            if fO1:
                self.bat_dgo_heat_warning_status_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_heat_warning_status_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DGO_EMPTY_BUCKET_TEST" :
            if fO1:
                self.bat_dgo_empty_bucket_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_empty_bucket_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_COOLDOWN_TEMP_TEST" :
            if fO1:
                self.bat_cooldown_temp_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_cooldown_temp_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_HEAT_LED_TEST" :
            if fO1:
                self.bat_heat_led_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_heat_led_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_PREMATURE_MASS_NO_RESET_TEST" :
            if fO1:
                self.bat_premature_mass_no_reset_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_premature_mass_no_reset_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_LOCKED_WHEN_HOT_SHADOWS_TEST" :
            if fO1:
                self.bat_locked_when_hot_shadows_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_locked_when_hot_shadows_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "SMOKE_DGO_INACTIVE_TEST" :
            if fO1:
                self.smoke_dgo_inactive_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.smoke_dgo_inactive_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))

        elif newK == "SMOKE_TEST_LID_TEST" :
            if fO1:
                self.smoke_test_lid_data = copy.deepcopy(self.update_and_get_forms2(rows, newK))
            else:
                self.smoke_test_lid_data_O2 = copy.deepcopy(self.update_and_get_forms2(rows, newK))






        #GUO_ADDED
        elif newK == "BAT_VACATION_CLEAN_MODE_TEST" :
            if fO1:
                self.bat_vacation_clean_mode_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_vacation_clean_mode_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_VACATION_ECO_MODE_TEST" :
            if fO1:
                self.bat_vacation_eco_mode_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_vacation_eco_mode_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_VACATION_ADD_MASS_COOLDOWN_TEST" :
            if fO1:
                self.bat_dgo_vacation_add_mass_cooldown_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_vacation_add_mass_cooldown_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_VACATION_RESET_TEST" :
            if fO1:
                self.bat_dgo_vacation_reset_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_vacation_reset_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_GRINDER_SOFT_STALL_RETRY_TEST" :
            if fO1:
                self.bat_grinder_soft_stall_retry_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_grinder_soft_stall_retry_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_GRINDER_STATE_LID_TEST" :
            if fO1:
                self.bat_dgo_grinder_state_lid_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_grinder_state_lid_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_GRINDER_HIGH_TEMP_JAM_TEST" :
            if fO1:
                self.bat_dgo_grinder_high_temp_jam_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_grinder_high_temp_jam_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_GRINDER_JAM_AUTO_RETRY_TEST" :
            if fO1:
                self.bat_dgo_grinder_jam_auto_retry_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_grinder_jam_auto_retry_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_FLUFF_NOT_RUN_TEST" :
            if fO1:
                self.bat_dgo_fluff_not_run_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_fluff_not_run_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_SET_START_TIME_DURING_HIP_TEST" :
            if fO1:
                self.dgo_set_cycle_start_time_HIP_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.dgo_set_cycle_start_time_HIP_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_RESUME_FROM_LIP_TEST" :
            if fO1:
                self.bat_dgo_resume_lip_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_resume_lip_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_ALWAYS_LOCKED_TEST" :
            if fO1:
                self.bat_dgo_always_locked_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_always_locked_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_ALWAYS_UNLOCKED_TEST" :
            if fO1:
                self.bat_dgo_always_unlocked_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_always_unlocked_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_BUCKET_FULLNESS_LOW_TEST" :
            if fO1:
                self.bat_dgo_bucket_fullness_low_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_bucket_fullness_low_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_DELTA_MR_HIP_MASS_BUCKET_TEST" :
            if fO1:
                self.bat_dgo_hip_mass_bucket_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_hip_mass_bucket_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_LOCKED_WHEN_RUNNING_TEST" :
            if fO1:
                self.bat_dgo_locked_when_running_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_locked_when_running_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_FR_HEAT_WARNING_STATUS_TEST" :
            if fO1:
                self.bat_dgo_fr_heat_warning_status_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_fr_heat_warning_status_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_MASS_NO_CHANGE_RESET_TEST" :
            if fO1:
                self.bat_dgo_mass_no_change_reset_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_mass_no_change_reset_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST" :
            if fO1:
                self.bat_dgo_lastDgoCycle_energy_shadows_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_lastDgoCycle_energy_shadows_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_CYCLEENDTIME_LID_OPEN_TEST" :
            if fO1:
                self.bat_dgo_cycleEndTime_lid_open_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_cycleEndTime_lid_open_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_UNPROCESSED_MASS_ZERO_TEST" :
            if fO1:
                self.bat_dgo_unprocessed_mass_zero_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_unprocessed_mass_zero_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST" :
            if fO1:
                self.bat_dgo_mass_add_lid_open_close_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_mass_add_lid_open_close_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_D_LIP_SKIPPED_HOT_TEST" :
            if fO1:
                self.bat_dgo_lip_skipped_hot_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_dgo_lip_skipped_hot_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))


        # 8/12/2024

        elif newK == "BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST" :
            if fO1:
                self.bat_hip_extension_lid_open_close_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_hip_extension_lid_open_close_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_START_DISCONNECTED_TEST" :
            if fO1:
                self.bat_start_disconnected_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_start_disconnected_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_RESUME_DISCONNECTED_TEST" :
            if fO1:
                self.bat_resume_disconnected_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_resume_disconnected_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_HEAT_LED_INTERRUPTIONS_TEST" :
            if fO1:
                self.bat_heat_led_interruptions_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_heat_led_interruptions_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_VACATION_AFTER_EMPTY_TEST" :
            if fO1:
                self.bat_vacation_after_empty_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_vacation_after_empty_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_RESUME_COOLDOWN_TEST" :
            if fO1:
                self.bat_resume_cooldown_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_resume_cooldown_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))






        # 9/4/2024 
        elif newK == "BAT_VACATION_OTA_PRE_TEST" :
            if fO1:
                self.bat_vacation_ota_pre_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_vacation_ota_pre_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_VACATION_OTA_POST_TEST" :
            if fO1:
                self.bat_vacation_ota_post_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_vacation_ota_post_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_BUCKET_CRASH_OTA_PRE_TEST" :
            if fO1:
                self.bat_bucket_crash_ota_pre_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_bucket_crash_ota_pre_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))

        elif newK == "BAT_BUCKET_CRASH_OTA_POST_TEST" :
            if fO1:
                self.bat_bucket_crash_ota_post_data = copy.deepcopy(self.update_and_get_forms3(rows, newK))
            else:
                self.bat_bucket_crash_ota_post_data_O2 = copy.deepcopy(self.update_and_get_forms3(rows, newK))








    def convertNPrepareDataJson(self, curBuild_O1, curBuild_O2, targetFile, templFile, logFile="logFile.log", fMDash=True, fLog=False):

        # print("curBuild_O1= ", curBuild_O1)
        # print("curBuild_O2= ", curBuild_O2)
        combined_data = {}
        if fMDash:
            self.json_data = json.dumps(self.m_nodes, indent=3)
        else:
            if curBuild_O1 and curBuild_O2:
                combined_data = {
                    'O1': {
                        **self.ota_self_data,
                        **self.ota_prod_data,
                        **self.ota_ext_ft_data,
                        **self.ota_int_ft_data,
                        **self.ota_power_data,
                        **self.dgo_idle_op_data,
                        **self.dgo_lip_op_data,
                        **self.dgo_hip_op_data,
                        **self.dgo_cooldown_op_data,
                        **self.dgo_fluff_op_data,
                        **self.dgo_idle_mass_data,
                        **self.dgo_lip_mass_data,
                        **self.dgo_hip_mass_data,
                        **self.dgo_cooldown_mass_data,
                        **self.dgo_fluff_mass_data,
                        **self.dgo_safety_data,
                        **self.dgo_pair_data,
                        **self.dgo_lid_data,
                        **self.dgo_start_bin_A_data,        
                        **self.dgo_start_bin_B_data,
                        **self.dgo_eeprom_data,
                        **self.dgo_lock_A_data,
                        **self.dgo_lock_B_data,
                        **self.boot_cycle_A_data,
                        **self.bat_dgo_add_mass_hip_data,
                        **self.bat_dgo_reset_hip_data,
                        **self.bat_dgo_sht40_calibration_data,
                        **self.bat_dgo_sht40_cal_skip_when_hot_data,
                        **self.bat_dgo_start_stop_no_vacation_data,
                        **self.smoke_pairing_data_data
                    },   
                    'O2': {
                        **self.ota_self_data_O2,
                        **self.ota_prod_data_O2,
                        **self.ota_ext_ft_data_O2,
                        **self.ota_int_ft_data_O2,
                        **self.ota_power_data_O2,
                        **self.dgo_idle_op_data_O2,
                        **self.dgo_lip_op_data_O2,
                        **self.dgo_hip_op_data_O2,
                        **self.dgo_cooldown_op_data_O2,
                        **self.dgo_fluff_op_data_O2,
                        **self.dgo_idle_mass_data_O2,
                        **self.dgo_lip_mass_data_O2,
                        **self.dgo_hip_mass_data_O2,
                        **self.dgo_cooldown_mass_data_O2,
                        **self.dgo_fluff_mass_data_O2,
                        **self.dgo_safety_data_O2,
                        **self.dgo_pair_data_O2,
                        **self.dgo_start_bin_A_data_O2,        
                        **self.dgo_start_bin_B_data_O2,
                        **self.dgo_eeprom_data_O2,
                        **self.dgo_lock_A_data_O2,
                        **self.dgo_lock_B_data_O2,
                        **self.boot_cycle_A_data_O2,
                        **self.bat_dgo_add_mass_hip_data_O2,
                        **self.bat_dgo_reset_hip_data_O2,
                        **self.bat_dgo_sht40_calibration_data_O2,
                        **self.bat_dgo_sht40_cal_skip_when_hot_data_O2,
                        **self.bat_dgo_start_stop_no_vacation_data_O2,
                        **self.smoke_pairing_data_O2,
                        **self.bat_dgo_jam_error_data_O2,
                        **self.bat_dgo_jam_inactive_data_O2,
                        **self.bat_dgo_hip_moisture_food_add_data_O2,
                        **self.bat_dgo_heat_warning_status_data_O2,
                        **self.bat_dgo_empty_bucket_data_O2,
                        **self.bat_cooldown_temp_data_O2,
                        **self.bat_heat_led_data_O2,
                        **self.bat_premature_mass_no_reset_data_O2,
                        **self.bat_locked_when_hot_shadows_data_O2,
                        **self.smoke_dgo_inactive_data_O2,
                        **self.smoke_test_lid_data_O2,

                        #GUO_ADDED
                        **self.bat_vacation_clean_mode_data_O2,
                        **self.bat_vacation_eco_mode_data_O2,
                        **self.bat_dgo_vacation_add_mass_cooldown_data_O2,
                        **self.bat_dgo_vacation_reset_data_O2,
                        **self.bat_grinder_soft_stall_retry_data_O2,
                        **self.bat_dgo_grinder_state_lid_data_O2,
                        **self.bat_dgo_grinder_high_temp_jam_data_O2,
                        **self.bat_dgo_grinder_jam_auto_retry_data_O2,
                        **self.bat_dgo_fluff_not_run_data_O2,
                        **self.dgo_set_cycle_start_time_HIP_data_O2,
                        **self.bat_dgo_resume_lip_data_O2,
                        **self.bat_dgo_always_locked_data_O2,
                        **self.bat_dgo_always_unlocked_data_O2,
                        **self.bat_dgo_bucket_fullness_low_data_O2,
                        **self.bat_dgo_hip_mass_bucket_data_O2,
                        **self.bat_dgo_locked_when_running_data_O2,
                        **self.bat_dgo_fr_heat_warning_status_data_O2,
                        **self.bat_dgo_mass_no_change_reset_data_O2,
                        **self.bat_dgo_lastDgoCycle_energy_shadows_data_O2,
                        **self.bat_dgo_cycleEndTime_lid_open_data_O2,
                        **self.bat_dgo_unprocessed_mass_zero_data_O2,
                        **self.bat_dgo_mass_add_lid_open_close_data_O2,
                        **self.bat_dgo_lip_skipped_hot_data_O2,

                        # 8/12/2024
                        **self.bat_hip_extension_lid_open_close_data_O2,
                        **self.bat_start_disconnected_data_O2,
                        **self.bat_resume_disconnected_data_O2,
                        **self.bat_heat_led_interruptions_data_O2,
                        **self.bat_vacation_after_empty_data_O2,
                        **self.bat_resume_cooldown_data_O2,

                        # 9/4/2024 
                        **self.bat_vacation_ota_pre_data_O2,
                        **self.bat_vacation_ota_post_data_O2,
                        **self.bat_bucket_crash_ota_pre_data_O2,
                        **self.bat_bucket_crash_ota_post_data_O2

                    }
                }
            elif curBuild_O1:
                combined_data = {
                    'O1': {
                        **self.ota_self_data,
                        **self.ota_prod_data,
                        **self.ota_ext_ft_data,
                        **self.ota_int_ft_data,
                        **self.ota_power_data,
                        **self.dgo_idle_op_data,
                        **self.dgo_lip_op_data,
                        **self.dgo_hip_op_data,
                        **self.dgo_cooldown_op_data,
                        **self.dgo_fluff_op_data,
                        **self.dgo_idle_mass_data,
                        **self.dgo_lip_mass_data,
                        **self.dgo_hip_mass_data,
                        **self.dgo_cooldown_mass_data,
                        **self.dgo_fluff_mass_data,
                        **self.dgo_safety_data,
                        **self.dgo_pair_data,
                        **self.dgo_lid_data,
                        **self.dgo_start_bin_A_data,        
                        **self.dgo_start_bin_B_data,
                        **self.dgo_eeprom_data,
                        **self.dgo_lock_A_data,
                        **self.dgo_lock_B_data,
                        **self.boot_cycle_A_data,
                        **self.bat_dgo_add_mass_hip_data,
                        **self.bat_dgo_reset_hip_data,
                        **self.bat_dgo_sht40_calibration_data,
                        **self.bat_dgo_sht40_cal_skip_when_hot_data,
                        **self.bat_dgo_start_stop_no_vacation_data,
                        **self.smoke_pairing_data
                    }
                }
            elif curBuild_O2:
                combined_data = {
                    'O2': {
                        **self.ota_self_data_O2,
                        **self.ota_prod_data_O2,
                        **self.ota_ext_ft_data_O2,
                        **self.ota_int_ft_data_O2,
                        **self.ota_power_data_O2,
                        **self.dgo_idle_op_data_O2,
                        **self.dgo_lip_op_data_O2,
                        **self.dgo_hip_op_data_O2,
                        **self.dgo_cooldown_op_data_O2,
                        **self.dgo_fluff_op_data_O2,
                        **self.dgo_idle_mass_data_O2,
                        **self.dgo_lip_mass_data_O2,
                        **self.dgo_hip_mass_data_O2,
                        **self.dgo_cooldown_mass_data_O2,
                        **self.dgo_fluff_mass_data_O2,
                        **self.dgo_safety_data_O2,
                        **self.dgo_pair_data_O2,
                        **self.dgo_start_bin_A_data_O2,        
                        **self.dgo_start_bin_B_data_O2,
                        **self.dgo_eeprom_data_O2,
                        **self.dgo_lock_A_data_O2,
                        **self.dgo_lock_B_data_O2,
                        **self.boot_cycle_A_data_O2,
                        **self.bat_dgo_add_mass_hip_data_O2,
                        **self.bat_dgo_reset_hip_data_O2,
                        **self.bat_dgo_sht40_calibration_data_O2,
                        **self.bat_dgo_sht40_cal_skip_when_hot_data_O2,
                        **self.bat_dgo_start_stop_no_vacation_data_O2,
                        **self.smoke_pairing_data_O2,
                        **self.bat_dgo_jam_error_data_O2,
                        **self.bat_dgo_jam_inactive_data_O2,
                        **self.bat_dgo_hip_moisture_food_add_data_O2,
                        **self.bat_dgo_heat_warning_status_data_O2,
                        **self.bat_dgo_empty_bucket_data_O2,
                        **self.bat_cooldown_temp_data_O2,
                        **self.bat_heat_led_data_O2,
                        **self.bat_premature_mass_no_reset_data_O2,
                        **self.bat_locked_when_hot_shadows_data_O2,
                        **self.smoke_dgo_inactive_data_O2,
                        **self.smoke_test_lid_data_O2,

                        #GUO_ADDED
                        **self.bat_vacation_clean_mode_data_O2,
                        **self.bat_vacation_eco_mode_data_O2,
                        **self.bat_dgo_vacation_add_mass_cooldown_data_O2,
                        **self.bat_dgo_vacation_reset_data_O2,
                        **self.bat_grinder_soft_stall_retry_data_O2,
                        **self.bat_dgo_grinder_state_lid_data_O2,
                        **self.bat_dgo_grinder_high_temp_jam_data_O2,
                        **self.bat_dgo_grinder_jam_auto_retry_data_O2,
                        **self.bat_dgo_fluff_not_run_data_O2,
                        **self.dgo_set_cycle_start_time_HIP_data_O2,
                        **self.bat_dgo_resume_lip_data_O2,
                        **self.bat_dgo_always_locked_data_O2,
                        **self.bat_dgo_always_unlocked_data_O2,
                        **self.bat_dgo_bucket_fullness_low_data_O2,
                        **self.bat_dgo_hip_mass_bucket_data_O2,
                        **self.bat_dgo_locked_when_running_data_O2,
                        **self.bat_dgo_fr_heat_warning_status_data_O2,
                        **self.bat_dgo_mass_no_change_reset_data_O2,
                        **self.bat_dgo_lastDgoCycle_energy_shadows_data_O2,
                        **self.bat_dgo_cycleEndTime_lid_open_data_O2,
                        **self.bat_dgo_unprocessed_mass_zero_data_O2,
                        **self.bat_dgo_mass_add_lid_open_close_data_O2,
                        **self.bat_dgo_lip_skipped_hot_data_O2,

                        # 8/12/2024
                        **self.bat_hip_extension_lid_open_close_data_O2,
                        **self.bat_start_disconnected_data_O2,
                        **self.bat_resume_disconnected_data_O2,
                        **self.bat_heat_led_interruptions_data_O2,
                        **self.bat_vacation_after_empty_data_O2,
                        **self.bat_resume_cooldown_data_O2,

                        # 9/4/2024 
                        **self.bat_vacation_ota_pre_data_O2,
                        **self.bat_vacation_ota_post_data_O2,
                        **self.bat_bucket_crash_ota_pre_data_O2,
                        **self.bat_bucket_crash_ota_post_data_O2

                    }
                }
            self.json_data = json.dumps(combined_data, indent=3)

        if fLog:
            if fMDash:
                with open(logFile, 'w') as file:
                    file.write(self.json_data)
            else:
                with open(logFile, 'w') as file:
                    file.write(self.json_data)

        self.replace_file(targetFile, templFile)


    def build_structure_O1(self, js_code):
        data = json.loads(self.json_data)
        js_code = re.sub(r'O1SWITCH', '1', js_code)

        if self.rel_info_rows[0][7] != "N/A" or self.rel_info_rows[0][7] != "":
            js_code = re.sub(r'O1_PROD', '"' + self.rel_info_rows[0][7] + '"', js_code)

        if self.rel_info_rows[0][9] != "N/A" or self.rel_info_rows[0][9] != "":   
            js_code = re.sub(r'O1_EXT_FT', '"' + self.rel_info_rows[0][9] + '"', js_code)

        if self.rel_info_rows[0][11] != "N/A" or self.rel_info_rows[0][11] != "": 
            js_code = re.sub(r'O1_INT_FT', '"' + self.rel_info_rows[0][11] + '"', js_code)

        if "OTA_SELF" in data["O1"]:
            js_code = re.sub(r'O1SELFSWITCH', '1', js_code)
            js_code = re.sub(r'O1_OTA_SELF_PASSED', data['O1']['OTA_SELF']['Passed'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_FAILED', data['O1']['OTA_SELF']['Failed'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_TESTS', data['O1']['OTA_SELF']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_EXECTIME', '"' + data['O1']['OTA_SELF']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_SELF_REPEATS', data['O1']['OTA_SELF']['Repeats'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_JIRA1_FLAG', data['O1']['OTA_SELF']['JiraF1'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_JIRA1', '"' + data['O1']['OTA_SELF']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_SELF_JIRA2_FLAG', data['O1']['OTA_SELF']['JiraF2'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_JIRA2', '"' + data['O1']['OTA_SELF']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_SELF_JIRA3_FLAG', data['O1']['OTA_SELF']['JiraF3'], js_code)
            js_code = re.sub(r'O1_OTA_SELF_JIRA3', '"' + data['O1']['OTA_SELF']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_SELF_RESULT_LINK', '"' + data['O1']['OTA_SELF']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_SELF_TCASE_LINK', '"' + data['O1']['OTA_SELF']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1SELFSWITCH', '0', js_code)

        if "OTA_PROD_UPGRADE" in data["O1"]:
            js_code = re.sub(r'O1PRODSWITCH', '1', js_code)
            js_code = re.sub(r'O1_OTA_PROD_PASSED', data['O1']['OTA_PROD_UPGRADE']['Passed'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_FAILED', data['O1']['OTA_PROD_UPGRADE']['Failed'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_TESTS', data['O1']['OTA_PROD_UPGRADE']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_EXECTIME', '"' + data['O1']['OTA_PROD_UPGRADE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_PROD_REPEATS', data['O1']['OTA_PROD_UPGRADE']['Repeats'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_JIRA1_FLAG', data['O1']['OTA_PROD_UPGRADE']['JiraF1'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_JIRA1', '"' + data['O1']['OTA_PROD_UPGRADE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_PROD_JIRA2_FLAG', data['O1']['OTA_PROD_UPGRADE']['JiraF2'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_JIRA2', '"' + data['O1']['OTA_PROD_UPGRADE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_PROD_JIRA3_FLAG', data['O1']['OTA_PROD_UPGRADE']['JiraF3'], js_code)
            js_code = re.sub(r'O1_OTA_PROD_JIRA3', '"' + data['O1']['OTA_PROD_UPGRADE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_PROD_RESULT_LINK', '"' + data['O1']['OTA_PROD_UPGRADE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_PROD_TCASE_LINK', '"' + data['O1']['OTA_PROD_UPGRADE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1PRODSWITCH', '0', js_code)

        if "OTA_EXT_FT_UPGRADE" in data["O1"]:
            js_code = re.sub(r'O1EXTSWITCH', '1', js_code)
            js_code = re.sub(r'O1_OTA_EXT_PASSED', data['O1']['OTA_EXT_FT_UPGRADE']['Passed'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_FAILED', data['O1']['OTA_EXT_FT_UPGRADE']['Failed'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_TESTS', data['O1']['OTA_EXT_FT_UPGRADE']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_EXECTIME', '"' + data['O1']['OTA_EXT_FT_UPGRADE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_EXT_REPEATS', data['O1']['OTA_EXT_FT_UPGRADE']['Repeats'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_JIRA1_FLAG', data['O1']['OTA_EXT_FT_UPGRADE']['JiraF1'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_JIRA1', '"' + data['O1']['OTA_EXT_FT_UPGRADE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_EXT_JIRA2_FLAG', data['O1']['OTA_EXT_FT_UPGRADE']['JiraF2'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_JIRA2', '"' + data['O1']['OTA_EXT_FT_UPGRADE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_EXT_JIRA3_FLAG', data['O1']['OTA_EXT_FT_UPGRADE']['JiraF3'], js_code)
            js_code = re.sub(r'O1_OTA_EXT_JIRA3', '"' + data['O1']['OTA_EXT_FT_UPGRADE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_EXT_RESULT_LINK', '"' + data['O1']['OTA_EXT_FT_UPGRADE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_EXT_TCASE_LINK', '"' + data['O1']['OTA_EXT_FT_UPGRADE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1EXTSWITCH', '0', js_code)

        if "OTA_INT_FT_UPGRADE" in data["O1"]:
            js_code = re.sub(r'O1INTSWITCH', '1', js_code)
            js_code = re.sub(r'O1_OTA_INT_PASSED', data['O1']['OTA_INT_FT_UPGRADE']['Passed'], js_code)
            js_code = re.sub(r'O1_OTA_INT_FAILED', data['O1']['OTA_INT_FT_UPGRADE']['Failed'], js_code)
            js_code = re.sub(r'O1_OTA_INT_TESTS', data['O1']['OTA_INT_FT_UPGRADE']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_OTA_INT_EXECTIME', '"' + data['O1']['OTA_INT_FT_UPGRADE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_INT_REPEATS', data['O1']['OTA_INT_FT_UPGRADE']['Repeats'], js_code)
            js_code = re.sub(r'O1_OTA_INT_JIRA1_FLAG', data['O1']['OTA_INT_FT_UPGRADE']['JiraF1'], js_code)
            js_code = re.sub(r'O1_OTA_INT_JIRA1', '"' + data['O1']['OTA_INT_FT_UPGRADE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_INT_JIRA2_FLAG', data['O1']['OTA_INT_FT_UPGRADE']['JiraF2'], js_code)
            js_code = re.sub(r'O1_OTA_INT_JIRA2', '"' + data['O1']['OTA_INT_FT_UPGRADE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_INT_JIRA3_FLAG', data['O1']['OTA_INT_FT_UPGRADE']['JiraF3'], js_code)
            js_code = re.sub(r'O1_OTA_INT_JIRA3', '"' + data['O1']['OTA_INT_FT_UPGRADE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_INT_RESULT_LINK', '"' + data['O1']['OTA_INT_FT_UPGRADE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_INT_TCASE_LINK', '"' + data['O1']['OTA_INT_FT_UPGRADE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1INTSWITCH', '0', js_code)

        if "POWER_DURING_OTA" in data["O1"]:
            js_code = re.sub(r'O1POWERSWITCH', '1', js_code)
            js_code = re.sub(r'O1_OTA_POWER_PASSED', data['O1']['POWER_DURING_OTA']['Passed'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_FAILED', data['O1']['POWER_DURING_OTA']['Failed'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_TESTS', data['O1']['POWER_DURING_OTA']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_EXECTIME', '"' + data['O1']['POWER_DURING_OTA']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_POWER_REPEATS', data['O1']['POWER_DURING_OTA']['Repeats'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_JIRA1_FLAG', data['O1']['POWER_DURING_OTA']['JiraF1'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_JIRA1', '"' + data['O1']['POWER_DURING_OTA']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_POWER_JIRA2_FLAG', data['O1']['POWER_DURING_OTA']['JiraF2'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_JIRA2', '"' + data['O1']['POWER_DURING_OTA']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_POWER_JIRA3_FLAG', data['O1']['POWER_DURING_OTA']['JiraF3'], js_code)
            js_code = re.sub(r'O1_OTA_POWER_JIRA3', '"' + data['O1']['POWER_DURING_OTA']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_POWER_RESULT_LINK', '"' + data['O1']['POWER_DURING_OTA']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_OTA_POWER_TCASE_LINK', '"' + data['O1']['POWER_DURING_OTA']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1POWERSWITCH', '0', js_code)

        if "DGO_IDLE_OP_PR" in data["O1"]:
            js_code = re.sub(r'O1IDLEOPSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_PASSED', data['O1']['DGO_IDLE_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_FAILED', data['O1']['DGO_IDLE_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_TESTS', data['O1']['DGO_IDLE_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_EXECTIME', '"' + data['O1']['DGO_IDLE_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_REPEATS', data['O1']['DGO_IDLE_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_JIRA1_FLAG', data['O1']['DGO_IDLE_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_JIRA1', '"' + data['O1']['DGO_IDLE_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_JIRA2_FLAG', data['O1']['DGO_IDLE_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_JIRA2', '"' + data['O1']['DGO_IDLE_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_JIRA3_FLAG', data['O1']['DGO_IDLE_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_JIRA3', '"' + data['O1']['DGO_IDLE_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_RESULT_LINK', '"' + data['O1']['DGO_IDLE_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_OP_TCASE_LINK', '"' + data['O1']['DGO_IDLE_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1IDLEOPSWITCH', '0', js_code)

        if "DGO_LIP_OP_PR" in data["O1"]:
            js_code = re.sub(r'O1LIPOPSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_PASSED', data['O1']['DGO_LIP_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_FAILED', data['O1']['DGO_LIP_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_TESTS', data['O1']['DGO_LIP_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_EXECTIME', '"' + data['O1']['DGO_LIP_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_REPEATS', data['O1']['DGO_LIP_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_JIRA1_FLAG', data['O1']['DGO_LIP_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_JIRA1', '"' + data['O1']['DGO_LIP_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_JIRA2_FLAG', data['O1']['DGO_LIP_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_JIRA2', '"' + data['O1']['DGO_LIP_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_JIRA3_FLAG', data['O1']['DGO_LIP_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_JIRA3', '"' + data['O1']['DGO_LIP_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_RESULT_LINK', '"' + data['O1']['DGO_LIP_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_OP_TCASE_LINK', '"' + data['O1']['DGO_LIP_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1LIPOPSWITCH', '0', js_code)

        if "DGO_HIP_OP_PR" in data["O1"]:
            js_code = re.sub(r'O1HIPOPSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_PASSED', data['O1']['DGO_HIP_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_FAILED', data['O1']['DGO_HIP_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_TESTS', data['O1']['DGO_HIP_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_EXECTIME', '"' + data['O1']['DGO_HIP_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_REPEATS', data['O1']['DGO_HIP_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_JIRA1_FLAG', data['O1']['DGO_HIP_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_JIRA1', '"' + data['O1']['DGO_HIP_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_JIRA2_FLAG', data['O1']['DGO_HIP_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_JIRA2', '"' + data['O1']['DGO_HIP_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_JIRA3_FLAG', data['O1']['DGO_HIP_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_JIRA3', '"' + data['O1']['DGO_HIP_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_RESULT_LINK', '"' + data['O1']['DGO_HIP_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_OP_TCASE_LINK', '"' + data['O1']['DGO_HIP_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1HIPOPSWITCH', '0', js_code)

        if "DGO_COOLDOWN_OP_PR" in data["O1"]:
            js_code = re.sub(r'O1COOLOPSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_PASSED', data['O1']['DGO_COOLDOWN_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_FAILED', data['O1']['DGO_COOLDOWN_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_TESTS', data['O1']['DGO_COOLDOWN_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_EXECTIME', '"' + data['O1']['DGO_COOLDOWN_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_REPEATS', data['O1']['DGO_COOLDOWN_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_JIRA1_FLAG', data['O1']['DGO_COOLDOWN_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_JIRA1', '"' + data['O1']['DGO_COOLDOWN_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_JIRA2_FLAG', data['O1']['DGO_COOLDOWN_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_JIRA2', '"' + data['O1']['DGO_COOLDOWN_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_JIRA3_FLAG', data['O1']['DGO_COOLDOWN_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_JIRA3', '"' + data['O1']['DGO_COOLDOWN_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_RESULT_LINK', '"' + data['O1']['DGO_COOLDOWN_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_OP_TCASE_LINK', '"' + data['O1']['DGO_COOLDOWN_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1COOLOPSWITCH', '0', js_code)

        if "DGO_FLUFF_OP_PR" in data["O1"]:
            js_code = re.sub(r'O1FLUFFOPSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_PASSED', data['O1']['DGO_FLUFF_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_FAILED', data['O1']['DGO_FLUFF_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_TESTS', data['O1']['DGO_FLUFF_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_EXECTIME', '"' + data['O1']['DGO_FLUFF_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_REPEATS', data['O1']['DGO_FLUFF_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_JIRA1_FLAG', data['O1']['DGO_FLUFF_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_JIRA1', '"' + data['O1']['DGO_FLUFF_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_JIRA2_FLAG', data['O1']['DGO_FLUFF_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_JIRA2', '"' + data['O1']['DGO_FLUFF_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_JIRA3_FLAG', data['O1']['DGO_FLUFF_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_JIRA3', '"' + data['O1']['DGO_FLUFF_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_RESULT_LINK', '"' + data['O1']['DGO_FLUFF_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_OP_TCASE_LINK', '"' + data['O1']['DGO_FLUFF_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1FLUFFOPSWITCH', '0', js_code)


        if "DGO_IDLE_ADD_MASS" in data["O1"]:
            js_code = re.sub(r'O1IDLEMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_PASSED', data['O1']['DGO_IDLE_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_FAILED', data['O1']['DGO_IDLE_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_TESTS', data['O1']['DGO_IDLE_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_EXECTIME', '"' + data['O1']['DGO_IDLE_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_REPEATS', data['O1']['DGO_IDLE_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_JIRA1_FLAG', data['O1']['DGO_IDLE_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_JIRA1', '"' + data['O1']['DGO_IDLE_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_JIRA2_FLAG', data['O1']['DGO_IDLE_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_JIRA2', '"' + data['O1']['DGO_IDLE_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_JIRA3_FLAG', data['O1']['DGO_IDLE_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_JIRA3', '"' + data['O1']['DGO_IDLE_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_RESULT_LINK', '"' + data['O1']['DGO_IDLE_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_IDLE_MASS_TCASE_LINK', '"' + data['O1']['DGO_IDLE_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1IDLEMASSSWITCH', '0', js_code)

        if "DGO_LIP_ADD_MASS" in data["O1"]:
            js_code = re.sub(r'O1LIPMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_PASSED', data['O1']['DGO_LIP_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_FAILED', data['O1']['DGO_LIP_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_TESTS', data['O1']['DGO_LIP_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_EXECTIME', '"' + data['O1']['DGO_LIP_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_REPEATS', data['O1']['DGO_LIP_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_JIRA1_FLAG', data['O1']['DGO_LIP_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_JIRA1', '"' + data['O1']['DGO_LIP_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_JIRA2_FLAG', data['O1']['DGO_LIP_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_JIRA2', '"' + data['O1']['DGO_LIP_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_JIRA3_FLAG', data['O1']['DGO_LIP_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_JIRA3', '"' + data['O1']['DGO_LIP_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_RESULT_LINK', '"' + data['O1']['DGO_LIP_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_LIP_MASS_TCASE_LINK', '"' + data['O1']['DGO_LIP_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1LIPMASSSWITCH', '0', js_code)

        if "DGO_HIP_ADD_MASS" in data["O1"]:
            js_code = re.sub(r'O1HIPMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_PASSED', data['O1']['DGO_HIP_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_FAILED', data['O1']['DGO_HIP_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_TESTS', data['O1']['DGO_HIP_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_EXECTIME', '"' + data['O1']['DGO_HIP_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_REPEATS', data['O1']['DGO_HIP_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_JIRA1_FLAG', data['O1']['DGO_HIP_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_JIRA1', '"' + data['O1']['DGO_HIP_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_JIRA2_FLAG', data['O1']['DGO_HIP_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_JIRA2', '"' + data['O1']['DGO_HIP_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_JIRA3_FLAG', data['O1']['DGO_HIP_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_JIRA3', '"' + data['O1']['DGO_HIP_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_RESULT_LINK', '"' + data['O1']['DGO_HIP_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_HIP_MASS_TCASE_LINK', '"' + data['O1']['DGO_HIP_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1HIPMASSSWITCH', '0', js_code)

        if "DGO_COOLDOWN_ADD_MASS" in data["O1"]:
            js_code = re.sub(r'O1COOLMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_PASSED', data['O1']['DGO_COOLDOWN_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_FAILED', data['O1']['DGO_COOLDOWN_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_TESTS', data['O1']['DGO_COOLDOWN_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_EXECTIME', '"' + data['O1']['DGO_COOLDOWN_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_REPEATS', data['O1']['DGO_COOLDOWN_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_JIRA1_FLAG', data['O1']['DGO_COOLDOWN_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_JIRA1', '"' + data['O1']['DGO_COOLDOWN_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_JIRA2_FLAG', data['O1']['DGO_COOLDOWN_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_JIRA2', '"' + data['O1']['DGO_COOLDOWN_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_JIRA3_FLAG', data['O1']['DGO_COOLDOWN_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_JIRA3', '"' + data['O1']['DGO_COOLDOWN_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_RESULT_LINK', '"' + data['O1']['DGO_COOLDOWN_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_COOLDOWN_MASS_TCASE_LINK', '"' + data['O1']['DGO_COOLDOWN_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1COOLMASSSWITCH', '0', js_code)

        if "DGO_FLUFF_ADD_MASS" in data["O1"]:
            js_code = re.sub(r'O1FLUFFMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_PASSED', data['O1']['DGO_FLUFF_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_FAILED', data['O1']['DGO_FLUFF_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_TESTS', data['O1']['DGO_FLUFF_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_EXECTIME', '"' + data['O1']['DGO_FLUFF_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_REPEATS', data['O1']['DGO_FLUFF_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_JIRA1_FLAG', data['O1']['DGO_FLUFF_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_JIRA1', '"' + data['O1']['DGO_FLUFF_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_JIRA2_FLAG', data['O1']['DGO_FLUFF_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_JIRA2', '"' + data['O1']['DGO_FLUFF_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_JIRA3_FLAG', data['O1']['DGO_FLUFF_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_JIRA3', '"' + data['O1']['DGO_FLUFF_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_RESULT_LINK', '"' + data['O1']['DGO_FLUFF_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_DGO_FLUFF_MASS_TCASE_LINK', '"' + data['O1']['DGO_FLUFF_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1FLUFFMASSSWITCH', '0', js_code)

        if "SAFETY_TEST" in data["O1"]:
            js_code = re.sub(r'O1SAFETYSWITCH', '1', js_code)
            js_code = re.sub(r'O1_SAFETY_PASSED', data['O1']['SAFETY_TEST']['Passed'], js_code)
            js_code = re.sub(r'O1_SAFETY_FAILED', data['O1']['SAFETY_TEST']['Failed'], js_code)
            js_code = re.sub(r'O1_SAFETY_TESTS', data['O1']['SAFETY_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_SAFETY_EXECTIME', '"' + data['O1']['SAFETY_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_SAFETY_REPEATS', data['O1']['SAFETY_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O1_SAFETY_JIRA1_FLAG', data['O1']['SAFETY_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O1_SAFETY_JIRA1', '"' + data['O1']['SAFETY_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_SAFETY_JIRA2_FLAG', data['O1']['SAFETY_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O1_SAFETY_JIRA2', '"' + data['O1']['SAFETY_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_SAFETY_JIRA3_FLAG', data['O1']['SAFETY_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O1_SAFETY_JIRA3', '"' + data['O1']['SAFETY_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_SAFETY_RESULT_LINK', '"' + data['O1']['SAFETY_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_SAFETY_TCASE_LINK', '"' + data['O1']['SAFETY_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1SAFETYSWITCH', '0', js_code)

        if "PAIRING_WITHOUT_BLE" in data["O1"]:
            js_code = re.sub(r'O1PAIRINGSWITCH', '1', js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_PASSED', data['O1']['PAIRING_WITHOUT_BLE']['Passed'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_FAILED', data['O1']['PAIRING_WITHOUT_BLE']['Failed'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_TESTS', data['O1']['PAIRING_WITHOUT_BLE']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_EXECTIME', '"' + data['O1']['PAIRING_WITHOUT_BLE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_REPEATS', data['O1']['PAIRING_WITHOUT_BLE']['Repeats'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_JIRA1_FLAG', data['O1']['PAIRING_WITHOUT_BLE']['JiraF1'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_JIRA1', '"' + data['O1']['PAIRING_WITHOUT_BLE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_JIRA2_FLAG', data['O1']['PAIRING_WITHOUT_BLE']['JiraF2'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_JIRA2', '"' + data['O1']['PAIRING_WITHOUT_BLE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_JIRA3_FLAG', data['O1']['PAIRING_WITHOUT_BLE']['JiraF3'], js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_JIRA3', '"' + data['O1']['PAIRING_WITHOUT_BLE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_RESULT_LINK', '"' + data['O1']['PAIRING_WITHOUT_BLE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_PAIRING_WITHOUT_BLE_TCASE_LINK', '"' + data['O1']['PAIRING_WITHOUT_BLE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1PAIRINGSWITCH', '0', js_code)

        if "LID_OPEN_CLOSE" in data["O1"]:
            js_code = re.sub(r'O1LIDSWITCH', '1', js_code)
            js_code = re.sub(r'O1_LID_OPEN_PASSED', data['O1']['LID_OPEN_CLOSE']['Passed'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_FAILED', data['O1']['LID_OPEN_CLOSE']['Failed'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_TESTS', data['O1']['LID_OPEN_CLOSE']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_EXECTIME', '"' + data['O1']['LID_OPEN_CLOSE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_LID_OPEN_REPEATS', data['O1']['LID_OPEN_CLOSE']['Repeats'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_JIRA1_FLAG', data['O1']['LID_OPEN_CLOSE']['JiraF1'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_JIRA1', '"' + data['O1']['LID_OPEN_CLOSE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_LID_OPEN_JIRA2_FLAG', data['O1']['LID_OPEN_CLOSE']['JiraF2'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_JIRA2', '"' + data['O1']['LID_OPEN_CLOSE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_LID_OPEN_JIRA3_FLAG', data['O1']['LID_OPEN_CLOSE']['JiraF3'], js_code)
            js_code = re.sub(r'O1_LID_OPEN_JIRA3', '"' + data['O1']['LID_OPEN_CLOSE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_LID_OPEN_RESULT_LINK', '"' + data['O1']['LID_OPEN_CLOSE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_LID_OPEN_TCASE_LINK', '"' + data['O1']['LID_OPEN_CLOSE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1LIDSWITCH', '0', js_code)

        if "START_VIA_BIN_STRESS_A" in data["O1"]:
            js_code = re.sub(r'O1STARTASWITCH', '1', js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_PASSED', data['O1']['START_VIA_BIN_STRESS_A']['Passed'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_FAILED', data['O1']['START_VIA_BIN_STRESS_A']['Failed'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_TESTS', data['O1']['START_VIA_BIN_STRESS_A']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_EXECTIME', '"' + data['O1']['START_VIA_BIN_STRESS_A']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_REPEATS', data['O1']['START_VIA_BIN_STRESS_A']['Repeats'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_JIRA1_FLAG', data['O1']['START_VIA_BIN_STRESS_A']['JiraF1'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_JIRA1', '"' + data['O1']['START_VIA_BIN_STRESS_A']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_JIRA2_FLAG', data['O1']['START_VIA_BIN_STRESS_A']['JiraF2'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_JIRA2', '"' + data['O1']['START_VIA_BIN_STRESS_A']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_JIRA3_FLAG', data['O1']['START_VIA_BIN_STRESS_A']['JiraF3'], js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_JIRA3', '"' + data['O1']['START_VIA_BIN_STRESS_A']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_RESULT_LINK', '"' + data['O1']['START_VIA_BIN_STRESS_A']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_STRESS_TCASE_LINK', '"' + data['O1']['START_VIA_BIN_STRESS_A']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1STARTASWITCH', '0', js_code)

        if "START_VIA_BIN_B" in data["O1"]:
            js_code = re.sub(r'O1STARTBSWITCH', '1', js_code)
            js_code = re.sub(r'O1_START_BIN_PASSED', data['O1']['START_VIA_BIN_B']['Passed'], js_code)
            js_code = re.sub(r'O1_START_BIN_FAILED', data['O1']['START_VIA_BIN_B']['Failed'], js_code)
            js_code = re.sub(r'O1_START_BIN_TESTS', data['O1']['START_VIA_BIN_B']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_START_BIN_EXECTIME', '"' + data['O1']['START_VIA_BIN_B']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_REPEATS', data['O1']['START_VIA_BIN_B']['Repeats'], js_code)
            js_code = re.sub(r'O1_START_BIN_JIRA1_FLAG', data['O1']['START_VIA_BIN_B']['JiraF1'], js_code)
            js_code = re.sub(r'O1_START_BIN_JIRA1', '"' + data['O1']['START_VIA_BIN_B']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_JIRA2_FLAG', data['O1']['START_VIA_BIN_B']['JiraF2'], js_code)
            js_code = re.sub(r'O1_START_BIN_JIRA2', '"' + data['O1']['START_VIA_BIN_B']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_JIRA3_FLAG', data['O1']['START_VIA_BIN_B']['JiraF3'], js_code)
            js_code = re.sub(r'O1_START_BIN_JIRA3', '"' + data['O1']['START_VIA_BIN_B']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_RESULT_LINK', '"' + data['O1']['START_VIA_BIN_B']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_START_BIN_TCASE_LINK', '"' + data['O1']['START_VIA_BIN_B']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1STARTBSWITCH', '0', js_code)

        if "EEPROM_STRESS_TEST" in data["O1"]:
            js_code = re.sub(r'O1EEPROMSWITCH', '1', js_code)
            js_code = re.sub(r'O1_EEPROM_PASSED', data['O1']['EEPROM_STRESS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O1_EEPROM_FAILED', data['O1']['EEPROM_STRESS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O1_EEPROM_TESTS', data['O1']['EEPROM_STRESS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_EEPROM_EXECTIME', '"' + data['O1']['EEPROM_STRESS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_EEPROM_REPEATS', data['O1']['EEPROM_STRESS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O1_EEPROM_JIRA1_FLAG', data['O1']['EEPROM_STRESS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O1_EEPROM_JIRA1', '"' + data['O1']['EEPROM_STRESS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_EEPROM_JIRA2_FLAG', data['O1']['EEPROM_STRESS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O1_EEPROM_JIRA2', '"' + data['O1']['EEPROM_STRESS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_EEPROM_JIRA3_FLAG', data['O1']['EEPROM_STRESS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O1_EEPROM_JIRA3', '"' + data['O1']['EEPROM_STRESS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_EEPROM_RESULT_LINK', '"' + data['O1']['EEPROM_STRESS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_EEPROM_TCASE_LINK', '"' + data['O1']['EEPROM_STRESS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1EEPROMSWITCH', '0', js_code)

        if "CHILD_LOCK_STRESS_TEST" in data["O1"]:
            js_code = re.sub(r'O1CHILDASWITCH', '1', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_PASSED', data['O1']['CHILD_LOCK_STRESS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_FAILED', data['O1']['CHILD_LOCK_STRESS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_TESTS', data['O1']['CHILD_LOCK_STRESS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_EXECTIME', '"' + data['O1']['CHILD_LOCK_STRESS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_REPEATS', data['O1']['CHILD_LOCK_STRESS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_JIRA1_FLAG', data['O1']['CHILD_LOCK_STRESS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_JIRA1', '"' + data['O1']['CHILD_LOCK_STRESS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_JIRA2_FLAG', data['O1']['CHILD_LOCK_STRESS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_JIRA2', '"' + data['O1']['CHILD_LOCK_STRESS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_JIRA3_FLAG', data['O1']['CHILD_LOCK_STRESS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_JIRA3', '"' + data['O1']['CHILD_LOCK_STRESS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_RESULT_LINK', '"' + data['O1']['CHILD_LOCK_STRESS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_STRESS_TCASE_LINK', '"' + data['O1']['CHILD_LOCK_STRESS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1CHILDASWITCH', '0', js_code)

        if "CHILD_LOCK_TEST" in data["O1"]:
            js_code = re.sub(r'O1CHILDBSWITCH', '1', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_PASSED', data['O1']['CHILD_LOCK_TEST']['Passed'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_FAILED', data['O1']['CHILD_LOCK_TEST']['Failed'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_TESTS', data['O1']['CHILD_LOCK_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_EXECTIME', '"' + data['O1']['CHILD_LOCK_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_REPEATS', data['O1']['CHILD_LOCK_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_JIRA1_FLAG', data['O1']['CHILD_LOCK_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_JIRA1', '"' + data['O1']['CHILD_LOCK_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_JIRA2_FLAG', data['O1']['CHILD_LOCK_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_JIRA2', '"' + data['O1']['CHILD_LOCK_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_JIRA3_FLAG', data['O1']['CHILD_LOCK_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_JIRA3', '"' + data['O1']['CHILD_LOCK_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_RESULT_LINK', '"' + data['O1']['CHILD_LOCK_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O1_CHILD_LOCK_TCASE_LINK', '"' + data['O1']['CHILD_LOCK_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O1CHILDBSWITCH', '0', js_code)

        return js_code


    def build_structure_O2(self, js_code):
        data = json.loads(self.json_data)
        js_code = re.sub(r'O2SWITCH', '1', js_code)

        if self.rel_info_rows_O2[0][7] != "N/A" or self.rel_info_rows_O2[0][7] != "":
            js_code = re.sub(r'O2_PROD', '"' + self.rel_info_rows_O2[0][7] + '"', js_code)

        if self.rel_info_rows_O2[0][9] != "N/A" or self.rel_info_rows_O2[0][9] != "":    
            js_code = re.sub(r'O2_EXT_FT', '"' + self.rel_info_rows_O2[0][9] + '"', js_code)
        if self.rel_info_rows_O2[0][11] != "N/A" or self.rel_info_rows_O2[0][11] != "":    
            js_code = re.sub(r'O2_INT_FT', '"' + self.rel_info_rows_O2[0][11] + '"', js_code)

        if "OTA_SELF" in data["O2"]:
            js_code = re.sub(r'O2SELFSWITCH', '1', js_code)
            js_code = re.sub(r'O2_OTA_SELF_PASSED', data['O2']['OTA_SELF']['Passed'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_FAILED', data['O2']['OTA_SELF']['Failed'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_TESTS', data['O2']['OTA_SELF']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_EXECTIME', '"' + data['O2']['OTA_SELF']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_SELF_REPEATS', data['O2']['OTA_SELF']['Repeats'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_JIRA1_FLAG', data['O2']['OTA_SELF']['JiraF1'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_JIRA1', '"' + data['O2']['OTA_SELF']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_SELF_JIRA2_FLAG', data['O2']['OTA_SELF']['JiraF2'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_JIRA2', '"' + data['O2']['OTA_SELF']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_SELF_JIRA3_FLAG', data['O2']['OTA_SELF']['JiraF3'], js_code)
            js_code = re.sub(r'O2_OTA_SELF_JIRA3', '"' + data['O2']['OTA_SELF']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_SELF_RESULT_LINK', '"' + data['O2']['OTA_SELF']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_SELF_TCASE_LINK', '"' + data['O2']['OTA_SELF']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2SELFSWITCH', '0', js_code)

        if "OTA_PROD_UPGRADE" in data["O2"]:
            js_code = re.sub(r'O2PRODSWITCH', '1', js_code)
            js_code = re.sub(r'O2_OTA_PROD_PASSED', data['O2']['OTA_PROD_UPGRADE']['Passed'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_FAILED', data['O2']['OTA_PROD_UPGRADE']['Failed'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_TESTS', data['O2']['OTA_PROD_UPGRADE']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_EXECTIME', '"' + data['O2']['OTA_PROD_UPGRADE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_PROD_REPEATS', data['O2']['OTA_PROD_UPGRADE']['Repeats'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_JIRA1_FLAG', data['O2']['OTA_PROD_UPGRADE']['JiraF1'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_JIRA1', '"' + data['O2']['OTA_PROD_UPGRADE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_PROD_JIRA2_FLAG', data['O2']['OTA_PROD_UPGRADE']['JiraF2'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_JIRA2', '"' + data['O2']['OTA_PROD_UPGRADE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_PROD_JIRA3_FLAG', data['O2']['OTA_PROD_UPGRADE']['JiraF3'], js_code)
            js_code = re.sub(r'O2_OTA_PROD_JIRA3', '"' + data['O2']['OTA_PROD_UPGRADE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_PROD_RESULT_LINK', '"' + data['O2']['OTA_PROD_UPGRADE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_PROD_TCASE_LINK', '"' + data['O2']['OTA_PROD_UPGRADE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2PRODSWITCH', '0', js_code)

        if "OTA_EXT_FT_UPGRADE" in data["O2"]:
            js_code = re.sub(r'O2EXTSWITCH', '1', js_code)
            js_code = re.sub(r'O2_OTA_EXT_PASSED', data['O2']['OTA_EXT_FT_UPGRADE']['Passed'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_FAILED', data['O2']['OTA_EXT_FT_UPGRADE']['Failed'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_TESTS', data['O2']['OTA_EXT_FT_UPGRADE']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_EXECTIME', '"' + data['O2']['OTA_EXT_FT_UPGRADE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_EXT_REPEATS', data['O2']['OTA_EXT_FT_UPGRADE']['Repeats'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_JIRA1_FLAG', data['O2']['OTA_EXT_FT_UPGRADE']['JiraF1'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_JIRA1', '"' + data['O2']['OTA_EXT_FT_UPGRADE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_EXT_JIRA2_FLAG', data['O2']['OTA_EXT_FT_UPGRADE']['JiraF2'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_JIRA2', '"' + data['O2']['OTA_EXT_FT_UPGRADE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_EXT_JIRA3_FLAG', data['O2']['OTA_EXT_FT_UPGRADE']['JiraF3'], js_code)
            js_code = re.sub(r'O2_OTA_EXT_JIRA3', '"' + data['O2']['OTA_EXT_FT_UPGRADE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_EXT_RESULT_LINK', '"' + data['O2']['OTA_EXT_FT_UPGRADE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_EXT_TCASE_LINK', '"' + data['O2']['OTA_EXT_FT_UPGRADE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2EXTSWITCH', '0', js_code)

        if "OTA_INT_FT_UPGRADE" in data["O2"]:
            js_code = re.sub(r'O2INTSWITCH', '1', js_code)
            js_code = re.sub(r'O2_OTA_INT_PASSED', data['O2']['OTA_INT_FT_UPGRADE']['Passed'], js_code)
            js_code = re.sub(r'O2_OTA_INT_FAILED', data['O2']['OTA_INT_FT_UPGRADE']['Failed'], js_code)
            js_code = re.sub(r'O2_OTA_INT_TESTS', data['O2']['OTA_INT_FT_UPGRADE']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_OTA_INT_EXECTIME', '"' + data['O2']['OTA_INT_FT_UPGRADE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_INT_REPEATS', data['O2']['OTA_INT_FT_UPGRADE']['Repeats'], js_code)
            js_code = re.sub(r'O2_OTA_INT_JIRA1_FLAG', data['O2']['OTA_INT_FT_UPGRADE']['JiraF1'], js_code)
            js_code = re.sub(r'O2_OTA_INT_JIRA1', '"' + data['O2']['OTA_INT_FT_UPGRADE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_INT_JIRA2_FLAG', data['O2']['OTA_INT_FT_UPGRADE']['JiraF2'], js_code)
            js_code = re.sub(r'O2_OTA_INT_JIRA2', '"' + data['O2']['OTA_INT_FT_UPGRADE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_INT_JIRA3_FLAG', data['O2']['OTA_INT_FT_UPGRADE']['JiraF3'], js_code)
            js_code = re.sub(r'O2_OTA_INT_JIRA3', '"' + data['O2']['OTA_INT_FT_UPGRADE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_INT_RESULT_LINK', '"' + data['O2']['OTA_INT_FT_UPGRADE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_INT_TCASE_LINK', '"' + data['O2']['OTA_INT_FT_UPGRADE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2INTSWITCH', '0', js_code)

        if "POWER_DURING_OTA" in data["O2"]:
            js_code = re.sub(r'O2POWERSWITCH', '1', js_code)
            js_code = re.sub(r'O2_OTA_POWER_PASSED', data['O2']['POWER_DURING_OTA']['Passed'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_FAILED', data['O2']['POWER_DURING_OTA']['Failed'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_TESTS', data['O2']['POWER_DURING_OTA']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_EXECTIME', '"' + data['O2']['POWER_DURING_OTA']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_POWER_REPEATS', data['O2']['POWER_DURING_OTA']['Repeats'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_JIRA1_FLAG', data['O2']['POWER_DURING_OTA']['JiraF1'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_JIRA1', '"' + data['O2']['POWER_DURING_OTA']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_POWER_JIRA2_FLAG', data['O2']['POWER_DURING_OTA']['JiraF2'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_JIRA2', '"' + data['O2']['POWER_DURING_OTA']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_POWER_JIRA3_FLAG', data['O2']['POWER_DURING_OTA']['JiraF3'], js_code)
            js_code = re.sub(r'O2_OTA_POWER_JIRA3', '"' + data['O2']['POWER_DURING_OTA']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_POWER_RESULT_LINK', '"' + data['O2']['POWER_DURING_OTA']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_OTA_POWER_TCASE_LINK', '"' + data['O2']['POWER_DURING_OTA']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2POWERSWITCH', '0', js_code)

        if "DGO_IDLE_OP_PR" in data["O2"]:
            js_code = re.sub(r'O2IDLEOPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_PASSED', data['O2']['DGO_IDLE_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_FAILED', data['O2']['DGO_IDLE_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_TESTS', data['O2']['DGO_IDLE_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_EXECTIME', '"' + data['O2']['DGO_IDLE_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_REPEATS', data['O2']['DGO_IDLE_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_JIRA1_FLAG', data['O2']['DGO_IDLE_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_JIRA1', '"' + data['O2']['DGO_IDLE_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_JIRA2_FLAG', data['O2']['DGO_IDLE_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_JIRA2', '"' + data['O2']['DGO_IDLE_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_JIRA3_FLAG', data['O2']['DGO_IDLE_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_JIRA3', '"' + data['O2']['DGO_IDLE_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_RESULT_LINK', '"' + data['O2']['DGO_IDLE_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_OP_TCASE_LINK', '"' + data['O2']['DGO_IDLE_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2IDLEOPSWITCH', '0', js_code)

        if "DGO_LIP_OP_PR" in data["O2"]:
            js_code = re.sub(r'O2LIPOPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_PASSED', data['O2']['DGO_LIP_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_FAILED', data['O2']['DGO_LIP_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_TESTS', data['O2']['DGO_LIP_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_EXECTIME', '"' + data['O2']['DGO_LIP_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_REPEATS', data['O2']['DGO_LIP_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_JIRA1_FLAG', data['O2']['DGO_LIP_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_JIRA1', '"' + data['O2']['DGO_LIP_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_JIRA2_FLAG', data['O2']['DGO_LIP_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_JIRA2', '"' + data['O2']['DGO_LIP_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_JIRA3_FLAG', data['O2']['DGO_LIP_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_JIRA3', '"' + data['O2']['DGO_LIP_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_RESULT_LINK', '"' + data['O2']['DGO_LIP_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_OP_TCASE_LINK', '"' + data['O2']['DGO_LIP_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2LIPOPSWITCH', '0', js_code)

        if "DGO_HIP_OP_PR" in data["O2"]:
            js_code = re.sub(r'O2HIPOPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_PASSED', data['O2']['DGO_HIP_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_FAILED', data['O2']['DGO_HIP_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_TESTS', data['O2']['DGO_HIP_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_EXECTIME', '"' + data['O2']['DGO_HIP_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_REPEATS', data['O2']['DGO_HIP_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_JIRA1_FLAG', data['O2']['DGO_HIP_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_JIRA1', '"' + data['O2']['DGO_HIP_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_JIRA2_FLAG', data['O2']['DGO_HIP_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_JIRA2', '"' + data['O2']['DGO_HIP_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_JIRA3_FLAG', data['O2']['DGO_HIP_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_JIRA3', '"' + data['O2']['DGO_HIP_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_RESULT_LINK', '"' + data['O2']['DGO_HIP_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_OP_TCASE_LINK', '"' + data['O2']['DGO_HIP_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2HIPOPSWITCH', '0', js_code)

        if "DGO_COOLDOWN_OP_PR" in data["O2"]:
            js_code = re.sub(r'O2COOLOPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_PASSED', data['O2']['DGO_COOLDOWN_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_FAILED', data['O2']['DGO_COOLDOWN_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_TESTS', data['O2']['DGO_COOLDOWN_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_EXECTIME', '"' + data['O2']['DGO_COOLDOWN_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_REPEATS', data['O2']['DGO_COOLDOWN_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_JIRA1_FLAG', data['O2']['DGO_COOLDOWN_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_JIRA1', '"' + data['O2']['DGO_COOLDOWN_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_JIRA2_FLAG', data['O2']['DGO_COOLDOWN_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_JIRA2', '"' + data['O2']['DGO_COOLDOWN_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_JIRA3_FLAG', data['O2']['DGO_COOLDOWN_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_JIRA3', '"' + data['O2']['DGO_COOLDOWN_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_RESULT_LINK', '"' + data['O2']['DGO_COOLDOWN_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_OP_TCASE_LINK', '"' + data['O2']['DGO_COOLDOWN_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2COOLOPSWITCH', '0', js_code)

        if "DGO_FLUFF_OP_PR" in data["O2"]:
            js_code = re.sub(r'O2FLUFFOPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_PASSED', data['O2']['DGO_FLUFF_OP_PR']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_FAILED', data['O2']['DGO_FLUFF_OP_PR']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_TESTS', data['O2']['DGO_FLUFF_OP_PR']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_EXECTIME', '"' + data['O2']['DGO_FLUFF_OP_PR']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_REPEATS', data['O2']['DGO_FLUFF_OP_PR']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_JIRA1_FLAG', data['O2']['DGO_FLUFF_OP_PR']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_JIRA1', '"' + data['O2']['DGO_FLUFF_OP_PR']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_JIRA2_FLAG', data['O2']['DGO_FLUFF_OP_PR']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_JIRA2', '"' + data['O2']['DGO_FLUFF_OP_PR']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_JIRA3_FLAG', data['O2']['DGO_FLUFF_OP_PR']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_JIRA3', '"' + data['O2']['DGO_FLUFF_OP_PR']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_RESULT_LINK', '"' + data['O2']['DGO_FLUFF_OP_PR']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_OP_TCASE_LINK', '"' + data['O2']['DGO_FLUFF_OP_PR']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2FLUFFOPSWITCH', '0', js_code)


        if "DGO_IDLE_ADD_MASS" in data["O2"]:
            js_code = re.sub(r'O2IDLEMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_PASSED', data['O2']['DGO_IDLE_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_FAILED', data['O2']['DGO_IDLE_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_TESTS', data['O2']['DGO_IDLE_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_EXECTIME', '"' + data['O2']['DGO_IDLE_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_REPEATS', data['O2']['DGO_IDLE_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_JIRA1_FLAG', data['O2']['DGO_IDLE_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_JIRA1', '"' + data['O2']['DGO_IDLE_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_JIRA2_FLAG', data['O2']['DGO_IDLE_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_JIRA2', '"' + data['O2']['DGO_IDLE_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_JIRA3_FLAG', data['O2']['DGO_IDLE_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_JIRA3', '"' + data['O2']['DGO_IDLE_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_RESULT_LINK', '"' + data['O2']['DGO_IDLE_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_IDLE_MASS_TCASE_LINK', '"' + data['O2']['DGO_IDLE_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2IDLEMASSSWITCH', '0', js_code)

        if "DGO_LIP_ADD_MASS" in data["O2"]:
            js_code = re.sub(r'O2LIPMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_PASSED', data['O2']['DGO_LIP_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_FAILED', data['O2']['DGO_LIP_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_TESTS', data['O2']['DGO_LIP_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_EXECTIME', '"' + data['O2']['DGO_LIP_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_REPEATS', data['O2']['DGO_LIP_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_JIRA1_FLAG', data['O2']['DGO_LIP_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_JIRA1', '"' + data['O2']['DGO_LIP_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_JIRA2_FLAG', data['O2']['DGO_LIP_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_JIRA2', '"' + data['O2']['DGO_LIP_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_JIRA3_FLAG', data['O2']['DGO_LIP_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_JIRA3', '"' + data['O2']['DGO_LIP_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_RESULT_LINK', '"' + data['O2']['DGO_LIP_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_LIP_MASS_TCASE_LINK', '"' + data['O2']['DGO_LIP_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2LIPMASSSWITCH', '0', js_code)

        if "DGO_HIP_ADD_MASS" in data["O2"]:
            js_code = re.sub(r'O2HIPMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_PASSED', data['O2']['DGO_HIP_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_FAILED', data['O2']['DGO_HIP_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_TESTS', data['O2']['DGO_HIP_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_EXECTIME', '"' + data['O2']['DGO_HIP_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_REPEATS', data['O2']['DGO_HIP_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_JIRA1_FLAG', data['O2']['DGO_HIP_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_JIRA1', '"' + data['O2']['DGO_HIP_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_JIRA2_FLAG', data['O2']['DGO_HIP_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_JIRA2', '"' + data['O2']['DGO_HIP_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_JIRA3_FLAG', data['O2']['DGO_HIP_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_JIRA3', '"' + data['O2']['DGO_HIP_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_RESULT_LINK', '"' + data['O2']['DGO_HIP_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_HIP_MASS_TCASE_LINK', '"' + data['O2']['DGO_HIP_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2HIPMASSSWITCH', '0', js_code)

        if "DGO_COOLDOWN_ADD_MASS" in data["O2"]:
            js_code = re.sub(r'O2COOLMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_PASSED', data['O2']['DGO_COOLDOWN_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_FAILED', data['O2']['DGO_COOLDOWN_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_TESTS', data['O2']['DGO_COOLDOWN_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_EXECTIME', '"' + data['O2']['DGO_COOLDOWN_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_REPEATS', data['O2']['DGO_COOLDOWN_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_JIRA1_FLAG', data['O2']['DGO_COOLDOWN_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_JIRA1', '"' + data['O2']['DGO_COOLDOWN_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_JIRA2_FLAG', data['O2']['DGO_COOLDOWN_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_JIRA2', '"' + data['O2']['DGO_COOLDOWN_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_JIRA3_FLAG', data['O2']['DGO_COOLDOWN_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_JIRA3', '"' + data['O2']['DGO_COOLDOWN_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_RESULT_LINK', '"' + data['O2']['DGO_COOLDOWN_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_COOLDOWN_MASS_TCASE_LINK', '"' + data['O2']['DGO_COOLDOWN_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2COOLMASSSWITCH', '0', js_code)

        if "DGO_FLUFF_ADD_MASS" in data["O2"]:
            js_code = re.sub(r'O2FLUFFMASSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_PASSED', data['O2']['DGO_FLUFF_ADD_MASS']['Passed'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_FAILED', data['O2']['DGO_FLUFF_ADD_MASS']['Failed'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_TESTS', data['O2']['DGO_FLUFF_ADD_MASS']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_EXECTIME', '"' + data['O2']['DGO_FLUFF_ADD_MASS']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_REPEATS', data['O2']['DGO_FLUFF_ADD_MASS']['Repeats'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_JIRA1_FLAG', data['O2']['DGO_FLUFF_ADD_MASS']['JiraF1'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_JIRA1', '"' + data['O2']['DGO_FLUFF_ADD_MASS']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_JIRA2_FLAG', data['O2']['DGO_FLUFF_ADD_MASS']['JiraF2'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_JIRA2', '"' + data['O2']['DGO_FLUFF_ADD_MASS']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_JIRA3_FLAG', data['O2']['DGO_FLUFF_ADD_MASS']['JiraF3'], js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_JIRA3', '"' + data['O2']['DGO_FLUFF_ADD_MASS']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_RESULT_LINK', '"' + data['O2']['DGO_FLUFF_ADD_MASS']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_DGO_FLUFF_MASS_TCASE_LINK', '"' + data['O2']['DGO_FLUFF_ADD_MASS']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2FLUFFMASSSWITCH', '0', js_code)

        if "SAFETY_TEST" in data["O2"]:
            js_code = re.sub(r'O2SAFETYSWITCH', '1', js_code)
            js_code = re.sub(r'O2_SAFETY_PASSED', data['O2']['SAFETY_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_SAFETY_FAILED', data['O2']['SAFETY_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_SAFETY_TESTS', data['O2']['SAFETY_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_SAFETY_EXECTIME', '"' + data['O2']['SAFETY_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_SAFETY_REPEATS', data['O2']['SAFETY_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_SAFETY_JIRA1_FLAG', data['O2']['SAFETY_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_SAFETY_JIRA1', '"' + data['O2']['SAFETY_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_SAFETY_JIRA2_FLAG', data['O2']['SAFETY_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_SAFETY_JIRA2', '"' + data['O2']['SAFETY_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_SAFETY_JIRA3_FLAG', data['O2']['SAFETY_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_SAFETY_JIRA3', '"' + data['O2']['SAFETY_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_SAFETY_RESULT_LINK', '"' + data['O2']['SAFETY_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_SAFETY_TCASE_LINK', '"' + data['O2']['SAFETY_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2SAFETYSWITCH', '0', js_code)

        if "PAIRING_WITHOUT_BLE" in data["O2"]:
            js_code = re.sub(r'O2PAIRINGSWITCH', '1', js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_PASSED', data['O2']['PAIRING_WITHOUT_BLE']['Passed'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_FAILED', data['O2']['PAIRING_WITHOUT_BLE']['Failed'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_TESTS', data['O2']['PAIRING_WITHOUT_BLE']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_EXECTIME', '"' + data['O2']['PAIRING_WITHOUT_BLE']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_REPEATS', data['O2']['PAIRING_WITHOUT_BLE']['Repeats'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_JIRA1_FLAG', data['O2']['PAIRING_WITHOUT_BLE']['JiraF1'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_JIRA1', '"' + data['O2']['PAIRING_WITHOUT_BLE']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_JIRA2_FLAG', data['O2']['PAIRING_WITHOUT_BLE']['JiraF2'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_JIRA2', '"' + data['O2']['PAIRING_WITHOUT_BLE']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_JIRA3_FLAG', data['O2']['PAIRING_WITHOUT_BLE']['JiraF3'], js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_JIRA3', '"' + data['O2']['PAIRING_WITHOUT_BLE']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_RESULT_LINK', '"' + data['O2']['PAIRING_WITHOUT_BLE']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_PAIRING_WITHOUT_BLE_TCASE_LINK', '"' + data['O2']['PAIRING_WITHOUT_BLE']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2PAIRINGSWITCH', '0', js_code)

        if "START_VIA_BIN_STRESS_A" in data["O2"]:
            js_code = re.sub(r'O2STARTASWITCH', '1', js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_PASSED', data['O2']['START_VIA_BIN_STRESS_A']['Passed'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_FAILED', data['O2']['START_VIA_BIN_STRESS_A']['Failed'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_TESTS', data['O2']['START_VIA_BIN_STRESS_A']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_EXECTIME', '"' + data['O2']['START_VIA_BIN_STRESS_A']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_REPEATS', data['O2']['START_VIA_BIN_STRESS_A']['Repeats'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_JIRA1_FLAG', data['O2']['START_VIA_BIN_STRESS_A']['JiraF1'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_JIRA1', '"' + data['O2']['START_VIA_BIN_STRESS_A']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_JIRA2_FLAG', data['O2']['START_VIA_BIN_STRESS_A']['JiraF2'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_JIRA2', '"' + data['O2']['START_VIA_BIN_STRESS_A']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_JIRA3_FLAG', data['O2']['START_VIA_BIN_STRESS_A']['JiraF3'], js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_JIRA3', '"' + data['O2']['START_VIA_BIN_STRESS_A']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_RESULT_LINK', '"' + data['O2']['START_VIA_BIN_STRESS_A']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_STRESS_TCASE_LINK', '"' + data['O2']['START_VIA_BIN_STRESS_A']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2STARTASWITCH', '0', js_code)

        if "START_VIA_BIN_B" in data["O2"]:
            js_code = re.sub(r'O2STARTBSWITCH', '1', js_code)
            js_code = re.sub(r'O2_START_BIN_PASSED', data['O2']['START_VIA_BIN_B']['Passed'], js_code)
            js_code = re.sub(r'O2_START_BIN_FAILED', data['O2']['START_VIA_BIN_B']['Failed'], js_code)
            js_code = re.sub(r'O2_START_BIN_TESTS', data['O2']['START_VIA_BIN_B']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_START_BIN_EXECTIME', '"' + data['O2']['START_VIA_BIN_B']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_REPEATS', data['O2']['START_VIA_BIN_B']['Repeats'], js_code)
            js_code = re.sub(r'O2_START_BIN_JIRA1_FLAG', data['O2']['START_VIA_BIN_B']['JiraF1'], js_code)
            js_code = re.sub(r'O2_START_BIN_JIRA1', '"' + data['O2']['START_VIA_BIN_B']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_JIRA2_FLAG', data['O2']['START_VIA_BIN_B']['JiraF2'], js_code)
            js_code = re.sub(r'O2_START_BIN_JIRA2', '"' + data['O2']['START_VIA_BIN_B']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_JIRA3_FLAG', data['O2']['START_VIA_BIN_B']['JiraF3'], js_code)
            js_code = re.sub(r'O2_START_BIN_JIRA3', '"' + data['O2']['START_VIA_BIN_B']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_RESULT_LINK', '"' + data['O2']['START_VIA_BIN_B']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_START_BIN_TCASE_LINK', '"' + data['O2']['START_VIA_BIN_B']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2STARTBSWITCH', '0', js_code)

        if "EEPROM_STRESS_TEST" in data["O2"]:
            js_code = re.sub(r'O2EEPROMSWITCH', '1', js_code)
            js_code = re.sub(r'O2_EEPROM_PASSED', data['O2']['EEPROM_STRESS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_EEPROM_FAILED', data['O2']['EEPROM_STRESS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_EEPROM_TESTS', data['O2']['EEPROM_STRESS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_EEPROM_EXECTIME', '"' + data['O2']['EEPROM_STRESS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_EEPROM_REPEATS', data['O2']['EEPROM_STRESS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_EEPROM_JIRA1_FLAG', data['O2']['EEPROM_STRESS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_EEPROM_JIRA1', '"' + data['O2']['EEPROM_STRESS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_EEPROM_JIRA2_FLAG', data['O2']['EEPROM_STRESS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_EEPROM_JIRA2', '"' + data['O2']['EEPROM_STRESS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_EEPROM_JIRA3_FLAG', data['O2']['EEPROM_STRESS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_EEPROM_JIRA3', '"' + data['O2']['EEPROM_STRESS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_EEPROM_RESULT_LINK', '"' + data['O2']['EEPROM_STRESS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_EEPROM_TCASE_LINK', '"' + data['O2']['EEPROM_STRESS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2EEPROMSWITCH', '0', js_code)

        if "CHILD_LOCK_STRESS_TEST" in data["O2"]:
            js_code = re.sub(r'O2CHILDASWITCH', '1', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_PASSED', data['O2']['CHILD_LOCK_STRESS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_FAILED', data['O2']['CHILD_LOCK_STRESS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_TESTS', data['O2']['CHILD_LOCK_STRESS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_EXECTIME', '"' + data['O2']['CHILD_LOCK_STRESS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_REPEATS', data['O2']['CHILD_LOCK_STRESS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_JIRA1_FLAG', data['O2']['CHILD_LOCK_STRESS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_JIRA1', '"' + data['O2']['CHILD_LOCK_STRESS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_JIRA2_FLAG', data['O2']['CHILD_LOCK_STRESS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_JIRA2', '"' + data['O2']['CHILD_LOCK_STRESS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_JIRA3_FLAG', data['O2']['CHILD_LOCK_STRESS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_JIRA3', '"' + data['O2']['CHILD_LOCK_STRESS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_RESULT_LINK', '"' + data['O2']['CHILD_LOCK_STRESS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_STRESS_TCASE_LINK', '"' + data['O2']['CHILD_LOCK_STRESS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2CHILDASWITCH', '0', js_code)

        if "CHILD_LOCK_TEST" in data["O2"]:
            js_code = re.sub(r'O2CHILDBSWITCH', '1', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_PASSED', data['O2']['CHILD_LOCK_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_FAILED', data['O2']['CHILD_LOCK_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_TESTS', data['O2']['CHILD_LOCK_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_EXECTIME', '"' + data['O2']['CHILD_LOCK_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_REPEATS', data['O2']['CHILD_LOCK_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_JIRA1_FLAG', data['O2']['CHILD_LOCK_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_JIRA1', '"' + data['O2']['CHILD_LOCK_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_JIRA2_FLAG', data['O2']['CHILD_LOCK_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_JIRA2', '"' + data['O2']['CHILD_LOCK_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_JIRA3_FLAG', data['O2']['CHILD_LOCK_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_JIRA3', '"' + data['O2']['CHILD_LOCK_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_RESULT_LINK', '"' + data['O2']['CHILD_LOCK_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_CHILD_LOCK_TCASE_LINK', '"' + data['O2']['CHILD_LOCK_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2CHILDBSWITCH', '0', js_code)

        if "BOOT_CYCLE_STRESS_TEST" in data["O2"]:
            js_code = re.sub(r'O2BOOTASWITCH', '1', js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_PASSED', data['O2']['BOOT_CYCLE_STRESS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_FAILED', data['O2']['BOOT_CYCLE_STRESS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_TESTS', data['O2']['BOOT_CYCLE_STRESS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_EXECTIME', '"' + data['O2']['BOOT_CYCLE_STRESS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_REPEATS', data['O2']['BOOT_CYCLE_STRESS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_JIRA1_FLAG', data['O2']['BOOT_CYCLE_STRESS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_JIRA1', '"' + data['O2']['BOOT_CYCLE_STRESS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_JIRA2_FLAG', data['O2']['BOOT_CYCLE_STRESS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_JIRA2', '"' + data['O2']['BOOT_CYCLE_STRESS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_JIRA3_FLAG', data['O2']['BOOT_CYCLE_STRESS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_JIRA3', '"' + data['O2']['BOOT_CYCLE_STRESS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_RESULT_LINK', '"' + data['O2']['BOOT_CYCLE_STRESS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BOOT_STRESS_TCASE_LINK', '"' + data['O2']['BOOT_CYCLE_STRESS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BOOTASWITCH', '0', js_code)

        if "BAT_DGO_ADD_MASS_HIP_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_A_M_HSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_PASSED', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_FAILED', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_TESTS', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_EXECTIME', '"' + data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_REPEATS', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_JIRA1_FLAG', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_JIRA1', '"' + data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_JIRA2_FLAG', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_JIRA2', '"' + data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_JIRA3_FLAG', data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_JIRA3', '"' + data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_RESULT_LINK', '"' + data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_A_M_H_TCASE_LINK', '"' + data['O2']['BAT_DGO_ADD_MASS_HIP_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_A_M_HSWITCH', '0', js_code)

        if "BAT_DGO_RESET_HIP_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_R_HSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_PASSED', data['O2']['BAT_DGO_RESET_HIP_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_FAILED', data['O2']['BAT_DGO_RESET_HIP_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_TESTS', data['O2']['BAT_DGO_RESET_HIP_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_EXECTIME', '"' + data['O2']['BAT_DGO_RESET_HIP_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_REPEATS', data['O2']['BAT_DGO_RESET_HIP_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_JIRA1_FLAG', data['O2']['BAT_DGO_RESET_HIP_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_JIRA1', '"' + data['O2']['BAT_DGO_RESET_HIP_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_JIRA2_FLAG', data['O2']['BAT_DGO_RESET_HIP_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_JIRA2', '"' + data['O2']['BAT_DGO_RESET_HIP_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_JIRA3_FLAG', data['O2']['BAT_DGO_RESET_HIP_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_JIRA3', '"' + data['O2']['BAT_DGO_RESET_HIP_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_RESULT_LINK', '"' + data['O2']['BAT_DGO_RESET_HIP_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_R_H_TCASE_LINK', '"' + data['O2']['BAT_DGO_RESET_HIP_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_R_HSWITCH', '0', js_code)

        if "BAT_DGO_SHT40_CALIBRATION_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_S_CSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_S_C_PASSED', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_FAILED', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_TESTS', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_EXECTIME', '"' + data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_S_C_REPEATS', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_JIRA1_FLAG', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_JIRA1', '"' + data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_S_C_JIRA2_FLAG', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_JIRA2', '"' + data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_S_C_JIRA3_FLAG', data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_S_C_JIRA3', '"' + data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_S_C_RESULT_LINK', '"' + data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_S_C_TCASE_LINK', '"' + data['O2']['BAT_DGO_SHT40_CALIBRATION_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_S_CSWITCH', '0', js_code)

        if "BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_S_C_S_W_HSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_PASSED', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_FAILED', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_TESTS', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_EXECTIME', '"' + data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_REPEATS', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_JIRA1_FLAG', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_JIRA1', '"' + data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_JIRA2_FLAG', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_JIRA2', '"' + data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_JIRA3_FLAG', data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_JIRA3', '"' + data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_RESULT_LINK', '"' + data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_C_S_W_H_TCASE_LINK', '"' + data['O2']['BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_S_C_S_W_HSWITCH', '0', js_code)

        if "BAT_DGO_START_STOP_NO_VACATION_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_S_S_N_VSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_PASSED', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_FAILED', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_TESTS', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_EXECTIME', '"' + data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_REPEATS', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_JIRA1_FLAG', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_JIRA1', '"' + data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_JIRA2_FLAG', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_JIRA2', '"' + data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_JIRA3_FLAG', data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_JIRA3', '"' + data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_RESULT_LINK', '"' + data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_S_S_N_V_TCASE_LINK', '"' + data['O2']['BAT_DGO_START_STOP_NO_VACATION_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_S_S_N_VSWITCH', '0', js_code)

        if "SMOKE_PAIRING_TEST" in data["O2"]:
            js_code = re.sub(r'O2SMOKEPAIRINGSWITCH', '1', js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_PASSED', data['O2']['SMOKE_PAIRING_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_FAILED', data['O2']['SMOKE_PAIRING_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_TESTS', data['O2']['SMOKE_PAIRING_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_EXECTIME', '"' + data['O2']['SMOKE_PAIRING_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_REPEATS', data['O2']['SMOKE_PAIRING_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_JIRA1_FLAG', data['O2']['SMOKE_PAIRING_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_JIRA1', '"' + data['O2']['SMOKE_PAIRING_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_JIRA2_FLAG', data['O2']['SMOKE_PAIRING_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_JIRA2', '"' + data['O2']['SMOKE_PAIRING_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_JIRA3_FLAG', data['O2']['SMOKE_PAIRING_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_JIRA3', '"' + data['O2']['SMOKE_PAIRING_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_RESULT_LINK', '"' + data['O2']['SMOKE_PAIRING_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_PAIRING_TCASE_LINK', '"' + data['O2']['SMOKE_PAIRING_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2SMOKEPAIRINGSWITCH', '0', js_code)

        if "BAT_DGO_JAM_ERROR_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_J_ESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_PASSED', data['O2']['BAT_DGO_JAM_ERROR_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_FAILED', data['O2']['BAT_DGO_JAM_ERROR_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_TESTS', data['O2']['BAT_DGO_JAM_ERROR_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_EXECTIME', '"' + data['O2']['BAT_DGO_JAM_ERROR_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_REPEATS', data['O2']['BAT_DGO_JAM_ERROR_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_JIRA1_FLAG', data['O2']['BAT_DGO_JAM_ERROR_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_JIRA1', '"' + data['O2']['BAT_DGO_JAM_ERROR_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_JIRA2_FLAG', data['O2']['BAT_DGO_JAM_ERROR_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_JIRA2', '"' + data['O2']['BAT_DGO_JAM_ERROR_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_JIRA3_FLAG', data['O2']['BAT_DGO_JAM_ERROR_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_JIRA3', '"' + data['O2']['BAT_DGO_JAM_ERROR_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_RESULT_LINK', '"' + data['O2']['BAT_DGO_JAM_ERROR_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_E_TCASE_LINK', '"' + data['O2']['BAT_DGO_JAM_ERROR_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_J_ESWITCH', '0', js_code)

        if "BAT_DGO_JAM_INACTIVE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_J_ISWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_PASSED', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_FAILED', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_TESTS', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_EXECTIME', '"' + data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_REPEATS', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_JIRA1_FLAG', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_JIRA1', '"' + data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_JIRA2_FLAG', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_JIRA2', '"' + data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_JIRA3_FLAG', data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_JIRA3', '"' + data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_RESULT_LINK', '"' + data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_J_I_TCASE_LINK', '"' + data['O2']['BAT_DGO_JAM_INACTIVE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_J_ISWITCH', '0', js_code)

        if "BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_H_M_F_ASWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_PASSED', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_FAILED', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_TESTS', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_EXECTIME', '"' + data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_REPEATS', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_JIRA1_FLAG', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_JIRA1', '"' + data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_JIRA2_FLAG', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_JIRA2', '"' + data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_JIRA3_FLAG', data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_JIRA3', '"' + data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_RESULT_LINK', '"' + data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_M_F_A_TCASE_LINK', '"' + data['O2']['BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_H_M_F_ASWITCH', '0', js_code)

        if "BAT_DGO_HEAT_WARNING_STATUS_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_H_W_SSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_PASSED', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_FAILED', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_TESTS', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_EXECTIME', '"' + data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_REPEATS', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_JIRA1_FLAG', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_JIRA1', '"' + data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_JIRA2_FLAG', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_JIRA2', '"' + data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_JIRA3_FLAG', data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_JIRA3', '"' + data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_RESULT_LINK', '"' + data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_H_W_S_TCASE_LINK', '"' + data['O2']['BAT_DGO_HEAT_WARNING_STATUS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_H_W_SSWITCH', '0', js_code)

        if "BAT_DGO_EMPTY_BUCKET_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_E_BSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_PASSED', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_FAILED', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_TESTS', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_EXECTIME', '"' + data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_REPEATS', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_JIRA1_FLAG', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_JIRA1', '"' + data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_JIRA2_FLAG', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_JIRA2', '"' + data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_JIRA3_FLAG', data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_JIRA3', '"' + data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_RESULT_LINK', '"' + data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_E_B_TCASE_LINK', '"' + data['O2']['BAT_DGO_EMPTY_BUCKET_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_E_BSWITCH', '0', js_code)


        if "BAT_COOLDOWN_TEMP_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_COOLDOWN_TEMPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_PASSED', data['O2']['BAT_COOLDOWN_TEMP_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_FAILED', data['O2']['BAT_COOLDOWN_TEMP_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_TESTS', data['O2']['BAT_COOLDOWN_TEMP_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_EXECTIME', '"' + data['O2']['BAT_COOLDOWN_TEMP_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_REPEATS', data['O2']['BAT_COOLDOWN_TEMP_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_JIRA1_FLAG', data['O2']['BAT_COOLDOWN_TEMP_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_JIRA1', '"' + data['O2']['BAT_COOLDOWN_TEMP_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_JIRA2_FLAG', data['O2']['BAT_COOLDOWN_TEMP_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_JIRA2', '"' + data['O2']['BAT_COOLDOWN_TEMP_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_JIRA3_FLAG', data['O2']['BAT_COOLDOWN_TEMP_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_JIRA3', '"' + data['O2']['BAT_COOLDOWN_TEMP_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_RESULT_LINK', '"' + data['O2']['BAT_COOLDOWN_TEMP_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_COOLDOWN_TEMP_TCASE_LINK', '"' + data['O2']['BAT_COOLDOWN_TEMP_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_COOLDOWN_TEMPSWITCH', '0', js_code)

        if "BAT_HEAT_LED_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_HEAT_LEDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_PASSED', data['O2']['BAT_HEAT_LED_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_FAILED', data['O2']['BAT_HEAT_LED_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_TESTS', data['O2']['BAT_HEAT_LED_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_EXECTIME', '"' + data['O2']['BAT_HEAT_LED_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_REPEATS', data['O2']['BAT_HEAT_LED_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_JIRA1_FLAG', data['O2']['BAT_HEAT_LED_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_JIRA1', '"' + data['O2']['BAT_HEAT_LED_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_JIRA2_FLAG', data['O2']['BAT_HEAT_LED_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_JIRA2', '"' + data['O2']['BAT_HEAT_LED_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_JIRA3_FLAG', data['O2']['BAT_HEAT_LED_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_JIRA3', '"' + data['O2']['BAT_HEAT_LED_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_RESULT_LINK', '"' + data['O2']['BAT_HEAT_LED_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_TCASE_LINK', '"' + data['O2']['BAT_HEAT_LED_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_HEAT_LEDSWITCH', '0', js_code)

        if "BAT_PREMATURE_MASS_NO_RESET_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_PREMATURE_MASS_NO_RESETSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_PASSED', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_FAILED', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_TESTS', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_EXECTIME', '"' + data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_REPEATS', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_JIRA1_FLAG', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_JIRA1', '"' + data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_JIRA2_FLAG', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_JIRA2', '"' + data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_JIRA3_FLAG', data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_JIRA3', '"' + data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_RESULT_LINK', '"' + data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_PREMATURE_MASS_NO_RESET_TCASE_LINK', '"' + data['O2']['BAT_PREMATURE_MASS_NO_RESET_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_PREMATURE_MASS_NO_RESETSWITCH', '0', js_code)

        if "BAT_LOCKED_WHEN_HOT_SHADOWS_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_LOCKED_WHEN_HOT_SHADOWSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_PASSED', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_FAILED', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_TESTS', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_EXECTIME', '"' + data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_REPEATS', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_JIRA1_FLAG', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_JIRA1', '"' + data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_JIRA2_FLAG', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_JIRA2', '"' + data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_JIRA3_FLAG', data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_JIRA3', '"' + data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_RESULT_LINK', '"' + data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_LOCKED_WHEN_HOT_SHADOWS_TCASE_LINK', '"' + data['O2']['BAT_LOCKED_WHEN_HOT_SHADOWS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_LOCKED_WHEN_HOT_SHADOWSSWITCH', '0', js_code)

        if "SMOKE_DGO_INACTIVE_TEST" in data["O2"]:
            js_code = re.sub(r'O2SMOKE_DGO_INACTIVESWITCH', '1', js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_PASSED', data['O2']['SMOKE_DGO_INACTIVE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_FAILED', data['O2']['SMOKE_DGO_INACTIVE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_TESTS', data['O2']['SMOKE_DGO_INACTIVE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_EXECTIME', '"' + data['O2']['SMOKE_DGO_INACTIVE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_REPEATS', data['O2']['SMOKE_DGO_INACTIVE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_JIRA1_FLAG', data['O2']['SMOKE_DGO_INACTIVE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_JIRA1', '"' + data['O2']['SMOKE_DGO_INACTIVE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_JIRA2_FLAG', data['O2']['SMOKE_DGO_INACTIVE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_JIRA2', '"' + data['O2']['SMOKE_DGO_INACTIVE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_JIRA3_FLAG', data['O2']['SMOKE_DGO_INACTIVE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_JIRA3', '"' + data['O2']['SMOKE_DGO_INACTIVE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_RESULT_LINK', '"' + data['O2']['SMOKE_DGO_INACTIVE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_DGO_INACTIVE_TCASE_LINK', '"' + data['O2']['SMOKE_DGO_INACTIVE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2SMOKE_DGO_INACTIVESWITCH', '0', js_code)

        if "SMOKE_TEST_LID_TEST" in data["O2"]:
            js_code = re.sub(r'O2SMOKE_TEST_LIDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_PASSED', data['O2']['SMOKE_TEST_LID_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_FAILED', data['O2']['SMOKE_TEST_LID_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_TESTS', data['O2']['SMOKE_TEST_LID_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_EXECTIME', '"' + data['O2']['SMOKE_TEST_LID_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_REPEATS', data['O2']['SMOKE_TEST_LID_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_JIRA1_FLAG', data['O2']['SMOKE_TEST_LID_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_JIRA1', '"' + data['O2']['SMOKE_TEST_LID_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_JIRA2_FLAG', data['O2']['SMOKE_TEST_LID_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_JIRA2', '"' + data['O2']['SMOKE_TEST_LID_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_JIRA3_FLAG', data['O2']['SMOKE_TEST_LID_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_JIRA3', '"' + data['O2']['SMOKE_TEST_LID_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_RESULT_LINK', '"' + data['O2']['SMOKE_TEST_LID_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_SMOKE_TEST_LID_TCASE_LINK', '"' + data['O2']['SMOKE_TEST_LID_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2SMOKE_TEST_LIDSWITCH', '0', js_code)    





        #GUO_ADDED
        if "BAT_VACATION_CLEAN_MODE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_CLEAN_MODESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_PASSED', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_FAILED', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_TESTS', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_EXECTIME', '"' + data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_REPEATS', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_JIRA1_FLAG', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_JIRA1', '"' + data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_JIRA2_FLAG', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_JIRA2', '"' + data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_JIRA3_FLAG', data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_JIRA3', '"' + data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_RESULT_LINK', '"' + data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_CLEAN_MODE_TCASE_LINK', '"' + data['O2']['BAT_VACATION_CLEAN_MODE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_CLEAN_MODESWITCH', '0', js_code)    

        if "BAT_VACATION_ECO_MODE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_ECO_MODESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_PASSED', data['O2']['BAT_VACATION_ECO_MODE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_FAILED', data['O2']['BAT_VACATION_ECO_MODE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_TESTS', data['O2']['BAT_VACATION_ECO_MODE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_EXECTIME', '"' + data['O2']['BAT_VACATION_ECO_MODE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_REPEATS', data['O2']['BAT_VACATION_ECO_MODE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_JIRA1_FLAG', data['O2']['BAT_VACATION_ECO_MODE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_JIRA1', '"' + data['O2']['BAT_VACATION_ECO_MODE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_JIRA2_FLAG', data['O2']['BAT_VACATION_ECO_MODE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_JIRA2', '"' + data['O2']['BAT_VACATION_ECO_MODE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_JIRA3_FLAG', data['O2']['BAT_VACATION_ECO_MODE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_JIRA3', '"' + data['O2']['BAT_VACATION_ECO_MODE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_RESULT_LINK', '"' + data['O2']['BAT_VACATION_ECO_MODE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ECO_MODE_TCASE_LINK', '"' + data['O2']['BAT_VACATION_ECO_MODE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_ECO_MODESWITCH', '0', js_code)

        if "BAT_VACATION_ADD_MASS_COOLDOWN_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_ADD_MASS_COOLDOWNSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_PASSED', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_FAILED', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_TESTS', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_EXECTIME', '"' + data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_REPEATS', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_JIRA1_FLAG', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_JIRA1', '"' + data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_JIRA2_FLAG', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_JIRA2', '"' + data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_JIRA3_FLAG', data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_JIRA3', '"' + data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_RESULT_LINK', '"' + data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_ADD_MASS_COOLDOWN_TCASE_LINK', '"' + data['O2']['BAT_VACATION_ADD_MASS_COOLDOWN_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_ADD_MASS_COOLDOWNSWITCH', '0', js_code)

        if "BAT_VACATION_RESET_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_RESETSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_PASSED', data['O2']['BAT_VACATION_RESET_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_FAILED', data['O2']['BAT_VACATION_RESET_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_TESTS', data['O2']['BAT_VACATION_RESET_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_EXECTIME', '"' + data['O2']['BAT_VACATION_RESET_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_REPEATS', data['O2']['BAT_VACATION_RESET_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_JIRA1_FLAG', data['O2']['BAT_VACATION_RESET_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_JIRA1', '"' + data['O2']['BAT_VACATION_RESET_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_JIRA2_FLAG', data['O2']['BAT_VACATION_RESET_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_JIRA2', '"' + data['O2']['BAT_VACATION_RESET_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_JIRA3_FLAG', data['O2']['BAT_VACATION_RESET_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_JIRA3', '"' + data['O2']['BAT_VACATION_RESET_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_RESULT_LINK', '"' + data['O2']['BAT_VACATION_RESET_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_RESET_TCASE_LINK', '"' + data['O2']['BAT_VACATION_RESET_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_RESETSWITCH', '0', js_code)

        if "BAT_D_GRINDER_SOFT_STALL_RETRY_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_GRINDER_SOFT_STALL_RETRYSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_PASSED', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_FAILED', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_TESTS', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_EXECTIME', '"' + data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_REPEATS', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_JIRA1_FLAG', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_JIRA1', '"' + data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_JIRA2_FLAG', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_JIRA2', '"' + data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_JIRA3_FLAG', data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_JIRA3', '"' + data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_RESULT_LINK', '"' + data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_SOFT_STALL_RETRY_TCASE_LINK', '"' + data['O2']['BAT_D_GRINDER_SOFT_STALL_RETRY_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_GRINDER_SOFT_STALL_RETRYSWITCH', '0', js_code)

        if "BAT_D_GRINDER_STATE_LID_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_GRINDER_STATE_LIDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_PASSED', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_FAILED', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_TESTS', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_EXECTIME', '"' + data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_REPEATS', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_JIRA1_FLAG', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_JIRA1', '"' + data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_JIRA2_FLAG', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_JIRA2', '"' + data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_JIRA3_FLAG', data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_JIRA3', '"' + data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_RESULT_LINK', '"' + data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_STATE_LID_TCASE_LINK', '"' + data['O2']['BAT_D_GRINDER_STATE_LID_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_GRINDER_STATE_LIDSWITCH', '0', js_code)

        if "BAT_D_GRINDER_HIGH_TEMP_JAM_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_GRINDER_HIGH_TEMP_JAMSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_PASSED', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_FAILED', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_TESTS', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_EXECTIME', '"' + data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_REPEATS', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_JIRA1_FLAG', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_JIRA1', '"' + data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_JIRA2_FLAG', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_JIRA2', '"' + data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_JIRA3_FLAG', data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_JIRA3', '"' + data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_RESULT_LINK', '"' + data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_HIGH_TEMP_JAM_TCASE_LINK', '"' + data['O2']['BAT_D_GRINDER_HIGH_TEMP_JAM_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_GRINDER_HIGH_TEMP_JAMSWITCH', '0', js_code)

        if "BAT_D_GRINDER_JAM_AUTO_RETRY_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_GRINDER_JAM_AUTO_RETRYSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_PASSED', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_FAILED', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_TESTS', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_EXECTIME', '"' + data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_REPEATS', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_JIRA1_FLAG', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_JIRA1', '"' + data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_JIRA2_FLAG', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_JIRA2', '"' + data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_JIRA3_FLAG', data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_JIRA3', '"' + data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_RESULT_LINK', '"' + data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_GRINDER_JAM_AUTO_RETRY_TCASE_LINK', '"' + data['O2']['BAT_D_GRINDER_JAM_AUTO_RETRY_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_GRINDER_JAM_AUTO_RETRYSWITCH', '0', js_code)

        if "BAT_D_FLUFF_NOT_RUN_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_FLUFF_NOT_RUNSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_PASSED', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_FAILED', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_TESTS', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_EXECTIME', '"' + data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_REPEATS', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_JIRA1_FLAG', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_JIRA1', '"' + data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_JIRA2_FLAG', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_JIRA2', '"' + data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_JIRA3_FLAG', data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_JIRA3', '"' + data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_RESULT_LINK', '"' + data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FLUFF_NOT_RUN_TCASE_LINK', '"' + data['O2']['BAT_D_FLUFF_NOT_RUN_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_FLUFF_NOT_RUNSWITCH', '0', js_code)

        if "BAT_SET_START_TIME_DURING_HIP_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_SET_START_TIME_DURING_HIPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_PASSED', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_FAILED', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_TESTS', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_EXECTIME', '"' + data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_REPEATS', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_JIRA1_FLAG', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_JIRA1', '"' + data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_JIRA2_FLAG', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_JIRA2', '"' + data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_JIRA3_FLAG', data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_JIRA3', '"' + data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_RESULT_LINK', '"' + data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_SET_START_TIME_DURING_HIP_TCASE_LINK', '"' + data['O2']['BAT_SET_START_TIME_DURING_HIP_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_SET_START_TIME_DURING_HIPSWITCH', '0', js_code)


        if "BAT_RESUME_FROM_LIP_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_RESUME_FROM_LIPSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_PASSED', data['O2']['BAT_RESUME_FROM_LIP_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_FAILED', data['O2']['BAT_RESUME_FROM_LIP_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_TESTS', data['O2']['BAT_RESUME_FROM_LIP_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_EXECTIME', '"' + data['O2']['BAT_RESUME_FROM_LIP_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_REPEATS', data['O2']['BAT_RESUME_FROM_LIP_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_JIRA1_FLAG', data['O2']['BAT_RESUME_FROM_LIP_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_JIRA1', '"' + data['O2']['BAT_RESUME_FROM_LIP_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_JIRA2_FLAG', data['O2']['BAT_RESUME_FROM_LIP_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_JIRA2', '"' + data['O2']['BAT_RESUME_FROM_LIP_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_JIRA3_FLAG', data['O2']['BAT_RESUME_FROM_LIP_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_JIRA3', '"' + data['O2']['BAT_RESUME_FROM_LIP_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_RESULT_LINK', '"' + data['O2']['BAT_RESUME_FROM_LIP_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_FROM_LIP_TCASE_LINK', '"' + data['O2']['BAT_RESUME_FROM_LIP_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_RESUME_FROM_LIPSWITCH', '0', js_code)

        if "BAT_D_ALWAYS_LOCKED_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_ALWAYS_LOCKEDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_PASSED', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_FAILED', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_TESTS', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_EXECTIME', '"' + data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_REPEATS', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_JIRA1_FLAG', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_JIRA1', '"' + data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_JIRA2_FLAG', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_JIRA2', '"' + data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_JIRA3_FLAG', data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_JIRA3', '"' + data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_RESULT_LINK', '"' + data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_LOCKED_TCASE_LINK', '"' + data['O2']['BAT_D_ALWAYS_LOCKED_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_ALWAYS_LOCKEDSWITCH', '0', js_code)

        if "BAT_D_ALWAYS_UNLOCKED_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_ALWAYS_UNLOCKEDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_PASSED', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_FAILED', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_TESTS', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_EXECTIME', '"' + data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_REPEATS', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_JIRA1_FLAG', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_JIRA1', '"' + data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_JIRA2_FLAG', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_JIRA2', '"' + data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_JIRA3_FLAG', data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_JIRA3', '"' + data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_RESULT_LINK', '"' + data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_ALWAYS_UNLOCKED_TCASE_LINK', '"' + data['O2']['BAT_D_ALWAYS_UNLOCKED_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_ALWAYS_UNLOCKEDSWITCH', '0', js_code)

        if "BAT_D_BUCKET_FULLNESS_LOW_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_BUCKET_FULLNESS_LOWSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_PASSED', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_FAILED', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_TESTS', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_EXECTIME', '"' + data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_REPEATS', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_JIRA1_FLAG', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_JIRA1', '"' + data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_JIRA2_FLAG', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_JIRA2', '"' + data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_JIRA3_FLAG', data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_JIRA3', '"' + data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_RESULT_LINK', '"' + data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_BUCKET_FULLNESS_LOW_TCASE_LINK', '"' + data['O2']['BAT_D_BUCKET_FULLNESS_LOW_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_BUCKET_FULLNESS_LOWSWITCH', '0', js_code)

        if "BAT_DELTA_MR_HIP_MASS_BUCKET_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_DELTA_MR_HIP_MASS_BUCKETSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_PASSED', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_FAILED', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_TESTS', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_EXECTIME', '"' + data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_REPEATS', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_JIRA1_FLAG', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_JIRA1', '"' + data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_JIRA2_FLAG', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_JIRA2', '"' + data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_JIRA3_FLAG', data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_JIRA3', '"' + data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_RESULT_LINK', '"' + data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_DELTA_MR_HIP_MASS_BUCKET_TCASE_LINK', '"' + data['O2']['BAT_DELTA_MR_HIP_MASS_BUCKET_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_DELTA_MR_HIP_MASS_BUCKETSWITCH', '0', js_code)

        if "BAT_D_LOCKED_WHEN_RUNNING_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_LOCKED_WHEN_RUNNINGSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_PASSED', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_FAILED', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_TESTS', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_EXECTIME', '"' + data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_REPEATS', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_JIRA1_FLAG', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_JIRA1', '"' + data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_JIRA2_FLAG', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_JIRA2', '"' + data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_JIRA3_FLAG', data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_JIRA3', '"' + data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_RESULT_LINK', '"' + data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LOCKED_WHEN_RUNNING_TCASE_LINK', '"' + data['O2']['BAT_D_LOCKED_WHEN_RUNNING_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_LOCKED_WHEN_RUNNINGSWITCH', '0', js_code)

        if "BAT_D_FR_HEAT_WARNING_STATUS_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_FR_HEAT_WARNING_STATUSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_PASSED', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_FAILED', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_TESTS', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_EXECTIME', '"' + data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_REPEATS', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_JIRA1_FLAG', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_JIRA1', '"' + data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_JIRA2_FLAG', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_JIRA2', '"' + data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_JIRA3_FLAG', data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_JIRA3', '"' + data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_RESULT_LINK', '"' + data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_FR_HEAT_WARNING_STATUS_TCASE_LINK', '"' + data['O2']['BAT_D_FR_HEAT_WARNING_STATUS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_FR_HEAT_WARNING_STATUSSWITCH', '0', js_code)

        if "BAT_D_MASS_NO_CHANGE_RESET_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_MASS_NO_CHANGE_RESETSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_PASSED', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_FAILED', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_TESTS', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_EXECTIME', '"' + data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_REPEATS', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_JIRA1_FLAG', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_JIRA1', '"' + data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_JIRA2_FLAG', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_JIRA2', '"' + data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_JIRA3_FLAG', data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_JIRA3', '"' + data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_RESULT_LINK', '"' + data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_NO_CHANGE_RESET_TCASE_LINK', '"' + data['O2']['BAT_D_MASS_NO_CHANGE_RESET_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_MASS_NO_CHANGE_RESETSWITCH', '0', js_code)

        if "BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_LASTDGOCYCLE_ENERGY_SHADOWSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_PASSED', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_FAILED', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TESTS', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_EXECTIME', '"' + data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_REPEATS', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_JIRA1_FLAG', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_JIRA1', '"' + data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_JIRA2_FLAG', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_JIRA2', '"' + data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_JIRA3_FLAG', data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_JIRA3', '"' + data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_RESULT_LINK', '"' + data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TCASE_LINK', '"' + data['O2']['BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_LASTDGOCYCLE_ENERGY_SHADOWSSWITCH', '0', js_code)

        if "BAT_D_CYCLEENDTIME_LID_OPEN_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_CYCLEENDTIME_LID_OPENSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_PASSED', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_FAILED', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_TESTS', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_EXECTIME', '"' + data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_REPEATS', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_JIRA1_FLAG', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_JIRA1', '"' + data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_JIRA2_FLAG', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_JIRA2', '"' + data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_JIRA3_FLAG', data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_JIRA3', '"' + data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_RESULT_LINK', '"' + data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_CYCLEENDTIME_LID_OPEN_TCASE_LINK', '"' + data['O2']['BAT_D_CYCLEENDTIME_LID_OPEN_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_CYCLEENDTIME_LID_OPENSWITCH', '0', js_code)

        if "BAT_D_UNPROCESSED_MASS_ZERO_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_UNPROCESSED_MASS_ZEROSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_PASSED', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_FAILED', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_TESTS', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_EXECTIME', '"' + data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_REPEATS', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_JIRA1_FLAG', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_JIRA1', '"' + data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_JIRA2_FLAG', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_JIRA2', '"' + data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_JIRA3_FLAG', data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_JIRA3', '"' + data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_RESULT_LINK', '"' + data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_UNPROCESSED_MASS_ZERO_TCASE_LINK', '"' + data['O2']['BAT_D_UNPROCESSED_MASS_ZERO_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_UNPROCESSED_MASS_ZEROSWITCH', '0', js_code)

        if "BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_MASS_ADD_LID_OPEN_CLOSESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_PASSED', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_FAILED', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_TESTS', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_EXECTIME', '"' + data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_REPEATS', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_JIRA1_FLAG', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_JIRA1', '"' + data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_JIRA2_FLAG', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_JIRA2', '"' + data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_JIRA3_FLAG', data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_JIRA3', '"' + data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_RESULT_LINK', '"' + data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_MASS_ADD_LID_OPEN_CLOSE_TCASE_LINK', '"' + data['O2']['BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_MASS_ADD_LID_OPEN_CLOSESWITCH', '0', js_code)

        if "BAT_D_LIP_SKIPPED_HOT_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_D_LIP_SKIPPED_HOTSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_PASSED', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_FAILED', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_TESTS', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_EXECTIME', '"' + data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_REPEATS', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_JIRA1_FLAG', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_JIRA1', '"' + data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_JIRA2_FLAG', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_JIRA2', '"' + data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_JIRA3_FLAG', data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_JIRA3', '"' + data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_RESULT_LINK', '"' + data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_D_LIP_SKIPPED_HOT_TCASE_LINK', '"' + data['O2']['BAT_D_LIP_SKIPPED_HOT_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_D_LIP_SKIPPED_HOTSWITCH', '0', js_code)




        # 8/12/2024

        if "BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_HIP_EXTENSION_LID_OPEN_CLOSESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_PASSED', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_FAILED', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TESTS', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_EXECTIME', '"' + data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_REPEATS', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_JIRA1_FLAG', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_JIRA1', '"' + data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_JIRA2_FLAG', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_JIRA2', '"' + data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_JIRA3_FLAG', data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_JIRA3', '"' + data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_RESULT_LINK', '"' + data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TCASE_LINK', '"' + data['O2']['BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_HIP_EXTENSION_LID_OPEN_CLOSESWITCH', '0', js_code)

        if "BAT_START_DISCONNECTED_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_START_DISCONNECTEDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_PASSED', data['O2']['BAT_START_DISCONNECTED_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_FAILED', data['O2']['BAT_START_DISCONNECTED_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_TESTS', data['O2']['BAT_START_DISCONNECTED_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_EXECTIME', '"' + data['O2']['BAT_START_DISCONNECTED_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_REPEATS', data['O2']['BAT_START_DISCONNECTED_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_JIRA1_FLAG', data['O2']['BAT_START_DISCONNECTED_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_JIRA1', '"' + data['O2']['BAT_START_DISCONNECTED_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_JIRA2_FLAG', data['O2']['BAT_START_DISCONNECTED_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_JIRA2', '"' + data['O2']['BAT_START_DISCONNECTED_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_JIRA3_FLAG', data['O2']['BAT_START_DISCONNECTED_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_JIRA3', '"' + data['O2']['BAT_START_DISCONNECTED_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_RESULT_LINK', '"' + data['O2']['BAT_START_DISCONNECTED_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_START_DISCONNECTED_TCASE_LINK', '"' + data['O2']['BAT_START_DISCONNECTED_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_START_DISCONNECTEDSWITCH', '0', js_code)

        if "BAT_RESUME_DISCONNECTED_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_RESUME_DISCONNECTEDSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_PASSED', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_FAILED', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_TESTS', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_EXECTIME', '"' + data['O2']['BAT_RESUME_DISCONNECTED_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_REPEATS', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_JIRA1_FLAG', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_JIRA1', '"' + data['O2']['BAT_RESUME_DISCONNECTED_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_JIRA2_FLAG', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_JIRA2', '"' + data['O2']['BAT_RESUME_DISCONNECTED_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_JIRA3_FLAG', data['O2']['BAT_RESUME_DISCONNECTED_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_JIRA3', '"' + data['O2']['BAT_RESUME_DISCONNECTED_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_RESULT_LINK', '"' + data['O2']['BAT_RESUME_DISCONNECTED_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_DISCONNECTED_TCASE_LINK', '"' + data['O2']['BAT_RESUME_DISCONNECTED_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_RESUME_DISCONNECTEDSWITCH', '0', js_code)

        if "BAT_HEAT_LED_INTERRUPTIONS_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_HEAT_LED_INTERRUPTIONSSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_PASSED', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_FAILED', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_TESTS', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_EXECTIME', '"' + data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_REPEATS', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_JIRA1_FLAG', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_JIRA1', '"' + data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_JIRA2_FLAG', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_JIRA2', '"' + data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_JIRA3_FLAG', data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_JIRA3', '"' + data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_RESULT_LINK', '"' + data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_HEAT_LED_INTERRUPTIONS_TCASE_LINK', '"' + data['O2']['BAT_HEAT_LED_INTERRUPTIONS_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_HEAT_LED_INTERRUPTIONSSWITCH', '0', js_code)


        if "BAT_VACATION_AFTER_EMPTY_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_AFTER_EMPTYSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_PASSED', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_FAILED', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_TESTS', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_EXECTIME', '"' + data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_REPEATS', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_JIRA1_FLAG', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_JIRA1', '"' + data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_JIRA2_FLAG', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_JIRA2', '"' + data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_JIRA3_FLAG', data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_JIRA3', '"' + data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_RESULT_LINK', '"' + data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_AFTER_EMPTY_TCASE_LINK', '"' + data['O2']['BAT_VACATION_AFTER_EMPTY_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_AFTER_EMPTYSWITCH', '0', js_code)


        if "BAT_RESUME_COOLDOWN_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_RESUME_COOLDOWNSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_PASSED', data['O2']['BAT_RESUME_COOLDOWN_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_FAILED', data['O2']['BAT_RESUME_COOLDOWN_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_TESTS', data['O2']['BAT_RESUME_COOLDOWN_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_EXECTIME', '"' + data['O2']['BAT_RESUME_COOLDOWN_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_REPEATS', data['O2']['BAT_RESUME_COOLDOWN_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_JIRA1_FLAG', data['O2']['BAT_RESUME_COOLDOWN_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_JIRA1', '"' + data['O2']['BAT_RESUME_COOLDOWN_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_JIRA2_FLAG', data['O2']['BAT_RESUME_COOLDOWN_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_JIRA2', '"' + data['O2']['BAT_RESUME_COOLDOWN_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_JIRA3_FLAG', data['O2']['BAT_RESUME_COOLDOWN_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_JIRA3', '"' + data['O2']['BAT_RESUME_COOLDOWN_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_RESULT_LINK', '"' + data['O2']['BAT_RESUME_COOLDOWN_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_RESUME_COOLDOWN_TCASE_LINK', '"' + data['O2']['BAT_RESUME_COOLDOWN_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_RESUME_COOLDOWNSWITCH', '0', js_code)





        # 9/4/2024 
        if "BAT_VACATION_OTA_PRE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_OTA_PRESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_PASSED', data['O2']['BAT_VACATION_OTA_PRE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_FAILED', data['O2']['BAT_VACATION_OTA_PRE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_TESTS', data['O2']['BAT_VACATION_OTA_PRE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_EXECTIME', '"' + data['O2']['BAT_VACATION_OTA_PRE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_REPEATS', data['O2']['BAT_VACATION_OTA_PRE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_JIRA1_FLAG', data['O2']['BAT_VACATION_OTA_PRE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_JIRA1', '"' + data['O2']['BAT_VACATION_OTA_PRE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_JIRA2_FLAG', data['O2']['BAT_VACATION_OTA_PRE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_JIRA2', '"' + data['O2']['BAT_VACATION_OTA_PRE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_JIRA3_FLAG', data['O2']['BAT_VACATION_OTA_PRE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_JIRA3', '"' + data['O2']['BAT_VACATION_OTA_PRE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_RESULT_LINK', '"' + data['O2']['BAT_VACATION_OTA_PRE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_PRE_TCASE_LINK', '"' + data['O2']['BAT_VACATION_OTA_PRE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_OTA_PRESWITCH', '0', js_code)

        if "BAT_VACATION_OTA_POST_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_VACATION_OTA_POSTSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_PASSED', data['O2']['BAT_VACATION_OTA_POST_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_FAILED', data['O2']['BAT_VACATION_OTA_POST_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_TESTS', data['O2']['BAT_VACATION_OTA_POST_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_EXECTIME', '"' + data['O2']['BAT_VACATION_OTA_POST_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_REPEATS', data['O2']['BAT_VACATION_OTA_POST_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_JIRA1_FLAG', data['O2']['BAT_VACATION_OTA_POST_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_JIRA1', '"' + data['O2']['BAT_VACATION_OTA_POST_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_JIRA2_FLAG', data['O2']['BAT_VACATION_OTA_POST_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_JIRA2', '"' + data['O2']['BAT_VACATION_OTA_POST_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_JIRA3_FLAG', data['O2']['BAT_VACATION_OTA_POST_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_JIRA3', '"' + data['O2']['BAT_VACATION_OTA_POST_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_RESULT_LINK', '"' + data['O2']['BAT_VACATION_OTA_POST_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_VACATION_OTA_POST_TCASE_LINK', '"' + data['O2']['BAT_VACATION_OTA_POST_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_VACATION_OTA_POSTSWITCH', '0', js_code)

        if "BAT_BUCKET_CRASH_OTA_PRE_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_BUCKET_CRASH_OTA_PRESWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_PASSED', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_FAILED', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_TESTS', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_EXECTIME', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_REPEATS', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_JIRA1_FLAG', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_JIRA1', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_JIRA2_FLAG', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_JIRA2', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_JIRA3_FLAG', data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_JIRA3', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_RESULT_LINK', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_PRE_TCASE_LINK', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_PRE_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_BUCKET_CRASH_OTA_PRESWITCH', '0', js_code)

        if "BAT_BUCKET_CRASH_OTA_POST_TEST" in data["O2"]:
            js_code = re.sub(r'O2BAT_BUCKET_CRASH_OTA_POSTSWITCH', '1', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_PASSED', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['Passed'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_FAILED', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['Failed'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_TESTS', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['TestExecuted'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_EXECTIME', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['ExeTime'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_REPEATS', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['Repeats'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_JIRA1_FLAG', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['JiraF1'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_JIRA1', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['Jira1'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_JIRA2_FLAG', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['JiraF2'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_JIRA2', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['Jira2'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_JIRA3_FLAG', data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['JiraF3'], js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_JIRA3', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['Jira3'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_RESULT_LINK', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['ResultLink'] + '"', js_code)
            js_code = re.sub(r'O2_BAT_BUCKET_CRASH_OTA_POST_TCASE_LINK', '"' + data['O2']['BAT_BUCKET_CRASH_OTA_POST_TEST']['TestCasesLink'] + '"', js_code)
        else:
            js_code = re.sub(r'O2BAT_BUCKET_CRASH_OTA_POSTSWITCH', '0', js_code)




        return js_code

    def convertSQL(self, line, placeholder, replacement):
        try:
            pattern = re.escape(placeholder)
            line = re.sub(pattern, replacement, line)
        except Exception as e:
            print(f"Exception in converting SQL: {e}")    
        return line


    def prepareDashHTML(self, curBuild_O1, curBuild_O2, htmlName, fMDash=True):

        with open(htmlName, 'r', encoding='utf-8') as file:
            fileCT = file.read()
            if curBuild_O1 and curBuild_O2:
                updatedCT = fileCT.replace('<o1sw_open/>', '')
                updatedCT = updatedCT.replace('<o1sw_close/>', '')
                updatedCT = updatedCT.replace('<o2sw_open/>', '')
                updatedCT = updatedCT.replace('<o2sw_close/>', '')
            elif curBuild_O1:
                updatedCT = fileCT.replace('<o1sw_open></o1sw_open>', '')
                updatedCT = updatedCT.replace('<o1sw_close></o1sw_close>', '')
                updatedCT = updatedCT.replace('<o2sw_open></o2sw_open>', '<!--')
                updatedCT = updatedCT.replace('<o2sw_close></o2sw_close>', '-->')
            elif curBuild_O2:
                updatedCT = fileCT.replace('<o1sw_open></o1sw_open>', '<!--')
                updatedCT = updatedCT.replace('<o1sw_close></o1sw_close>', '-->')
                updatedCT = updatedCT.replace('<o2sw_open></o2sw_open>', '')
                updatedCT = updatedCT.replace('<o2sw_close></o2sw_close>', '')

            fObject = io.StringIO(updatedCT)
            soup = BeautifulSoup(fObject, 'lxml')

        script_tag = soup.find('script')

        if fMDash:
            if script_tag:
                js_code = script_tag.string
                js_code = re.sub(r'GET_M_DATA', self.json_data, js_code)
                script_tag.string = js_code
        else:
            if script_tag:
                js_code = script_tag.string
                if curBuild_O1 and curBuild_O2:
                    js_code = re.sub(r'O1_BUILT_DATE', '"' + self.rel_info_rows[0][2] + '"', js_code)
                    js_code = re.sub(r'O1_TEMPLATE', '"' + self.rel_info_rows[0][3] + '"', js_code)
                    js_code = re.sub(r'O1_BUILD', '"' + self.rel_info_rows[0][4] + '"', js_code)
                    js_code = re.sub(r'O1_CODE', '"' + self.rel_info_rows[0][5] + '"', js_code)
                    js_code = self.build_structure_O1(js_code)
                    js_code = self.build_structure_O2(js_code)
                elif curBuild_O1:
                    js_code = re.sub(r'O1_BUILT_DATE', '"' + self.rel_info_rows[0][2] + '"', js_code)
                    js_code = re.sub(r'O1_TEMPLATE', '"' + self.rel_info_rows[0][3] + '"', js_code)
                    js_code = re.sub(r'O1_BUILD', '"' + self.rel_info_rows[0][4] + '"', js_code)
                    js_code = re.sub(r'O1_CODE', '"' + self.rel_info_rows[0][5] + '"', js_code)
                    js_code = self.build_structure_O1(js_code)
                    js_code = re.sub(r'O2SWITCH', '0', js_code)
                elif curBuild_O2:
                    js_code = re.sub(r'O1_BUILT_DATE', '"' + self.rel_info_rows_O2[0][2] + '"', js_code)
                    js_code = re.sub(r'O1_TEMPLATE', '"' + self.rel_info_rows_O2[0][3] + '"', js_code)
                    js_code = re.sub(r'O1_BUILD', '"' + self.rel_info_rows_O2[0][4] + '"', js_code)
                    js_code = re.sub(r'O1_CODE', '"' + self.rel_info_rows_O2[0][5] + '"', js_code)
                    js_code = re.sub(r'O1SWITCH', '0', js_code)
                    js_code = self.build_structure_O2(js_code)
                   
                script_tag.string = js_code

        with open(htmlName, 'w') as file:
            file.write(str(soup))

        print(f'HTML file "{htmlName}" has been generated.')


    def generateHTMLPages(self, pageT, curBuild_O1, curBuild_O2, curBuildHtml=None):
        # print("curBuild_O1= ", curBuild_O1)
        # print("curBuild_O2= ", curBuild_O2)
        # print("curBuildHtml= ", curBuildHtml)
    
        if pageT == "main":
            self.convertNPrepareDataJson(curBuild_O1, curBuild_O2, 'dashboards.html', 'm_dash_t.html', 'm_dash_t_data.json', True, False)

            self.prepareDashHTML(curBuild_O1, curBuild_O2, 'dashboards.html')
        else:
            self.convertNPrepareDataJson(curBuild_O1, curBuild_O2, curBuildHtml, 'details_t.html', 'detail_t_data.json', False, True)

            self.prepareDashHTML(curBuild_O1, curBuild_O2, curBuildHtml, False)


    def queryMainReportTable(self):
        self.queryReportTable(sqlsDash.report_q)



    def queryTables_O1(self, curBuild_O1, curBuild_O1_B):
        self.queryCurShippedBuilds(self.convertSQL(sqlsDash.ota_o1_self_q, '[curBuild_O1]', curBuild_O1))

        self.query_release_info_by_build(curBuild_O1, "O1")

        self.queryOTASelfTable2(self.convertSQL(sqlsDash.ota_o1_self_q, '[curBuild_O1]', curBuild_O1))

        sqlRun = self.convertSQL(sqlsDash.ota_o1_prod_q, '[curBuild_O1]', curBuild_O1)
        self.queryTable(sqlRun, 'OTA_PROD_UPGRADE')

        sqlRun = self.convertSQL(sqlsDash.ota_o1_ext_q, '[curBuild_O1]', curBuild_O1)
        self.queryTable(sqlRun, 'OTA_EXT_FT_UPGRADE')

        sqlRun = self.convertSQL(sqlsDash.ota_o1_int_q, '[curBuild_O1]', curBuild_O1)
        self.queryTable(sqlRun, 'OTA_INT_FT_UPGRADE')

        sqlRun = self.convertSQL(sqlsDash.power_o1_q, '[curBuild_O1]', curBuild_O1)
        self.queryTable(sqlRun, 'POWER_DURING_OTA')

        sqlRun = self.convertSQL(sqlsDash.dgo_op_idle_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_IDLE_OP_PR')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_lip_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_LIP_OP_PR')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_hip_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_HIP_OP_PR')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_cool_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_COOLDOWN_OP_PR')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_fluff_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_FLUFF_OP_PR')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_idle_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_IDLE_ADD_MASS')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_lip_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_LIP_ADD_MASS')
       
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_hip_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_HIP_ADD_MASS')
       
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_cool_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_COOLDOWN_ADD_MASS')
        
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_fluff_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'DGO_FLUFF_ADD_MASS')    
        
        sqlRun = self.convertSQL(sqlsDash.safety_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'SAFETY_TEST')
        
        sqlRun = self.convertSQL(sqlsDash.pairing_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'PAIRING_WITHOUT_BLE')

        sqlRun = self.convertSQL(sqlsDash.lid_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'LID_OPEN_CLOSE')
        
        sqlRun = self.convertSQL(sqlsDash.start_a_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'START_VIA_BIN_STRESS_A')
        
        sqlRun = self.convertSQL(sqlsDash.start_b_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'START_VIA_BIN_B')    
        
        sqlRun = self.convertSQL(sqlsDash.eeprom_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'EEPROM_STRESS_TEST')
        
        sqlRun = self.convertSQL(sqlsDash.child_a_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'CHILD_LOCK_STRESS_TEST')
        
        sqlRun = self.convertSQL(sqlsDash.child_b_o1_q, '[curBuild_O1_B]', curBuild_O1_B)
        self.queryTable(sqlRun, 'CHILD_LOCK_TEST')


    def queryTables_O2(self, curBuild_O2, curBuild_O2_B):
        self.queryCurShippedBuilds(self.convertSQL(sqlsDash.ota_o2_self_q, '[curBuild_O2]', curBuild_O2), False)

        self.query_release_info_by_build(curBuild_O2, "O2")

        self.queryOTASelfTable2(self.convertSQL(sqlsDash.ota_o2_self_q, '[curBuild_O2]', curBuild_O2), False)

        sqlRun = self.convertSQL(sqlsDash.ota_o2_prod_q, '[curBuild_O2]', curBuild_O2)
        self.queryTable(sqlRun, 'OTA_PROD_UPGRADE', False)

        sqlRun = self.convertSQL(sqlsDash.ota_o2_ext_q, '[curBuild_O2]', curBuild_O2)
        self.queryTable(sqlRun, 'OTA_EXT_FT_UPGRADE', False)

        sqlRun = self.convertSQL(sqlsDash.ota_o2_int_q, '[curBuild_O2]', curBuild_O2)
        self.queryTable(sqlRun, 'OTA_INT_FT_UPGRADE', False)

        sqlRun = self.convertSQL(sqlsDash.power_o2_q, '[curBuild_O2]', curBuild_O2)
        self.queryTable(sqlRun, 'POWER_DURING_OTA', False)

        sqlRun = self.convertSQL(sqlsDash.dgo_op_idle_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_IDLE_OP_PR', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_lip_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_LIP_OP_PR', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_hip_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_HIP_OP_PR', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_cool_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_COOLDOWN_OP_PR', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_op_fluff_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_FLUFF_OP_PR', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_idle_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_IDLE_ADD_MASS', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_lip_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_LIP_ADD_MASS', False)
       
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_hip_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_HIP_ADD_MASS', False)
       
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_cool_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_COOLDOWN_ADD_MASS', False)
        
        sqlRun = self.convertSQL(sqlsDash.dgo_mass_fluff_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'DGO_FLUFF_ADD_MASS', False)    
        
        sqlRun = self.convertSQL(sqlsDash.safety_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'SAFETY_TEST', False)
        
        sqlRun = self.convertSQL(sqlsDash.pairing_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'PAIRING_WITHOUT_BLE', False)

        sqlRun = self.convertSQL(sqlsDash.start_a_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'START_VIA_BIN_STRESS_A', False)
        
        sqlRun = self.convertSQL(sqlsDash.start_b_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'START_VIA_BIN_B', False)    
        
        sqlRun = self.convertSQL(sqlsDash.eeprom_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'EEPROM_STRESS_TEST', False)
        
        sqlRun = self.convertSQL(sqlsDash.child_a_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'CHILD_LOCK_STRESS_TEST', False)
        
        sqlRun = self.convertSQL(sqlsDash.child_b_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'CHILD_LOCK_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.boot_a_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BOOT_CYCLE_STRESS_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_a_m_h_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_ADD_MASS_HIP_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_r_h_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_RESET_HIP_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_s_c_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_SHT40_CALIBRATION_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_s_c_s_w_h_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_SHT40_CAL_SKIP_WHEN_HOT_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_s_s_n_v_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_START_STOP_NO_VACATION_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.smoke_pairing_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'SMOKE_PAIRING_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_j_e_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_JAM_ERROR_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_j_i_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_JAM_INACTIVE_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_h_m_f_a_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_HIP_MOISTURE_FOOD_ADD_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_h_w_s_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_HEAT_WARNING_STATUS_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_e_b_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DGO_EMPTY_BUCKET_TEST', False)


        sqlRun = self.convertSQL(sqlsDash.bat_cooldown_temp_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_COOLDOWN_TEMP_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_heat_led_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_HEAT_LED_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_premature_mass_no_reset_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_PREMATURE_MASS_NO_RESET_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_locked_when_hot_shadows_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_LOCKED_WHEN_HOT_SHADOWS_TEST', False)


        sqlRun = self.convertSQL(sqlsDash.smoke_dgo_inactive_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'SMOKE_DGO_INACTIVE_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.smoke_test_lid_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'SMOKE_TEST_LID_TEST', False)



        #GUO_ADDED
        sqlRun = self.convertSQL(sqlsDash.bat_vacation_clean_mode_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_CLEAN_MODE_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_vacation_eco_mode_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_ECO_MODE_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_vacation_add_mass_cooldown_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_ADD_MASS_COOLDOWN_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_vacation_reset_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_RESET_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_grinder_soft_stall_retry_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_GRINDER_SOFT_STALL_RETRY_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_grinder_state_lid_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_GRINDER_STATE_LID_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_grinder_high_temp_jam_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_GRINDER_HIGH_TEMP_JAM_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_grinder_jam_auto_retry_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_GRINDER_JAM_AUTO_RETRY_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_fluff_not_run_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_FLUFF_NOT_RUN_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_set_start_time_during_hip_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_SET_START_TIME_DURING_HIP_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_resume_from_lip_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_RESUME_FROM_LIP_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_always_locked_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_ALWAYS_LOCKED_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_always_unlocked_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_ALWAYS_UNLOCKED_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_bucket_fullness_low_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_BUCKET_FULLNESS_LOW_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_delta_mr_hip_mass_bucket_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_DELTA_MR_HIP_MASS_BUCKET_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_locked_when_running_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_LOCKED_WHEN_RUNNING_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_fr_heat_warning_status_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_FR_HEAT_WARNING_STATUS_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_mass_no_change_reset_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_MASS_NO_CHANGE_RESET_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_lastdgocycle_energy_shadows_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_LASTDGOCYCLE_ENERGY_SHADOWS_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_cycleendtime_lid_open_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_CYCLEENDTIME_LID_OPEN_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_unprocessed_mass_zero_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_UNPROCESSED_MASS_ZERO_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_mass_add_lid_open_close_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_MASS_ADD_LID_OPEN_CLOSE_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_d_lip_skipped_hot_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_D_LIP_SKIPPED_HOT_TEST', False)


        # 8/12/2024
        sqlRun = self.convertSQL(sqlsDash.bat_hip_extension_lid_skipped_hot_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_HIP_EXTENSION_LID_OPEN_CLOSE_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_start_disconnected_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_START_DISCONNECTED_TEST', False)        

        sqlRun = self.convertSQL(sqlsDash.bat_resume_disconnected_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_RESUME_DISCONNECTED_TEST', False)        

        sqlRun = self.convertSQL(sqlsDash.bat_heat_led_interruptions_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_HEAT_LED_INTERRUPTIONS_TEST', False)

        sqlRun = self.convertSQL(sqlsDash.bat_vacation_after_empty_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_AFTER_EMPTY_TEST', False)        

        sqlRun = self.convertSQL(sqlsDash.bat_resume_cooldown_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_RESUME_COOLDOWN_TEST', False)                




        # 9/4/2024 
        sqlRun = self.convertSQL(sqlsDash.bat_vacation_ota_pre_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_OTA_PRE_TEST', False)  

        sqlRun = self.convertSQL(sqlsDash.bat_vacation_ota_post_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_VACATION_OTA_POST_TEST', False)          

        sqlRun = self.convertSQL(sqlsDash.bat_bucket_crash_ota_pre_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_BUCKET_CRASH_OTA_PRE_TEST', False)         

        sqlRun = self.convertSQL(sqlsDash.bat_bucket_crash_ota_post_o2_q, '[curBuild_O2_B]', curBuild_O2_B)
        self.queryTable(sqlRun, 'BAT_BUCKET_CRASH_OTA_POST_TEST', False)          