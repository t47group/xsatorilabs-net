---
title: Stopping fake invoices and payment-change fraud with better software controls
description: Business email compromise costs businesses billions a year. These software controls make fake invoices and bank-change scams much harder to pull off.
date: 2026-11-16
kicker: Security
tags: Security, Payments, Internal Tools
---

The most expensive cyber attack most small businesses will face does not involve hacking a server. It is an email. A vendor you pay every month writes to say their bank account has changed. Or an executive asks for an urgent wire before end of day. The email looks right, the request sounds routine, and the money goes to a criminal's account.

The FBI calls this business email compromise, or BEC. In its [2025 Internet Crime Report](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf), the FBI's Internet Crime Complaint Center recorded more than $3 billion in reported BEC losses for the year, the second-largest loss category among cyber-enabled fraud, behind investment scams.

Training staff to spot suspicious emails helps. But the year-end rush — when invoices pile up, people are out, and everyone is trying to close the books — is exactly when people are least likely to slow down. The more reliable defense is to build the checks into the systems your team uses, so the safe path is also the easy one.

## How these scams usually work

The patterns repeat:

- **A changed bank account.** A real vendor's email is compromised, or a lookalike domain is registered, and a message asks you to update payment details before the next invoice.
- **An urgent request from the top.** Someone appearing to be the owner or a manager asks for a wire, a payment, or gift cards, often with a reason it cannot wait.
- **A fake invoice.** An invoice arrives for a plausible service from a plausible vendor, sometimes as a reply in an existing email thread.

The [FBI's Phoenix office advises](https://www.fbi.gov/contact-us/field-offices/phoenix/news/press-releases/fbi-tech-tuesday-business-email-compromise-bec-fraud) checking sender addresses closely for lookalike domains, being cautious of pressure to act quickly, turning on multi-factor authentication, and not relying on email alone — confirming any payment or account change by contacting the person or company directly through a known channel.

That last point is the one software can enforce.

## Controls worth building in

### Make bank-detail changes a workflow, not an edit

In many accounting setups, anyone with access can open a vendor record and change the bank account. That is the single most valuable field to lock down.

A safer design:

1. A change to payment details creates a pending request instead of updating the record.
2. The request requires a callback to a phone number already on file — not one from the email — and the person who made the call records it.
3. A second person approves the change.
4. The vendor's next payment is flagged for extra review.
5. The vendor is notified at their previously known contact that their details changed.

None of this is complicated to build. It turns a single risky click into a short, logged process.

### Require two people for payments above a threshold

Set an amount above which a payment needs approval from someone other than the person who entered it. The threshold depends on your business, but the principle is the same as two signatures on a check.

### Match payments to something real

An invoice should match a purchase order, a contract, or a vendor you have paid before. New vendors should go through their own setup step before they can be paid. Software can flag invoices that do not match anything, arrive from an unfamiliar address, or come from a vendor whose details changed recently.

### Show people what changed

When someone approves a payment, the screen should make it obvious if the bank account is different from last time, if this is the first payment to a vendor, or if the amount is unusual. People approve what they see. Make the risk visible.

### Lock down email and accounting logins

Most of these scams start with a compromised mailbox. Multi-factor authentication on email, accounting, and banking is the baseline, along with removing access promptly when people leave.

### Log everything

Every change to vendor details and every payment approval should record who did it and when. If something goes wrong, that log is the first thing your bank, insurer, and investigators will ask for.

## Where custom software fits

Some accounting platforms offer approval workflows and permission settings; turn on what you already have. Where custom software helps is in the gaps between tools — the vendor portal, the job management system, the payment step that lives outside accounting — and in businesses that pay many vendors or subcontractors and need the checks to fit how they actually work.

These are the kinds of internal controls we build into operations software when payments are involved: approval steps, change logs, and flags that put the right information in front of the right person at the moment of decision.

## If it happens

Speed matters. Contact your bank immediately and ask them to try to recall or freeze the transfer. File a complaint with the FBI's Internet Crime Complaint Center at [ic3.gov](https://www.ic3.gov). Preserve the emails and logs. Then talk to your insurer and, if needed, an attorney about next steps. This is general information, not legal advice.

## A short checklist

- Who can change a vendor's bank details today, and is that change logged?
- Is a callback to a known number required before the change takes effect?
- Do payments above a threshold need a second approver?
- Is multi-factor authentication on for email, accounting, and banking?
- Would your approval screen show that a vendor's account had just changed?

If your payment process depends on people catching a convincing email, it is worth tightening. [Tell us how payments move through your business](mailto:hello@xsatorilabs.net) and we will show you where a control would do the most good.
