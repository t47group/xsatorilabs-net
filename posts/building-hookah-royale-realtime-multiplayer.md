---
title: Building Hookah Royale: real-time multiplayer on a small team
description: A case study in shipping synchronized card games across web, iOS, and Android — and the architectural decisions that kept the team small.
date: 2026-09-16
kicker: Case Study
tags: Case Study, Real-Time, Mobile
---

Multiplayer is where ambitious consumer products usually go over budget. Everything is fine until two people need to see the same thing at the same time, and then a category of problem appears that has no equivalent in ordinary web work.

[Hookah Royale](https://hookahroyale.com) is a social card-game lounge — Kon Khan, 31, Texas Hold'em, Blackjack — playable with friends on web and mobile. Here is what building it taught us.

## The hard part is not the game

Card game rules are finite and testable. You can write the rules of Blackjack in an afternoon and be confident they are right.

The hard part is that six people are holding six devices on six different networks, and all of them must agree on the state of one table. One player's connection drops mid-hand. Another's phone sleeps. A third has 400ms of latency. The game must remain coherent for everyone, and it must be impossible for any client to lie about what it holds.

## Rule one: the server owns the truth

The single most important decision was that the client never decides anything. It renders and it sends intent. The server holds the deck, evaluates every action against the actual state, and broadcasts the result.

This sounds obvious and it is routinely violated, usually for a good-seeming reason — dealing on the client feels faster, validating locally saves a round trip. The moment any authority lives on the device, you have created a cheating surface, and in a social card game the appearance of cheating destroys the product faster than any bug.

The rule that saved us repeated work: **if a client could gain by lying about it, the server computes it.**

## Rule two: design for the disconnect, not the connection

The naive model treats disconnection as an error state. In mobile reality it is the normal state — phones sleep, apps background, elevators exist, cell handoffs drop packets.

So reconnection is not error handling, it is a core feature. A returning client asks for the current state and receives enough to rebuild the table exactly, without the other five players noticing anything happened. Once we treated resync as the primary path rather than the exception, an entire class of bug disappeared, because the recovery path was the same well-tested path everyone used constantly.

The corollary: never assume a player will come back. Every seat needs a timeout policy, an auto-action, and a way for the table to continue without them. A game that stalls because one person's battery died is a game nobody finishes.

## Rule three: one codebase, three platforms

We ship web, iOS, and Android. Maintaining three native implementations of the same card game would have meant three times the surface area and three chances for the rules to drift apart — and rule drift in a multiplayer game is not a cosmetic bug, it is a desynchronized table.

We built the game once as a web application and wrapped it for the native stores, keeping the game logic in exactly one place. The native layer handles what genuinely needs to be native: push notifications, store integration, device features.

This is not the right call for every product. A game demanding sixty-frames-per-second rendering or deep hardware access should be native. A turn-based card game is nowhere near those limits, and pretending otherwise would have tripled the cost for no player-visible benefit.

## Rule four: pick infrastructure that does the boring parts

Real-time subscriptions, authentication, and row-level access control are solved problems. Building them in-house would have been months of work to arrive at a worse version of something available off the shelf.

We used managed infrastructure for that layer and spent the saved time on the parts that are actually ours: the game logic, the table experience, the feel of it. The general principle we apply on every project — **build what is yours, rent what is everyone's** — is the reason a small team could ship this at all.

## What we would tell someone starting one

- Decide the authority model on day one. Retrofitting server authority into a client-authoritative game is close to a rewrite.
- Test with bad networks deliberately, not with good ones accidentally. Throttle, drop, and background your own app constantly.
- Build the spectator and reconnect path early. They share almost all their machinery with the recovery path you will need at 2am when a table is stuck.
- Instrument the table. When a player says "it froze," you need to be able to see what that table's state actually was.

We build products like this for clients and for ourselves — Hookah Royale is one of our own, which means we live with every decision we made in it. If you are building something with real-time mechanics and want a straight read on the architecture, [tell us what you're working on](mailto:hello@xsatorilabs.net).
