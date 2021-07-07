from google.cloud import bigquery
import time

def get_client():
    # Construct a BigQuery client object.
    client = bigquery.Client()
    return client

def get_dataset():
    return "sky-did-129154.testdataset"
