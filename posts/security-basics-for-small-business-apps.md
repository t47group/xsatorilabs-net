---
title: Security basics every small-business app should have
description: Security basics for small-business apps that every owner should ask about: logins, permissions, backups, data handling, and who has access to what.
date: 2026-10-26
kicker: Security
tags: Security, Small Business, Internal Tools
---

Small businesses are often told they are too small to be targets. In practice, most attacks are not aimed at anyone in particular. Automated tools scan the internet for weak passwords, outdated software, and exposed data, and they find small businesses because small businesses are less likely to have someone checking.

You do not need an enterprise security program to build safe software. You need a short list of fundamentals done consistently. These are the ones we expect in every application we build, and the ones we would ask about if we were hiring a studio.

## Logins

**Use a proven authentication service.** Login, password reset, and session handling are easy to get subtly wrong. Established services and libraries have already absorbed years of attacks. A studio writing its own password system from scratch should have a very good reason.

**Offer two-factor authentication**, and require it for anyone with admin access. Most account takeovers start with a reused password.

**Support single sign-on for staff** if your team already uses Google Workspace or Microsoft 365. It means one place to remove access when someone leaves.

## Permissions

Every user should be able to see and do only what their job requires. A field worker does not need billing data. A client should never see another client's records.

This sounds obvious, and it is one of the most common gaps in custom software. The check has to happen on the server, for every request, not only by hiding buttons in the interface. Ask your developers how access is enforced and how they test it.

## Data in transit and at rest

All traffic should use HTTPS. This is standard now, but it should cover every endpoint, including the admin tools and the API the mobile app talks to.

Sensitive data — Social Security numbers, bank details, health information, identity documents — should be encrypted where it is stored, and ideally not stored at all if you can avoid it. The safest data is the data you never kept. If a payment processor can hold card numbers for you, let it.

## Secrets and keys

Passwords for databases and API keys for outside services should never be written into the code or shared in chat messages. They belong in a secrets manager or the hosting platform's environment settings, with access limited to the people who need it.

When someone with access leaves, rotate the keys they could see.

## Updates

Most real-world breaches exploit known problems that already had a fix available. Libraries and frameworks need regular updates, and the hosting platform needs to be kept current. This is one of the reasons maintenance is an ongoing cost rather than an optional one.

## Backups you have tested

Backups should run automatically, be stored separately from the main system, and — the part that gets skipped — be restored on a test basis now and then. A backup nobody has ever restored is a hope, not a plan.

## Logging and alerts

The system should record logins, permission changes, exports, and other sensitive actions, along with who did them. Someone should be alerted to unusual activity, like many failed logins or a large export at 3am. Without logs, you cannot answer the first question after an incident: what happened?

## Accounts and people

Most of security is administrative. Keep accounts in your business's name. Remove access promptly when staff or contractors leave. Give your developers the access they need for the project and no more. Know who has admin rights to your hosting, domain, and code.

## Industry rules

Some data comes with legal obligations. Health information, payment card data, financial records, and information about minors each carry specific requirements. If your software touches any of these, raise it at the start of the project, because it affects design decisions that are expensive to change later.

## What to ask a studio

1. Which authentication service do you use, and is two-factor supported?
2. How are permissions enforced and tested?
3. Where are secrets stored, and who can see them?
4. How often are dependencies updated, and who is responsible after launch?
5. How are backups tested?
6. What gets logged, and who gets alerted?

These questions shape our designs from the first week, whether the project is a consumer app or internal software for a nonprofit like Credit4Vets. If you want a second set of eyes on an app you already have or one you are planning, [reach out](mailto:hello@xsatorilabs.net).
