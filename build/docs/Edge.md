---
title: Edge
---
## Edge

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
| **interfaces** | [**list[EdgeInterface]**](EdgeInterface.html) |  | [optional] |
| **make** | **str** |  | [optional] |
| **model** | **str** |  | [optional] |
| **api_version** | **str** |  | [optional] |
| **software_version** | **str** |  | [optional] |
| **software_version_timestamp** | **str** |  | [optional] |
| **software_version_platform** | **str** |  | [optional] |
| **software_version_configuration** | **str** |  | [optional] |
| **full_software_version** | **str** |  | [optional] |
| **pairing_id** | **str** | The pairing Id for a hardware Edge in the format: 00000-00000-00000-00000-00000. This field is only required when creating an Edge with a deployment type of HARDWARE. | [optional] |
| **fingerprint** | **str** |  | [optional] |
| **fingerprint_hint** | **str** |  | [optional] |
| **current_version** | **str** |  | [optional] |
| **staged_version** | **str** |  | [optional] |
| **patch** | **str** |  | [optional] |
| **status_code** | **str** |  | [optional] |
| **edge_group** | [**EdgeGroup**](EdgeGroup.html) |  | [optional] |
| **site** | [**Site**](Site.html) | The Site to which the Edge is assigned. | [optional] |
| **software_status** | [**DomainEdgeSoftwareUpdateDto**](DomainEdgeSoftwareUpdateDto.html) |  | [optional] |
| **online_status** | **str** |  | [optional] |
| **serial_number** | **str** |  | [optional] |
| **physical_edge** | **bool** |  | [optional] |
| **managed** | **bool** |  | [optional] |
| **edge_deployment_type** | **str** |  | [optional] |
| **call_draining_state** | **str** |  | [optional] |
| **conversation_count** | **int** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

