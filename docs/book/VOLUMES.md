# Designing Android at Scale — 5-Volume Series Blueprint (Kindle / KDP)

The 100-chapter book (**1,626 pages** across the five volumes, 7×10″) is published as a **5-volume series** for Amazon
KDP. Each volume is a merged **DOCX** (front matter → chapters → back matter), uploadable to KDP
as a Kindle eBook, plus a matching cover. Volumes are split on **whole-Part boundaries** so each
is a coherent, self-contained unit.

> **Series title:** *Designing Android at Scale*
> **Reference app across all volumes:** StreamCart (e-commerce + streaming)
> **Author byline:** `Prakash Sharma` — replace in every volume's metadata/front/back matter.

## The five volumes

| Vol | Subtitle | Parts | Chapters | Pages (7×10″) | Key topics |
|-----|----------|-------|----------|---------------|-----------|
| **1** | Foundations — Networking & Local Data | I–II | 1–18 | 295 | Core infrastructure, networking patterns, retries, caching, search |
| **2** | Security, Offline-First & State | III–V | 19–43 | 395 | Auth, crypto/Keystore, PII, offline sync, outbox, conflict resolution, shared state |
| **3** | Lifecycle, Background & Media | VI–VII | 44–62 | 307 | Lifecycle, WorkManager, Doze, notifications, Media3/ExoPlayer, DRM, files |
| **4** | Real-Time & Feature Architectures | VIII–IX | 63–81 | 318 | WebSocket, presence, BLE, feeds, checkout, payments, order tracking |
| **5** | Performance, Scale & Platform Breadth | X–XI | 82–100 | 311 | Analytics, crash, tracing, perf, memory, modularization, TV/Wear, capstone |

**Part → Volume map**

- **Vol 1:** Part I — Core Infrastructure (Ch 1–8) · Part II — Networking Patterns (Ch 9–18)
- **Vol 2:** Part III — Authentication & Security (Ch 19–28) · Part IV — Offline-First &
  Synchronization (Ch 29–37) · Part V — Shared & Global State (Ch 38–43)
- **Vol 3:** Part VI — Lifecycle, Background & Platform (Ch 44–55) · Part VII — Media & Files
  (Ch 56–62)
- **Vol 4:** Part VIII — Real-Time & Connectivity (Ch 63–70) · Part IX — Feature Architectures
  (Ch 71–81)
- **Vol 5:** Part X — Performance, Observability & Quality (Ch 82–93) · Part XI — Reach, Scale &
  Platform Breadth (Ch 94–100)

## Per-volume structure (front & back matter)

Each volume's DOCX is assembled in this order:

1. **Title page** (series title, volume subtitle, author) — from DOCX metadata.
2. **Copyright page** — © year, author, rights, disclaimer, edition.
3. **Table of Contents** — auto-generated from Heading 1 (Parts + Chapters); drives Kindle nav.
4. **Preface** — what the series is, who it's for, the StreamCart thread, how volumes fit.
5. **How to Read This Book** — the 18-section chapter structure, conventions, code/diagram notes,
   and the cross-volume reference note.
6. **The Series at a Glance** — the 5-volume map (so a reader of one volume sees the whole).
7. **Part dividers + Chapters** — each Part gets a divider page; each chapter starts on a new page.
8. **Glossary & Index of Key Terms** — alphabetical concept index (linked; reflowable-friendly).
9. **Acknowledgements.**
10. **About the Author.**
11. **Also in This Series** — cross-promotion to the other four volumes.

## KDP essentials (verified)

- **Manuscript:** DOCX accepted. Page break before each chapter. Heading 1 styles drive the
  Kindle navigable TOC (auto). Validate in **Kindle Previewer** before publishing.
- **eBook cover:** **1600 × 2560 px** (1.6:1 / 5:8), **RGB**, JPEG or TIFF, < 50 MB. One cover
  per volume (see `COVER-PROMPTS.md`).
- **Paperback cover** (optional): a single wraparound **PDF** sized by KDP's **Print Cover
  Calculator** (depends on final page count + trim size + paper) — not the 1600×2560 eBook canvas.
- **Caveat — code & diagrams on reflowable Kindle:** this is a code-heavy technical book. Wide
  code blocks and wide tables reflow imperfectly on small eReaders. Options: (a) ship the DOCX as
  a reflowable eBook and accept horizontal scroll on code; (b) publish a **print paperback** from
  the same DOCX (code renders fine at a fixed trim like 7×10"); (c) produce a **fixed-layout**
  eBook from the per-chapter PDFs for pixel-perfect code. Recommended: paperback + reflowable
  eBook from this DOCX; consider a 7×10" or 8×10" trim for the print edition.

## Build

`docs/book/build-volume.sh <vol-number>` merges that volume's front matter, chapters (with the
internal "Chapter review (Phase 4)" QA notes stripped), Part dividers, page breaks, and back
matter, then runs pandoc → `docs/book/volN/Designing-Android-at-Scale-VolN.docx`.

## TODO before publishing (per volume)

- [ ] Replace `Prakash Sharma`, `{{YEAR}}`, and `{{AUTHOR BIO}}` placeholders.
- [ ] Generate the cover (see `COVER-PROMPTS.md`) at 1600×2560 and review.
- [ ] Open the DOCX in Word/LibreOffice, confirm styles/TOC, fix any wide-code overflow.
- [ ] Validate in Kindle Previewer.
- [ ] (Optional) Set up the paperback trim + wraparound cover via the KDP calculator.
