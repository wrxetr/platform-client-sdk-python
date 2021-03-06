---
title: ConversationChat
---
## ConversationChat

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **state** | **str** | The connection state of this communication. | [optional] |
| **id** | **str** | A globally unique identifier for this communication. | [optional] |
| **room_id** | **str** | The room id for the chat. | [optional] |
| **recording_id** | **str** | A globally unique identifier for the recording associated with this chat. | [optional] |
| **segments** | [**list[Segment]**](Segment.html) | The time line of the participant&#39;s chat, divided into activity segments. | [optional] |
| **held** | **bool** | True if this call is held and the person on this side hears silence. | [optional] |
| **direction** | **str** | The direction of the chat | [optional] |
| **disconnect_type** | **str** | System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects. | [optional] |
| **start_hold_time** | **datetime** | The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **start_alerting_time** | **datetime** | The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **disconnected_time** | **datetime** | The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **provider** | **str** | The source provider for the email. | [optional] |
| **script_id** | **str** | The UUID of the script to use. | [optional] |
| **peer_id** | **str** | The id of the peer communication corresponding to a matching leg for this communication. | [optional] |
| **avatar_image_url** | **str** | If available, the URI to the avatar image of this communication. | [optional] |
| **journey_context** | [**JourneyContext**](JourneyContext.html) | A subset of the Journey System&#39;s data relevant to a part of a conversation (for external linkage and internal usage/context). | [optional] |
{: class="table table-striped"}


