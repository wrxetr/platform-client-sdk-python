---
title: CallbackMediaParticipant
---
## CallbackMediaParticipant

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The unique participant ID. | [optional] |
| **name** | **str** | The display friendly name of the participant. | [optional] |
| **address** | **str** | The participant address. | [optional] |
| **start_time** | **datetime** | The time when this participant first joined the conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **connected_time** | **datetime** | The time when this participant went connected for this media (eg: video connected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **end_time** | **datetime** | The time when this participant went disconnected for this media (eg: video disconnected time). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **start_hold_time** | **datetime** | The time when this participant&#39;s hold started. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **purpose** | **str** | The participant&#39;s purpose.  Values can be: &#39;agent&#39;, &#39;user&#39;, &#39;customer&#39;, &#39;external&#39;, &#39;acd&#39;, &#39;ivr | [optional] |
| **state** | **str** | The participant&#39;s state.  Values can be: &#39;alerting&#39;, &#39;connected&#39;, &#39;disconnected&#39;, &#39;dialing&#39;, &#39;contacting | [optional] |
| **direction** | **str** | The participant&#39;s direction.  Values can be: &#39;inbound&#39; or &#39;outbound&#39; | [optional] |
| **disconnect_type** | **str** | The reason the participant was disconnected from the conversation. | [optional] |
| **held** | **bool** | Value is true when the participant is on hold. | [optional] |
| **wrapup_required** | **bool** | Value is true when the participant requires wrap-up. | [optional] |
| **wrapup_prompt** | **str** | The wrap-up prompt indicating the type of wrap-up to be performed. | [optional] |
| **user** | [**UriReference**](UriReference.html) | The PureCloud user for this participant. | [optional] |
| **queue** | [**UriReference**](UriReference.html) | The PureCloud queue for this participant. | [optional] |
| **attributes** | **dict(str, str)** | A list of ad-hoc attributes for the participant. | [optional] |
| **error_info** | [**ErrorBody**](ErrorBody.html) | If the conversation ends in error, contains additional error details. | [optional] |
| **script** | [**UriReference**](UriReference.html) | The Engage script that should be used by this participant. | [optional] |
| **wrapup_timeout_ms** | **int** | The amount of time the participant has to complete wrap-up. | [optional] |
| **wrapup_skipped** | **bool** | Value is true when the participant has skipped wrap-up. | [optional] |
| **provider** | **str** | The source provider for the communication. | [optional] |
| **external_contact** | [**UriReference**](UriReference.html) | If this participant represents an external contact, then this will be the reference for the external contact. | [optional] |
| **external_organization** | [**UriReference**](UriReference.html) | If this participant represents an external org, then this will be the reference for the external org. | [optional] |
| **wrapup** | [**Wrapup**](Wrapup.html) | Wrapup for this participant, if it has been applied. | [optional] |
| **outbound_preview** | [**DialerPreview**](DialerPreview.html) | The outbound preview associated with this callback. | [optional] |
| **callback_numbers** | **list[str]** | The list of phone number to use for this callback. | [optional] |
| **callback_user_name** | **str** | The name of the callback target. | [optional] |
| **skip_enabled** | **bool** | If true, the callback can be skipped | [optional] |
| **timeout_seconds** | **int** | Duration in seconds before the callback will be auto-dialed. | [optional] |
| **automated_callback_config_id** | **str** | The id of the config for automatically placing the callback (and handling the disposition). If absent, the callback will not be placed automatically but routed to an agent as per normal. | [optional] |
| **callback_scheduled_time** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
{: class="table table-striped"}

