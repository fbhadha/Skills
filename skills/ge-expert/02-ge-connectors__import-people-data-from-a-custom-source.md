# Gemini Enterprise: connectors and data stores / Import people data from a custom source to Connect to Data Cloud
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 122-162, extracted 2026-10-18

Contains:
- Import people data from a custom source (pages 122-141) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people-custom
- Enable Gemini Notebook Enterprise as a search source (pages 142-143) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-notebooklm
- Import from Firestore (pages 144-146) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-firestore
- Import from Bigtable (pages 147-151) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigtable
- Connect to data from AlloyDB for PostgreSQL (pages 152-156) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb-data
- Connect to Data Cloud (pages 157-162) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud

## Import people data from a custom source

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people-custom

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the GCP Service Specifc Terms i (https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the Generative AI Preview terms and conditions 

(https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the Cloud Data Processing Addendum 

(https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

Instead of syncing people data from Google Workspace 

(/gemini/enterprise/docs/connectors/connect-people), you can import people data from Cloud Storage or BigQuery. This page describes how to create a people search connector and import custom data about people from a Cloud Storage bucket or a BigQuery table. 

### Before you begin

- You must have your people data in a BigQuery table or a Cloud Storage bucket. 

- You must have your data in a Google-specified schema. For details about the schema, see Google-specified schema for people data (#fields). 

### Ingest people data from a custom source

To use the Google Cloud console to ingest people data, follow these steps: 

l 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

_Create a new data store._ 

4. On the **Select a data source** page, in the **Cloud sources** section, select **People via Custom Connector** . 

_Select a data source._ 

5. Import the people data: 

   - **Import later** : If you haven't imported your people data to Cloud SQL or BigQuery yet, select **Import later** . 

   - **BigQuery** : Import the data from a BigQuery table. 

   - **Cloud Storage** : Import the data from a Cloud Storage table. 

_Import people data._ 

6. Click **Continue** . 

7. Choose a region for your data store. 

8. Enter a name for your data store. 

9. Optional: If the data needs to be access controlled, select **This data store contains access control information** . For more information, see Data source access control (/gemini/enterprise/docs/identity). 

10. Click **Create** . 

_Configure the data connector._ 

11. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete. 

Depending on the size of your data, ingestion can take several minutes or several hours. 

**Note:** After you configure a people data source for your app, Google strongly recommends that you enable Knowledge Graph to significantly enhance search quality 

for your users. For more information, see Knowledge Graph: Powering intelligent and context-aware search (/gemini/enterprise/docs/use-knowledge-graph-search). 

### Customize search results

To include or exclude personal information from the search results, follow these steps: 

1. In your data store, click the **Entity** tab, and click **Users** . 

2. In the **Users** page, click the **Schema** tab. 

3. Click **Edit** . 

4. Select or clear the attributes, such as country, to specify whether they're retrievable, searchable, and indexable. To be searchable, the attribute must be marked **Retrievable** , **Indexable** , and **Searchable** . 

5. Click **Save** . 

**Note:** After you save your changes, the **Edit** button remains inactive for a few minutes before reactivating. 

### Preview people search results

1. If you have already connected the data store to an app, click **Apps** , and click the name of your app. 

**Note:** If you haven't connected your data store to an app yet, follow the steps in Create an app (/gemini/enterprise/docs/create-app) to create an app and select your data store. 

2. Click **Preview** . 

3. Search for people in your organization using the search bar. The search results show details such as name, job title, email, and profile picture. 

To open your Gemini Enterprise web app in a browser, see View the search web app 

(/gemini/enterprise/docs/quickstart-gemini-enterprise#view_the_search_web_app). 

_Preview the search results._ 

If you have made custom attributes searchable, then you can use the attributes in searches, but the attributes themselves aren't returned in profiles. For example, if `team-position` is a custom attribute and marked retrievable, indexable, and searchable in the schema, then you can search for people with a specific team position, such as "tech lead". You get a list of people who have that position, but the output won't include the words "tech lead". 

### View the search web app

To view your Gemini Enterprise web app, do the following: 

1. In the navigation menu, click **Integration** . 

2. Make sure that **Enable the Web App** is enabled. 

3. In the **The link to your web app** section, click **Copy** and open the link in your browser. 

### Example Organization-defined schema fields for people data

The data set for each person must be formatted according to the following schema. In the example of a file imported from Cloud Storage, each line of the JSONL file represents a person. A valid but minimal file might look as follows: 

```
{"id":"01","structData":{"personId":"01","name":
{"familyName":"Doe","givenName":"Jane"},"email":
{"type":"work","value":"jdoe@example.com"}}}
{"id":"02","structData":{"personId":"02","name":
{"familyName":"Kumar","givenName":"Ashok"},"email":
{"type":"home","value":"akumar@example.net"}}}
```

**Note:** You can add your own custom fields to the schema, but this might require setting one or more of the standard fields as not retrievable (the number of fields in a people schema is limited to 600). 

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearc|hableDescription|
|---|---|---|---|---|---|---|
|`personId`|string|N|Y|Y|Y|The person’s u<br>ID. Required fie<br>value of the`pe`<br>field must be t<br>same as the`id`<br>document.|
|`name.familyName`|string|N|Y|Y|Y|The person’s fa<br>name/last nam|
|`name.givenName`|string|N|Y|Y|Y|The person’s g<br>name/first nam|
|`name.displayName`|string|N|Y|Y|Y|The person’s d<br>name.|

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearc|hableDescription|
|---|---|---|---|---|---|---|
|`name.username`|string|N|Y|Y|Y|The person’s<br>username.|
|`emails.type`|string|Y|N|N|N|The type of the<br>account, such<br>"work", "home<br>"other", or "cus|
|`emails.value`|string|Y|Y|Y|Y|The person's e<br>address, such<br>"acruz@examp|
|`phoneNumbers.type`|string|Y|Y|Y|Y|The type of the<br>number, such a<br>"office", "mobi<br>"other".|
|`phoneNumbers.value`|string|Y|Y|Y|Y|The person's p<br>number, such a<br>800-555-1212"|
|`suspended`|boolean|N|N|N|N|Whether the pe<br>suspended wit<br>organization.|
|`employeeId`|string|N|Y|Y|Y|The person’s<br>employee ID.|
|`employeeType`|string|N|Y|Y|Y|The person’s<br>employee type<br>as "FTE", "Inte<br>"Temp".|
|`employmentStatus`|string|N|N|N|N|The person’s<br>employment st|
|`availabilityStatus`|string|N|N|N|N|The person’s<br>availability sta<br>such as "OOO"<br>"WFH", or "In<br>Meeting".|

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearc|hableDescription|
|---|---|---|---|---|---|---|
|`creationDate`|datetim|eN|N|N|N|The person’s c<br>date in the sou<br>system.|
|`modifiedDate`|datetim|eN|N|N|N|The person’s la<br>modified date<br>source system|
|`deletionDate`|datetim|eN|N|N|N|The person’s d<br>date in the sou<br>system.|
|`hireDate`|datetim|eN|Y|Y|N|The date when<br>person was hir|
|`gender.addressMeAs`|string|N|Y|Y|Y|The person’s<br>preferred pron<br>choice, such as<br>"he/him", "she/<br>or "they/them"|
|`gender.type`|string|N|Y|Y|Y|The person’s g<br>such as "male"<br>"female", or "o|
|`displayPhoto.url`|string|N|Y|Y|Y|The URL of the|
|`displayPhoto.image`<br>`Binary`|string|N|Y|Y|Y|The Base64 en<br>string of the im<br>binary of the p|
|`displayPhoto.format`|string|N|Y|Y|Y|The format of t<br>image binary,<br>“png”.|
|`addresses.country`|string|Y|Y|Y|Y|The country of<br>associated add<br>such as "Unite<br>States".|

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearch|ableDescription|
|---|---|---|---|---|---|---|
|`addresses.countryCode`|string|Y|N|N|N|The country co<br>the associated<br>address, such<br>"US".|
|`addresses.locality`|string|Y|Y|Y|Y|The locality of<br>associated add<br>such as "Moun<br>View".|
|`addresses.poBox`|string|Y|N|N|N|The PO Box of<br>associated add<br>such as "PO Bo|
|`addresses.postalCode`|string|Y|N|N|N|The postal cod<br>associated add<br>such as "94045|
|`addresses.region`|string|Y|N|N|N|The region of t<br>associated add<br>such as "CA".|
|`addresses.streetAddress`|string|Y|Y|Y|Y|The associated<br>address, such<br>"1800 Amphibi<br>Blvd.”.|
|`addresses.type`|string|Y|N|N|N|The type of the<br>associated add<br>such as "home<br>"work", or "oth|
|`location.value`|string|N|Y|Y|Y|The person's o<br>location, such<br>"London".|
|`location.buildingId`|string|N|Y|Y|Y|The building ID<br>person's office<br>location, such<br>"London".|

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearc|hableDescription|
|---|---|---|---|---|---|---|
|`location.deskCode`|string|N|Y|Y|Y|The desk code<br>person's office<br>location, such<br>"5C1C".|
|`location.floorName`|string|N|Y|Y|Y|The floor name<br>person's office<br>location, such<br>"Floor 5".|
|`location.floorSection`|string|N|Y|Y|Y|The floor sectio<br>the location, su<br>"Section C".|
|`location.type`|string|N|N|N|N|The type of the<br>location, such<br>"desk", or "bui|
|`organizations.`<br>`department`|string|Y|Y|Y|Y|The departmen<br>the organizatio<br>as "Engineerin|
|`organizations.`<br>`description`|string|Y|N|N|N|The description<br>organization.|
|`organizations.jobTitle`|string|Y|Y|Y|Y|The person’s jo<br>such as "Softw<br>Engineer".|
|`organizations.location`|string|Y|Y|Y|Y|The location of<br>organization, s<br>"London".|
|`organizations`<br>`.`<br>`name`<br>(http://organizations.name/|)<br>string|Y|Y|Y|Y|The name of th<br>organization.|
|`organizations.symbol`|string|Y|N|N|N|The ticker sym<br>the organizatio|
|`organizations.cost`<br>`Center`|string|Y|Y|Y|Y|The cost cente<br>organization, s<br>"75B".|

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearc|hableDescription|
|---|---|---|---|---|---|---|
|`organizations.type`|string|Y|N|N|N|The type of the<br>organization, s<br>"work" or "othe|
|`organizations`<br>`.`<br>`projects`<br>`.`<br>`name` (http://projects.name/)|string|Y|Y|Y|Y|The name of th<br>person's assign<br>project, such a<br>Ops".|
|`organizations.projects.`<br>`description`|string|Y|N|N|N|The description<br>person's assign<br>project, such a<br>world's best M|
|`organizations.projects.`<br>`role`|string|Y|N|N|N|The role of the<br>in the project,<br>"Lead".|
|`managers.personId`|string|Y|Y|Y|Y|The personId o<br>person’s curren<br>management c<br>starting from<br>immediate ma<br>to the highest<br>manager.|
|`managers.email`|string|Y|Y|Y|Y|The email addr<br>each manager<br>person’s curren<br>management c<br>starting at imm<br>manager and e<br>at the highest<br>manager.|
|`dottedLineReports.`<br>`personId`|string|Y|N|N|N|The person's d<br>line report(s)<br>(`personId`).|
|`dottedLineReports.email`|string|Y|N|N|N|The person's d<br>line reports (`em`|

|Field Name|Type|Repea|tableIndex|ableRetrie|vableSearch|ableDescription|
|---|---|---|---|---|---|---|
|`topCoworkers.personId`|string|Y|N|N|N|The person’s<br>coworker(s)<br>(`personId`).|
|`topCoworkers.affinity`<br>`Score`|number|Y|N|N|N|The person’s a<br>score relative t<br>coworkers (use<br>ranking).|
|`admins.personId`|string|Y|N|N|N|Person's assign<br>admin(s) (`pers`|
|`admins.email`|string|Y|N|N|N|Person's assign<br>admins (`email`|
|`websites.type`|string|Y|N|N|N|Person's websi<br>such as "work"<br>"blog", or "othe|
|`websites.value`|string|Y|N|N|N|The type of the<br>website, such a<br>"https://examp<br>store.com".|
|`directManager.personId`|string|N|Y|Y|Y|The personId o<br>person’s<br>direct/immedia<br>manager.|

#### Example payload for BigQuery

```
INSERT INTO `playground-koyel.ibank_ccai_uat.people_connector_3` (id,
structData)
WITH records_to_insert AS (
 SELECT [
   -- Record 1: jdoe
   STRUCT('jdoe' as id, STRUCT(
       "jdoe" AS personId,
       STRUCT("Doe","Jane","Jane Doe","jdoe") AS name,
       [STRUCT("work","jdoe@example.net")] AS emails,
       [STRUCT("personal","9131568042")] AS phoneNumbers,
       false AS suspended,
       "13" AS employeeId,
       CAST(NULL AS STRING) as employeeType,
       CAST(NULL AS STRING) as employmentStatus,
       "focus" AS availabilityStatus,
       CAST(NULL AS DATETIME) AS creationDate,
       CAST(NULL AS DATETIME) AS modifiedDate,
       CAST(NULL AS DATETIME) AS deletionDate,
       CAST(NULL AS DATETIME) AS hireDate,
       STRUCT("Male","Male") AS gender,
       STRUCT(CAST(NULL AS STRING) AS url, CAST(NULL AS STRING) AS
imageBinary, "png" as format) AS displayPhoto,
       [STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))] AS
addresses,
       STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL
AS STRING),CAST(NULL AS STRING)) AS location,
       [STRUCT("Engineering","Our mission is to help organizations be more
productive by making contextually relevant information and collaborators
accessible at the right time","Software Engineer","Bangalore","Intranet
search",CAST(NULL AS STRING),"80997GX000",CAST(NULL AS STRING),[STRUCT("People
Search",CAST(NULL AS STRING),"Individual Contributor")])] AS organizations,
       [STRUCT("dwilson",CAST(NULL AS STRING)),STRUCT("smiller",CAST(NULL AS
STRING)),STRUCT("jmartinez",CAST(NULL AS STRING))] AS managers,
       CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>) AS
dottedLineReports,
       CAST(NULL AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>) AS
topCoworkers,
       CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>) AS admins,
       [STRUCT("personal","https://jdoe.myownpersonaldomain.com")] AS
websites,
       STRUCT("dwilson") AS directManager
   ) AS structData),
   -- Record 2: psmith
   STRUCT('psmith' as id, STRUCT(
       "psmith",
       STRUCT("Smith","Peter","Peter Smith","psmith"),
       [STRUCT("work","psmith@example.net")],
       [STRUCT("personal","abc")],
       false, "1249989", CAST(NULL AS STRING), CAST(NULL AS STRING), "focus",
CAST(NULL AS DATETIME), CAST(NULL AS DATETIME), CAST(NULL AS DATETIME),
CAST(NULL AS DATETIME),
       STRUCT("Male","Male"),
       CAST(NULL AS STRUCT<url STRING, imageBinary STRING, format STRING>),
       [STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
       STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL
AS STRING),CAST(NULL AS STRING)),
       [STRUCT("Engineering","Our mission is to help organizations be more
productive by making contextually relevant information and collaborators
accessible at the right time","Software Engineer","Bangalore","Intranet
search",CAST(NULL AS STRING),"80997GX000",CAST(NULL AS STRING),
[STRUCT("ACL",CAST(NULL AS STRING),"Individual Contributor")])],
       [STRUCT("dwilson",CAST(NULL AS STRING)),STRUCT("smiller",CAST(NULL AS
STRING)),STRUCT("jmartinez",CAST(NULL AS STRING))],
       CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>), CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>), CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),
       CAST(NULL AS ARRAY<STRUCT<type STRING, value STRING>>),
       STRUCT("dwilson")
   ) AS structData),
   -- Record 3: mgarcia
   STRUCT('mgarcia' as id, STRUCT(
       "mgarcia",
       STRUCT("Garcia","Maria","Maria Garcia","mgarcia"),
       [STRUCT("work","mgarcia@example.net")],
       [STRUCT("personal","abc")],
       false, "1204052", CAST(NULL AS STRING), CAST(NULL AS STRING), "focus",
CAST(NULL AS DATETIME), CAST(NULL AS DATETIME), CAST(NULL AS DATETIME),
CAST(NULL AS DATETIME),
       STRUCT("Female","Female"),
       CAST(NULL AS STRUCT<url STRING, imageBinary STRING, format STRING>),
       [STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
       STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL
AS STRING),CAST(NULL AS STRING)),
       [STRUCT("Engineering","Our mission is to help organizations be more
productive by making contextually relevant information and collaborators
accessible at the right time","Software Engineer","Bangalore","Intranet
search",CAST(NULL AS STRING),"80997GX000",CAST(NULL AS STRING),[STRUCT("People
Search",CAST(NULL AS STRING),"Individual Contributor")]),
STRUCT("gBadminton","To organize our team's badminton community and make the
sport accessible to all.","Organizer","Bangalore","OneBlr",CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
ARRAY<STRUCT<name STRING, description STRING, role STRING>>))],
       [STRUCT("dwilson",CAST(NULL AS STRING)),STRUCT("smiller",CAST(NULL AS
STRING)),STRUCT("jmartinez",CAST(NULL AS STRING))],
       CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>), CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>), CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),
       [STRUCT("personal","https://mgarcia.myownpersonaldomain.com")],
       STRUCT("dwilson")
   ) AS structData),
   -- Other records follow the same pattern...
   STRUCT('dwilson' as id, STRUCT("dwilson", STRUCT("Wilson","David","David
Wilson","dwilson"),[STRUCT("work","dwilson@example.net")],
[STRUCT("personal","abc")],false,"14",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>),
[STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL AS
STRING),CAST(NULL AS STRING)),[STRUCT("Engineering","Our mission is to help
organizations be more productive by making contextually relevant information
and collaborators accessible at the right time","Engineering
Manager","Bangalore","Intranet search",CAST(NULL AS
STRING),"80997GX000",CAST(NULL AS STRING),[STRUCT("Connectors",CAST(NULL AS
STRING),"Engineering Manager")])],[STRUCT("smiller",CAST(NULL AS
STRING)),STRUCT("jmartinez",CAST(NULL AS STRING))],CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),STRUCT("smiller")) AS structData),
   STRUCT('ejohnson' as id, STRUCT("ejohnson", STRUCT("Johnson","Emily","Emily
Johnson","ejohnson"),[STRUCT("work","ejohnson@example.net")],
[STRUCT("personal","abc")],false,"652365",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>),
[STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL AS
STRING),CAST(NULL AS STRING)),[STRUCT("Engineering","Our mission is to help
organizations be more productive by making contextually relevant information
and collaborators accessible at the right time","Senior Software
Engineer","Bangalore","Intranet search",CAST(NULL AS
STRING),"80997GX000",CAST(NULL AS STRING),[STRUCT("BAP Connector
Integration",CAST(NULL AS STRING),"Team Lead")])],[STRUCT("smiller",CAST(NULL
AS STRING)),STRUCT("jmartinez",CAST(NULL AS STRING))],CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),STRUCT("smiller")) AS structData),
   STRUCT('mbrown' as id, STRUCT("mbrown", STRUCT("Brown","Michael","Michael
Brown","mbrown"),[STRUCT("work","mbrown@example.net")],
[STRUCT("personal","abc")],false,"1007126",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Female","Female"),CAST(NULL AS
STRUCT<url STRING, imageBinary STRING, format STRING>),
[STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL AS
STRING),CAST(NULL AS STRING)),[STRUCT("Engineering","Our mission is to help
organizations be more productive by making contextually relevant information
and collaborators accessible at the right time","Software
Engineer","Bangalore","Intranet search",CAST(NULL AS
STRING),"80997GX000",CAST(NULL AS STRING),[STRUCT("BAP Connector
Integration",CAST(NULL AS STRING),"Individual Contributor")])],
[STRUCT("smiller",CAST(NULL AS STRING)),STRUCT("jmartinez",CAST(NULL AS
STRING))],CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),STRUCT("smiller")) AS structData),
   STRUCT('smiller' as id, STRUCT("smiller", STRUCT("Miller","Sarah","Sarah
Miller","smiller"),[STRUCT("work","smiller@example.net")],
[STRUCT("personal","abc")],false,"15",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>),
[STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),"7",CAST(NULL AS
STRING),CAST(NULL AS STRING)),[STRUCT("Engineering","Our mission is to help
organizations be more productive by making contextually relevant information
and collaborators accessible at the right time","Senior Engineering
Manager","Bangalore","Intranet search",CAST(NULL AS
STRING),"80997GX000",CAST(NULL AS STRING),[STRUCT("Intranet Search",CAST(NULL
AS STRING),"Senior Engineering Manager")])],[STRUCT("jmartinez",CAST(NULL AS
STRING))],CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),STRUCT("jmartinez")) AS structData),
   STRUCT('clee' as id, STRUCT("clee", STRUCT("Lee","Chris","Chris
Lee","clee"),[STRUCT("work","clee@example.net")],
[STRUCT("personal","abc")],false,"717389",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Female","Female"),CAST(NULL AS
STRUCT<url STRING, imageBinary STRING, format STRING>),
[STRUCT("US","US","Kirkland",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Kirkland","US-KIR-6THC",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING)),
[STRUCT("Engineering","Empower every GCP customer to transform themselves
through intelligence from their data.","Software Engineer","Kirkland","Vertex
AI Search",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS ARRAY<STRUCT<name STRING, description STRING, role
STRING>>))],[STRUCT("jmartinez",CAST(NULL AS STRING))],CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),STRUCT("jmartinez")) AS structData),
   STRUCT('jmartinez' as id, STRUCT("jmartinez",
STRUCT("Martinez","Jessica","Jessica Martinez","jmartinez"),
[STRUCT("work","jmartinez@example.net")],
[STRUCT("personal","abc")],false,"153035",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>), [STRUCT("United States of
America","US","Sunnyvale",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL
AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))], STRUCT("Sunnyvale","US-
SVL-MP2",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING)),[STRUCT("Engineering","Empower every GCP customer
to transform themselves through intelligence from their data.","Engineering
Director","Sunnyvale","Vertex AI Search",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS ARRAY<STRUCT<name STRING, description
STRING, role STRING>>))],CAST(NULL AS ARRAY<STRUCT<personId STRING, email
STRING>>),CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),CAST(NULL AS STRUCT<personId STRING>)) AS structData),
   STRUCT('dtaylor' as id, STRUCT("dtaylor", STRUCT("Taylor","Daniel","Daniel
Taylor","dtaylor"),[STRUCT("work","dtaylor@example.net")],
[STRUCT("personal","abc")],false,"950380",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Female","Female"),CAST(NULL AS
STRUCT<url STRING, imageBinary STRING, format STRING>), [STRUCT("United States
of America","US","Sunnyvale",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Sunnyvale","US-SVL-MP5",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING)),
[STRUCT("Engineering","Empower every GCP customer to transform themselves
through intelligence from their data.","Product Manager","Sunnyvale","Vertex AI
Search",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS ARRAY<STRUCT<name STRING, description STRING, role
STRING>>))],CAST(NULL AS ARRAY<STRUCT<personId STRING, email
STRING>>),CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),CAST(NULL AS STRUCT<personId STRING>)) AS structData),
   STRUCT('oanderson' as id, STRUCT("oanderson",
STRUCT("Anderson","Olivia","Olivia Anderson","oanderson"),
[STRUCT("work","oanderson@example.net")],
[STRUCT("personal","abc")],false,"103388",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>), [STRUCT("United States of
America","US","Remote",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))], STRUCT("Remote","US-
REMOTE-MTV",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING)),[STRUCT("Engineering","Keep developers happy with
their source code tools and services.","Git Maintainer",CAST(NULL AS
STRING),"Developer Services",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS ARRAY<STRUCT<name STRING, description
STRING, role STRING>>))],CAST(NULL AS ARRAY<STRUCT<personId STRING, email
STRING>>),CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),CAST(NULL AS STRUCT<personId STRING>)) AS structData),
   STRUCT('mthomas' as id, STRUCT("mthomas",
STRUCT("Thomas","Matthew","Matthew Thomas","mthomas"),
[STRUCT("work","mthomas@example.net")],
[STRUCT("personal","abc")],false,"363045",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Female","Female"),CAST(NULL AS
STRUCT<url STRING, imageBinary STRING, format STRING>), [STRUCT("United States
of America","US","Mountain View",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Remote","US-MTV-40",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL
AS STRING),CAST(NULL AS STRING)),[STRUCT("Finance","Getting more ambitious
things done","CIO",CAST(NULL AS STRING),"Alphabet",CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS
ARRAY<STRUCT<name STRING, description STRING, role STRING>>))],CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),CAST(NULL AS STRUCT<personId STRING>)) AS structData),
   STRUCT('swhite' as id, STRUCT("swhite", STRUCT("White","Sophia","Sophia
White","swhite"),[STRUCT("work","swhite@example.net")],
[STRUCT("personal","abc")],false,"938578",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>),
[STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING)),
[STRUCT("Customer","Successful Strategic Customer in the Cloud!","Strategic
Cloud Engineer",CAST(NULL AS STRING),"Cloud Professional Services Organization
(PSO)",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL
AS ARRAY<STRUCT<name STRING, description STRING, role STRING>>))],CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),CAST(NULL AS STRUCT<personId STRING>)) AS structData),
   STRUCT('jharris' as id, STRUCT("jharris", STRUCT("Harris","James","James
Harris","jharris"),[STRUCT("work","jharris@example.net")],
[STRUCT("personal","abc")],false,"723457",CAST(NULL AS STRING),CAST(NULL AS
STRING),"focus",CAST(NULL AS DATETIME),CAST(NULL AS DATETIME),CAST(NULL AS
DATETIME),CAST(NULL AS DATETIME),STRUCT("Male","Male"),CAST(NULL AS STRUCT<url
STRING, imageBinary STRING, format STRING>),
[STRUCT("India","IN","Bangalore",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL AS STRING))],
STRUCT("Bangalore","IN-LOCATION-01",CAST(NULL AS STRING),CAST(NULL AS
STRING),CAST(NULL AS STRING),CAST(NULL AS STRING)),
[STRUCT("Recruiting",CAST(NULL AS STRING),"Sr Recruiter",CAST(NULL AS
STRING),"Hiring Committee",CAST(NULL AS STRING),CAST(NULL AS STRING),CAST(NULL
AS STRING),CAST(NULL AS ARRAY<STRUCT<name STRING, description STRING, role
STRING>>))],CAST(NULL AS ARRAY<STRUCT<personId STRING, email
STRING>>),CAST(NULL AS ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL
AS ARRAY<STRUCT<personId STRING, affinityScore NUMERIC>>),CAST(NULL AS
ARRAY<STRUCT<personId STRING, email STRING>>),CAST(NULL AS ARRAY<STRUCT<type
STRING, value STRING>>),CAST(NULL AS STRUCT<personId STRING>)) AS structData)
 ] AS all_records
)
SELECT
 record.id,
 record.structData
```

#### Example payload for Cloud Storage

```
{"id":"person1","structData":{"working_from_home": "false",
"personId":"person1","name":
{"familyName":"Kumar","givenName":"person1","displayName":"person1
Kumar","username":"person1"},"emails":
[{"type":"work","value":"person1@example.net"}],"phoneNumbers":
[{"type":"personal","value":"1234"}],"suspended":false,"employeeId":"13","avail
abilityStatus":"focus","gender":
{"addressMeAs":"Male","type":"Male"},"addresses":
[{"country":"India","countryCode":"IN","locality":"Bangalore"}],"location":
{"value":"Bangalore","buildingId":"IN-LOCATION-
01","floorName":"7"},"organizations":
[{"department":"Engineering","description":"Our mission is to help
organizations be more productive by making contextually relevant information
and collaborators accessible at the right time","jobTitle":"Software
Engineer","location":"Bangalore","name":"Intranet search","projects":
[{"name":"People Search","role":"Individual
Contributor"}],"costCenter":"123"}],"directManager":
{"personId":"manager1"},"managers":[{"personId":"manager1"},
{"personId":"manager2"},{"personId":"manager3"}],"websites":
[{"type":"personal","value":"https://person1.myownpersonaldomain.com"}],"displa
yPhoto":{"imageBinary":{"format":"image/png","data":"binary_content"}}}}
```

Last updated 2026-10-14 UTC. 



## Enable Gemini Notebook Enterprise as a search source

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-notebooklm

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the GCP Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the Generative AI Preview terms and conditions 

(https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the Cloud Data Processing Addendum (https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

If your users create notebooks in Gemini Notebook Enterprise, you can enable notebooks as a search source. You create a data store of type Gemini Notebook Enterprise and attach that data store to Gemini Enterprise apps. The data from the notebooks isn't imported into the data store, but creating this notebook data store gives the app real-time access to the notebook titles in the project. 

Users can then use Gemini Enterprise apps to search on notebook titles. Each user is only shown the notebooks that they created. 

When creating a notebook, the following conditions apply: 

- It must be in the same project as the app. 

- Only one Gemini Notebook Enterprise data store can be attached to an app. 

- The region for the notebooks, data store, and app must be the same. For example, a notebook in the EU multi-region should be linked to a data store in the EU multi-region, which then must be connected to an app in the EU multiregion. 

- The data store is linked to all the notebooks in a given multi-region in that project. 

Console 

To use the console to create a data store that makes notebooks available as search sources, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, select **Gemini Notebook** . 

5. Choose a location for your data store. 

Use the same location as the notebooks that you want to make searchable. 

6. Enter a name for your data store. 

7. Click **Create** . 

### Next steps

- Attach your data store to an app by following Create a search app (/gemini/enterprise/docs/create-app). 

- Preview search results after setup by following the steps in Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Import from Firestore

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-firestore

To ingest data from Firestore, use the following steps to create a data store and ingest data using either the Google Cloud console or the API. 

If your Firestore data is in the same project as Gemini Enterprise, go to Import data from Firestore (#firestore-procedure). 

If your Firestore data is in a different project than your Gemini Enterprise project, go to Set up Firestore access (#set-up-firestore-access). 

### Set up Firestore access from a different project

To give Gemini Enterprise access to Firestore data that's in a different project, follow these steps: 

1. Replace the following _`PROJECT_NUMBER`_ variable with your Gemini Enterprise project number, and then copy the contents of this code block. This is your Gemini Enterprise service account identifier: 

```
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com
```

2. Go to the **IAM & Admin** page. 

IAM & Admin (https://console.cloud.google.com/iam-admin/iam) 

3. Switch to your Firestore project on the **IAM & Admin** page and click **Grant Access** . 

4. For **New principals** , enter the instance's service account identifier and select the **Datastore > Cloud Datastore Import Export Admin** role. 

5. Click **Save** . 

6. Switch back to your Gemini Enterprise project. 

Next, go to Import data from Firestore (#firestore-procedure). 

### Import data from Firestore

ConsoleREST (#rest) (#console) 

To use the console to ingest data from Firestore, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, select **Firestore** . 

5. Specify the project ID, database ID, and collection ID of the data that you plan to import. 

6. Click **Continue** . 

7. Choose a region for your data store. 

8. Enter a name for your data store. 

9. Click **Create** . 

10. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete. 

Depending on the size of your data, ingestion can take several minutes or several hours. 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps in Create a search app (/gemini/enterprise/docs/create-app). 

- To preview how your search results appear after your app and data store are set up, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Import from Bigtable

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigtable

To ingest data from Bigtable, use the following steps to create a data store and ingest data using the API. 

### Set up Bigtable access

To give Gemini Enterprise access to Bigtable data that's in a different project, follow these steps: 

1. Replace the following _`PROJECT_NUMBER`_ variable with your Gemini Enterprise project number, then copy the contents of this code block. This is your Gemini Enterprise service account identifier: 

```
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`
```

2. Go to the **IAM & Admin** page. 

IAM & Admin (https://console.cloud.google.com/iam-admin/iam) 

3. Switch to your Bigtable project on the **IAM & Admin** page and click **Grant Access** . 

4. For **New principals** , enter the instance's service account identifier and select the **Bigtable > Bigtable Reader** role. 

5. Click **Save** . 

6. Switch back to your Gemini Enterprise project. 

Next, go to Import data from Bigtable (#bigtable-procedure). 

### Import data from Bigtable

REST 

To use the command line to create a data store and ingest data from Bigtable, follow these steps: 

1. Create a data store. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/l
ocations/global/collections/default_collection/dataStores?
dataStoreId=DATA_STORE_ID" \
-d '{
 "displayName": "DISPLAY_NAME",
 "industryVertical": "GENERIC",
 "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

   - _`DATA_STORE_ID`_ : the ID of the data store. The ID can contain only lowercase letters, digits, underscores, and hyphens. 

   - _`DISPLAY_NAME`_ : the display name of the data store. This might be displayed in the Google Cloud console. 

2. Import data from Bigtable. 

```
 curl -X POST \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/dataStores/DATA_STORE_ID/br
anches/0/documents:import" \
 -d '{
   "bigtableSource ": {
     "projectId": "BIGTABLE_PROJECT_ID",
     "instanceId": "INSTANCE_ID",
     "tableId": "TABLE_ID",
     "bigtableOptions": {
       "keyFieldName": "KEY_FIELD_NAME",
       "families": {
         "key": "KEY",
         "value": {
           "fieldName": "FIELD_NAME",
           "encoding": "ENCODING",
           "type": "TYPE",
           "columns": [
             {
               "qualifier": "QUALIFIER",
               "fieldName": "FIELD_NAME",
               "encoding": "COLUMN_ENCODING",
               "type": "COLUMN_VALUES_TYPE"
             }
           ]
         }
        }
        ...
     }
   },
   "reconciliationMode": "RECONCILIATION_MODE",
   "autoGenerateIds": "AUTO_GENERATE_IDS",
   "idField": "ID_FIELD",
 }'
```

- Replace the following: 

   - _`PROJECT_ID`_ : the ID of your Gemini Enterprise project. 

   - _`DATA_STORE_ID`_ : the ID of the data store. The ID can contain only lowercase letters, digits, underscores, and hyphens. 

   - _`BIGTABLE_PROJECT_ID`_ : the ID of your Bigtable project. 

   - _`INSTANCE_ID`_ : the ID of your Bigtable instance. 

   - _`TABLE_ID`_ : the ID of your Bigtable table. 

   - _`KEY_FIELD_NAME`_ : optional but recommended. The field name to use for the row key value after ingesting to Gemini Enterprise. 

- _`KEY`_ : required. A string value for the column family key. 

- _`ENCODING`_ : optional. The encoding mode of the values when the type is not STRING.This can be overridden for a specific column by listing that column in `columns` and specifying an encoding for it. 

- _`COLUMN_TYPE`_ : optional. The type of values in this column family. 

- _`QUALIFIER`_ : required. Qualifier of the column. 

- _`FIELD_NAME`_ : optional but recommended. The field name to use for this column after ingesting to Gemini Enterprise. 

- _`COLUMN_ENCODING`_ : optional. The encoding mode of the values for a specific column when the type is not STRING. 

- _`RECONCILIATION_MODE`_ : optional. Values are `FULL` and `INCREMENTAL` . Default is `INCREMENTAL` . Specifying `INCREMENTAL` causes an incremental refresh of data from Bigtable to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID. Specifying `FULL` causes a full rebase of the documents in your data store. In other words, new and updated documents are added to your data store, and documents that are not in Bigtable are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need. 

- _`AUTO_GENERATE_IDS`_ : optional. Specifies whether to automatically generate document IDs. If set to `true` , document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you autogenerate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs. 

Specify `autoGenerateIds` only when `bigquerySource.dataSchema` is set to `custom` . Otherwise an `INVALID_ARGUMENT` error is returned. If you don't specify `autoGenerateIds` or set it to `false` , you must specify `idField` . Otherwise the documents fail to import. 

_`ID_FIELD`_ : optional. Specifies which fields are the document IDs. 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps in Create a search app (/gemini/enterprise/docs/create-app). 

- To preview how your search results appear after your app and data store are set up, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Connect to data from AlloyDB for PostgreSQL

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb-data

**Preview:** You need to be on the allowlist to use this connector. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

You can connect your AlloyDB instance to Gemini Enterprise, enabling live access to your data. 

Compared to importing from AlloyDB, connecting has the following advantages: 

   - Avoids the need for importing, indexing, and duplicating data. 

   - Maximal data freshness. 

   - No additional indexing and storage costs. 

   - No need to flatten structured data into uniform records. 

- Consider the following disadvantages of connecting compared to importing: 

   - This approach supports only structured queries, not semantic or semisemantic queries. 

   - The setup is slightly more involved compared to importing the data. 

### Limitations

Connecting to AlloyDB has the following limitations: 

- Gemini Enterprise supports access control on the level of database objects, such as tables and columns, but not on a per-user level. All users with access to your Gemini Enterprise app can see the same data. 

- Creating an AlloyDB data store is supported through the API, not through the Google Cloud console. 

### Set up AlloyDB AI natural language

This connector relies on AlloyDB AI natural language in AlloyDB, which translates natural language queries into SQL queries. 

Before connecting, set up AlloyDB AI natural language in your database using the steps in Generate SQL queries that answer natural language questions (/alloydb/docs/ai/generate-sql-queries-natural-language) in the AlloyDB documentation. 

Note that adding templates in AlloyDB AI natural language (a curated set of natural language questions with corresponding SQL queries) is particularly useful for quality. When adding templates, Google recommends the following: 

- Use `ORDER BY` to avoid non-determinism. For example: `SELECT customers.id FROM customers ORDER BY customers.id;` . 

**Note:** You can add templates and other context later. For example, when you notice low answer quality in Gemini Enterprise for a specific question. 

### Set up authentication between Gemini Enterprise and AlloyDB

Gemini Enterprise accesses AlloyDB using a dedicated service account and a database user in your AlloyDB instance. With this approach, every Gemini Enterprise user can see the same data, without user-specific access control. 

A service account is used to connect and interact with your AlloyDB instance. To enable this, you need to configure the Identity and Access Management (IAM) settings in the Google Cloud project where your database instance resides. 

To set up authentication, do the following: 

1. Navigate to the IAM configuration page of the project that hosts your AlloyDB instance. 

2. Grant the **Cloud AlloyDB Database User** role to the following principal: `service-` _`PROJECT_NUMBER`_ `@gcp-sa-discoveryengine.iam.gserviceaccount.com` 

Replace `PROJECT_NUMBER` with the Google Cloud project number where you use Gemini Enterprise. 

3. In your AlloyDB instance, create a DB user to be used by Gemini Enterprise to execute SQL queries. 

It is very important that you grant this user read-only access and only for tables, views and columns that should be accessible from Gemini Enterprise. This ensures that: 

- Queries from Gemini Enterprise cannot change or delete your data. Gemini Enterprise is designed to only read data from your database and not change anything, but Google can't fully exclude the possibility that the AI might generate unintended write-queries. 

- Users in Gemini Enterprise can only see data they are supposed to see. 

- For example: 

```
CREATE ROLE USER_NAME WITH LOGIN PASSWORD 'PASSWORD';
GRANT SELECT ON TABLE "public"."TABLE_NAME_1" TO USER_NAME;
GRANT SELECT ON TABLE "public"."TABLE_NAME_2" TO USER_NAME;
```

When linking Gemini Enterprise with AlloyDB, provide the username and password in the **User** and **Password** fields of `alloydbConnectionConfig` . 

#### Link Gemini Enterprise with AlloyDB

To connect your AlloyDB instance, follow these steps: 

1. Create a data store in Gemini Enterprise with your AlloyDB connection details using the API, including `federatedSearchConfig.alloyDbConfig` . 

The following example: 

```
curl -X POST \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json" \` 

```
 -H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locati
ons/LOCATION/collections/default_collection/dataStores?
dataStoreId=DATA_STORE_ID" -d '{
 "displayName": "DATA_STORE_NAME",
 "federatedSearchConfig": {
   "alloyDbConfig": {
     "alloydbConnectionConfig": {
       "instance": "INSTANCE_PATH",
       "database": "DATABASE_NAME",
       "user": "DATABASE_USER_NAME",
       "password": "DATABASE_USER_PASSWORD",
       "authMode": "AUTH_MODE_SERVICE_ACCOUNT"
     },
     "alloydb_ai_nl_config": { "nlConfigId": "NL_CONFIG_ID" }
   }
 },
 "industryVertical": "GENERIC",
 "solutionTypes": ["SOLUTION_TYPE_SEARCH"]
}'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project where you use Gemini Enterprise. 

- _`LOCATION`_ : The location of your data store. This should be the same location as your Gemini Enterprise instance. 

**Important:** For locations other than **`global`** , replace **`discoveryengine`** with the location-specific path. For more information, see Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

- _`DATA_STORE_ID`_ : the ID of the data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens. 

- _`DATA_STORE_NAME`_ : the display name of the data store that you want to create. 

- _`INSTANCE_PATH`_ : The path of your AlloyDB instance, in the format `projects/.../locations/.../clusters/.../instances/...` . 

   - _`DATABASE_NAME`_ : the ID of the AlloyDB database. 

   - _`DATABASE_USER_NAME`_ : the ID of the AlloyDB database user. 

   - _`DATABASE_USER_PASSWORD`_ : the password of the AlloyDB database user. 

   - _`NL_CONFIG_ID`_ : the ID of the AlloyDB AI natural language configuration. 

2. Attach your data store to an existing Gemini Enterprise app, or create a new app and select your connector, following the steps in Create an app (/gemini/enterprise/docs/create-app). 

3. To preview how your search results appear after your app is set up, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Connect to Data Cloud

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-data-cloud

Gemini Enterprise Data Cloud connectors let you connect your Gemini Enterprise apps directly to Google Cloud analytical and operational data sources. The following Data Cloud connectors are available: 

- BigQuery (available in data ingestion mode 

- (/gemini/enterprise/docs/connectors/connect-bigquery#data-ingestion) and federated query mode (/gemini/enterprise/docs/connectors/connect-bigquery#federated-query) (Preview (https://cloud.google.com/products#product-launch-stages))) 

- Spanner (available in data ingestion mode 

- (/gemini/enterprise/docs/connectors/connect-spanner#data-ingestion) and federated query mode (/gemini/enterprise/docs/connectors/connect-spanner#federated-query) (Preview (https://cloud.google.com/products#product-launch-stages))) 

- Cloud SQL (available in data ingestion mode 

- (/gemini/enterprise/docs/connectors/connect-cloud-sql#data-ingestion) and federated query mode (/gemini/enterprise/docs/connectors/connect-cloud-sql#federated-query) (Preview (https://cloud.google.com/products#product-launch-stages))) 

- AlloyDB for PostgreSQL (available in data ingestion mode 

- (/gemini/enterprise/docs/connectors/connect-alloydb#data-ingestion) and federated query mode (/gemini/enterprise/docs/connectors/connect-alloydb#federated-query) (Preview (https://cloud.google.com/products#product-launch-stages))) 

When you connect a BigQuery, Spanner, Cloud SQL, or AlloyDB for PostgreSQL data store in **federated query mode** , Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (Preview (https://cloud.google.com/products#product-launch-stages)) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app—rather than as a separate data store—to give the agent tools to search for data that the user has access to and look up context. 

### Use cases

Data Cloud connectors are built to power conversational analytics, enabling business users and analysts to ask questions in natural language, explore data, and generate insights in Gemini Enterprise apps. Example use cases include: 

- **BigQuery analytics** : Use natural language prompts to query and analyze structured data residing in BigQuery or that can be consumed in BigQuery. 

- **Real-time operational database insights (Spanner, Cloud SQL, and AlloyDB for PostgreSQL)** : Run live analytical queries and authorized database operations across relational and distributed databases. 

### How Data Cloud connectors work

In data ingestion mode, Data Cloud connectors copy data from the data source into the Gemini Enterprise data store. 

In federated query mode, Data Cloud connectors query your data in place without copying or indexing it into a Gemini Enterprise data store: 

1. **Model Context Protocol (MCP) and per-user authentication** : Each Data Cloud connector is powered by a first-party (1P) MCP server. When a user asks a question, Gemini Enterprise authenticates the request using the user's own credentials (Identity and Access Management (IAM) permissions or OAuth 2.1) and executes queries directly against the underlying data source. 

2. **Semantic discovery and context retrieval with Knowledge Catalog** : When a user asks a data question, the Gemini Enterprise root agent uses built-in Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog) tools to search for data assets that the user has access to and look up context—including relevant tables, schemas, business glossary terms, and enriched metadata (derived from technical metadata, historical query patterns, and LLM inference). 

3. **Live query formulation and execution** : Using the schema and business context retrieved from Knowledge Catalog, the agent formulates a SQL query and invokes the connector's MCP tools to return governed, real-time results. 

**Important: Data Cloud connectors are not scoped to specific resources.** When you attach a Data Cloud connector (such as the BigQuery connector) to an app, the connector is not restricted to a single dataset, table, or database instance—it can access **all resources in that data source that the authenticated user has permission to view or query** . To guide the agent toward specific datasets or business definitions, use Knowledge Catalog metadata, custom instructions, and agent skills. If your workload requires strict deterministic scoping to a specific database or table set for high accuracy, consider creating a scoped data agent (#connectors-vs-agents) for conversational analytics and publishing it to Gemini Enterprise instead. 

### Benefits of first-party Data Cloud connectors over custom MCP servers

Compared to connecting to public or self-managed MCP servers using a generic custom MCP server data store, first-party Data Cloud connectors provide the following advantages: 

1. **Built-in skills for higher response quality** : First-party connectors include pre-configured agent skills tailored to each data engine — such as advanced SQL and AI function generation for BigQuery and databases — to improve query accuracy and response quality. 

2. **Streamlined setup and managed authentication** : First-party connectors provide a guided setup experience with managed authentication for Google Cloud databases and BigQuery, removing the need to deploy MCP middleware or manage your own OAuth client configuration for Google Cloud services. In addition, connector-specific settings — such as deterministically specifying a default Google Cloud billing project for BigQuery query execution — help administrators enforce governance and manage query costs. 

### When to use Data Cloud connectors versus conversational analytics data agents

You can connect data to Gemini Enterprise using **Data Cloud connectors** (lowfriction, broad-access connections directly in Gemini Enterprise) or **conversational analytics data agents** (purpose-built domain experts scoped to curated datasets for high accuracy). 

The following table compares the two approaches to help you choose the approach for your use case: 

|Characteristic|Data Cloud connectors|Conversational analytics data agents|
|---|---|---|
|Best for|Broad, low-friction data access across<br>multiple databases, data warehouses,<br>and BI sources directly within Gemini<br>Enterprise without upfront schema<br>curation.|Curated, domain-specific analytics<br>where high query accuracy is<br>essential and a dedicated expert<br>agent requires strict, deterministic<br>scoping to specific data.|
|Query accuracy<br>and verification|Formulates queries dynamically across<br>a broad schema using catalog<br>metadata and general skills. Query<br>accuracy can vary on complex or<br>normalized relational database<br>schemas without explicit table scoping<br>or verified queries.|Uses curated schemas, focused table<br>and column scoping, and verified<br>queries (golden SQL) to provide high<br>query accuracy and deterministic<br>results on targeted datasets.|
|Resource<br>scoping|Broad access: Accesses all resources in<br>the connected data source that the<br>authenticated user has permission to<br>query (guided by Knowledge Catalog<br>and skills).|Deterministic scoping:<br>Deterministically restricts the agent to<br>a specific set of pre-selected datasets<br>or tables.|
|Multi-source<br>queries and<br>context|Can join and query across multiple<br>connected data sources in a single<br>conversation; the Gemini Enterprise<br>root agent retains full context across<br>the entire conversation and across all<br>Gemini Enterprise experiences (chat,<br>prompts, agent and workflow<br>designers, and projects).|Each data agent is limited to a single<br>data source (for example, a BigQuery<br>data agent only queries BigQuery);<br>users must discover and route to the<br>specific agent, and subagent handoffs<br>may not retain full root conversation<br>context.|
|Setup and<br>maintenance|Quick configuration: Configure one<br>connector per data source type to mak<br>all user-accessible data available<br>immediately without manual schema<br>curation.|e<br>Upfront curation trade-off: Requires<br>selecting tables, defining metrics and<br>KPIs, and authoring verified queries.<br>This upfront curation yields<br>deterministic, reliable query results.|

Characteristic Data Cloud connectors Conversational analytics data agents Discovering tables across a broad data Domain-curated context can yield Performance estate can introduce additional latency higher accuracy on targeted and billing and relies on well-maintained metadata workloads, but conversational considerations and skills for accuracy. analytics data agents incur data token charges. 

#### Create and publish conversational analytics data agents

To achieve high query accuracy on relational databases and targeted business metrics, you can create and publish scoped conversational analytics data agents to Gemini Enterprise: 

Publish Spanner data agents to Gemini Enterprise 

- (/gemini/data-agents/conversational-analytics/spanner/create-data-agents#publishagent-gemini-enterprise) 

Publish Cloud SQL data agents to Gemini Enterprise 

- (/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents#publishagent-gemini-enterprise) 

Publish AlloyDB for PostgreSQL data agents to Gemini Enterprise 

- (/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#publishagent-gemini-enterprise) 

- Conversational analytics in BigQuery (/bigquery/docs/conversational-analytics) 

### Limitations

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Federated queries on relational databases have no table scoping or verified queries. Query accuracy can vary on complex transactional database (for example, AlloyDB for PostgreSQL, Cloud SQL, Spanner) schemas. 

### What's next

- To learn how the built-in analytical harness works and how to provide organizational context with skills and Knowledge Catalog, see Best practices for Data Cloud connectors that use conversational analytics 

- (/gemini/enterprise/docs/connectors/data-cloud-best-practices). 

- To learn about supported security controls (DRZ, CMEK, and VPC Service Controls) and organization policy configuration, see Secure Data Cloud connectors (/gemini/enterprise/docs/connectors/data-cloud-security). 

- To learn how Knowledge Catalog works with Data Cloud connectors and how to manage it in your app's assistant configuration, see Connect to Knowledge Catalog (/gemini/enterprise/docs/connectors/connect-knowledge-catalog). 

- To create and configure a connector with BigQuery, see Connect to BigQuery (/gemini/enterprise/docs/connectors/connect-bigquery). 

- To create and configure a connector with Spanner, see Connect to Spanner (/gemini/enterprise/docs/connectors/connect-spanner). 

- To create and configure a connector with Cloud SQL, see Connect to Cloud SQL (/gemini/enterprise/docs/connectors/connect-cloud-sql). 

- To create and configure a connector with AlloyDB for PostgreSQL, see Connect to AlloyDB for PostgreSQL (/gemini/enterprise/docs/connectors/connect-alloydb). 

Last updated 2026-10-14 UTC.
