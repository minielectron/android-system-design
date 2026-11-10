#!/usr/bin/env python3
"""Generate personalized front/back matter (00-front-matter.md, 99-back-matter.md) for all 5
volumes of 'Designing Android at Scale'. Author details baked in; per-volume intro + glossary."""
import os

AUTHOR = "Prakash Sharma"
YEAR   = "2026"
BIO = (
"Prakash Sharma is a Senior Software Engineer at Deutsche Telekom with a decade of experience "
"building Android applications across mobile, television (TV), and set-top-box (STB) platforms. "
"Over those years he has shipped and maintained large, long-lived Android codebases — the kind "
"where architecture, offline behavior, security, performance, and multi-team maintainability are "
"not optional extras but the whole job.\n\n"
"He writes about Android architecture and engineering on **Medium**, and is the author of "
"technical books on modern Android development. He wrote *Designing Android at Scale* to close "
"the gap he kept seeing — and interviewing for — between *knowing Android APIs* and *designing "
"systems* that survive real-world scale, constraints, and teams."
)
MEDIUM = "Follow Prakash on **Medium** for articles, updates, and corrections to this series: {{MEDIUM PROFILE URL}}"

# (vol, subtitle, parts-line, short blurb for series map)
VOLS = [
 (1, "Foundations: Networking & Local Data", "Parts I–II · Chapters 1–18",
    "the networking core, persistence and the single source of truth, threading, dependency "
    "injection, and the networking patterns layered on top — search, pagination, caching, and "
    "reliability."),
 (2, "Security, Offline-First & State", "Parts III–V · Chapters 19–43",
    "authentication and token management, cryptography and the Keystore, secure storage and PII "
    "handling, offline-first architecture, the outbox pattern, delta sync and conflict "
    "resolution, and shared/global state."),
 (3, "Lifecycle, Background & Media", "Parts VI–VII · Chapters 44–62",
    "the Android lifecycle and startup, foreground and background work, WorkManager, Doze and "
    "background limits, notifications, deep links and navigation, plus media playback with "
    "Media3/ExoPlayer, DRM, the camera, and file handling."),
 (4, "Real-Time & Feature Architectures", "Parts VIII–IX · Chapters 63–81",
    "WebSocket and SSE, presence and typing, live location, BLE and nearby connections, and the "
    "commerce feature stack — feeds, recommendations, cart, checkout, payments, order tracking, "
    "reviews, and onboarding."),
 (5, "Performance, Scale & Platform Breadth", "Parts X–XI · Chapters 82–100",
    "analytics, crash reporting, distributed tracing, performance and memory, rendering and jank, "
    "battery, baseline profiles, modularization, localization, accessibility, theming, Android TV "
    "and Wear OS, and the end-to-end StreamCart capstone."),
]

# per-volume: list of (Part roman, Part name, "Chapters a–b", one-line description)
VOL_PARTS = {
 1: [("I","Core Infrastructure","Chapters 1–8",
      "the networking core, persistence and the single source of truth, configuration storage, "
      "dependency injection, UI state modeling, and surviving process death — the spine the whole "
      "app hangs from."),
     ("II","Networking Patterns","Chapters 9–18",
      "the patterns layered on that core — debounced search and autocomplete, request "
      "de-duplication, caching, pagination, prioritization and rate limiting, idempotency, schema "
      "evolution, and resilient uploads and downloads.")],
 2: [("III","Authentication & Security","Chapters 19–28",
      "authentication and token refresh, the Keystore and biometrics, session management and "
      "logout-everywhere, certificate pinning, encryption at rest, secure files, app integrity and "
      "root detection, secrets and R8, and PII-safe logging."),
     ("IV","Offline-First & Synchronization","Chapters 29–37",
      "offline-first architecture, background sync with WorkManager, the outbox pattern, delta "
      "sync, conflict resolution, cache invalidation, full-text search, Room migrations, and "
      "backup."),
     ("V","Shared & Global State","Chapters 38–43",
      "a shared cart across screens, global app state, shared ViewModel scoping, feature flags and "
      "remote config, multi-account switching, and personalization sync.")],
 3: [("VI","Lifecycle, Background & Platform","Chapters 44–55",
      "the lifecycle and startup, foreground services, Doze and background limits, alarms, FCM and "
      "the notification inbox, runtime permissions, deep links, navigation, app updates, and "
      "widgets."),
     ("VII","Media & Files","Chapters 56–62",
      "image loading and thumbnails with Coil, Media3/ExoPlayer playback, offline OTT with DRM, "
      "the CameraX capture pipeline, large-file streaming, and the Storage Access Framework.")],
 4: [("VIII","Real-Time & Connectivity","Chapters 63–70",
      "real-time communication over WebSocket, chat, presence and typing, SSE and long-polling, "
      "live location, network-state monitoring, BLE, and peer-to-peer nearby connections."),
     ("IX","Feature Architectures","Chapters 71–81",
      "domain-rich product features composed from the earlier parts — infinite feeds, optimistic "
      "updates, recommendations, wishlist, fintech-grade checkout, billing and payments, order "
      "tracking, reviews, onboarding, and in-app feedback.")],
 5: [("X","Performance, Observability & Quality","Chapters 82–93",
      "analytics, crash and ANR reporting, distributed tracing, performance monitoring, A/B "
      "testing, the error pipeline, cold start, memory, rendering and jank, battery, baseline "
      "profiles, and large-list performance."),
     ("XI","Reach, Scale & Platform Breadth","Chapters 94–100",
      "multi-module architecture at enterprise scale, localization and RTL, accessibility, "
      "theming, Android TV / STB / Fire TV, Wear OS, and the end-to-end StreamCart capstone.")],
}

# per-volume glossary: (term, definition-with-chapter-refs). Curated for that volume's chapters.
GLOSS = {
 1: [
  ("Backoff","Progressively increasing the delay between retries (often exponential, with jitter) to avoid hammering a failing server. Ch 2."),
  ("Circuit breaker","A reliability pattern that stops calling a failing dependency for a cooldown, then probes before resuming. Ch 2."),
  ("Coroutine","Kotlin's unit of structured, cancellable asynchronous work; the foundation of off-main-thread execution. Ch 3."),
  ("Debounce","Waiting for input to settle before acting, so rapid events (keystrokes) collapse into one action. Ch 9."),
  ("Dependency injection (DI)","Supplying an object's dependencies from outside rather than constructing them internally; here via Hilt. Ch 5."),
  ("DataStore","The modern typed replacement for SharedPreferences, for app configuration (Preferences and Proto). Ch 4."),
  ("Flow","A cold, asynchronous stream of values in Kotlin coroutines; the backbone of reactive data. Ch 3, Ch 6."),
  ("Idempotency key","A client-supplied key that lets a server safely de-duplicate retried mutations. Ch 15; applied to checkout in Ch 75."),
  ("Interceptor","An OkHttp hook that observes or modifies requests/responses; application vs network interceptors. Ch 1."),
  ("Mapper / DTO","A DTO is the wire shape of data; a mapper converts DTOs to domain models, isolating the app from API changes. Ch 1, Ch 16."),
  ("Pagination","Loading a large list in pages as the user scrolls, bounding memory and network. Ch 13."),
  ("Process death","The OS reclaiming a backgrounded app's process; state must be restored on return. Ch 8."),
  ("Repository","The data layer's single entry point for a domain type; owns the sources, exposes the single source of truth. Ch 1, Ch 3."),
  ("Result / Outcome type","A uniform success/failure return type that keeps exceptions out of domain and UI. Ch 1."),
  ("Retrofit","A declarative HTTP client that turns a Kotlin interface into networked calls over OkHttp. Ch 1."),
  ("Request de-duplication","Collapsing concurrent identical in-flight requests into one shared call. Ch 11."),
  ("Single source of truth (SSOT)","One authoritative local store (Room) that the UI reads from; the network updates it, the UI observes it. Ch 3."),
  ("StateFlow / UDF","A hot, state-holding Flow driving unidirectional data flow — state down, events up. Ch 6."),
  ("Timeout (call/connect/read/write)","Bounds on how long a network operation may take; callTimeout bounds the whole call. Ch 1, Ch 2."),
  ("Resumable upload","An upload that can continue from where it left off after interruption. Ch 17; downloads in Ch 18."),
 ],
 2: [
  ("Access / refresh token","Short-lived access tokens with a longer-lived refresh token; refreshed transparently on 401. Ch 19."),
  ("Android Keystore","Hardware-backed secure storage for cryptographic keys; keys never leave secure hardware. Ch 20."),
  ("Biometric authentication","Fingerprint/face authentication gating sensitive actions, tied to a Keystore key. Ch 21."),
  ("Session management","Tracking active sessions and supporting logout-everywhere across devices. Ch 22."),
  ("Certificate pinning","Restricting trust to specific server certificates/keys to resist MITM. Ch 23."),
  ("Encryption at rest","Encrypting the local database/files (e.g. SQLCipher) so data is useless if the device is compromised. Ch 24, Ch 25."),
  ("App integrity / root detection","Verifying the app and device are untampered (Play Integrity, root checks). Ch 26."),
  ("R8 / obfuscation","Shrinking and obfuscating release code; raises the reverse-engineering bar (not a secret store). Ch 27."),
  ("PII redaction","Scrubbing personally identifiable information from logs and telemetry. Ch 28."),
  ("Offline-first","Treating the local store as the source of truth so the app works without a network. Ch 29."),
  ("WorkManager","The deferrable, guaranteed background-work scheduler used for sync. Ch 30."),
  ("Outbox pattern","Writing a mutation locally plus a pending operation, then syncing it reliably (with retries). Ch 31."),
  ("Delta / incremental sync","Transferring only what changed since the last sync, not the full dataset. Ch 32."),
  ("Conflict resolution","Reconciling concurrent edits (last-writer-wins, merges, versioning) in a sync engine. Ch 33."),
  ("Cache invalidation","Deciding when cached data is stale and must be refetched or evicted. Ch 34."),
  ("Full-text search (FTS)","Indexed local text search over Room data. Ch 35."),
  ("Room migration","Evolving the local database schema safely across app versions. Ch 36."),
  ("Backup / export","Exporting, importing, and backing up user data. Ch 37."),
  ("Feature flags / remote config","Toggling features and tuning behavior remotely without an app update. Ch 41."),
  ("Multi-account isolation","Keeping each account's data strictly separate; clearing on switch/sign-out. Ch 42."),
  ("Shared ViewModel scope","Sharing state across screens via a ViewModel scoped to a navigation graph or activity. Ch 38, Ch 40."),
 ],
 3: [
  ("Lifecycle-aware component","A component that observes the lifecycle and starts/stops work at the right time. Ch 44."),
  ("Cold start","Launching when the process does not exist — the slowest, first-impression path. Ch 45; optimized in Ch 88."),
  ("Foreground service","A user-visible, long-running service for ongoing work (playback, navigation). Ch 46."),
  ("Doze / App Standby","Battery-saving modes that defer background work and network to maintenance windows. Ch 47."),
  ("Exact alarm","A precisely-timed alarm (setExactAndAllowWhileIdle) for genuinely time-critical work. Ch 48."),
  ("Push notification (FCM)","Server-initiated messages delivered over Firebase Cloud Messaging. Ch 49."),
  ("Notification inbox","An in-app center that mirrors and manages delivered notifications. Ch 50."),
  ("Runtime permission","A dangerous permission requested at runtime with a clear rationale. Ch 51."),
  ("Deep link / App Link","A URL that routes directly into app content; App Links are verified. Ch 52."),
  ("Navigation architecture","Structured, multi-module navigation between destinations. Ch 53."),
  ("In-app update","Prompting or forcing an app upgrade via Play In-App Updates. Ch 54."),
  ("Widget / shortcut","Home-screen widgets and app shortcuts for glanceable access. Ch 55."),
  ("Coil / image loading","Asynchronous image loading with memory/disk caching and downsampling. Ch 56."),
  ("Thumbnail generation","Producing and caching small preview images efficiently. Ch 57."),
  ("Media3 / ExoPlayer","The media playback stack: adaptive streaming, media session, transport. Ch 58."),
  ("DRM / offline OTT","Protected playback (Widevine) and downloading premium content for offline viewing. Ch 59."),
  ("CameraX","The Jetpack camera API for a robust capture pipeline. Ch 60."),
  ("Storage Access Framework (SAF)","System document UI and content providers for sharing files safely. Ch 62."),
 ],
 4: [
  ("WebSocket","A persistent, bidirectional connection for real-time messaging. Ch 63."),
  ("Chat / messaging architecture","Ordered, delivered, synced messages with offline support. Ch 64."),
  ("Presence / typing","Showing who is online and who is typing, efficiently. Ch 65."),
  ("SSE / long-polling","Server-push alternatives to WebSocket for one-way updates. Ch 66."),
  ("Live location","Streaming and displaying moving location updates. Ch 67."),
  ("Metered network","A connection where the user pays per byte (cellular); gates heavy transfers. Ch 68."),
  ("Bluetooth Low Energy (BLE)","Low-power device connectivity for peripherals. Ch 69."),
  ("Nearby Connections","Peer-to-peer device-to-device communication. Ch 70."),
  ("Infinite feed","An endlessly scrolling, paged list (Paging 3). Ch 71; list performance in Ch 93."),
  ("Optimistic update","Updating the UI immediately and reconciling with the server on confirm. Ch 72."),
  ("Recommendations","A personalized, ranked content feed. Ch 73."),
  ("Wishlist","A synced list of saved items. Ch 74."),
  ("Exactly-once checkout","Placing an order at most once using idempotency keys plus the outbox. Ch 75."),
  ("Play Billing","In-app purchases and subscriptions via Google Play. Ch 76."),
  ("Tokenization / PCI","Replacing card data with a token so the app never handles raw card numbers. Ch 77."),
  ("Order tracking","Real-time order status, updated via push and sync. Ch 78."),
  ("Reviews & ratings","User-generated ratings and reviews with moderation. Ch 79."),
  ("Onboarding","First-run flows and feature discovery. Ch 80."),
  ("In-app feedback / diagnostics","Capturing user feedback with privacy-safe diagnostics. Ch 81."),
 ],
 5: [
  ("Analytics pipeline","A reliable, batched, consented, PII-safe path for events. Ch 82."),
  ("Crash / ANR reporting","Capturing fatal crashes and Application-Not-Responding errors from the field. Ch 83."),
  ("Distributed tracing","Correlating a request across client and services via trace/correlation IDs. Ch 84."),
  ("Percentiles (p95/p99)","Tail latency metrics; the tail, not the average, is where users suffer. Ch 85."),
  ("Real-user monitoring (RUM)","Measuring performance from real users in the field, not just the lab. Ch 85."),
  ("A/B testing","Comparing variants with sticky assignment, guardrails, and significance. Ch 86."),
  ("Error fingerprinting","Grouping identical errors by a stable signature so thousands collapse to one issue. Ch 87."),
  ("TTID / TTFD","Time to initial display and time to full display — key startup metrics. Ch 88."),
  ("Memory leak / LeakCanary","A reachable object that should be freed; detected with LeakCanary. Ch 89."),
  ("Recomposition / jank","Excess Compose recomposition and dropped frames that cause stutter. Ch 90."),
  ("Radio tail","The cellular radio staying in a high-power state for seconds after a transfer. Ch 91."),
  ("Baseline Profile","A list of startup/critical-path methods AOT-compiled at install for a fast first launch. Ch 92."),
  ("Lazy list","A recycling list (LazyColumn) that composes only visible items with stable keys. Ch 93."),
  ("Multi-module architecture","Splitting the app into app/feature/core Gradle modules with a one-way dependency graph. Ch 94."),
  ("Localization / RTL","Translating and mirroring the UI for every language and direction. Ch 95."),
  ("Accessibility / semantics","The semantics tree that screen readers consume; targets, contrast, scalable text. Ch 96."),
  ("Design tokens / theming","A single source of color/type/shape tokens driving the whole UI, with dark/dynamic color. Ch 97."),
  ("D-pad focus","The focus-state model that drives TV/STB navigation with a remote. Ch 98."),
  ("Wear Data Layer","The API that syncs small state between a phone and a Wear OS watch. Ch 99."),
  ("Capstone","The end-to-end StreamCart system design that composes the whole book. Ch 100."),
 ],
}

def copyright_page(vol, subtitle):
    return f"""# Copyright

*Designing Android at Scale*
**Volume {vol} — {subtitle}**

Copyright © {YEAR} {AUTHOR}. All rights reserved.

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

First Edition · {YEAR}
"""

def preface(vol, subtitle):
    parts = VOL_PARTS[vol]
    part_bullets = "\n".join(
        f"- **Part {r} — {name}** ({ch}): {desc}" for (r, name, ch, desc) in parts)
    pstr = " and ".join(f"Part {r}" for (r, *_ ) in parts) if len(parts) <= 2 else \
           ", ".join(f"Part {r}" for (r, *_ ) in parts[:-1]) + f", and Part {parts[-1][0]}"
    return f"""# Preface

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

**This is Volume {vol} — {subtitle.split(':')[0] if ':' in subtitle else subtitle}.** It covers
{pstr}:

{part_bullets}

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
"""

HOW_TO_READ = """# How to Read This Book

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
"""

def series_map(cur):
    lines = []
    for (v, sub, parts, blurb) in VOLS:
        tag = " *(this volume)*" if v == cur else ""
        lines.append(f"- **Volume {v} — {sub}** · {parts}{tag} — {blurb}")
    return "# The Series at a Glance\n\n" \
        "**Designing Android at Scale** is published in five volumes. Each is self-contained, but " \
        "together they form one continuous 100-chapter system-design curriculum built on the " \
        "StreamCart reference application.\n\n" + "\n\n".join(lines) + \
        "\n\nTurn the page to begin.\n"

def glossary(vol):
    items = "\n\n".join(f"**{t}** — {d}" for (t, d) in GLOSS[vol])
    return ("# Glossary & Index of Key Terms\n\n"
            "A quick reference to the core terms introduced in this volume, with the chapters where "
            "each is treated. (Chapter numbers outside this volume's range point to other volumes "
            "of the series.)\n\n" + items + "\n")

ACK = """# Acknowledgements

This book exists because of the Android engineering community — the library authors, the writers
of official documentation and release notes, the conference speakers, and the countless engineers
who have shared hard-won lessons in blog posts, talks, and code reviews. The patterns in this
series are not invented in isolation; they are the distilled, composed practice of that community,
organized into one coherent curriculum.

Special thanks to the maintainers of the open-source libraries this book builds on — including
Kotlin and Coroutines, Jetpack (Compose, Room, WorkManager, Paging, Lifecycle), OkHttp and
Retrofit, Hilt/Dagger, and Media3 — whose work makes modern Android development what it is.

And thank you, the reader, for investing in the craft of building software that lasts.
"""

def about_author():
    return f"# About the Author\n\n{BIO}\n\n*{MEDIUM}*\n"

def also_in_series(cur):
    others = [v for v in VOLS if v[0] != cur]
    lines = [f"- **Volume {v} — {sub}** ({parts.split('·')[1].strip()}) — {blurb}"
             for (v, sub, parts, blurb) in others]
    return ("# Also in This Series\n\n"
            "If this volume was useful, the series continues:\n\n" + "\n\n".join(lines) +
            "\n\nAll five volumes build on the **StreamCart** reference application and the "
            "foundations introduced in Volume 1.\n\n"
            "*Reviews help other engineers find the series. If this book helped you, please "
            "consider leaving a rating or review.*\n")

for (vol, sub, parts, blurb) in VOLS:
    outdir = f"/home/user/android-system-design/docs/book/vol{vol}"
    os.makedirs(outdir, exist_ok=True)
    front = "\n\n---\n\n".join([copyright_page(vol, sub), preface(vol, sub), HOW_TO_READ, series_map(vol)])
    back  = "\n\n---\n\n".join([glossary(vol), ACK, about_author(), also_in_series(vol)])
    open(f"{outdir}/00-front-matter.md", "w", encoding="utf-8").write(front + "\n")
    open(f"{outdir}/99-back-matter.md", "w", encoding="utf-8").write(back + "\n")
    print(f"vol{vol}: front+back matter written")
