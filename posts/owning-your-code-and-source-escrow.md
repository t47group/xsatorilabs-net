---
title: Who owns your code? IP, accounts, and source escrow explained
description: Who owns your code after a custom software project? A plain guide to IP assignment, account ownership, licenses, and when source code escrow helps.
date: 2026-10-16
kicker: Working Together
tags: Contracts, Ownership, Working With Studios
---

Business owners usually assume that if they paid for software, they own it. Often that is true. Sometimes it is only partly true, and occasionally it is not true at all, and the owner finds out when they try to change developers.

This is not legal advice; have an attorney read your contract. But these are the questions we think every client should be able to answer before signing with any studio, including us.

## Copyright does not automatically follow payment

In the United States, the person who writes code generally owns the copyright unless a written agreement says otherwise. Paying an outside company or contractor to write it does not, by itself, transfer ownership.

What transfers it is a clear **assignment of intellectual property** in the contract: language stating that the work product created for you becomes yours, usually upon payment. Look for it. If the contract is silent, ask for it to be added.

Watch for the timing. Many agreements assign ownership once invoices are paid. That is reasonable. What you want to avoid is ambiguity about what happens to work that was paid for if the relationship ends mid-project.

## Not every line will be yours, and that is fine

Modern software is built on top of open-source libraries, frameworks, and paid services. You will not own React or Postgres or Stripe, and you do not need to. You need the right to use them, which their licenses provide.

Studios also bring their own reusable code: authentication setup, deployment scripts, internal tools they use on every project. A fair contract gives you a permanent, transferable license to use that pre-existing material as part of your product, while the studio keeps the right to use it elsewhere. What matters is that you are never in a position where you cannot run, modify, or sell your own software without the studio's permission.

## Accounts are where people actually get stuck

Ownership disputes over copyright are rare. Ownership problems over accounts are common.

Your domain name, hosting, cloud provider, database, code repository, app store developer accounts, email sending service, payment processor, and analytics should be registered to your business, under an email address your business controls, with the studio invited as a user. Not the other way around.

When a studio sets everything up under its own accounts for convenience, it can be very hard to get it back later. Ask for this at the start of the project. It costs nothing to do it correctly on day one.

## What a real handoff includes

Owning code you cannot run is not much better than not owning it. At any point, you should be able to get:

- The complete source code in a repository you control, with its history.
- Instructions to set up, build, and deploy it.
- A list of every outside service it depends on and where the credentials live.
- Notes on anything unusual: scheduled jobs, manual steps, known issues.

A simple way to check is to ask, partway through a project: "If we parted ways next month, what would you hand us?" The answer tells you a lot.

## Source code escrow

Escrow solves a different problem. It matters when you are **licensing** software rather than owning it outright — for example, a vendor's platform that your business depends on, where you do not receive the source code.

In an escrow arrangement, the vendor deposits its source code with a neutral third party. If certain events happen, such as the vendor going out of business or stopping support, the code is released to you so you can keep operating.

For a custom build where the code is assigned to you and lives in your repository, escrow is usually unnecessary; you already have the code. It becomes worth considering when:

- A vendor keeps ownership and licenses the software to you.
- The software is critical enough that losing it would stop your business.
- The vendor is small or early-stage, and continuity is a reasonable concern.

If you go this route, ask that deposits be updated regularly and verified, so that what is in escrow can actually be built. An outdated or incomplete deposit gives you less protection than it appears to.

## Questions to ask before you sign

1. Does the contract assign all custom work product to my business?
2. What pre-existing or third-party code is included, and what license do I get?
3. Whose name are the accounts in?
4. Where does the code live during the project, and can I see it now?
5. What do I receive if we stop working together?

At Xsatori Labs, the code we write for you is yours, in your repository, deployed to your accounts. If you would like us to walk through a contract you have been handed, or our own, [get in touch](mailto:hello@xsatorilabs.net).
