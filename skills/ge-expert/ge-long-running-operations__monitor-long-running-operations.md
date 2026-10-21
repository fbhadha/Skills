# Gemini Enterprise Docs (Monitor usage) / Monitor long-running operations
Source: https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations, page last updated 2026-10-14, extracted 2026-10-19

This page describes how to manage the lifecycle of a long-running operation
(LRO) in Gemini Enterprise.

A [long-running operation](https://google.aip.dev/151) object is returned when a call
to a method might take a long time to complete. For example, the Gemini Enterprise API creates a long-running operation when you call
[`documents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents/import)
through the API or Client Libraries. The operation tracks the status of the
processing job.

You can use the long-running operations methods that the Gemini Enterprise API provides to
check the [status](https://google.aip.dev/216#common-states) of the operations. You
can also list or poll operations.

The record of an operation is kept for approximately 30 days after the operation
finishes, meaning that you can't view or list an operation after that time.

## List long-running operations

The following show how to list the operations for a Google Cloud
resource.

**Note:** Long running operations can't be filtered or paginated in
Gemini Enterprise. That is, when you call the `operations.list` method,
you can't use the `filter`, `pageSize`, or `pageToken` fields.

### REST

To list the long-running operations for a Google Cloud resource, follow
this step:

- Call the [`operations.list`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.operations/list)
  method:

  ```
  curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/operations"
  ```

  `DATA_STORE_ID`: The ID of the Gemini Enterprise data store that
  was created with your engine. In the Google Cloud console URL, the data store ID
  appears after `engines/` and before `/data`.

### Python

Before trying this sample, follow the Python setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Python API
reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
from typing import Optional

from google.cloud import discoveryengine
from google.longrunning import operations_pb2

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_PROCESSOR_LOCATION"  # Options: "global"
# search_engine_id = "YOUR_SEARCH_ENGINE_ID"

# Create filter in https://google.aip.dev/160 syntax
# operations_filter = "YOUR_FILTER"

def list_operations_sample(
    project_id: str,
    location: str,
    search_engine_id: str,
    operations_filter: Optional[str] = None,
) -> operations_pb2.ListOperationsResponse:
    # Create a client
    client = discoveryengine.DocumentServiceClient()

    # The full resource name of the search engine branch.
    name = f"projects/{project_id}/locations/{location}/collections/default_collection/dataStores/{search_engine_id}"

    # Make ListOperations request
    request = operations_pb2.ListOperationsRequest(
        name=name,
        filter=operations_filter,
    )

    # Make ListOperations request
    response = client.list_operations(request=request)

    # Print the Operation Information
    for operation in response.operations:
        print(operation)

    return response
```

## Get details about a long-running operation

The following show how to get details about an operation.

### REST

To get the status of and view details about a long-running operation, follow these steps:

1. Find the name of the operation in one of two ways:

   - After you've made a call to a method that returns a long-running
     operation, review the response.

     For example, if you call
     [`documents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents/import),
     the start of the response looks something like this:

     ```
     {
       "operations": [
         {
           "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-datastore_4321/branches/0/operations/import-documents-56789",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.ImportDocumentsMetadata",
           }
         }
       ]
     }
     ```

     The `name` value in the response provides the operation name, which can
     be used to query the operation status. Don't include the quotes when you
     copy the operation name.
   - Get the operation name by [listing long-running
     operations](#list-lros).
2. Call the [`operations.get`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.operations/get)
   method on the resource that created the operation:

   ```
   curl -X GET \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       "https://discoveryengine.googleapis.com/v1/OPERATION_NAME"
   ```

   `OPERATION_NAME`: Provide the name of the operation for
   which you need information. You can find the operation name by
   [listing long-running operations](#list-lros).

   The first lines of the response from the `GET` command look something like this:

   ```
   {
         "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-datastore_4321/branches/0/operations/import-documents-56789",
         "metadata": {
           "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.ImportDocumentsMetadata"
         }
       }
   ```

### Python

Before trying this sample, follow the Python setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Python API
reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
from google.cloud import discoveryengine
from google.longrunning import operations_pb2

# TODO(developer): Uncomment these variables before running the sample.
# Example: `projects/{project}/locations/{location}/collections/{default_collection}/dataStores/{search_engine_id}/branches/{0}/operations/{operation_id}`
# operation_name = "YOUR_OPERATION_NAME"

def get_operation_sample(operation_name: str) -> operations_pb2.Operation:
    # Create a client
    client = discoveryengine.DocumentServiceClient()

    # Make GetOperation request
    request = operations_pb2.GetOperationRequest(name=operation_name)
    operation = client.get_operation(request=request)

    # Print the Operation Information
    print(operation)

    return operation
```

## Poll a long-running operation

The following show how to poll the status of an operation.

### REST

To poll the long-running operation until it finishes, follow these steps:

1. Run the following command, which calls the
   [`operations.get`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.operations/get)
   method repeatedly, using a backoff of 10 seconds between each request:

   ```
   while true; \
       do curl -X GET \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       "https://discoveryengine.googleapis.com/v1/OPERATION_NAME"; \
       sleep 10; \
       done
   ```

   `OPERATION_NAME`: Provide the name of the operation you want to
   poll. You can find the operation name by
   [listing long-running operations](#list-lros).
   For example, `projects/12345/locations/global/collections/default_collection/dataStores/my-datastore_4321/branches/0/operations/import-documents-56789`.
2. Stop the polling job (`Control+Z`) after the status shows `"done": true`.

### Python

Before trying this sample, follow the Python setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Python API
reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
from time import sleep

from google.cloud import discoveryengine
from google.longrunning import operations_pb2

# TODO(developer): Uncomment these variables before running the sample.
# Example: `projects/{project}/locations/{location}/collections/{default_collection}/dataStores/{search_engine_id}/branches/{0}/operations/{operation_id}`
# operation_name = "YOUR_OPERATION_NAME"

def poll_operation_sample(
    operation_name: str, limit: int = 10
) -> operations_pb2.Operation:
    # Create a client
    client = discoveryengine.DocumentServiceClient()

    # Make GetOperation request
    request = operations_pb2.GetOperationRequest(name=operation_name)

    for _ in range(limit):
        operation = client.get_operation(request=request)
        # Print the Operation Information
        print(operation)

        # Stop polling when Operation is no longer running
        if operation.done:
            break

        # Wait 10 seconds before polling again
        sleep(10)

    return operation
```

## Cancel a long-running operation

The following shows how to cancel an operation:

### REST

To cancel a long-running operation, follow these steps:

- Call the [`operations.cancel`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.operations/cancel)
  method:

  ```
  curl -X post \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     "https://discoveryengine.googleapis.com/v1/OPERATION_NAME":cancel
  ```

  `OPERATION_NAME`: Provide the name of the operation you
  want to cancel. You can find the operation name by
  [listing long-running operations](#list-lros).
  For example, `projects/12345/locations/global/collections/default_collection/dataStores/my-datastore_4321/branches/0/operations/import-documents-56789`.

  After the API call is made, the server attempts to cancel the operation.
  The results you see and the actions you can take are as follows:

  - An error with `"code": 400` and `"status": "FAILED_PRECONDITION"`
    indicates that the request couldn't be canceled.
  - A successful cancellation results in an empty JSON object. To verify the
    cancellation:

    - Use the [`operations.get`](#get-details) method.
    - If the operation is successfully cancelled, the response from the
      `operations.get` method has the error `"code": 1`, which represents
      the `CANCELLED` status code.

      For example:

      ```
      {
        "name": "projects/12345/locations/global/collections/default_collection/dataStores/my-datastore_4321/branches/0/operations/import-documents-56789",
        "metadata": {
          "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.ImportDocumentsMetadata",
          "createTime": "2025-04-28T21:29:21.199190Z",
          "updateTime": "2025-04-28T21:31:29.076865Z"
        },
        "done": true,
        "error": {
          "code": 1,
          "message": "Operation projects/12345/locations/global/collections/default_collection/dataStores/my-datastore_4321/branches/0/operations/import-documents-56789 is cancelled."
        }
      }
      ```

### Python

Before trying this sample, follow the Python setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Python API
reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
from google.cloud import discoveryengine
from google.longrunning import operations_pb2

# TODO(developer): Uncomment these variables before running the sample.
# Example: `projects/{project}/locations/{location}/collections/{default_collection}/dataStores/{search_engine_id}/branches/{0}/operations/{operation_id}`
# operation_name = "YOUR_OPERATION_NAME"

def cancel_operation_sample(operation_name: str) -> None:
    # Create a client
    client = discoveryengine.DocumentServiceClient()

    # Make CancelOperation request
    request = operations_pb2.CancelOperationRequest(name=operation_name)
    client.cancel_operation(request=request)

    return
```
