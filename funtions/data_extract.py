from funtions import db_connections
import pandas as pd
import logging

#How did the average revenue per contract develop between 01.10.2020 and 01.01.2021
def data_extract_usecase_1():
    usecase_1 = """SELECT
    c.id AS contract_id,
    c.startdate,
    c.enddate,
    c. energy,
    p.productcode,
    p.productname,
    (bp.price + c.usage * wp.price) AS revenue
    FROM contracts c
    JOIN products p ON c.productid = p.id
    JOIN (SELECT productid, price FROM lb.prices WHERE productcomponent = 'workingprice') AS wp 
    ON p.id = wp.productid 
    JOIN (SELECT productid, price FROM lb.prices WHERE productcomponent = 'baseprice') AS bp 
    ON p.id = bp.productid
    WHERE c.startdate BETWEEN '2020-10-01' AND '2021-01-01';"""
    result_df = pd.read_sql_query(usecase_1, con=db_connections.database_connection())
    logging.info(result_df.count())
    return result_df


# How many contracts were on delivery on 01.01.2021?
def data_extract_usecase_2():
    usecase_2 = """select * from contracts where startdate = '2021-01-01' and status='active';"""
    result_df = pd.read_sql_query(usecase_2, con=db_connections.database_connection())
    logging.info(result_df.count())
    return result_df

#How many new contract were loaded into the DWH on 01.12.2020?
def data_extract_usecase_3():
    usecase_3 = """select * from contracts where createdat = '2020-12-01';"""
    result_df = pd.read_sql_query(usecase_3, con=db_connections.database_connection())
    logging.info(result_df.count())
    return result_df
