# Gemini Enterprise Docs (User events) / About user events
Source: https://docs.cloud.google.com/gemini/enterprise/docs/user-events, page last updated 2026-10-14, extracted 2026-10-19

This page describes user events for Gemini Enterprise apps, including
user event types, requirements, and examples for user event types.

If you use the Gemini Enterprise APIs in your own apps, you need to
configure search in your app to get the user events and then add the user
events data to your Gemini Enterprise app.

If you [create your app through the
Google Cloud console](https://docs.cloud.google.com/gemini/enterprise/docs/create-app), then
you don't need to manually import user events (and you don't need to read
this page).

For help with recording user events, see
[Record real-time user events](https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events). To import past
user events in bulk, see [Import historical user events](https://docs.cloud.google.com/gemini/enterprise/docs/import-user-events).

## User event types

You can record the following types of user events as end users browse or search
your site:

| User event name | User action |
| --- | --- |
| [`view-item`](#view-item) | Views details of a document. |
| [`search`](#search) | Searches data in the Gemini Enterprise app. |

For details about the user event object, see the
[`UserEvent` API reference documentation][user-event].

## User event type examples and schemas

This section provides the data formats for each event type supported by
Gemini Enterprise apps.
Examples for JavaScript Pixel are provided. For
BigQuery, the full table schema for each type is provided.

For all user events types, `userId` is optional.

For more details about the user event object, see the
[`UserEvent` API reference documentation][user-event].

### view-item

The following shows the `view-item` user event data format.

#### Search optimization requirements for view-item events

To let search automatically optimize the search experience based
on overall user trends, upload the following data.

Events should be uploaded at least daily with a maximum delay of 24 hours.

| Events metric | Events volume/frequency | Description |
| --- | --- | --- |
| Volume of `view-item` events | 250k view items | At least 250,000 view items are **required** to optimize the search experience based on events ingested. |

#### Minimum required view-item object

The following examples show only the required fields of the `view-item`
user event format.

The
[`documents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo)
object contains the document's ID
([`id`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource
name ([`name`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)).

- When you ingest or record user events at a data-store level, you can provide
  the document's ID (`id`) or resource name (`name`).
- When you ingest or record events at a location level, you must supply the
  document's resource name (`name`) because it indicates a document's full path
  and refers to the data store where the document resides. You can provide the
  document's ID as an optional, additional information.

### JavaScript Pixel

```
var user_event = {
  "eventType": "view-item",
  "userPseudoId": "USER_PSEUDO_ID",
  "engine": "APP_ID",
  "eventTime": "2020-01-01T03:33:33.000001Z",
  "documents": [{
    "name": "DOCUMENT_NAME"
  }]
};
```

### BigQuery

This is the complete JSON schema for this user event type. Specify this schema
when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for
optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with
BigQuery. `eventTime` is a string with a Timestamp format.

```
[
  {
    "name": "eventType",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "userPseudoId",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "engine",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "eventTime",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "userInfo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "userId",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "userAgent",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "pageInfo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "pageviewId",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "uri",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "referrerUri",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "attributionToken",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "documents",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "tagIds",
    "type": "STRING",
    "mode": "REPEATED"
  },
  {
    "name": "attributes",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "example_text_attribute",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "text",
            "type": "STRING",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "example_number_attribute",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "numbers",
            "type": "NUMERIC",
            "mode": "REPEATED"
          }
        ]
      }
    ]
  }
]
```

#### Complete view-item object example

The following examples include both required and optional fields for the
`view-item` user event.

### JavaScript Pixel

```
var user_event = {
  eventType: "view-item",
  userPseudoId: "visitor0",
  "engine": "APP_ID",
  eventTime: "2020-01-01T03:33:33.000001Z",
  userInfo: {
    userId: "abc@example.com",
    userAgent: "Mozilla/5.0",
  },
  pageInfo: {
    pageViewId: "currentPageUri",
    uri: "http://example",
    referrerUri: "https://google",
  },
  attributionToken: "abcd",
  documents: [
    {
      id: "abcd",
    },
  ],
  tagIds: ["Treatment_B"],
  attributes: {
    example_text_attribute: {
      text: ["text_1", "text_2"],
    },
    example_number_attribute: {
      numbers: [3.14, 42, 1.2345],
    },
  },
  panels: [
         {
           panelId: "HOME_RFY_1",
           documents: [
             {
               id: "123"
             },
             {
               id: "456"
             }
           ],
           panelPosition: 1,
           totalPanels: 2
         }
      ]
};
```

### BigQuery

This is the complete JSON schema for this user event type. Specify this schema
when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for
optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with
BigQuery. `eventTime` is a string with a Timestamp format.

```
[
  {
    "name": "eventType",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "userPseudoId",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "engine",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "eventTime",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "userInfo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "userId",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "userAgent",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "pageInfo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "pageviewId",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "uri",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "referrerUri",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "attributionToken",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "documents",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "tagIds",
    "type": "STRING",
    "mode": "REPEATED"
  },
  {
    "name": "attributes",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "example_text_attribute",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "text",
            "type": "STRING",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "example_number_attribute",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "numbers",
            "type": "NUMERIC",
            "mode": "REPEATED"
          }
        ]
      }
    ]
  }
]
```

### search

The following shows the `search` user event format.

#### Search optimization requirements for search events

To let search automatically optimize the search experience based on overall user trends, upload the following data.

Events should be uploaded at least daily with a maximum delay of 24 hours.

| Events metric | Events volume/frequency | Description |
| --- | --- | --- |
| Volume of `search` events | 100k searches | At least 100,000 searches are **required** to optimize the search experience based on events ingested. |

#### Minimum required search object

The following examples show only the required fields of the `search` user event
format.

Provide `searchQuery` for search events where the user entered a text query.

The `attributionToken` is returned with the search query results.

The
[`documents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo)
object contains the document's ID
([`id`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource
name ([`name`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)).

- When you ingest or record user events at a data-store level, you can provide
  the document's ID (`id`) or resource name (`name`).
- When you ingest or record events at a location level, you must supply the
  document's resource name (`name`) because it indicates a document's full path
  and refers to the data store where the document resides. You can provide the
  document's ID as an optional, additional information.

### JavaScript Pixel

```
var user_event = {
  "eventType": "search",
  "userPseudoId": "USER_PSEUDO_ID",
  "engine": "APP_ID",
  "eventTime": "2020-01-01T03:33:33.000001Z",
  "searchInfo": {
    "searchQuery": "SEARCH_QUERY",
  },
  "attributionToken": "ATTRIBUTION_TOKEN",
  "documents": [
    {
      "name": "DOCUMENT_NAME_1",
    },
    {
      "name": "DOCUMENT_NAME_2",
    },
  ]
};
```

### BigQuery

This is the complete JSON schema for this user event type. Specify this schema
when creating tables for this user event type in BigQuery.

Modes for required fields are set to `REQUIRED` or `REPEATED`. Modes for
optional fields are set to `NULLABLE`.

Note that `eventTime` is required for importing events with
BigQuery. `eventTime` is a string with a Timestamp format.

```
[
  {
    "name": "eventType",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "userPseudoId",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "engine",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "eventTime",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "searchInfo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "searchQuery",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "pageInfo",
    "type": "RECORD",
    "mode": "NULLABLE",
    "fields": [
      {
        "name": "pageCategory",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "name": "attributionToken",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "documents",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "name": "id",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  }
]
```

## About user information

`userPseudoId` represents the unique user identifier and is required when you
record a user event.

The user information ([`UserInfo`][user-info]) included when you record a user
event contains the `userPseudoId` value and, if available, the `userId` value.
`userId` is optional and can be used as a unique, persistent identifier for a
user across devices whenever a user logs in to your site. When you record the
`userId` for a user,
Gemini Enterprise apps
can generate more personalized results for one user across multiple devices,
such as both a mobile device and a web browser.

**Note:** Use a secure form of a unique identifier to keep users anonymous to
Gemini Enterprise and protect your users' privacy. You are responsible
for redacting PII (personally identifiable information), such as email or home
addresses, from your data.

## About the timestamp

When you record a user event, be sure to include an accurate timestamp of when
the event occurred. Accurate timestamps make sure that your events are stored in
the correct order. Timestamps are recorded automatically for events collected
using the JavaScript Pixel. When you import events, you must provide the
timestamp in the [`eventTime`][event-time] field in the format specified by [RFC
3339](https://tools.ietf.org/html/rfc3339).

[rec-type-reqs]: /gemini/enterprise/docs/about-media-recommendations-types
[record-events]: /gemini/enterprise/docs/record-user-events
[event-time]: /gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.event\_time
[user-event]: /gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents
[user-info]: /gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#userinfo
