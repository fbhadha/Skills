# Google Workspace Admin SDK Reports API / Gemini in Workspace Apps Activity Events
Source: https://developers.google.com/workspace/admin/reports/v1/appendix/activity/gemini-in-workspace-apps, page last updated 2026-09-22, extracted 2026-10-19

This document lists the events and parameters for
various types of
Gemini in Workspace Apps activity events. You can retrieve these events by
calling [Activities.list()](https://developers.google.com/workspace/admin/reports/v1/reference/activities/list)
with `applicationName=gemini_in_workspace_apps`.

Note: 'Gemini in Workspace apps' logs will be available starting 2025-06-20T00:00:00Z. From this date forward, a rolling history of up to 180 days will be maintained.

## Gemini in Workspace Apps Utilization Event

Event type for usage related events.
Events of this type are returned with `type=ai_usage_event`.

### Gen AI Usage

Event is triggered when a user performs an action that uses Gemini in any of the Workspace apps.

**Event details**

**Event name**

`feature_utilization`

**Parameters**

**action**

`string`

Action performed by the user within a Workspace application, initiated or assisted by Gemini.
Possible values:

- `add_to_calendar`
  Gmail: User added an event extracted from their email to their calendar using Gemini.
- `auto_proofread`
  Gmail: Use case for polishing a draft inline at a minimum of sentence level granularity. It provides proactive suggestions to improve draft quality.
- `bulletize`
  Slides: Corresponds to "Bulletize" button in Help me Write entrypoint under textbox. Gemini returns the selected text organized into bullet points.
- `classic_use_case_convert_rubric`
  Classroom: User clicks on "+Rubric", then "Convert from file" on the Assignment creation page, which uploads a grading rubric based on the input Drive file.
- `classic_use_case_generate_audio_lesson`
  Classroom: User clicks on the "Generate audio lesson" button, which generates an audio lesson, including a Slides presentation of the transcript, based on the input grade, topic or content.
- `classic_use_case_generate_choice_board`
  Classroom: User clicks on the "Generate" button on the Build a choice board page, which generates a board of sample student exercises based on the input grade, topic & instructional materials.
- `classic_use_case_generate_common_misconceptions`
  Classroom: User clicks on the "Generate" button on the Tackle common misconceptions page, which generates a list of common issues that students face, based on the input grade & topic.
- `classic_use_case_generate_feedback`
  Classroom: User clicks on the "Help me write" on the assignment grading page, which generates a comment about the student's submission, based on the input grade and feedback topic.
- `classic_use_case_generate_hooks`
  Classroom: User clicks on the "Generate" button on the Craft a compelling hook page, which generates a short student exercise, based on the input grade, lesson & instructional materials.
- `classic_use_case_generate_informative_articles`
  Classroom: User clicks on the "Generate" button on the Write an informational text page, which generates text that describes the input topic, appropriate for the input grade level.
- `classic_use_case_generate_lesson_plan`
  Classroom: User clicks "Generate lesson plan" button, which generates a lesson plan based on input grade, topic & instructional materials.
- `classic_use_case_generate_presentation`
  Classroom: User clicks "Generate presentation outline" button, which generates a Slides presentation, based on input grade, topic & presentation length.
- `classic_use_case_generate_project_activities`
  Classroom: User clicks on "Generate project" button, which generates several individual or group project ideas, based on the input grade, topic & instructional materials.
- `classic_use_case_generate_questions`
  Classroom: User clicks on "Generate questions" button, which generates a list of questions, based on the input grade, topic & question type.
- `classic_use_case_generate_rubric`
  Classroom: User clicks on "Generate criteria" button on the Create a rubric page, which generates a grading rubric based on the input grade, performance level and assignment instructions.
- `classic_use_case_generate_story`
  Classroom: User clicks on the "Generate" button on the Write a story page, which generates a short story, based on the input grade, topic & keywords.
- `classic_use_case_generate_text_dependent_questions`
  Classroom: User clicks on "Generate questions" button on the Develop reading comprehension questions page, which generates a list of questions, based on the input grade, question type, reading skills & text prompt.
- `classic_use_case_generate_vocab_list`
  Classroom: User clicks on the "Generate" button on the Create a vocabulary list, which generates a list of vocabulary words & definitions, based on the input grade, topic & instructional materials.
- `classic_use_case_meet_studio_lighting`
  Meet: Improves user's video in poor lighting conditions and allows users to use virtual light sources for more fine grained control.
- `classic_use_case_meet_studio_look`
  Meet: Sharpens the user features when needed.
- `classic_use_case_meet_studio_sound`
  Meet: Improves the audio quality when needed. Notably when using a Bluetooth narrowband microphone.
- `classic_use_case_meet_take_notes_for_me_session`
  Meet: Generates a doc for meetings when Take notes for me feature was used.
- `classic_use_case_relevel_content`
  Classroom: User clicks on the "Generate" button on the Re-level text page, which generates an updated version of their specified text, appropriate for the input grade.
- `classic_use_case_sheets_turbofill`
  Sheets: User accepts a proactive suggestion to populate a column with text data based on another column in their table.
- `classic_use_case_suggest_time_reporting`
  Gmail: User accepted a Gemini-generated suggestion for a time to offer when scheduling a meeting using "Help me schedule" while composing a mail.
- `classic_use_case_teleprompter_word_match`
  Vids: Used for Recording Studio smart teleprompter, to match words from a script to a user's speech in real-time using a speech-to-text model.
- `classic_use_case_translate_text`
  Classroom: User clicks on the "Translate" button on the Translate text page, which translates the input text into the selected language.
- `condense`
  - Gmail: Shortens draft's content when the user clicks "shorten" in the refinement menu.
  - Slides: Corresponds to "Shorten" button in Help me Write entrypoint under textbox. Gemini returns a shortened version of the selected textbox..
- `conversation`
  A prompt is submitted to the Gemini side panel. This can be initiated by the user directly or by another feature on the user's behalf (e.g., an on-grid suggestion).
- `custom_prompt`
  Slides: Corresponds to "Modify with a prompt" input in Help me Write entrypoint under textbox. Gemini returns a reworded version of the selected textbox according to the user's prompt.
- `describe_gemini_uses`
  - Chat: Describes Gemini uses in context in the sidepanel.
  - Meet: "What can Gemini do in Google Meet" in Side Panel.
  - Sheets: User asks Gemini to describe its capabilities or suggest ways to use the feature..
- `elaborate`
  Gmail: Expands draft's content when the user clicks "elaborate" in the refinement menu.
- `formalize`
  - Gmail: Formalizes content of the draft when user clicks "formalize" in the refinement menu.
  - Slides: Corresponds to "More formal" button in Help me Write entrypoint under textbox. Gemini returns a reworded version of the selected textbox that's more formal in tone..
- `generate_ai_function_response`
  Sheets: Gemini generates content directly in a cell or range. This is triggered when a user manually enters the =AI() function or uses a feature that generates content on the grid on their behalf.
- `generate_avatar_video`
  Vids: Generates a video of a digital avatar when a user provides a script and clicks "Generate" in the AI avatar sidebar.
- `generate_document`
  - Vids: Generates a Google Vid based on a prompt, any attached files, a generated outline and a supported template from the Getting Started dialog.
  - Slides: Generates a Google Slides deck based on a prompt, and any provided sources and styles, from the Getting Started dialog..
- `generate_form`
  Forms: Generates a form based on user prompt; triggered when the user clicks "Create" in the "Help me create" dialog. The dialog is visible when creating a new form or alternatively when user clicks the "Help me create" button.
- `generate_form_questions`
  Forms: Generates more questions for the existing form when "Suggest questions" button is clicked; the button is shown for unpublished forms, when it already has some content (non default title and 2 questions minimum).
- `generate_image_for_current_page`
  Slides: No-prompt image generation for slides. User enters a prompt like "suggest an image for this slide". Gemini first generates the image prompt, and then uses it to generate images to return to the user.
- `generate_images_in_product`
  - Vids: Generates an image when a user enters a text prompt and clicks "Create" in the "Generate an image" sidebar.
  - Meet: Triggers from side panel, user inputs text prompt and clicks on "Create Samples" button; Meet will use the input text prompt to generate a few images which the user can use as their visual background image.
  - Slides: User clicks "Help Me Visualize" entry point in slides; Image Model returns the generated images to the user..
- `generate_nudge_prompts`
  Sheets: Gemini proactively suggests features or prompts for the user to try via on-grid suggestion.
- `generate_starter_active_view`
  Gemini generates suggested starter prompts to users that utilizes active context.
- `generate_starter_freeform`
  Generates response when starter tiles are clicked.
- `generate_starter_tile_prompts`
  Gemini displays initial, semi-contextual starter prompts as tiles in the side panel to help users get started.
- `generate_table_name`
  Sheets: Gemini automatically adds a table name (based on the table contents) for a newly converted table from a table conversion suggestion.
- `generate_text`
  Gmail: Generates a smart draft when user clicks "create" on Help me write prompt input.
- `generate_videos_in_product`
  Vids: Generates a video when a user enters a text prompt in the "AI video clip" sidebar.
- `live_generate_document`
  Docs: Generate document from live conversation with user.
- `outpaint`
  Vids: Generates an expanded version of a selected image, extending beyond its original borders, when a user requests outpainting in their prompt and clicks "Create" in the "Generate an image" sidebar.
- `paraphrase`
  Slides: Corresponds to "Rephrase" button in Help me Write entrypoint under textbox. Gemini returns the selected text reworded in a different way.
- `proactive_daily_briefs`
  Generates a proactive daily brief for the user in Chat.
- `proactive_suggestions`
  Generates text for proactive suggestion tiles based on context.
- `proactive_suggestions_response`
  User selected a proactive suggestion to try in Gemini sidepanel and a response was generated.
- `proofread`
- `remove_background`
  Vids: Removes the background from a selected image, making it transparent, when a user clicks on the "Remove background" button in the image floating toolbar.
- `replace_background`
  Vids: Replaces background for a selected image when a user provides a prompt describing the new background and clicks "Create" in the "Generate an image" sidebar.
- `search_web`
  User searched the web using Gemini sidepanel.
- `suggest_time`
  Calendar: Requested time suggestions for a meeting.
- `summarize`
  Gemini summarizes current context.
- `summarize_document_comment_thread`
  Summarize a comment thread in a document.
- `summarize_drive_homepage_doclist_files`
  Shows a short file summary inline in the Drive Homepage file list.
- `summarize_drive_homepage_doclist_files_long`
  Shows a longer file summary when user clicks on 'See Details' in the Drive Homepage file list.
- `summarize_file`
  Chat: Generates a summary of a file in chat side panel when the user clicks the summarize button on a Drive file preview card in the chat UI.
- `summarize_proactive`
  Gemini proactively generates and displays a summary of the detected active content when the side panel is opened.
- `summarize_proactive_short`
  Gemini generates a short proactive summary or title for the user's content.
- `user_confirmed_tools_operation`
  User clicks on buttons that come up in the sidepanel to confirm the operation during a conversation.

**app\_ name**

`string`

Name of the Workspace application through which the action was performed.
Possible values:

- `gemini_app`
- `chat`
- `classroom`
- `docs`
- `drive`
- `gmail`
- `keep`
- `meet`
- `sheets`
- `slides`
- `vids`

**event\_ category**

`string`

Event Category Name indicates the type of the generative AI action.
Possible values:

- `active_conversations`
  Represents a conversation with Gemini.
- `active_generate`
  Represents Gemini’s generation capabilities - Example: GENERATE\_IMAGES or GENERATE\_SLIDES.
- `active_summarize`
  Represents Gemini’s summarization capabilities Ex: SUMMARIZE\_THREAD.
- `active_unspecified`
  Represents a category that is neither generate nor summarize.
- `inactive`
  Represents a category where the user is not considered to be actively engaging with Gemini; that is not counted towards active usage.
- `unknown`
  Represents a category that is not classified.

**feature\_ source**

`string`

Identifies where a generative AI interaction originates within the user interface.
Possible values:

- `ai_function`
- `ask_gemini`
  Ask Gemini in Chat.
- `chat_with_gemini`
- `classroom_gemini_education`
- `drive_help_me_organize`
- `enhanced_smart_fill`
- `generate_background`
- `help_me_refine`
- `help_me_schedule`
- `help_me_visualize`
- `help_me_write`
- `proofread`
- `remove_image_background`
- `search_ai_overview`
- `side_panel`
- `studio_light`
- `studio_look`
- `studio_sound`
- `take_notes_for_me`
- `workflows_creation`
- `workflows_execution`

**Sample request**

`GET https://admin.googleapis.com/admin/reports/v1/activity/users/all/applications/gemini_in_workspace_apps?eventName=feature_utilization&maxResults=10&access_token=YOUR_ACCESS_TOKEN`

**Admin Console message format**

`{actor} used Gen AI in {app_name}`
