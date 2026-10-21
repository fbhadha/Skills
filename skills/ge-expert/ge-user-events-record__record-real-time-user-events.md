# Gemini Enterprise Docs (User events) / Record real-time user events
Source: https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events, page last updated 2026-10-14, extracted 2026-10-19

This page describes how to record user events in real time.

For the user event types that you can record, see the `eventType` field of the
[`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) object. By ingesting user events, you can improve the
quality of your results. For example, user events affect the ranking of search
results. Results with higher click-through rates are boosted, while results with
lower click-through rates are buried. Don't record user events for documents
that you have not yet imported.

If you are using an app with multiple data stores attached, ingest user events
at the location level instead of the data-store level. This allows a given user
event to be sent to the data store that it's associated with. When recording
user events at a location level, you must include the `engine` field in the user
events to associate the event with the correct app. For examples of user events
that include the `engine` field, see the following:

- [Custom apps user event type examples and schemas](https://docs.cloud.google.com/gemini/enterprise/docs/user-events#formats)

To import historical user events in bulk, see [Import historical user events](https://docs.cloud.google.com/gemini/enterprise/docs/import-user-events).

You can record user events in the following ways:

- [With a JavaScript pixel](#record-with-javascript-pixel).
- [With the `userEvents.write` method](#record-with-userevents-write-method).

For the JSON representation for user events, see
[`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) in the API reference.

## Before you begin

Before you import user events:

- Create a data store and an app.
- Review [About user events](https://docs.cloud.google.com/gemini/enterprise/docs/user-events)
  for user event requirements.

## Record real-time user events with a JavaScript pixel

To record user events with a JavaScript pixel:

1. [Create an API key](#create-key) for calls to the [`userEvents.collect`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect)
   method.
2. See the [JavaScript pixel example](#js-pixel-example) for an example of a
   JavaScript tag that collects user events.

### Create an API key

An API key is required if you use a JavaScript pixel to collect user events from
users' browsers.

To create an API key for calls to the [`userEvents.collect`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect)
method, complete the following steps:

1. In the Google Cloud console, go to the **Credentials** page.

   [Credentials](https://console.cloud.google.com/apis/credentials)
2. In the project list at the top of the Google Cloud console page, select
   your project (the project might already be selected).
3. Click **Create credentials** and then select **API key**.
   *Don't add any referrer restrictions*. Some user privacy settings don't
   pass the referrer URL.

   - Take note of the generated API key, which you will use when calling
     user event logging.
4. For increased security, add an
   [HTTP restriction](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions)
   to your API Key to restrict access to the Gemini Enterprise service
   at `https://discoveryengine.googleapis.com/*`.

**Note:** The API key is only for authenticating the
[`userEvents.collect`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect) method and the
[`servingConfigs.searchLite`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method.
Other Gemini Enterprise methods require OAuth 2.0 through a service account
or a user account.

### JavaScript pixel example

The following example records a `view-item` user event using a JavaScript
pixel.

For the JSON representation for user events, see [`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) in
the API reference.

```
<script type="text/javascript">
var user_event = {
  "eventType" : "view-item",
  "userPseudoId": "USER_PSEUDO_ID",
  "engine": "projects/PROJECT_ID/locations/LOCATION_ID/collections/default_collection/engines/APP_ID",
  "userInfo": {
      "userId": "USER_ID"
  },
  "attributionToken": "ATTRIBUTION_TOKEN",
  "tagIds": "TAG_ID",
  "documents": [
      {
        "id": "DOCUMENT_ID"
      }
  ]
};

var _gre = _gre || {};
// Credentials for project.
_gre.apiKey = '[API_KEY]';
_gre.logEvent = user_event;
_gre.projectId = 'PROJECT_ID';
_gre.locationId = 'LOCATION_ID';
_gre.dataStoreId = 'DATA_STORE_ID';

(function() {
  var gre = document.createElement('script'); gre.type = 'text/javascript'; gre.async = true;
  gre.src = 'https://www.gstatic.com/discoveryengine/v1beta_event.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(gre, s);
})();

</script>
```

## Record real-time user events with the `userEvents.write` method

### REST

You can use the [`userEvents.write`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write)
method to send user events directly to the API from your backend server.

To record user events, send a POST request to the `userEvents.write` method and
provide the appropriate request body. For the JSON representation for user
events, see [`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource:-userevent) in the API reference.

If you are recording user events at the location level, use the endpoint
`https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/userEvents:write`.

```
curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/userEvents:write" \
     -d '{
         "eventType": "view-item",
         "userPseudoId": "visitor0",
         "engine": "projects/PROJECT_NUMBER/locations/global/collections/default_collection/engines/APP_ID",
         "eventTime": "2020-01-01T03:33:33.000001Z",
         "tagIds": ["321"],
         "attributionToken": "ABC",
         "attributes": {
            "example_text_attribute": {
              "text": ["text_1", "text_2"]
            },
            "example_number_attribute": {
               "numbers": [3.14, 42, 1.2345]
            }
          },
         "documents": [{
            "id": "abc"
          }],
         "userInfo": {
           "userId": "abc",
           "userAgent": "Mozilla/5.0"
         },
         "pageInfo": {
          "uri": "http://example",
          "referrerUri": "http://example",
          "pageViewId": "currentPageUri"
         }
        }'
```

### C#

Before trying this sample, follow the C# setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise C# API
reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
using Google.Cloud.DiscoveryEngine.V1;

public sealed partial class GeneratedUserEventServiceClientSnippets
{
    /// <summary>Snippet for WriteUserEvent</summary>
    /// <remarks>
    /// This snippet has been automatically generated and should be regarded as a code template only.
    /// It will require modifications to work:
    /// - It may require correct/in-range values for request initialization.
    /// - It may require specifying regional endpoints when creating the service client as shown in
    ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
    /// </remarks>
    public void WriteUserEventRequestObject()
    {
        // Create client
        UserEventServiceClient userEventServiceClient = UserEventServiceClient.Create();
        // Initialize request argument(s)
        WriteUserEventRequest request = new WriteUserEventRequest
        {
            ParentAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
            UserEvent = new UserEvent(),
            WriteAsync = false,
        };
        // Make the request
        UserEvent response = userEventServiceClient.WriteUserEvent(request);
    }
}
```

### Go

Before trying this sample, follow the Go setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Go API
reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
//go:build examples

package main

import (
	"context"

	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
)

func main() {
	ctx := context.Background()
	// This snippet has been automatically generated and should be regarded as a code template only.
	// It will require modifications to work:
	// - It may require correct/in-range values for request initialization.
	// - It may require specifying regional endpoints when creating the service client as shown in:
	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
	c, err := discoveryengine.NewUserEventClient(ctx)
	if err != nil {
		// TODO: Handle error.
	}
	defer c.Close()

	req := &discoveryenginepb.WriteUserEventRequest{
		// TODO: Fill request struct fields.
		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#WriteUserEventRequest.
	}
	resp, err := c.WriteUserEvent(ctx, req)
	if err != nil {
		// TODO: Handle error.
	}
	// TODO: Use resp.
	_ = resp
}
```

### Java

Before trying this sample, follow the Java setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Java API
reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
import com.google.cloud.discoveryengine.v1.DataStoreName;
import com.google.cloud.discoveryengine.v1.UserEvent;
import com.google.cloud.discoveryengine.v1.UserEventServiceClient;
import com.google.cloud.discoveryengine.v1.WriteUserEventRequest;

public class SyncWriteUserEvent {

  public static void main(String[] args) throws Exception {
    syncWriteUserEvent();
  }

  public static void syncWriteUserEvent() throws Exception {
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in
    // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
    try (UserEventServiceClient userEventServiceClient = UserEventServiceClient.create()) {
      WriteUserEventRequest request =
          WriteUserEventRequest.newBuilder()
              .setParent(
                  DataStoreName.ofProjectLocationDataStoreName(
                          "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                      .toString())
              .setUserEvent(UserEvent.newBuilder().build())
              .setWriteAsync(true)
              .build();
      UserEvent response = userEventServiceClient.writeUserEvent(request);
    }
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
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import discoveryengine_v1

def sample_write_user_event():
    # Create a client
    client = discoveryengine_v1.UserEventServiceClient()

    # Initialize request argument(s)
    request = discoveryengine_v1.WriteUserEventRequest(
        parent="parent_value",
    )

    # Make the request
    response = client.write_user_event(request=request)

    # Handle the response
    print(response)
```

### Ruby

Before trying this sample, follow the Ruby setup instructions in the
[Gemini Enterprise quickstart using
client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries).
For more information, see the
[Gemini Enterprise Ruby API
reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest).

To authenticate to Gemini Enterprise, set up Application Default Credentials.
For more information, see
[Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

```
require "google/cloud/discovery_engine/v1"

##
# Snippet for the write_user_event call in the UserEventService service
#
# This snippet has been automatically generated and should be regarded as a code
# template only. It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
# client as shown in https://cloud.google.com/ruby/docs/reference.
#
# This is an auto-generated example demonstrating basic usage of
# Google::Cloud::DiscoveryEngine::V1::UserEventService::Client#write_user_event.
#
def write_user_event
  # Create a client object. The client can be reused for multiple calls.
  client = Google::Cloud::DiscoveryEngine::V1::UserEventService::Client.new

  # Create a request. To set request fields, pass in keyword arguments.
  request = Google::Cloud::DiscoveryEngine::V1::WriteUserEventRequest.new

  # Call the write_user_event method.
  result = client.write_user_event request

  # The returned object is of type Google::Cloud::DiscoveryEngine::V1::UserEvent.
  p result
end
```
