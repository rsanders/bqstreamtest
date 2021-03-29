from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

"""
CREATE TABLE sky-did-129154.testdataset.strstr
 (timestamp timestamp, scol string, strct STRUCT<a int64, b string, trailer string>);
"""

# TODO(developer): Set table_id to the ID of table to append to.
table_id = "sky-did-129154.testdataset.strstr"

rows_to_insert = [
    {u"timestamp": u"Phred Phlyntstone", "scol": "hello", "strct": {"a": 100}},
    {u"timestamp": u"Wylma Phlyntstone", "scol": "hello", "strct": {"b": "hello"}},
]

errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))