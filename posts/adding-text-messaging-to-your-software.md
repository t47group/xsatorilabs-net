---
title: Adding text messaging to your software: registration, consent, and costs
description: Adding SMS reminders or alerts to your business software? Here is what to know about carrier registration, customer consent, opt-outs, and per-message costs first.
date: 2026-11-20
kicker: Integrations
tags: Integrations, SMS, Customer Communication
---

Text messages are one of the most effective ways for software to reach people. Appointment reminders, shift notifications, delivery updates, and "your order is ready" messages get read in a way emails often do not. It is no surprise that "can it send texts?" comes up in nearly every project we scope.

It is also one of the features owners most often underestimate. Sending a text from software is technically simple. Sending texts that actually arrive, from a number carriers trust, to people who agreed to receive them, takes some setup that has nothing to do with code. Here is what to expect.

## Business texting goes through a provider

Your software does not send texts directly. It hands them to a messaging provider — Twilio is a common one, and there are others — which delivers them through the mobile carriers. You rent a phone number from that provider and pay per message, with rates and fees that vary by provider, number type, and carrier.

There are three kinds of numbers businesses typically text from:

- **Ordinary 10-digit local numbers.** Familiar to customers and good for two-way conversation.
- **Toll-free numbers.** Also capable of two-way messaging, with their own approval process.
- **Short codes.** Five- or six-digit numbers built for high volume, with a longer and more expensive approval process.

For most small and mid-sized businesses, the choice is between a local number and a toll-free number.

## Registration is required, and it takes time

US carriers require businesses to register before texting from software. This catches many owners off guard, because it can add days or weeks before the first message goes out.

**For local numbers, the system is called A2P 10DLC** (application-to-person, 10-digit long code). According to [Twilio's documentation](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc), anyone sending texts from an application to US numbers over a 10-digit number must register. Registration has two parts: a **brand**, which identifies your business, and a **campaign**, which describes what you are sending and how people opt in, opt out, and get help. Registered traffic gets less filtering and higher throughput; unregistered traffic is filtered more and costs more.

**For toll-free numbers, the equivalent is toll-free verification.** Twilio states that [unverified toll-free numbers are blocked](https://support.twilio.com/hc/en-us/articles/5377174717595-Toll-Free-Message-Verification-for-US-Canada) from sending messages to the US and Canada.

What this means for your project:

- Start registration early, in parallel with development, not the week before launch.
- Have your business details ready: legal name, EIN, address, and website. A standard business brand requires a tax ID.
- Write a clear description of your messages and include real sample messages. Vague campaigns get rejected.
- Make sure your website has a privacy policy and that your opt-in process is visible. Reviewers check.

## Consent is the core rule

The carrier industry's guidelines, published by CTIA in its [Messaging Principles and Best Practices](https://api.ctia.org/wp-content/uploads/2023/05/230523-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf), are built around consent. Customers should give permission before a business texts them, and promotional messages call for express written consent, such as checking a box on a form.

Federal law also applies. The Telephone Consumer Protection Act governs automated calls and texts, and the FCC's rules under it have been changing in recent years. Because the penalties can be significant, have an attorney review your consent language and practices, especially for marketing messages. This post is general information, not legal advice.

In software terms, consent means:

- **Capture it explicitly.** An unchecked checkbox, separate from other terms, that says what kind of messages the person will receive.
- **Record it.** Store when consent was given, how, and what wording the person saw. If a question ever comes up, that record is what you will need.
- **Keep transactional and marketing separate.** Someone who agreed to appointment reminders has not agreed to promotions.

## Opt-outs have to work instantly

CTIA's guidelines say senders should use standard "STOP" wording for opt-out instructions and honor common words like stop, end, unsubscribe, cancel, and quit, then send one final confirmation and nothing more.

Many providers handle the standard keywords automatically at the number level. Your software still needs to know about it: the opt-out should update the customer's record, so a different part of the system does not try to text them next week, and so your staff can see why reminders stopped.

## Design details that save headaches

**Respect quiet hours.** A reminder at 2am is not helpful. Schedule non-urgent messages for reasonable local hours. Most of Arizona does not observe daylight saving time, so if you text customers in other states, make sure the software handles their time zones properly.

**Keep messages short and identified.** Start with your business name, say what the message is about, and include opt-out instructions where appropriate. Long messages are split into segments and billed as multiple messages.

**Plan for replies.** Customers will reply to automated texts. Decide whether replies go to a shared inbox, a staff member's queue, or an automatic response, and make sure someone is responsible for reading them.

**Handle failures.** Numbers get disconnected and reassigned. Track delivery failures and stop texting numbers that consistently fail.

**Watch the cost.** Per-message fees are small individually and add up at volume. A reminder sent to every customer every day is a very different bill from one sent the day before an appointment.

## Where texting fits best

Texting is most valuable for time-sensitive, expected messages: reminders, confirmations, schedule changes, and status updates. Those are the messages that can head off missed appointments and cut down on inbound "where is my..." calls, which is why texting comes up so often in scheduling and operations software.

If you want your software to start texting customers or staff, [tell us what you need to send](mailto:hello@xsatorilabs.net) and we will help you set it up so the messages actually arrive.
