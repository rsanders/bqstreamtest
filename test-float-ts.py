from google.cloud import bigquery
import time
import datetime

import common

# Construct a BigQuery client object.
client = bigquery.Client()

"""
CREATE TABLE sky-did-129154.testdataset.strstr
 (timestamp timestamp, scol string, strct STRUCT<a int64, b string, trailer string>);
"""

# TODO(developer): Set table_id to the ID of table to append to.
table_id = "sky-did-129154.testdataset.strstr"

rows_to_insert = [
    {u"timestamp": float(time.time()), "scol": "TS as float", "strct": {"a": 100}},
    {u"timestamp": int(time.time()), "scol": "TS as int"},
    {u"timestamp": datetime.datetime.utcnow().isoformat(), "scol": "TS as ISO string", "strct": {"b": "hello"}},
]

errors = client.insert_rows_json(table_id, rows_to_insert, ignore_unknown_values=False, skip_invalid_rows=False)  # Make an API request.
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))