---
title: How to test software you're paying for: acceptance testing in plain English
description: A plain-English guide to acceptance testing for business owners: how to check that new software does what you paid for before you sign off and launch.
date: 2026-11-23
kicker: Working Together
tags: Testing, Working With Studios, Project Management
---

At some point in every software project, the studio says something like "it's ready for you to review." For many owners, that is an uncomfortable moment. You are not a developer. You do not know what you are supposed to be checking. You click around for twenty minutes, everything seems fine, and you approve it.

Then, two weeks after launch, your team finds that invoices with a discount calculate wrong, or the schedule breaks when someone works an overnight shift, or the report your accountant needs is missing a column.

Acceptance testing is the step meant to catch those problems before launch. It does not require technical skills. It requires knowing your business, which you already do. Here is how to do it well.

## What acceptance testing is for

Your developers should already be testing their own work: automated tests, code review, and checks that each feature behaves as designed. That kind of testing answers "did we build it correctly?"

Acceptance testing answers a different question: "did we build the right thing?" Only the people who run the business can answer that. Developers know how the software is supposed to work. Your team knows how the work actually happens.

## Write the tests before the software is done

The best time to decide how you will test something is when you are describing what you want, not when it is finished. For each feature, write down a few plain-language statements of what must be true for you to accept it.

For example, for an invoicing feature:

- An invoice for a job with three line items shows each item and the correct total.
- A 10 percent discount is applied before tax, not after.
- An invoice can be emailed to the client from the job screen.
- A voided invoice no longer appears in the unpaid report.

These are called acceptance criteria. They give the studio a clear target, and they give you a checklist when it is time to review. If you and the studio agree on them up front, there is far less room for "that's not what I meant" later.

## Test with real scenarios, not just the happy path

The most common testing mistake is checking only the normal case: a typical customer, a typical order, everything filled in correctly. Software rarely fails on the typical case. It fails on the awkward ones.

Make a list of the situations that actually happen in your business and are a little unusual:

- The customer with two locations and separate billing.
- The job that gets canceled halfway through.
- The employee who works across midnight.
- The order with a refund and a reorder on the same day.
- The name with an apostrophe, the address with a suite number, the phone number from another country.
- The month-end close, the year-end report, the holiday schedule.

Your staff know these cases by heart because they deal with them. Ask them for the list.

## Get the right people involved

The owner should not be the only tester. The people who will use the software every day should test the parts they will use: the dispatcher tests scheduling, the bookkeeper tests invoicing, the field staff test the mobile screens on their own phones.

Give each person a short list of scenarios to walk through and a simple way to report what they find. Block real time on their calendars for it. Testing squeezed between other work tends to be shallow.

## Use realistic data

Testing with "Test Customer 1" and round numbers hides problems. Ask the studio to load a copy of real data, or a realistic sample, into the test environment. Real data has the long names, odd characters, and edge cases that expose bugs.

If the data includes sensitive personal information, talk with the studio about how to protect or mask it in the test environment.

## Report problems so they can be fixed quickly

A good bug report saves hours. For each issue, include:

1. **What you did**, step by step.
2. **What you expected** to happen.
3. **What actually happened.**
4. **A screenshot**, if you can.
5. **Which record** you were working on, so the developer can look at the same one.

Then sort issues by importance. Something that blocks daily work is different from a typo on a settings page. Agree with the studio on what must be fixed before launch and what can wait.

## Know what "done" means before you sign off

Many contracts tie a payment or the end of a warranty period to acceptance. Before you sign off, make sure:

- Every acceptance criterion has been checked.
- Every launch-blocking issue is fixed and retested.
- Lower-priority issues are written down with an agreed plan.
- You know how to report problems after launch, and how quickly they will be addressed.

It is reasonable to ask for a short period after launch where issues found in real use are fixed under the original agreement. Many studios include this; confirm what yours offers in writing.

## Plan for testing time in the schedule

Acceptance testing takes your team's time, often more than owners expect. A week or two for a significant release is common, longer for systems that touch money or payroll. If the project schedule does not show time for your review, ask where it is.

## What we do on our side

We write acceptance criteria with clients during scoping, set up a test environment with realistic data, and walk through new features together before asking anyone to test them alone. The goal is that by the time something reaches your team, the only surprises left are the ones only your business could have found.

If you are about to review software and are not sure what to look for, or you want a studio that builds testing into the plan from the start, [tell us what you're working on](mailto:hello@xsatorilabs.net).
