
from ParsingResults import ParseData
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')
    parser.add_argument('vFile', type=str, nargs='?', help='', default=None)
    parser.add_argument('vSN', type=str, nargs='?', help='', default=None)
    parser.add_argument('vSVR', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuild', type=str, nargs='?', help='', default=None)
    parser.add_argument('vRunr', type=str, nargs='?', help='', default=None)
    args = parser.parse_args()

    db = "pi"
    host = "100.117.244.108"      # host = "127.0.0.1"
    user = "pi"       # user = "guo95132"
    passwd = "Welc0me123"
    port = "5432"
    parseObj = ParseData(db, host, user, passwd, port, False)
    parseObj.connectToPostDB()
    parseObj.getCursor()   
    #print("A1")
    results, vFile = parseObj.ProcessOTA(args.vFile, args.vBuild, args.vSVR, args.vSN, args.vRunr)
    #print("A2")
    parseObj.generate_insert_query(results, vFile, args.vBuild)
    #print("A3")
    results2, vFile2 = parseObj.ProcessDGO(args.vFile, args.vBuild, args.vSVR, args.vSN, args.vRunr)
    # print("A4")
    # print("results2= ", results2)
    # print("vFile2= ", vFile2)
    # print("args.vBuild= ", args.vBuild)
    parseObj.generate_insert_query(results2, vFile2, args.vBuild)
    # print("A5")