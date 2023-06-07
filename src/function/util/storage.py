"""
Base Storage Module for DynamoDB
"""
import boto3
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer


class Storage:
    """
    Base Storage class to connect and execute commands on DynamoDB
    """

    def __init__(self, endpoint=None, access_key=None, secret_key=None):
        """

        :param endpoint: The endpoint to use as DynamoDB Connection
        :param access_key: The Access Key to use to authenticate with DynamoDB
        :param secret_key:The Secret Key to use to authenticate with DynamoDB
        """
        self.serializer = TypeSerializer()
        self.deserializer = TypeDeserializer()
        if access_key and secret_key:
            self.db = boto3.client('dynamodb',
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key)
        if access_key and secret_key and endpoint:
            self.db = boto3.client('dynamodb',
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key,
                                   endpoint_url=endpoint)
        else:
            self.db = boto3.client('dynamodb')

    def create_table(self, table_name: str, attribute_definitions: list, key_schema: list,
                     local_secondary_indexes: list = None,
                     global_secondary_indexes: list = None,
                     billing_mode: str = None,
                     provisioned_throughput: dict = None,
                     stream_specification: dict = None,
                     sse_specification: dict = None,
                     tags: list = None,
                     table_class: str = None,
                     deletion_protection_enabled: bool = None):
        """
        Create a Table in the connected DynamoDB

        :param table_name: str, Name of the Table
        :param attribute_definitions: list, An array of attributes that describe the key schema for the table and indexes.
        :param key_schema: list, Specifies the attributes that make up the primary key for a table or an index. The attributes in KeySchema must also be defined in the AttributeDefinitions array. For more information, see Data Model in the Amazon DynamoDB Developer Guide.
        :param local_secondary_indexes: list, One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained.
        :param global_secondary_indexes: list, One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following:
        :param billing_mode: str, Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.
        :param provisioned_throughput: dict, Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the UpdateTable operation.
        :param stream_specification: dict, The settings for DynamoDB Streams on the table.
        :param sse_specification: dict, Represents the settings used to enable server-side encryption.
        :param tags: list, A list of key-value pairs to label the table. For more information, see Tagging for DynamoDB.
        :param table_class: str, The table class of the new table. Valid values are STANDARD and STANDARD_INFREQUENT_ACCESS.
        :param deletion_protection_enabled: bool, Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.
        :return: None
        """
        self.db.create_table(
            AttributeDefinitions=attribute_definitions,
            TableName=table_name,
            KeySchema=key_schema,
            LocalSecondaryIndexes=local_secondary_indexes,
            GlobalSecondaryIndexes=global_secondary_indexes,
            BillingMode=billing_mode,
            ProvisionedThroughput=provisioned_throughput,
            StreamSpecification=stream_specification,
            SSESpecification=sse_specification,
            Tags=tags,
            TableClass=table_class,
            DeletionProtectionEnabled=deletion_protection_enabled
        )

    def delete_table(self, table_name):
        """
        Delete a Table in the connected DynamoDB

        :param table_name: The name of the table to delete
        :return: None
        """
        self.db.delete_table(TableName=table_name)

    def list_tables(self):
        """
        Lists all existing Tables within the connected DynamoDB

        :return: list, A list of Table Names, that exist
        """
        res = self.db.list_tables()
        return res['TableNames']

    def update_table(self, table_name: str, attribute_definitions: list, key_schema: list,
                     local_secondary_indexes: list = None,
                     global_secondary_indexes: list = None,
                     billing_mode: str = None,
                     provisioned_throughput: dict = None,
                     stream_specification: dict = None,
                     sse_specification: dict = None,
                     tags: list = None,
                     table_class: str = None,
                     deletion_protection_enabled: bool = None):
        """
        Update a Table in the connected DynamoDB

        :param table_name: str, Name of the Table
        :param attribute_definitions: list, An array of attributes that describe the key schema for the table and indexes.
        :param key_schema: list, Specifies the attributes that make up the primary key for a table or an index. The attributes in KeySchema must also be defined in the AttributeDefinitions array. For more information, see Data Model in the Amazon DynamoDB Developer Guide.
        :param local_secondary_indexes: list, One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained.
        :param global_secondary_indexes: list, One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following:
        :param billing_mode: str, Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.
        :param provisioned_throughput: dict, Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the UpdateTable operation.
        :param stream_specification: dict, The settings for DynamoDB Streams on the table.
        :param sse_specification: dict, Represents the settings used to enable server-side encryption.
        :param tags: list, A list of key-value pairs to label the table. For more information, see Tagging for DynamoDB.
        :param table_class: str, The table class of the new table. Valid values are STANDARD and STANDARD_INFREQUENT_ACCESS.
        :param deletion_protection_enabled: bool, Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.
        :return: None
        """
        self.db.update_table(
            AttributeDefinitions=attribute_definitions,
            TableName=table_name,
            KeySchema=key_schema,
            LocalSecondaryIndexes=local_secondary_indexes,
            GlobalSecondaryIndexes=global_secondary_indexes,
            BillingMode=billing_mode,
            ProvisionedThroughput=provisioned_throughput,
            StreamSpecification=stream_specification,
            SSESpecification=sse_specification,
            Tags=tags,
            TableClass=table_class,
            DeletionProtectionEnabled=deletion_protection_enabled
        )

    def create_item(self, table_name: str, item: dict,
                    return_values: str = None,
                    return_consumed_capacity: str = None,
                    return_item_collection_metrics: str = None,
                    conditional_operator: str = None,
                    conditional_expression: str = None,
                    expression_attribute_names: dict = None,
                    expression_attribute_values: dict = None):
        """
        Create (Put) an item in(to) the specified Table.

        :param table_name: str, The name of the table from which to delete the item.
        :param item: dict, A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
        :param return_values: str, Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request. For PutItem, the valid values are:
        :param return_consumed_capacity: str, Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response
        :param return_item_collection_metrics: str, Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.
        :param conditional_operator: str, This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.
        :param conditional_expression: str, A condition that must be satisfied in order for a conditional PutItem operation to succeed.
        :param expression_attribute_names: dict, One or more substitution tokens for attribute names in an expression.
        :param expression_attribute_values: dict, One or more values that can be substituted in an expression.
        :return: None
        """

        item = {k: self.serializer.serialize(v) for k, v in item.items()}
        self.db.put_item(
            TableName=table_name,
            Item=item,
            ReturnValues=return_values,
            ReturnConsumedCapacity=return_consumed_capacity,
            ReturnItemCollectionMetrics=return_item_collection_metrics,
            ConditionalOperator=conditional_operator,
            ConditionExpression=conditional_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )

    def delete_item(self, table_name: str, key: dict,
                    return_values: str = None,
                    return_consumed_capacity: str = None,
                    return_item_collection_metrics: str = None,
                    conditional_operator: str = None,
                    conditional_expression: str = None,
                    expression_attribute_names: dict = None,
                    expression_attribute_values: dict = None):
        """
        Delete an item from the specified Table.

        :param table_name: str, The name of the table from which to delete the item.
        :param key: dict, A map of attribute names to AttributeValue objects, representing the primary key of the item to delete.
        :param return_values: str, Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request. For PutItem, the valid values are:
        :param return_consumed_capacity: str, Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response
        :param return_item_collection_metrics: str, Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.
        :param conditional_operator: str, This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.
        :param conditional_expression: str, A condition that must be satisfied in order for a conditional PutItem operation to succeed.
        :param expression_attribute_names: dict, One or more substitution tokens for attribute names in an expression.
        :param expression_attribute_values: dict, One or more values that can be substituted in an expression.
        :return: None
        """
        key = {k: self.serializer.serialize(v) for k, v in key.items()}
        self.db.delete_item(
            TableName=table_name,
            Key=key,
            ReturnValues=return_values,
            ReturnConsumedCapacity=return_consumed_capacity,
            ReturnItemCollectionMetrics=return_item_collection_metrics,
            ConditionalOperator=conditional_operator,
            ConditionExpression=conditional_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )

    def get_item(self, table_name: str, key: dict,
                 consistent_read: bool = None,
                 return_consumed_capacity: str = None,
                 projection_expression: str = None,
                 expression_attribute_names: dict = None):
        """
        Reads an Item from the given Table in the connected DynamoDB

        :param table_name: str, The name of the table containing the requested item.
        :param key: dict, A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve.d
        :param consistent_read: bool, Determines the read consistency model: If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.
        :param return_consumed_capacity: str, Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response
        :param projection_expression: str, A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.
        :param expression_attribute_names: dict, One or more substitution tokens for attribute names in an expression.
        :return: dict, The Item found in the given Table or None, if no item was found
        """
        key = {k: self.serializer.serialize(v) for k, v in key.items()}
        res = self.db.get_item(
            TableName=table_name,
            Key=key,
            ConsistentRead=consistent_read,
            ReturnConsumedCapacity=return_consumed_capacity,
            ProjectionExpression=projection_expression,
            ExpressionAttributeNames=expression_attribute_names
        )
        if "Item" in res.keys():
            item = res["Item"]
            item = {k: self.deserializer.deserialize(v) for k, v in item.items()}
            return item
        return None

    def query_table(self, table_name: str,
                    index_name: str = None,
                    select: str = None,
                    limit: int = None,
                    consistent_read: bool = None,
                    scan_index_forward: bool = None,
                    exclusive_start_key: dict = None,
                    return_consumed_capacity: str = None,
                    projection_expression: str = None,
                    filter_expression: str = None,
                    key_condition_expression: str = None,
                    expression_attribute_names: dict = None,
                    expression_attribute_values: dict = None):
        """
        Queries a Table and returns a list of items as a result

        :param table_name: str, The name of the table containing the requested items.
        :param index_name: str, The name of an index to query.
        :param select: str, The attributes to be returned in the result.
        :param limit: int, The maximum number of items to evaluate (not necessarily the number of matching items).
        :param consistent_read: bool, Determines the read consistency model: If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.
        :param scan_index_forward: bool, Specifies the order for index traversal: If true (default), the traversal is performed in ascending order; if false, the traversal is performed in descending order.
        :param exclusive_start_key: dict, The primary key of the first item that this operation will evaluate.
        :param return_consumed_capacity: str, Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response
        :param projection_expression: str, A string that identifies one or more attributes to retrieve from the table.
        :param filter_expression: str, A string that contains conditions that DynamoDB applies after the Query operation, but before the data is returned to you.
        :param key_condition_expression: str, The condition that specifies the key values for items to be retrieved by the Query action.
        :param expression_attribute_names: dict, One or more substitution tokens for attribute names in an expression.
        :param expression_attribute_values: dict, One or more values that can be substituted in an expression.
        :return: list, a list of items that match the query or None, if no items were found
        """
        res = self.db.query(
            TableName=table_name,
            IndexName=index_name,
            Select=select,
            Limit=limit,
            ConsistentRead=consistent_read,
            ScanIndexForward=scan_index_forward,
            ExclusiveStartKey=exclusive_start_key,
            ReturnConsumedCapacity=return_consumed_capacity,
            ProjectionExpression=projection_expression,
            FilterExpression=filter_expression,
            KeyConditionExpression=key_condition_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        if "Count" in res.keys():
            count = res["Count"]
            if count > 0 and "Items" in res.keys():
                items = res["Items"]
                items = [{k: self.deserializer.deserialize(v) for k, v in item.items()} for item in items]
                return items
            return None
        return None

    def scan_table(self, table_name: str,
                   index_name: str = None,
                   limit: int = None,
                   select: str = None,
                   exclusive_start_key: dict = None,
                   return_consumed_capacity: str = None,
                   total_segments: int = None,
                   segment: int = None,
                   projection_expression: str = None,
                   filter_expression: str = None,
                   consistent_read: bool = None,
                   expression_attribute_names: dict = None,
                   expression_attribute_values: dict = None):
        """

        :param table_name: str, The name of the table containing the requested items; or, if you provide IndexName, the name of the table to which that index belongs.
        :param index_name: str, The name of a secondary index to scan.
        :param limit: int, The maximum number of items to evaluate (not necessarily the number of matching items).
        :param select: str, The attributes to be returned in the result.
        :param exclusive_start_key: dict, The primary key of the first item that this operation will evaluate.
        :param return_consumed_capacity: str, Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response
        :param total_segments: int, For a parallel Scan request, TotalSegments represents the total number of segments into which the Scan operation will be divided.
        :param segment: int, For a parallel Scan request, Segment identifies an individual segment to be scanned by an application worker.
        :param projection_expression: str, A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document.
        :param filter_expression: str, A string that contains conditions that DynamoDB applies after the Scan operation, but before the data is returned to you.
        :param consistent_read: bool, A Boolean value that determines the read consistency model during the scan
        :param expression_attribute_names: dict, One or more substitution tokens for attribute names in an expression.
        :param expression_attribute_values: dict, One or more values that can be substituted in an expression.
        :return:
        """
        res = self.db.scan(
            TableName=table_name,
            IndexName=index_name,
            Select=select,
            Limit=limit,
            ConsistentRead=consistent_read,
            ExclusiveStartKey=exclusive_start_key,
            ReturnConsumedCapacity=return_consumed_capacity,
            TotalSegments=total_segments,
            Segment=segment,
            ProjectionExpression=projection_expression,
            FilterExpression=filter_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        if "Count" in res.keys():
            count = res["Count"]
            if count > 0 and "Items" in res.keys():
                items = res["Items"]
                items = [{k: self.deserializer.deserialize(v) for k, v in item.items()} for item in items]
                return items
            return None
        return None
