
from ParsingResults import ParseData
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Table paraters...')

    parser.add_argument('vPath', type=str, nargs='?', help='', default=None)
    parser.add_argument('vVer', type=str, nargs='?', help='', default=None)
    args = parser.parse_args()


    db = "pi"
    host = "127.0.0.1" 
    user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"
    parseObj = ParseData(db, host, user, passwd, port, False)
    parseObj.connectToPostDB()
    parseObj.getCursor()   

    print("vFile", args.vPath)
    print("vSN", args.vVer)


    print("===for O1====")
    parseObj.verify_specific_version_exists(args.vPath, args.vVer, 'O1')
    print("===for O2====")
    parseObj.verify_specific_version_exists(args.vPath, args.vVer, 'O2')



    
