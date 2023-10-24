# -*- coding:utf-8 -*-

"""
读写数据库clickhouse
"""
from clickhouse_driver import Client
import pandas as pd
from .utils import read_json, clickhouse_create_table_sql, timer,check_schema

class ClickhouseClient:
    """ 读写clickhouse数据库 """
    def __init__(self, host='localhost', port=9000, user='default', password='12345678', database='default'):
        """ 初始化 """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.connection= None

    def connect(self):
        """ 连接到server上的某个数据库 """
        # 使用提供的参数或默认值
        # db_name = db_name
        # 创建 ClickHouse 客户端并建立连接
        self.connection = Client(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if not self.is_connected():
            raise Exception('can not connect to server, please check your login info.')

    @property
    def current_database(self):
        return self.connection.execute("SELECT currentDatabase()")[0][0]

    def is_connected(self):
        """ 是否连接到数据库 """
        if self.connection is None:
            return False
        else:
            return True

    def use_db(self, db_name):
        """ 使用某个数据库 """
        self.connection.execute(f"USE {db_name}")

    def is_db_existed(self, db_name):
        """ 数据库是否存在 """
        databases = self.connection.execute("SHOW DATABASES")
        return db_name in [db[0] for db in databases]

    def is_table_existed(self, table_name):
        """ 表是否存在 """
        tables = self.connection.execute(f"SHOW TABLES FROM {self.current_database}")
        return table_name in [table[0] for table in tables]

    def excu(self, sql_script):
        """ 执行sql语句 """
        return self.connection.execute(sql_script)

    def create_db(self, db_name):
        """ 创建数据库 """
        sql_script = f"CREATE DATABASE IF NOT EXISTS {db_name}"
        self.connection.execute(sql_script)

    def create_table(self, sql_script, db_name = None):
        """ 创建表 """
        # 这里我们假设一个简单的表结构，真实使用中需要具体的字段和数据类型
        if db_name is not None:
            self.use_db(db_name)
        self.connection.execute(sql_script)

    def read_schema(self, table_name):
        """
        读取表的字段类型
        struct as --> name : type 
        """
        data = self.connection.execute(f"DESCRIBE TABLE {table_name}")
        schema = {}
        for record in data:
            schema[record[0]] =record[1]
        return schema

    def mergetree_create(self, table_name, schema, order_by, settings = None):
        """ 生成一个mergetree表 """
        sql_script = clickhouse_create_table_sql(table_name, schema, order_by, settings)
        self.connection.execute(sql_script)

    def async_insert_df(self, df, table_name):
        """ 异步插入 DataFrame 数据 """
        insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) SETTINGS async_insert=1, wait_for_async_insert=1 VALUES"
        self.connection.execute(insert_query, df.to_dict("records"))

    def insert_df(self, df, table_name):
        """ 同步插入 DataFrame 数据"""
        insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES"
        self.connection.execute(insert_query, df.to_dict("records"))

    @timer
    def insert_df1(self, df, table_name):
        """ 普通插入DataFrame """
        if not self.is_connected():
            raise Exception("Please connect to database first.")
        if not self.is_table_existed(table_name):
            raise Exception(f"Table {table_name} does not exist.")

        # 创建标准的插入查询，不包括与异步插入相关的设置
        insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES"

        # 执行标准的插入查询
        self.connection.execute(insert_query, df.to_dict("records"))

    def read_df(self, sql_query):
        """ 读取数据 """
        # query样例：query = "SELECT * FROM your_table WHERE your_condition"
        results = self.connection.execute(sql_query, with_column_types=True)
        data, column_types = results
        columns = [column[0] for column in column_types]
        df = pd.DataFrame(data, columns=columns)
        return df

    def update_data(self, table_name, data, condition):
        """ 更新数据 """
        updates = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
        self.connection.execute(f"ALTER TABLE {table_name} UPDATE {updates} WHERE {condition}")

    def add_column(self, table_name, column_name, column_type):
        """ 添加列 """
        self.connection.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")

    def delete_column(self, table_name, column_name):
        """ 删除列 """
        self.connection.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")

    def exists(self, table_name):
        """ 表是否存在 """
        pass

    def list_dbs(self):
        """ 列出所有数据库 """
        return [db[0] for db in self.connection.execute("SHOW DATABASES")]

    def list_tables(self, db_name = None):
        """ 列出所有表 """
        db_name = db_name or self.current_database
        return [table[0] for table in self.connection.execute(f"SHOW TABLES FROM {db_name}")]

    def table_size(self, db_name, table_name):
        """ 获取表大小 """
        query = f"SELECT COUNT(*) FROM {db_name}.{table_name}"
        return self.connection.execute(query)[0][0]

    def optimize_table(self):
        pass


class ClickhouseClientFriendly(ClickhouseClient):
    """
    用户友好下载数据和上传数据接口
    """
    def __init__(self,
                host='192.168.100.124',
                port=9000,
                user='test',
                password='test',
                db_name = 'test',
                ):
        super(ClickhouseClientFriendly, self).__init__(host= host,port = port,user = user, password=password)
        self.db_name = db_name
        self.login_db()
        self.use_default_db()

    def login_db(self,):
        self.connect()
        self.use_db(self.db_name)

    def use_default_db(self):
        self.excu(f"USE {self.db_name};")

    def create_db(self,):
        """不支持用户自建db"""
        raise Exception("not support user create clickhouse db, ask administrator of clickhouse")
    
    def dump_parquet(self, sql: str, path: str):
        """下载数据输出为parquet"""
        df = self.read_df(sql)
        return df.to_parquet(path)
    
    def dump_parquet(self, sql: str, path: str):
        """下载数据输出为csv"""
        df = self.read_df(sql)
        return df.to_csv(path)
    
    def exists(self, table_name: str):
        table_list = self.list_tables(self.db_name)
        if table_name in table_list:
            return True
        return False

    def create_table(self, table_name:str , schema:dict or str, order_by:list ,settings:list ):
        """
        上传用户特征table
        table_name: str, 指定表单的名字
        schema: dict or path, 通过json文件来传递每一个schema的内容
        order_by: string list
        settings: string list, other setting
        """
        if isinstance(schema,str):
            _schema = read_json(schema)
        else:
            _schema = schema
        
        create_sql = clickhouse_create_table_sql(table_name, _schema, order_by, settings=settings)
        self.excu(create_sql)
    
    def init_table(self, table_name:str, df:pd.DataFrame, _async: bool = False):
        """
        初始导入数据，对于存在数据的table不再导入数据，适合固定的表导入，避免重复导入
        备注：
            1. 导入的数据需要跟创建的table的schema匹配不然报错
            2. 默认同步方式上传数据
        """
        if self.table_size(self.db_name, table_name) != 0:
            raise Exception("function not support, consider using update_table to insert data")
        if self.exists(table_name):
            schema = self.read_schema(table_name)
        else:
            raise Exception("table not exists, please create it with function 'create_table'")
        if check_schema(df, schema):
            if _async:
                self.async_insert_df(df, table_name)
            else:
                self.insert_df(df, table_name)
        else:
            raise Exception("schema not compare, check df schema and clickhouse schema")

    def update_table(self, table_name:str, df:pd.DataFrame, _async: bool = False):
        """更新用户特征的内容"""
        if self.exists(table_name):
            schema = self.read_schema(table_name)
        else:
            raise Exception("table not exists, please create it with function 'create_table'")
        if check_schema(df, schema):
            if _async:
                self.async_insert_df(df, table_name)
            else:
                self.insert_df(df, table_name)
        else:
            raise Exception("schema not compare, check df schema and clickhouse schema")


    def create_materialized_table(self, table_name: str, source_table: str):
        """创建物化视图"""
        pass

    def get_tick(self, ):
        """tick衍生特征io"""
        pass

    def gen_bar(self,):
        """合成bar线"""
        pass

    def get_bar(self,):
        """bar线衍生特征io"""
        pass


def clickhouseclient_demo():
    ck = ClickhouseClient(host='192.168.100.124', port=9000, user='test', password='test')
    ck.connect()
    ck.list_tables()
    # ck.create_db('test')

def clickhouseclientfriendly_demo():
    ck = ClickhouseClientFriendly(host='192.168.100.124', port=9000, user='test', password='test',db_name='test')
    ck.create_table('test',"K:\qtData\cnstk\stk_tick_schema.json",["instrument","date","time"], ["partition by instrument"])
    df = pd.DataFrame()
    ck.init_table("test",df)


if __name__ == '__main__':
    # clickhouseclient_demo()
    clickhouseclientfriendly_demo()