#!/usr/bin/env python3
"""Generate KDP publishing metadata (metadata.md) for each of the 5 volumes:
title, subtitle, series, description, keywords, categories."""
import os

AUTHOR = "Prakash Sharma"
SERIES = "Designing Android at Scale"

VOLS = {
1: dict(
  subtitle="Foundations: Networking & Local Data",
  parts="Parts I–II · Chapters 1–18",
  desc="""**Most Android books teach you APIs. This one teaches you to design systems.**

Volume 1 of *Designing Android at Scale* lays the foundation every production Android app is built on: a clean networking core, a single-source-of-truth data layer, and the patterns that make data loading fast and reliable.

Across 18 chapters you'll **design — not just use** — the pieces that matter. A networking core on OkHttp and Retrofit with a uniform error model; timeouts, retries, backoff, and circuit breaking; a Room-backed single source of truth with reactive Flows; DataStore, dependency injection with Hilt, unidirectional UI state, and surviving process death. Then the networking patterns layered on top: debounced search and autocomplete, request de-duplication, caching strategies, Paging 3, client-side rate limiting, idempotency for safe mutations, API schema evolution, and resumable uploads and downloads.

Every chapter follows the same rigorous 18-section structure — problem, requirements, architecture, a complete Kotlin implementation, concurrency and failure analysis, scaling, security, performance, testing, and observability — and ends with a full set of **system-design interview questions** and hands-on exercises. Everything is built on one running reference app, **StreamCart** (e-commerce + streaming), so the patterns *compose* into a real system instead of floating as isolated recipes.

Written for **intermediate-to-senior Android engineers** who want to move from *API user* to *system designer* — and for anyone preparing for a **senior Android system-design interview**.

By Prakash Sharma, a Senior Software Engineer with a decade of Android experience across mobile, TV, and set-top-box platforms.""",
  keywords=[
    "android system design",
    "kotlin coroutines and flow",
    "retrofit okhttp networking",
    "room database android",
    "android architecture guide",
    "android interview preparation",
    "dependency injection hilt",
  ]),
2: dict(
  subtitle="Security, Offline-First & State",
  parts="Parts III–V · Chapters 19–43",
  desc="""**Build Android apps that stay secure, work offline, and keep their state straight.**

Volume 2 of *Designing Android at Scale* tackles the three hardest things about a real production app: **security, offline-first data, and shared state.**

Across 25 chapters you'll design authentication and token refresh, credential storage in the Android Keystore, biometric auth, session management with logout-everywhere, certificate pinning, encryption at rest, secure file storage, app-integrity and root detection, secrets and R8, and PII-safe logging. Then the offline-first core: an architecture where the local store is the source of truth, background sync with WorkManager, the **outbox pattern** for reliable writes, delta sync, **conflict resolution** and a sync engine, cache invalidation, full-text search, Room migrations, and backup. And finally shared and global state: a cart shared across screens, app-wide state, shared ViewModel scoping, feature flags and remote config, multi-account switching, and personalization sync.

Every chapter follows the same rigorous 18-section structure — problem, requirements, architecture, a complete Kotlin implementation, concurrency and failure analysis, scaling, security, performance, testing, and observability — and ends with a full set of **system-design interview questions** and exercises. All of it is built on one running reference app, **StreamCart**, so the patterns *compose* into a coherent system.

Written for **intermediate-to-senior Android engineers** leveling up to architecture and system design, and for anyone preparing for a **senior Android system-design interview**.

By Prakash Sharma, a Senior Software Engineer with a decade of Android experience across mobile, TV, and set-top-box platforms.""",
  keywords=[
    "android security",
    "offline first android",
    "android keystore encryption",
    "workmanager background sync",
    "android data synchronization",
    "kotlin android architecture",
    "android system design interview",
  ]),
3: dict(
  subtitle="Lifecycle, Background & Media",
  parts="Parts VI–VII · Chapters 44–62",
  desc="""**Master the Android platform: lifecycle, background work, and media.**

Volume 3 of *Designing Android at Scale* is about living inside the Android platform — the lifecycle, background execution, and the media stack that power real apps.

Across 19 chapters you'll design application lifecycle management and app-startup optimization, foreground services, working with Doze and background execution limits, exact alarms, a Firebase Cloud Messaging (FCM) push architecture, a notification inbox, runtime permissions, deep links and App Links, multi-module navigation, app-update and forced-upgrade flows, and widgets and shortcuts. Then the media and files layer: image loading and caching with Coil, thumbnail generation, **Media3/ExoPlayer** playback state, offline OTT downloads with **DRM**, the CameraX capture pipeline, large-file and streaming handling, and file sharing through the Storage Access Framework.

Every chapter follows the same rigorous 18-section structure — problem, requirements, architecture, a complete Kotlin implementation, concurrency and failure analysis, scaling, security, performance, testing, and observability — and ends with a full set of **system-design interview questions** and exercises. Everything is built on one running reference app, **StreamCart** (e-commerce + streaming), so the patterns *compose* into a coherent system.

Written for **intermediate-to-senior Android engineers** leveling up to architecture and system design, and for anyone preparing for a **senior Android system-design interview**.

By Prakash Sharma, a Senior Software Engineer with a decade of Android experience across mobile, TV, and set-top-box platforms.""",
  keywords=[
    "android lifecycle management",
    "workmanager background tasks",
    "exoplayer media3 android",
    "android push notifications fcm",
    "android media playback drm",
    "android background processing",
    "kotlin android development",
  ]),
4: dict(
  subtitle="Real-Time & Feature Architectures",
  parts="Parts VIII–IX · Chapters 63–81",
  desc="""**Design real-time Android features and the commerce stack that pays the bills.**

Volume 4 of *Designing Android at Scale* covers live, connected experiences and the domain-rich product features that compose everything from the earlier volumes.

Across 19 chapters you'll design real-time communication over WebSocket, a chat and messaging architecture, presence and typing indicators, Server-Sent Events and long-polling, live location tracking, network-state monitoring, Bluetooth Low Energy (BLE), and peer-to-peer nearby connections. Then the feature architectures: an infinite scrolling feed, optimistic updates for likes and comments, a recommendations feed, a wishlist, a **fintech-grade checkout flow** with exactly-once semantics, in-app purchases and Play Billing, wallet and payments with tokenization, order tracking with live status, reviews and ratings, onboarding and feature discovery, and in-app feedback and diagnostics.

Every chapter follows the same rigorous 18-section structure — problem, requirements, architecture, a complete Kotlin implementation, concurrency and failure analysis, scaling, security, performance, testing, and observability — and ends with a full set of **system-design interview questions** and exercises. All of it is built on one running reference app, **StreamCart**, so the patterns *compose* into a real system.

Written for **intermediate-to-senior Android engineers** leveling up to architecture and system design, and for anyone preparing for a **senior Android system-design interview**.

By Prakash Sharma, a Senior Software Engineer with a decade of Android experience across mobile, TV, and set-top-box platforms.""",
  keywords=[
    "android websocket real time",
    "android chat app architecture",
    "jetpack compose feature design",
    "android checkout and payments",
    "mobile system design interview",
    "kotlin android app development",
    "android realtime connectivity",
  ]),
5: dict(
  subtitle="Performance, Scale & Platform Breadth",
  parts="Parts X–XI · Chapters 82–100",
  desc="""**Make Android apps fast, observable, and ready for every device — then put it all together.**

Volume 5 of *Designing Android at Scale* is about measuring and operating the app, scaling the codebase, reaching every user and device, and composing the whole system end to end.

Across 19 chapters you'll design centralized logging and analytics, crash and ANR reporting, distributed tracing with correlation IDs, performance monitoring (startup, frames, custom metrics), A/B testing and experimentation, and an error-classification telemetry pipeline. Then performance itself: cold-start optimization, memory management and leak prevention, rendering performance and jank in Jetpack Compose, battery and network efficiency, baseline profiles and R8, and large-list performance. Finally, reach and platform breadth: multi-module architecture at enterprise scale, localization and RTL, accessibility, theming and dynamic configuration, **Android TV / STB / Fire TV**, **Wear OS**, and a full end-to-end **capstone** that designs StreamCart from requirements to trade-offs.

Every chapter follows the same rigorous 18-section structure — problem, requirements, architecture, a complete Kotlin implementation, concurrency and failure analysis, scaling, security, performance, testing, and observability — and ends with a full set of **system-design interview questions** and exercises. The closing capstone doubles as a complete senior-interview walkthrough.

Written for **intermediate-to-senior Android engineers** leveling up to architecture and system design, and for anyone preparing for a **senior Android system-design interview**.

By Prakash Sharma, a Senior Software Engineer with a decade of Android experience across mobile, TV, and set-top-box platforms.""",
  keywords=[
    "android performance optimization",
    "jetpack compose performance",
    "android baseline profiles r8",
    "android tv development",
    "wear os development",
    "android app scaling architecture",
    "android accessibility localization",
  ]),
}

CATEGORIES = [
  "COMPUTERS › Programming › Mobile Devices",
  "COMPUTERS › Software Development & Engineering › General",
  "COMPUTERS › Programming Languages › Java  (Kotlin runs on the JVM)",
]

def char_count(s):  # KDP description limit is 4000 characters
    return len(s)

for vol, d in VOLS.items():
    full_subtitle = f"Volume {vol} — {d['subtitle']}"
    md = f"""# KDP Publishing Metadata — Volume {vol}

> Paste these into the Amazon KDP listing for this volume. The description field accepts up to
> **4000 characters** and limited HTML (bold, italics, lists). Keywords are **7 slots, ≤50 chars
> each**. Set up the **Series** so all five volumes link together.

## Title
```
Designing Android at Scale
```

## Subtitle
```
{full_subtitle}: {d['parts']}
```
*(If your cover shows the parts/chapters strip, you can shorten the KDP subtitle to just
`{full_subtitle}`.)*

## Series
- **Series name:** `Designing Android at Scale`
- **Volume / number in series:** `{vol}` (Book {vol} of 5)

## Author
```
{AUTHOR}
```

## Language
English

## Description  ({char_count(d['desc'])} characters — within KDP's 4000 limit)

{d['desc']}

## Keywords (7 slots)

| # | Keyword |
|---|---------|
""" + "\n".join(f"| {i+1} | {k} |" for i, k in enumerate(d['keywords'])) + f"""

*(Plain list for easy copy-paste:)*
```
{chr(10).join(d['keywords'])}
```

## Categories / BISAC (choose up to 3)
""" + "\n".join(f"- {c}" for c in CATEGORIES) + f"""

## Other listing fields
- **Contributors:** {AUTHOR} (Author)
- **Edition:** First Edition
- **Publication:** 2026
- **Adult content:** No
- **Pricing/territories:** your choice (KDP sets these at upload)
- **Cover:** 1600 × 2560 px (see `../COVER-PROMPTS.md`, Volume {vol})
"""
    out = f"/home/user/android-system-design/docs/book/vol{vol}/metadata.md"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(md)
    print(f"vol{vol}/metadata.md  (description {char_count(d['desc'])} chars, {len(d['keywords'])} keywords)")
