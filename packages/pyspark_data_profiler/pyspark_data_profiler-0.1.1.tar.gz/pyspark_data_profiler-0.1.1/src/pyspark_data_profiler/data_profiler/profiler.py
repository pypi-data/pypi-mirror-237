from datetime import datetime
from pyspark.sql import Row
from pyspark.sql.functions import lit, min, max, avg, mean, col, desc, stddev, variance
from pyspark.sql.functions import median, isnull, regexp_replace, length, sum , round

from pyspark_data_profiler.utils.spark_setup_utils import spark


class Profiler:
    '''Class to profile data'''
    def __init__(self, spark_dict):
        # self.df = dictionary['df']
        # self.file_name = dictionary['file_name']
        # self.config_file = dictionary['config_file']
        # self.dictionary = dictionary
        self.spark_dict = spark_dict

    # create stat dictionary
    stat_dict = {
        'max': {
         'enable': 'Y',
         'additionalParameters': []},
        'min': {
         'enable': 'Y',
         'additionalParameters': []},
        'avg': {
         'enable': 'Y',
            'additionalParameters': []},
        'mean': {
            'enable': 'Y',
            'additionalParameters': []},
        'mode': {
            'enable': 'Y',
            'additionalParameters': []},
        'stddev': {
            'enable': 'Y',
            'additionalParameters': []},
        'variance': {
            'enable': 'Y',
            'additionalParameters': []},
        'unique': {
            'enable': 'Y',
            'additionalParameters': []},
        'outlier': {
            'enable': 'Y',
            'additionalParameters': []},
        'median': {
            'enable': 'Y',
            'additionalParameters': []},
        'null_count': {
            'enable': 'Y',
            'additionalParameters': []}
    }


    def config(self, output_format=None):
        spark_dict = self.spark_dict
        # df = self.df
        stat_dict = self.stat_dict
        config_dict = {}
        # get columns name and data type
        for spark_key, spark_val in spark_dict.items():
            df = spark_val['df']
            cols_names = [name for name in df.columns]

            # create output dictionary
            df_config_dict = {}

            for index, name in enumerate(cols_names, start=1):
                column_name = f'column{index}'
                column_dict = {
                    'name': name,
                    'enable': 'Y',
                    'calculations': stat_dict
                }
                df_config_dict[column_name] = column_dict
            config_dict[spark_key] = df_config_dict
        return config_dict

    def global_report(self):
        spark_dict=self.spark_dict
        # df=self.df
        # generate global stats
        global_report = {}

        for spark_key, spark_value in spark_dict.items():
            df = spark_value['df']
            file_name = spark_value['file_name']
            global_stats = {}
            # global stats data
            global_stats['columns_count'] = len(df.columns)
            global_stats['row_count'] = df.count()
            global_stats['unique_row_count'] = df.distinct().count()
            global_stats['duplicate_row_count'] = global_stats['row_count'] - global_stats['unique_row_count']
            global_stats['unique_row_ratio'] = global_stats['unique_row_count'] / global_stats['row_count']
            global_stats['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            global_stats['file_name'] = file_name
            # TODO global_stats['row_has_null_ratio']
            # TODO global_stats['row_is_null_ratio']
            global_report[spark_key] = global_stats
        return global_report

    def column_report(self, config=None):
        # df=self.df
        spark_dict = self.spark_dict
        stat_dict = self.stat_dict

        column_report = {}
        for spark_key, spark_value in spark_dict.items():
            df = spark_value['df']
            file_name = spark_value['file_name']
            config = spark_value['config_file']
            # generate column report
            data_stats = {}
            data_stats['file_name'] = file_name
            data_stats['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            col_stats = []
            data_stats['col_stats'] = col_stats

            if config != None:
                eval_dict = {}

                for key, value in config.items():
                    if value['enable'] == 'Y':
                        column_name = value['name']
                        calculations = {}
                        for calc_key, calc_value in value['calculations'].items():
                            if calc_value['enable'] == 'Y':
                                calculations[calc_key] = calc_value['additionalParameters']
                        if calculations:
                            eval_dict[column_name] = calculations

            else:
                eval_dict = {}
                for df_col in df.columns:
                    eval_dict[df_col] = stat_dict

            # data_stats data
            for df_col, vals in eval_dict.items():
                d = {}
                d['column_name'] = str(df_col)
                d['data_type'] = str(df.schema[df_col].dataType)
                d['categorical'] = 'Yes' if df.select(df_col).distinct().count() < 20 else 'No'
                d['samples'] = df.select(df_col).distinct().rdd.flatMap(lambda x: x).collect()[:10]
                for calc, params in vals.items():
                    if calc == 'min':
                        d['min'] = df.select(df_col).summary('min').collect()[0][1]
                    if calc == 'max':
                        d['max'] = df.select(df_col).summary('max').collect()[0][1]
                    if calc == 'avg':
                        d['avg'] = df.select(avg(df_col)).collect()[0][0]
                    if calc == 'mean':
                        d['mean'] = df.select(df_col).summary('mean').collect()[0][1]
                    if calc == 'mode':
                        d['mode'] = df.groupBy(df_col).count().orderBy(desc("count")).first()[df_col]
                    if calc == 'stddev':
                        d['stddev'] = df.select(df_col).summary('stddev').collect()[0][1]
                    if calc == 'variance':
                        d['variance'] = df.select(variance(df_col)).collect()[0][0]
                    if calc == 'unique':
                        d['unique'] = df.select(df_col).distinct().count()
                    if calc == 'outlier':
                        # test if column is not null
                        test_val = df.withColumn('test', col(df_col) / 1)\
                                     .select('test').distinct().collect()[0][0]
                        if test_val != None:
                            q1 = float(df.select(df_col).summary('25%').collect()[0][1])
                            q3 = float(df.select(df_col).summary('75%').collect()[0][1])
                            iqr = q3 - q1
                            lower_bound = q1 - (1.5 * iqr)
                            upper_bound = q3 + (1.5 * iqr)
                            d['outliers'] = {
                                'count': df.filter((col(df_col) < lower_bound) | (col(df_col) > upper_bound)).count(),
                                'samples': df.filter((col(df_col) < lower_bound) | (col(df_col) > upper_bound))\
                                .select(df_col)\
                                .rdd.flatMap(lambda x: x).collect()[:10]
                            }
                        else:
                            col_count = df.select(df_col).count()
                            # calculate IQR
                            q1 = col_count * 0.25
                            q3 = col_count * 0.75
                            iqr = q3 - q1
                            k = 0.25
                            lower_bound = q1 - (k * iqr)
                            upper_bound = q3 + (k * iqr)
                            # filtered dataframe
                            df_filt = df.select(df_col)\
                                        .groupBy(df_col)\
                                        .count()\
                                        .filter((col('count') < lower_bound) | (col('count') > upper_bound))
                            # calculate outliers and samples
                            out_count = df_filt.groupBy().sum().collect()[0][0]
                            if out_count == col_count:
                                out_count = None
                                out_sample = []
                            else:
                                out_sample = df_filt.select(df_col).rdd.flatMap(lambda x: x).collect()[:10]
                                d['outliers'] = {
                                    'count': out_count,
                                    'samples': out_sample
                                }
                    if calc == 'median':
                        d['median'] = df.select(median(df_col)).collect()[0][0]
                    if calc == 'null_count':
                        d['null_count'] = df.select(df_col).filter(isnull(df_col)).count()
                    if calc == 'covariance':
                        if dict(df.dtypes)[df_col] not in ['int', 'double']:
                            print(f"{df_col} is not a numeric type column. Can't execute a covariance.")
                        else:
                            try:
                                for cov_cols in vals['covariance']:
                                    d['cov_{}_{}'.format(df_col, cov_cols)] = df.cov(df_col, cov_cols)
                            except Exception as e:
                                print(f"Exception on the covariance stat. Error: {e}")
                    col_stats.append(d)
                column_report[spark_key] = col_stats
        return column_report


    def column_pattern(self, config=None):
        # df = self.df
        spark_dict = self.spark_dict
        column_pattern = {}

        for spark_key, spark_value in spark_dict.items():
            df = spark_value['df']
            file_name = spark_value['file_name']
            config = spark_value['config_file']
            # generate column pattern report
            col_pattern = {}
            col_pattern['file_name'] = file_name
            col_pattern['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            col_list_pattern = []
            col_pattern['col_patterns'] = col_list_pattern

            if config != None:
                eval_list = []
                for key, value in config.items():
                    if value['enable'] == 'Y':
                        eval_list.append(value['name'])

            else:
                eval_list = [df_col for df_col in df.columns]

            for df_col in eval_list:
                d = {}
                re_col = df.select(regexp_replace(df_col, r'[A-Z]', 'C').alias('pattern'))\
                           .select(regexp_replace('pattern', r'[a-z]', 'c').alias('pattern'))\
                           .select(regexp_replace('pattern', r'\d', 'N').alias('pattern'))\
                           .select(regexp_replace('pattern', r'\W', 'S').alias('pattern'))
                re_count = re_col.groupBy('pattern').count()
                total_count = re_count.agg(sum("count")).collect()[0][0]
                re_perc = re_count.withColumn('percentage', round(col("count") / total_count * 100, 2))\
                                  .withColumn("length", length(col("pattern")))
                d['patterns'] = [row.asDict () for row in re_perc.collect()]
                d['column_name'] = df_col
                col_list_pattern.append(d)
            column_pattern[spark_key] = col_list_pattern
        return column_pattern
