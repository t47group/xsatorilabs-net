---
title: When blockchain is actually the right call — and when it isn't
description: We build blockchain products. We also talk most people out of them. Here's the test we apply.
date: 2026-09-30
kicker: Architecture
tags: Blockchain, Architecture, Product Strategy
---

We build blockchain products, so it may be odd to say that most projects proposed to us as blockchain projects should not be. But the sales pitch has run so far ahead of the engineering that plenty of teams arrive having already decided on the technology, without a reason that survives a question.

Here is the test we actually apply.

## The one question

**Who are the parties that do not trust each other, and what specifically would they cheat on?**

That is what this technology is for. It replaces a trusted intermediary with a system where participants who have every reason to lie cannot successfully do so. That is a genuinely hard problem and the machinery is genuinely clever.

If you cannot name the adversarial parties and the specific thing they would falsify, you do not have that problem. You have a database problem, and a database will be faster, cheaper, easier to change, and simpler to explain to your customers.

## Where it usually falls apart

**"For transparency."** You can publish an audit log. You can have it independently attested. Transparency is a policy choice about what you expose, not a consequence of a particular data structure.

**"For immutability."** Append-only storage is a solved problem in ordinary databases. If the concern is that *you* might alter records, the fix is a system where you cannot — which is a permissions and architecture question, not a chain question.

**"To remove the middleman."** Frequently this replaces one intermediary with several: a chain, a wallet provider, an exchange, a bridge. Count the parties honestly at the end. Sometimes it is fewer. Often it is more, with worse recourse when something breaks.

**"For a supply chain."** The chain guarantees that what was written stays written. It cannot guarantee that what was written was true. If a person scanning a box types the wrong thing, you now have an immutable record of a lie. The hard part of supply-chain verification is the physical-to-digital boundary, and no consensus mechanism touches it.

## Where it genuinely earns its place

**Assets that must be transferable without you.** If a user should be able to move something to someone else without your permission, and continue to hold it if your company ceases to exist, that property is very hard to get otherwise.

**Settlement between mutually distrustful parties.** Multiple institutions that need to agree on a ledger and do not want any one of them controlling it. This is the original problem and it remains the best fit.

**Programmatic value transfer with no operator.** Rules that execute on their own, that no party can override — including you. Note that this cuts both ways: no override also means no override when something goes wrong, which is a product decision with real consequences, not a technical footnote.

**Verifiable scarcity that survives you.** If a limited-supply digital thing needs to remain limited even if your servers go away, that guarantee has to live somewhere outside your servers.

## The costs you inherit

Choosing a chain means choosing its constraints, and they are permanent:

- **Irreversibility.** Users lose keys. Users send to wrong addresses. Users get phished. There is no support ticket that undoes it, and your support team will spend real time on situations they cannot fix.
- **Public data.** Most chains are readable by everyone, forever. Anything approaching personal data needs careful design, and privacy regulation was not written with permanent public ledgers in mind.
- **Upgrade friction.** Changing deployed on-chain logic ranges from awkward to impossible. Bugs live longer.
- **Onboarding cost.** Wallets, keys, gas, and network switching each cost you users. If your product is aimed beyond a crypto-native audience, this is usually the dominant cost and it is routinely underestimated.
- **Regulatory surface.** Depending on what you are moving and for whom, you may have walked into a regulated activity. Get that answer before you build, not after.

## The hybrid answer

The right architecture is frequently hybrid: a conventional application for everything users touch, with a chain used narrowly for the one property that genuinely requires it.

Custody, settlement, or proof-of-ownership on-chain. Identity, search, messaging, preferences, and every ordinary interaction in a normal database, where they are fast and cheap and fixable. Most of what people imagine as a blockchain product should look like this.

## How we handle it

When someone brings us a blockchain project, we ask the trust question first. If there is a real answer, we build it and we build it carefully, because the mistakes are unusually permanent. If there is not, we say so — and usually the same product ships faster and cheaper without it.

That has cost us work. It has also meant the blockchain projects we do take on are ones where the technology is load-bearing rather than decorative.

If you are weighing this for your own product, [tell us what you're trying to build](mailto:hello@xsatorilabs.net) and we will give you a straight answer.
