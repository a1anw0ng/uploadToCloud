
import psycopg2
import argparse
from millPostDB import millPostDB

class ExecSetCases(millPostDB):
    def __init__(self, database, host, user, password, port, sysLogF):
        super().__init__(database, host, user, password, port, sysLogF)
        # Dictionary mapping keys to functions
        self.switch_case_dict = {
            'cur_g_o1': self.set_cur_g_o1,
            'b_type_o1': self.set_b_type_o1,
            'prod_o1': self.set_prod_o1,
            'ext_ft_o1': self.set_ext_ft_o1,
            'int_ft_o1': self.set_int_ft_o1
        }
        self.v1 = None
        self.v2 = None
        self.v3 = None
        self.v4 = None

    def run_case(self, key, v1=None, v2=None, v3=None, v4=None):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4        
        return self.switch_case_dict.get(key, self.default_case)()

    def default_case(self):
        return "error: invalid input"
    
    def set_cur_g_o1(self):
        vSql = f"update REPORT_TABLE set BuildDate = '{self.v1}',  TemplateN = '{self.v2}', BuildN = '{self.v3}', CodeN = '{self.v4}' where Oscar = 'O1'"
        self.updateRowData(vSql)
        return True

    def set_b_type_o1(self):
        vSql = f"update REPORT_TABLE set BuildType = '{self.v1}' where Oscar = 'O1'"
        self.updateRowData(vSql)
        return True

    def set_prod_o1(self):
        vSql = f"update REPORT_TABLE set ProdRelTemplate = '{self.v1}', ProdRelversion = '{self.v2}' where Oscar = 'O1'"
        self.updateRowData(vSql)
        return True

    def set_ext_ft_o1(self):
        vSql = "update REPORT_TABLE set ExtFTRelTemplate = '{}', ExtFTRelVersion = '{}' where Oscar = 'O1'".format(self.v1, self.v2)
        self.updateRowData(vSql)
        return True

    def set_int_ft_o1(self):
        vSql = f"update REPORT_TABLE set IntFTRelTemplate = '{self.v1}', IntFTRelVersion = '{self.v2}' where Oscar = 'O1'"
        self.updateRowData(vSql)
        return True

class ExecGetCases(millPostDB):
    def __init__(self, database, host, user, password, port, sysLogF):
        super().__init__(database, host, user, password, port, sysLogF)
        # Dictionary mapping keys to functions
        self.switch_case_dict = {
            'cur_t_o1': self.get_cur_t_o1,
            'cur_v_o1': self.get_cur_v_o1,
            'cur_b_date_o1': self.get_cur_b_date_o1,
            'cur_code_n_o1': self.get_cur_code_n_o1,
            'cur_b_type_o1': self.get_cur_b_type_o1,
            'prod_t_o1': self.get_prod_t_o1,
            'prod_v_o1': self.get_prod_v_o1,
            'ext_ft_t_o1': self.get_ext_ft_t_o1,
            'ext_ft_v_o1': self.get_ext_ft_v_o1,
            'int_ft_t_o1': self.get_int_ft_t_o1,
            'int_ft_v_o1': self.get_int_ft_v_o1,

            'int_ft_v_o1': self.get_int_ft_v_o1,

        }

    def get_cur_t_o1(self):
        vSql = "select TemplateN from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_cur_v_o1(self):
        vSql = "select BuildN from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_cur_b_type_o1(self):
        vSql = "select BuildType from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_cur_b_date_o1(self):
        vSql = "select BuildDate from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_cur_code_n_o1(self):
        vSql = "select CodeN from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_prod_t_o1(self):
        vSql = "select ProdRelTemplate from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_prod_v_o1(self):
        vSql = "select ProdRelversion from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_ext_ft_t_o1(self):
        vSql = "select ExtFTRelTemplate from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_ext_ft_v_o1(self):
        vSql = "select ExtFTRelVersion from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_int_ft_t_o1(self):
        vSql = "select IntFTRelTemplate from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def get_int_ft_v_o1(self):
        vSql = "select IntFTRelVersion from REPORT_TABLE where Oscar = 'O1'"
        return self.queryData(vSql)[0][0]

    def default_case(self):
        return "error: invalid input"


    def run_case(self, key):
        # Get the function from the dictionary based on the key and call it
        # Use default_case if key not found
        return self.switch_case_dict.get(key, self.default_case)()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Table paraters...')
    parser.add_argument('vAction', type=str, help='')
    parser.add_argument('vField', type=str, help='')
    parser.add_argument('--v1', type=str, help='')
    parser.add_argument('--v2', type=str, help='')
    parser.add_argument('--v3', type=str, help='')
    parser.add_argument('--v4', type=str, help='')
    args = parser.parse_args()

    db = "pi"
    host = "127.0.0.1" 
    user = "guo95132" 
    passwd = "Welc0me123"
    port = "5432"

    print("BBBBB")
    print("vAction= ", args.vAction)
    print("vField= ", args.vField)

    if args.vAction == 'get':
        getObj = ExecGetCases(db, host, user, passwd, port, False)
        getObj.connectToPostDB()
        getObj.getCursor()
        result = getObj.run_case(args.vField)
        print(result)
    elif args.vAction == 'set':
        setObj = ExecSetCases(db, host, user, passwd, port, False)
        setObj.connectToPostDB()
        setObj.getCursor()

        result = setObj.run_case(args.vField, args.v1, args.v2, args.v3, args.v4)
        print(result)

    # # Example usage
    # example = ExecuteCases()
    # result = example.run_case(args.vSql)
    # print(result)  # Output: This is case 1

    # # # Example with a key that doesn't exist
    # # result = example.run_case(99)
    # # print(result)  # Output: This is the default case
