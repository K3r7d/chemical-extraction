#!/usr/bin/env bash
# Integration test for setup_local.sh.
# Copies the project to a tmpdir, runs setup in TEST_MODE, checks imports, then deletes everything.
#
# Usage:
#   bash scripts/test_setup_local.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEST_DIR="$(mktemp -d)"

cleanup() {
    echo ""
    echo "=== Cleaning up ${TEST_DIR} ==="
    rm -rf "${TEST_DIR}"
}
trap cleanup EXIT

echo "=== test_setup_local: running in ${TEST_DIR} ==="
echo ""

# ── Copy only what setup_local.sh needs ───────────────────────────────────────
mkdir -p "${TEST_DIR}/scripts"
cp "${REPO_ROOT}/pyproject.toml" "${TEST_DIR}/"
[ -f "${REPO_ROOT}/uv.lock" ] && cp "${REPO_ROOT}/uv.lock" "${TEST_DIR}/"
cp -r "${REPO_ROOT}/src" "${TEST_DIR}/"
cp "${REPO_ROOT}/scripts/setup_local.sh" "${TEST_DIR}/scripts/"

cd "${TEST_DIR}"

export A2I2_TEST_MODE=1

# ── Run setup ─────────────────────────────────────────────────────────────────
bash scripts/setup_local.sh

# ── Verify imports in the created venv ────────────────────────────────────────
echo ""
echo "=== Verifying imports ==="

PASS=0
FAIL=0

check() {
    local label="$1"
    local stmt="$2"
    local err
    if err=$("${TEST_DIR}/.venv/bin/python" -c "$stmt" 2>&1); then
        printf "  [PASS] %s\n" "$label"
        PASS=$((PASS + 1))
    else
        printf "  [FAIL] %s\n" "$label"
        printf "         %s\n" "$(echo "$err" | tail -1)"
        FAIL=$((FAIL + 1))
    fi
}

check "a2i2_extraction"  "import a2i2_extraction"
check "fastapi"          "import fastapi"
check "uvicorn"          "import uvicorn"
check "httpx"            "import httpx"
check "structlog"        "import structlog"
check "rdkit"            "from rdkit import Chem"

echo ""
if [ "$FAIL" = "0" ]; then
    echo "=== All ${PASS} checks passed ==="
else
    echo "=== ${FAIL} check(s) FAILED (${PASS} passed) ==="
    exit 1
fi
