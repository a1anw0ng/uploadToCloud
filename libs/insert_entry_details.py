
import argparse
from millPostDB import millPostDB

class InsertData(millPostDB):
    def __init__(self, database, host, user, password, port, sysLogF):
        super().__init__(database, host, user, password, port, sysLogF)

    @staticmethod
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')

    parser.add_argument('vTable', type=str, nargs='?', help='', default=None)
    parser.add_argument('vAction', type=str, nargs='?', help='', default=None)
    parser.add_argument('vTemplateN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vOscarType', type=str, nargs='?', help='', default=None)
    parser.add_argument('vSvrName', type=str, nargs='?', help='', default=None)
    parser.add_argument('vThingSN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vOscarId', type=str, nargs='?', help='', default=0)
    parser.add_argument('vSvrId', type=str, nargs='?', help='', default=0)
    parser.add_argument('vDeviceId', type=str, nargs='?', help='', default=0)
    parser.add_argument('vTestExecuted', type=str, nargs='?', help='', default=0)
    parser.add_argument('vPassed', type=str, nargs='?', help='', default=0)
    parser.add_argument('vFailed', type=str, nargs='?', help='', default=0)
    parser.add_argument('vExeTime', type=str, nargs='?', help='', default=None)
    parser.add_argument('vRepeats', type=str, nargs='?', help='', default=0)
    parser.add_argument('vJira1', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraF1', type=InsertData.str2bool, nargs='?', const=True, default=False)
    parser.add_argument('vJira2', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraF2', type=InsertData.str2bool, nargs='?', const=True, default=False)
    parser.add_argument('vJira3', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraF3', type=InsertData.str2bool, nargs='?', const=True, default=False)
    parser.add_argument('vResultLink', type=str, nargs='?', help='', default=None)
    parser.add_argument('vTestCasesLink', type=str, nargs='?', help='', default=None)
    args = parser.parse_args()

    print("vJiraF1= ", args.vJiraF1)
    print("vJiraF2= ", args.vJiraF2)
    print("vJiraF3= ", args.vJiraF3)

    db = "pi"
    host = "127.0.0.1" 
    user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"
    insertObj = InsertData(db, host, user, passwd, port, False)
    insertObj.connectToPostDB()
    insertObj.getCursor()

    if args.vAction == "query":   
        select_query = f"""select * from {args.vTable} where TemplateN = '{args.vTemplateN}' and OscarType = '{args.vOscarType}'"""

        ret = insertObj.queryData(select_query)
        if ret:
            print(f"tabele: '{args.vTable}' => '{args.vOscarType}' and '{args.vTemplateN}' ", ret)


    elif args.vAction == "insert":   
        insert_query = """INSERT INTO {} (TemplateN, OscarType, SvrName, ThingSN, OscarId, SvrId,  
                    DeviceId, TestExecuted, Passed, Failed, ExeTime, Repeats, Jira1, JiraF1, Jira2, JiraF2, 
                    Jira3, JiraF3, ResultLink, TestCasesLink)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""".format(args.vTable)

        if insertObj.insertRowData(insert_query, (args.vTemplateN, args.vOscarType, args.vSvrName, args.vThingSN, args.vOscarId, args.vSvrId,  
                        args.vDeviceId, args.vTestExecuted, args.vPassed, args.vFailed, args.vExeTime, args.vRepeats, args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, 
                        args.vJira3, args.vJiraF3, args.vResultLink, args.vTestCasesLink)):
            print(f"insert tabele: '{args.vTable}' => '{args.vOscarType}' and '{args.vTemplateN}' data successful!")
        else:
            print(f"insert tabele: '{args.vTable}' => '{args.vOscarType}' and '{args.vTemplateN}' data failed!")

    elif args.vAction == "update":
        update_query = f"""UPDATE {args.vTable} 
                SET TemplateN = %s, OscarType = %s, SvrName = %s, ThingSN = %s, OscarId = %s, SvrId = %s, 
                DeviceId = %s, TestExecuted = %s, Passed = %s, Failed = %s, ExeTime = %s, Repeats = %s, 
                Jira1 = %s, JiraF1 = %s, Jira2 = %s, JiraF2 = %s, Jira3 = %s, JiraF3 = %s, ResultLink = %s, TestCasesLink = %s
                WHERE OscarType = %s AND TemplateN = %s;"""

        values = (args.vTemplateN, args.vOscarType, args.vSvrName, args.vThingSN, args.vOscarId, args.vSvrId, args.vDeviceId, args.vTestExecuted, 
                args.vPassed, args.vFailed, args.vExeTime, args.vRepeats, args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, 
                args.vJiraF3, args.vResultLink, args.vTestCasesLink, args.vOscarType, args.vTemplateN)

        if insertObj.updateRowData2(update_query, values):
            print(f"update tabele: '{args.vTable}' => '{args.vOscarType}' and '{args.vTemplateN}' data successful!")
        else:
            print(f"update tabele: '{args.vTable}' => '{args.vOscarType}' and '{args.vTemplateN}' data failed!")

