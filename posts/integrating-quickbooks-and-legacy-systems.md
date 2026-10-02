---
title: Connecting custom software to QuickBooks and legacy systems
description: Integrating custom software with QuickBooks and legacy systems is where projects often get harder than planned. Here is what to expect and how to scope it.
date: 2026-10-21
kicker: Integrations
tags: Integrations, QuickBooks, Internal Tools
---

Almost no business software lives alone. The new scheduling tool needs to send hours to payroll. The customer portal needs invoice status from accounting. The operations dashboard needs data from a system someone set up in 2011 and nobody wants to touch.

Integrations are where a large share of project risk lives, and they are often the line item that gets the least attention in an estimate. Here is what we have learned connecting new software to the tools businesses already run on.

## Why integration is usually the hard part

When you build a new application, you control everything about it. When you integrate, you control half. The other system has its own rules, its own data format, its own limits on how often you can call it, and its own ideas about what a "customer" or an "invoice" is.

Those mismatches are where the work goes. Your system might treat a job as one record; your accounting system might want it split into line items per service, with a tax code on each. Someone has to decide how those map, and what happens when they do not.

## QuickBooks specifically

QuickBooks Online has a well-documented API, and connecting to it is common work. It still comes with specifics worth knowing up front:

- **Online and Desktop are different products.** QuickBooks Online has a modern API. QuickBooks Desktop is integrated through different, older methods that usually require software running on a local machine. Know which one you use before asking for an estimate.
- **Your chart of accounts matters.** Clean, consistent accounts, items, and classes make integration simpler. A messy setup tends to get cleaned up during the project, whether planned or not.
- **Decide which system is the source of truth.** If customers can be edited in both places, you need a rule for which wins. Ambiguity here produces duplicate customers and mismatched balances.
- **Plan for connection maintenance.** Authorizations expire, and someone needs to be notified when the connection drops rather than finding out at month-end.

## Legacy systems

Older systems vary widely. In rough order from easiest to hardest:

1. **A documented API.** The best case, even if the API is old.
2. **Direct database access.** Workable, but you are depending on internal tables that the vendor never promised to keep stable.
3. **Scheduled file exports.** A CSV dropped in a folder every night. Unglamorous, often very reliable.
4. **Screen-driven data entry.** No way in except the user interface. This is sometimes automated, but it is fragile, and we treat it as a last resort.

Before estimating, a good studio will want to see what access actually exists. That investigation is often worth doing as a small paid step on its own.

## Patterns that hold up

**Sync on a schedule unless real time is needed.** Most businesses do not need invoices to appear in accounting within one second. A sync every few minutes, or nightly, is simpler and more robust.

**Log everything that crosses the line.** When a number does not match, you need to see what was sent, when, and what came back. Without that log, every discrepancy becomes an investigation.

**Make retries safe.** Networks fail. A sync that runs twice should not create two invoices.

**Surface failures to a person.** A sync that fails silently is worse than no sync, because people stop checking. Failed records should land somewhere visible with enough detail to fix them.

## Sometimes the integration is the project

Many businesses do not need a new system. They need their existing systems to talk to each other, so staff stop copying data between them by hand.

That was the thinking behind [Flat OS](https://t47group.com/#portfolio), the operations software we built for a Phoenix staffing company: a layer that ties together the tools the business already used rather than replacing all of them. We approach smaller internal builds, like the ones behind Credit4Vets and Wizeacquire, with the same question first: what do the existing tools already do well, and where are people acting as the connection between them?

## Questions to answer before scoping

- Which systems need to connect, and which product versions are they?
- What data moves in each direction, and how often?
- Which system wins when the same record differs?
- Who gets notified when something fails?
- Do you have admin access and vendor support for each system?

If you have systems that do not talk to each other and a team doing the translating, [describe the setup to us](mailto:hello@xsatorilabs.net). We will tell you what connecting them would involve.
