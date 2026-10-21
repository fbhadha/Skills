# Gemini Enterprise: user guide, Workflow Builder, developer guide / Authenticate to Gemini Enterprise to Gemini Enterprise client libraries
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 528-543, extracted 2026-10-18

Contains:
- Authenticate to Gemini Enterprise (pages 528-536) https://docs.cloud.google.com/gemini/enterprise/docs/authentication
- Gemini Enterprise client libraries (pages 537-543) https://docs.cloud.google.com/gemini/enterprise/docs/libraries

## Authenticate to Gemini Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/docs/authentication

This document describes how to authenticate to Gemini Enterprise programmatically. How you authenticate to Gemini Enterprise depends on the interface you use to access the API and the environment where your code is running. 

For more information about Google Cloud authentication, see the Authentication methods (/docs/authentication). 

### API access

Gemini Enterprise supports programmatic access. You can access the API in the following ways: 

Client libraries (#client-libraries) 

REST (#rest) 

#### Client libraries

The Gemini Enterprise client libraries (/gemini/enterprise/docs/libraries) provide highlevel language support for authenticating to Gemini Enterprise programmatically. To authenticate calls to Google Cloud APIs, client libraries support Application Default Credentials (ADC) (/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

#### REST

You can authenticate to the Gemini Enterprise API (/gemini/enterprise/docs/apis) by using your gcloud CLI credentials (/sdk/docs/authenticate) or by using Application Default Credentials (/docs/authentication/application-default-credentials). For more 

information about authentication for REST requests, see Authenticate for using REST (/docs/authentication/rest). 

### Set up authentication for Gemini Enterprise

How you set up authentication depends on the environment where your code is running. 

The following options for setting up authentication are the most commonly used. For more options and information about authentication, see Authentication methods (/docs/authentication). 

Before you complete these instructions, you must complete the basic setup for Gemini Enterprise, as described in Before you begin (/gemini/enterprise/docs/before-you-begin). 

#### For a local development environment

You can set up credentials for a local development environment in the following ways: 

- User credentials for client libraries or third-party tools (#client-libs) 

- User credentials for REST requests from the command line (#rest-requests) Service account impersonation (#sa-impersonation) 

Client libraries or third-party tools 

Set up Application Default Credentials (ADC) 

(/docs/authentication/application-default-credentials) in your local environment: 

1. Install (/sdk/docs/install) the Google Cloud CLI. After installation, initialize (/sdk/docs/initializing) the Google Cloud CLI by running the following command: 

```
gcloud init
```

If you're using an external identity provider (IdP), you must first sign in to the gcloud CLI with your federated identity (/iam/docs/workforce-log-in-gcloud). 

2. If you're using a local shell, then create local authentication credentials for your user account: 

```
gcloud auth application-default login
```

You don't need to do this if you're using Cloud Shell. 

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have signed in to the gcloud CLI with your federated identity (/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the local credential file used by ADC 

(/docs/authentication/application-default-credentials#personal). 

For more information about working with ADC in a local environment, see Set up ADC for a local development environment (/docs/authentication/set-up-adc-local-dev-environment). 

REST requests from the command line 

When you make a REST request from the command line, you can use your gcloud CLI credentials by including `gcloud auth print-access-token` (/sdk/gcloud/reference/auth/print-access-token) as part of the command that sends the request. 

The following example lists service accounts for the specified project. You can use the same pattern for any REST request. 

Before using any of the request data, make the following replacements: 

_PROJECT_ID_ : Your Google Cloud project ID. 

To send your request, expand one of these options: 

<sup>curl (Linux, macOS, or Cloud Shell)</sup> 

Execute the following command: 

```
curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts"
```

<sup>PowerShell (Windows)</sup> 

Execute the following command: 

```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }
Invoke-WebRequest `
   -Method GET `
   -Headers $headers `
   -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts" |
Select-Object -Expand Content
```

For more information about authenticating using REST and gRPC, see Authenticate for using REST (/docs/authentication/rest). For information about the difference between your local ADC credentials and your gcloud CLI credentials, see gcloud CLI authentication configuration and ADC configuration 

(/docs/authentication/provide-credentials-adc#gcloud-credentials). 

Service account impersonation 

In most cases, you can use your user credentials to authenticate from a local development environment. If that is not feasible, or if you need to test the permissions assigned to a service account, you can use service account impersonation. You must have the `iam.serviceAccounts.getAccessToken` permission, 

which is included in the Service Account Token Creator 

(/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) ( `roles/iam.serviceAccountTokenCreator` ) IAM role. 

You can set up the gcloud CLI to use service account impersonation by using the `gcloud config set` command (/sdk/gcloud/reference/config): 

```
gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL
```

For select languages, you can use service account impersonation to create a local ADC file for use by client libraries. This approach is supported only for the Go, Java, Node.js, and Python client libraries—it is not supported for the other languages. To set up a local ADC file with service account impersonation, use the `--impersonate-` `service-account` flag (/sdk/gcloud/reference#--impersonate-service-account) with the `gcloud auth application-default login` command 

(/sdk/gcloud/reference/auth/application-default/login): 

```
gcloud auth application-default login --impersonate-service-
account=SERVICE_ACCT_EMAIL
```

For more information about service account impersonation, see Use service account impersonation (/docs/authentication/use-service-account-impersonation). 

#### On Google Cloud

To authenticate a workload running on Google Cloud, you use the credentials of the service account attached to the compute resource where your code is running, such as a Compute Engine virtual machine (VM) instance 

(/compute/docs/access/create-enable-service-accounts-for-instances#using). This approach is the preferred authentication method for code running on a Google Cloud compute resource. 

For most services, you must attach the service account when you create the resource that will run your code; you cannot add or replace the service account 

later. Compute Engine is an exception—it lets you attach a service account to a VM instance at any time. 

Use the gcloud CLI to create a service account and attach it to your resource: 

1. Install (/sdk/docs/install) the Google Cloud CLI. After installation, initialize (/sdk/docs/initializing) the Google Cloud CLI by running the following command: 

```
gcloud init
```

If you're using an external identity provider (IdP), you must first sign in to the gcloud CLI with your federated identity (/iam/docs/workforce-log-in-gcloud). 

2. Set up authentication: 

   - a. Ensure that you have the Create Service Accounts IAM role ( `roles/iam.serviceAccountCreator` ) and the Project IAM Admin role ( `roles/resourcemanager.projectIamAdmin` ) . Learn how to grant roles (/iam/docs/granting-changing-revoking-access). 

   - b. Create the service account: 

```
gcloud iam service-accounts create SERVICE_ACCOUNT_NAME
```

Replace _`SERVICE_ACCOUNT_NAME`_ with a name for the service account. 

- c. To provide access to your project and your resources, grant a role to the service account: 

```
gcloud projects add-iam-policy-binding PROJECT_ID --
member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceacc
ount.com" --role=ROLE
```

Replace the following: 

- _`SERVICE_ACCOUNT_NAME`_ : the name of the service account 

- _`PROJECT_ID`_ : the project ID where you created the service account _`ROLE`_ : the role to grant 

**Note** : The **`--role`** flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a predefned rolei 

(/iam/docs/understanding-roles#predefined_roles) or custom role 

(/iam/docs/understanding-custom-roles) that meets your needs. 

- d. To grant another role to the service account, run the command as you did in the previous step. 

- e. Grant the required role to the principal that will attach the service account to other resources. 

```
gcloud iam service-accounts add-iam-policy-binding
SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --
member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser
```

Replace the following: 

   - _`SERVICE_ACCOUNT_NAME`_ : the name of the service account 

   - _`PROJECT_ID`_ : the project ID where you created the service account 

   - _`USER_EMAIL`_ : the email address for a Google Account 

3. Create the resource that will run your code, and attach the service account to that resource. For example, if you use Compute Engine: 

Create a Compute Engine instance. Configure the instance as follows: 

- Replace _`INSTANCE_NAME`_ with your preferred instance name. 

- Set the `--zone` flag to the zone (/compute/docs/zones#available) in which you want to create your instance. 

- Set the `--service-account` flag to the email address for the service account that you created. 

```
gcloud compute instances create INSTANCE_NAME --zone=ZONE --service-
account=SERVICE_ACCOUNT_EMAIL
```

For more information about authenticating to Google APIs, see Authentication methods (/docs/authentication). 

#### On-premises or on a different cloud provider

The preferred method to set up authentication from outside of Google Cloud is to use workload identity federation. For more information, see Set up ADC for on- premises or another cloud provider (/docs/authentication/set-up-adc-on-premises) in the authentication documentation. 

### Access control for Gemini Enterprise

After you authenticate to Gemini Enterprise, you must be authorized to access Google Cloud resources. Gemini Enterprise uses Identity and Access Management (IAM) for authorization. 

For more information about the roles for Gemini Enterprise, see Access control with IAM (/gemini/enterprise/docs/access-control). For more information about IAM and authorization, see IAM overview (/iam/docs/overview). 

### What's next

- Learn about Google Cloud authentication methods (/docs/authentication#auth-decision-tree). 

See a list of authentication use cases (/docs/authentication/use-cases). 

Last updated 2026-10-14 UTC. 



## Gemini Enterprise client libraries

URL: https://docs.cloud.google.com/gemini/enterprise/docs/libraries

This page shows how to get started with the Cloud Client Libraries for the Gemini Enterprise API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write. 

Read more about the Cloud Client Libraries and the older Google API Client Libraries in Client libraries explained (/apis/docs/client-libraries-explained). 

**Important:** Gemini Enterprise uses the Discovery Engine API and client libraries. 

### Install the client library

C#Java (#java)Node.js (#node.js)PHP (#php)Python (#python)Ruby (#ruby) (#c) 

```
Install-Package Google.Cloud.DiscoveryEngine.V1Beta -Pre
```

For more information, see Setting Up a C# Development Environment (/dotnet/docs/setup). 

### Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support Application Default Credentials (ADC) (/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see Set up Application Default Credentials (/docs/authentication/provide-credentials-adc). 

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account: 

1. Install (/sdk/docs/install) the Google Cloud CLI. After installation, initialize (/sdk/docs/initializing) the Google Cloud CLI by running the following command: 

```
gcloud init
```

If you're using an external identity provider (IdP), you must first sign in to the gcloud CLI with your federated identity (/iam/docs/workforce-log-in-gcloud). 

2. If you're using a local shell, then create local authentication credentials for your user account: 

```
gcloud auth application-default login
```

You don't need to do this if you're using Cloud Shell. 

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have signed in to the gcloud CLI with your federated identity (/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the local credential file used by ADC 

(/docs/authentication/application-default-credentials#personal). 

### Use the client library

The following example shows how to use the client library. 

`using Google.Api.Gax` 

(https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api. Gax.html) `;` 

```
using Google.Cloud.DiscoveryEngine.V1Beta
```

(https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.html) `; using Google.Protobuf.WellKnownTypes` 

(https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Pro tobuf.WellKnownTypes.html) `; using System;` 

```
public sealed partial class GeneratedSearchServiceClientSnippets
{
   /// <summary>Snippet for Search</summary>
   /// <remarks>
   /// This snippet has been automatically generated and should be
regarded as a code template only.
```

`/// It will require modifications to work: /// - It may require correct/in-range values for request initialization. /// - It may require specifying regional endpoints when creating the service client as shown in ///   https://cloud.google.com/dotnet/docs/reference/help/clientconfiguration#endpoint. /// </remarks> public void SearchRequestObject() { // Create client SearchServiceClient searchServiceClient = SearchServiceClient.Create(); // Initialize request argument(s) SearchRequest request = new SearchRequest { ServingConfigAsServingConfigName = ServingConfigName` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html) `.FromProjectLocationDataStoreServingConfig` 

(https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ServingConfigName.html#Google_Clo ud_DiscoveryEngine_V1Beta_ServingConfigName_FromProjectLocationDataStoreServing Config_System_String_System_String_System_String_System_String_) `("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]"), BranchAsBranchName = BranchName` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName.html) `.FromProjectLocationDataStoreBranch` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName.html#Google_Cloud_Dis coveryEngine_V1Beta_BranchName_FromProjectLocationDataStoreBranch_System_Strin g_System_String_System_String_System_String_) `("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"), Query = "", Offset = 0, Filter = "", OrderBy = "", FacetSpecs = { new SearchRequest.Types.FacetSpec(), }, BoostSpec = new SearchRequest.Types.BoostSpec(), Params = { { "", new Value` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Pro tobuf.WellKnownTypes.Value.html) `() }, }, QueryExpansionSpec = new SearchRequest.Types.QueryExpansionSpec(), SpellCorrectionSpec = new SearchRequest.Types.SpellCorrectionSpec(), UserPseudoId = "", ImageQuery = new SearchRequest.Types.ImageQuery(), SafeSearch = false, UserInfo = new UserInfo` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UserInfo.html) `(), UserLabels = { { "", "" }, }, EmbeddingSpec = new SearchRequest.Types.EmbeddingSpec(), ContentSearchSpec = new SearchRequest.Types.ContentSearchSpec(), RankingExpression = "", NaturalLanguageQueryUnderstandingSpec = new SearchRequest.Types.NaturalLanguageQueryUnderstandingSpec(),` 

`CanonicalFilter = "", SearchAsYouTypeSpec = new SearchRequest.Types.SearchAsYouTypeSpec(), DataStoreSpecs = { new SearchRequest.Types.DataStoreSpec(), }, LanguageCode = "", RegionCode = "", DisplaySpec = new SearchRequest.Types.DisplaySpec(), CrowdingSpecs = { new SearchRequest.Types.CrowdingSpec(), }, SessionAsSessionName = SessionName.FromProjectLocationDataStoreSession("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]"), SessionSpec = new SearchRequest.Types.SessionSpec(), RelevanceThreshold = SearchRequest.Types.RelevanceThreshold.Unspecified` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest.Types.Reco nciliationMode.html#Google_Cloud_DiscoveryEngine_V1Beta_ImportDocumentsRequest _Types_ReconciliationMode_Unspecified) `, PersonalizationSpec = new SearchRequest.Types.PersonalizationSpec(), OneBoxPageSize = 0, RelevanceScoreSpec = new SearchRequest.Types.RelevanceScoreSpec(), RankingExpressionBackend = SearchRequest.Types.RankingExpressionBackend.Unspecified` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest.Types.Reco nciliationMode.html#Google_Cloud_DiscoveryEngine_V1Beta_ImportDocumentsRequest _Types_ReconciliationMode_Unspecified) `, SearchAddonSpec = new SearchRequest.Types.SearchAddonSpec(), PageCategories = { "", }, CustomRankingParams = new SearchRequest.Types.CustomRankingParams(), NumResultsPerDataStore = 0, Entity = "", RelevanceFilterSpec = new SearchRequest.Types.RelevanceFilterSpec(),` 

`}; // Make the request PagedEnumerable<SearchResponse, SearchResponse.Types.SearchResult> response = searchServiceClient.Search(request); // Iterate over all response items, lazily performing RPCs as required foreach (SearchResponse.Types.SearchResult item in response) { // Do something with each item Console.WriteLine(item); } // Or iterate over pages (of server-defined size), performing one RPC per page foreach (SearchResponse page in response.AsRawResponses()) { // Do something with each page of items Console.WriteLine("A page of results:"); foreach (SearchResponse.Types.SearchResult item in page) { // Do something with each item Console.WriteLine(item); } } // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required int pageSize = 10; Page<SearchResponse.Types.SearchResult> singlePage = response.ReadPage(pageSize); // Do something with the page of items Console.WriteLine($"A page of {pageSize} results (unless it's the final page):"); foreach (SearchResponse.Types.SearchResult item in singlePage) { // Do something with each item Console.WriteLine(item); } // Store the pageToken, for when the next page is required. string nextPageToken = singlePage.NextPageToken` (https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1 Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse.html#Googl e_Cloud_DiscoveryEngine_V1Beta_ListDocumentsResponse_NextPageToken) `;` 

```
   }
}
```

### Additional resources

C#Java (#java)Node.js (#node.js)PHP (#php)Python (#python)Ruby (#ruby) (#c) 

The following list contains links to more resources related to the client library for C#: 

- API reference (/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest) Client libraries best practices (/apis/docs/client-libraries-best-practices) 

- Issue tracker (https://github.com/googleapis/google-cloud-dotnet/issues) 

- `Gemini Enterprise` on Stack Overflow (https://stackoverflow.com/search?q=%5BGemini Enterprise%5D+%5Bc%23%5D) 

- Source code (https://github.com/googleapis/google-cloud-dotnet) 

Last updated 2026-08-18 UTC.
