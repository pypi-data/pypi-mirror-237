import pymysql 
from sqlalchemy import create_engine,text
import pandas as pd
import sys
lastid = 0



def df插入入mysql():
    table_name = 'stock_all_codes'
    # define the columns to be inserted
    columns = ['code', 'name', 'tradeStatus', 'ipoDate']

    # loop through each row in the dataframe
    for index, row in df.iterrows():
        # check if the code already exists in the table
        query = f"SELECT * FROM {table_name} WHERE code = {row['code']}"
        result = engine.execute(query).fetchall()
        
        # if the code exists, update the tradeStatus column
        if len(result) > 0:
            update_query = f"UPDATE {table_name} SET tradeStatus = {row['tradeStatus']} WHERE code = {row['code']}"
            engine.execute(update_query)
        # if the code does not exist, insert a new row
        else:
            insert_query = f"INSERT INTO {table_name} (code, name, tradeStatus, ipoDate) VALUES ({row['code']}, '{row['code_name']}', {row['tradeStatus']}, '{row['ipodate']}')"
            engine.execute(insert_query)

def get_tdx_server_list():
    df = pd.read_sql_table('stock_tdx_server', conn)
    #print(df)
    return df.ip.to_list()

def 获取股票代码表(debug=False):
    if debug: print(sys._getframe().f_code.co_name)
    df = pd.read_sql_table('stock_all_codes', conn)
    code_list = df['code'].tolist()
    if debug: print("code_list:",len(code_list))
    return code_list,df

def get_date_list_mysql():
    df = pd.read_sql_query('SELECT day FROM stock_trade_calendars', conn)
    date_list = df['day'].tolist()
    return date_list

def get_list_from_sql(table_name,column_name,codition=None):
    """
    直接读取数据库中的table_name表中的column_name列，返回list
    """

    if not codition:
        df = pd.read_sql_table(table_name, conn)
    else:
        query = "SELECT * FROM "+table_name+" WHERE "+codition
        df = pd.read_sql_query(text(query),conn)
    return_list = df[column_name].tolist()
    return return_list,df



def search_keyword(stk_code, company):
    conn = con_aliyun()
    cursor = conn.cursor()
    company=company.replace("股份","").replace("科技","").replace("控股","").replace("集团","").replace("信息","").replace("电子","").replace("环保","")
    sql = "SELECT * FROM message WHERE (message LIKE '%"+ stk_code+"%'"+ " OR message LIKE '%"+company+"%') AND time >= DATE_SUB(NOW(), INTERVAL 3 DAY) order by time desc limit 40"
    print("sql:",sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    return_data = ""
    for row in results:
        print(row)
        msg =row[5].replace("\n\n","\n").replace("\n\n\n","\n")
        return_data+=str(row[1])+" "+row[3]+"："+msg+"\n"
    conn.close()

    return return_data

def insert_mysql_multi(fulldf,conn, db_last_date_int,code_str6):
    pass



def insert_mysql(wmdf,engine,start_date,stk_code_num):
    print("endter insert_mysql")
    #print(wmdf)
    sqlquery2 = "day>" + str(start_date)
    newdf = wmdf.query(sqlquery2)
    结果长度 = len(newdf)
    if 结果长度> 0:
        print(结果长度)
        inserted_rows=mysql_insert(newdf, engine,stk_code_num, output=True)           
        return(inserted_rows)
    else:
        print("需要插入的数据条数为"+str(结果长度))
    return 0

def mysql_insert(df, engine, table_name, output=True):
    inserted_rows = 0
    # 检查表是否存在,如果不存在则创建 
    if not engine.dialect.has_table(engine, table_name):        
        df.to_sql(table_name, engine, index=False)
        inserted_rows = df.shape[0]  

    else:      
        # 逐行比较DataFrame和表
        for row in df.iterrows():       
            index = row[0]
            value = row[1]
            # 通过SQL查询获取表对应行
            query = f"SELECT * FROM `{table_name}` WHERE {df.columns[0]}={int(value[0])}"
            try: 
                current_row = pd.read_sql(query, engine)    
            except:
                dtypes = {0:'int', 1:'int', 2:'int', 3:'int', 4:'int', 5:'int', 6:'float',  
       7:'float', 8:'float', 9:'float', 10:'int'}
                current_row = pd.DataFrame(columns= ['day', 'open', 'high', 'low', 'close', 'volume', 'tenhigh',  
       'up', 'chonggao', 'huitoubo', 'notfull'])   # 空DataFrame代替空表
            # 比较DataFrame行和表对应行
            print("table_name:",table_name) 
            print("-----------------------")
            print(df.loc[index],type(df.loc[index]))
           # df.reset_index(drop=True, inplace=True)
            if current_row.empty:                
                # 表无对应行,插入新行
                print(df.iloc[index])
                df.iloc[index].to_sql(table_name, engine, index=False, if_exists='replace')
                inserted_rows += 1  # 计算插入行数
            elif not value.eq(current_row.loc[0]).all():               
                # DataFrame和表对应行不同,更新表行
                df.iloc[index].to_sql(table_name, engine, index=False, if_exists='replace')
                inserted_rows += 1  # 计算插入行数
        
    if output:
        print(f'Finished loading {table_name}! Inserted {inserted_rows} rows.')
    return inserted_rows



if __name__ == '__main__':
    #df插入入mysql()
    #print(df)
    df = get_tdx_server_list()
    print(df)

