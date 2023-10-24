# -*- coding:utf-8 -*-

import json
import time
import h5py
from functools import wraps

def read_json(json_file):
    """Read a JSON file and return its content as a Python object."""
    with open(json_file, 'r') as file:
        return json.load(file)


def clickhouse_create_table_sql(table_name, schema, order_by, engine='MergeTree', settings = None):
    """ 生成clickhouse创建表的sql语句
    schema: dict
    order_by: list
    settings: list 例如：
        ['PARTITION BY toYYYYMMDD(toDate(date))', 'ORDER BY (date, symbol, time)';
    """
    columns = ',\n '.join([f"{column_name} {data_type}" for column_name, data_type in schema.items()])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name}\n(\n {columns}\n) ENGINE = {engine}()"
    order_by = "(" + ", ".join(order_by) + ")"
    create_table_sql += f"\nORDER BY {order_by}"
    if settings:
        for setting in settings:
            create_table_sql += f"\n{setting}"
    return create_table_sql

def check_schema(df, schema):
    """检查df的schema是否和schema一致"""
    clickhouseFormat2dfFormat = {
        "UInt32":"uint32",
        "UInt64":"uint64",
        "Float32":"float32",
        "Float64":"Float64",
        "String" :"string"
    }
    columns_name =df.columns.tolist()
    df_dtypes = [str(i) for i in list(df.dtypes)]

    df_schema = dict(zip(columns_name, df_dtypes))

    for key in schema.keys():
        if key not in df_schema:
            return False
        if key in df_schema and clickhouseFormat2dfFormat[schema[key]] != df_schema[key]:
            return False
    return True

def read_h5(pth, key):
    with h5py.File(pth, 'r') as h5r:
        data = h5r[key][()]
    return data

def list_keys(pth):
    with h5py.File(pth, 'r') as h5r:
        return list(h5r.keys())

def timer(func):
    """一个用于计时的装饰器"""
    @wraps(func)  # 用于保持原始函数的名称和文档字符串
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 开始时间
        result = func(*args, **kwargs)  # 函数执行
        end_time = time.time()  # 结束时间
        run_time = end_time - start_time  # 运行时间
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return result
    return wrapper

if __name__ == '__main__':
    clickhouse_create_table_sql('test', read_json(r"K:\qtData\futdata\fut_lev1_schma.json"), order_by = ['symbol','date','time'],settings =['PARTITION BY toYYYYMMDD(toDate(date))'])