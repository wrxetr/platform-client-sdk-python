---
title: ReportingExportJobRequest
---
## ReportingExportJobRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **name** | **str** | The user supplied name of the export request | |
| **time_zone** | **str** | The requested timezone of the exported data. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London | |
| **export_format** | **str** | The requested format of the exported data | |
| **interval** | **str** | The time period used to limit the the exported data. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **period** | **str** | The Period of the request in which to break down the intervals. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H | |
| **view_type** | **str** | The type of view export job to be created | |
| **filter** | [**ViewFilter**](ViewFilter.html) | Filters to apply to create the view | |
| **read** | **bool** | Indicates if the request has been marked as read | [optional] |
| **locale** | **str** | The locale use for localization of the exported data, i.e. en-us, es-mx   | |
| **has_format_durations** | **bool** | Indicates if durations are formatted in hh:mm:ss format instead of ms | [optional] |
| **has_split_filters** | **bool** | Indicates if filters will be split in aggregate detail exports | [optional] |
| **selected_columns** | [**list[SelectedColumns]**](SelectedColumns.html) | The list of ordered selected columns from the export view by the user | [optional] |
| **has_custom_participant_attributes** | **bool** | Indicates if custom participant attributes will be exported | [optional] |
{: class="table table-striped"}


