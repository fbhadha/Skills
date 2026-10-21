# Gemini Enterprise: user guide, Workflow Builder, developer guide / Get feedback on a pitch to Get search results from StreamAssist
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 289-323, extracted 2026-10-18

Contains:
- Get feedback on a pitch (pages 289-292) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/pitch-feedback
- Generate and refactor code (pages 293-295) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/generate-refactor-code
- Debug and troubleshoot code (pages 296-298) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/debug-troubleshoot-code
- Generate test cases (pages 299-300) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/generate-test-cases
- Optimize performance (pages 301-302) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/optimize-performance
- Resolve IT issues (pages 303-305) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/it-helpdesk-automation
- Streamline onboarding and training (pages 306-307) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/onboarding-training
- Get search results from StreamAssist (pages 308-323) https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist

## Get feedback on a pitch

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/pitch-feedback

Refine pitch decks with feedback on message clarity and to brainstorm potential questions. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Please review the [ATTACHED PITCH] for Cymbal Labs [PRODUCT] for [CUSTOMER]. I
need your feedback on three things:
1. Product & Value Clarity: Does the pitch clearly communicate the product's
value to [CUSTOMER]?
2. Messaging Improvements: What specific parts of the messaging can be improved
for clarity or impact?
3. Anticipated Questions: What questions or objections might [CUSTOMER] have
after reading this?
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

After reviewing your introductory pitch for Apex Pharmaceuticals, here is my feedback on the three areas you requested. 

Overall, this is a very strong, data-driven pitch that effectively communicates a compelling ROI. The feedback below is intended to help you refine it to be even more impactful. 

1. Product & Value Clarity 

The pitch does an excellent job of communicating the product and its value. 

- **Product Clarity: High.** The presentation clearly identifies the product as "Cymbal Labs 'Synapse' R&D Intelligence Platform." Page 3 ("Accelerating Drug Discovery") is particularly effective at explaining what the product does by showing a clear, step-by-step evolution of capabilities from basic literature search to fully predictive, AI-driven research modeling. 

- **Value Clarity: Excellent.** The value proposition is the strongest part of the pitch. It is clear, quantitative, and directly tied to Apex Pharmaceuticals' business objectives. 

   - The **three core value drivers** on page 4 (Accelerated Compound Screening, De-risked Clinical Pathways, Enhanced IP Moat) are concise and powerful. 

   - The **$150M+ pipeline value acceleration** and **5.2x ROI** figures are attention-grabbing and make the value immediately obvious. 

   - The **"Low Break Even" slide (Page 7)** is a brilliant touch, as it effectively minimizes the perceived risk of the investment by showing that only a very small improvement (a 0.5% increase in successful preclinical candidates) is needed to cover the cost. 

2. Messaging Improvements 

The messaging is professional and compelling. Here are a few suggestions to enhance its clarity and impact. 

|Section|Suggested Improvement|Rationale|
|---|---|---|
|Value Drivers<br>(Page 4)|Frame the exclusion of downstream<br>revenue from approved drugs more<br>positively. For example: "This 5.2x ROI is<br>based purely on R&D operational<br>efficiency. Additional value, not included<br>in this calculation, comes from increased<br>patent licensing opportunities and first-<br>mover market advantages."|This turns a disclaimer into an<br>additional selling point,<br>suggesting the true ROI is even<br>higher.|
|"Automated<br>Hypothesis<br>Generation"<br>(Page 3)|Consider renaming "Automated<br>Hypothesis Generation" to something<br>more descriptive of the user benefit, such<br>as "Predictive Molecule Design" or<br>"Intelligent Pathway Modeling."|The term "Automated<br>Hypothesis Generation" might<br>be unfamiliar jargon to a<br>business audience. Focusing on<br>the outcome makes the benefit<br>more immediate and<br>understandable.|
|"Cymbal's<br>proprietary<br>genomic and<br>proteomic<br>datasets" (Page<br>4)|Be prepared to elaborate on this. Consider<br>adding a short, reassuring note like:<br>"...powered by Cymbal's anonymized and<br>ethically sourced clinical trial and<br>molecular data signals."|<br>This is Cymbal's "secret sauce,"<br>but it can also create<br>uncertainty. A brief, proactive<br>clarification can build trust and<br>pre-empt questions about data<br>privacy and usage.|
|Pricing Slide<br>(Page 8)|Move the detailed pricing slide to an<br>appendix. Keep it in your back pocket for<br>the Q&A.|The slide is dense and complex.<br>Introducing it too early can<br>distract from the value<br>proposition you have just built.|

3. Anticipated Questions 

Last updated 2026-10-14 UTC. 



## Generate and refactor code

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/generate-refactor-code

Boost coding productivity by generating or refactoring code. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Can you generate a Python function to parse a JSON file and extract specific
keys? Also, can you refactor the code in the attached file to improve its
readability and efficiency?
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Of course. I can help with both of your requests. 

First, here is a general-purpose Python function to parse a JSON file and extract a list of specified keys. It includes error handling for common issues like a missing file or invalid JSON content. 

#### Function to Parse JSON and Extract Keys

```
import json
def extract_keys_from_json(file_path, keys_to_extract):
   """
   Parses a JSON file and extracts values for a specific list of keys.
   Args:
       file_path (str): The path to the JSON file.
       keys_to_extract (list): A list of strings representing the keys to
extract.
   Returns:
       dict: A dictionary containing the extracted keys and their values.
             Returns an empty dictionary if the file is not found or is
invalid.
   """
   extracted_data = {}
   try:
       with open(file_path, 'r') as f:
           data = json.load(f)
           # ...
```

#### Refactored Code

Here is the refactored version of the `hi.py` file you provided. The primary improvements focus on making the code safer and more readable by removing the deeply nested `if` statements. 

This version uses the `.get()` method, which is a more "Pythonic" way to access dictionary keys that might not exist. It helps avoid `KeyError` exceptions and makes the code flatter and easier to follow. 

```
import json
def update_user_status_refactored(json_data):
   """
   Parses user data, updates status, and handles nested keys safely.
   """
   data = json.loads(json_data)
   # Safely get the email using .get() to avoid errors if keys are missing
   # .get('user', {}) returns an empty dict if 'user' is not found
   email = data.get('user', {}).get('details', {}).get('email')
   if email:
       print(f"Processing user: {email}")
   # Update the user status
   if 'user' in data:
       # ...
```

Last updated 2026-10-14 UTC. 



## Debug and troubleshoot code

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/debug-troubleshoot-code

Resolve code errors faster by debugging and troubleshooting. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I'm getting a NullPointerException in this Java code. Can you analyze the stack
trace, identify the likely cause, and suggest a fix? Can you also help me debug
this issue by simulating different inputs?
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Of course! I can certainly help you with this `NullPointerException` . Let's break down the problem and find a solution. 

#### Analysis of the Error

The stack trace you provided is the key to understanding the issue: 

```
 Exception in thread "main" java.lang.NullPointerException: Cannot invoke
"Address.getStreet()" because the return value of "User.getAddress()" is null
 at MyClass.main(MyClass.java:8)
```

Here's what it means: 

1. **`java.lang.NullPointerException`** : This is the error. It happens when you try to use a reference that hasn't been assigned to an object, meaning it points to `null` . 

2. **`Cannot invoke "Address.getStreet()"`** : The program failed because it tried to call the `getStreet()` method. 

3. **`because the return value of "User.getAddress()" is null`** : This is the crucial part. The method `user.getAddress()` returned `null` , and you cannot call any methods on a `null` reference. 

4. **`at MyClass.main(MyClass.java:8)`** : The error occurred on line 8 in your `MyClass.java` file, which is: `System.out.println("User's street: " + user.getAddress().getStreet());` 

#### Likely Cause

The `NullPointerException` occurs because the `address` field of your `User` object was never initialized. 

1. In `MyClass.java` , you create a `User` object: `User user = new User("Alice");` . 

2. The `User` constructor `public User(String name)` sets the user's `name` but leaves the `address` field as `null` . 

3. When your code executes `user.getAddress()` , it correctly returns the value of the `address` field, which is `null` . 

4. The program then attempts to run `.getStreet()` on that `null` value, causing the crash. 

#### Suggested Fix

To fix this, you need to create an `Address` object and associate it with the `User` object before you try to access it. 

Here is the corrected `MyClass.java` file: 

```
// File: MyClass.java
public class MyClass {
 public static void main(String[] args) {
   // Create a new user
   User user = new User("Alice");
   // Create and set the user's address
   Address address = new Address("123 Main St", "Anytown");
   user.setAddress(address);
   // Now, this line will work correctly
   System.out.println("User's street: " + user.getAddress().getStreet());
 }
}
```

#### Simulating Inputs for Debugging

As you requested, we can simulate different scenarios to understand how to write more robust code. I'll use Python to demonstrate the logic, as it's great for quick simulations. 

Here's a simulation that shows the original problem, the fix, and a defensive check to prevent future crashes.... 

Last updated 2026-10-14 UTC. 



## Generate test cases

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/generate-test-cases

Ensure code reliability by generating comprehensive test cases. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Can you generate a comprehensive set of unit tests for this function, covering
both edge cases and normal scenarios? Also, can you help me create a mock
object for this external dependency?
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Of course! I can help with that. Unit testing is crucial for ensuring your code is reliable, and mocking external dependencies is a key part of that process. 

Below is a comprehensive set of unit tests for your `is_user_eligible_for_promo` function. I've used Python's built-in `unittest` library to create the test suite and `unittest.mock` to create a mock object for the `UserDatabase` . 

#### Mocking the External Dependency

First, let's talk about the mock object. We need to isolate the function we are testing ( `is_user_eligible_for_promo` ) from its external dependency ( `UserDatabase` ). By creating a mock, we can simulate the behavior of the database in a controlled way, allowing us to test how our function reacts to different scenarios without making actual database calls. 

#### The Unit Test Suite

Here is the complete file, including the original code, the mock implementation, and a comprehensive set of unit tests covering normal and edge cases. 

```
import unittest
from unittest.mock import Mock
...
```

Last updated 2026-10-14 UTC. 



## Optimize performance

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/optimize-performance

Improve code efficiency by identifying bottlenecks. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Analyze this code snippet for potential performance bottlenecks. Can you
suggest alternative data structures or algorithms that might be more efficient?
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Of course. I can analyze this code for you and suggest more efficient alternatives. 

#### Performance Analysis

The primary performance bottleneck in your `find_matching_users` function lies in this line: 

```
if user in all_users:
```

When `all_users` is a list, checking for the existence of an element ( `user in all_users` ) requires iterating through the list until a match is found. In the worstcase scenario, this operation has a time complexity of O(n), where 'n' is the number of items in `all_users` . 

Since this check is performed for every `user` in `users_to_check` (let's say it has 'm' items), the total time complexity of the function becomes **O(n * m)** . This can become very inefficient if both lists are large. 

#### Suggested Alternatives

Here are two more efficient approaches to accomplish the same task. 

1. Convert to a Set for Faster Lookups 

You can significantly speed up the lookup process by converting `all_users` into a `set` . Checking for an element's existence in a set is, on average, an O(1) operation. 

This reduces the overall time complexity to roughly O(n + m), which is a massive improvement. 

Last updated 2026-10-14 UTC. 



## Resolve IT issues

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/it-helpdesk-automation

Resolve common IT issues without needing to contact a human technician. This frees IT staff to focus on more complex problems. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I'm having trouble connecting to the company VPN. My password seems to be
correct, but it's not working. Can you help me troubleshoot?
```

Or the following: 

```
I need to request a new software license. What's the process and what
information do I need to provide?
```

### Example output

In response to such a prompt, Gemini Enterprise produces output similar to the following: 

1. Basic Checks 

First, let's rule out the most common and simplest culprits. 

|Step|Action|
|---|---|
|Check for<br>Typos|Carefully re-enter your password. It's easy to make a small mistake. You can try<br>typing it into a text editor like Notepad to see the characters clearly, then copy<br>and paste it into the password field.|
|Verify<br>Username|Double-check that your username or email address is spelled correctly. An error<br>there will cause the login to fail even with the right password.|
|Caps Lock|Ensure that the Caps Lock key is turned off. Passwords are almost always case-<br>sensitive.|
|Virtual|Try using the on-screen or virtual keyboard to enter your password. This can|
|Keyboard|help rule out any issues with your physical keyboard.|

2. Browser and Device Troubleshooting 

Sometimes, the problem isn't the password itself, but the environment you're using to log in. 

|Step|Action|
|---|---|
|Clear Cache and<br>Cookies|Your browser might be holding on to old, incorrect login information.<br>Clearing the cache and cookies can resolve this.|
|Try a Different<br>Browser|Attempt to log in using a different web browser (like Chrome, Firefox, or<br>Safari) or a private/incognito window.|
|Disable<br>Extensions &<br>VPN|Browser extensions or a VPN can sometimes interfere with login processes.<br>Try disabling them temporarily to see if that resolves the issue.|
|Use a Different<br>Device|If possible, try logging in from another device, like your phone or a<br>different computer. This helps determine if the issue is specific to one<br>device.|

3. Account-Specific Issues 

If the basic checks don't work, the issue might be with your account's status. 

Issue Description Account If you've entered the wrong password too many times, your account may be Lockout temporarily locked for security reasons. 

Last updated 2026-10-14 UTC. 



## Streamline onboarding and training

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/onboarding-training

New hires and team members can use Gemini Enterprise to navigate the onboarding process, find answers to common questions about the company or their new role, and access training materials. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I'm a new employee and I need to know where to find the company's
organizational chart and directory.
```

Or the following: 

```
What are the required training modules for all new hires? Can you provide me
with the links to access them?
```

### Example output

In response to such a prompt, Gemini Enterprise produces output similar to the following: 

#### Mandatory Training for All New Hires

All new hires are expected to complete a series of mandatory training modules. These courses cover essential company-wide information and policies. 

|Training Module|Description|
|---|---|
|New Hire Orientation|An introduction to the company's history, mission, values, and<br>culture.|
|Code of Conduct & Policies|Covers the company's code of conduct, anti-bribery and<br>corruption policies, and insider trading policies.|
|Cybersecurity & Data<br>Protection|Training on how to handle sensitive data, identify phishing<br>attempts, and general cybersecurity best practices.|
|Health, Safety & Well-<br>being|Includes general safety procedures, emergency preparedness,<br>and information on promoting a healthy work environment.|
|Harassment &<br>Discrimination Prevention|Mandatory compliance training that addresses the prevention of<br>harassment and discrimination in the workplace.|
|Diversity & Inclusion|Training that promotes a diverse and inclusive workplace.|

Last updated 2026-10-14 UTC. 



## Get search results from StreamAssist

URL: https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist

In your web app, you can get answers to your questions in the form of streaming responses. This document shows you how to use the REST API to get answers. If you want to use the Gemini Enterprise web app, see Chat with the assistant (/gemini/enterprise/docs/assistant-chat). 

`StreamAssist` overview 

`StreamAssist` provides a powerful, interactive way to handle user queries. It operates in a streaming fashion, enabling real-time, back-and-forth interactions. 

The key capabilities of the API include the following: 

- **Maintaining conversational context:** it uses sessions to maintain conversational context, ensuring it understands follow-up queries within the scope of previous interactions. 

- **Incorporating provided files:** it includes the attached files as context for more informed and relevant responses. 

- **Seamless integration:** it integrates with various agents and tools to fulfill a wide range of user requests. 

### Before you begin

Ensure that you have the following: 

The **Discovery Engine API** enabled for your Google Cloud. You can enable it on the **Discovery Engine API** page in the Google Cloud console. 

Go to Discovery Engine API (https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics) 

- A Discovery Engine role (/iam/docs/roles-permissions/discoveryengine) that has the `discoveryengine.assistants.assist` permission assigned to it. 

- An existing Gemini Enterprise app. To create an app, see Create an app (/gemini/enterprise/docs/create-app). 

### Get search results

You can use the `streamAssist` 

(https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/s treamAssist) 

method to query and get answers from Gemini Enterprise. The following curl command lists the mandatory fields. 

RESTPython (#python) (#rest) 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default
_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
 -d '
{
 "query": {
   "text": "QUERY_TEXT_1"
 }
}'
```

Replace the following: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_APP_ID_ : the unique identifier for the Gemini Enterprise app. 

_LOCATION_ : the multi-region of your data store: `global` , `us` , or `eu` 

_QUERY_TEXT_1_ : the search query text. 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant:streamAssist" \
 -d '
{
 "query": {
   "text": "By when do corporations need to file taxes?"
 }
}'
{
 "answer": {
   "name": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/123456789013/assistAnswers/123456789019",
   "state": "SUCCEEDED",
   "replies": [
     {
       "groundedContent": {},
       "replyId": "123456789050"
     },
     {
       "groundedContent": {},
       "replyId": "123456789050"
     }
   ],
   "diagnosticInfo": {
     "plannerSteps": [
       {
         "createTime": "2025-11-24T22:21:13.958569117Z",
         "queryStep": {
           "parts": [
             {
               "text": "By when do corporations need to file taxes?"
             }
           ]
         }
       },
       {
         "createTime": "2025-11-24T22:21:17.218914056Z",
         "planStep": {
           "parts": [
             {
               "text": "**Formulating the Query**\n"
             }
           ],
           "planStepId": "123456789050",
           "role": "MODEL"
         }
       },
       {
         "planStep": {
           "parts": [
             {
               "text": "**Refining the Response**\n"
             }
           ],
           "role": "MODEL",
           "planStepId": "123456789050"
         },
         "createTime": "2025-11-24T22:21:19.734447578Z"
       },
       {
         "createTime": "2025-11-24T22:21:21.940682307Z",
         "planStep": {
           "planStepId": "123456789050",
           "role": "MODEL",
           "parts": [
             {
               "text": "**Processing the Results**\n"
             }
           ]
         }
       },
       {
         "planStep": {
           "role": "MODEL",
           "parts": [
             {
               "text": "**Querying and Analyzing**\n**Structuring the Answer**\n"
             }
           ],
           "planStepId": "123456789050"
         },
         "createTime": "2025-11-24T22:21:25.058155923Z"
       },
       {
         "createTime": "2025-11-24T22:21:25.955761161Z",
         "planStep": {
           "planStepId": "123456789050",
           "role": "MODEL",
           "parts": [
             {
               "text": "**Refining the Details**\n"
             }
           ]
         }
       },
       {
         "createTime": "2025-11-24T22:21:25.967576803Z",
         "planStep": {
           "role": "MODEL",
           "parts": [
             {
               "text": "Of course, I can help with that. The deadline for corporations to
file their federal income tax returns depends on the type of corporation.\n\n### **Corporate
Tax Filing Deadlines**\n\n| Corporation Type | Deadline | For Calendar Year-End (Dec. 31)
|\n| :--- | :--- | :--- |"
             }
           ],
           "planStepId": "123456789050"
         }
       },
       {
         "createTime": "2025-11-24T22:21:25.988820408Z",
         "planStep": {
           "planStepId": "123456789050",
           "role": "MODEL",
           "parts": [
             {
               "text": "\n| **C Corporations** | 15th day of the fourth month after the end
of their fiscal year. | April 15 |\n| **S Corporations** | 15th day of the third month after
the end of their fiscal year. | March 15 |\n\n---\n\n###"
             }
           ]
         }
       },
       {
         "createTime": "2025-11-24T22:21:26.016095651Z",
         "planStep": {
           "planStepId": "123456789050",
           "role": "MODEL",
           "parts": [
             {
               "text": " **Extensions**\n\nIf a corporation needs more time to file, it can
request a six-month extension by filing the appropriate form with the IRS. It's important to
note that an extension to file is not an extension to pay. Taxes are still due by the
original deadline.\n\nWould you like to know about"
             }
           ]
         }
       },
       {
         "planStep": {
           "parts": [
             {
               "text": " the deadlines for any other types of business entities?"
             }
           ],
           "planStepId": "123456789050",
           "role": "MODEL"
         },
         "createTime": "2025-11-24T22:21:26.070810455Z"
       }
     ]
   }
 },
 "sessionInfo": {
   "session": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
   "queryId": "123456789078",
   "turnId": "123456789013_123456789029"
 },
 "assistToken": "1234567890123456789012345678901234567890"
}
```

For more information on the fields and what is returned, see Response body (https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assis tants/streamAssist#response-body) 

**Note:** To continue the conversation in the same session, save the **`session`** value from the response and include it in your next query. 

### Get search results using the same session

To continue a conversation and get answers from Gemini Enterprise within an existing session, use the 

`streamAssist` 

(https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/s treamAssist) 

method. The following code sample shows the mandatory fields: 

RESTPython (#python) (#rest) 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default
_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
 -d '
{
 "session":
"projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sessions
/SESSION_ID",
 "query": {
   "text": "QUERY_TEXT_2"
 }
}'
```

Replace the following: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_APP_ID_ : the unique identifier for the Gemini Enterprise app. 

_LOCATION_ : the multi-region of your data store: `global` , `us` , or `eu` 

_QUERY_TEXT_2_ : the search query text. 

- _SESSION_ID_ : the ID of a session from a previous conversation or query. 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant:streamAssist" \
 -d '
{
 "session": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
 "query": {
   "text": "what are the documents you need to file taxes?"
 }
}'
{
 "answer": {
   "name": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/123456789013/assistAnswers/15195007515750046778",
   "state": "SUCCEEDED",
   "replies": [
     {
       "groundedContent": {},
       "replyId": "123456789051"
     },
     {
       "groundedContent": {},
       "replyId": "123456789051"
     }
   ],
   "diagnosticInfo": {
     "plannerSteps": [
       {
         "queryStep": {
           "parts": [
             {
               "text": "what are the documents you need to file taxes?"
             }
           ]
         },
         "createTime": "2025-11-24T23:06:45.101296577Z"
       },
       {
         "planStep": {
           "role": "MODEL",
           "parts": [
             {
               "text": "**Identifying Tax Documents**\n"
             }
           ],
           "planStepId": "123456789051"
         },
         "createTime": "2025-11-24T23:06:48.201642404Z"
       },
       {
         "planStep": {
           "parts": [
             {
               "text": "**Formulating the Search Strategy**\n"
             }
           ],
           "role": "MODEL",
           "planStepId": "123456789051"
         },
         "createTime": "2025-11-24T23:06:51.081693248Z"
       },
       {
         "createTime": "2025-11-24T23:06:53.884827627Z",
         "planStep": {
           "parts": [
             {
               "text": "**Searching for Information**\n"
             }
           ],
           "role": "MODEL",
           "planStepId": "123456789051"
         }
       },
       {
         "createTime": "2025-11-24T23:06:55.663545003Z",
         "planStep": {
           "role": "MODEL",
           "parts": [
             {
               "text": "**Planning the Response Structure**\n"
             }
           ],
           "planStepId": "123456789051"
         }
       },
       {
         "planStep": {
           "planStepId": "123456789051",
           "parts": [
             {
               "text": "Of course, I can provide a list of the common documents and
information you'll need to file your personal income taxes. Having these ready can make the
process much smoother.\n\n### **Documents for Filing Personal Taxes**\n\n| Category |
Document/Information | Purpose |\n| :--- | :--- | :--- |"
             }
           ],
           "role": "MODEL"
         },
         "createTime": "2025-11-24T23:06:55.687661122Z"
       },
       {
         "planStep": {
           "planStepId": "123456789051",
           "parts": [
             {
               "text": "\n| **Personal Information** | \u003cul\u003e\u003cli\u003eYour
Social Security Number (SSN) or Individual Taxpayer Identification Number
(ITIN)\u003c/li\u003e\u003cli\u003eSSNs or ITINs for your spouse and any
dependents\u003c/li\u003e\u003c/ul\u003e | To identify you and your family members to the
IRS. |\n| **Income Information** | \u003cul\u003e\u003cli\u003e**"
             }
           ],
           "role": "MODEL"
         },
         "createTime": "2025-11-24T23:06:55.713426005Z"
       },
       {
         "planStep": {
           "role": "MODEL",
           "parts": [
             {
               "text": "W-2 forms** from all employers.\u003c/li\u003e\u003cli\u003e**1099
forms** such as 1099-NEC, 1099-DIV, 1099-INT, 1099-G.\u003c/li\u003e\u003cli\u003eRecords of
any other income (business, rental, etc.).\u003c/li\u003e\u003c/ul\u003e | To"
             }
           ],
           "planStepId": "123456789051"
         },
         "createTime": "2025-11-24T23:06:56.158732383Z"
       },
       {
         "createTime": "2025-11-24T23:06:56.700143436Z",
         "planStep": {
           "role": "MODEL",
           "parts": [
             {
               "text": " report all of your income from various sources. |\n| **Deductions
& Credits** | \u003cul\u003e\u003cli\u003eReceipts for charitable
donations.\u003c/li\u003e\u003cli\u003eMedical expense
records.\u003c/li\u003e\u003cli\u003e**Form 1098** (mortgage interest) & **1098-T**
(tuition).\u003c/li\u003e\u003cli\u003eChild"
             }
           ],
           "planStepId": "123456789051"
         }
       },
       {
         "planStep": {
           "planStepId": "123456789051",
           "role": "MODEL",
           "parts": [
             {
               "text": "care expense records.\u003c/li\u003e\u003c/ul\u003e | To reduce
your taxable income and take advantage of tax credits. |\n| **Other Documents** |
\u003cul\u003e\u003cli\u003eLast year's tax return.\u003c/li\u003e\u003cli\u003eBank account
and routing numbers.\u003c/li\u003e\u003c/ul\u003e | For reference and to receive a direct
deposit refund or make a payment. |\n\n---\n\nThis"
             }
           ]
         },
         "createTime": "2025-11-24T23:06:57.410549380Z"
       },
       {
         "planStep": {
           "planStepId": "123456789051",
           "parts": [
             {
               "text": " list covers the most common items, but your specific needs may
vary depending on your financial situation. It's always a good idea to keep your tax-related
documents organized throughout the year.\n\nIs there a specific type of income or deduction
you would like to know more about?"
             }
           ],
           "role": "MODEL"
         },
         "createTime": "2025-11-24T23:06:57.960883085Z"
       }
     ]
   }
 },
 "sessionInfo": {
   "session": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-app/sessions/123456789013",
   "queryId": "123456789057",
   "turnId": "123456789013_123456789072"
 },
 "assistToken": "1234567890123456789012345678901234567890"
}
```

For more information on the fields and what is returned, see Response body (https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assis tants/streamAssist#response-body) 

**Note:** To continue the conversation in the same session, save the **`session`** value from the response and include it in your next query. 

### Upload a file and get search results (Preview)

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

To give the assistant more context, upload a file to a session and then query its content. Follow these steps: 

1. Upload a file to a session using the `addContextFile` 

(https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessio ns/addContextFile) 

method. 

REST 

(#rest) 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/def
ault_collection/engines/APP_ID/sessions/SESSION_ID:addContextFile" \
 -d '
{
 "fileName": "FILE_NAME",
 "mimeType": "MIME_TYPE",
 "fileContents": "BASE64_ENCODED_FILE"
}'
```

Replace the following: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your data store: `global` , `us` , or `eu` 

- _APP_ID_ : the unique identifier for the Gemini Enterprise app. 

- _SESSION_ID_ : the ID of a session from a previous conversation or query. 

- _FILE_NAME_ : the name of the file. 

- _MIME_TYPE_ : the MIME type of the file, for example, `text/plain` or `application/pdf` . For more information on the different media types, see Media Types 

- (https://www.iana.org/assignments/media-types/media-types.xhtml). 

_BASE64_ENCODED_FILE_ : the base64-encoded representation of the file. 

<sup>Example command and result</sup> 

```
Create a sample file to upload
export FILE_NAME="my_test_file.txt"
export FILE_PATH="/tmp/${FILE_NAME}"
echo "This is a sample text file to upload for the Gemini Enterprise assistant." >
"${FILE_PATH}"
echo "It contains a few lines of text." >> "${FILE_PATH}"
Base64 encode the file content
export BASE64_ENCODED_FILE=$(base64 -w 0 "${FILE_PATH}")
#Upload the file to the session using the curl command
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/123456789013:addContextFile" \
 -d '
{
 "fileName": "my_test_file.txt",
 "mimeType": "text/plain",
 "fileContents": "'"$BASE64_ENCODED_FILE"'"
}'
Response
{
 "session": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/123456789013",
 "fileId": "123456789012345",
 "tokenCount": "24"
}
```

For more information on the fields and what is returned, see Response body (https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines .sessions/addContextFile#response-body) 

**Note:** To continue the conversation in the same session, save the **`session`** and the **`fileId`** values from the response and include them in your next query. 

2. Use the same session to ask a question about the file you uploaded using the `streamAssist` (https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines. assistants/streamAssist) 

method. 

REST 

(#rest) 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collection
s/default_collection/engines/APP_ID/assistants/default_assistant:streamAssist" \
 -d '
{
 "session":
"projects/PROJECT_ID/locations/global/collections/default_collection/engines/APP_ID/sess
ions/SESSION_ID",
 "fileIds": ["FILE_ID"],
 "query": {
   "text": "QUERY_TEXT_3"
 }
}'
```

Replace the following: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_APP_ID_ : the unique identifier for the Gemini Enterprise app. 

_LOCATION_ : the multi-region of your data store: `global` , `us` , or `eu` 

_QUERY_TEXT_3_ : the search query text. 

_SESSION_ID_ : the ID of a session from a previous conversation or query. 

_FILE_ID_ : the ID of the file you uploaded to the assistant. 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant:streamAssist" \
 -d '
{
 "session": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/123456789013",
 "fileIds": ["123456789012345"],
 "query": {
   "text": "Repeat the text in the file"
 }
}'
{
 "answer": {
   "name": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/123456789013/assistAnswers/123456789065",
   "state": "SUCCEEDED",
   "replies": [
     {
       "groundedContent": {},
       "replyId": "123456789009"
     },
     {
       "groundedContent": {},
       "replyId": "717422098702389109"
     }
   ],
   "diagnosticInfo": {
     "plannerSteps": [
       {
         "createTime": "2025-11-26T03:56:30.270018719Z",
         "queryStep": {
           "parts": [
             {
               "text": "repeat the text in the file"
             },
             {}
           ]
         }
       },
       {
         "createTime": "2025-11-26T03:56:32.976071976Z",
         "planStep": {
           "role": "MODEL",
           "planStepId": "717422098702389109",
           "parts": [
             {
               "text": "**Addressing the Repetition**\n"
             }
           ]
         }
       },
       {
         "createTime": "2025-11-26T03:56:35.390573666Z",
         "planStep": {
           "planStepId": "717422098702389109",
           "parts": [
             {
               "text": "**Identifying User Intent**\n"
             }
           ],
           "role": "MODEL"
         }
       },
       {
         "createTime": "2025-11-26T03:56:37.586889807Z",
         "planStep": {
           "planStepId": "717422098702389109",
           "parts": [
             {
               "text": "**Analyzing the Repetition**\n"
             }
           ],
           "role": "MODEL"
         }
       },
       {
         "createTime": "2025-11-26T03:56:37.611172643Z",
         "planStep": {
           "parts": [
             {
               "text": "Of course. The text in the file `my_test_file.txt` is:\n\nThis
is a sample text file to upload for the Gemini Enterprise assistant.\nIt contains a few
lines of text.\n\nIs there anything else I can assist you with?"
             }
           ],
           "role": "MODEL",
           "planStepId": "717422098702389109"
         }
       }
     ]
   }
 },
 "sessionInfo": {
   "session": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions/8715627784376195363",
   "queryId": "2129985467851228910",
   "turnId": "8715627784376195363_2129985467851230549"
 },
 "assistToken":
"NMwKDAjt9JnJBhCGypGkARIkNjkyMWQzZjktMDAwMC0yM2UyLWJlMjAtNTgyNDI5YTdhOTYw"
}
```

For more information on the fields and what is returned, see Response body (https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines .assistants/streamAssist#response-body) 

Last updated 2026-10-14 UTC.
