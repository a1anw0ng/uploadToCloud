
from ParsingResults import ParseData
import argparse


class InsertMDashData:
    def __init__(self):
        pass

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

    args = parser.parse_args()

    print("vJiraF1= ", args.vJiraF1)
    print("vJiraF2= ", args.vJiraF2)
    print("vJiraF3= ", args.vJiraF3)

    db = "pi"
    host = "100.117.244.108"    # host = "127.0.0.1"
    user = "pi"           # user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"
    parseObj = ParseData(db, host, user, passwd, port, False)
    parseObj.connectToPostDB()
    parseObj.getCursor()   

    if args.vAction == "insert":
        data = (args.vOscar, args.vBuildDate, args.vTemplateN, args.vBuildN, args.vCodeN, args.vBuildType, args.vProdRelTemplate, args.vProdRelversion,  
                        args.vExtFTRelTemplate, args.vExtFTRelVersion, args.vIntFTRelTemplate, args.vIntFTRelVersion, args.vBuildId, args.vStatusId, args.vJiraId, args.vBuildStatus,     
                        args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, args.vJiraF3, args.BuildNotes, args.ClsStatus, args.BuildLink)
        parseObj.insertReportEntry(args.vTable, data, args.vOscar, args.vTemplateN)

    elif args.vAction == "update":

        values = (args.vOscar, args.vBuildDate, args.vTemplateN, args.vBuildN, args.vCodeN, args.vBuildType, 
                args.vProdRelTemplate, args.vProdRelversion, args.vExtFTRelTemplate, args.vExtFTRelVersion, 
                args.vIntFTRelTemplate, args.vIntFTRelVersion, args.vBuildId, args.vStatusId, args.vJiraId, 
                args.vBuildStatus, args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, 
                args.vJiraF3, args.BuildNotes, args.ClsStatus, args.BuildLink, args.vOscar, args.vTemplateN)

        parseObj.updateReportEntry(args.vTable, values, args.vOscar, args.vTemplateN)

    elif args.vAction == "query":
        parseObj.selectReportEntry(args.vTable, args.vOscar, args.vTemplateN)

        