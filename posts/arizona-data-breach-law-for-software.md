---
title: Arizona's data breach law and what your software should be ready for
description: A plain-English look at Arizona's data breach notification law, what counts as personal information, and how to design software to limit a breach.
date: 2026-11-18
kicker: Compliance
tags: Compliance, Security, Arizona
---

Most business owners only learn the details of Arizona's data breach law after something has gone wrong. That is the worst time to learn it, because the clock is already running and the questions the law asks — what was taken, from whom, and when — are only easy to answer if your software was built to answer them.

This post walks through what the law requires in plain English, then what that means for how your systems should be designed. It is general information, not legal advice. If you have had an incident or think you might have, talk to an attorney and your insurer right away.

## What the law covers

Arizona's breach notification law is in [A.R.S. § 18-551](https://www.azleg.gov/ars/18/00551.htm) (definitions) and [§ 18-552](https://www.azleg.gov/ars/18/00552.htm) (requirements). It applies to businesses that own, maintain, or license unencrypted and unredacted computerized personal information.

"Personal information" has a specific meaning. It is a person's name, or first initial and last name, combined with one or more of these:

- Social Security number
- Driver license or nonoperating identification license number
- Financial account or card number together with a code or password that allows access
- Health insurance identification number
- Information about medical or mental health treatment or diagnosis
- Passport number
- Taxpayer identification number or IRS identity protection PIN
- Biometric data used to authenticate access to an online account
- A private key used to sign or authenticate electronic records

The definition also includes a username or email address combined with a password or security question and answer that allows access to an online account — even without a name attached. That matters for any business that runs a customer login.

## What it requires

The short version, from the statute and the [Arizona Attorney General's breach FAQ](https://www.azag.gov/consumer/data-breach/faq):

- **Investigate promptly** when you become aware of a possible security incident, to determine whether a breach occurred.
- **Notify affected individuals within 45 days** after determining there was a breach. The notice must include the approximate date of the breach, a brief description of the information involved, and contact information for the three largest consumer reporting agencies and the Federal Trade Commission.
- **If more than 1,000 people must be notified**, also notify the three largest nationwide consumer reporting agencies, and notify the Attorney General and the Director of the Arizona Department of Homeland Security in writing.
- **If you hold data on behalf of another business** — as a vendor or service provider — notify the owner of the data as soon as practicable and cooperate with them.

There are exceptions, including a delay when law enforcement says notice would impede an investigation, and specific rules for organizations covered by federal financial and health privacy laws. The Attorney General enforces the law, and the AG's office notes that knowing and willful violations can carry civil penalties of up to $500,000, plus restitution.

## The software questions hiding in the law

Read those requirements from a developer's point of view and they turn into questions your system must be able to answer quickly:

1. **What personal information do we store, and where?**
2. **Was it encrypted?**
3. **Whose records were in the affected system?**
4. **When did the unauthorized access start, and what did it touch?**
5. **How do we contact those people?**

If your software cannot answer those, the 45 days get spent reconstructing facts instead of notifying people.

## Design choices that make a breach smaller

**Do not store what you do not need.** The safest Social Security number is the one you never collected. If you only need the last four digits to verify identity, store the last four. If a payment processor can hold card data, let it. Every field you leave out is a field that cannot be part of a breach.

**Encrypt sensitive fields, and manage the keys properly.** The law is written around unencrypted data. Encryption at the storage level is standard on major hosting platforms; for the most sensitive fields, encrypting them individually adds another layer. Keys belong in a dedicated secrets or key management service, not in the code or the same database.

**Separate the sensitive data.** Keeping identity documents and financial details in a separate, tightly restricted store means a problem in the main application does not automatically expose them.

**Limit who can see it.** Most staff do not need to view full identification numbers. Mask them by default and log every time someone reveals one.

**Delete on a schedule.** Records you are no longer required to keep are pure risk. A retention policy that automatically removes or archives old data shrinks what is exposed if something goes wrong. Ask your accountant or attorney how long different records need to be kept.

## Design choices that make a breach easier to answer

**Keep an inventory.** A simple, maintained document listing what personal data each system holds, where it lives, and who has access is the starting point for every incident response.

**Log access to sensitive data.** Record who viewed, exported, or changed sensitive records, and when. Keep those logs somewhere an attacker in the main system cannot erase them.

**Know your vendors.** If your payroll provider, CRM, or hosting company holds your customers' data, your contracts should say how quickly they will tell you about an incident and what information they will provide.

**Store contact details you can use.** Notice can go by mail or, if you have it, email. Software that keeps current contact information for the people whose data you hold makes notification possible.

**Write the plan before you need it.** Who decides whether an incident is a breach? Who calls the attorney and the insurer? Who drafts the notice? An hour of planning now saves days later.

## Where to start

If you are building something new, raise these questions in the first week, because they shape the data model. If you have an existing system, start with the inventory: list what personal information you hold and whether you need all of it. Most businesses find at least one field they can stop collecting.

We think about data handling from the start on every build, including internal software for nonprofits like Credit4Vets. If you want help figuring out what your systems hold and how exposed it is, [tell us what you're storing](mailto:hello@xsatorilabs.net) and we will help you shrink the risk.
