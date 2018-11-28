---
title: ConversationEmailEventTopicEmailMediaParticipant
---
## ConversationEmailEventTopicEmailMediaParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **name** | **str** |  | [optional] |
| **address** | **str** |  | [optional] |
| **start_time** | **datetime** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **end_time** | **datetime** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **purpose** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **direction** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **wrapup_required** | **bool** |  | [optional] |
| **wrapup_prompt** | **str** |  | [optional] |
| **user** | [**ConversationEmailEventTopicUriReference**](ConversationEmailEventTopicUriReference.html) |  | [optional] |
| **queue** | [**ConversationEmailEventTopicUriReference**](ConversationEmailEventTopicUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**ConversationEmailEventTopicErrorBody**](ConversationEmailEventTopicErrorBody.html) |  | [optional] |
| **script** | [**ConversationEmailEventTopicUriReference**](ConversationEmailEventTopicUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **alerting_timeout_ms** | **int** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**ConversationEmailEventTopicUriReference**](ConversationEmailEventTopicUriReference.html) |  | [optional] |
| **external_organization** | [**ConversationEmailEventTopicUriReference**](ConversationEmailEventTopicUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationEmailEventTopicWrapup**](ConversationEmailEventTopicWrapup.html) |  | [optional] |
| **peer** | **str** |  | [optional] |
| **screen_recording_state** | **str** |  | [optional] |
| **flagged_reason** | **str** |  | [optional] |
| **subject** | **str** |  | [optional] |
| **messages_sent** | **int** |  | [optional] |
| **auto_generated** | **bool** |  | [optional] |
| **message_id** | **str** |  | [optional] |
| **draft_attachments** | [**list[ConversationEmailEventTopicAttachment]**](ConversationEmailEventTopicAttachment.html) |  | [optional] |
{: class="table table-striped"}

