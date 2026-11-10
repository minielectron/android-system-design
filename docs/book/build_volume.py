#!/usr/bin/env python3
"""Build a KDP-ready merged DOCX for one volume of 'Designing Android at Scale'.
Usage: build_volume.py <vol 1-5>
Assembles: YAML title block -> front matter -> (Part divider + chapters, with page breaks)
           -> back matter, strips each chapter's internal 'Chapter review (Phase 4)' QA notes,
           then runs pandoc -> docs/book/volN/Designing-Android-at-Scale-VolN.docx
"""
import sys, re, glob, subprocess, os

ROOT = "/home/user/android-system-design"
CH   = f"{ROOT}/docs/chapters"
BOOK = f"{ROOT}/docs/book"

PAGEBREAK = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'

PARTS = {
    "I":   ("Core Infrastructure", range(1, 9),
            "The foundation every feature stands on: the networking core, the persistence layer "
            "and single source of truth, configuration storage, dependency injection, UI state "
            "modeling, and surviving process death."),
    "II":  ("Networking Patterns", range(9, 19),
            "The patterns layered on the core — debounced search and autocomplete, request "
            "de-duplication, caching, pagination, prioritization and rate limiting, idempotency, "
            "schema evolution, and resilient uploads and downloads."),
    "III": ("Authentication & Security", range(19, 29),
            "Securing the app end to end: authentication and token management, certificate "
            "pinning, cryptography and the Android Keystore, encrypted and secure storage, app "
            "integrity, secrets, and privacy-safe logging."),
    "IV":  ("Offline-First & Synchronization", range(29, 38),
            "Making the app work without a network: offline-first architecture, background sync, "
            "the outbox pattern, delta sync, conflict resolution, and cache invalidation."),
    "V":   ("Shared & Global State", range(38, 44),
            "Coordinating state across the app: in-memory shared state, session and user state, "
            "feature flags and remote config, and cross-screen coordination."),
    "VI":  ("Lifecycle, Background & Platform", range(44, 56),
            "Living inside the Android platform: the lifecycle, startup, foreground and background "
            "work, Doze and app standby, alarms, WorkManager, notifications, permissions, deep "
            "links, navigation, app updates, and widgets."),
    "VII": ("Media & Files", range(56, 63),
            "Media and storage: image loading and thumbnails, Media3/ExoPlayer playback, offline "
            "OTT and DRM, camera, large-file streaming, and the Storage Access Framework."),
    "VIII":("Real-Time & Connectivity", range(63, 71),
            "Live and connected experiences: WebSocket and chat, presence and typing, SSE and "
            "long-polling, live location, network-state monitoring, BLE, and nearby connections."),
    "IX":  ("Feature Architectures", range(71, 82),
            "Domain-rich product features composed from the earlier parts: infinite feeds, "
            "optimistic updates, recommendations, wishlist, checkout, payments and billing, order "
            "tracking, reviews, onboarding, and in-app feedback."),
    "X":   ("Performance, Observability & Quality", range(82, 94),
            "Measuring and operating the app: analytics, crash and ANR reporting, distributed "
            "tracing, performance monitoring, A/B testing, error pipelines, cold start, memory, "
            "rendering and jank, battery, baseline profiles, and large-list performance."),
    "XI":  ("Reach, Scale & Platform Breadth", range(94, 101),
            "Reaching every user and device: multi-module architecture, localization and RTL, "
            "accessibility, theming, Android TV and set-top boxes, Wear OS, and the end-to-end "
            "StreamCart capstone."),
}

VOLUMES = {
    1: ("Foundations: Networking & Local Data", ["I", "II"]),
    2: ("Security, Offline-First & State",       ["III", "IV", "V"]),
    3: ("Lifecycle, Background & Media",         ["VI", "VII"]),
    4: ("Real-Time & Feature Architectures",     ["VIII", "IX"]),
    5: ("Performance, Scale & Platform Breadth", ["X", "XI"]),
}

def chapter_file(n):
    pat = f"{CH}/{n:02d}-*.md" if n < 100 else f"{CH}/{n}-*.md"
    m = glob.glob(pat)
    if not m: raise SystemExit(f"missing chapter {n} ({pat})")
    return m[0]

def strip_meta(text):
    # remove the internal 'Chapter review (Phase 4)' QA notes (and trailing final-line banner)
    text = re.split(r'\n### Chapter review \(Phase 4\)', text)[0]
    text = re.split(r'\n> \*\*This completes the book', text)[0]
    return text.rstrip() + "\n"

def build(vol):
    subtitle, part_keys = VOLUMES[vol]
    outdir = f"{BOOK}/vol{vol}"
    os.makedirs(outdir, exist_ok=True)
    parts_list = ", ".join(part_keys)

    import re as _re
    def _slug(t):
        return _re.sub(r'[\s_]+', '-', _re.sub(r'[^\w\s-]', '', t.lower())).strip('-')

    toc = []  # (level, label, anchor); level 1 = chapter (indented under its part), 0 = part/section

    def _front_back(md):
        # fence-aware: add an explicit {#id} to every H1 heading and record it for the TOC
        out, incode = [], False
        for ln in md.split("\n"):
            if ln.lstrip().startswith("```"):
                incode = not incode; out.append(ln); continue
            m = _re.match(r'^# (.+?)\s*$', ln)
            if (not incode) and m:
                title = m.group(1); a = _slug(title)
                out.append(f"# {title} {{#{a}}}"); toc.append((0, title, a))
            else:
                out.append(ln)
        return "\n".join(out)

    yaml = (
        "---\n"
        'title: "Designing Android at Scale"\n'
        f'subtitle: "Volume {vol} — {subtitle}"\n'
        'author: "Prakash Sharma"\n'
        'date: "First Edition · 2026"\n'
        "lang: en-US\n"
        "---\n"
    )
    front = _front_back(open(f"{outdir}/00-front-matter.md", encoding="utf-8").read().rstrip())

    chunks = []
    for pk in part_keys:
        title, chapters, blurb = PARTS[pk]
        pa = _slug(f"part-{pk}-{title}")
        toc.append((0, f"Part {pk} — {title}", pa))
        chunks.append(PAGEBREAK)
        chunks.append(f"# Part {pk} — {title} {{#{pa}}}\n\n{blurb}\n")
        for n in chapters:
            lines = strip_meta(open(chapter_file(n), encoding="utf-8").read()).split("\n")
            for i, ln in enumerate(lines):          # the chapter's first H1 is its title
                m = _re.match(r'^# (.+?)\s*$', ln)
                if m:
                    toc.append((1, m.group(1), f"ch-{n}"))
                    lines[i] = f"# {m.group(1)} {{#ch-{n}}}"
                    break
            chunks.append(PAGEBREAK)
            chunks.append("\n".join(lines))
    back = _front_back(open(f"{outdir}/99-back-matter.md", encoding="utf-8").read().rstrip())

    # Build a real hyperlinked Table of Contents (bookmarks + internal links -> KDP-recognized)
    toc_lines = ["# Table of Contents {#table-of-contents}", ""]
    for lvl, label, anchor in toc:
        toc_lines.append(("    " if lvl == 1 else "") + f"- [{label}](#{anchor})")
    toc_md = "\n".join(toc_lines)

    doc = [yaml, PAGEBREAK, toc_md, PAGEBREAK, front] + chunks + [PAGEBREAK, back]
    body = "\n\n".join(doc)

    # Size each diagram so it never overflows the 7x10 page: cap width at 4.2in, but when a tall
    # (portrait) diagram would exceed the text height, constrain by height instead (aspect kept).
    import struct as _struct
    MAX_W, MAX_H = 4.2, 7.4   # inches; text area on a 7x10 page is ~5.7 x 8.6in
    def _png_dims(path):
        with open(path, "rb") as f:
            f.read(16); return _struct.unpack(">II", f.read(8))   # (width, height) px
    def _img_attr(m):
        link, rel = m.group(1), m.group(2)
        try:
            w, h = _png_dims(f"{CH}/{rel}")
            return link + ("{width=%sin}" % MAX_W if (MAX_W * (h / w)) <= MAX_H
                           else "{height=%sin}" % MAX_H)
        except Exception:
            return link + "{width=%sin}" % MAX_W
    body = _re.sub(r'(!\[[^\]]*\]\((images/[^)]+\.png)\))', _img_attr, body)
    merged = f"{outdir}/_merged.md"
    open(merged, "w", encoding="utf-8").write(body)

    out = f"{outdir}/Designing-Android-at-Scale-Vol{vol}.docx"
    subprocess.run([
        "pandoc", merged,
        "-f", "markdown+task_lists+autolink_bare_uris",
        "--dpi=140",
        "--reference-doc", f"{BOOK}/reference-compact.docx",
        f"--resource-path={CH}",
        "-o", out,
    ], check=True)

    # make Word/LibreOffice refresh the TOC (and field page numbers) when the file is opened
    import zipfile, shutil, re as _re2
    tmp = out + ".tmp"
    with zipfile.ZipFile(out) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            if item == "word/settings.xml":
                txt = data.decode("utf-8")
                if "updateFields" not in txt:
                    txt = _re2.sub(r"(<w:settings[^>]*>)", r'\1<w:updateFields w:val="true"/>', txt, count=1)
                data = txt.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, out)
    print(f"built {out}")

build(int(sys.argv[1]))
