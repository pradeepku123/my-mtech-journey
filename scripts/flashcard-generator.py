#!/usr/bin/env python3
"""
flashcard-generator.py
=======================
Generates Anki-ready flashcards from your study notes.

Usage:
    python3 scripts/flashcard-generator.py subjects/core/machine-learning/week-01-notes.md
    python3 scripts/flashcard-generator.py --all   # Process all notes files

Output:
    flashcards/YYYY-MM-DD-<subject>-cards.txt  (Anki import format)
"""

import os
import re
import sys
import glob
import argparse
from datetime import date
from pathlib import Path

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "resources" / "flashcards"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Anki-compatible separator
ANKI_SEPARATOR = "\t"  # Tab-separated for Anki import


def extract_flashcards_from_markdown(filepath: Path) -> list[dict]:
    """
    Extract flashcard candidates from markdown notes.
    
    Looks for patterns:
    1. Bold terms: **Term**: Definition
    2. Q&A blocks: Q: question / A: answer
    3. Header + first sentence pairs
    4. Code blocks with explanatory comments
    """
    cards = []
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    # Pattern 1: **Term**: Definition on same line
    pattern_definition = re.compile(r"\*\*(.+?)\*\*\s*[:–—]\s*(.+)")
    
    # Pattern 2: Q: / A: blocks
    q_line = None
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Q/A pairs
        if line.startswith("Q:") or line.startswith("**Q:**"):
            q_line = re.sub(r"(\*\*Q:\*\*|Q:)\s*", "", line)
        elif (line.startswith("A:") or line.startswith("**A:**")) and q_line:
            answer = re.sub(r"(\*\*A:\*\*|A:)\s*", "", line)
            cards.append({
                "front": q_line,
                "back": answer,
                "tag": derive_tag(filepath)
            })
            q_line = None
        
        # Bold definitions
        match = pattern_definition.search(line)
        if match:
            term, definition = match.group(1), match.group(2)
            # Skip if it's just formatting (e.g., **Note**: ...)
            if len(term) < 50 and not term.lower().startswith(("note", "tip", "warning", "important")):
                cards.append({
                    "front": f"Define: {term}",
                    "back": definition.strip(),
                    "tag": derive_tag(filepath)
                })
    
    # Pattern 3: ## Headers as questions (with next paragraph as answer)
    header_pattern = re.compile(r"^#{2,3}\s+(.+)$")
    for i, line in enumerate(lines):
        match = header_pattern.match(line.strip())
        if match:
            header_text = match.group(1).strip()
            # Collect next non-empty lines as answer (up to 3 lines)
            answer_lines = []
            for j in range(i + 1, min(i + 5, len(lines))):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith("#"):
                    answer_lines.append(next_line)
                    if len(answer_lines) >= 2:
                        break
            
            if answer_lines and len(header_text) > 10:
                cards.append({
                    "front": f"What is {header_text}?",
                    "back": " ".join(answer_lines),
                    "tag": derive_tag(filepath)
                })
    
    return cards


def derive_tag(filepath: Path) -> str:
    """Derive Anki tag from file path."""
    parts = filepath.parts
    # Try to extract subject from path
    for i, part in enumerate(parts):
        if part in ("core", "electives", "subjects"):
            if i + 1 < len(parts):
                subject = parts[i + 1].replace("-", "_")
                return f"mtech::{subject}"
    return "mtech::general"


def write_anki_file(cards: list[dict], output_path: Path, subject: str):
    """Write cards in Anki tab-separated import format."""
    with open(output_path, "w", encoding="utf-8") as f:
        # Anki import header
        f.write(f"#separator:tab\n")
        f.write(f"#html:false\n")
        f.write(f"#tags column:3\n")
        f.write(f"#deck:{subject}\n")
        f.write(f"\n")
        
        for card in cards:
            front = card["front"].replace("\t", " ").replace("\n", " ")
            back = card["back"].replace("\t", " ").replace("\n", " ")
            tag = card["tag"]
            f.write(f"{front}{ANKI_SEPARATOR}{back}{ANKI_SEPARATOR}{tag}\n")
    
    return len(cards)


def process_file(filepath: str):
    """Process a single markdown file."""
    path = Path(filepath)
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        return 0
    
    print(f"📖 Processing: {path.name}")
    cards = extract_flashcards_from_markdown(path)
    
    if not cards:
        print(f"   ⚠️  No flashcard patterns found in {path.name}")
        print(f"   💡 Tip: Use **Term**: Definition or Q: / A: patterns in your notes")
        return 0
    
    # Generate output filename
    today = date.today().isoformat()
    stem = path.stem.replace(" ", "-").lower()
    output_file = OUTPUT_DIR / f"{today}-{stem}-cards.txt"
    
    count = write_anki_file(cards, output_file, stem)
    print(f"   ✅ Generated {count} flashcards → {output_file}")
    print(f"   📥 Import in Anki: File → Import → Select this .txt file")
    
    # Preview first 3 cards
    if cards:
        print(f"\n   📋 Preview (first {min(3, len(cards))} cards):")
        for i, card in enumerate(cards[:3]):
            print(f"   [{i+1}] Q: {card['front'][:60]}...")
            print(f"       A: {card['back'][:60]}...")
    
    return count


def process_all():
    """Process all notes files in semesters/ directory."""
    notes_files = list(Path('semesters').rglob('*.md'))
    if not notes_files:
        print("📂 No notes files found in semesters/")
        return
    
    total = 0
    for filepath in notes_files:
        total += process_file(str(filepath))
    
    print(f"\n🎉 Total flashcards generated: {total}")
    print(f"📁 Saved to: {OUTPUT_DIR}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Anki flashcards from study notes"
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Markdown note files to process"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all notes in semesters/ directory"
    )
    
    args = parser.parse_args()
    
    print("🃏 Flashcard Generator for MTech AI/ML Journey")
    print("=" * 50)
    
    if args.all:
        process_all()
    elif args.files:
        for filepath in args.files:
            process_file(filepath)
    else:
        parser.print_help()
        print("\n💡 Example:")
        print("   python3 scripts/flashcard-generator.py subjects/core/machine-learning/week-01-notes.md")


if __name__ == "__main__":
    main()
