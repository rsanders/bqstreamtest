from google.cloud import bigquery

import common

# Construct a BigQuery client object.
client = bigquery.Client()

## 
## Demonstration of the use of the BQ API with a Dry Run query to extract a list
## of referenced tables. This can be used to simulate access control. Note that it
## fully resolves all referenced tables -- views are "invisible" and manifest
## as the underlying tables.
##

"""
CREATE TABLE sky-did-129154.testdataset.strstr
 (timestamp timestamp, scol string, strct STRUCT<a int64, b string, trailer string>);

 select *
    from sky-did-129154.testdataset.strstr
    where timestamp > '2021-07-01'
    order by timestamp desc;

CREATE VIEW strstriew AS
  select * from sky-did-129154.testdataset.strstr;
"""

# TODO(developer): Set table_id to the ID of table to append to.
table_id = "sky-did-129154.testdataset.strstr"


job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)

# Start the query, passing in the extra configuration.
query_job = client.query(
    (
        "SELECT * from  sky-did-129154.testdataset.strstrview limit 100;"
    ),
    job_config=job_config,
)  # Make an API request.

# A dry run query completes immediately.
print("Query: {}".format(query_job.query))
print("This query will process {} bytes.".format(query_job.total_bytes_processed))
print("Tables referenced: {}".format(query_job.referenced_tables))

# import pdb; pdb.set_trace()

