---
title: QueueMediaAssociation
---
## QueueMediaAssociation

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The reference ID for this QueueMediaAssociation | [optional] |
| **queue** | [**QueueReference**](QueueReference.html) | The queue to associate with the service goal group | [optional] |
| **media_types** | **list[str]** | The media types of the given queue to associate with the service goal group | [optional] |
| **delete** | **bool** | If marked true on a PATCH, this QueueMediaAssociation will be permanently deleted | [optional] |
{: class="table table-striped"}


