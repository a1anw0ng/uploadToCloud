# import os
# import re

# class LogFiles:
#     O1_patterns = [
#         'O1_dgo_idle_mass_results_{version}.txt',
#         'O1_dgo_idle_op_results_{version}.txt',
#         'O1_dgo_lip_mass_results_{version}.txt',
#         'O1_dgo_lip_op_results_{version}.txt',
#         'O1_dgo_hip_mass_results_{version}.txt',
#     ]

# def verify_files_exist(folder_path):
#     # List all files in the target folder
#     existing_files = os.listdir(folder_path)
#     print("existing_files= ", existing_files)

#     # Update regex pattern to match the versioning scheme in your file names (e.g., v01_05_08)
#     # We'll use \w+ to match one or more word characters (which includes letters and digits) and underscores
#     for pattern in LogFiles.O1_patterns:
#         regex_pattern = pattern.replace('{version}', r'v\w+_\w+_\w+')
#         # Compile the regex pattern to match files
#         compiled_pattern = re.compile(regex_pattern)

#         # Check if there is at least one file in the folder that matches the pattern
#         found = any(compiled_pattern.match(file_name) for file_name in existing_files)
#         if not found:
#             print(f"Missing file for pattern: {pattern.replace('{version}', 'vXX_XX_XX')}")
#         else:
#             print(f"Found files matching pattern: {pattern.replace('{version}', 'vXX_XX_XX')}")


# # Example usage
# folder_path = "rls-v01.05.08-ba5f554/"
# verify_files_exist(folder_path)


import os

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
        'O2_pairing_results_{version}.txt',
        'O2_boot_cycle_A_stress_results_{version}.txt'
    ]



# print("aa= ", LogFiles.O1_patterns[0])
# print("aa= ", LogFiles.O1_patterns[1])

def verify_specific_version_exists(folder_path, version, patterns):
    existing_files = os.listdir(folder_path)
    missing_files = []

    for pattern in patterns:
        #print("pattern= ", pattern)
        expected_filename = pattern.format(version=version)
        if expected_filename not in existing_files:
            missing_files.append(expected_filename)

    if missing_files:
        print("Missing files:")
        for file in missing_files:
            print(f"  - {file}")
    else:
        print("All specified version files are present.")





# folder_path = "rls-v01.05.05-19dc16c_2/"
# version = "v01_05_05" 

# folder_path = "rls-v01.05.06-3725fcf/"
# version = "v01_05_06" 


# Example usage, specify the exact version you're checking for
# folder_path = "rls-v01.05.08-ba5f554/"
# version = "v01_05_08" # Update this to the version you want to check

# folder_path = "rls-v01.05.09-ff78838/"
# version = "v01_05_09" # Update this to the version you want to check

# folder_path = "rls-v01.06.03-b75e7a3/"
# version = "v01_06_03" 

# folder_path = "rls-v01.06.04-eb8795d/"
# version = "v01_06_04" 

# folder_path = "rls-v01.06.05-5a226ee/"
# version = "v01_06_05" 


# folder_path = "rls-v01.06.06-de336c5/"
# version = "v01_06_06" 

# folder_path = "rls-v01.06.07-f1f2159/"
# version = "v01_06_07" 

# folder_path = "rls-v01.06.08-76ef61d/"
# version = "v01_06_08" 

# folder_path = "rls-v01.06.09-ef2de6d/"
# version = "v01_06_09" 

# folder_path = "rls-v01.06.10-fa2a8cf/"
# version = "v01_06_10" 


# folder_path = "rls-v01.06.12-a345ff2/"
# version = "v01_06_12" 

# folder_path = "rls-v01.06.14-b294226/"
# version = "v01_06_14" 

# folder_path = "rls-v01.06.15-16daade/"
# version = "v01_06_15" 

# folder_path = "rls-v01.06.16-2a88ab6/"
# version = "v01_06_16" 


# folder_path = "rls-v01.06.17-8b85b9b/"
# version = "v01_06_17" 

# folder_path = "rls-v01.06.18-d868772/"
# version = "v01_06_18" 

# folder_path = "rls-v01.06.19-8cafe27/"
# version = "v01_06_19" 

# folder_path = "rls-v01.06.20-62fcc39/"
# version = "v01_06_20" 

folder_path = "rls-v01.06.21-e1529df/"
version = "v01_06_21" 


#v01.06.07 and v01.06.08 are in github already, but not ota

print("===for O1====")
verify_specific_version_exists(folder_path, version, LogFiles.O1_patterns)
print("===for O2====")
verify_specific_version_exists(folder_path, version, LogFiles.O2_patterns)
