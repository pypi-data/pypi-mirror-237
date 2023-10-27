import json
import os

from pyspark_data_profiler.utils.spark_setup_utils import spark


def read_spark(path, file_extension, config_file):
    # read data on spark
    try:
        if file_extension == '.csv':
            df = spark.read.format('csv')\
                           .option('header', 'true')\
                           .option('inferSchema', 'true')\
                           .load(path)
            return {'df': df, 'file_name': path, 'config_file': config_file}
        elif file_extension == '.parquet':
            df = spark.read.format('parquet').load(path)
            return {'df': df, 'file_name': path, 'config_file': config_file}
        else:
            # raise NotImplementedError("The file extension you're trying to read has not been implement")
            print(f"WARNING: The file format for {path} has not been implemented.")
    except Exception as e:
        raise e


class Reader:
    '''Class to read the data'''
    def __init__(self, path, configuration_file=None):
        self.path = path
        self._data = None
        self.configuration_file = configuration_file

    @property
    def data(self):
        if self._data is None:
            self._data = self.read_data()
        return self._data

    def read_data(self):
        path = self.path
        configuration_file = self.configuration_file
        # spark_list = []
        spark_dict = {}
        # check if path is a folder or a file
        if os.path.isdir(path):
            file_dict = {}
            print(f'{path} is a directory.')
            print('Analyzing all the files in the directory.')
            # list all the files in the directory
            all_files = os.listdir(path)

            for file_path in all_files:
                file_name, file_extension = os.path.splitext(file_path)

                if file_name in file_dict:
                    if file_extension == '.json':
                        file_dict[file_name]['json'] = file_path
                        file_dict[file_name]['extension'] = file_extension
                    else:
                        file_dict[file_name]['data'] = file_path
                        file_dict[file_name]['extension'] = file_extension
                else:
                    file_dict[file_name] = {'json': None, 'data': None}
                    if file_extension == '.json':
                        file_dict[file_name]['json'] = file_path
                        file_dict[file_name]['extension'] = file_extension
                    else:
                        file_dict[file_name]['data'] = file_path
                        file_dict[file_name]['extension'] = file_extension

            for file_key, file_vals in file_dict.items():
                # spark_list.append(read_spark(file_vals['data'], file_vals['extension'], file_vals['json']))
                # read json config file
                if file_vals['json'] != None:
                    with open(file_vals['json'], 'r') as f:
                        json_data = json.load(f)
                else:
                    json_data = None
                spark_dict[file_key] = read_spark(file_vals['data'], file_vals['extension'], json_data)

            # filter the spark dictionary to only have usable data
            # filtered_spark_list = [x for x in spark_list if x is not None]
            # return filtered_spark_list
            filtered_spark_dict = {key: val for key, val in spark_dict.items() if val is not None}
            return filtered_spark_dict

        elif os.path.isfile(path):
            file_name, file_extension = os.path.splitext(path)
            # spark_list.append(read_spark(path, file_extension, None))
            # return spark_list
            if configuration_file != None:
                with open(configuration_file, 'r') as f:
                    json_data = json.load(f)
            else:
                json_data = None
            spark_dict[file_name] = read_spark(path, file_extension, json_data)
            return spark_dict
