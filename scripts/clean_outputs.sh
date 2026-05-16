#!/usr/bin/env bash
# Prune MinerU debug artifacts from outputs/mineru/.
#
# Keeps: <stem>.md, <stem>_content_list.json, images/
# Drops: <stem>_origin.pdf, <stem>_layout.pdf, <stem>_span.pdf,
#        <stem>_model.json, <stem>_middle.json, <stem>_content_list_v2.json
#
# Usage:
#   bash scripts/clean_outputs.sh             # show what would be freed (dry run)
#   bash scripts/clean_outputs.sh --apply     # actually delete
set -euo pipefail

cd "$(dirname "$0")/.."

ROOT="outputs/mineru"
APPLY=0
for arg in "$@"; do
  case $arg in
    --apply) APPLY=1 ;;
  esac
done

if [ ! -d "$ROOT" ]; then
    echo "Nothing to clean: $ROOT does not exist."
    exit 0
fi

# Patterns to drop. Anchored to the auto/ dir layout.
find_cmd=(find "$ROOT" -type f \(
    -name "*_origin.pdf"
    -o -name "*_layout.pdf"
    -o -name "*_span.pdf"
    -o -name "*_model.json"
    -o -name "*_middle.json"
    -o -name "*_content_list_v2.json"
\))

total=$("${find_cmd[@]}" -printf '%s\n' | awk '{s+=$1} END {printf "%.1f MB\n", s/1024/1024}')
count=$("${find_cmd[@]}" | wc -l)

echo "Found $count debug files totaling $total under $ROOT/"

if [ "$APPLY" = "0" ]; then
    echo ""
    echo "Dry run. Re-run with --apply to delete."
    exit 0
fi

"${find_cmd[@]}" -delete
echo "Deleted."
