
import argparse
from ParsingResults import ParseData

# class InsertMDashData(millPostDB):
#     def __init__(self, database, host, user, password, port, sysLogF):
#         super().__init__(database, host, user, password, port, sysLogF)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')

    parser.add_argument('vTable', type=str, nargs='?', help='', default=None)
    parser.add_argument('vAction', type=str, nargs='?', help='', default=None)
    parser.add_argument('vOscar', type=str, nargs='?', help='', default=None)
    parser.add_argument('vCodeN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildType', type=str, nargs='?', help='', default=None)
    parser.add_argument('vProdRelT', type=str, nargs='?', help='', default=None)
    parser.add_argument('vProdRelV', type=str, nargs='?', help='', default=None)
    parser.add_argument('vExtFTRelT', type=str, nargs='?', help='', default=None)
    parser.add_argument('vExtFTRelV', type=str, nargs='?', help='', default=None)
    parser.add_argument('vIntFTRelT', type=str, nargs='?', help='', default=None)
    parser.add_argument('vIntFTRelV', type=str, nargs='?', help='', default=None)


    parser.add_argument('DayOImgT', type=str, nargs='?', help='', default=None)
    parser.add_argument('DayOImgV', type=str, nargs='?', help='', default=None)
    parser.add_argument('FFUImgT', type=str, nargs='?', help='', default=None)
    parser.add_argument('FFUImgV', type=str, nargs='?', help='', default=None)

    parser.add_argument('AutoOTAT', type=str, nargs='?', help='', default=None)
    parser.add_argument('AutoOTAV', type=str, nargs='?', help='', default=None)
    parser.add_argument('FactoryImg', type=str, nargs='?', help='', default=None)
    parser.add_argument('DiagImg', type=str, nargs='?', help='', default=None)


    parser.add_argument('UserGrp1T', type=str, nargs='?', help='', default=None)
    parser.add_argument('UserGrp1V', type=str, nargs='?', help='', default=None)
    parser.add_argument('UserGrp2T', type=str, nargs='?', help='', default=None)
    parser.add_argument('UserGrp2V', type=str, nargs='?', help='', default=None)
    parser.add_argument('UserGrp3T', type=str, nargs='?', help='', default=None)
    parser.add_argument('UserGrp3V', type=str, nargs='?', help='', default=None)

    args = parser.parse_args()


    db = "pi"
    host = "127.0.0.1" 
    user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"
    parseObj = ParseData(db, host, user, passwd, port, False)
    parseObj.connectToPostDB()
    parseObj.getCursor()   

    if args.vAction == "query":
        parseObj.selectCurShippedEntry(args.vTable, args.vOscar)


        # select_query = f"""select * from {args.vTable} where Oscar = '{args.vOscar}' ORDER BY CreatedAt DESC LIMIT 1"""

        # ret = parseObj.queryData(select_query)
        # if ret:
        #     print("ret= ", ret)



    elif args.vAction == "insert":
        # data = (args.vOscar, args.vBuildDate, args.vTemplateN, args.vBuildN, args.vCodeN, args.vBuildType, args.vProdRelTemplate, args.vProdRelversion,  
        #                 args.vExtFTRelTemplate, args.vExtFTRelVersion, args.vIntFTRelTemplate, args.vIntFTRelVersion, args.vBuildId, args.vStatusId, args.vJiraId, args.vBuildStatus,     
        #                 args.vJira1, args.vJiraF1, args.vJira2, args.vJiraF2, args.vJira3, args.vJiraF3, args.BuildNotes, args.ClsStatus, args.BuildLink)
        
        data = (args.vOscar, args.vCodeN, args.vBuildType, args.vProdRelT, args.vProdRelV, args.vExtFTRelT, args.vExtFTRelV, args.vIntFTRelT, args.vIntFTRelV, 
                args.DayOImgT, args.DayOImgV, args.FFUImgT, args.FFUImgV, args.AutoOTAT, args.AutoOTAV, args.FactoryImg, args.DiagImg, args.UserGrp1T, args.UserGrp1V, args.UserGrp2T, args.UserGrp2V, args.UserGrp3T, args.UserGrp3V)

        parseObj.insertCurShippedEntry(args.vTable, data, args.vOscar)



        # insert_query = """INSERT INTO {} (Oscar, CodeN, BuildType, ProdRelT, ProdRelV, ExtFTRelT, ExtFTRelV, IntFTRelT, IntFTRelV, DayOImgT, DayOImgV, FFUImgT, FFUImgV, 
        #                 AutoOTAT, AutoOTAV, FactoryImg, DiagImg, UserGrp1T, UserGrp1V, UserGrp2T, UserGrp2V, UserGrp3T, UserGrp3V)
        #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""".format(args.vTable)

        # ret = parseObj.insertRowData(insert_query, (args.vOscar, args.vCodeN, args.vBuildType, args.vProdRelT, args.vProdRelV, args.vExtFTRelT, args.vExtFTRelV, args.vIntFTRelT, args.vIntFTRelV, 
        #                 args.DayOImgT, args.DayOImgV, args.FFUImgT, args.FFUImgV, args.AutoOTAT, args.AutoOTAV, args.FactoryImg, args.DiagImg, args.UserGrp1T, args.UserGrp1V, args.UserGrp2T, args.UserGrp2V, args.UserGrp3T, args.UserGrp3V))
        # if ret:
        #     print("insert data successful!")
        # else:
        #     print("insert data failed!")
    elif args.vAction == "update":

        values = (args.vOscar, args.vOscar, args.vCodeN, args.vBuildType, args.vProdRelT, args.vProdRelV, args.vExtFTRelT, args.vExtFTRelV, 
                  args.vIntFTRelT, args.vIntFTRelV, args.DayOImgT, args.DayOImgV, args.FFUImgT, args.FFUImgV, args.AutoOTAT, args.AutoOTAV, args.FactoryImg, args.DiagImg,
                  args.UserGrp1T, args.UserGrp1V, args.UserGrp2T, args.UserGrp2V, args.UserGrp3T, args.UserGrp3V)

        parseObj.updateCurShippedEntry(args.vTable, values, args.vOscar)



        # update_query = """
        #     WITH sorted_rows AS (
        #         SELECT id
        #         FROM CUR_SHIPPED_TABLE
        #         WHERE Oscar = %s
        #         ORDER BY CreatedAt DESC
        #         LIMIT 1
        #     )
        #     UPDATE CUR_SHIPPED_TABLE
        #     SET 
        #         Oscar = %s,
        #         CodeN = %s,
        #         BuildType = %s,
        #         ProdRelT = %s,
        #         ProdRelV = %s,
        #         ExtFTRelT = %s,
        #         ExtFTRelV = %s,
        #         IntFTRelT = %s,
        #         IntFTRelV = %s,
        #         DayOImgT = %s,
        #         DayOImgV = %s,    
        #         FFUImgT = %s,
        #         FFUImgV = %s,
        #         AutoOTAT = %s,
        #         AutoOTAV = %s,    
        #         FactoryImg = %s,
        #         DiagImg = %s,
        #         UserGrp1T = %s,
        #         UserGrp1V = %s,
        #         UserGrp2T = %s,
        #         UserGrp2V = %s,
        #         UserGrp3T = %s,
        #         UserGrp3V = %s
        #     FROM sorted_rows
        #     WHERE CUR_SHIPPED_TABLE.id = sorted_rows.id;
        # """

        # values = (args.vOscar, args.vOscar, args.vCodeN, args.vBuildType, args.vProdRelT, args.vProdRelV, args.vExtFTRelT, args.vExtFTRelV, 
        #           args.vIntFTRelT, args.vIntFTRelV, args.DayOImgT, args.DayOImgV, args.FFUImgT, args.FFUImgV, args.AutoOTAT, args.AutoOTAV, args.FactoryImg, args.DiagImg,
        #           args.UserGrp1T, args.UserGrp1V, args.UserGrp2T, args.UserGrp2V, args.UserGrp3T, args.UserGrp3V)

        # ret = insertObj.updateRowData2(update_query, values)
        # if ret:
        #     print("update data successful!")
        # else:
        #     print("update data failed!")