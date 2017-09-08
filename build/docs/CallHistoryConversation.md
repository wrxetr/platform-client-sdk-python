---
title: CallHistoryConversation
---
## CallHistoryConversation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **participants** | [**list[CallHistoryParticipant]**](CallHistoryParticipant.html) | The list of participants involved in the conversation. | [optional] |
| **direction** | **str** | The direction of the call relating to the current user | [optional] |
| **went_to_voicemail** | **bool** | Did the call end in the current user&#39;s voicemail | [optional] |
| **missed_call** | **bool** | Did the user not answer this conversation | [optional] |
| **start_time** | **datetime** | The time the user joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **was_conference** | **bool** | Was this conversation a conference | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

