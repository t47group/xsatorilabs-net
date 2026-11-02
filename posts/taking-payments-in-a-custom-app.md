---
title: Taking payments in a custom app: fees, PCI scope, and what to own
description: What business owners should know before adding payments to a custom app: processor fees, PCI compliance scope, refunds and disputes, and keeping control of the account.
date: 2026-11-27
kicker: Payments
tags: Payments, Integrations, Security
---

It is Black Friday, which makes it a fitting day to talk about the part of a custom app that touches money. Taking payments — deposits, invoices, subscriptions, online orders — is one of the most common features in the software we scope, and one of the easiest to get wrong in ways that do not show up until something goes sideways.

The good news is that you almost never need to build payment handling yourself. The decisions that matter are about which provider you use, how the payment form is set up, and who controls the account. Here is what to know.

## Use a payment processor, and let it hold the card data

Payment processors such as Stripe, Square, and others handle the hard parts: collecting card details securely, talking to the card networks, detecting fraud, and moving money into your bank account. Your app tells the processor what to charge, and the processor tells your app whether it worked.

The most important design principle is that card numbers should never touch your servers. Modern processors provide payment forms and hosted checkout pages that collect card details directly, then give your app a token that represents the card. Your software can charge that token again later — for a subscription or a repeat customer — without ever seeing the number.

This is not just good security. It shapes your compliance obligations.

## What PCI compliance means for you

Any business that accepts card payments is expected to follow the Payment Card Industry Data Security Standard, or PCI DSS, maintained by the PCI Security Standards Council. Most small businesses demonstrate compliance with a self-assessment questionnaire, and which questionnaire applies depends on how card data flows through your systems.

The shortest one, known as SAQ A, is for merchants that fully outsource card handling to a compliant provider. That is a strong reason to use a hosted checkout or the processor's embedded payment fields rather than building your own form.

Two details worth knowing:

- **The standard was updated for embedded payment forms.** According to the [PCI Security Standards Council](https://blog.pcisecuritystandards.org/faq-clarifies-new-saq-a-eligibility-criteria-for-e-commerce-merchants), as of April 1, 2025, merchants using SAQ A with a provider's payment form embedded in their own page (for example, in an iframe) must confirm their site is protected against malicious scripts. The Council describes ways to meet that, including written confirmation from the payment provider. Redirecting customers to the provider's own checkout page is treated differently.
- **Your processor and bank decide which questionnaire applies.** The Council advises merchants to confirm with their acquirer that SAQ A is right for their setup. Ask your processor, and keep the answer on file.

This is general information. Your processor's support team and, where needed, a qualified security assessor can confirm what applies to you.

## Understand the fees before you set prices

Processor fees vary by provider, card type, and how the payment is taken. As one reference point, Stripe's [published US pricing](https://stripe.com/pricing) at the time of writing lists 2.9% plus 30 cents for domestic card payments online, 0.8% capped at $5 for ACH bank debits, an additional 1.5% for international cards, and a $15 fee for each dispute. Other providers price differently, and businesses with larger volume can sometimes negotiate.

What this means for your app:

- **Large invoices may be cheaper by bank transfer.** For a business that bills clients thousands of dollars at a time, offering ACH alongside cards can make a real difference in fees. Your app can present both.
- **Small transactions are expensive in percentage terms.** A fixed per-transaction fee matters a lot on a $5 charge and very little on a $500 one.
- **Do not forget refunds and disputes.** Know your processor's policy on whether fees are returned when you refund a customer.
- **Talk to your accountant** about how fees and refunds are recorded, especially if the app also syncs with your accounting system.

## Plan for the messy parts

The charge itself is the easy part. Most of the design work goes into what happens around it:

- **Failed payments.** Cards expire and get declined. For subscriptions, decide how many times to retry, how to notify the customer, and what happens to their access.
- **Refunds and partial refunds.** Who can issue them, up to what amount, and how they are recorded.
- **Disputes.** When a customer disputes a charge with their bank, you will need to respond with evidence. Software that stores receipts, delivery confirmations, signed agreements, and communication history makes that much easier.
- **Deposits and balances.** If you take a deposit now and charge the balance later, the app has to track both and handle cancellations in between.
- **Notifications from the processor.** Payment status changes arrive as messages from the processor to your app, sometimes out of order or more than once. The app needs to handle them so a payment is never recorded twice.

## Keep the account in your name

The processor account should belong to your business, set up with your business's legal name, tax ID, and bank account, and owned by someone at your company. Your developers can be given limited access to build and test.

When a payment account is set up by a developer under a personal login and that developer moves on, untangling it is slow and stressful, and in the meantime the business may not be able to see its own payment history. The same principle applies to every account your software depends on, and we wrote more about it in [who owns your code](/blog/owning-your-code-and-source-escrow/).

## Watch for fraud

Online payment forms attract automated card testing — criminals running stolen card numbers through small charges to see which work. Turn on your processor's fraud tools, add bot protection to public payment forms, and set up alerts for unusual patterns like many small failed charges in a short period.

## Questions to ask before you build

1. Which processor, and does it support the payment methods your customers want?
2. Will card details be collected by the processor's hosted page or embedded fields?
3. Which PCI questionnaire applies, and has the processor confirmed it?
4. How will refunds, disputes, and failed payments be handled in the app?
5. Who owns the processor account?
6. How do payments flow into your accounting system?

If you want to start taking payments in your app, or you are not sure the way you take them today is set up safely, [tell us how you get paid](mailto:hello@xsatorilabs.net) and we will help you design it properly.
