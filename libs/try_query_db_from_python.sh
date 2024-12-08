
#!/bin/bash


#output=$(python query_db_from_python_2.py get_cur_t_o1)
#output=$(python query_db_from_python_2.py get_cur_v_o1)
#output=$(python query_db_from_python_2.py get_cur_b_type_o1)
#output=$(python query_db_from_python_2.py get_cur_b_date_o1)
#output=$(python query_db_from_python_2.py get_cur_code_n_o1)


#output=$(python query_db_from_python_2.py get_prod_t_o1)
#output=$(python query_db_from_python_2.py get_prod_v_o1)

#output=$(python query_db_from_python_2.py get_ext_ft_t_o1)
#output=$(python query_db_from_python_2.py get_ext_ft_v_o1)
#output=$(python query_db_from_python_2.py get_int_ft_t_o1)
#output=$(python query_db_from_python_2.py get int_ft_v_o1)

#output=$(python query_db_from_python_2.py set cur_g_o1 --v1 '12_7_2023' --v2 'rls-v01_05_05-19dc16c' --v3 'rls-v01.05.05-19dc16c' --v4 'Gournay')
#output=$(python query_db_from_python_2.py set cur_g_o1 --v1 12_7_2023 --v2 rls-v01_05_05-19dc16c --v3 rls-v01.05.05-19dc16c --v4 Gournay)

#output=$(python query_db_from_python_2.py set b_type_o1 --v1 debug)
#output=$(python query_db_from_python_2.py set b_type_o1 --v1 release)

#output=$(python query_db_from_python_2.py set prod_o1 --v1 rls-v01_04_07-6a5dcd4 --v2 rls-v01.04.07-6a5dcd4)

#output=$(python query_db_from_python_2.py set prod_o1 --v1 rls-v01_05_04-f3e2334 --v2 rls-v01.04.07-6a5dcd4)

output=$(python query_db_from_python_2.py set ext_ft_o1 --v1 rls-v01_05_04-f3e2334 --v2 rls-v01.05.04-f3e2334)

#output=$(python query_db_from_python_2.py set int_ft_o1 --v1 rls-v01_05_04-f3e2334 --v2 rls-v01.05.04-f3e2334)

# Print the output
echo "output= $output"



            # 'prod_o1': self.set_prod_o1,
            # 'ext_ft_o1': self.set_ext_ft_o1,
            # 'int_ft_o1': self.set_int_ft_o1


# "O1"	"12_7_2023"	"rls-v01_05_05-19dc16c"	"rls-v01.05.05-19dc16c"	"Gournay"	"release"	
# "rls-v01_04_07-6a5dcd4"	"rls-v01.04.07-6a5dcd4"	
# "rls-v01_05_04-f3e2334"	"rls-v01.05.04-f3e2334"	
# "rls-v01_05_04-f3e2334"	"rls-v01.05.04-f3e2334"

# python query_db_from_python_2.py get_prod_t_o1


# output=$(python3 query_db_from_python.py "select * from REPORT_TABLE")

#python insert_data_into_tables_2.py OTA_SELF_TABLE 'rls-v01_05_05-19dc16c' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 1 1 0 '~2hrs' 30 ''  ''  ''  './O1_ota_self_results_v01_05_05.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

#python insert_data_into_tables.py OTA_SELF_TABLE 'rls-v01_05_05-19dc16c' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 1 1 0 '~2hrs' 30 '' --vJiraF1 '' --vJiraF2 '' --vJiraF3 './O1_ota_self_results_v01_05_05.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'

#python insert_data_into_tables.py OTA_SELF_TABLE 'rls-v01_05_05-19dc16c' 'O1' 'qa3' 'MG52306A1US002C' 1 2 2 1 1 0 '~2hrs' 30 '' --vJiraF1 ''  '' --vJiraF3 './O1_ota_self_results_v01_05_05.txt' 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'



    # cursor.execute(insert_query, ('rls-v01_05_05-19dc16c', 'O1', 'qa3', 'MG52306A1US002C', 1, 2, 2, 1, 1, 0, 
    #                               '~2hrs', 30, '', False, '', False, '', False, './O1_ota_self_results_v01_05_05.txt', 
    #                               'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/run_ota_3D.py'))


# #echo "::set-output name=ver_o2::$(yq e '.O2.Int_FT_O2.version' $SYS_SETUP)"

# TEST_RESULTS="test_results_v01_05_05.yml"

# TemplateN=$(yq e '.O1.TemplateN' $TEST_RESULTS)
# echo "TemplateN= $TemplateN"

# BuildN=$(yq e '.O1.BuildN' $TEST_RESULTS)
# echo "BuildN= $BuildN"

# CodeN=$(yq e '.O1.CodeN' $TEST_RESULTS)
# echo "CodeN= $CodeN"



# Passed=$(yq e '.O1.OTA_SELF.Passed' $TEST_RESULTS)
# echo "Passed= $Passed"

# Failed=$(yq e '.O1.OTA_SELF.Failed' $TEST_RESULTS)
# echo "Failed= $Failed"

# ExeTime=$(yq e '.O1.OTA_SELF.ExeTime' $TEST_RESULTS)
# echo "ExeTime= $ExeTime"

# ResultLink=$(yq e '.O1.OTA_SELF.ResultLink' $TEST_RESULTS)
# echo "ResultLink= $ResultLink"

# ################################################

# echo "################################################\n"
# SOURCE_FILE="dashboard_template.html"
# DESTINATION_FILE="dashboard_v01_05_05.html"

# rm "$DESTINATION_FILE"

# cp "$SOURCE_FILE" "$DESTINATION_FILE"

# #sed -i 's/var /\/\/var /' $DESTINATION_FILE

# python prepare_dashboard.py


# # TemplateN=$(yq e '.O1.TemplateN' $TEST_RESULTS)
# # echo "TemplateN= $TemplateN"

# # sed -i "s/O1_TEMPLATE/\"$TemplateN\"/" $DESTINATION_FILE

# # BuildN=$(yq e '.O1.BuildN' $TEST_RESULTS)
# # echo "BuildN= $BuildN"

# # sed -i "s/O1_BUILD/\"$BuildN\"/" $DESTINATION_FILE

# # CodeN=$(yq e '.O1.CodeN' $TEST_RESULTS)
# # echo "CodeN= $CodeN"