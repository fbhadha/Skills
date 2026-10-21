# Gemini Enterprise: platform, security, agents, cost, monitoring / Parse and chunk documents to Create an app
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 332-363, extracted 2026-10-18

Contains:
- Parse and chunk documents (pages 332-361) https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents
- Create an app (pages 362-363) https://docs.cloud.google.com/gemini/enterprise/docs/create-app

## Parse and chunk documents

URL: https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents

The default parser for Gemini Enterprise is the Layout parser. It's generally the best choice because it detects and understands document hierarchy, which leads to better chunking and ultimately better answer generation and retrieval. However, you might want to change the default parser in certain situations, such as when you have a lot of scanned data to upload into your data store. This page describes how to change the parser. 

You can specify how to parse unstructured content when you upload it to Gemini Enterprise. Gemini Enterprise provides a layout parser (default, recommended), a digital parser, and an OCR parser for PDFs. You can also bring your own parsed documents. 

See Improve content detection with parsing (#parsing). 

### Parse documents

You can control content parsing in the following ways: 

- **Specify parser type.** You can specify the type of parsing to apply depending on file type: 

   - **Layout parser.** The layout parser is the default parser. See Chunk documents for RAG (#parse-chunk-rag) for information about this parser. 

   - **OCR parsing for PDFs** . If you plan to upload scanned PDFs or PDFs with text inside images, you can turn on the OCR parser to improve PDF indexing. See the OCR parser for PDFs (#parsing-pdfs) section of this document. 

   - **Digital parser.** The digital parser is a basic parser that extracts machine-readable text from documents. For more information, see Digital parser (#digital-parsing). 

- **Bring your own parsed document.** (Preview) If you've already parsed your unstructured documents, you can import that pre-parsed content into Gemini Enterprise. See Bring your own parsed document (#bring-parsed-document). 

#### Parser availability comparison

The following table lists the availability of each parser by document file types and shows which elements each parser can detect and parse. 

|File<br>type|Digital parser|OCR parser|Layout parser|
|---|---|---|---|
|HTML|Detects paragraph<br>elements|Not applicable|Detects paragraph, table, image, list,<br>title, and heading elements|
|PDF|Detects paragraph (digital<br>text) elements|Detects paragraph<br>elements|Detects paragraph, table, title, image,<br>and heading elements|
|DOCX|Detects paragraph<br>elements|Not applicable|Detects paragraph, table, image, list,<br>title, heading elements|
|PPTX|Detects paragraph<br>elements|Not applicable|Detects paragraph, table, image, list,<br>title, heading elements|
|TXT|Detects paragraph<br>elements|Not applicable|Not applicable|
|XLSX|Detects paragraph<br>elements|Not applicable|Detects paragraph, table, title, heading<br>elements|
|XLSM|Detects paragraph<br>elements|Not applicable|Detects paragraph, table, title, heading<br>elements|

#### OCR parser for PDFs

If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images, such as infographics) Google recommends turning on optical character recognition (OCR) processing during data store creation. This allows Gemini Enterprise to extract paragraph elements. 

If you have searchable PDFs or other digital formats that are mostly composed of machine-readable text, you typically don't need to use the OCR parser. However, if you have PDFs that have both non-searchable text (such as scanned text or infographics) and machine-readable text, you can set the field `useNativeText` to true when specifying the OCR parser. In this case, machine-readable text is merged with OCR parsing outputs to improve text extraction quality. 

OCR processing features are available for custom search apps with unstructured data stores. 

The OCR processor can parse the first 500 pages of a PDF file. Pages beyond the 500 limit aren't processed. 

#### Layout parser

This is the default parser. It lets Gemini Enterprise detect layouts for PDF, HTML, DOCX, PPTX, XLSX, and XLSM. Gemini Enterprise can then identify content elements like text blocks, tables, lists, and structural elements such as titles and headings and use them to define the organization and hierarchy of a document. 

The layout parser detects content elements like paragraphs, tables, lists, and structural elements like titles, headings, headers, footnotes. 

Gemini Enterprise breaks documents up into chunks at ingestion time and can return documents as chunks. Detecting document layout enables content-aware chunking and enhances search and answer generation related to document elements. For more information about chunking documents for RAG, see Chunk documents for RAG (#parse-chunk-rag). 

The layout parser's full capabilities, like analyzing tables, multi-column layouts, and OCR-dependent content, are best leveraged in data ingestion mode. 

While connectors in federated search connection mode (such as Microsoft SharePoint and Microsoft OneDrive) also use the layout parser, the real-time nature of these queries can prevent the parser from fully analyzing complex PDF structures. For in-depth parsing of complex PDFs, we recommend using connectors in data ingestion mode. 

Image annotation 

With image annotation, when an image is detected in a source document, a description (annotation) of the image and the image itself are assigned to a chunk. The annotation determines if the chunk should be returned in a search result. If an answer is generated, the annotation can be a source for the answer. 

The layout parser can detect the following image types: BMP, GIF, JPEG, PNG, and TIFF. 

Table annotation 

With table annotation, when a table is detected in a source document, a description (annotation) of the table and the table itself are assigned to a chunk. The annotation determines if the chunk should be returned in a search result. If an answer is generated, the annotation can be a source for the answer. 

Exclude HTML content 

When using the layout parser for HTML documents, you can exclude specific parts of the HTML content from being processed. To improve data quality for search applications and RAG applications, you can exclude boilerplate or sections such as navigation menus, headers, footers, or sidebars. 

The `layoutParsingConfig` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#layoutpar singconfig) 

provides the following fields for this purpose: 

- `excludeHtmlElements` : List of HTML tags to be excluded. Content within these tags is excluded. 

- `excludeHtmlClasses` : List of HTML class attributes to be excluded. HTML elements containing these class attributes, along with their content, are excluded. 

- `excludeHtmlIds` : List of HTML element ID attributes to be excluded. HTML elements with these ID attributes, along with their content, are excluded. 

#### Digital parser

The digital parser extracts machine-readable text from documents. It detects text blocks, but not document elements such as tables, lists, and headings. 

The digital parser is used if the specified parser doesn't support a file type that's being uploaded. For example, if the layout parser is specified, the digital parser is used to parse TXT files because the layout parser doesn't support text files. 

#### Specify a default parser

By including the `documentProcessingConfig` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#document processingconfig) 

object when you create a data store, you can specify a default parser for that data store. If you don't include `documentProcessingConfig.defaultParsingConfig` , the digital parser is used. The digital parser is also used if the specified parser is not available for a file type. 

RESTConsole (#console) (#rest) 

To specify a default parser: 

1. When creating a data store 

(/gemini/enterprise/docs/connectors/create-data-store) using the API, include `documentProcessingConfig.defaultParsingConfig` in the data store creation request. You can specify the OCR parser, the layout parser, or the digital parser: 

To specify the OCR parser for PDFs: 

```
"documentProcessingConfig": {
 "defaultParsingConfig": {
   "ocrParsingConfig": {
     "useNativeText": "NATIVE_TEXT_BOOLEAN"
   }
 }
}
```

_`NATIVE_TEXT_BOOLEAN`_ is optional. Set only if you're ingesting PDFs. If set to `true` , this turns on machine-readable text processing for the OCR parser. The default is `false` . 

To specify the layout parser: 

```
"documentProcessingConfig": {
 "defaultParsingConfig": {
   "layoutParsingConfig": {}
 }
}
```

To specify the digital parser: 

**Note:** Specifying the digital parser as **`defaultParsingConfig`** is typically not necessary. When no other parser is explicitly specified, the digital parser is used by default. 

```
"documentProcessingConfig": {
   "defaultParsingConfig": { "digitalParsingConfig": {} }
}
```

Example 

The following example specifies during data store creation that the OCR parser will be the default parser. Because the OCR parser only applies to PDF files, all PDF files that are ingested will be processed by the OCR parser, and any other file types will be processed by the digital parser. 

`curl -X POST \` 

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \ -H "X-Goog-User-Project: exampleproject" \` 

```
"https://discoveryengine.googleapis.com/v1/projects/exampleproject/locations/gl
obal/collections/default_collection/dataStores?dataStoreId=datastore123" \
-d '{
```

- `"displayName": "exampledatastore",` 

- `"industryVertical": "GENERIC",` 

- `"solutionTypes": ["SOLUTION_TYPE_SEARCH"],` 

- `"contentConfig": "CONTENT_REQUIRED",` 

```
 "documentProcessingConfig": {
   "defaultParsingConfig": {
     "ocrParsingConfig": {
       "useNativeText": "false"
     }
   }
 }
}'
```

#### Specify parser overrides for file types

You can specify that a particular file type should be parsed by a different parser than the default parser. To do so, include the `documentProcessingConfig` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#document processingconfig) 

field in your data store creation request and specify the override parser. If you don't specify a default parser, then the digital parser is the default. 

RESTConsole (#console) (#rest) 

To specify a file-type-specific parser override: 

1. When creating a data store 

   - (/gemini/enterprise/docs/connectors/create-data-store) using the API, include `documentProcessingConfig.defaultParsingConfig` in the data store creation request. 

You can specify a parser for a given file type: 

- `"documentProcessingConfig": { "parsingConfigOverrides": { "` _`FILE_TYPE`_ `": {` _`PARSING_CONFIG`_ `}, } }` 

Replace the following: 

- _`FILE_TYPE`_ : Accepted values are `pdf` , `html` , `docx` , `pptx` , `xlsm` , and `xlsx` . 

- _`PARSING_CONFIG`_ : Specify the configuration for the parser that you want to apply to the file type. You can specify the OCR parser, the layout parser, or the digital parser: 

To specify the OCR parser for PDFs: 

- `"ocrParsingConfig": { "useNativeText": "` _`NATIVE_TEXT_BOOLEAN`_ `"` 

- `}` 

   - _`NATIVE_TEXT_BOOLEAN`_ : Optional. Set only if you're ingesting PDFs. If set to `true` , this turns on machinereadable text processing for the OCR parser. The default is `false` . 

- To specify the layout parser: 

```
"layoutParsingConfig": {}
```

- To specify the digital parser: 

- `"documentProcessingConfig": { "defaultParsingConfig": { "digitalParsingConfig": {} }` 

- `}` 

Example 

The following example specifies during data store creation that PDF files should be processed by the OCR parser and that HTML files should be processed by the layout parser. In this case, any files other than PDF and HTML files would be processed by the digital parser. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: exampleproject" \
"https://discoveryengine.googleapis.com/v1/projects/exampleproject/locations/gl
obal/collections/default_collection/dataStores?dataStoreId=datastore123" \
-d '{
 "displayName": "exampledatastore",
 "industryVertical": "GENERIC",
 "solutionTypes": ["SOLUTION_TYPE_SEARCH"],
 "contentConfig": "CONTENT_REQUIRED",
 "documentProcessingConfig": {
   "parsingConfigOverrides": {
     "pdf": {
       "ocrParsingConfig": {
           "useNativeText": "false"
         },
     },
     "html": {
        "layoutParsingConfig": {}
     }
   }
 }
}'
```

#### Edit document parsing for existing data stores

If you already have a data store, you can change the default parser and add file format exceptions. However, the updated parser settings only apply to new documents imported to the data store. Documents already in the data store are not re-parsed with the new settings. 

To change document parsing settings for a data store, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/apps) 

2. In the navigation menu, click **Data Stores** . 

3. In the **Name** column, click the data store that you want to edit. 

4. On the **Processing config** tab, edit the **Document parsing** settings. 

The **Document chunking** settings can't be changed. If the data store doesn't have document chunking enabled, then you can't choose the layout parser. 

5. Click **Submit** . 

#### Configure layout parser to exclude HTML content

You can configure layout parser to exclude HTML content (#exclude-html-content) by specifying `excludeHtmlElements` , `excludeHtmlClasses` or `excludeHtmlIds` in `documentProcessingConfig.defaultParsingConfig.layoutParsingConfig` . 

REST 

(#rest) 

To exclude certain HTML content from being processed by the layout parser, follow these steps: 

1. When creating a search data store 

(/gemini/enterprise/docs/connectors/create-data-store) using the API, include `documentProcessingConfig.defaultParsingConfig.layoutParsingConfig` in the data store creation request. 

2. To exclude specific HTML tag types, use: 

   - `"documentProcessingConfig": { "defaultParsingConfig": { "layoutParsingConfig": { "excludeHtmlElements": ["` _`HTML_TAG_1`_ `","` _`HTML_TAG_2`_ `","` _`HTML_TAG_N`_ `"] } } }` 

Replace the _HTML_TAG_ variables with tag names, for example, `nav` and `footer` . 

3. To exclude specific HTML element class attributes, use: 

```
"documentProcessingConfig": {
 "defaultParsingConfig": {
  "layoutParsingConfig": {
   "excludeHtmlClasses":
["HTML_CLASS_1","HTML_CLASS_2","HTML_CLASS_N"]
  }
 }
}
```

Replace the _HTML_CLASS_ variables with class attributes, for example, `overlay` and `screenreader` . 

4. To exclude specific HTML element ID attributes, use: 

<!-- Start of picture text -->
"documentProcessingConfig": {<br> "defaultParsingConfig": {<br>  "layoutParsingConfig": {<br>   "excludeHtmlIds": [" HTML_ID_1 "," HTML_ID_2 "," HTML_ID_N "]<br>  }<br> }<br>}<br><!-- End of picture text -->

Replace the _HTML_ID_ variables with ID attributes, for example, `cookiebanner` . 

Example 

This example specifies that when HTML files are processed by the layout parser, the following are skipped by the parser: 

HTML element tags, `header` , `footer` , `nav` , and `aside` 

HTML element class attributes of type `overlays` and `screenreader` 

Any elements with the attribute ID of `cookie-banner` 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: exampleproject" \
"https://discoveryengine.googleapis.com/v1/projects/exampleproject/locations/gl
obal/collections/default_collection/dataStores?
dataStoreId=datastore123&createAdvancedSiteSearch=true" \
-d '{
 "displayName": "exampledatastore",
 "industryVertical": "GENERIC",
 "contentConfig": "PUBLIC_WEBSITE",
 "documentProcessingConfig": {
   "chunkingConfig": {
     "layoutBasedChunkingConfig": {}
   },
   "defaultParsingConfig": {
     "layoutParsingConfig": {
      "excludeHtmlElements": ["header", "footer", "nav", "aside"],
      "excludeHtmlClasses": ["overlays", "screenreader"],
      "excludeHtmlIds": ["cookie-banner"]
     }
   }
 }
}'
```

#### Get parsed documents in JSON

You can get a parsed document in JSON format by calling the `getProcessedDocument` (/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branc hes.documents/getProcessedDocument) 

method and specifying `PARSED_DOCUMENT` as the processed document type. Getting parsed documents in JSON can be helpful if you need to upload the parsed document elsewhere or if you decide to re-import parsed documents to Gemini Enterprise using the bring your own parsed document (#bring-parsed-document) feature. 

REST (#rest) 

To get parsed documents in JSON, follow this step: 

1. Call the `getProcessedDocument` method: 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/l
ocations/global/collections/default_collection/dataStores/
DATA_STORE_ID/branches/0/documents/DOCUMENT_ID:getProcessedDocument?
processed_document_type=PARSED_DOCUMENT"
```

Replace the following: 

_`PROJECT_ID`_ : The ID of your project. 

_`DATA_STORE_ID`_ : The ID your data store. 

_`DOCUMENT_ID`_ : The ID of the document to get. 

#### Bring your own parsed document

You can import pre-parsed, unstructured documents into Gemini Enterprise data stores. For example, instead of importing a raw PDF document, you can parse the PDF yourself and import the parsing result instead. This lets you import your documents in a structured way, ensuring that search and answer generation have information about the document's layout and elements. 

A parsed, unstructured document is represented by JSON that describes the unstructured document using a sequence of text, table, and list blocks. 

Before you begin 

Prepare your parsed documents. 

Each parsed document that you want to ingest into an unstructured data store must be represented by a standalone JSON file adhering to the following JSON schema structure: 

|Field|Type<br>Description|
|---|---|
|`title`|String Title of the content file.|
|`description`|String Optional: Description of the document.|
|`uri`|String The Cloud Storage URI of the content.|
|`name`|String Optional: Full resource name path of the document.|
|`blocks`|Array Ordered list of layout blocks representing the document structure.|

<sup>Click to see an example of a layout payload for a parsed document.</sup> 

```
{
 "title": "Document Title",
 "description": "Optional brief description of the document",
 "uri": "gs://my-bucket-123/my_folder/my_first_document.pdf",
 "name": "projects/my-project-
123/locations/global/collections/default_collection/dataStores/my-data-
store/branches/0/documents/document_1",
 "blocks": [
   {
     "blockId": "1",
     "text": "Introduction",
     "type": "HEADING_1",
     "parentBlockId": "0"
   },
   {
     "blockId": "2",
     "text": "This is the first paragraph of the document, explaining the core
concepts.",
     "type": "PARAGRAPH",
     "parentBlockId": "1",
     "childrenBlockIds": ["3"]
   },
   {
     "blockId": "3",
     "listType": "UNORDERED",
     "listEntries": [
       {
         "blockId": "4",
         "text": "First list item supporting the paragraph above."
       },
       {
         "blockId": "5",
         "text": "Second list item."
       }
     ],
     "parentBlockId": "2"
   },
   {
     "blockId": "6",
     "tableCaption": "Summary of Data",
     "headerRows": [
       {
         "cells": [
           {
             "blockId": "7",
             "text": "Column A Header"
           },
           {
             "blockId": "8",
             "text": "Column B Header"
           }
         ]
       }
     ],
     "bodyRows": [
       {
         "cells": [
           {
             "blockId": "9",
             "text": "Row 1, Cell 1"
           },
           {
             "blockId": "10",
             "text": "Row 1, Cell 2"
           }
         ]
       }
     ],
     "parentBlockId": "1"
   }
 ]
}
```

Ingest parsed unstructured data 

You import JSON files with your parsed unstructured document data in the same way that you import other types of unstructured documents, such as PDFs. Whenever a JSON file is uploaded and identified by either an `application/json` MIME type or a JSON file extension in your metadata JSON Lines file, it is treated as a parsed document. 

To ingest parsed unstructured data, do the following: 

1. Prepare your JSON Lines metadata file. 

Each row of the metadata file must follow the structData format: 

<!-- Start of picture text -->
{<br> "id": " DOCUMENT_ID ",<br> "structData": {<br>   "category": " CATEGORY ",<br>   "updated": " YYYY-MM-DD "<br> },<br> "content": {<br>   "mimeType": "application/json",<br>   "uri": "gs:// PARSED_DOC_FILE "<br> }<br>}<br><!-- End of picture text -->

Replace the following: 

   - _`DOCUMENT_ID`_ : The unique ID for the document. 

   - _`CATEGORY`_ : A label of your choice for document classification. This field is typically for metadata that can be used for filtering and faceting. 

   - _`YYYY-MM-DD`_ : The modification date of the document. 

   - _`PARSED_DOC_FILE`_ : The Cloud Storage path to one of the standalone JSON files that you created in the Before you begin (#schema-parsed) above, for example, `my_bucket/my_folder/my_file.json` . 

2. Ingest the data into a new unstructured data store (Create a first-party data store (/gemini/enterprise/docs/connectors/create-data-store)) or into an existing data 

store (Refresh unstructured data (/gemini/enterprise/docs/refresh-data#refresh-unstructured)). 

### Chunk documents for RAG

By default, Gemini Enterprise is optimized for document retrieval, where your search app returns a document such as a PDF or web page with each search result. 

Document chunking features are available for custom search apps with unstructured data stores. 

Gemini Enterprise can instead be optimized for RAG, where your search app is primarily used to augment LLM output with your custom data. When document chunking is turned on, Gemini Enterprise breaks up your documents into chunks. In search results, your search app can return relevant chunks of data instead of full documents. Using chunked data for RAG increases relevance for LLM answers and reduces computational load for LLMs. 

To use Gemini Enterprise for RAG: 

1. Turn on document chunking (#turn-on-chunking) when you create your data store. Alternatively, upload your own chunks (#bring-chunks) (Preview) if you've already chunked your own documents. 

2. Retrieve and view chunks in the following ways: 

   - List chunks from a document (#list-chunks) 

   - Get chunks in JSON from a processed document (#get-processed-chunks) Get specific chunks (#get-chunks) 

3. Return chunks in search requests (#get-chunks-in-search). 

#### Limitations

The following limitations apply to chunking: 

Document chunking can't be turned on or off after data store creation. 

- You can make search requests for documents instead of chunks from a data store with document chunking turned on. However, data stores with document chunking turned on aren't optimized for returning documents. Documents are returned by aggregating chunks into documents. 

#### Document chunking options

This section describes the options that you specify in order to turn on document chunking. 

During data store creation, turn on the following options so that Gemini Enterprise can index your documents as chunks. 

**Layout-aware document chunking.** To turn this option on, include the `documentProcessingConfig` field in your data store creation request and specify `ChunkingConfig.LayoutBasedChunkingConfig` . 

When layout-aware document chunking is turned on, Gemini Enterprise detects a document's layout and take it into account during chunking. This improves semantic coherence and reduces noise in the content when it's used for retrieval and LLM generation. All text in a chunk will come from the same layout entity, such as headings, subheadings, and lists. 

- **Layout parsing.** To turn this option on, specify `ParsingConfig.LayoutParsingConfig` during data store creation. 

The layout parser detects layouts for PDF, HTML, DOCX, PPTX, XLSX, and XLSM files. It identifies elements like text blocks, tables, lists, titles, and headings, and uses them to define the organization and hierarchy of a document. 

For more about layout parsing, see Layout parsing (#layout-parsing). 

#### Turn on document chunking

You can turn on document chunking by including the `documentProcessingConfig` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#document processingconfig) 

object in your data store creation request and turning on layout-aware document chunking and layout parsing. 

RESTConsole (#console) (#rest) 

To turn on document chunking: 

1. When creating a search data store 

(/gemini/enterprise/docs/connectors/create-data-store) using the API, include the `documentProcessingConfig.chunkingConfig` object in the data store creation request. 

```
"documentProcessingConfig": {
  "chunkingConfig": {
      "layoutBasedChunkingConfig": {
          "chunkSize": CHUNK_SIZE_LIMIT,
          "includeAncestorHeadings": HEADINGS_BOOLEAN,
      }
  },
  "defaultParsingConfig": {
    "layoutParsingConfig": {}
  }
}
```

Replace the following: 

_`CHUNK_SIZE_LIMIT`_ : Optional. The token size limit for each chunk. The default value is 500. Supported values are 100-500 (inclusive). _`HEADINGS_BOOLEAN`_ : Optional. Determines whether headings are included in each chunk. The default value is `false` . Appending title and headings at all levels to chunks from the middle of the document can help prevent context loss in chunk retrieval and ranking. 

#### Bring your own chunks

If you've already chunked your own documents, you can upload those to Gemini Enterprise instead of turning on document chunking options. 

Each document you want to bring as pre-segmented chunks must be represented by a standalone JSON file adhering to the following schema: 

<!-- Start of picture text -->
{<br> "documentMetadata": {<br>   "title": " DOCUMENT_TITLE ",<br>   "uri": "gs:// ORIGINAL_DOC_FILE "<br> },<br> "chunks": [<br>   {<br>     "id": " CHUNK_ID ",<br>     "content": " CHUNK_CONTENT ",<br>     "pageSpan": {<br>       "pageStart":  PAGE_START ,<br>       "pageEnd":  PAGE_END<br>     }<br>   }<br> ]<br>}<br><!-- End of picture text -->

Replace the following: 

   - _`DOCUMENT_TITLE`_ : The title of the document. 

   - _`ORIGINAL_DOC_FILE`_ : The Cloud Storage path to the original document file, for example, `my-bucket-123/my_folder/document.pdf` . 

   - _`CHUNK_ID`_ : A unique ID for the chunk. 

   - _`CHUNK_CONTENT`_ : The text content of the chunk. 

   - _`PAGE_START`_ : The page number starting at 1 where the chunk starts in the original document. 

   - _`PAGE_END`_ : The page number starting at 1 where the chunk ends in the original document. 

- <sup>Click to see an example of a chunked payload.</sup> 

```
{
 "documentMetadata": {
   "title": "Document Title",
   "uri": "gs://my-bucket-123/folder/document.pdf"
 },
 "chunks": [
   {
     "id": "chunk_1",
     "content": "This is the text content of the first chunk.",
     "pageSpan": {
       "pageStart": 1,
       "pageEnd": 1
     }
   },
   {
     "id": "chunk_2",
     "content": "This is the text content of the second chunk.",
     "pageSpan": {
       "pageStart": 1,
       "pageEnd": 2
     }
   }
 ]
}
```

There is no explicit toggle to turn on this feature. When a JSON file adhering to this schema is uploaded and identified by either an `application/json` MIME type or JSON file extension in your metadata lines file, it is automatically recognized and ingested as a pre-chunked document. 

#### List a document's chunks

To list all chunks for a specific document, call the `Chunks.list` method. 

REST (#rest) 

To list chunks for a document, follow this step: 

1. Call the `Chunks.list` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.data Stores.branches.documents.chunks/list) 

method: 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/l
ocations/global/collections/default_collection/dataStores/
DATA_STORE_ID/branches/0/documents/DOCUMENT_ID/chunks"
```

Replace the following: 

_`PROJECT_ID`_ : The ID of your project. 

_`DATA_STORE_ID`_ : The ID your data store. 

_`DOCUMENT_ID`_ : The ID of the document to list chunks from. 

#### Get chunks in JSON from a processed document

You can get all the chunks from a specific document in JSON format by calling the `getProcessedDocument` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branc hes.documents/getProcessedDocument) 

method. Getting chunks in JSON can be helpful if you need to upload chunks elsewhere or if you decide to re-import chunks to Gemini Enterprise using the bring your own chunks (#bring-chunks) feature. 

REST 

(#rest) 

To get JSON chunks for a document, follow this step: 

1. Call the `getProcessedDocument` method: 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/l
ocations/global/collections/default_collection/dataStores/
DATA_STORE_ID/branches/0/documents/DOCUMENT_ID:getProcessedDocument?
processed_document_type=CHUNKED_DOCUMENT"
```

Replace the following: 

_`PROJECT_ID`_ : The ID of your project. 

_`DATA_STORE_ID`_ : The ID your data store. 

_`DOCUMENT_ID`_ : The ID of the document to get chunks from. 

#### Get specific chunks

To get a specific chunk, call the `Chunks.get` method. 

REST 

(#rest) 

To get a specific chunk, follow this step: 

1. Call the `Chunks.get` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.data Stores.branches.documents.chunks/get) 

method: 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/l
ocations/global/collections/default_collection/dataStores/
DATA_STORE_ID/branches/0/documents/DOCUMENT_ID/chunks/CHUNK_ID"
```

Replace the following: 

- _`PROJECT_ID`_ : The ID of your project. 

- _`DATA_STORE_ID`_ : The ID your data store. 

- _`DOCUMENT_ID`_ : The ID of the document that the chunk is from. 

- _`CHUNK_ID`_ : The ID of the chunk to return. 

#### Return chunks in search requests

After you've confirmed that your data has been chunked correctly, your Gemini Enterprise can return chunked data in its search results. 

The response returns a chunk that is relevant to the search query. In addition, you can choose to return adjacent chunks that appear before and after the relevant chunk in the source document. Adjacent chunks can add context and accuracy. 

REST 

(#rest) 

To get chunked data: 

1. When making a search request, specify 

`ContentSearchSpec.SearchResultMode` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStore s.servingConfigs#contentsearchspec) 

as `chunks` . 

```
contentSearchSpec": {
 "searchResultMode": "RESULT_MODE",
 "chunkSpec": {
      "numPreviousChunks": NUMBER_OF_PREVIOUS_CHUNKS,
      "numNextChunks": NUMBER_OF_NEXT_CHUNKS
  }
}
```

_`RESULT_MODE`_ : Determines whether search results are returned as full documents or in chunks. To get chunks, the data store must have document chunking turned on. Accepted values are `documents` 

and `chunks` . If document chunking is turned on for your data store, the default value is `chunks` . 

_`NUMBER_OF_PREVIOUS_CHUNKS`_ : The number of chunks to return that immediately preceded the relevant chunk. The maximum allowed value is 5. 

_`NUMBER_OF_NEXT_CHUNKS`_ : The number of chunks to return that immediately follow the relevant chunk. The maximum allowed value is 5. 

Example 

The following example of a search query request sets `SearchResultMode` to `chunks` , requests one previous chunk and one next chunk, and limits the number of results to a single relevant chunk using `pageSize` . 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: exampleproject" \
"https://discoveryengine.googleapis.com/v1/projects/exampleproject/locations/gl
obal/collections/default_collection/dataStores/datastore123/servingConfigs/defa
ult_search:search" \
-d '{
 "query": "animal",
 "pageSize": 1,
 "contentSearchSpec": {
   "searchResultMode": "CHUNKS",
   "chunkSpec": {
          "numPreviousChunks": 1,
          "numNextChunks": 1
      }
 }
}'
```

The following example shows the response that is returned for the example query. The response contains the relevant chunks, the previous and next chunks, the 

original document's metadata, and the span of document pages that each chunk was derived from. 

<sup>Response</sup> 

```
{
 "results": [
   {
     "chunk": {
       "name":
"projects/961309680810/locations/global/collections/default_collection/dataStor
es/allie-pdf-adjacent-
chunks_1711394998841/branches/0/documents/0d8619f429d7f20b3575b14cd0ad0813/chun
ks/c17",
       "id": "c17",
       "content": "\n# ESS10: Stakeholder Engagement and Information
Disclosure\nReaders should also refer to ESS10 and its guidance notes, plus the
template available for a stakeholder engagement plan. More detail on
stakeholder engagement in projects with risks related to animal health is
contained in section 4 below. The type of stakeholders (men and women) that can
be engaged by the Borrower as part of the project's environmental and social
assessment and project design and implementation are diverse and vary based on
the type of intervention. The stakeholders can include: Pastoralists, farmers,
herders, women's groups, women farmers, community members, fishermen, youths,
etc. Cooperatives members, farmer groups, women's livestock associations, water
user associations, community councils, slaughterhouse workers, traders, etc.
Veterinarians, para-veterinary professionals, animal health workers, community
animal health workers, faculties and students in veterinary colleges, etc. 8
\n# 4. Good Practice in Animal Health Risk Assessment and Management\n\n#
Approach\nRisk assessment provides the transparent, adequate and objective
evaluation needed by interested parties to make decisions on health-related
risks associated with project activities involving live animals. As the ESF
requires, it is conducted throughout the project cycle, to provide or indicate
likelihood and impact of a given hazard, identify factors that shape the risk,
and find proportionate and appropriate management options. The level of risk
may be reduced by mitigation measures, such as infrastructure (e.g., diagnostic
laboratories, border control posts, quarantine stations), codes of practice
(e.g., good animal husbandry practices, on-farm biosecurity, quarantine,
vaccination), policies and regulations (e.g., rules for importing live animals,
ban on growth hormones and promotors, feed standards, distance required between
farms, vaccination), institutional capacity (e.g., veterinary services,
surveillance and monitoring), changes in individual behavior (e.g., hygiene,
hand washing, care for animals). Annex 2 provides examples of mitigation
practices. This list is not an exhaustive one but a compendium of most
practiced interventions and activities. The cited measures should take into
account social, economic, as well as cultural, gender and occupational aspects,
and other factors that may affect the acceptability of mitigation practices by
project beneficiaries and other stakeholders. Risk assessment is reviewed and
updated through the project cycle (for example to take into account increased
trade and travel connectivity between rural and urban settings and how this may
affect risks of disease occurrence and/or outbreak). Projects monitor changes
in risks (likelihood and impact) b               by using data, triggers or
indicators. ",
       "documentMetadata": {
         "uri":
"gs://table_eval_set/pdf/worldbank/AnimalHealthGoodPracticeNote.pdf",
         "title": "AnimalHealthGoodPracticeNote"
       },
       "pageSpan": {
         "pageStart": 14,
         "pageEnd": 15
       },
       "chunkMetadata": {
         "previousChunks": [
           {
             "name":
"projects/961309680810/locations/global/collections/default_collection/dataStor
es/allie-pdf-adjacent-
chunks_1711394998841/branches/0/documents/0d8619f429d7f20b3575b14cd0ad0813/chun
ks/c16",
             "id": "c16",
             "content": "\n# ESS6: Biodiversity Conservation and Sustainable
Management of Living Natural Resources\nThe risks associated with livestock
interventions under ESS6 include animal welfare (in relation to housing,
transport, and slaughter); diffusion of pathogens from domestic animals to
wildlife, with risks for endemic species and biodiversity (e.g., sheep and goat
plague in Mongolia affecting the saiga, an endemic species of wild antelope);
the introduction of new breeds with potential risk of introducing exotic or new
diseases; and the release of new species that are not endemic with competitive
advantage, potentially putting endemic species at risk of extinction. Animal
welfare relates to how an animal is coping with the conditions in which it
lives. An animal is in a good state of welfare if it is healthy, comfortable,
well nourished, safe, able to express innate behavior, 7 Good Practice Note -
Animal Health and related risks and is not suffering from unpleasant states
such as pain, fear or distress. Good animal welfare requires appropriate animal
care, disease prevention and veterinary treatment; appropriate shelter,
management and nutrition; humane handling, slaughter or culling. The OIE
provides standards for animal welfare on farms, during transport and at the
time of slaughter, for their welfare and for purposes of disease control, in
its Terrestrial and Aquatic Codes. The 2014 IFC Good Practice Note: Improving
Animal Welfare in Livestock Operations is another example of practical guidance
provided to development practitioners for implementation in investments and
operations. Pastoralists rely heavily on livestock as a source of food, income
and social status. Emergency projects to restock the herds of pastoralists
affected by drought, disease or other natural disaster should pay particular
attention to animal welfare (in terms of transport, access to water, feed, and
animal health) to avoid potential disease transmission and ensure humane
treatment of animals. Restocking also entails assessing the assets of
pastoralists and their ability to maintain livestock in good conditions (access
to pasture and water, social relationship, technical knowledge, etc.).
Pastoralist communities also need to be engaged by the project to determine the
type of animals and breed and the minimum herd size to be considered for
restocking. \n# Box 5. Safeguarding the welfare of animals and related risks in
project activities\nIn Haiti, the RESEPAG project (Relaunching Agriculture:
Strengthening Agriculture Public Services) financed housing for goats and
provided technical recommendations for improving their welfare, which is
critical to avoid the respiratory infections, including pneumonia, that are
serious diseases for goats. To prevent these diseases, requires optimal
sanitation and air quality in herd housing. This involves ensuring that
buildings have adequate ventilation and dust levels are reduced to minimize the
opportunity for infection. Good nutrition, water and minerals are also needed
to support the goats' immune function. The project paid particular attention
to: (i) housing design to ensure good ventilation; (ii) locating housing close
to water sources and away from human habitation and noisy areas; (iii)
providing mineral blocks for micronutrients; (iv) ensuring availability of
drinking water and clean food troughs. ",
             "documentMetadata": {
               "uri":
"gs://table_eval_set/pdf/worldbank/AnimalHealthGoodPracticeNote.pdf",
               "title": "AnimalHealthGoodPracticeNote"
             },
             "pageSpan": {
               "pageStart": 13,
               "pageEnd": 14
             }
           }
         ],
         "nextChunks": [
           {
             "name":
"projects/961309680810/locations/global/collections/default_collection/dataStor
es/allie-pdf-adjacent-
chunks_1711394998841/branches/0/documents/0d8619f429d7f20b3575b14cd0ad0813/chun
ks/c18",
             "id": "c18",
             "content": "\n# Scoping of risks\nEarly scoping of risks related
to animal health informs decisions to initiate more comprehensive risk
assessment according to the type of livestock interventions and activities. It
can be based on the following considerations: • • • • Type of livestock
interventions supported by the project (such as expansion of feed resources,
improvement of animal genetics, construction/upgrading and management of post-
farm-gate facilities, etc. – see also Annex 2); Geographic scope and scale of
the livestock interventions; Human and animal populations that are likely to be
affected (farmers, women, children, domestic animals, wildlife, etc.); and
Changes in the project or project context (such as emerging disease outbreak,
extreme weather or climatic conditions) that would require a re-assessment of
risk levels, mitigation measures and their likely effect on risk reduction.
Scenario planning can also help to identify project-specific vulnerabilities,
country-wide or locally, and help shape pragmatic analyses that address single
or multiple hazards. In this process, some populations may be identified as
having disproportionate exposure or vulnerability to certain risks because of
occupation, gender, age, cultural or religious affiliation, socio-economic or
health status. For example, women and children may be the main caretakers of
livestock in the case of 9 Good Practice Note - Animal Health and related risks
household farming, which puts them into close contact with animals and animal
products. In farms and slaughterhouses, workers and veterinarians are
particularly exposed, as they may be in direct contact with sick animals (see
Box 2 for an illustration). Fragility, conflict, and violence (FCV) can
exacerbate risk, in terms of likelihood and impact. Migrants new to a
geographic area may be immunologically naïve to endemic zoonotic diseases or
they may inadvertently introduce exotic diseases; and refugees or internally
displaced populations may have high population density with limited
infrastructure, leaving them vulnerable to disease exposure. Factors such as
lack of access to sanitation, hygiene, housing, and health and veterinary
services may also affect disease prevalence, contributing to perpetuation of
poverty in some populations. Risk assessment should identify populations at
risk and prioritize vulnerable populations and circumstances where risks may be
increased. It should be noted that activities that seem minor can still have
major consequences. See Box 6 for an example illustrating how such small
interventions in a project may have large-scale consequences. It highlights the
need for risk assessment, even for simple livestock interventions and
activities, and how this can help during the project cycle (from concept to
implementation). ",
             "documentMetadata": {
               "uri":
"gs://table_eval_set/pdf/worldbank/AnimalHealthGoodPracticeNote.pdf",
               "title": "AnimalHealthGoodPracticeNote"
             },
             "pageSpan": {
               "pageStart": 15,
               "pageEnd": 16
             }
           }
         ]
       }
     }
   }
 ],
 "totalSize": 61,
 "attributionToken":
"jwHwjgoMCICPjbAGEISp2J0BEiQ2NjAzMmZhYS0wMDAwLTJjYzEtYWQxYS1hYzNlYjE0Mzc2MTQiB0
dFTkVSSUMqUMLwnhXb7Ygtq8SKLa3Eii3d7Ygtj_enIqOAlyLm7Ygtt7eMLduPmiKN96cijr6dFcXL8
xfdj5oi9-yILdSynRWCspoi-eyILYCymiLk7Ygt",
 "nextPageToken":
"ANxYzNzQTMiV2MjFWLhFDZh1SMjNmMtADMwATL5EmZyMDM2YDJaMQv3yagQYAsciPgIwgExEgC",
 "guidedSearchResult": {},
 "summary": {}
}
```

### What's next

Create a first-party data store (/gemini/enterprise/docs/connectors/create-data-store) 

Last updated 2026-10-14 UTC. 



## Create an app

URL: https://docs.cloud.google.com/gemini/enterprise/docs/create-app

This page describes how to create a Gemini Enterprise app. 

**Important:** If you want to use customer-managed encryption keys (CMEK) to protect your app's data, you must register your CMEK key before creating the app. Apps created prior to key registration remain unprotected. For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

**Note:** You can't connect website data stores to your Gemini Enterprise search and assistant apps. 

## Create an app

ConsoleREST (#rest) (#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise page** (https://console.cloud.google.com/gemini-enterprise/start). 

2. On the **Apps** page, click **Create app** . 

3. In the **App name** field, enter a name for your app. 

4. To update the automatically generated app **ID** , click **Edit** . The app ID cannot be updated after you create the app. 

5. In the **Choose a location** section, select a **Multi-region** . Use the default **global (Global)** multi-region unless you need to restrict your data to a specific geography. 

6. Optional. Expand **Advanced options** and configure the following: 

   - a. In the **Company name** field, enter your company's external name, omitting suffixes such as Inc or LLC. This helps the LLM identify the company the app represents. 

- b. If you are connecting a **Google Drive** data store, you can allow the app to search documents outside your organization. To enable this feature, select the **Include cross-domain documents** checkbox. 

**Warning:** Enabling this feature increases security risks, such as prompt injection from external documents and manipulation of search results. 

7. Click **Create** . 

### What's next

- To connect an app to an existing data store, see Connect an app to an existing data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To connect your data sources, see Connect a Google data source (/gemini/enterprise/docs/create-data-store) and Connect a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source). 

- To preview search results, go to **Configurations** > **Search UI** in the Google Cloud console or see Get search results from StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

- To configure the web app, such as to turn on and off settings like the model selector and image generator, see Manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

Last updated 2026-10-14 UTC.
