import pandas as pd
from sqlalchemy import create_engine
import requests
import json

# Establish a connection to the MySQL database
engine = create_engine('mysql+mysqldb://root:db_root@localhost/northstar2')
connection = engine.connect()

# Define chunk size
chunk_size = 50 # Adjust based on your memory capacity

# Query templates
property_query = "SELECT * FROM property"
media_query = "SELECT * FROM media WHERE ListingId IN ({})"
rooms_query = "SELECT * FROM propertyrooms WHERE ListingId IN ({})"

# Function to forward data to another API
def forward_to_api(data):
    print(data)
    print("API")

# Function to process data in chunks
def process_data_in_chunks():
    property_chunks = pd.read_sql(property_query, connection, chunksize=chunk_size)
    
    for property_chunk in property_chunks:
        property_ids = property_chunk['ListingId'].tolist()

        # Create a placeholder string for property IDs
        placeholders = ','.join(['%s'] * len(property_ids))

        # Fetch corresponding media and rooms records
        media_data = pd.read_sql(media_query.format(placeholders), connection, params=[tuple(property_ids)])
        rooms_data = pd.read_sql(rooms_query.format(placeholders), connection, params=[tuple(property_ids)])

        # Combine data as needed (e.g., merge or join)
        combined_data = property_chunk.merge(media_data, left_on='ListingId', right_on='ListingId', how='left')\
                                      .merge(rooms_data, left_on='ListingId', right_on='ListingId', how='left')
        
        # Forward combined data to another API
        forward_to_api(combined_data)

# Execute the data processing
process_data_in_chunks()
