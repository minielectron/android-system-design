# Glossary & Index of Key Terms

A quick reference to the core terms introduced in this volume, with the chapters where each is treated. (Chapter numbers outside this volume's range point to other volumes of the series.)

**Lifecycle-aware component** — A component that observes the lifecycle and starts/stops work at the right time. Ch 44.

**Cold start** — Launching when the process does not exist — the slowest, first-impression path. Ch 45; optimized in Ch 88.

**Foreground service** — A user-visible, long-running service for ongoing work (playback, navigation). Ch 46.

**Doze / App Standby** — Battery-saving modes that defer background work and network to maintenance windows. Ch 47.

**Exact alarm** — A precisely-timed alarm (setExactAndAllowWhileIdle) for genuinely time-critical work. Ch 48.

**Push notification (FCM)** — Server-initiated messages delivered over Firebase Cloud Messaging. Ch 49.

**Notification inbox** — An in-app center that mirrors and manages delivered notifications. Ch 50.

**Runtime permission** — A dangerous permission requested at runtime with a clear rationale. Ch 51.

**Deep link / App Link** — A URL that routes directly into app content; App Links are verified. Ch 52.

**Navigation architecture** — Structured, multi-module navigation between destinations. Ch 53.

**In-app update** — Prompting or forcing an app upgrade via Play In-App Updates. Ch 54.

**Widget / shortcut** — Home-screen widgets and app shortcuts for glanceable access. Ch 55.

**Coil / image loading** — Asynchronous image loading with memory/disk caching and downsampling. Ch 56.

**Thumbnail generation** — Producing and caching small preview images efficiently. Ch 57.

**Media3 / ExoPlayer** — The media playback stack: adaptive streaming, media session, transport. Ch 58.

**DRM / offline OTT** — Protected playback (Widevine) and downloading premium content for offline viewing. Ch 59.

**CameraX** — The Jetpack camera API for a robust capture pipeline. Ch 60.

**Storage Access Framework (SAF)** — System document UI and content providers for sharing files safely. Ch 62.


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

- **Volume 4 — Real-Time & Feature Architectures** (Chapters 63–81) — WebSocket and SSE, presence and typing, live location, BLE and nearby connections, and the commerce feature stack — feeds, recommendations, cart, checkout, payments, order tracking, reviews, and onboarding.

- **Volume 5 — Performance, Scale & Platform Breadth** (Chapters 82–100) — analytics, crash reporting, distributed tracing, performance and memory, rendering and jank, battery, baseline profiles, modularization, localization, accessibility, theming, Android TV and Wear OS, and the end-to-end StreamCart capstone.

All five volumes build on the **StreamCart** reference application and the foundations introduced in Volume 1.

*Reviews help other engineers find the series. If this book helped you, please consider leaving a rating or review.*

