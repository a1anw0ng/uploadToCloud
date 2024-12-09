#!/bin/bash

FILE="rls-v01_06_23-562210a_metadata_O1.sh"

if [ -f "$FILE" ]; then
    echo "File $FILE exists. Deleting now..."
    rm "$FILE"
    echo "File deleted."
else
    echo "File $FILE does not exist."
fi






# For Build v01.06.23

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_ota_self_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_ota_power_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_ota_int_upgrade_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_ota_ext_upgrade_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_ota_prod_upgrade_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3


python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_idle_op_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_lip_op_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_hip_op_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_cooldown_op_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_fluff_op_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3



python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_idle_mass_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_lip_mass_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_hip_mass_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_cooldown_mass_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_dgo_fluff_mass_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3


python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_eeprom_stress_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_pairing_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_start_via_bin_B_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_start_via_bin_A_stress_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_child_lock_B_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3
python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_child_lock_A_stress_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_safety_test_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_boot_cycle_A_stress_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_lid_open_close_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
sleep 3

# 1. update to:  rls-v01.06.23-562210a
# 2. update to:  v01_06_23.txt
# 3. update SN:
# 4. update svr: 
#########################################################################################
# For O1 add 1 more:
# python3 Use_ParsingResults.py rls-v01.06.23-562210a_O1/O1_lid_open_close_results_v01_06_23.txt MG22332A2US0019 qa7 rls-v01.06.23-562210a
#
#  Update: rls-v01.06.23-562210a/O2