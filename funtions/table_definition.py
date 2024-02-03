import pandas as pd

def products():

    # Define columns
    columns = [
        'id','productcode','productname','energy','consumptiontype',
        'deleted','modificationdate','Releasedversion'
    ]

    # Create an empty DataFrame with defined columns and data types
    product_df = pd.DataFrame(columns=columns).astype(products_datatype())

    return product_df


def contracts():

    # Define columns
    columns = [
        'id','type','energy','usage','usagenet','createdat','startdate','enddate',
        'fillingdatecancellation','cancellationreason','city','status','productid',
        'modificationdate'
    ]

    # Create an empty DataFrame with defined columns and data types
    contracts_df = pd.DataFrame(columns=columns).astype(contracts_datatype())

    return contracts_df


def prices():
    # Define columns
    columns = [
        'id','productid','pricecomponentid','productcomponent','price',
        'unit','valid_from','valid_until','modificationdate'
    ]

    # Create an empty DataFrame with defined columns and data types
    prices_df = pd.DataFrame(columns=columns).astype(prices_datatype())

    return prices_df

def products_datatype():

    # Define data types
    data_types = {
        'id': 'int64',
        'productcode': 'str',
        'productname': 'str',
        'energy': 'str',
        'consumptiontype': 'str',
        'deleted': 'int64',
        'modificationdate': 'datetime64[ns]',
        'Releasedversion': 'int64'
    }

    return data_types


def contracts_datatype():

    # Define data types
    data_types = {
        'id': 'int64',
        'type': 'str',
        'energy': 'str',
        'usage': 'int64',
        'usagenet': 'int64',
        'createdat': 'datetime64[ns]',
        'startdate': 'datetime64[ns]',
        'enddate': 'datetime64[ns]',
        'fillingdatecancellation': 'datetime64[ns]',
        'cancellationreason': 'str',
        'city': 'str',
        'status': 'str',
        'productid': 'int64',
        'modificationdate': 'datetime64[ns]'
    }

    return data_types


def prices_datatype():

    # Define data types
    data_types = {
        'id': 'int64',
        'productid': 'int64',
        'pricecomponentid': 'int64',
        'productcomponent': 'str',
        'price': 'float64',
        'unit': 'str',
        'valid_from': 'datetime64[ns]',
        'valid_until': 'datetime64[ns]',
        'modificationdate': 'datetime64[ns]'
    }

    return data_types