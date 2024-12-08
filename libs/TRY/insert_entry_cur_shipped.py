
import argparse
from millPostDB import millPostDB

class InsertMDashData(millPostDB):
    def __init__(self, database, host, user, password, port, sysLogF):
        super().__init__(database, host, user, password, port, sysLogF)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')

    parser.add_argument('vTable', type=str, help='')
    parser.add_argument('vOscar', type=str, help='')
    parser.add_argument('vBuildDate', type=str, help='')
    parser.add_argument('vTemplateN', type=str, help='')
    parser.add_argument('vBuildN', type=str, help='')
    parser.add_argument('vCodeN', type=str, help='')
    parser.add_argument('vBuildType', type=str, help='')
    parser.add_argument('vProdRelTemplate', type=str, help='')
    parser.add_argument('vProdRelversion', type=str, help='')
    parser.add_argument('vExtFTRelTemplate', type=str, help='')
    parser.add_argument('vExtFTRelVersion', type=str, help='')
    parser.add_argument('vIntFTRelTemplate', type=str, help='')
    parser.add_argument('vIntFTRelVersion', type=str, help='')
    parser.add_argument('vBuildId', type=str, help='')
    parser.add_argument('vStatusId', type=str, help='')
    parser.add_argument('vJiraId', type=str, help='')
    parser.add_argument('vBuildStatus', type=str, help='')
    parser.add_argument('vJira1', type=str, help='')
    parser.add_argument('--vJiraF1', action='store_true', help='')
    parser.add_argument('vJira2', type=str, help='')
    parser.add_argument('--vJiraF2', action='store_true', help='')
    parser.add_argument('vJira3', type=str, help='')
    parser.add_argument('--vJiraF3', action='store_true', help='')
    parser.add_argument('BuildNotes', type=str, help='')
    parser.add_argument('ClsStatus', type=str, help='')
    parser.add_argument('BuildLink', type=str, help='')
    args = parser.parse_args()

    print("vJiraF1= ", args.vJiraF1)
    print("vJiraF2= ", args.vJiraF2)
    print("vJiraF3= ", args.vJiraF3)

    db = "pi"
    host = "127.0.0.1" 
    user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"
    insertObj = InsertMDashData(db, host, user, passwd, port, False)
    insertObj.connectToPostDB()
    insertObj.getCursor()

    insert_query = """INSERT INTO {} (Oscar, BuildDate, TemplateN, BuildN, CodeN, BuildType, ProdRelTemplate, ProdRelversion, ExtFTRelTemplate, ExtFTRelVersion, IntFTRelTemplate,  
                    IntFTRelVersion, BuildId, StatusId, JiraId, BuildStatus, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, BuildNotes, ClsStatus, BuildLink)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""".format(args.vTable)

    ret = insertObj.insertRowData(insert_query, (args.vOscar, args.vBuildDate, args.vTemplateN, args.vBuildN, args.vCodeN, args.vBuildType, args.vProdRelTemplate, args.vProdRelversion,  
                    args.vExtFTRelTemplate, args.vExtFTRelVersion, args.vIntFTRelTemplate, args.vIntFTRelVersion, args.vBuildId, args.vStatusId, args.vJiraId, args.vBuildStatus,     
                    args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, args.vJiraF3, args.BuildNotes, args.ClsStatus, args.BuildLink))

    if ret:
        print("insert data successful!")
    else:
        print("insert data failed!")

