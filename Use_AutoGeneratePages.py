
from AutoGeneratePages import AutoGeneratePages
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')
    parser.add_argument('vHtml', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildO1', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildO1B', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildO2', type=str, nargs='?', help='', default=None)
    parser.add_argument('vBuildO2B', type=str, nargs='?', help='', default=None)
    args = parser.parse_args()


    # print("args.vBuildO1= ", args.vBuildO1)
    # print("args.vBuildO1B= ", args.vBuildO1B)

    # print("args.vBuildO2= ", args.vBuildO2)

    # print("args.vBuildO2B= ", args.vBuildO2B)
    # print("args.vHtml= ", args.vHtml)

    # curBuild_O1_B = ""
    # curBuild_O1 = ""
    # curBuild_O2 = "rls-v01_07_04-f463d98"
    # curBuild_O2_B = "dbg-v01_07_04-f463d98"
    # curBuildHtml = "dashboard_v01_07_04.html"

    #local obj = AutoGeneratePages("pi", "guo95132", "Welc0me123", "127.0.0.1")
    obj = AutoGeneratePages("pi", "pi", "Welc0me123", "100.117.244.108")

    obj.connectToPostDB()
    obj.getCursor()

    obj.queryMainReportTable()

    obj.generateHTMLPages('main', args.vBuildO1, args.vBuildO2)

    # local obj = AutoGeneratePages("pi", "guo95132", "Welc0me123", "127.0.0.1")
    obj = AutoGeneratePages("pi", "pi", "Welc0me123", "100.117.244.108")

    obj.connectToPostDB()
    obj.getCursor()

    if args.vBuildO1:
        obj.queryTables_O1(args.vBuildO1, args.vBuildO1B)

    if args.vBuildO2:
        obj.queryTables_O2(args.vBuildO2, args.vBuildO2B)

    obj.generateHTMLPages('detal', args.vBuildO1, args.vBuildO2, args.vHtml)












