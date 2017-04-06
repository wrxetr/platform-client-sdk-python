---
title: CobrowseConversationNotificationCobrowseMediaParticipant
---
## CobrowseConversationNotificationCobrowseMediaParticipant

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
| **user** | [**DocumentDataV2NotificationCreatedBy**](DocumentDataV2NotificationCreatedBy.html) |  | [optional] |
| **queue** | [**CobrowseConversationNotificationUriReference**](CobrowseConversationNotificationUriReference.html) |  | [optional] |
| **attributes** | **dict(str, str)** |  | [optional] |
| **error_info** | [**CobrowseConversationNotificationErrorInfo**](CobrowseConversationNotificationErrorInfo.html) |  | [optional] |
| **script** | [**CobrowseConversationNotificationUriReference**](CobrowseConversationNotificationUriReference.html) |  | [optional] |
| **wrapup_timeout_ms** | **int** |  | [optional] |
| **wrapup_skipped** | **bool** |  | [optional] |
| **provider** | **str** |  | [optional] |
| **external_contact** | [**CobrowseConversationNotificationUriReference**](CobrowseConversationNotificationUriReference.html) |  | [optional] |
| **external_organization** | [**CobrowseConversationNotificationUriReference**](CobrowseConversationNotificationUriReference.html) |  | [optional] |
| **wrapup** | [**ConversationNotificationWrapup**](ConversationNotificationWrapup.html) |  | [optional] |
| **cobrowse_session_id** | **str** |  | [optional] |
| **cobrowse_role** | **str** |  | [optional] |
| **viewer_url** | **str** |  | [optional] |
| **provider_event_time** | **datetime** |  | [optional] |
| **controlling** | **list[str]** |  | [optional] |
{: class="table table-striped"}

