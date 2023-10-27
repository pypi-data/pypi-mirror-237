from .blob import BlobManager
from .table import TableManager
from .queue import QueueManager


class Eazure:
    connection_string = None

    def __init__(self, connection_string=None):
        self.connection_string = connection_string or Eazure.connection_string

    # BLOB METHODS
    def download_blob(self, container_name, blob_name, output_file_path, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.download_blob(container_name, blob_name, output_file_path)

    def upload_blob(self, container_name, blob_name, blob_content, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        blob_manager.upload_blob(container_name, blob_name, blob_content)

    def blob_exists(self, container_name, blob_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.blob_exists(container_name, blob_name)

    def delete_blob(self, container_name, blob_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.delete_blob(container_name, blob_name)

    def list_blobs_in_container(self, container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.list_blobs_in_container(container_name)

    def create_container(self, container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.create_container(container_name)

    def list_containers(self, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.list_containers()

    def delete_container(self, container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.delete_container(container_name)

    def rename_container(self, container_name, new_container_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        blob_manager = BlobManager(connection_string)
        return blob_manager.rename_container(container_name, new_container_name)

    # TABLE METHODS
    def create_table(self, table_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.create_table(table_name)

    def create_entity(self, table_name, new_entity, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.create_entity(table_name, new_entity)

    def get_all_entities(self, table_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.get_all_entities(table_name)

    def get_single_entity(self, table_name, partition_key, row_key, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.get_single_entity(table_name, partition_key, row_key)

    def update_entity(self, table_name, partition_key, row_key, new_entity, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.update_entity(table_name, partition_key, row_key, new_entity)

    def remove_entity(self, table_name, partition_key, row_key, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.remove_entity(table_name, partition_key, row_key)

    def get_cell_value(self, table_name, partition_key, row_key, cell_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        table_manager = TableManager(connection_string)
        return table_manager.get_cell_value(table_name, partition_key, row_key, cell_name)

    # QUEUE METHODS
    def get_queue_item(self, queue_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.get_queue_item(queue_name)

    def add_message_to_queue(self, queue_name, message, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.add_message_to_queue(queue_name, message)

    def get_queue_length(self, queue_name, connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.get_queue_length(queue_name)

    def delete_message_from_queue(self, queue_name, message_id,connection_string=None):
        connection_string = connection_string or self.connection_string
        if connection_string is None:
            raise ValueError("A connection string must be provided")
        queue_manager = QueueManager(connection_string)
        return queue_manager.delete_message(queue_name, message_id)