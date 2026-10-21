# Gemini Enterprise REST API Reference (v1alpha) / Method: projects.locations.collections.engines.analytics.exportMetrics
Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.analytics/exportMetrics, page last updated 2026-10-09, extracted 2026-10-19

Exports metrics.

### HTTP request

Choose an endpoint:

global us

`POST https://discoveryengine.googleapis.com/v1alpha/{analytics=projects/*/locations/*/collections/*/engines/*/analytics}:exportMetrics`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters | |
| --- | --- |
| `analytics` | `string`  Required. The analytics resource name under the engine where the metrics are created. The format is `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/analytics`. |

### Request body

The request body contains data with the following structure:

**JSON representation**

```
{
  "outputConfig": {
    object (OutputConfig)
  },
  "startDate": {
    object (Date)
  }
}
```

| Fields | |
| --- | --- |
| `outputConfig` | `object (OutputConfig)`  Required. The output location of the data. |
| `startDate` | `object (Date)`  Optional. The earliest date (inclusive), interpreted in the UTC time zone, whose metrics are included in the export.  If unset, defaults to 30 days before the current UTC date. The value must be a valid calendar date that is not in the future and not older than 180 days (the source data retention window); otherwise the request fails with `INVALID_ARGUMENT`. |

### Response body

If successful, the response body contains an instance of `Operation`.

### Authorization scopes

Requires one of the following OAuth scopes:

- `https://www.googleapis.com/auth/cloud-platform`
- `https://www.googleapis.com/auth/discoveryengine.readwrite`
- `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## OutputConfig

The output configuration setting.

**JSON representation**

```
{

  // The following is a list of mutually exclusive fields. At most one of the
  // fields will be set in a response:
  "bigqueryDestination": {
    object (BigQueryDestination)
  }
  // End of mutually exclusive fields.
}
```

| Fields | |
| --- | --- |
| The configuration of destination for holding output data. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response: | |
| `bigqueryDestination` | `object (BigQueryDestination)`  The BigQuery location where the output is to be written to. |
| End of mutually exclusive fields. | |

## BigQueryDestination

The BigQuery output destination configuration.

**JSON representation**

```
{
  "datasetId": string,
  "tableId": string
}
```

| Fields | |
| --- | --- |
| `datasetId` | `string`  Required. The ID of a BigQuery Dataset. |
| `tableId` | `string`  Required. The tableId of exported BigQuery table. |
