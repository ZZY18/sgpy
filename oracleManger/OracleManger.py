"""
# 在对oracle数据库进行查询
"""
class OpenDB(object):
    
    def __init__(self, connstr):
        import cx_Oracle as oc
        # 初始化
        
        self.conn = oc.connect(connstr)
        self.cs = self.conn.cursor()

    def __enter__(self):
        # 返回游标进行执行操作
        return self.cs

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 结束提交数据并关闭数据库
        self.conn.commit()
        self.cs.close()
        self.conn.close()

class oracleManger():
    import pandas as pd 
    import cx_Oracle as cs 
    import pandas as pd
    """
    对数据库进行查询操作

    初始化：
    要求输入数据库连接信息,eg:connstr='qidao/aA123456@orcl'
    """
    def __init__(self,connstr):
        self.__connstr=connstr
        
    def SelectDataD(self,sql):
        import pandas as pd
        with OpenDB(self.__connstr) as f:
            f.execute(sql)
            data = f.fetchall()#获得所有数据，以list(tuple)
            columnDes = f.description #获取连接对象的描述信息
            columnNames = [columnDes[i][0] for i in range(len(columnDes))]
            dt= pd.DataFrame([list(i) for i in data],columns=columnNames)
        return dt
	
	def InsertData(self,tablename,data_dic):
		insert_sql = "INSERT INTO "+tablename+"("+" VALUES(:1, :2)"
		with OpenDB(self.__connstr) as f:
			f.executemany(insert_sql,)
		

if __name__=="__main__":
    manger=oracleManger('qidao/aA123456@orcl')
    dt=manger.SelectDataD("""select * from basisdata""")
	args_data={1:'hello', 2:'Python'}
    print(dt[0,0])
    a=",".join(["123","234"])