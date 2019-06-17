---
title: ScimV2CreateUser
---
## ScimV2CreateUser

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **display_name** | **str** | Display Name | |
| **schemas** | **list[str]** | schemas supported | [optional] |
| **active** | **bool** | Active flag | [optional] |
| **user_name** | **str** | User Name (Must be Unique) maps to PureCloud e-mail address | |
| **password** | **str** | Password (updateOnly) | [optional] |
| **title** | **str** | Title | [optional] |
| **phone_numbers** | [**list[ScimPhoneNumber]**](ScimPhoneNumber.html) | Phone numbers | [optional] |
| **emails** | [**list[ScimEmail]**](ScimEmail.html) | Emails | [optional] |
| **photos** | [**list[Photo]**](Photo.html) | Photos | [optional] |
| **groups** | [**list[ScimV2GroupReference]**](ScimV2GroupReference.html) | Group References | [optional] |
| **meta** | [**ScimMetadata**](ScimMetadata.html) | Resource SCIM meta | [optional] |
| **urnietfparamsscimschemasextensionenterprise2_0_user** | [**ScimV2EnterpriseUser**](ScimV2EnterpriseUser.html) |  | [optional] |
{: class="table table-striped"}

