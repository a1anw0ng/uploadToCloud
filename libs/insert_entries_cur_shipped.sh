


# # To insert data in cur_shipped table:

# python insert_entry_cur_shipped.py CUR_SHIPPED_TABLE 'insert' 'O1' 'Gournay' 'release' 'rls-v01_04_07-6a5dcd4' 'rls-v01.04.07-6a5dcd4' 'rls-v01_05_04-f3e2334' 'rls-v01.05.04-f3e2334' 'rls-v01_05_04-f3e2334' 'rls-v01.05.04-f3e2334' '' '' '' '' '' '' '' '' '' ''

# python insert_entry_cur_shipped.py CUR_SHIPPED_TABLE 'insert' 'O2' 'Gournay' 'debug' 'N/A' 'N/A' 'dbg-v01_05_04-f3e2334' 'dbg-v01.05.04-f3e2334' 'dbg-v01_05_04-f3e2334' 'dbg-v01.05.04-f3e2334' '' '' '' '' '' '' '' '' '' ''



# To update m_dash:

# python insert_entry_cur_shipped.py CUR_SHIPPED_TABLE "update" 'O1' 'Gournay' 'release' 'rls-v01_04_07-6a5dcd4' 'rls-v01.04.07-6a5dcd4' 'rls-v01_05_04-f3e2334' 'rls-v01.05.04-f3e2334' 'rls-v01_05_04-f3e2334' 'rls-v01.05.04-f3e2334' 'this is O1' '' '' '' '' '' '' '' '' ''

# python insert_entry_cur_shipped.py CUR_SHIPPED_TABLE "update" 'O2' 'Gournay' 'debug' 'N/A' 'N/A' 'dbg-v01_05_04-f3e2334' 'dbg-v01.05.04-f3e2334' 'dbg-v01_05_04-f3e2334' 'dbg-v01.05.04-f3e2334' 'Cool' 'Yes!' '' '' '' '' '' '' '' ''




# To query the latest entry 

# python insert_entry_cur_shipped.py CUR_SHIPPED_TABLE "query" "O2"

# python insert_entry_cur_shipped.py CUR_SHIPPED_TABLE "query" "O1"