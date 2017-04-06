---
title: TrunkBase
---
## TrunkBase

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of the entity. | |
| **description** | **str** |  | [optional] |
| **version** | **int** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | **str** |  | [optional] |
| **created_by** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **modified_by_app** | **str** |  | [optional] |
| **created_by_app** | **str** |  | [optional] |
| **trunk_metabase** | [**UriReference**](UriReference.html) | The meta-base this trunk is based on. | |
| **properties** | **dict(str, object)** |  | [optional] |
| **trunk_type** | **str** | The type of this trunk base. | |
| **managed** | **bool** | Is this trunk being managed remotely. This property is synchronized with the managed property of the Edge Group to which it is assigned. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

