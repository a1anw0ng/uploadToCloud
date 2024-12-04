# For Build v01.06.26

python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_ota_self_results_v01_07_05.txt MG22332A2US0019 qa7 rls-v01.07.05-1b8bb0d qa7
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_ota_power_results_v01_07_05.txt guo_sn_14_o2 qa6 rls-v01.07.05-1b8bb0d qa6_O2
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_ota_int_upgrade_results_v01_07_05.txt MG22332A2US0019 qa7 rls-v01.07.05-1b8bb0d qa7
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_ota_ext_upgrade_results_v01_07_05.txt MG22332A2US0019 qa7 rls-v01.07.05-1b8bb0d qa7
sleep 3

python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_ota_prod_upgrade_results_v01_07_05.txt MG22332A2US0019 qa7 rls-v01.07.05-1b8bb0d qa7
sleep 3


python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_idle_op_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_lip_op_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_hip_op_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_cooldown_op_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_fluff_op_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3



python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_idle_mass_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_lip_mass_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_hip_mass_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_cooldown_mass_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_dgo_fluff_mass_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3


python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_eeprom_stress_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_pairing_results_v01_07_05.txt MG22335A2US0024 home_O2 rls-v01.07.05-1b8bb0d home_O2
sleep 3 

python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_start_via_bin_B_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_start_via_bin_A_stress_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3

python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_child_lock_B_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3
python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_child_lock_A_stress_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3

python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_safety_test_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
sleep 3

python3 Use_ParsingResults.py rls-v01.07.05-1b8bb0d/O2_boot_cycle_A_stress_results_v01_07_05.txt MG32401A2US100204 qa9 rls-v01.07.05-1b8bb0d qa9
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

