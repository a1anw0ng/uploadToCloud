# For Build v01.06.28 O1

python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_ota_self_results_v01_06_31.txt MGM2327A1US0030 dgo1 rls-v01.06.31-aaaa605 dgo1
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_ota_power_results_v01_06_31.txt MG52306A1US002C qa6 rls-v01.06.31-aaaa605 qa6_O1
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_ota_int_upgrade_results_v01_06_31.txt MGM2327A1US0030 dgo1 rls-v01.06.31-aaaa605 dgo1
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_ota_ext_upgrade_results_v01_06_31.txt MGM2327A1US0030 dgo1 rls-v01.06.31-aaaa605 dgo1
sleep 3

python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_ota_prod_upgrade_results_v01_06_31.txt MGM2327A1US0030 dgo1 rls-v01.06.31-aaaa605 dgo1
sleep 3


python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_idle_op_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_lip_op_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_hip_op_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_cooldown_op_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_fluff_op_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3



python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_idle_mass_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_lip_mass_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_hip_mass_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_cooldown_mass_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_dgo_fluff_mass_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3


python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_eeprom_stress_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_pairing_results_v01_06_31.txt MG52306A1US002E home_O1 rls-v01.06.31-aaaa605 home_O1
sleep 3 

python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_start_via_bin_B_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_start_via_bin_A_stress_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3

python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_child_lock_B_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3
python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_child_lock_A_stress_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3

python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_safety_test_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3

python3 Use_ParsingResults.py rls-v01.06.31-aaaa605_O1/O1_lid_open_close_results_v01_06_31.txt MG62311A1US0028 qa5 rls-v01.06.31-aaaa605 qa5
sleep 3


# Template:
# python3 Use_ParsingResults.py <buildN folder>/<each results file> <SN> <serverN> <buildN> <runner>
#
# 1. update to:  rls-v01.07.00-37e01a1
# 2. update to:  v01_06_23.txt
# 3. update SN:
# 4. update svr: 
# 5. update runner:
#########################################################################################

