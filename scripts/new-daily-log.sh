#!/bin/bash
# ============================================================
# new-daily-log.sh
# Creates a new daily study log from the template
# Usage: bash scripts/new-daily-log.sh
# ============================================================

# Get date components
DATE=$(date +%Y-%m-%d)
YEAR=$(date +%Y)
MONTH=$(date +%m)
DAY_NAME=$(date +%A)
WEEK_NUM=$(date +%U)

# Define paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
LOG_DIR="$REPO_ROOT/daily-log/$YEAR/$MONTH"
LOG_FILE="$LOG_DIR/$DATE.md"
TEMPLATE="$REPO_ROOT/daily-log/TEMPLATE.md"

# Create directory if needed
mkdir -p "$LOG_DIR"

# Check if log already exists
if [ -f "$LOG_FILE" ]; then
    echo "✅ Log for $DATE already exists: $LOG_FILE"
    echo "Opening existing log..."
    ${EDITOR:-nano} "$LOG_FILE"
    exit 0
fi

# Copy template and substitute date
sed \
    -e "s/YYYY-MM-DD/$DATE/g" \
    -e "s/\[Monday\/Tuesday\/...\]/$DAY_NAME/g" \
    -e "s/\[W01\/W02\/...\]/W$WEEK_NUM/g" \
    "$TEMPLATE" > "$LOG_FILE"

echo ""
echo "📅 Created daily log: $LOG_FILE"
echo "📌 Date: $DATE ($DAY_NAME)"
echo ""
echo "📝 Open with: code $LOG_FILE"
echo "   Or:        cat $LOG_FILE"
echo ""

# Try to open in VS Code or default editor
if command -v code &>/dev/null; then
    code "$LOG_FILE"
elif [ -n "$EDITOR" ]; then
    $EDITOR "$LOG_FILE"
fi
