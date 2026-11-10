# Copyright

*Designing Android at Scale*
**Volume 1 — Foundations: Networking & Local Data**

Copyright © 2026 Prakash Sharma. All rights reserved.

No part of this publication may be reproduced, stored in a retrieval system, or transmitted in
any form or by any means — electronic, mechanical, photocopying, recording, or otherwise —
without the prior written permission of the author, except for brief quotations in reviews.

This book is an independent work. All product names, trademarks, and registered trademarks —
including Android, Kotlin, and any third-party libraries, services, or platforms referenced — are
the property of their respective owners and are used for identification and educational purposes
only. Their use does not imply any affiliation with or endorsement by the trademark holders, nor
by the author's employer.

The code, patterns, and architectures in this book are provided for educational purposes "as is,"
without warranty of any kind. The author assumes no responsibility for errors or omissions, or
for damages resulting from the use of the information herein. Always validate designs against your
own requirements, security review, and the current official platform documentation.

**StreamCart** is a fictional application used throughout this series as a running example. Any
resemblance to real products or companies is coincidental.

First Edition · 2026


---

# Preface

Most Android books teach you APIs. This series teaches you to **design systems**.

There is a large gap between knowing what `OkHttp`, `Room`, or `WorkManager` *are* and knowing how
to compose them into an application that works offline, survives process death, syncs reliably,
stays secure, performs on a budget phone, and can be maintained by a large team for years.
Closing that gap — moving from *API user* to *system designer* — is the goal of **Designing
Android at Scale**.

The complete work spans **100 chapters** across **eleven parts**, published as a **five-volume
series**. Every chapter follows the same rigorous 18-section structure — from problem definition
and requirements, through architecture, a complete Kotlin implementation, concurrency and failure
analysis, scaling, security, performance, testing, and observability, to a full set of
system-design interview questions and exercises. Every chapter is anchored to one running
reference application — **StreamCart**, a fictional e-commerce and streaming app — so the patterns
compose into a coherent system rather than floating as isolated recipes.

**This is Volume 1 — Foundations.** It covers
Part I and Part II:

- **Part I — Core Infrastructure** (Chapters 1–8): the networking core, persistence and the single source of truth, configuration storage, dependency injection, UI state modeling, and surviving process death — the spine the whole app hangs from.
- **Part II — Networking Patterns** (Chapters 9–18): the patterns layered on that core — debounced search and autocomplete, request de-duplication, caching, pagination, prioritization and rate limiting, idempotency, schema evolution, and resilient uploads and downloads.

You do not need to read the volumes strictly in order, but each builds on the vocabulary, the
layering, and the StreamCart reference application established across the series — most of all on
**Volume 1 — Foundations**, which introduces them.

## Who this book is for

This series is written for **intermediate-to-senior Android engineers** who are comfortable with
Kotlin and Jetpack and want to level up to **architecture and system design** — and for anyone
preparing for a **senior Android system-design interview**, where exactly this skill (composing
subsystems with explicit trade-offs under real requirements) is what's assessed. Chapter 100, the
capstone, models that interview end to end.

Let's design.


---

# How to Read This Book

**The 18-section chapter structure.** Every chapter is deliberately uniform, so you always know
where to find things: Problem Definition → Requirements → System Design Fundamentals → High-Level
Architecture → Detailed Component Design → End-to-End Data Flow → Complete Kotlin Implementation →
Concurrency & Race Conditions → Failure Scenarios → Scaling → Alternatives & Trade-offs → Security
→ Performance → Testing → Observability → Interview Preparation → Exercises → Summary & Reference
Sheet. Read a chapter top-to-bottom the first time; afterwards, the **Summary & Reference Sheet**
at the end is your quick refresher, and the **Interview Preparation** section is your drill.

**Code.** Implementations are in **Kotlin**, using current Jetpack libraries and idioms (Compose,
Coroutines/Flow, Hilt, Room). Snippets are focused on the design point rather than being
copy-paste-complete apps; package names and some glue are elided for clarity. Treat the code as a
precise description of the design, not a finished module.

**Diagrams.** Architecture, data-flow, and failure diagrams appear throughout. They are the fast
path to the mental model — study them before the prose.

**The StreamCart reference app.** Every pattern is applied to **StreamCart**, a fictional
e-commerce + streaming application (catalog, cart, checkout, payments, order tracking, streaming,
real-time updates, across phone/TV/watch). Reusing one app lets the patterns *compose*.

**Cross-references between volumes.** Because the complete work is one 100-chapter book split
across five volumes, chapters reference each other by number (for example, "Ch 29" or "Ch 75").
References outside this volume's chapter range point to other volumes of the series — see *The
Series at a Glance*, next. Each reference is a pointer to where a topic is treated in depth, not a
prerequisite you must read first.

**Conventions.** `monospace` denotes code, types, APIs, and file paths. **Bold** marks key terms
on first use. Chapter numbers in parentheses — "(Ch 5)" — are cross-references.


---

# The Series at a Glance

**Designing Android at Scale** is published in five volumes. Each is self-contained, but together they form one continuous 100-chapter system-design curriculum built on the StreamCart reference application.

- **Volume 1 — Foundations: Networking & Local Data** · Parts I–II · Chapters 1–18 *(this volume)* — the networking core, persistence and the single source of truth, threading, dependency injection, and the networking patterns layered on top — search, pagination, caching, and reliability.

- **Volume 2 — Security, Offline-First & State** · Parts III–V · Chapters 19–43 — authentication and token management, cryptography and the Keystore, secure storage and PII handling, offline-first architecture, the outbox pattern, delta sync and conflict resolution, and shared/global state.

- **Volume 3 — Lifecycle, Background & Media** · Parts VI–VII · Chapters 44–62 — the Android lifecycle and startup, foreground and background work, WorkManager, Doze and background limits, notifications, deep links and navigation, plus media playback with Media3/ExoPlayer, DRM, the camera, and file handling.

- **Volume 4 — Real-Time & Feature Architectures** · Parts VIII–IX · Chapters 63–81 — WebSocket and SSE, presence and typing, live location, BLE and nearby connections, and the commerce feature stack — feeds, recommendations, cart, checkout, payments, order tracking, reviews, and onboarding.

- **Volume 5 — Performance, Scale & Platform Breadth** · Parts X–XI · Chapters 82–100 — analytics, crash reporting, distributed tracing, performance and memory, rendering and jank, battery, baseline profiles, modularization, localization, accessibility, theming, Android TV and Wear OS, and the end-to-end StreamCart capstone.

Turn the page to begin.

