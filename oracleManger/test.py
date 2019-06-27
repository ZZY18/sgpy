# -*- coding: utf-8 -*-
from OracleManger import oracleManger 
import cx_Oracle
age_dic={'ID':2,'NAME':'niming','COUNTRY':'CN'}
age_dic1={'NAME':'niming','COUNTRY':'CN'}
tablename='TEST1'
insert_sql = "INSERT INTO "+tablename+" ("
insert_sql=insert_sql+",".join(age_dic.keys())+") VALUES("
insert_sql=insert_sql+",".join([":"+i for i in age_dic.keys()])+")"

update_sql="UPDATE "+tablename+" SET "
update_sql=update_sql+",".join([i+"=:"+i for i in age_dic1.keys()])
update_sql=update_sql+" where ID=10"

db = cx_Oracle.connect('scott', 'aA123456', '127.0.0.1:1521/orcl')
cursor = db.cursor()
cursor.prepare(update_sql)
rown = cursor.execute(None, age_dic1)
db.commit()
