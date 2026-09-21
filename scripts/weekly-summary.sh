#!/bin/bash
# ============================================================
# weekly-summary.sh
# Generates a weekly summary from daily logs
# Usage: bash scripts/weekly-summary.sh [YYYY-WW]
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
LOG_BASE="$REPO_ROOT/daily-log"
PROGRESS_DIR="$REPO_ROOT/progress"

# Get current week's dates
YEAR=$(date +%Y)
WEEK=$(date +%U)

echo ""
echo "📊 WEEKLY STUDY SUMMARY — Week $WEEK, $YEAR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Count logs this week
LOG_COUNT=0
TOTAL_MINUTES=0

# Find logs from this week (Mon-Sun)
for i in 0 1 2 3 4 5 6; do
    # Get date for each day of the week (Linux date)
    OFFSET=$((6 - i))
    DAY=$(date -d "$OFFSET days ago" +%Y-%m-%d 2>/dev/null || date -v-${OFFSET}d +%Y-%m-%d 2>/dev/null)
    DAY_YEAR=$(echo $DAY | cut -d'-' -f1)
    DAY_MONTH=$(echo $DAY | cut -d'-' -f2)
    LOG="$LOG_BASE/$DAY_YEAR/$DAY_MONTH/$DAY.md"
    
    if [ -f "$LOG" ]; then
        LOG_COUNT=$((LOG_COUNT + 1))
        DAY_NAME=$(date -d "$DAY" +%A 2>/dev/null || date -j -f "%Y-%m-%d" "$DAY" +%A 2>/dev/null)
        echo "✅ $DAY_NAME ($DAY): Log found"
        
        # Extract topics (lines after "## What I Studied" containing "**Topic**:")
        TOPICS=$(grep "**Topic**:" "$LOG" 2>/dev/null | sed 's/.*\*\*Topic\*\*: //' || true)
        if [ -n "$TOPICS" ]; then
            echo "   📚 Topics: $TOPICS"
        fi
    else
        DAY_NAME=$(date -d "$DAY" +%A 2>/dev/null || echo "Day")
        echo "❌ $DAY_NAME ($DAY): No log"
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📈 Study Days: $LOG_COUNT / 7"

if [ $LOG_COUNT -ge 5 ]; then
    echo "🟢 Status: ON TRACK (≥5 days)"
elif [ $LOG_COUNT -ge 3 ]; then
    echo "🟡 Status: AT RISK (3-4 days)"
else
    echo "🔴 Status: INTERVENTION NEEDED (<3 days)"
fi

echo ""
echo "📝 Update your weekly review: $PROGRESS_DIR/weekly-review.md"
echo ""

# Append summary to weekly review file
WEEKLY_FILE="$PROGRESS_DIR/weekly-review.md"
{
    echo ""
    echo "---"
    echo ""
    echo "## Week $WEEK — $YEAR (Generated $(date '+%Y-%m-%d %H:%M'))"
    echo "Study days: $LOG_COUNT/7"
    echo "Status: $([ $LOG_COUNT -ge 5 ] && echo 'ON TRACK' || ([ $LOG_COUNT -ge 3 ] && echo 'AT RISK' || echo 'INTERVENTION NEEDED'))"
    echo ""
} >> "$WEEKLY_FILE"

echo "✅ Summary appended to weekly-review.md"
