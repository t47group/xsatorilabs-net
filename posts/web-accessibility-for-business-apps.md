---
title: Is your website or app accessible? What the ADA means for business software
description: What the ADA means for your business website and app, which accessibility standards matter, and how to build accessibility in without an expensive retrofit.
date: 2026-11-04
kicker: Accessibility
tags: Accessibility, Compliance, Web Apps
---

Accessibility tends to come up in one of two ways. Either someone on the team asks about it early, or a customer complains that they cannot finish a form, book an appointment, or read a page. The first way is much cheaper.

This post is not legal advice. It is a plain-English look at what the rules say, what "accessible" actually means in software, and how we build it into projects from the start. If you have a specific legal question, talk to an attorney who handles ADA matters.

## What the ADA says about websites

The Americans with Disabilities Act was written before most businesses had websites, but the U.S. Department of Justice has been clear that it reaches online services. In its [guidance on web accessibility](https://www.ada.gov/resources/web-guidance/), the Department says businesses open to the public must provide equal access to their goods and services, including those offered online.

Two points in that guidance matter for planning:

- **There is no detailed federal web standard for private businesses.** The Department notes that businesses have flexibility in how they comply, but they still have to comply.
- **Existing technical standards are the practical yardstick.** The guidance points to the Web Content Accessibility Guidelines (WCAG) and the federal Section 508 Standards as helpful references for making website features accessible.

In other words, the law tells you the outcome — people with disabilities need to be able to use what you offer — and the industry standards tell you how to get there.

## If you sell to cities, counties, or school districts

State and local governments have a more specific rule. The Department of Justice's Title II rule requires their web content and mobile apps to meet WCAG 2.1 Level AA. Under an interim final rule issued in April 2026, the [compliance dates](https://www.ada.gov/resources/web-rule-first-steps/) are April 26, 2027 for governments serving populations of 50,000 or more, and April 26, 2028 for smaller governments and special districts.

That rule applies to the government, not to you. But the Department also says a public entity cannot contract away its ADA responsibilities, so any content or app a vendor provides on its behalf has to meet the standard. If your business builds software, portals, or online forms for an Arizona city, county, or district, expect accessibility requirements to start showing up in contracts and RFPs.

## What WCAG is, briefly

WCAG is published by the World Wide Web Consortium. Version 2.2 [became a W3C Recommendation](https://www.w3.org/WAI/news/2023-10-05/wcag22rec/) in October 2023, and version 2.1 is the one named in the government rule. Both are organized around the same idea: content should be perceivable, operable, understandable, and robust for people using different abilities and tools.

"Level AA" is the middle of three conformance levels and the one most organizations target.

## What accessibility looks like in practice

The DOJ guidance lists common barriers, and they line up closely with what we see in audits of business apps:

- **Low color contrast.** Light gray text on a white background is hard to read for people with low vision, and for everyone else outdoors on a phone in a Phoenix afternoon.
- **Images with no text alternative.** A screen reader cannot describe a picture, a chart, or an icon button unless the developer provided a text description.
- **Video without captions.** People who are deaf or hard of hearing miss whatever is only said aloud.
- **Pages that need a mouse.** Some people navigate entirely by keyboard or by switch devices. If a menu, date picker, or checkout button cannot be reached with the Tab key, it is unusable for them.
- **Unlabeled forms.** A field that only shows placeholder text, or an error message that only turns a box red, leaves screen reader users guessing.

None of these are exotic. They are the ordinary details of building an interface, done carefully or done carelessly.

## Why retrofitting costs more

Accessibility is cheapest when it is a requirement on day one. At that point it is mostly a matter of choosing components that already handle keyboard focus and labels, picking a color palette that passes contrast checks, and writing alt text as content is created.

Retrofitting is a different job. Custom widgets have to be rebuilt. Colors baked into a brand have to change. Hundreds of images need descriptions. Forms need to be restructured. We have seen retrofits take longer than the original feature, because the team is untangling decisions instead of making them.

## A note on overlay widgets

You may be pitched a script you add to your site that promises instant compliance. Be skeptical. These tools can adjust some things on the surface, but they cannot fix a checkout flow that was never built to work with a keyboard, or describe images nobody wrote descriptions for. Accessibility lives in how the software is built.

## How we approach it

On new builds, we treat accessibility as part of the definition of done:

1. **Pick accessible building blocks.** Well-maintained component libraries handle much of the keyboard and screen reader behavior correctly out of the box.
2. **Set contrast and type sizes in the design system** so every new screen inherits them.
3. **Test with a keyboard and a screen reader**, not only with automated scanners. Scanners catch a useful share of problems, but not whether a flow makes sense.
4. **Write it into acceptance criteria.** "A user can complete checkout using only a keyboard" is a testable requirement.
5. **Keep it up.** New content and new features can break what worked at launch, so accessibility checks belong in ongoing maintenance.

## Questions to ask about your current site or app

- Can someone complete your most important task — booking, buying, applying, paying — without a mouse?
- Do your images and icon buttons have text descriptions?
- Do your videos have captions?
- Does your text pass a contrast check?
- If you sell to a government entity, does your contract mention WCAG?

If you are not sure how your site or app holds up, or you are planning something new and want accessibility built in from the start, [tell us what you have](mailto:hello@xsatorilabs.net). We will tell you where the real gaps are and what it would take to close them.
