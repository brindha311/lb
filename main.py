import pandas as pd
import os
import logging
from sqlalchemy import create_engine
import pymysql
import shutil
from funtions import file_processing, table_definition, db_connections, data_validation, data_extract ,trigger

# Configure the logging settings
logging.basicConfig(filename='logfile.log', level=logging.DEBUG)


def handler():
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create the path to the file in the 'src_data' folder
    src_path = os.path.join(script_dir, 'src_data')
    # path for the files after processed
    processed_path = os.path.join(script_dir, 'processed_data')


    try:

        # Start watching the directory for changes
        #trigger.watch_directory(src_path)
        # Create an empty DataFrame to store the data of 3 tables
        logging.info("create empty dataframe")
        products_df = table_definition.products()
        contracts_df = table_definition.contracts()
        prices_df = table_definition.prices()
        # List all files in the directory
        files = [f for f in os.listdir(src_path) if f.lower().endswith('.csv')]

        # Iterate over each CSV file and read into the DataFrame
        for file_name in files:
            src_file_path = os.path.join(src_path, file_name)

            # Read CSV file into corresponding DataFrame
            df = file_processing.read_csv_file_to_dataframe(src_file_path)
            if "product" in file_name:
                products_df = pd.concat([products_df, df], ignore_index=True)
            elif "contracts" in file_name:
                contracts_df = pd.concat([contracts_df, df], ignore_index=True)
            elif "price" in file_name:
                prices_df = pd.concat([prices_df, df], ignore_index=True)

        # Do the duplicate validation
        products_df = data_validation.duplicate_detection(products_df,"products")
        contracts_df = data_validation.duplicate_detection(contracts_df,"contracts")
        prices_df = data_validation.duplicate_detection(prices_df,"prices")

        # Validate data types and fix if needed
        products_df = data_validation.schema_validation(products_df,table_definition.products_datatype())
        contracts_df = data_validation.schema_validation(contracts_df,table_definition.contracts_datatype())
        prices_df = data_validation.schema_validation(prices_df,table_definition.prices_datatype())

        # load to corresponding tables
        products_df.to_sql(name="products", con=db_connections.database_connection(), index=False, if_exists='append')
        contracts_df.to_sql(name="contracts", con=db_connections.database_connection(), index=False, if_exists='append')
        prices_df.to_sql(name="prices", con=db_connections.database_connection(), index=False, if_exists='append')
        logging.info("load dataframe sucessfully to the database")

        # move the processed file to the destination folder
        for file_name in files:
            src_file_path = os.path.join(src_path, file_name)
            destination_file_path = os.path.join(processed_path, file_name)
            shutil.move(src_file_path, destination_file_path)

        # Run SQL query to get result for coresponding usecases
        usecase_path = os.path.join(script_dir, 'load_usecase')
        usecase1_path = os.path.join(usecase_path, "usecase1.csv")
        file_processing.load_dataframe_to_csv(data_extract.data_extract_usecase_1(),usecase1_path)
        usecase2_path = os.path.join(usecase_path, "usecase2.csv")
        file_processing.load_dataframe_to_csv(data_extract.data_extract_usecase_2(), usecase2_path)
        usecase3_path = os.path.join(usecase_path, "usecase3.csv")
        file_processing.load_dataframe_to_csv(data_extract.data_extract_usecase_3(), usecase3_path)

    except Exception as e:
        logging.error(f"An unexpected error occurred in the main block: {e}")
        raise

if __name__ == "__main__":

    handler()