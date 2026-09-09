---
title: The cold-start problem: why marketplaces fail before they launch
description: Most failed marketplaces had working software. What they didn't have was a credible plan for the first ninety days of emptiness.
date: 2026-09-11
kicker: Product Strategy
tags: Marketplaces, Go-to-Market, Product Strategy
---

A marketplace is worth nothing on its launch day. That is not pessimism, it is arithmetic. Buyers arrive, find no inventory, and leave. Sellers arrive, find no buyers, and stop listing. Both sides are behaving rationally and the result is a dead product.

This is the cold-start problem, and it is the single most reliable killer of marketplace startups. Not bugs. Not scaling. Emptiness.

## Why it is not a marketing problem

The instinct is to treat this as a traffic problem — build the thing, then buy ads until enough people show up.

This fails because you are paying to send users into a bad experience. A buyer who arrives to an empty marketplace does not come back when it fills up. You spent acquisition budget to permanently burn a prospect. Do this at scale and you have converted your funding into a list of people who have already decided your product does not work.

The sequencing has to be the other way around. You need enough density to make the experience good *before* you spend on getting people to see it.

## The four approaches that actually work

**Go absurdly narrow.** Thin supply feels dense if the market is small enough. Twenty listings is nothing nationally and plenty for one neighborhood, one campus, or one niche category. Most successful marketplaces launched somewhere embarrassingly specific and expanded outward. Pick the smallest market where you can look full.

**Recruit one side manually.** Not scalably, not through ads — by hand, by phone, by showing up. Founders sourcing early supply personally is not a failure to build a system; it is the correct move at this stage and it teaches you what the supply side actually cares about, which no survey will.

**Subsidize the harder side.** Figure out which side is scarcer and pay for it, in cash, fees waived, or guaranteed minimums. This is expensive and it is supposed to be. The question is whether the density it buys becomes self-sustaining before the money runs out.

**Be useful to one side alone.** The strongest play when you can find it: build something that has standalone value to one side before the other side exists. A tool sellers would use even with zero buyers. Then flip on the marketplace once supply has accumulated for reasons that had nothing to do with your marketplace.

## What this means for the build

This is the part that concerns us as the people writing the software, because the cold-start plan should change what gets built.

If you are launching in one city, you do not need the geographic infrastructure. If you are hand-recruiting supply, your seller onboarding can be a spreadsheet and a human for months — but your *admin tooling* needs to be excellent on day one, because your team is doing manually what the product will eventually automate. If you are subsidizing one side, you need the accounting to track that subsidy from the first transaction, or you will not know whether it is working.

We have watched teams build beautiful self-serve seller onboarding that no seller used for a year, because every early seller was recruited over the phone and set up by hand. That was months of engineering spent on the wrong end of the timeline.

## The question to answer first

Before writing a line of code, answer this: *on day ninety, where does the inventory come from, and who specifically put it there?*

If the answer involves a growth strategy that begins after launch, you do not have a plan, you have a hope. If the answer is a list of names and a phone number, you are in far better shape than most funded marketplace startups.

When we scope marketplace work, we ask this before we ask about features. It changes the architecture, the sequencing, and often the budget — usually downward, because a narrow launch needs less software than the version in your head.

If you are working on a marketplace and want a straight conversation about what to build first, [get in touch](mailto:hello@xsatorilabs.net).
