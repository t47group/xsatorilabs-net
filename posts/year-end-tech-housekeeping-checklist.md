---
title: A year-end tech housekeeping checklist for small businesses
description: A practical year-end checklist for your business technology: domains, certificates, accounts, subscriptions, backups, and documentation to sort out before 2027.
date: 2026-11-25
kicker: Planning
tags: Planning, Operations, Small Business
---

The last weeks of the year are when most businesses tidy up their books. It is also a good time to tidy up the technology the business runs on. Small problems in this area — an expired domain, a former employee who still has access, a backup nobody has checked — tend to stay invisible until they cause an outage or a security incident.

None of the items below require a developer. Most can be done in an afternoon by whoever handles operations. Here is the checklist we recommend.

## 1. Domains

Your domain name is the foundation of your website and your email. If it expires, both can stop working.

- Confirm who owns the domain registration. It should be in the business's name, using a company email address, not a personal account belonging to a former employee or web designer.
- Check the expiration date and turn on auto-renew.
- Make sure the payment card on file is current. An expired card is a common reason domains lapse.
- Turn on two-factor authentication on the registrar account.

## 2. Security certificates

The padlock in the browser comes from a TLS certificate, and certificates expire. That has become more important recently. Under a [CA/Browser Forum ballot](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/) passed in 2025, the maximum lifetime of public certificates began shrinking in March 2026 and is scheduled to drop to 47 days by 2029.

Shorter lifetimes mean manual renewal is no longer realistic. Ask whoever manages your website and apps to confirm that certificates renew automatically, and that someone gets an alert if a renewal fails.

## 3. Who has access to what

This is the most valuable item on the list. Over a year, people come and go, contractors finish projects, and vendors get logins for a one-time task. Their access often stays.

Make a list of the systems that matter — email, accounting, payroll, banking, your website host, your domain registrar, your CRM, your code repository, your social media accounts — and for each one:

- Remove anyone who no longer needs access.
- Confirm at least two trusted people in the business have admin access, so you are never locked out if one person is unavailable.
- Check that admin accounts use two-factor authentication.
- Rotate shared passwords and API keys that former staff or contractors could have seen.

## 4. Subscriptions and licenses

Software subscriptions accumulate. Look through your card statements and accounting records for recurring software charges and ask of each one: are we still using this, and are we paying for more seats than we need?

Year-end is a good time for this because any annual plans that renew in January are coming up soon. Canceling before renewal is easier than requesting a refund after.

While you are there, note which subscriptions hold important business data. Before canceling anything, export what you need to keep.

## 5. Backups

Confirm that the important data is being backed up: your website, your databases, your accounting data, and shared files.

Then do the step that usually gets skipped: try restoring something. Pick a file or a record and confirm you can actually get it back. A backup that has never been restored is an assumption, not a safety net.

Also check where backups are stored. They should be separate from the system they protect, so a problem with one does not take out both.

## 6. Software updates

Websites, plugins, apps, and the servers they run on all need updates. Many security incidents exploit known problems that already had a fix available.

- If you run a content management system, update the core software, theme, and plugins, and remove plugins you no longer use.
- Ask your developer or hosting provider when your custom software's dependencies were last updated.
- Retire old devices and computers that no longer receive security updates.

## 7. Documentation

Write down, in one place the business controls:

- Where your website and apps are hosted, and who to contact for support.
- Where your code lives and who has access to it.
- Which vendors provide which services, with account numbers and support contacts.
- How to reach your developer or studio in an emergency.

If the only person who knows how your systems fit together left tomorrow, this document is what the next person would need.

## 8. Contracts and renewals

Look at your agreements with technology vendors, including maintenance and support contracts with developers. Note renewal dates, price changes, and notice periods for canceling. If a contract auto-renews in January for another year, now is when you decide whether you want it to.

## 9. Your plan for next year

Finally, write down the technology problems that cost you the most this year: the manual work, the systems that do not talk to each other, the reports that take too long. That list is the starting point for next year's priorities and budget. We wrote about [planning a 2027 software budget](/blog/budgeting-for-2027-software-projects/) in more detail.

## Make it a yearly habit

Put this checklist on the calendar for the same time each year. The first pass usually turns up a few surprises. After that, it becomes a short, routine review.

If you go through this list and find things you are not sure how to handle — access nobody can explain, software that has not been updated in years, a vendor you cannot reach — [get in touch](mailto:hello@xsatorilabs.net). We can help you sort out what you have before the new year starts.
