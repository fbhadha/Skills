# Gemini Enterprise Docs (Manage costs) / View feature usage
Source: https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage, page last updated 2026-10-14, extracted 2026-10-19

When you view feature usage in Gemini Enterprise, the usage details depend
on your product edition:

- **Gemini Enterprise Pay-as-you-go:** You see only the usage amount for each
  feature.
- **License-based editions (such as Gemini Enterprise Standard, Plus, Frontline, EDU, and Emerging Market editions):** You see
  pooled quotas based on the number of licenses per subscription.

## Pooled quotas overview

In Gemini Enterprise, for editions with license-based subscriptions
(such as Gemini Enterprise Standard, Plus, Frontline, EDU, and Emerging Market editions),
all users in a Google Cloud project share resource quotas. For more information about
the quotas for each edition, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages).
To enable overages when your project reaches a pooled quota, see
[Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages).

### Quota reset times

Your subscription entitles you to certain quotas across product features. Except
for storage and data indexing, feature quotas are pooled across users in the
same edition within a project and location. For more information, see
[Feature and edition-based quotas](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#feature-quotas).

Pooled quotas reset on the following schedule:

| Feature | Reset schedule |
| --- | --- |
| All features except AI developer tools | Daily at midnight Pacific Time (PT) |
| [AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview) | Every seven days, starting from when a prompt or request is first sent to an AI developer tool.    For example, if a user in your project sends the first prompt using Antigravity on Wednesday at 2 PM Pacific Time (PT), the seven-day quota cycle starts at that time, and the AI developer tools quota resets the following Wednesday at 2 PM PT. |

## Pay-as-you-go usage overview

For the Gemini Enterprise Pay-as-you-go edition, Gemini Enterprise does not
pool usage based on user licenses. Instead, when you view feature usage in the
dashboard, you see the actual usage amount consumed by your project.

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition,
your project must be linked to an
[invoiced
Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

## Before you begin

### Gemini Enterprise

You can view the usage dashboard only if the following are true:

- You're a [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin).
- You have at least one active [Gemini Enterprise subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) (such as
  Gemini Enterprise Standard, Plus, Frontline, EDU, Emerging Market editions, or Pay-as-you-go).

To view quota usage on the **Usage** tab of the
**Usage & Spending** page, you need the following IAM
permissions:

- `monitoring.timeSeries.list`
  - Included by default in the [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin)
    (`roles/discoveryengine.agentspaceAdmin`) role.
  - Without this permission, quota usage displays as
    `0`.
- `serviceconsumermanagement.quota.get`
  - Without this permission, the quota limit displays as
    `Unknown`.

If you use user roles that don't include these permissions,
you must [add the
required permissions to the role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#edit-role).

### Agentspace

If you have an active Agentspace subscription, you can view the usage
dashboard only if you're a [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin).

The dashboard shows the quotas of your Agentspace subscription or the
combined quotas of your Agentspace and Gemini Enterprise subscriptions as
follows:

- Gemini Enterprise Plus quotas include Agentspace Enterprise Plus quotas
- Gemini Enterprise Standard quotas include Agentspace Enterprise quotas
- Gemini Enterprise Frontline quotas include Agentspace Frontline Worker quotas

To view quota usage on the **Usage** tab of the
**Usage & Spending** page, you need the following IAM
permissions:

- `monitoring.timeSeries.list`
  - Included by default in the [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin)
    (`roles/discoveryengine.agentspaceAdmin`) role.
  - Without this permission, quota usage displays as
    `0`.
- `serviceconsumermanagement.quota.get`
  - Without this permission, the quota limit displays as
    `Unknown`.

If you use user roles that don't include these permissions,
you must [add the
required permissions to the role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#edit-role).

## View the usage dashboard

To view feature usage and quota details in your project, follow these steps:

1. In the Google Cloud console, go to the **Gemini Enterprise > Usage &
   Spending** page.

   [Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)
2. Select the **location** of the licenses or subscription.
3. In the **Usage details** section, from the **Subscription tier** list, select the product edition for which you want to view details.

   The dashboard shows the features and usage details for your selected
   edition:

   - For **Pay-as-you-go**, it displays the usage amount.
   - For Gemini Enterprise editions, such as Standard, Plus, Frontline, EDU, and Emerging Market editions, it displays the
     absolute and percentage usage of each pooled quota.

## What's next

- Learn how to [configure overages and spend limits](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages).
- Learn how to [view costs](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).
