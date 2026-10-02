---
title: Building Xsatori: pricing a sports market with an AMM
description: A case study in building a sports market exchange with an automated market maker, and what custom pricing engines teach about financial software design.
date: 2026-11-02
kicker: Case Study
tags: Case Study, Marketplaces, Architecture
---

Most marketplaces have a cold-start problem. Exchanges have a sharper version of it: a price only exists when a buyer and a seller agree, and on a new platform there may be no one on the other side of a trade.

[Xsatori](https://xsatori.com) is a sports market exchange we are building, where users take positions on sports outcomes and prices move with demand. Rather than wait for matching buyers and sellers, it uses an automated market maker, or AMM, to price the market. This post covers why that model fits and what it teaches about building software where the core product is a number.

## Why not a traditional order book

A traditional exchange uses an order book. Buyers post the price they will pay, sellers post the price they will accept, and trades happen where those meet. This works well when there are many participants. When there are few, the book is thin, the gap between buying and selling prices is wide, and an individual user may not be able to trade at all.

For a new platform with many markets — every team, every season, every event — expecting deep order books everywhere from launch is not realistic.

## What an AMM does differently

An automated market maker replaces the counterparty with a formula. The platform always stands ready to trade, and the price is calculated from the current state of the market. As more people buy one side, its price rises according to the formula; as they sell, it falls.

The result is that every market is tradable from the first minute, and prices respond to demand in a predictable, auditable way. The tradeoff is that the formula has to be designed carefully, because it now determines how prices behave under every possible pattern of trading.

## The formula is the product

In most software, the business logic supports the product. In an exchange, the pricing logic is the product. That changes how the work should be done.

**Model before you build.** The pricing behavior needs to be understood under many trading patterns — steady demand, sudden swings, one large trade, many small ones — before an interface is wrapped around it. The edges matter more than the average case.

**Separate the engine from everything else.** Pricing belongs in its own component, apart from the interface, accounts, and notifications, with its own tests. When anything that touches price or balances goes through one place, it is far easier to reason about and to verify.

**Treat precision as a requirement.** Financial calculations cannot accumulate rounding errors. Anything that affects a balance should use exact arithmetic with explicit rounding rules, and totals should be checkable at any time.

## The server decides

As with real-time games, the rule that matters most is that the server owns the truth. The client shows a price and sends a request. The server recalculates the price at the moment of execution, applies the trade only if it is still valid, and records the result.

This prevents a user from trading on a stale price and keeps every balance consistent no matter how many requests arrive at once. It also means every trade has a complete record: what was requested, what price applied, and why.

## Rules beyond the code

Any product that involves money and outcomes operates under legal and regulatory constraints, and those vary by jurisdiction. That has to shape the architecture from the start: market rules that can be configured rather than hard-coded, and a complete record of every transaction.

We would give the same advice to anyone building in a regulated space: involve qualified counsel early, and design so that rules can change without rewriting the core system.

## What carries over to other projects

Few clients are building a sports exchange. Many are building software where a number has to be right: pricing engines, quoting tools, commission calculations, billing, inventory valuation. The lessons transfer directly:

- Model the logic and test its edge cases before building the interface around it.
- Keep the calculation in one isolated, well-tested place.
- Never let the client be the authority on a value that matters.
- Record every input and output, so any number can be explained later.

We build our own products, like Xsatori, alongside client work, and the experience shapes how we approach every system that handles money. More about our founder and the companies behind the studio is at [ninomihilli.com](https://www.ninomihilli.com). If you are building something where the math has to be right, [tell us about it](mailto:hello@xsatorilabs.net).
