# Glossary & Index of Key Terms

A quick reference to the core terms introduced in this volume, with the chapters where each is treated. (Chapter numbers outside this volume's range point to other volumes of the series.)

**WebSocket** — A persistent, bidirectional connection for real-time messaging. Ch 63.

**Chat / messaging architecture** — Ordered, delivered, synced messages with offline support. Ch 64.

**Presence / typing** — Showing who is online and who is typing, efficiently. Ch 65.

**SSE / long-polling** — Server-push alternatives to WebSocket for one-way updates. Ch 66.

**Live location** — Streaming and displaying moving location updates. Ch 67.

**Metered network** — A connection where the user pays per byte (cellular); gates heavy transfers. Ch 68.

**Bluetooth Low Energy (BLE)** — Low-power device connectivity for peripherals. Ch 69.

**Nearby Connections** — Peer-to-peer device-to-device communication. Ch 70.

**Infinite feed** — An endlessly scrolling, paged list (Paging 3). Ch 71; list performance in Ch 93.

**Optimistic update** — Updating the UI immediately and reconciling with the server on confirm. Ch 72.

**Recommendations** — A personalized, ranked content feed. Ch 73.

**Wishlist** — A synced list of saved items. Ch 74.

**Exactly-once checkout** — Placing an order at most once using idempotency keys plus the outbox. Ch 75.

**Play Billing** — In-app purchases and subscriptions via Google Play. Ch 76.

**Tokenization / PCI** — Replacing card data with a token so the app never handles raw card numbers. Ch 77.

**Order tracking** — Real-time order status, updated via push and sync. Ch 78.

**Reviews & ratings** — User-generated ratings and reviews with moderation. Ch 79.

**Onboarding** — First-run flows and feature discovery. Ch 80.

**In-app feedback / diagnostics** — Capturing user feedback with privacy-safe diagnostics. Ch 81.


---

# Acknowledgements

This book exists because of the Android engineering community — the library authors, the writers
of official documentation and release notes, the conference speakers, and the countless engineers
who have shared hard-won lessons in blog posts, talks, and code reviews. The patterns in this
series are not invented in isolation; they are the distilled, composed practice of that community,
organized into one coherent curriculum.

Special thanks to the maintainers of the open-source libraries this book builds on — including
Kotlin and Coroutines, Jetpack (Compose, Room, WorkManager, Paging, Lifecycle), OkHttp and
Retrofit, Hilt/Dagger, and Media3 — whose work makes modern Android development what it is.

And thank you, the reader, for investing in the craft of building software that lasts.


---

# About the Author

Prakash Sharma is a Senior Software Engineer at Deutsche Telekom with a decade of experience building Android applications across mobile, television (TV), and set-top-box (STB) platforms. Over those years he has shipped and maintained large, long-lived Android codebases — the kind where architecture, offline behavior, security, performance, and multi-team maintainability are not optional extras but the whole job.

He writes about Android architecture and engineering on **Medium**, and is the author of technical books on modern Android development. He wrote *Designing Android at Scale* to close the gap he kept seeing — and interviewing for — between *knowing Android APIs* and *designing systems* that survive real-world scale, constraints, and teams.

*Follow Prakash on **Medium** for articles, updates, and corrections to this series: {{MEDIUM PROFILE URL}}*


---

# Also in This Series

If this volume was useful, the series continues:

- **Volume 1 — Foundations: Networking & Local Data** (Chapters 1–18) — the networking core, persistence and the single source of truth, threading, dependency injection, and the networking patterns layered on top — search, pagination, caching, and reliability.

- **Volume 2 — Security, Offline-First & State** (Chapters 19–43) — authentication and token management, cryptography and the Keystore, secure storage and PII handling, offline-first architecture, the outbox pattern, delta sync and conflict resolution, and shared/global state.

- **Volume 3 — Lifecycle, Background & Media** (Chapters 44–62) — the Android lifecycle and startup, foreground and background work, WorkManager, Doze and background limits, notifications, deep links and navigation, plus media playback with Media3/ExoPlayer, DRM, the camera, and file handling.

- **Volume 5 — Performance, Scale & Platform Breadth** (Chapters 82–100) — analytics, crash reporting, distributed tracing, performance and memory, rendering and jank, battery, baseline profiles, modularization, localization, accessibility, theming, Android TV and Wear OS, and the end-to-end StreamCart capstone.

All five volumes build on the **StreamCart** reference application and the foundations introduced in Volume 1.

*Reviews help other engineers find the series. If this book helped you, please consider leaving a rating or review.*

