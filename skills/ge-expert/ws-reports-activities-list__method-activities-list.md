# Google Workspace Admin SDK Reports API / Method: activities.list
Source: https://developers.google.com/workspace/admin/reports/reference/rest/v1/activities/list, page last updated 2026-10-02, extracted 2026-10-19

Retrieves a list of activities for a specific customer's account and application such as the Admin console application or the Google Drive application. For more information, see the guides for [administrator](https://docs.cloud.google.com/admin-sdk/reports/v1/guides/manage-audit-admin) and [Google Drive](https://docs.cloud.google.com/admin-sdk/reports/v1/guides/manage-audit-drive) activity reports. For more information about the activity report's parameters, see the [activity parameters](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/admin-event-names) reference guides.

### HTTP request

`GET https://admin.googleapis.com/admin/reports/v1/activity/users/{userKey or all}/applications/{applicationName}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters | |
| --- | --- |
| `userKey or all` | `string`  Represents the profile ID or the user email for which the data should be filtered. Can be `all` for all information, or `userKey` for a user's unique Google Workspace profile ID or their primary email address. Must not be a deleted user. For a deleted user, call `users.list` in Directory API with  [`showDeleted=true`](https://developers.google.com/workspace/admin/directory/reference/rest/v1/users/list#body.QUERY_PARAMETERS.show_deleted), then use the returned `ID` as the `userKey`. |
| `applicationName` | `enum (ApplicationName)`  Application name for which the events are to be retrieved. |

### Query parameters

**Parameters**

**actorIpAddress**

`string`

The Internet Protocol (IP) Address of host where the event was performed. This is an additional way to filter a report's summary using the IP address of the user whose activity is being reported. This IP address may or may not reflect the user's physical location. For example, the IP address can be the user's proxy server's address or a virtual private network (VPN) address. This parameter supports both [IPv4](http://wikipedia.org/wiki/IPv4) and [IPv6](http://wikipedia.org/wiki/IPv6_address) address versions.

**customerId**

`string`

The unique ID of the customer to retrieve data for.

**endTime**

`string`

Sets the end of the range of time shown in the report. The date is in the [RFC 3339 format](http://www.ietf.org/rfc/rfc3339.txt), for example 2010-10-28T10:26:35.000Z. The default value is the approximate time of the API request. An API report has three basic time concepts:

- **Date of the API's request for a report**: When the API created and retrieved the report.
- **Report's start time**: The beginning of the timespan shown in the report. The `startTime` must be before the `endTime` (if specified) and the current time when the request is made, or the API returns an error.
- **Report's end time**: The end of the timespan shown in the report. For example, the timespan of events summarized in a report can start in April and end in May. The report itself can be requested in August.

If the `endTime` is not specified, the report returns all activities from the `startTime` until the current time or the most recent 180 days if the `startTime` is more than 180 days in the past.

 For Gmail requests, `startTime` and `endTime` must be provided and the difference must not be greater than 30 days.

**eventName**

`string`

The name of the event being queried by the API. Each `eventName` is related to a specific Google Workspace service or feature which the API organizes into types of events. An example is the Google Calendar events in the Admin console application's reports. The Calendar Settings `type` structure has all of the Calendar `eventName` activities reported by the API. When an administrator changes a Calendar setting, the API reports this activity in the Calendar Settings `type` and `eventName` parameters. For more information about `eventName` query strings and parameters, see the list of event names for various applications above in `applicationName`.

**filters**

`string`

The `filters` query string is a comma-separated list composed of event parameters manipulated by relational operators. Event parameters are in the form `{parameter1 name}{relational operator}{parameter1 value},{parameter2
name}{relational operator}{parameter2 value},...`

These event parameters are associated with a specific `eventName`. An empty report is returned if the request's parameter doesn't belong to the `eventName`. For more information about the available `eventName` fields for each application and their associated parameters, go to the [ApplicationName](#applicationname) table, then click through to the Activity Events page in the Appendix for the application you want.

In the following Drive activity examples, the returned list consists of all `edit` events where the `doc_id` parameter value matches the conditions defined by the relational operator. In the first example, the request returns all edited documents with a `doc_id` value equal to `12345`. In the second example, the report returns any edited documents where the `doc_id` value is not equal to `98765`. The `<>` operator is URL-encoded in the request's query string (`%3C%3E`):

```
GET...&eventName=edit&filters=doc_id==12345
GET...&eventName=edit&filters=doc_id%3C%3E98765
```

A `filters` query supports these relational operators:

- `==`—'equal to'.
- `<>`—'not equal to'. Must be URL-encoded (%3C%3E).
- `<`—'less than'. Must be URL-encoded (%3C).
- `<=`—'less than or equal to'. Must be URL-encoded (%3C=).
- `>`—'greater than'. Must be URL-encoded (%3E).
- `>=`—'greater than or equal to'. Must be URL-encoded (%3E=).

**Note:** The API doesn't accept multiple values of the same parameter. If a parameter is supplied more than once in the API request, the API only accepts the last value of that parameter. In addition, if an invalid parameter is supplied in the API request, the API ignores that parameter and returns the response corresponding to the remaining valid parameters. If no parameters are requested, all parameters are returned.

**maxResults**

`integer`

Determines how many activity records are shown on each response page. For example, if the request sets `maxResults=1` and the report has two activities, the report has two pages. The response's `nextPageToken` property has the token to the second page. The `maxResults` query string is optional in the request. The default value is 1000.

**orgUnitID**

`string`

ID of the [organizational unit](https://docs.cloud.google.com/admin-sdk/directory/v1/guides/manage-org-units) to report on. Activity records will be shown only for users who belong to the specified organizational unit. Data before Dec 17, 2018 doesn't appear in the filtered results.

**pageToken**

`string`

The token to specify next page. A report with multiple pages has a `nextPageToken` property in the response. In your follow-on request getting the next page of the report, enter the `nextPageToken` value in the `pageToken` query string.

**startTime**

`string`

Sets the beginning of the range of time shown in the report. The date is in the [RFC 3339 format](http://www.ietf.org/rfc/rfc3339.txt), for example 2010-10-28T10:26:35.000Z. The report returns all activities from `startTime` until `endTime`. The `startTime` must be before the `endTime` (if specified) and the current time when the request is made, or the API returns an error.

 For Gmail requests, `startTime` and `endTime` must be provided and the difference must not be greater than 30 days.

**groupIdFilter**

`string`

Comma separated group ids (obfuscated) on which user activities are filtered, i.e. the response will contain activities for only those users that are a part of at least one of the group ids mentioned here. Format: "id:abc123,id:xyz456" **Important:** To filter by groups, you must explicitly add the groups to your filtering groups allowlist. For more information about adding groups to filtering groups allowlist, see [Filter results by Google Group](https://support.google.com/a/answer/11482175)

**resourceDetailsFilter**

`string`

Optional. The `resourceDetailsFilter` query string is an AND separated list composed of [Resource Details](#resourcedetails) fields manipulated by relational operators.

Resource Details Filters are in the form `{resourceDetails.field1}{relational operator}{field1 value} AND
{resourceDetails.field2}{relational operator}{field2 value}...`

All the inner fields are traversed using the `.` operator, as shown in the following example:

```
resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id =
"appliedLabelId" AND resourceDetails.appliedLabels.fieldValue.id =
"fieldValueId"
```

`resourceDetailsFilter` query supports these relational operators:

- `=`—'equal to'.
- `!=`—'not equal to'.
- `:`—'exists'. This is used for filtering on repeated fields.

[`FieldValue`](#fieldvalue) types that are repeated in nature uses `exists` operator for filtering.
 The following [`FieldValue`](#fieldvalue) types are repeated:

For example, in the following filter, [`SelectionListValue`](#selectionlistvalue), is a repeated field. The filter checks whether [`SelectionListValue`](#selectionlistvalue) contains `selection_id`:

```
resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id =
"appliedLabelId" AND resourceDetails.appliedLabels.fieldValue.id =
"fieldValueId" AND resourceDetails.appliedLabels.fieldValue.type =
"SELECTION_LIST_VALUE" AND
resourceDetails.appliedLabels.fieldValue.selectionListValue.id: "id"
```

**Usage**

```
GET...&resourceDetailsFilter=resourceDetails.id = "resourceId" AND
resourceDetails.appliedLabels.id = "appliedLabelId"
GET...&resourceDetailsFilter=resourceDetails.id=%22resourceId%22%20AND%20resourceDetails.appliedLabels.id=%22appliedLabelId%22
```

**Note the following**:

- You must URL encode the query string before sending the request.
- The API supports a maximum of 5 fields separated by the AND operator.

- When filtering on deeper levels (e.g., [`AppliedLabel`](#appliedlabel), [`FieldValue`](#fieldvalue)), the IDs of all preceding levels in the hierarchy must be included in the filter. For example: Filtering on [`FieldValue`](#fieldvalue) requires [`AppliedLabel`](#appliedlabel) ID and resourceDetails ID to be present.
  **Sample Query**:

  `resourceDetails.id = "resourceId" AND resourceDetails.appliedLabels.id =
  "appliedLabelId" AND resourceDetails.appliedLabels.fieldValue.id =
  "fieldValueId"`

- Filtering on inner [`FieldValue`](#fieldvalue) types like `longTextValue` and `textValue` requires `resourceDetails.appliedLabels.fieldValue.type` to be present.
- Only Filtering on a single [`AppliedLabel`](#appliedlabel) id and [`FieldValue`](#fieldvalue) id is supported.

**networkInfoFilter**

`string`

Optional. Used to filter on the `regionCode` field present in [`NetworkInfo`](#networkinfo) message.

**Usage**

```
GET...&networkInfoFilter=regionCode="IN"
GET...&networkInfoFilter=regionCode=%22IN%22
```

**statusFilter**

`string`

Optional. Used to filter on the `statusCode` field present in [`Status`](#status) message.

**Usage**

```
GET...&statusFilter=statusCode="200"
GET...&statusFilter=statusCode=%22200%22
```

**applicationInfoFilter**

`string`

Optional. Used to filter on the `oAuthClientId` field present in [`ApplicationInfo`](#applicationinfo) message.

**Usage**

```
GET...&applicationInfoFilter=oAuthClientId="clientId"
GET...&applicationInfoFilter=oAuthClientId=%22clientId%22
```

**includeSensitiveData**

`boolean`

Optional. When set to `true`, this field allows sensitive user-generated content to be included in the returned audit logs. This parameter is supported only for Rules (DLP), Chat and Workspace Studio applications; using it with any other application will result in a permission error.

**agentInfoFilter**

`string`

Optional. Filters on agent info fields in the activity. This filter gets applied in conjunction(AND) with other filters. Example: "agentInfoFilter=agentId="agent-id" AND agentName="agent-name" AND agentOwnerEmail="agent-owner-email""

**deviceFilter**

`string`

Optional. Used to filter on the fields present in [`UserDeviceInfo`](#userdeviceinfo) message like `deviceId`, `deviceType`, and `deviceOsVersion`.

**Usage**

```
GET...&deviceFilter=deviceId="123"
GET...&deviceFilter=deviceType="ANDROID"
GET...&deviceFilter=deviceOsVersion="14.0"
```

### Request body

The request body must be empty.

### Response body

JSON template for a collection of activities.

If successful, the response body contains data with the following structure:

**JSON representation**

```
{
  "kind": string,
  "etag": string,
  "items": [
    {
      object (Activity)
    }
  ],
  "nextPageToken": string
}
```

| Fields | |
| --- | --- |
| `kind` | `string`  The type of API resource. For an activity report, the value is `reports#activities`. |
| `etag` | `string`  ETag of the resource. |
| `items[]` | `object (Activity)`  Each activity record in the response. |
| `nextPageToken` | `string`  Token for retrieving the follow-on next page of the report. The `nextPageToken` value is used in the request's `pageToken` query string. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/admin.reports.audit.readonly`

For more information, see the [Authorization guide](https://docs.cloud.google.com/workspace/guides/configure-oauth-consent).

## ApplicationName

| Enums | |
| --- | --- |
| `access_transparency` | The Google Workspace Access Transparency activity reports return information about different types of [Access Transparency activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/access-transparency). |
| `admin` | The Admin console application's activity reports return account information about different types of [administrator activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/admin-event-names). |
| `calendar` | The Google Calendar application's activity reports return information about various [Calendar activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/calendar-event-names). |
| `chat` | The Chat activity reports return information about various [Chat activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/chat). |
| `drive` | The Google Drive application's activity reports return information about various [Google Drive activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/drive-event-names). The Drive activity report is only available for Google Workspace Business and Enterprise customers. |
| `gcp` | The Google Cloud Platform application's activity reports return information about various [GCP activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/gcp). |
| `gmail` | The Gmail application's activity reports return information about various [Gmail activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/gmail). |
| `gplus` | The Google+ application's activity reports return information about various [Google+ activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/gplus). |
| `groups` | The Google Groups application's activity reports return information about various [Groups activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/groups-event-names). |
| `groups_enterprise` | The Enterprise Groups activity reports return information about various [Enterprise group activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/groups-enterprise). |
| `jamboard` | The Jamboard activity reports return information about various [Jamboard activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/jamboard). |
| `login` | The Login application's activity reports return account information about different types of [Login activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-/login-event-names). |
| `meet` | The Meet Audit activity report returns information about different types of [Meet Audit activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/meet). |
| `mobile` | The Device Audit activity report returns information about different types of [Device Audit activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/appendix/mobile). |
| `rules` | The Rules activity report returns information about different types of [Rules activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/rules). |
| `saml` | The SAML activity report returns information about different types of [SAML activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/saml). |
| `token` | The Token application's activity reports return account information about different types of [Token activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/reference/activity-ref-appendix-a/token-event-names). |
| `user_accounts` | The User Accounts application's activity reports return account information about different types of [User Accounts activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/user_accounts). |
| `context_aware_access` | The Context-aware access activity reports return information about users' access denied events due to  [Context-aware access rules](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/context-aware-access). |
| `chrome` | The Chrome activity reports return information about  [Chrome browser and Chrome OS events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/chrome). |
| `data_studio` | The Data Studio activity reports return information about various types of [Data Studio activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/data-studio). |
| `keep` | The Keep application's activity reports return information about various [Google Keep activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/keep). The Keep activity report is only available for Google Workspace Business and Enterprise customers. |
| `vault` | The Vault activity reports return information about various types of [Vault activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/vault). |
| `gemini_in_workspace_apps` | The Gemini for Workspace activity reports return information about various types of [Gemini activity events](https://docs.cloud.google.com/admin-sdk/reports/v1/appendix/activity/gemini-in-workspace-apps) performed by users within a Workspace application. |
| `classroom` | The Classroom activity reports return information about different types of [Classroom activity events](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/classroom). |
| `assignments` | The assignments application's activity reports return information about various types of assignments activity events. |
| `cloud_search` | The Cloud Search application's activity reports return information about various types of cloud\_search activity events. |
| `tasks` | The Tasks application's activity reports return information about various types of Tasks activity events. |
| `data_migration` | The Data Migration application's activity reports return information about various types of data migration activity events. |
| `meet_hardware` | The Meet Hardware application's activity reports return information about various types of Meet Hardware activity events. |
| `directory_sync` | The Directory Sync application's activity reports return information about various types of Directory Sync activity events. |
| `ldap` | The ldap application's activity reports return information about various types of ldap activity events. |
| `profile` | The Profile application's activity reports return information about various types of Profile activity events. |
| `access_evaluation` | The Access Evaluation activity reports return information about various types of Access Evaluation activity events. |
| `admin_data_action` | The Admin Data Action application's activity reports return information about various types of Admin Data Action activity events. |
| `contacts` | The Contacts application's activity reports return information about various types of Contacts activity events. |
| `takeout` | The Takeout application's activity reports return information about various types of Takeout activity events. |
| `graduation` | The Graduation application's activity reports return information about various types of Graduation activity events. |
| `voice` | The Voice application's activity reports return information about various types of Voice activity events. |
| `chrome_sync` | The Chrome Sync application's activity reports return information about various types of Chrome Sync activity events. |
| `workspace_studio` | The Workspace Studio application's activity reports return information about various types of Workspace Studio activity events. |
| `gemini_notebook` | The Gemini Notebook application's activity reports return information about various types of Gemini Notebook activity events. |

## Activity

JSON template for the activity resource.

**JSON representation**

```
{
  "kind": string,
  "etag": string,
  "ownerDomain": string,
  "ipAddress": string,
  "events": [
    {
      "type": string,
      "name": string,
      "parameters": [
        {
          "messageValue": {
            "parameter": [
              {
                object (NestedParameter)
              }
            ]
          },
          "name": string,
          "value": string,
          "multiValue": [
            string
          ],
          "intValue": string,
          "multiIntValue": [
            string
          ],
          "boolValue": boolean,
          "multiMessageValue": [
            {
              "parameter": [
                {
                  object (NestedParameter)
                }
              ]
            }
          ]
        }
      ],
      "sensitiveParameters": [
        {
          "messageValue": {
            "parameter": [
              {
                object (NestedParameter)
              }
            ]
          },
          "name": string,
          "value": string,
          "multiValue": [
            string
          ],
          "intValue": string,
          "multiIntValue": [
            string
          ],
          "boolValue": boolean,
          "multiMessageValue": [
            {
              "parameter": [
                {
                  object (NestedParameter)
                }
              ]
            }
          ]
        }
      ],
      "resourceIds": [
        string
      ],
      "status": {
        object (Status)
      }
    }
  ],
  "id": {
    "time": string,
    "uniqueQualifier": string,
    "applicationName": string,
    "customerId": string
  },
  "actor": {
    "profileId": string,
    "email": string,
    "callerType": string,
    "key": string,
    "applicationInfo": {
      "oauthClientId": string,
      "applicationName": string,
      "impersonation": boolean
    },
    "agentAttributionInfo": {
      object (AgentAttributionInfo)
    }
  },
  "networkInfo": {
    object (NetworkInfo)
  },
  "resourceDetails": [
    {
      object (ResourceDetails)
    }
  ],
  "isAgenticAction": boolean,
  "userDeviceInfo": {
    object (UserDeviceInfo)
  }
}
```

**Fields**

**kind**

`string`

The type of API resource. For an activity report, the value is `audit#activity`.

**etag**

`string`

ETag of the entry.

**ownerDomain**

`string`

This is the domain that is affected by the report's event. For example domain of Admin console or the Drive application's document owner.

**ipAddress**

`string`

IP address of the user doing the action. This is the Internet Protocol (IP) address of the user when logging into Google Workspace, which may or may not reflect the user's physical location. For example, the IP address can be the user's proxy server's address or a virtual private network (VPN) address. The API supports [IPv4](http://wikipedia.org/wiki/IPv4) and [IPv6](http://wikipedia.org/wiki/IPv6_address).

**events[]**

`object`

Activity events in the report.

**events[].type**

`string`

Type of event. The Google Workspace service or feature that an administrator changes is identified in the `type` property which identifies an event using the `eventName` property. For a full list of the API's `type` categories, see the list of event names for various applications above in `applicationName`.

**events[].name**

`string`

Name of the event. This is the specific name of the activity reported by the API. And each `eventName` is related to a specific Google Workspace service or feature which the API organizes into types of events.
For `eventName` request parameters in general:

- If no `eventName` is given, the report returns all possible instances of an `eventName`.
- When you request an `eventName`, the API's response returns all activities which contain that `eventName`.

For more information about `eventName` properties, see the list of event names for various applications above in `applicationName`.

**events[].parameters[]**

`object`

Parameter value pairs for various applications. For more information about `eventName` parameters, see the list of event names for various applications above in `applicationName`.

**events[].parameters[].messageValue**

`object`

Nested parameter value pairs associated with this parameter. Complex value type for a parameter are returned as a list of parameter values. For example, the address parameter may have a value as `[{parameter: [{name: city, value: abc}]}]`

**events[].parameters[].messageValue.parameter[]**

`object (NestedParameter)`

Parameter values

**events[].parameters[].name**

`string`

The name of the parameter.

**events[].parameters[].value**

`string`

String value of the parameter.

**events[].parameters[].multiValue[]**

`string`

String values of the parameter.

**events[].parameters[].intValue**

`string (int64 format)`

Integer value of the parameter.

**events[].parameters[].multiIntValue[]**

`string (int64 format)`

Integer values of the parameter.

**events[].parameters[].boolValue**

`boolean`

Boolean value of the parameter.

**events[].parameters[].multiMessageValue[]**

`object`

activities.list of `messageValue` objects.

**events[].parameters[].multiMessageValue[].parameter[]**

`object (NestedParameter)`

Parameter values

**events[].sensitiveParameters[]**

`object`

Includes sensitive parameter value pairs for various applications.

**events[].sensitiveParameters[].messageValue**

`object`

Nested parameter value pairs associated with this parameter. Complex value type for a parameter are returned as a list of parameter values. For example, the address parameter may have a value as `[{parameter: [{name: city, value: abc}]}]`

**events[].sensitiveParameters[].messageValue.parameter[]**

`object (NestedParameter)`

Parameter values

**events[].sensitiveParameters[].name**

`string`

The name of the parameter.

**events[].sensitiveParameters[].value**

`string`

String value of the parameter.

**events[].sensitiveParameters[].multiValue[]**

`string`

String values of the parameter.

**events[].sensitiveParameters[].intValue**

`string (int64 format)`

Integer value of the parameter.

**events[].sensitiveParameters[].multiIntValue[]**

`string (int64 format)`

Integer values of the parameter.

**events[].sensitiveParameters[].boolValue**

`boolean`

Boolean value of the parameter.

**events[].sensitiveParameters[].multiMessageValue[]**

`object`

activities.list of `messageValue` objects.

**events[].sensitiveParameters[].multiMessageValue[].parameter[]**

`object (NestedParameter)`

Parameter values

**events[].resourceIds[]**

`string`

Resource ids associated with the event.

**events[].status**

`object (Status)`

Status of the event. Note: Not all events have status.

**id**

`object`

Unique identifier for each activity record.

**id.time**

`string`

Time of occurrence of the activity. This is in UNIX epoch time in seconds.

**id.uniqueQualifier**

`string (int64 format)`

Unique qualifier if multiple events have the same time.

**id.applicationName**

`string`

Application name to which the event belongs. For possible values see the list of applications above in `applicationName`.

**id.customerId**

`string`

The unique identifier for a Google Workspace account.

**actor**

`object`

User doing the action.

**actor.profileId**

`string`

The unique Google Workspace profile ID of the actor. This value might be absent if the actor is not a Google Workspace user, or may be the number 105250506097979753968 which acts as a placeholder ID.

**actor.email**

`string`

The primary email address of the actor. May be absent if there is no email address associated with the actor.

**actor.callerType**

`string`

The type of actor.

**actor.key**

`string`

Only present when `callerType` is `KEY`. Can be the `consumer_key` of the requestor for OAuth 2LO API requests or an identifier for robot accounts.

**actor.applicationInfo**

`object`

Details of the application that was the actor for the activity.

**actor.applicationInfo.oauthClientId**

`string`

OAuth client id of the third party application used to perform the action.

**actor.applicationInfo.applicationName**

`string`

Name of the application used to perform the action.

**actor.applicationInfo.impersonation**

`boolean`

Whether the application was impersonating a user.

**actor.agentAttributionInfo**

`object (AgentAttributionInfo)`

Details of the AI agent that was the actor for the activity.

**networkInfo**

`object (NetworkInfo)`

Network information of the user doing the action.

**resourceDetails[]**

`object (ResourceDetails)`

Details of the resource on which the action was performed.

**isAgenticAction**

`boolean`

Whether the activity was performed by an agent.

**userDeviceInfo**

`object (UserDeviceInfo)`

Device details of the user doing the action. This field is only exposed for the `contacts`, `gemini_in_workspace_apps`, `keep`, `meet_hardware`, `meet`, `chat`, `chrome`, `directory_sync`, `drive`, `groups`, `rules`, `data_studio`, `saml` applications.

## NetworkInfo

Network information of the user doing the action.

**JSON representation**

```
{
  "ipAsn": [
    integer
  ],
  "regionCode": string,
  "subdivisionCode": string
}
```

| Fields | |
| --- | --- |
| `ipAsn[]` | `integer`  IP Address of the user doing the action. |
| `regionCode` | `string`  ISO 3166-1 alpha-2 region code of the user doing the action. |
| `subdivisionCode` | `string`  ISO 3166-2 region code (states and provinces) for countries of the user doing the action. |

## ResourceDetails

Details of the resource on which the action was performed.

**JSON representation**

```
{
  "id": string,
  "title": string,
  "type": string,
  "appliedLabels": [
    {
      object (AppliedLabel)
    }
  ],
  "relation": string,
  "ownerDetails": {
    object (OwnerDetails)
  }
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Identifier of the resource, such as a doc\_id for a Drive document, a conference\_id for a Meet conference, or a "gaia\_id/rfc2822\_message\_id" for an email. |
| `title` | `string`  Title of the resource. For instance, in case of a drive document, this would be the title of the document. In case of an email, this would be the subject. |
| `type` | `string`  Type of the resource - document, email, chat message |
| `appliedLabels[]` | `object (AppliedLabel)`  activities.list of labels applied on the resource |
| `relation` | `string`  Defines relationship of the resource to the events |
| `ownerDetails` | `object (OwnerDetails)`  Owner details of the resource. |

## AppliedLabel

Details of the label applied on the resource.

**JSON representation**

```
{
  "id": string,
  "title": string,
  "fieldValues": [
    {
      object (FieldValue)
    }
  ],
  "reason": {
    object (Reason)
  }
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Identifier of the label - Only the label id, not the full OnePlatform resource name. |
| `title` | `string`  Title of the label |
| `fieldValues[]` | `object (FieldValue)`  activities.list of fields which are part of the label and have been set by the user. If label has a field which was not set by the user, it would not be present in this list. |
| `reason` | `object (Reason)`  The reason why the label was applied on the resource. |

## FieldValue

Details of the field value set by the user for the particular label.

**JSON representation**

```
{
  "id": string,
  "displayName": string,
  "type": string,
  "reason": {
    object (Reason)
  },

  "unsetValue": boolean,
  "longTextValue": string,
  "textValue": string,
  "textListValue": {
    object (TextListValue)
  },
  "selectionValue": {
    object (SelectionValue)
  },
  "selectionListValue": {
    object (SelectionListValue)
  },
  "integerValue": string,
  "userValue": {
    object (UserValue)
  },
  "userListValue": {
    object (UserListValue)
  },
  "dateValue": {
    object (Date)
  }
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Identifier of the field |
| `displayName` | `string`  Display name of the field |
| `type` | `string`  Type of the field |
| `reason` | `object (Reason)`  The reason why the field was applied to the label. |
| Union field `value`. Stores the values stored in the field `value` can be only one of the following: | |
| `unsetValue` | `boolean`  If the field is unset, this will be true. |
| `longTextValue` | `string`  Setting a long text value. |
| `textValue` | `string`  Setting a text value. |
| `textListValue` | `object (TextListValue)`  Setting a text list value. |
| `selectionValue` | `object (SelectionValue)`  Setting a selection value by selecting a single value from a dropdown. |
| `selectionListValue` | `object (SelectionListValue)`  Setting a selection list value by selecting multiple values from a dropdown. |
| `integerValue` | `string (int64 format)`  Setting an integer value. |
| `userValue` | `object (UserValue)`  Setting a user value by selecting a single user. |
| `userListValue` | `object (UserListValue)`  Setting a user list value by selecting multiple users. |
| `dateValue` | `object (Date)`  Setting a date value. |

## TextListValue

Setting a text list value.

**JSON representation**

```
{
  "values": [
    string
  ]
}
```

| Fields | |
| --- | --- |
| `values[]` | `string`  activities.list of text values. |

## SelectionValue

Setting a selection value by selecting a single value from a dropdown.

**JSON representation**

```
{
  "id": string,
  "displayName": string,
  "badged": boolean
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Identifier of the selection. |
| `displayName` | `string`  Display name of the selection. |
| `badged` | `boolean`  Whether the selection is badged. |

## SelectionListValue

Setting a selection list value by selecting multiple values from a dropdown.

**JSON representation**

```
{
  "values": [
    {
      object (SelectionValue)
    }
  ]
}
```

| Fields | |
| --- | --- |
| `values[]` | `object (SelectionValue)`  activities.list of selections. |

## UserValue

Setting a user value by selecting a single user.

**JSON representation**

```
{
  "email": string
}
```

| Fields | |
| --- | --- |
| `email` | `string`  Email of the user. |

## UserListValue

Setting a user list value by selecting multiple users.

**JSON representation**

```
{
  "values": [
    {
      object (UserValue)
    }
  ]
}
```

| Fields | |
| --- | --- |
| `values[]` | `object (UserValue)`  activities.list of users. |

## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

- A full date, with non-zero year, month, and day values.
- A month and day, with a zero year (for example, an anniversary).
- A year on its own, with a zero month and a zero day.
- A year and month, with a zero day (for example, a credit card expiration date).

Related types:

- `google.type.TimeOfDay`
- `google.type.DateTime`
- `google.protobuf.Timestamp`

**JSON representation**

```
{
  "year": integer,
  "month": integer,
  "day": integer
}
```

| Fields | |
| --- | --- |
| `year` | `integer`  Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. |
| `month` | `integer`  Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. |
| `day` | `integer`  Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant. |

## Reason

The reason why the label/field was applied.

**JSON representation**

```
{
  "reasonType": string
}
```

| Fields | |
| --- | --- |
| `reasonType` | `string`  The type of the reason. |

## OwnerDetails

Details of the owner of the resource.

**JSON representation**

```
{
  "ownerType": string,
  "ownerIdentity": [
    {
      object (OwnerIdentity)
    }
  ]
}
```

| Fields | |
| --- | --- |
| `ownerType` | `string`  Type of the owner of the resource. |
| `ownerIdentity[]` | `object (OwnerIdentity)`  Identity details of the owner(s) of the resource. |

## OwnerIdentity

Identity details of the owner of the resource.

**JSON representation**

```
{

  "customerIdentity": {
    object (CustomerIdentity)
  },
  "userIdentity": {
    object (UserIdentity)
  },
  "groupIdentity": {
    object (GroupIdentity)
  },
  "sharedDriveIdentity": {
    object (SharedDriveIdentity)
  }
}
```

| Fields | |
| --- | --- |
| Union field `identity`. This is a oneof field and only one of the following fields can be set. `identity` can be only one of the following: | |
| `customerIdentity` | `object (CustomerIdentity)`  Identity of the Google Workspace customer who owns the resource. |
| `userIdentity` | `object (UserIdentity)`  Identity of the user who owns the resource. |
| `groupIdentity` | `object (GroupIdentity)`  Identity of the group who owns the resource. |
| `sharedDriveIdentity` | `object (SharedDriveIdentity)`  Identity of the shared drive who owns the resource. |

## CustomerIdentity

Identity of the Google Workspace customer who owns the resource.

**JSON representation**

```
{
  "id": string
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Customer id. |

## UserIdentity

Identity of the user who owns the resource.

**JSON representation**

```
{
  "id": string,
  "userEmail": string
}
```

| Fields | |
| --- | --- |
| `id` | `string`  User gaia id. |
| `userEmail` | `string`  User email. |

## GroupIdentity

Identity of the group who owns the resource.

**JSON representation**

```
{
  "id": string,
  "groupEmail": string
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Group gaia id. |
| `groupEmail` | `string`  Group email. |

## SharedDriveIdentity

Identity of the shared drive who owns the resource.

**JSON representation**

```
{
  "id": string,
  "sharedDriveName": string
}
```

| Fields | |
| --- | --- |
| `id` | `string`  Shared drive gaia id. |
| `sharedDriveName` | `string`  Shared drive name. |

## UserDeviceInfo

Device details of the user doing the action.

**JSON representation**

```
{
  "deviceId": string,
  "deviceType": string,
  "deviceOsVersion": string
}
```

| Fields | |
| --- | --- |
| `deviceId` | `string`  Output only. Device ID of the user's device. |
| `deviceType` | `string`  Output only. The type of the user's device. |
| `deviceOsVersion` | `string`  Output only. Device OS version of the user's device. |
