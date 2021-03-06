---
title: ViewFilter
---
## ViewFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_types** | **list[str]** | The media types are used to filter the view | [optional] |
| **queue_ids** | **list[str]** | The queue ids are used to filter the view | [optional] |
| **skill_ids** | **list[str]** | The skill ids are used to filter the view | [optional] |
| **skill_groups** | **list[str]** | The skill groups used to filter the view | [optional] |
| **language_ids** | **list[str]** | The language ids are used to filter the view | [optional] |
| **language_groups** | **list[str]** | The language groups used to filter the view | [optional] |
| **directions** | **list[str]** | The directions are used to filter the view | [optional] |
| **originating_directions** | **list[str]** | The list of orginating directions used to filter the view | [optional] |
| **wrap_up_codes** | **list[str]** | The wrap up codes are used to filter the view | [optional] |
| **dnis_list** | **list[str]** | The dnis list is used to filter the view | [optional] |
| **session_dnis_list** | **list[str]** | The list of session dnis used to filter the view | [optional] |
| **filter_queues_by_user_ids** | **list[str]** | The user ids are used to fetch associated queues for the view | [optional] |
| **filter_users_by_queue_ids** | **list[str]** | The queue ids are used to fetch associated users for the view | [optional] |
| **user_ids** | **list[str]** | The user ids are used to filter the view | [optional] |
| **address_tos** | **list[str]** | The address To values are used to filter the view | [optional] |
| **address_froms** | **list[str]** | The address from values are used to filter the view | [optional] |
| **outbound_campaign_ids** | **list[str]** | The outbound campaign ids are used to filter the view | [optional] |
| **outbound_contact_list_ids** | **list[str]** | The outbound contact list ids are used to filter the view | [optional] |
| **contact_ids** | **list[str]** | The contact ids are used to filter the view | [optional] |
| **external_contact_ids** | **list[str]** | The external contact ids are used to filter the view | [optional] |
| **external_org_ids** | **list[str]** | The external org ids are used to filter the view | [optional] |
| **ani_list** | **list[str]** | The ani list ids are used to filter the view | [optional] |
| **durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The durations in milliseconds used to filter the view | [optional] |
| **acd_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The acd durations in milliseconds used to filter the view | [optional] |
| **talk_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The talk durations in milliseconds used to filter the view | [optional] |
| **acw_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The acw durations in milliseconds used to filter the view | [optional] |
| **handle_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The handle durations in milliseconds used to filter the view | [optional] |
| **hold_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The hold durations in milliseconds used to filter the view | [optional] |
| **abandon_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The abandon durations in milliseconds used to filter the view | [optional] |
| **evaluation_score** | [**NumericRange**](NumericRange.html) | The evaluationScore is used to filter the view | [optional] |
| **evaluation_critical_score** | [**NumericRange**](NumericRange.html) | The evaluationCriticalScore is used to filter the view | [optional] |
| **evaluation_form_ids** | **list[str]** | The evaluation form ids are used to filter the view | [optional] |
| **evaluated_agent_ids** | **list[str]** | The evaluated agent ids are used to filter the view | [optional] |
| **evaluator_ids** | **list[str]** | The evaluator ids are used to filter the view | [optional] |
| **transferred** | **bool** | Indicates filtering for transfers | [optional] |
| **abandoned** | **bool** | Indicates filtering for abandons | [optional] |
| **message_types** | **list[str]** | The message media types used to filter the view | [optional] |
| **division_ids** | **list[str]** | The divison Ids used to filter the view | [optional] |
| **survey_form_ids** | **list[str]** | The survey form ids used to filter the view | [optional] |
| **survey_total_score** | [**NumericRange**](NumericRange.html) | The survey total score used to filter the view | [optional] |
| **survey_nps_score** | [**NumericRange**](NumericRange.html) | The survey NPS score used to filter the view | [optional] |
| **mos** | [**NumericRange**](NumericRange.html) | The desired range for mos values | [optional] |
| **survey_question_group_score** | [**NumericRange**](NumericRange.html) | The survey question group score used to filter the view | [optional] |
| **survey_promoter_score** | [**NumericRange**](NumericRange.html) | The survey promoter score used to filter the view | [optional] |
| **survey_form_context_ids** | **list[str]** | The list of survey form context ids used to filter the view | [optional] |
| **conversation_ids** | **list[str]** | The list of conversation ids used to filter the view | [optional] |
| **sip_call_ids** | **list[str]** | The list of SIP call ids used to filter the view | [optional] |
| **is_ended** | **bool** | Indicates filtering for ended | [optional] |
| **is_surveyed** | **bool** | Indicates filtering for survey | [optional] |
| **survey_scores** | [**list[NumericRange]**](NumericRange.html) | The list of survey score ranges used to filter the view | [optional] |
| **promoter_scores** | [**list[NumericRange]**](NumericRange.html) | The list of promoter score ranges used to filter the view | [optional] |
| **is_campaign** | **bool** | Indicates filtering for campaign | [optional] |
| **survey_statuses** | **list[str]** | The list of survey statuses used to filter the view | [optional] |
| **conversation_properties** | [**ConversationProperties**](ConversationProperties.html) | A grouping of conversation level filters | [optional] |
| **is_blind_transferred** | **bool** | Indicates filtering for blind transferred | [optional] |
| **is_consulted** | **bool** | Indicates filtering for consulted | [optional] |
| **is_consult_transferred** | **bool** | Indicates filtering for consult transferred | [optional] |
| **remote_participants** | **list[str]** | The list of remote participants used to filter the view | [optional] |
| **flow_ids** | **list[str]** | The list of flow Ids | [optional] |
| **flow_outcome_ids** | **list[str]** | A list of outcome ids of the flow | [optional] |
| **flow_outcome_values** | **list[str]** | A list of outcome values of the flow | [optional] |
| **flow_destination_types** | **list[str]** | The list of destination types of the flow | [optional] |
| **flow_disconnect_reasons** | **list[str]** | The list of reasons for the flow to disconnect | [optional] |
| **flow_types** | **list[str]** | A list of types of the flow | [optional] |
| **flow_entry_types** | **list[str]** | A list of types of the flow entry | [optional] |
| **flow_entry_reasons** | **list[str]** | A list of reasons of flow entry | [optional] |
| **flow_versions** | **list[str]** | A list of versions of a flow | [optional] |
| **group_ids** | **list[str]** | A list of directory group ids | [optional] |
| **has_journey_customer_id** | **bool** | Indicates filtering for journey customer id | [optional] |
| **has_journey_action_map_id** | **bool** | Indicates filtering for Journey action map id | [optional] |
| **has_journey_visit_id** | **bool** | Indicates filtering for Journey visit id | [optional] |
| **has_media** | **bool** | Indicates filtering for presence of MMS media | [optional] |
| **role_ids** | **list[str]** | The role Ids used to filter the view | [optional] |
| **reports_tos** | **list[str]** | The report to user IDs used to filter the view | [optional] |
| **location_ids** | **list[str]** | The location Ids used to filter the view | [optional] |
{: class="table table-striped"}


