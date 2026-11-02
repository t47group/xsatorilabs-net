---
title: Data migration: moving off an old system without losing what matters
description: Moving data off an old system is where many software projects slip. Here is how to plan a data migration, clean records, test it, and cut over without surprises.
date: 2026-11-09
kicker: Scoping
tags: Data Migration, Scoping, Internal Tools
---

When businesses plan a new system, the conversation is almost always about the new screens, the new reports, and the new features. The data sitting in the old system gets a single line in the plan: "migrate existing data."

That line is frequently where the schedule slips. Years of customer records, job history, invoices, and notes have to come out of one system and land correctly in another, and the old data is never as clean as anyone remembers. Here is how we approach migrations so they stop being the surprise at the end of a project.

## Start by deciding what actually needs to move

Not all data deserves a ticket to the new system. Before anyone writes a script, sort what you have into three groups:

- **Live data** that the business uses every day: active customers, open jobs, current pricing, unpaid invoices. This has to move, and it has to be right.
- **History** that people look up occasionally: closed jobs, old invoices, past correspondence. This often needs to move, but it may not need every field.
- **Archive** that you keep for records but rarely open. This may not need to move at all. An export stored safely, with a way to search it, can be enough.

Every record you choose not to migrate is a record you do not have to map, clean, and test. Ask your accountant or attorney how long you need to keep different kinds of records, and keep a readable archive for anything with a retention requirement.

## Get the data out early

The first real step is a full export from the old system, done at the start of the project rather than near the end. Until you have actually looked at the data, every estimate is a guess.

Some systems have a clean export. Others offer only a report you can download, a backup file in a format nobody else reads, or direct database access with tables named in ways only the original developer understood. If the vendor charges for an export or makes it difficult, find out now. That is also a good time to confirm, in writing, that the data is yours.

## Expect the data to be messier than anyone says

Once the export is in hand, look at it closely. Typical findings:

- The same customer entered three times with slightly different spellings.
- Phone numbers, dates, and addresses in several formats.
- A "notes" field that staff have been using to store information the system had no proper place for — gate codes, preferred contact times, billing quirks.
- Fields that were required in the new design but are blank for half the old records.
- Records that reference other records that no longer exist.

None of this is anyone's fault. It is what happens when a system is used by real people for years. But each issue needs a decision: fix it during migration, fix it by hand afterward, or accept it.

## Map every field, and write it down

A field mapping is a simple table: this field in the old system becomes that field in the new one, transformed this way. It sounds tedious, and it is the most valuable document in the migration.

The mapping is where you make business decisions explicit. Does "inactive" in the old system mean the same thing as "archived" in the new one? Does a job with three line items become one record or three? Which of the duplicate customers wins? These are not technical questions. Someone who knows the business has to answer them.

## Rehearse it more than once

Run the migration into a test copy of the new system, then have the people who use the data every day look at the results. Not a developer — the office manager, the dispatcher, the bookkeeper. They will spot things in five minutes that a script will never flag.

Then fix the problems and run it again. A good migration is rehearsed several times before the real one, and each run should be faster and cleaner than the last.

Useful checks after each rehearsal:

- Record counts match what you expected, by type.
- Totals match: the sum of open invoices, the number of active customers, account balances.
- A sample of specific records, chosen by staff, looks right end to end.
- The awkward cases — the customer with two locations, the job that was split — came through correctly.

## Plan the cutover

The cutover is the moment the business stops using the old system and starts using the new one. A few decisions make it go smoothly:

- **Pick a quiet window.** A weekend or a slow week, not the end of a month or the week before a holiday.
- **Freeze changes in the old system** once the final export starts, so nothing is entered in a place that is about to be retired.
- **Decide what happens to in-flight work.** Orders or jobs that are half-finished at cutover need a clear rule.
- **Keep the old system readable** for a period afterward, so people can look things up if something seems wrong.
- **Have a fallback plan.** Know what you would do if the cutover had to be reversed, even if you never use it.

## Budget for it honestly

Migration work depends heavily on the condition of the old data, which is why studios are often cautious about estimating it before seeing an export. If a proposal treats migration as a small fixed item without having looked at your data, ask how they arrived at the number.

It also takes your team's time. Someone has to answer mapping questions, review test runs, and clean up records by hand. That time belongs in the plan.

## Where this shows up most

Migration questions come up in almost every project that replaces an existing tool, whether it is a full operations platform or a small internal app. The pattern is always the same: the earlier the data is examined, the fewer surprises at the end.

If you are planning to move off an old system and are not sure how hard the data will be, [send us a description](mailto:hello@xsatorilabs.net) of what you are running today. We will tell you what to look at first.
