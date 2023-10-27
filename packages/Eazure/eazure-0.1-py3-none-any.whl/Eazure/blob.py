from azure.storage.blob import BlobServiceClient, BlobType, ContainerClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
import os
import tempfile
import logging


class BlobManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    def blob_exists(self, container_name, blob_name):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        # If blob exists don't upload
        exists = blob_client.exists()

        if exists:
            print(f"{blob_name} was found in the {container_name} container")
        else:
            print(f"{blob_name} was not found in the {container_name}")
        return exists

    def delete_blob(self, container, blob_name):
        blob_client = self.blob_service_client.get_blob_client(
            container=container, blob=blob_name
        )
        try:
            blob_client.delete_blob()
            print(f"deleted {blob_name} from the {container} container")
            return True
        except:
            print(f"failed to delete {blob_name} from {container} container")
            return False

    def upload_blob(self, container_name, blob_name, local_file_path):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        # check if container exists
        container = self.create_container(container_name)
        logging.info(f"container {container_name} exists")

        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"uploaded {blob_name} to the {container_name} container")

    def download_blob(self, container_name, blob_name, output_file_path):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )

        with open(output_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        print(f"File downloaded successfully to {output_file_path}")

    def list_blobs_in_container(self, container_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_list = container_client.list_blobs()

        # Iterate over the blob_list to get the blob names
        blob_names = [blob.name for blob in blob_list]

        return blob_names

    def list_containers(self):
        containers = []
        for container in self.blob_service_client.list_containers():
            containers.append(container.name)

        return containers

    def create_container(self, container_name):
        try:
            container_client = self.blob_service_client.create_container(container_name)
            print(f"Container {container_name} created")
            return container_client
        except HttpResponseError as e:
            if (
                e.status_code == 409
            ):  # HTTP status code 409 means 'Conflict', i.e., the resource already exists
                print(f"Container {container_name} already exists")
                return container_client

    def delete_container(self, container_name):
        try:
            container_client = self.blob_service_client.get_container_client(container_name)
            container_client.delete_container()
            print(f"Container {container_name} deleted")
        except ResourceNotFoundError:
            print(f"Container {container_name} not found.")

    def rename_container(self, old_name, new_name):
        # Create a new container
        try:
            self.create_container(new_name)
        except Exception as e:
            print(f"Failed to create container {new_name}. Error: {str(e)}")
            return

        # Get reference to the old container
        try:
            old_container_client = self.blob_service_client.get_container_client(old_name)
        except ResourceNotFoundError:
            print(f"Container {old_name} not found.")
            return

        # Copy all the blobs from old container to new container
        try:
            blobs = self.list_blobs(old_name)
            for blob in blobs:
                old_blob_client = old_container_client.get_blob_client(blob)
                # Download the blob to a stream
                data = old_blob_client.download_blob().readall()
                # Create a new blob in the new container
                self.create_blob_any_type(blob, data, new_name)

            print(f"All blobs copied from container {old_name} to {new_name}")
        except Exception as e:
            print(f"Failed to copy blobs. Error: {str(e)}")
            return

        # Delete the old container
        try:
            self.delete_container(old_name)
        except ResourceNotFoundError:
            print(f"Container {old_name} not found.")

