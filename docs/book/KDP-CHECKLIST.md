# KDP Publishing Checklist — *Designing Android at Scale* (5 volumes)

A one-page runbook for publishing the series on Amazon KDP (kdp.amazon.com). Do the **one-time
series setup** once, then repeat the **per-volume** steps for each of the five books.

## 0. What you already have (in this repo)

| Asset | Where |
|-------|-------|
| 5 manuscripts (DOCX, with clickable TOC) | `docs/book/vol{1..5}/Designing-Android-at-Scale-Vol*.docx` |
| Per-volume listing metadata | `docs/book/vol{1..5}/metadata.md` |
| Series page metadata | `docs/book/SERIES-METADATA.md` |
| Cover prompts (5, cohesive) | `docs/book/COVER-PROMPTS.md` |
| Plan + KDP guidelines | `docs/book/VOLUMES.md` |

**Per-volume quick reference**

| Vol | Subtitle | Chapters | Paperback pp (7×10") | Cover accent |
|-----|----------|----------|----------------------|--------------|
| 1 | Foundations: Networking & Local Data | 1–18 | 296 | Teal `#1DB596` |
| 2 | Security, Offline-First & State | 19–43 | 397 | Crimson `#E5484D` |
| 3 | Lifecycle, Background & Media | 44–62 | 306 | Violet `#8A5CF6` |
| 4 | Real-Time & Feature Architectures | 63–81 | 316 | Azure `#2E90FA` |
| 5 | Performance, Scale & Platform Breadth | 82–100 | 306 | Amber `#F79009` |

---

## 1. Before you upload anything (per volume)

- [ ] **Open the DOCX in Word/LibreOffice**, skim it, and confirm the **Table of Contents** page
      shows clickable links (it does — bookmarks + hyperlinks). If prompted to "update fields,"
      allow it.
- [ ] **Replace the one remaining placeholder:** search for `{{MEDIUM PROFILE URL}}` in *About the
      Author* and insert your Medium link (or delete the line).
- [ ] **Check wide code blocks** — scan a few code-heavy pages. On the reflowable Kindle eBook,
      very wide code lines get a horizontal-scroll strip; that's expected. If any line is
      unacceptably long, you can shorten it in the chapter source and rebuild.
- [ ] **Generate the cover** from `COVER-PROMPTS.md` (that volume's prompt) at **1600 × 2560 px**,
      RGB, JPEG or TIFF, < 50 MB. Put the real title text on crisply (Canva/Figma) if the AI text
      is imperfect.

---

## 2. One-time series setup (do once)

- [ ] In KDP, create (or plan) a **Series**: **Bookshelf → Create → Series**, or add each book to a
      series during setup.
  - Series title: **`Designing Android at Scale`** (from `SERIES-METADATA.md`)
  - Series description: paste from `SERIES-METADATA.md` (1,983 chars; HTML bold OK)
  - Reading order: Volume 1 → 5 (set each book's number when you add it)
- [ ] Download **Kindle Previewer** (free, Amazon) — you'll validate every volume in it.

---

## 3. Create each eBook (Kindle) — repeat per volume

**KDP → Create → Kindle eBook**

### Details tab
- [ ] **Language:** English
- [ ] **Book Title:** `Designing Android at Scale`
- [ ] **Subtitle:** from that volume's `metadata.md` (e.g. `Volume 1 — Foundations: Networking &
      Local Data`)
- [ ] **Series:** `Designing Android at Scale`, number = volume number (1–5)
- [ ] **Author:** `Prakash Sharma`
- [ ] **Description:** paste from `metadata.md` (HTML bold/italics/lists render on the listing)
- [ ] **Publishing rights:** "I own the copyright…"
- [ ] **Keywords (7):** paste the 7 from `metadata.md`
- [ ] **Categories:** choose up to 3 (BISAC suggestions in `metadata.md`)
- [ ] **Age/grade:** leave blank (not a children's book)

### Content tab
- [ ] **Manuscript:** upload the volume's **DOCX**. Wait for conversion.
- [ ] **KDP ISBN:** not required for Kindle eBooks (KDP assigns an ASIN).
- [ ] **Cover:** upload your 1600 × 2560 cover (or use the Cover Creator).
- [ ] **Kindle eBook Preview:** launch the previewer. **Confirm:**
  - [ ] The **Table of Contents** appears and its links jump to the right chapters.
  - [ ] No "Missing Table of Contents" warning (fixed — the DOCX has a real hyperlink TOC).
  - [ ] Images/diagrams render; code blocks are readable (horizontal scroll on wide lines is OK).
  - [ ] Title page, Copyright, Preface, chapters, and back matter are in order.
- [ ] **(Recommended) Set the "Start reading" location** in the previewer to **Chapter 1 / Part I**
      (so the book opens at the content, not the title page) if your previewer offers it.

### Pricing tab
- [ ] **KDP Select** (optional): 90-day Amazon exclusivity for Kindle Unlimited + promos — your
      choice.
- [ ] **Territories:** All.
- [ ] **Royalty & price:** pick the **70%** tier (list price **$2.99–$9.99**) if you want 70%;
      otherwise 35%. (Technical titles commonly sit $7.99–$12.99 for the eBook; the 70% tier caps
      at $9.99.)
- [ ] **Publish** (or save as draft until all five are ready to launch together).

---

## 4. Optional: paperback edition (per volume)

**KDP → Create → Paperback** (same Details tab as above)

- [ ] **ISBN:** get a **free KDP ISBN** (or use your own). Note: a paperback needs its own ISBN;
      the eBook does not.
- [ ] **Trim size:** **7 × 10 in** (what the manuscript is laid out for). Interior margins are
      already set in the DOCX; KDP may ask you to confirm/adjust gutter for the page count.
- [ ] **Bleed:** No (diagrams don't run to the edge). **Paper:** white. **Ink:** black & white
      (there's no color interior).
- [ ] **Manuscript:** the **same DOCX** works, or export it to PDF first for exact fidelity.
- [ ] **Cover:** a **wraparound PDF** (back + spine + front). Use KDP's **Print Cover Calculator**
      with the trim (7×10"), page count (see table above), paper type → it gives exact dimensions
      and a template. Reuse the eBook's accent color + artwork for the front; spine text =
      `Designing Android at Scale · Vol N`.
- [ ] Preview the printed interior; confirm nothing is cut off by the gutter.
- [ ] Set print price (KDP shows the minimum based on page count/printing cost) and publish.

> **Reflowable eBook vs. print:** the eBook has **no fixed page size** — it reflows to the reader's
> device and font size (so "page count" there is only an estimate). The **7×10"** trim and the page
> counts above apply only to the paperback.

---

## 5. After publishing

- [ ] Verify each book shows the correct **series** grouping on its Amazon page.
- [ ] Double-check the **Look Inside** preview once Amazon processes it (can take a few hours).
- [ ] If you published the paperbacks, **link** the Kindle + paperback editions (KDP usually does
      this automatically when they share title/author).
- [ ] Consider launching all five **together** so the series page looks complete on day one.

---

## 6. If you change the books later

Everything is generated from source in this repo:

```bash
# rebuild one volume's DOCX after editing chapters or matter
python3 docs/book/build_volume.py <1-5>

# regenerate per-volume + series metadata
python3 docs/book/make_metadata.py

# regenerate front/back matter (author bio, prefaces, glossaries)
python3 docs/book/make_matter.py
```

Then re-upload the changed DOCX and re-paste any changed metadata. The TOC, page breaks, image
sizing, and compact 7×10" styling are all applied automatically by `build_volume.py`.
