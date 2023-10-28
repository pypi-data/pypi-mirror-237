import polars as pl
from compare import compare
#import logging
#
#import time
#
#start = time.time()
#logging.basicConfig(level=logging.DEBUG)
#logging.info("hello")
#
#pl.Config.set_tbl_rows(100)
#chicago1 = pl.scan_parquet("pl_compare/output_data/chicago1.parquet").head(1000000)
#chicago2 = pl.scan_parquet("pl_compare/output_data/chicago2.parquet").head(1000000)
#compare(["ID", "Case Number"], chicago1, chicago2).report(print=logging.info)
#
#end = time.time()



base_df = pl.DataFrame(
    {
        "ID": ["123456", "123456", "1234567", "12345678"],
        "ID2": ["123456", "123457", "1234567", "12345678"],
        "Example1": [1,1, 6, 3],
        "Example2": [1,1, 2, 3],
    }
)
compare_df = pl.DataFrame(
    {
        "ID": ["123456", "1234567", "1234567810"],
        "ID2": ["123456", "1234567", "1234567810"],
        "Example1": [1, 2, 3],
        "Example2": [1, 2, 3],
    },
)
#try:
#    base_df.join(compare_df, how='left', on='ID', validate='1:1')
#except pl.exceptions.ComputeError as e:
#    print('b;ah')
compare(["ID"], base_df, compare_df).value_differences_summary()
