#!/usr/bin/env python3
"""
generate-site-nav.py
====================
Auto-generates the daily log index page for the MkDocs site.
Run by GitHub Actions before every mkdocs build.

Also updates mkdocs.yml's nav section for daily logs dynamically.
"""

import os
import glob
import yaml
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
DAILY_LOG_DOCS = DOCS_DIR / "daily-log"
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"


def get_all_logs() -> list[dict]:
    """Collect all daily log files from docs/daily-log/"""
    logs = []
    pattern = str(DAILY_LOG_DOCS / "**" / "*.md")
    for filepath in sorted(glob.glob(pattern, recursive=True)):
        path = Path(filepath)
        filename = path.stem  # e.g. 2026-09-21
        
        # Skip template and index files
        if filename in ("TEMPLATE", "index"):
            continue
        
        # Try to parse as a date
        try:
            dt = datetime.strptime(filename, "%Y-%m-%d")
            # Relative path from docs/daily-log/
            rel_path = path.relative_to(DAILY_LOG_DOCS)
            logs.append({
                "date": dt,
                "filename": filename,
                "rel_path": str(rel_path),
                "year": dt.year,
                "month": dt.strftime("%B %Y"),
                "day_name": dt.strftime("%A"),
            })
        except ValueError:
            continue
    
    return sorted(logs, key=lambda x: x["date"], reverse=True)


def generate_log_index(logs: list[dict]) -> str:
    """Generate a beautiful index markdown for daily logs."""
    lines = [
        "# 📅 Daily Study Logs",
        "",
        "> Every day of learning is a step forward. One commit at a time. 🚀",
        "",
        "---",
        "",
    ]

    # Stats block
    total = len(logs)
    if total > 0:
        first_date = min(logs, key=lambda x: x["date"])["date"]
        days_since = (datetime.now() - first_date).days + 1
        lines += [
            "## 📊 Quick Stats",
            "",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Total Study Days Logged | **{total}** |",
            f"| Journey Started | **{first_date.strftime('%B %d, %Y')}** |",
            f"| Days into Journey | **{days_since}** |",
            f"| Study Rate | **{total/max(days_since,1)*100:.0f}%** of days logged |",
            "",
            "---",
            "",
        ]

    # Group logs by month
    by_month: dict[str, list] = {}
    for log in logs:
        month_key = log["month"]
        by_month.setdefault(month_key, []).append(log)

    lines.append("## 📖 All Logs")
    lines.append("")

    for month, month_logs in by_month.items():
        lines.append(f"### {month}")
        lines.append("")
        for log in month_logs:
            day_name = log["day_name"]
            filename = log["filename"]
            rel = log["rel_path"]
            lines.append(f"- [{filename} ({day_name})]({rel})")
        lines.append("")

    lines += [
        "---",
        "",
        "!!! tip \"How to add today's log\"",
        "    Run `bash scripts/new-daily-log.sh` in your terminal to create today's log.",
        "    Once you `git push`, this page auto-updates! 🤖",
        "",
    ]

    return "\n".join(lines)


def update_mkdocs_nav_daily_logs(logs: list[dict]):
    """
    Update the mkdocs.yml nav to include all daily log entries.
    Groups by year → month → individual log.
    """
    if not logs:
        return

    # Build nav entries for daily logs
    # Structure: {year: {month: [logs]}}
    from collections import defaultdict
    tree = defaultdict(lambda: defaultdict(list))
    for log in sorted(logs, key=lambda x: x["date"], reverse=True):
        year = str(log["year"])
        month = log["date"].strftime("%B %Y")
        tree[year][month].append({
            log["filename"]: f"daily-log/{log['rel_path']}"
        })

    # Build the nav structure for daily logs section
    daily_nav = [{"Overview": "daily-log/index.md"}]
    for year in sorted(tree.keys(), reverse=True):
        month_entries = []
        for month in sorted(tree[year].keys(), reverse=True):
            month_entries.append({month: tree[year][month]})
        daily_nav.append({year: month_entries})

    # Load and update mkdocs.yml
    with open(MKDOCS_YML, "r") as f:
        config = yaml.safe_load(f)

    # Find and update the Daily Logs section in nav
    nav = config.get("nav", [])
    for i, section in enumerate(nav):
        if isinstance(section, dict):
            key = list(section.keys())[0]
            if "Daily Log" in key or "📅" in key:
                nav[i] = {key: daily_nav}
                break

    config["nav"] = nav

    with open(MKDOCS_YML, "w") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"✅ Updated mkdocs.yml nav with {len(logs)} daily log entries")


def main():
    print("🔧 Generating site navigation...")
    DAILY_LOG_DOCS.mkdir(parents=True, exist_ok=True)

    # Collect logs
    logs = get_all_logs()
    print(f"   Found {len(logs)} daily logs")

    # Generate index page
    index_content = generate_log_index(logs)
    index_file = DAILY_LOG_DOCS / "index.md"
    index_file.write_text(index_content, encoding="utf-8")
    print(f"✅ Generated: {index_file}")

    # Update mkdocs.yml nav
    update_mkdocs_nav_daily_logs(logs)

    print("🎉 Site nav generation complete!")


if __name__ == "__main__":
    main()
