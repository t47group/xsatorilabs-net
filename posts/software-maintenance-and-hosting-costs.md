---
title: What software costs after launch: maintenance, hosting, and support
description: Software maintenance and hosting costs after launch are never zero. Here is what you will pay for each year and how to budget for it without surprises.
date: 2026-10-19
kicker: Budgeting
tags: Budgeting, Maintenance, Hosting
---

Launch day feels like the finish line. Financially, it is closer to the start. Custom software keeps costing money as long as people use it, and most of the unpleasant surprises we hear about come from businesses that budgeted for the build and nothing after.

None of this is a reason not to build. It is a reason to know the number before you commit.

## Hosting and services

Your application runs on servers somewhere, and someone bills for them monthly. For most business software, the bill is made up of several smaller pieces:

- **Hosting** for the application itself.
- **A managed database**, plus backups.
- **File storage** for uploads, documents, and images.
- **Email and text messaging** services, often billed per message.
- **Third-party APIs** such as maps, address validation, AI models, or identity checks, usually billed by usage.
- **Monitoring and error tracking**, so problems get noticed before customers report them.
- **Domain names and certificates.**
- **App store developer accounts**, if you have a mobile app.

For a small internal tool, this can be modest. For a customer-facing product with real traffic, it grows with usage. The important thing is that the cost scales with your business, so a sudden jump usually means something good happened, or something is misconfigured.

## Maintenance that keeps the lights on

Software sits on top of libraries, frameworks, operating systems, and services that change constantly, whether or not you touch your own code.

Security patches come out and should be applied. Libraries release new major versions and eventually stop supporting old ones. Payment processors and other integrations retire old API versions on their own schedules. Apple and Google update their requirements every year, and apps that fall behind can be removed from the stores.

None of this adds features. All of it is required to keep what you have working and safe. A system left alone for two or three years often needs a sizable catch-up project before anyone can safely change it again.

## Support and small changes

Once people use the software every day, they will find bugs, request small changes, and ask how to do things. Someone has to field those requests, fix what is broken, and decide what is worth changing.

This is usually the largest ongoing line item, and the most variable. A stable internal tool might need a few hours a month. A product that is still finding its fit with customers might need a steady stream of work.

## Common ways to structure it

**A monthly retainer.** A set number of hours each month for maintenance, fixes, and small improvements. Predictable for both sides, and it keeps the team who built the system familiar with it.

**Pay as you go.** Hourly work when something comes up. Cheaper in quiet months, but slower to respond, and patches tend to get skipped until they become urgent.

**In-house ownership.** Your own developer or IT person takes over. This works well for larger systems, provided the handoff included documentation and the person has time set aside for it.

There is no single correct structure. The wrong one is having none, because then maintenance happens only after something breaks.

## How to budget for it

A common rule of thumb in the industry is to set aside a meaningful percentage of the original build cost each year for maintenance and support, on top of hosting. The right figure for you depends on how much the system will change and how critical it is. Ask your studio to estimate it for your specific project, in writing, before the build begins.

Ways to keep it lower:

- **Build less.** Every feature is something to maintain forever.
- **Rent common pieces.** Managed services for authentication, payments, and email shift maintenance onto vendors who do it at scale.
- **Choose mainstream tools.** Popular frameworks get security fixes quickly and have more people who can work on them.
- **Keep it documented.** Documentation makes maintenance faster and makes you less dependent on any one developer.

## Ask before you sign

Any proposal for custom software should include an estimate of annual hosting and service fees and a recommended maintenance arrangement. If it does not, ask. A studio that has thought about your project should be able to answer.

We think about this on our own products as much as client ones, because we pay their hosting bills too. If you want a realistic picture of the total cost of something you are planning, [tell us what you have in mind](mailto:hello@xsatorilabs.net).
