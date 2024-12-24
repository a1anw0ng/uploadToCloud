from datetime import datetime
from millPostDB import millPostDB
import re
import argparse
import os
from sqlsDash import sqlsDash


GH_OTA_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/ota/'
GH_DGO_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/dgo/testsuites/'
GH_PAIR_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/pairing/testsuites/'
GH_MORE_PATH = 'https://github.com/chewielabs/Oscar-Python-CLI/blob/main/src/oscar/more/testsuites/'

class TSLink:
    OTA = GH_OTA_PATH + 'run_ota_3D.py'
    OTA_POWER = GH_OTA_PATH + 'testsuites/ota_power_cycles.json'

    O1_DGO_OP_IDLE = GH_DGO_PATH + 'dgo_testsuite_IDLE_5hr.json'
    O1_DGO_OP_LIP = GH_DGO_PATH + 'dgo_testsuite_LIP_5hr.json'
    O1_DGO_OP_HIP = GH_DGO_PATH + 'dgo_testsuite_HIP_5hr.json'
    O1_DGO_OP_COOLDOWN = GH_DGO_PATH + 'dgo_testsuite_COOLDOWN_5hr.json'
    O1_DGO_OP_FLUFF = GH_DGO_PATH + 'dgo_testsuite_FLUFF_5hr.json'

    O2_DGO_OP_IDLE = GH_DGO_PATH + 'dgo_testsuite_IDLE_5hr_O2.json'
    O2_DGO_OP_LIP = GH_DGO_PATH + 'dgo_testsuite_LIP_5hr_O2.json'
    O2_DGO_OP_HIP = GH_DGO_PATH + 'dgo_testsuite_HIP_5hr_O2.json'
    O2_DGO_OP_COOLDOWN = GH_DGO_PATH + 'dgo_testsuite_COOLDOWN_5hr_O2.json'
    O2_DGO_OP_FLUFF = GH_DGO_PATH + 'dgo_testsuite_FLUFF_5hr_O2.json'

    O1_DGO_MASS_IDLE = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_IDLE.json'
    O1_DGO_MASS_LIP = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_LIP.json'
    O1_DGO_MASS_HIP = GH_DGO_PATH +'dgo_mass_add_5hr_min_runtime_HIP.json'
    O1_DGO_MASS_COOLDOWN = GH_DGO_PATH +'dgo_mass_add_5hr_min_runtime_COOLDOWN.json'
    O1_DGO_MASS_FLUFF = GH_DGO_PATH +'dgo_mass_add_5hr_min_runtime_FLUFF.json'

    O2_DGO_MASS_IDLE = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_IDLE_O2.json'
    O2_DGO_MASS_LIP = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_LIP_O2.json'
    O2_DGO_MASS_HIP = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_HIP_O2.json'
    O2_DGO_MASS_COOLDOWN = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_COOLDOWN_O2.json'
    O2_DGO_MASS_FLUFF = GH_DGO_PATH + 'dgo_mass_add_5hr_min_runtime_FLUFF_O2.json'

    O1_SAFETY = GH_DGO_PATH + 'safety_test.json'
    O2_SAFETY = ''

    O1_PAIRING = GH_PAIR_PATH + 'pairing.json'
    O2_PAIRING = GH_PAIR_PATH + 'pairing_O2.json'    

    O1_LID = GH_DGO_PATH + 'lid_open_close_stress.json'

    O1_STARTA = GH_DGO_PATH + 'dgo_start_via_bin_stress_A.json'
    O1_STARTB = GH_DGO_PATH + 'dgo_start_via_bin_B.json'

    O2_STARTA = GH_DGO_PATH + 'dgo_start_via_bin_stress_A_O2.json'
    O2_STARTB = GH_DGO_PATH + 'dgo_start_via_bin_B_O2.json'

    EEPROM = GH_DGO_PATH + 'eeprom_stress_test.json'

    O1_CHILDA = GH_DGO_PATH + 'child_lock_stress_A.json'
    O1_CHILDB = GH_DGO_PATH + 'child_lock_B.json'

    O2_CHILDA = GH_DGO_PATH + 'child_lock_stress_A_O2.json'
    O2_CHILDB = GH_DGO_PATH + 'child_lock_B_O2.json'

    O1_BOOTA = GH_DGO_PATH + 'boot_cycle_stress_A_O1.json'
    O1_BOOTB = GH_DGO_PATH + 'boot_cycle_B_O1.json'

    O2_BOOTA = GH_DGO_PATH + 'boot_cycle_stress_A_O2.json'
    O2_BOOTB = GH_DGO_PATH + 'boot_cycle_B_O2.json'



class DBT:
    OTA_TABLE = 'OTA_TABLE'
    POWER_DURING_OTA_TABLE = 'POWER_DURING_OTA_TABLE'
    DGO_OP_PR_TABLE = 'DGO_OP_PR_TABLE'
    DGO_ADD_MASS_TABLE = 'DGO_ADD_MASS_TABLE'
    SAFETY_TEST_TABLE = 'SAFETY_TEST_TABLE'
    PAIRING_WITHOUT_BLE_TABLE = 'PAIRING_WITHOUT_BLE_TABLE'
    LID_OPEN_CLOSE_TABLE = 'LID_OPEN_CLOSE_TABLE'
    START_VIA_BIN_TABLE = 'START_VIA_BIN_TABLE'
    EEPROM_STRESS_TEST_TABLE = 'EEPROM_STRESS_TEST_TABLE'
    CHILD_LOCK_TABLE = 'CHILD_LOCK_TABLE'
    BOOT_CYCLE_TABLE = 'BOOT_CYCLE_TABLE'

class LgF:
    O1_DGO_IDLE_MASS = 'O1_dgo_idle_mass_results_xxx.txt'
    O1_DGO_IDLE_OP = 'O1_dgo_idle_op_results_xxx.txt'
    O1_DGO_LIP_MASS = 'O1_dgo_lip_mass_results_xxx.txt'
    O1_DGO_LIP_OP = 'O1_dgo_lip_op_results_xxx.txt'
    O1_DGO_HIP_MASS = 'O1_dgo_hip_mass_results_xxx.txt'
    O1_DGO_HIP_OP = 'O1_dgo_hip_op_results_xxx.txt'
    O1_DGO_COOLDOWN_MASS = 'O1_dgo_cooldown_mass_results_xxx.txt'
    O1_DGO_COOLDOWN_OP = 'O1_dgo_cooldown_op_results_xxx.txt'
    O1_DGO_FLUFF_MASS = 'O1_dgo_fluff_mass_results_xxx.txt'
    O1_DGO_FLUFF_OP = 'O1_dgo_fluff_op_results_xxx.txt'
    O1_CHILD_A = 'O1_child_lock_A_stress_results_xxx.txt'
    O1_CHILD_B = 'O1_child_lock_B_results_xxx.txt'
    O1_START_A = 'O1_start_via_bin_A_stress_results_xxx.txt'
    O1_START_B = 'O1_start_via_bin_B_results_xxx.txt'
    O1_EEPROM = 'O1_eeprom_stress_results_xxx.txt'
    O1_PAIRING = 'O1_pairing_results_xxx.txt'
    O1_SAFETY = 'O1_safety_test_results_xxx.txt'
    O1_LID = 'O1_lid_open_close_results_xxx.txt'
    O1_BOOTA = 'O1_boot_cycle_A_stress_results_xxx.txt'

    O2_DGO_IDLE_MASS = 'O2_dgo_idle_mass_results_xxx.txt'
    O2_DGO_IDLE_OP = 'O2_dgo_idle_op_results_xxx.txt'
    O2_DGO_LIP_MASS = 'O2_dgo_lip_mass_results_xxx.txt'
    O2_DGO_LIP_OP = 'O2_dgo_lip_op_results_xxx.txt'
    O2_DGO_HIP_MASS = 'O2_dgo_hip_mass_results_xxx.txt'
    O2_DGO_HIP_OP = 'O2_dgo_hip_op_results_xxx.txt'
    O2_DGO_COOLDOWN_MASS = 'O2_dgo_cooldown_mass_results_xxx.txt'
    O2_DGO_COOLDOWN_OP = 'O2_dgo_cooldown_op_results_xxx.txt'
    O2_DGO_FLUFF_MASS = 'O2_dgo_fluff_mass_results_xxx.txt'
    O2_DGO_FLUFF_OP = 'O2_dgo_fluff_op_results_xxx.txt'
    O1_CHILD_A = 'O2_child_lock_A_stress_results_xxx.txt'
    O1_CHILD_B = 'O2_child_lock_B_results_xxx.txt'
    O1_START_A = 'O2_start_via_bin_A_stress_results_xxx.txt'
    O1_START_B = 'O2_start_via_bin_B_results_xxx.txt'
    O2_EEPROM = 'O2_eeprom_stress_results_xxx.txt'
    O2_PAIRING = 'O2_pairing_results_xxx.txt'
    O2_BOOTA = 'O2_boot_cycle_A_stress_results_xxx.txt'


class ParseData(millPostDB):
    def __init__(self, database, host, user, password, port, sysLogF):
        super().__init__(database, host, user, password, port, sysLogF)

        self.run_details = {}  # Dictionary to hold run IDs and their corresponding sub-runs
        self.tests_passed = 0
        self.tests_failed = 0

        self.total_duration_seconds = 0
        self.datetime_format = "%m-%d %H:%M"
        self.start_times = {}
        self.end_times = {}

        self.test_durations = []  # List to store duration of each test in seconds

        self.first_line = None
        self.second_line = None


        # DGO
        self.total_collected = None
        self.dgo_passed = 0
        self.dgo_failed = 0
        self.total_tests = 0

        self.dgo_total_time = 0
        self.dgo_run_count = 0


        # After Parsed
        self.results = {}



    def extract_timestamp_with_format_detection(self, date_time_string):
        """
        Extracts the timestamp from a date-time string, handling different formats including:
        - "%Y-%m-%d %H:%M:%S"
        - "%m-%d %H:%M"
        Additionally handles the presence of milliseconds.
        """
        # Define possible formats
        formats = [
            {"format": "%Y-%m-%d %H:%M:%S,%f", "has_year": True},
            {"format": "%Y-%m-%d %H:%M:%S", "has_year": True},
            {"format": "%m-%d %H:%M", "has_year": False}
        ]
        
        # Current year as fallback for formats without a year
        current_year = datetime.now().year
    
        for fmt in formats:
            try:
                # Attempt to parse the string with the current format
                if fmt["format"].endswith(",%f"):  # Handling milliseconds if present
                    datetime_part, milliseconds = date_time_string.split(',')
                    datetime_object = datetime.strptime(datetime_part, fmt["format"].rstrip(",%f"))
                    timestamp = datetime_object.timestamp() + int(milliseconds) / 1000
                else:
                    datetime_object = datetime.strptime(date_time_string, fmt["format"])
                    timestamp = datetime_object.timestamp()
                    
                # If the format does not include the year, set the year to the current year
                if not fmt["has_year"]:
                    datetime_object = datetime_object.replace(year=current_year)
                    timestamp = datetime_object.timestamp()
                
                return timestamp
            except ValueError:
                # If parsing fails, try the next format
                continue
        
        # If none of the formats match, return an error message
        return None

    def detect_invalid_timestamps(self, parts):
        # print("parts= ", parts)
        """
        Detects if both part[0] and part[1] from a list of parts are not valid timestamps.
        Returns True if both parts are invalid, otherwise False.
        """
        # Define possible formats
        formats = [
            "%Y-%m-%d %H:%M:%S,%f",
            "%Y-%m-%d %H:%M:%S",
            "%m-%d %H:%M",
            "%Y-%m-%d",
            "%H:%M:%S",
            "%m-%d",
            "%H:%M"
        ]
        
        # Function to check if a part matches any format
        def is_valid_datetime(part):

            for fmt in formats:
                try:
                    datetime.strptime(part, fmt)
                    return True  # Part matches format, valid datetime
                except ValueError:
                    continue  # Part does not match this format, try next
            return False  # No formats matched, invalid datetime
        
        # Check the first two parts for valid timestamp information
        is_first_part_valid = is_valid_datetime(parts[0])
        is_second_part_valid = is_valid_datetime(parts[1])
        
        # Return True if both parts are invalid timestamps
        return not (is_first_part_valid or is_second_part_valid)

    def extract_filename(self, path):
        # Split the path by '/' and get the last part as the file name
        return path.split('/')[-1]

    def parseOTAFile(self, file_path):
        # Open the file and process each line
        with open(file_path, 'r') as file:
            self.first_line = file.readline().strip()  # Read the first line and strip newline characters
            self.second_line = file.readline().strip()  # Read the second line and strip newline characters

            for line in file:
                parts = line.split()
                if not parts:
                    continue

                if len(parts) < 2:
                    continue

                if self.detect_invalid_timestamps(parts):
                    continue

                timestamp_str = parts[0] + " " + parts[1]
                #print("1. timestamp_str= ", timestamp_str)
                timestamp = self.extract_timestamp_with_format_detection(timestamp_str)


                #print("timestamp= ", timestamp)

                if "================= Run:" in line:
                    # Extract the part of the line that should contain run and sub-run numbers
                    try:
                        run_part = line.split('================= Run:')[1].strip()
                        if '->' in run_part:
                            run_id, sub_run_id = run_part.split('->')
                            run_id = run_id.strip()
                            sub_run_id = sub_run_id.strip()

                            # Update the dictionary with runs and sub-runs
                            if run_id in self.run_details:
                                self.run_details[run_id].add(sub_run_id)
                            else:
                                self.run_details[run_id] = {sub_run_id}


                            run_key = f"{run_id}->{sub_run_id}"

                            # Assuming each run starts with a "Run:" line, record start time
                            self.start_times[run_key] = timestamp

                    
                        else:
                            print(f"Line does not contain expected '->': {line.strip()}")
                    except ValueError as e:
                        print(f"Error processing line: {line.strip()}. Error: {e}")
                        
                elif "End timestamp" in line:
                    # Find the run_key that matches the ending run to record end time
                    for run_key in self.start_times.keys():
                        if run_key not in self.end_times:
                            self.end_times[run_key] = timestamp
                            break

                elif "-- Passed! ***" in line:
                    self.tests_passed += 1

                elif "-- Failed! ***" in line:
                    self.tests_failed += 1        

                elif "Takes seconds to complete:" in line:
                    # Extract the numerical part of the duration more accurately
                    try:
                        duration_str = line.split("Takes seconds to complete:")[1].strip()
                        duration_seconds = int(duration_str)
                        self.test_durations.append(duration_seconds)
                    except ValueError as e:
                        print(f"Error processing line for duration: '{line.strip()}'. Error: {e}")


    def getSerialNum(self):
        return self.first_line[self.first_line.find("['")+2:self.first_line.find("']")]
    
    def getThingGrp(self):
        return self.second_line[self.second_line.find("['")+2:self.second_line.find("']")]

    def getPassed(self):
        return self.tests_passed
    
    def getFailed(self):
        return self.tests_failed

    def getMin(self):
        return min(self.test_durations)
    
    def getMax(self):
        return max(self.test_durations)

    def getAvg(self):
        total = sum(self.test_durations)
        return total // len(self.test_durations)

    def calculateRunTotals(self):
        # Calculating totals
        total_runs = len(self.run_details)
        total_sub_runs = sum(len(sub_runs) for sub_runs in self.run_details.values())
        return total_runs, total_sub_runs

    def calculateDuration(self):
        # Calculate total duration
        for run_key, start_time in self.start_times.items():

            if run_key in self.end_times:
                #self.total_duration_seconds += (self.end_times[run_key] - start_time).total_seconds()
                self.total_duration_seconds += (self.end_times[run_key] - start_time)
                self.total_duration_seconds += 60

        return self.total_duration_seconds
    
    def convertSQL(self, line, placeholder, replacement):
        try:
            pattern = re.escape(placeholder)
            line = re.sub(pattern, replacement, line)
        except Exception as e:
            print(f"Exception in converting SQL: {e}")    
        return line

    def queryServerName(self, sn):
        pass

    def queryFKeyReportT(self, oscarT, buildN): 
        vSql = self.convertSQL(sqlsDash.report_fk_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)[0][0]

    def queryFKeyServerT(self, serverN):
        vSql = self.convertSQL(sqlsDash.server_fk_q, '[serverN]', serverN)
        return  self.queryData(vSql)[0][0]

    def queryFKeyDeviceT(self, sn):
        vSql = self.convertSQL(sqlsDash.device_fk_q, '[SN]', sn)
        return  self.queryData(vSql)[0][0]

    def queryJira(self, oscarT, buildN):
        vSql = self.convertSQL(sqlsDash.jiras_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)

    def queryBlocker(self, oscarT, buildN):
        vSql = self.convertSQL(sqlsDash.blockers_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)

    def queryNotes(self, oscarT, buildN):
        vSql = self.convertSQL(sqlsDash.build_notes_q, '[oscarT]', oscarT)
        vSql = self.convertSQL(vSql, '[buildN]', buildN)
        return  self.queryData(vSql)[0][0]

    def fetchFailedNum(self, sn, grp):
        # temparary hard-codes the failed number
        # TODO: fetch AWS API for it
        return 0
        

    def fetchRetryPassNum(self, sn, grp):
        # temparary hard-codes the Retries Pass number
        # TODO: fetch AWS API for it
        return 0


    def extractFilename(self, path):
        # Extract the filename from the given path
        filename = os.path.basename(path)
        return filename

    # DGO OP
    def getDGOPassedFailed(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                #print("line= ", line)
                # Check if the line starts with the specific run marker
                if line.startswith("RUN COUNT:"):
                    #print("AA")
                    self.dgo_run_count += 1
                # Check for passed tests
                elif line.startswith("PASSED"):
                    self.dgo_passed += 1
                # Check for failed tests
                elif line.startswith("FAILED"):
                    self.dgo_failed += 1

                elif "in" in line and "s (" in line and ") ============" in line:
                    # Extract the time in seconds from the line
                    time_str = line.split("in")[1].split("s")[0].strip()
                    self.dgo_total_time += float(time_str)


        return self.dgo_passed, self.dgo_failed    

    def getRepeatedCount(self):
        return self.dgo_run_count

    def getTotalTime(self):
        return self.dgo_total_time 
    

    # DGO MASS
    def getPassedFailed(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                #print("line= ", line)
                # Check if the line starts with the specific run marker
                if line.startswith("RUN COUNT:"):
                    #print("AA")
                    self.dgo_run_count += 1
                # Check for passed tests
                elif line.startswith("PASSED"):
                    self.dgo_passed += 1
                # Check for failed tests
                elif line.startswith("FAILED"):
                    self.dgo_failed += 1

                elif "in" in line and "s (" in line and ") ============" in line:
                    # Extract the time in seconds from the line
                    # print("line= ", line)
                    # print("line.split(" in ")= ", line.split("in"))
                    # print('line.split(" in ")[1].split("s")= ', line.split("in")[1].split("s"))
                    time_str = line.split(" in ")[1].split("s")[0].strip()
                    # print("time_str= ", time_str)
                    self.dgo_total_time += float(time_str)

                elif "in" in line and "s =================" in line:
                    time_match = re.search(r"in (\d+\.?\d*)s", line)
                    if time_match:
                        self.dgo_total_time += float(time_match.group(1))

        return self.dgo_passed, self.dgo_failed    



    def ProcessOTA(self, vFile, vBuild, vSVR, vSN):
        fileName = parseObj.extractFilename(vFile)
        print("fileName= ", fileName)
        parts = fileName.split('_')
        print("parts= ", parts)

        if parts[1] == 'ota':
            self.parseOTAFile(vFile)
            total_runs, total_sub_runs = self.calculateRunTotals()
            total_duration_seconds = self.calculateDuration()
            tests_passed = self.getPassed()
            tests_failed = self.getFailed()
            min_duration_seconds = self.getMin()
            max_duration_seconds = self.getMax()
            average_duration_seconds = self.getAvg()
            sn = self.getSerialNum()
            thingGrp = self.getThingGrp()


            results = {}
            results["Build"] = vBuild
            results["Oscar"] = parts[0]
            results["ThingSN"] = sn
            results["ThingGroup"] = thingGrp
            results["Server"] =  vSVR
            results["TestExecuted"] = (tests_passed + tests_failed) // total_runs // 2
            results["Passed"] = tests_passed // total_runs // 2
            results["Failed"] = tests_failed
            results["ExeTime"] = average_duration_seconds * total_sub_runs
            results["Repeats"] = total_runs

            results["MinT"] = min_duration_seconds
            results["MaxT"] = max_duration_seconds
            results["AvgT"] = average_duration_seconds

            if parts[2] == 'self':
                results["TestType"] = 'self'
                results["TCLink"] = TSLink.OTA
                results["Tbl"] = DBT.OTA_TABLE
            elif parts[2] == 'prod':
                results["TestType"] = 'prodUG'
                results["TCLink"] = TSLink.OTA
                results["Tbl"] = DBT.OTA_TABLE
            elif parts[2] == 'int':
                results["TestType"] = 'intFTUG'
                results["TCLink"] = TSLink.OTA
                results["Tbl"] = DBT.OTA_TABLE
            elif parts[2] == 'ext':
                results["TestType"] = 'extFTUG'
                results["TCLink"] = TSLink.OTA
                results["Tbl"] = DBT.OTA_TABLE
            elif parts[2] == 'power':
                results["TestType"] = 'power'    
                results["TCLink"] = TSLink.OTA_POWER
                results["Tbl"] = DBT.POWER_DURING_OTA_TABLE    
            else:
                print("Invalid Type: ", parts[2])

            results["RLink"] = './' + self.extract_filename(vFile)
            print("AAAAAA")
            results["DebugLink"] = 'guo'
            results["Notes"] = self.queryNotes(parts[0], vBuild)
            print("AAAAAA222222")

            print("vBuild= ", vBuild)
            print("parts[0]= ", parts[0])
            results["ReportId"] = self.queryFKeyReportT(parts[0], vBuild)
            print('results["ReportId"]= ', results["ReportId"])



            results["SvrId"] = self.queryFKeyServerT(vSVR)
            print('results["SvrId"]= ', results["SvrId"])

            results["DevId"] = self.queryFKeyDeviceT(vSN)
            print('results["DevId"]= ', results["DevId"])


            jiras = self.queryJira(parts[0], vBuild)
            results["Jira1"] = jiras[0][0]
            results["Jira2"] = jiras[0][1]
            results["Jira3"] = jiras[0][2]



            blockerF = self.queryBlocker(parts[0], vBuild)
            results["JiraF1"] = blockerF[0][1]
            results["JiraF2"] = blockerF[0][3]
            results["JiraF3"] = blockerF[0][5]

            results["failedNum"] = self.fetchFailedNum(sn, thingGrp)
            results["repPass"] = self.fetchRetryPassNum(sn, thingGrp)


            print("results= ", results)
            print("======================AA===========================")


    def ProcessDGO(self, vFile, vBuild, vSVR, vSN):
        fileName = parseObj.extractFilename(vFile)
        print("fileName= ", fileName)
        parts = fileName.split('_')
        print("parts= ", parts)
    
        if parts[1] == 'dgo' or parts[1] == 'eeprom' or parts[1] == 'pairing' or parts[1] == 'start' \
                or parts[1] == 'child' or parts[1] == 'lid' or parts[1] == 'safety' or parts[1] == 'boot':
        
            passed, failed = parseObj.getPassedFailed(args.vFile)
            runs = parseObj.getRepeatedCount()
            totalT = parseObj.getTotalTime()
            print("passed= ", passed / runs)
            print("failed= ", failed / runs)
            print("runs= ", runs)
            print("totalT= ", totalT)
            print("AvgT= ", totalT / runs)

            results = {}
            results["Build"] = vBuild
            results["Oscar"] = parts[0]
            results["ThingSN"] = vSN
            results["ThingGroup"] = ""
            results["Server"] =  vSVR
            results["TestExecuted"] = (passed // runs) + (failed // runs)
            results["Passed"] = passed // runs
            results["Failed"] = failed // runs
            results["ExeTime"] = totalT // runs
            results["Repeats"] = runs

            if parts[1] == 'dgo':
                if parts[2] == 'idle':
                    results["TestType"] = 'idle'
                    if parts[3] == 'op':
                        results["TCLink"] = TSLink.O1_DGO_OP_IDLE
                        results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    elif parts[3] == 'mass':
                        results["TCLink"] = TSLink.O1_DGO_MASS_IDLE
                        results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    else:
                        print("Invalid Type: ", parts[3])

                elif parts[2] == 'lip':
                    results["TestType"] = 'lip'
                    if parts[3] == 'op':
                        results["TCLink"] = TSLink.O1_DGO_OP_LIP
                        results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    elif parts[3] == 'mass':
                        results["TCLink"] = TSLink.O1_DGO_MASS_LIP
                        results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    else:
                        print("Invalid Type: ", parts[3])

                elif parts[2] == 'hip':
                    results["TestType"] = 'hip'
                    if parts[3] == 'op':
                        results["TCLink"] = TSLink.O1_DGO_OP_HIP
                        results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    elif parts[3] == 'mass':
                        results["TCLink"] = TSLink.O1_DGO_MASS_HIP
                        results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    else:
                        print("Invalid Type: ", parts[3])

                elif parts[2] == 'cooldown':
                    results["TestType"] = 'cooldown'
                    if parts[3] == 'op':
                        results["TCLink"] = TSLink.O1_DGO_OP_COOLDOWN
                        results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    elif parts[3] == 'mass':
                        results["TCLink"] = TSLink.O1_DGO_MASS_COOLDOWN
                        results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    else:
                        print("Invalid Type: ", parts[3])

                elif parts[2] == 'fluff':
                    results["TestType"] = 'fluff'
                    if parts[3] == 'op':
                        results["TCLink"] = TSLink.O1_DGO_OP_FLUFF
                        results["Tbl"] = DBT.DGO_OP_PR_TABLE
                    elif parts[3] == 'mass':
                        results["TCLink"] = TSLink.O1_DGO_MASS_FLUFF
                        results["Tbl"] = DBT.DGO_ADD_MASS_TABLE
                    else:
                        print("Invalid Type: ", parts[3])
                else:
                    print("Invalid Type: ", parts[2])

            elif parts[1] == 'eeprom':
                results["TestType"] = None
                results["TCLink"] = TSLink.EEPROM
                results["Tbl"] = DBT.EEPROM_STRESS_TEST_TABLE
            elif parts[1] == 'pairing':
                results["TestType"] = None
                results["TCLink"] = TSLink.O1_PAIRING
                results["Tbl"] = DBT.PAIRING_WITHOUT_BLE_TABLE         
            elif parts[1] == 'start':
                if parts[4] == 'A':
                    results["TestType"] = 'stress'
                    results["TCLink"] = TSLink.O1_STARTA
                    results["Tbl"] = DBT.START_VIA_BIN_TABLE          
                elif parts[4] == 'B':    
                    results["TestType"] = 'normal'
                    results["TCLink"] = TSLink.O1_STARTB
                    results["Tbl"] = DBT.START_VIA_BIN_TABLE     
                else:
                    print("Invalid Type: ", parts[4])

            elif parts[1] == 'child':
                if parts[3] == 'A':
                    results["TestType"] = 'stress'
                    results["TCLink"] = TSLink.O1_CHILDA
                    results["Tbl"] = DBT.CHILD_LOCK_TABLE          
                elif parts[3] == 'B':    
                    results["TestType"] = 'normal'
                    results["TCLink"] = TSLink.O1_CHILDB
                    results["Tbl"] = DBT.CHILD_LOCK_TABLE     
                else:
                    print("Invalid Type: ", parts[3])

            elif parts[1] == 'lid':
                results["TestType"] = None
                results["TCLink"] = TSLink.O1_LID
                results["Tbl"] = DBT.LID_OPEN_CLOSE_TABLE   

            elif parts[1] == 'safety':
                results["TestType"] = None
                results["TCLink"] = TSLink.O1_SAFETY
                results["Tbl"] = DBT.SAFETY_TEST_TABLE   

            elif parts[1] == 'boot':
                if parts[3] == 'A':
                    results["TestType"] = 'stress'
                    results["TCLink"] = TSLink.O1_BOOTA
                    results["Tbl"] = DBT.BOOT_CYCLE_TABLE          
                elif parts[3] == 'B':    
                    results["TestType"] = 'normal'
                    results["TCLink"] = TSLink.O1_BOOTB
                    results["Tbl"] = DBT.BOOT_CYCLE_TABLE     
                else:
                    print("Invalid Type: ", parts[3])


            results["RLink"] = './' + parseObj.extract_filename(args.vFile)
            results["DebugLink"] = ''

            print("vBuild= ", vBuild)
            print("parts[0]= ", parts[0])
            results["ReportId"] = self.queryFKeyReportT(parts[0], vBuild)
            print('results["ReportId"]= ', results["ReportId"])



            results["SvrId"] = self.queryFKeyServerT(vSVR)
            print('results["SvrId"]= ', results["SvrId"])

            results["DevId"] = self.queryFKeyDeviceT(vSN)
            print('results["DevId"]= ', results["DevId"])


            jiras = self.queryJira(parts[0], vBuild)
            results["Jira1"] = jiras[0][0]
            results["Jira2"] = jiras[0][1]
            results["Jira3"] = jiras[0][2]



            blockerF = self.queryBlocker(parts[0], vBuild)
            results["JiraF1"] = blockerF[0][1]
            results["JiraF2"] = blockerF[0][3]
            results["JiraF3"] = blockerF[0][5]


            print("results= ", results)

            print("=======================BB==========================")
















if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')

    parser.add_argument('vFile', type=str, nargs='?', help='', default=None)
    parser.add_argument('vSN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vSVR', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuild', type=str, nargs='?', help='', default=None)
    args = parser.parse_args()


    
    db = "pi"
    host = "127.0.0.1" 
    user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"
    parseObj = ParseData(db, host, user, passwd, port, False)
    parseObj.connectToPostDB()
    parseObj.getCursor()   

    print("vFile", args.vFile)
    print("vSN", args.vSN)
    print("vSVR", args.vSVR)
    print("vBuild", args.vBuild)

    # rrr = parseObj.queryFKeyReportT("O2", "dbg-v01.05.05-19dc16c")
    # print("rrr= ", rrr)


    # rrr2 = parseObj.queryFKeyServerT("qa3")
    # print("rrr2= ", rrr2)


    # rrr3 = parseObj.queryFKeyDeviceT("MG22332A2US0019")
    # print("rrr3= ", rrr3)




    # rrr4 = parseObj.queryJira("O2", "dbg-v01.05.05-19dc16c")
    # print("rrr4= ", rrr4)


    # rrr5 = parseObj.queryBlocker("O2", "dbg-v01.05.05-19dc16c")
    # print("rrr5= ", rrr5)



    parseObj.ProcessOTA(args.vFile, args.vBuild, args.vSVR, args.vSN)

    parseObj.ProcessDGO(args.vFile, args.vBuild, args.vSVR, args.vSN)

    