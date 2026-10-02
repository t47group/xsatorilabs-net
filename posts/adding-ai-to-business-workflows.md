---
title: Adding AI to an existing business workflow without the hype
description: A practical guide to adding AI to an existing business workflow: where it pays off, where it fails, and how to test it before you commit budget.
date: 2026-10-09
kicker: AI
tags: AI, Automation, Operations
---

Most of the AI conversations we have with business owners start the same way. Someone saw a demo, the demo was impressive, and now there is pressure to "do something with AI." The demo is rarely the problem. The problem is that a demo shows what a model can do once, under ideal conditions, and a business needs something that works the same way on the four hundredth try on a Tuesday afternoon.

Here is how we approach it when the goal is a working tool rather than a press release.

## Start with the workflow, not the model

The useful question is not "where can we use AI?" It is "which step in our process is slow, repetitive, and mostly about reading or writing text?"

That second question has concrete answers. Sorting inbound emails and forms into the right queue. Pulling fields out of documents that arrive in a dozen different layouts. Drafting a first-pass reply that a person reviews and sends. Summarizing a long record so the next person can act on it in thirty seconds instead of ten minutes.

Each of those is a specific step with an input, an output, and a person who currently does it by hand. That is what you can build against.

## Where it tends to work

**Reading messy input.** Models are good at taking unstructured text — an email, a scanned form, a voicemail transcript — and turning it into structured fields. This is often the highest-value use in an operations-heavy business, because so much work starts with someone retyping what was sent to them.

**Drafting, with a human in the loop.** A model that writes the first version of a reply, a job description, or a summary saves real time, as long as a person approves it before it goes anywhere that matters.

**Search over your own material.** Letting staff ask questions of your policies, past jobs, or internal documents in plain language can replace a lot of "who knows where that is?" interruptions.

**Classification and routing.** Deciding which bucket something belongs in, and flagging the ones that do not fit any bucket, is a task models handle well and people find tedious.

## Where it tends to fail

**Anything that has to be exactly right every time without review.** Models produce plausible output, and plausible is not the same as correct. Pricing, payroll amounts, compliance decisions, and anything with legal weight should be computed by ordinary code or decided by a person.

**Replacing a process nobody has written down.** If your team cannot describe how they make a decision, a model will not figure it out for them. It will produce something that looks like a decision.

**Long autonomous chains.** A model that takes one step and hands it to a person is reliable. A model that takes ten steps on its own, each depending on the last, compounds small errors into large ones.

## Build it like any other feature

The parts of an AI feature that make it dependable are not AI. They are the same engineering discipline as everything else.

Keep a set of real examples from your business — fifty or a hundred is enough to start — and test every change against them, so you know whether a new prompt or model made things better or worse. Log what the model received and what it returned, so that when someone says "it got this wrong," you can see why. Put limits on what it is allowed to touch. And decide in advance what happens when it is unsure: the right answer is usually to hand the item to a person rather than guess.

Cost deserves a line as well. Model usage is billed per request, and a feature that runs on every record in a busy system can cost more than expected. Estimate volume before you build, not after the first invoice.

## Protect your data

Before any customer or employee information goes to a model provider, know where it goes, whether it is retained, and whether it is used for training. Business tiers from the major providers have clear terms on this; consumer tools often do not. If you handle health, financial, or personnel records, this is the first conversation, not the last.

## A sensible first project

Pick one step. Measure how long it takes today and how often it goes wrong. Build the smallest version that handles the common case and routes everything else to a person. Run it alongside the existing process for a few weeks before relying on it.

If it earns its place, expand. If it does not, you have spent a small amount to learn that, which is far better than a large AI initiative that quietly gets turned off.

We have spent a lot of time on operations software, including [Flat OS](https://t47group.com/#portfolio) for a staffing business, and the opportunities are usually in the unglamorous middle of a process. If you want help finding the step worth automating, [tell us how your workflow runs today](mailto:hello@xsatorilabs.net).
