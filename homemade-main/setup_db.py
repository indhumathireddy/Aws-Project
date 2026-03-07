import boto3
import time

def create_tables():
    dynamodb = boto3.client('dynamodb', region_name='ap-south-1')
    
    existing_tables = dynamodb.list_tables()['TableNames']
    
    # Create Users table
    if 'Users' not in existing_tables:
        print("Creating 'Users' table...")
        dynamodb.create_table(
            TableName='Users',
            KeySchema=[{'AttributeName': 'username', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'username', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
    
    # Create Orders table
    if 'Orders' not in existing_tables:
        print("Creating 'Orders' table...")
        dynamodb.create_table(
            TableName='Orders',
            KeySchema=[{'AttributeName': 'order_id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'order_id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
    
    print("Waiting for tables to become active...")
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName='Users')
    waiter.wait(TableName='Orders')
    print("Tables are active.")

if __name__ == "__main__":
    create_tables()
