---
title: Building software on a nonprofit budget
description: Nonprofits get quoted like enterprises and funded like side projects. Here's how we scope technology work when every dollar is donated.
date: 2026-09-25
kicker: Case Study
tags: Case Study, Nonprofits, Scoping
---

Nonprofit technology projects fail in a specific way. An organization with a real mission gets a quote sized for a commercial product, cannot fund it, waits, tries again a year later, and repeats. Meanwhile the work the software was supposed to enable does not happen.

The problem is rarely that the developers were greedy. It is that the project was scoped as if it were a startup with venture funding, when the actual constraint is that every dollar was donated by someone who expects it to go to the mission.

## Scope to the constraint, not the vision

Commercial software gets scoped against opportunity: what could this become, what should we build to be ready. Nonprofit software has to be scoped against a budget that is fixed before the project starts and does not grow because the project got interesting.

That inverts the process. Instead of asking what the ideal version looks like and pricing it, you ask what this specific amount of money can buy that produces real mission value, and you build exactly that. It is a less satisfying conversation and it produces far more shipped software.

## The rule: one outcome, not one platform

The most expensive mistake is building a platform when the organization needed one outcome.

A nonprofit rarely needs a system. It needs a specific thing to happen — a person warned, a form submitted, a volunteer matched, a donation processed. Build the narrowest thing that makes that happen. Resist every "while we're in there" instinct, because in a donated-dollar context each of those is money taken from the mission and spent on optionality.

## Rent almost everything

We tell commercial clients to build what is theirs and rent what is everyone's. For nonprofits the ratio shifts hard toward renting.

Authentication, hosting, payments, email, forms, content management — all of it should be off-the-shelf, and much of it is free or heavily discounted for registered nonprofits, which is a discount many organizations never claim because nobody told them to ask. The custom code should be confined to the part that is genuinely specific to the mission, and that part is usually small.

A nonprofit that owns 5,000 lines of code it understands is in a much better position than one that owns 80,000 it cannot maintain.

## Plan for the maintenance nobody funds

This is where nonprofit software actually dies. The build gets funded because it is exciting and grant-shaped. The maintenance does not, because it is neither.

Two years later dependencies are out of date, an integration has changed underneath, nobody has touched it, and it stops working. The organization is back where it started, with the added problem that a system people relied on has failed.

So the maintenance question has to be answered before the build starts, not after: who keeps this running, what does that cost annually, and where does that money come from? If there is no answer, the correct move is to build something smaller and simpler that can survive neglect — a static site that runs untouched for a decade beats an application that needs quarterly attention nobody is funded to give.

## What this looks like in practice

[NMWWD](https://nmwwd.org) is a Phoenix road-safety nonprofit working to prevent wrong-way driving. Its core technology is a mobile app that warns drivers of wrong-way risk in real time — currently being rebuilt from the ground up.

That rebuild decision is the interesting part, and it is the pattern this whole post describes. The right question was not "how do we add features to what exists," it was "what is the smallest, most maintainable version of this that can actually stay running and reach drivers." A safety app that is offline helps nobody, so durability is not a nice-to-have, it is the product requirement.

Meanwhile the organization's public presence runs on a static site that costs essentially nothing to host and will not break on its own. That is deliberate. Money not spent on infrastructure is money available for the mission.

## If you run a nonprofit and need software

A few things worth knowing:

- Ask every vendor about nonprofit pricing. Most major platforms have it, and most will not volunteer it.
- Insist on owning your accounts, domains, and code. Get it in writing. Organizations get held hostage by vendors more often than you would think.
- Be suspicious of any proposal that does not name an annual maintenance cost. It is not zero, and a proposal that implies it is has not been thought through.
- Build the smallest useful thing and let it prove itself before funding the next piece.

We do this work at cost or close to it when the mission warrants it. If you are a nonprofit trying to figure out what your technology should actually be, [tell us what you're trying to do](mailto:hello@xsatorilabs.net) — and we will tell you honestly if the answer is that you do not need custom software at all.
