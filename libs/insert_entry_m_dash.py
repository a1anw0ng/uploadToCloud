
import argparse
from millPostDB import millPostDB



class InsertMDashData(millPostDB):
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


#parser.add_argument('--vJiraF1', type=str2bool, nargs='?', const=True, default=False, help='Description of vJiraF1')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')

    parser.add_argument('vTable', type=str, nargs='?', help='', default=None)
    parser.add_argument('vAction', type=str, nargs='?', help='', default=None)
    parser.add_argument('vOscar', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildDate', type=str, nargs='?', help='', default=None)
    parser.add_argument('vTemplateN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vCodeN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildType', type=str, nargs='?', help='', default=None)
    parser.add_argument('vProdRelTemplate', type=str, nargs='?', help='', default=None)
    parser.add_argument('vProdRelversion', type=str, nargs='?', help='', default=None)
    parser.add_argument('vExtFTRelTemplate', type=str, nargs='?', help='', default=None)
    parser.add_argument('vExtFTRelVersion', type=str, nargs='?', help='', default=None)
    parser.add_argument('vIntFTRelTemplate', type=str, nargs='?', help='', default=None)
    parser.add_argument('vIntFTRelVersion', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildId', type=str, nargs='?', help='', default=None)
    parser.add_argument('vStatusId', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraId', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildStatus', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJira1', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraF1', type=InsertMDashData.str2bool, nargs='?', const=True, default=False)
    parser.add_argument('vJira2', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraF2', type=InsertMDashData.str2bool, nargs='?', const=True, default=False)
    parser.add_argument('vJira3', type=str, nargs='?', help='', default=None)
    parser.add_argument('vJiraF3', type=InsertMDashData.str2bool, nargs='?', const=True, default=False)
    parser.add_argument('BuildNotes', type=str, nargs='?', help='', default=None)
    parser.add_argument('ClsStatus', type=str, nargs='?', help='', default=None)
    parser.add_argument('BuildLink', type=str, nargs='?', help='', default=None)



    # parser.add_argument('vTable', type=str, help='')
    # parser.add_argument('vAction', type=str, help='')
    # parser.add_argument('vOscar', type=str, help='')
    # parser.add_argument('--vBuildDate', type=str, help='', required=False)
    # parser.add_argument('--vTemplateN', type=str, help='', required=False)
    # parser.add_argument('--vBuildN', type=str, help='', required=False)
    # parser.add_argument('--vCodeN', type=str, help='', required=False)
    # parser.add_argument('--vBuildType', type=str, help='', required=False)
    # parser.add_argument('--vProdRelTemplate', type=str, help='', required=False)
    # parser.add_argument('--vProdRelversion', type=str, help='', required=False)
    # parser.add_argument('--vExtFTRelTemplate', type=str, help='', required=False)
    # parser.add_argument('--vExtFTRelVersion', type=str, help='', required=False)
    # parser.add_argument('--vIntFTRelTemplate', type=str, help='', required=False)
    # parser.add_argument('--vIntFTRelVersion', type=str, help='', required=False)
    # parser.add_argument('--vBuildId', type=str, help='', required=False)
    # parser.add_argument('--vStatusId', type=str, help='', required=False)
    # parser.add_argument('--vJiraId', type=str, help='', required=False)
    # parser.add_argument('--vBuildStatus', type=str, help='', required=False)
    # parser.add_argument('--vJira1', type=str, help='', required=False)
    # parser.add_argument('--vJiraF1', action='store_true', help='', required=False)
    # parser.add_argument('--vJira2', type=str, help='', required=False)
    # parser.add_argument('--vJiraF2', action='store_true', help='', required=False)
    # parser.add_argument('--vJira3', type=str, help='', required=False)
    # parser.add_argument('--vJiraF3', action='store_true', help='', required=False)
    # parser.add_argument('--BuildNotes', type=str, help='', required=False)
    # parser.add_argument('--ClsStatus', type=str, help='', required=False)
    # parser.add_argument('--BuildLink', type=str, help='', required=False)
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

    if args.vAction == "insert":
        insert_query = """INSERT INTO {} (Oscar, BuildDate, TemplateN, BuildN, CodeN, BuildType, ProdRelTemplate, ProdRelversion, ExtFTRelTemplate, ExtFTRelVersion, IntFTRelTemplate,  
                        IntFTRelVersion, BuildId, StatusId, JiraId, BuildStatus, Jira1, JiraF1, Jira2, JiraF2, Jira3, JiraF3, BuildNotes, ClsStatus, BuildLink)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""".format(args.vTable)

        if insertObj.insertRowData(insert_query, (args.vOscar, args.vBuildDate, args.vTemplateN, args.vBuildN, args.vCodeN, args.vBuildType, args.vProdRelTemplate, args.vProdRelversion,  
                        args.vExtFTRelTemplate, args.vExtFTRelVersion, args.vIntFTRelTemplate, args.vIntFTRelVersion, args.vBuildId, args.vStatusId, args.vJiraId, args.vBuildStatus,     
                        args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, args.vJiraF3, args.BuildNotes, args.ClsStatus, args.BuildLink)):

            print(f"insert tabele: '{args.vTable}' => '{args.vOscar}' and '{args.vTemplateN}' data successful!")
        else:
            print(f"insert tabele: '{args.vTable}' => '{args.vOscar}' and '{args.vTemplateN}' data failed!")

    elif args.vAction == "update":
        update_query = f"""UPDATE {args.vTable} 
                SET Oscar = %s, BuildDate = %s, TemplateN = %s, BuildN = %s, CodeN = %s, BuildType = %s, 
                ProdRelTemplate = %s, ProdRelversion = %s, ExtFTRelTemplate = %s, ExtFTRelVersion = %s, 
                IntFTRelTemplate = %s, IntFTRelVersion = %s, BuildId = %s, StatusId = %s, JiraId = %s, 
                BuildStatus = %s, Jira1 = %s, JiraF1 = %s, Jira2 = %s, JiraF2 = %s, Jira3 = %s, 
                JiraF3 = %s, BuildNotes = %s, ClsStatus = %s, BuildLink = %s 
                WHERE Oscar = %s AND TemplateN = %s;"""

        values = (args.vOscar, args.vBuildDate, args.vTemplateN, args.vBuildN, args.vCodeN, args.vBuildType, 
                args.vProdRelTemplate, args.vProdRelversion, args.vExtFTRelTemplate, args.vExtFTRelVersion, 
                args.vIntFTRelTemplate, args.vIntFTRelVersion, args.vBuildId, args.vStatusId, args.vJiraId, 
                args.vBuildStatus, args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, 
                args.vJiraF3, args.BuildNotes, args.ClsStatus, args.BuildLink, args.vOscar, args.vTemplateN)

        if insertObj.updateRowData2(update_query, values):
            print(f"update tabele: '{args.vTable}' => '{args.vOscar}' and '{args.vTemplateN}' data successful!")
        else:
            print(f"update tabele: '{args.vTable}' => '{args.vOscar}' and '{args.vTemplateN}' data failed!")

    elif args.vAction == "query":

        select_query = f"""select * from {args.vTable} where Oscar = '{args.vOscar}' and TemplateN = '{args.vTemplateN}'"""

        ret = insertObj.queryData(select_query)
        if ret:
            print(f"tabele: '{args.vTable}' => '{args.vOscar}' and '{args.vTemplateN}' ", ret)
        