---
title: CreateEmailRequest
---
## CreateEmailRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **queue_id** | **str** | The ID of the queue to use for routing the chat conversation. | |
| **provider** | **str** | The name of the provider that is sourcing the web chat. | |
| **skill_ids** | **list[str]** | The list of skill ID&#39;s to use for routing. | [optional] |
| **language_id** | **str** | The ID of the langauge to use for routing. | [optional] |
| **priority** | **int** | The priority to assign to the conversation for routing. | [optional] |
| **attributes** | **dict(str, str)** | The list of attributes to associate with the customer participant. | [optional] |
| **to_address** | **str** | The email address of the recipient of the email. | [optional] |
| **to_name** | **str** | The name of the recipient of the email. | [optional] |
| **from_address** | **str** | The email address of the sender of the email. | [optional] |
| **from_name** | **str** | The name of the sender of the email. | [optional] |
| **subject** | **str** | The subject of the email | [optional] |
| **direction** | **str** | Specify INBOUND to create an inbound email conversation to route to a queue, or OUTBOUND to send an email on behalf of a queue. | [optional] |
{: class="table table-striped"}

