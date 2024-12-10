#!/bin/bash

DB_NAME="pi"
DB_USER="guo95132"   #guo95132          #pi
DB_HOST="localhost"   #localhost  #qa3
DB_PORT="5432"  
DB_PASSWORD="Welc0me123"

#### OTA ####
TABLE_NAME="REPORT_TABLE" 
COLUMN_NAMES="(Oscar, BuildDate, TemplateN, BuildN, CodeN, BuildType, ProdRelTemplate, ProdRelversion, ExtFTRelTemplate, ExtFTRelVersion, IntFTRelTemplate, IntFTRelVersion, BuildId, StatusId, JiraId, BuildStatus, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, BuildNotes, ClsStatus, BuildLink)"

VALUES="('O1', '12_7_2023', 'rls-v01_05_05-19dc16c', 'rls-v01.05.05-19dc16c', 'Gournay', 'release', 'rls-v01_04_07-6a5dcd4', 'rls-v01.04.07-6a5dcd4', 'rls-v01_05_04-f3e2334', 'rls-v01.05.04-f3e2334', 'rls-v01_05_04-f3e2334', 'rls-v01.05.04-f3e2334', 'id_build_1', 'id_status_1', 'id_jira_1', 'PASS', '', false, '', false, '', false, 'First in Dashboard', 'passed', './rls-v01.05.05-19dc16c/dashboard_v01_05_05.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
export PGPASSWORD=$DB_PASSWORD
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


# -- For v01_05_05
VALUES="('O2', '12_7_2023', 'dbg-v01_05_05-19dc16c', 'dbg-v01.05.05-19dc16c', 'Gournay', 'debug', 'N/A', 'N/A', 'dbg-v01_05_04-f3e2334', 'dbg-v01.05.04-f3e2334', 'dbg-v01_05_04-f3e2334', 'dbg-v01.05.04-f3e2334', 'id_build_2', 'id_status_2', 'id_jira_2', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.05.05-19dc16c/dashboard_v01_05_05.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2



# -- For v01_05_06
VALUES="('O1', '12_13_2023', 'rls-v01_05_06-3725fcf', 'rls-v01.05.06-3725fcf', 'Gournay', 'release', '', '', '', '', '', '', 'id_build_3', 'id_status_3', 'id_jira_3', 'RESPIN', 'FW-3843', false, '', false, '', false, 'build respin', 'respin', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', '12_13_2023', 'dbg-v01_05_06-3725fcf', 'dbg-v01.05.06-3725fcf', 'Gournay', 'debug', 'N/A', 'N/A', '', '', '', '', 'id_build_4', 'id_status_4', 'id_jira_4', 'RESPIN', 'FW-3843', false, '', false, '', false, 'build respin', 'respin', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


# -- For v01_05_08
VALUES="('O1', '12_14_2023', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'Gournay', 'release', 'rls-v01_04_07-6a5dcd4', 'rls-v01.04.07-6a5dcd4', 'rls-v01_05_05-19dc16c', 'rls-v01.05.05-19dc16c', 'rls-v01_05_05-19dc16c', 'rls-v01.05.05-19dc16c', 'id_build_5', 'id_status_5', 'id_jira_5', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', '12_14_2023', 'dbg-v01_05_08-ba5f554', 'dbg-v01.05.08-ba5f554', 'Gournay', 'debug', 'N/A', 'N/A', 'dbg-v01_05_05-19dc16c', 'dbg-v01.05.05-19dc16c', 'dbg-v01_05_05-19dc16c', 'dbg-v01.05.05-19dc16c', 'id_build_6', 'id_status_6', 'id_jira_6', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


# -- For v01_06_03
VALUES="('O2', '1_11_2024', 'rls-v01_06_03-b75e7a3', 'rls-v01.06.03-b75e7a3', 'Hamburgh', 'release', 'N/A', 'N/A', 'dbg-v01_05_08-ba5f554', 'dbg-v01.05.08-ba5f554', 'dbg-v01_05_08-ba5f554', 'dbg-v01.05.08-ba5f554', 'id_build_7', 'id_status_7', 'id_jira_7', 'PASS', '', false, '', false, '', false, 'O2 only', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_04
VALUES="('O2', '1_18_2024', 'rls-v01_06_04-eb8795d', 'rls-v01.06.04-eb8795d', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_04-eb8795d', 'rls-v01.06.04-eb8795d', '', '', 'id_build_8', 'id_status_8', 'id_jira_8', 'RESPIN', 'FW-3924', false, '', false, '', false, 'O2 only & respin', 'respin', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


# -- For v01_06_05
VALUES="('O2', '1_20_2024', 'rls-v01.06.05-5a226ee', 'rls-v01.06.05-5a226ee', 'Hamburgh', 'release', 'N/A', 'N/A', 'dbg-v01_05_08-ba5f554', 'dbg-v01.05.08-ba5f554', 'rls-v01_06_03-b75e7a3', 'rls-v01.06.03-b75e7a3', 'id_build_9', 'id_status_9', 'id_jira_9', 'PASS', '', false, '', false, '', false, 'O2 only', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_05_09
VALUES="('O1', '1_24_2024', 'rls-v01_05_09-ff78838', 'rls-v01.05.09-ff78838', 'Gournay', 'release', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'id_build_10', 'id_status_10', 'id_jira_10', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

VALUES="('O2', '1_24_2024', 'dbg-v01_05_09-ff78838', 'dbg-v01.05.09-ff78838', 'Gournay', 'debug', 'N/A', 'N/A', 'dbg-v01_05_08-ba5f554', 'dbg-v01.05.08-ba5f554', 'dbg-v01_05_08-ba5f554', 'dbg-v01.05.08-ba5f554', 'id_build_11', 'id_status_11', 'id_jira_11', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_06
VALUES="('O2', '1_25_2024', 'rls-v01_06_06-de336c5', 'rls-v01.06.06-de336c5', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'id_build_12', 'id_status_12', 'id_jira_12', 'RESPIN', '', false, 'FW-3955', false, '', false, '', 'respin', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_07
VALUES="('O2', '1_30_2024', 'rls-v01_06_07-f1f2159', 'rls-v01.06.07-f1f2159', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'id_build_13', 'id_status_13', 'id_jira_13', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2





# -- For v01_06_08
VALUES="('O2', '1_31_2024', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_05_08-ba5f554', 'rls-v01.05.08-ba5f554', 'rls-v01_06_05-5a226ee', 'rls-v01.06.05-5a226ee', 'id_build_14', 'id_status_14', 'id_jira_14', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_09
VALUES="('O2', '2_8_2024', 'rls-v01_06_09-ef2de6d', 'rls-v01.06.09-ef2de6d', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'id_build_15', 'id_status_15', 'id_jira_15', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_10  
VALUES="('O2', '2_9_2024', 'rls-v01_06_10-fa2a8cf', 'rls-v01.06.10-fa2a8cf', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'id_build_16', 'id_status_16', 'id_jira_16', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_12
VALUES="('O2', '2_13_2024', 'rls-v01_06_12-a345ff2', 'rls-v01.06.12-a345ff2', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'id_build_17', 'id_status_17', 'id_jira_17', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_14
VALUES="('O2', '2_14_2024', 'rls-v01_06_14-b294226', 'rls-v01.06.14-b294226', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'id_build_18', 'id_status_18', 'id_jira_18', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.14-b294226/dashboard_v01_06_14.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_15
VALUES="('O2', '2_21_2024', 'rls-v01_06_15-16daade', 'rls-v01.06.15-16daade', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_14-b294226', 'rls-v01.06.14-b294226', 'rls-v01_06_14-b294226', 'rls-v01.06.14-b294226', 'id_build_19', 'id_status_19', 'id_jira_19', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.15-16daade/dashboard_v01_06_15.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_16
VALUES="('O2', '2_28_2024', 'rls-v01_06_16-2a88ab6', 'rls-v01.06.16-2a88ab6', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_15-16daade', 'rls-v01.06.15-16daade', 'rls-v01_06_15-16daade', 'rls-v01.06.15-16daade', 'id_build_20', 'id_status_20', 'id_jira_20', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.16-2a88ab6/dashboard_v01_06_16.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_17
VALUES="('O2', '3_6_2024', 'rls-v01_06_17-8b85b9b', 'rls-v01.06.17-8b85b9b', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'rls-v01_06_12-a345ff2', 'rls-v01.06.12-a345ff2', 'id_build_21', 'id_status_21', 'id_jira_21', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_18
VALUES="('O2', '3_8_2024', 'rls-v01_06_18-d868772', 'rls-v01.06.18-d868772', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_08-76ef61d', 'rls-v01.06.08-76ef61d', 'rls-v01_06_12-a345ff2', 'rls-v01.06.12-a345ff2', 'id_build_22', 'id_status_22', 'id_jira_22', 'PASS', '', false, '', false, '', false, '', 'passed', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_19
VALUES="('O2', '3_13_2024', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_17-8b85b9b', 'rls-v01.06.17-8b85b9b', 'rls-v01_06_17-8b85b9b', 'rls-v01.06.17-8b85b9b', 'id_build_23', 'id_status_23', 'id_jira_23', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.19-8cafe27/dashboard_v01_06_19.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


# -- For v01_06_20
VALUES="('O2', '3_20_2024', 'rls-v01_06_20-62fcc39', 'rls-v01.06.20-62fcc39', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'id_build_24', 'id_status_24', 'id_jira_24', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.20-62fcc39/dashboard_v01_06_20.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2


# -- For v01_06_21
VALUES="('O2', '3_21_2024', 'rls-v01_06_21-e1529df', 'rls-v01.06.21-e1529df', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'id_build_25', 'id_status_25', 'id_jira_25', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.21-e1529df/dashboard_v01_06_21.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_22
VALUES="('O2', '3_27_2024', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_21-e1529df', 'rls-v01.06.21-e1529df', 'rls-v01_06_21-e1529df', 'rls-v01.06.21-e1529df', 'id_build_26', 'id_status_26', 'id_jira_26', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.22-c356fff/dashboard_v01_06_22.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_23
VALUES="('O2', '4_3_2024', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', 'id_build_27', 'id_status_27', 'id_jira_27', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.23-562210a/dashboard_v01_06_23.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_07_00
VALUES="('O2', '4_3_2024', 'rls-v01_07_00-37e01a1', 'rls-v01.07.00-37e01a1', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', 'rls-v01_06_22-c356fff', 'rls-v01.06.22-c356fff', 'id_build_28', 'id_status_28', 'id_jira_28', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.07.00-37e01a1/dashboard_v01_07_00.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_07_01
VALUES="('O2', '4_10_2024', 'rls-v01_07_01-c8be6d6', 'rls-v01.07.01-c8be6d6', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'id_build_29', 'id_status_29', 'id_jira_29', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.07.01-c8be6d6/dashboard_v01_07_01.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_24
VALUES="('O2', '4_12_2024', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'Hamburgh', 'release', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'id_build_30', 'id_status_30', 'id_jira_30', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.06.24-b0df8e4/dashboard_v01_06_24.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_07_02
VALUES="('O2', '4_17_2024', 'rls-v01_07_02-f974177', 'rls-v01.07.02-f974177', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'id_build_33', 'id_status_33', 'id_jira_33', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.07.02-f974177/dashboard_v01_07_02.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_07_03
VALUES="('O2', '4_20_2024', 'rls-v01_07_03-c21042a', 'rls-v01.07.03-c21042a', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'id_build_34', 'id_status_34', 'id_jira_34', 'PASS', '', false, '', false, '', false, '', 'passed', './rls-v01.07.03-c21042a/dashboard_v01_07_03.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_23 O1
VALUES="('O1', '4_3_2024', 'rls-v01_06_23-562210a', 'rls-v01.06.23-562210a', 'Hamburgh', 'release', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'id_build_30', 'id_status_30', 'id_jira_30', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_24 O1
VALUES="('O1', '4_12_2024', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'Hamburgh', 'release', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'rls-v01_06_19-8cafe27', 'rls-v01.06.19-8cafe27', 'id_build_32', 'id_status_32', 'id_jira_32', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_27
VALUES="('O2', '4_26_2024', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'Hamburgh', 'release', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'id_build_37', 'id_status_37', 'id_jira_37', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_25
VALUES="('O2', '4_24_2024', 'rls-v01_06_25-07f852f', 'rls-v01.06.25-07f852f', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'id_build_35', 'id_status_35', 'id_jira_35', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_06_26
VALUES="('O2', '4_25_2024', 'rls-v01_06_26-f09d1ae', 'rls-v01.06.26-f09d1ae', 'Hamburgh', 'release', 'N/A', 'N/A', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'rls-v01_06_24-b0df8e4', 'rls-v01.06.24-b0df8e4', 'id_build_36', 'id_status_36', 'id_jira_36', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2

# -- For v01_07_05
VALUES="('O2', '5_3_2024', 'rls-v01_07_05-1b8bb0d', 'rls-v01.07.05-1b8bb0d', 'Lxworth', 'release', 'N/A', 'N/A', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'rls-v01_06_27-3a12001', 'rls-v01.06.27-3a12001', 'id_build_39', 'id_status_39', 'id_jira_39', 'PENDING', '', false, '', false, '', false, '', 'pending', './asset/under_construction.html')"
QUERY="INSERT INTO $TABLE_NAME $COLUMN_NAMES VALUES $VALUES;"
psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -c "$QUERY"
sleep 2
