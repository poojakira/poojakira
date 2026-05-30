#!/bin/bash

set -euo pipefail

EVIDENCE_DIR="/home/ubuntu/evidence"
mkdir -p "$EVIDENCE_DIR"

REPOS=(
  "secure_ml"
  "ML-Privacy-Attacks"
  "production-ml-platform"
  "coderev-agents"
  "docquery"
  "Model-Supply-Chain-Auditor"
  "LLM-Guard-Scanner"
  "Adversarial-Robustness-Toolkit"
  "PulseNet-RUL-Forecasting"
)

ALL_SARIF_RESULTS=()

for repo in "${REPOS[@]}"; do
  echo "--- Processing $repo ---"
  REPO_PATH="/home/ubuntu/repos/$repo"
  
  # Update or clone repo
  if [ -d "$REPO_PATH/.git" ]; then
    echo "Updating $repo..."
    (cd "$REPO_PATH" && git pull)
  else
    echo "Cloning $repo..."
    gh repo clone "poojakira/$repo" "$REPO_PATH"
  fi

  # Run smoke test
  if [ -f "$REPO_PATH/smoke_test.sh" ]; then
    echo "Running smoke_test.sh for $repo..."
    (cd "$REPO_PATH" && ./smoke_test.sh)
    
    # Aggregate SARIF output
    if [ -f "$REPO_PATH/sarif_output.json" ]; then
      SARIF_CONTENT=$(cat "$REPO_PATH/sarif_output.json")
      ALL_SARIF_RESULTS+=("$SARIF_CONTENT")
      echo "SARIF output found for $repo."
    else
      echo "No sarif_output.json found for $repo."
    fi
  else
    echo "No smoke_test.sh found for $repo."
  fi
  echo
done

# Aggregate all SARIF results into a single evidence.sarif
if [ ${#ALL_SARIF_RESULTS[@]} -gt 0 ]; then
  echo "Aggregating SARIF results..."
  echo "{\"runs\": [" > "$EVIDENCE_DIR/evidence.sarif"
  for i in "${!ALL_SARIF_RESULTS[@]}"; do
    echo "${ALL_SARIF_RESULTS[$i]}" | jq ".runs[0]" >> "$EVIDENCE_DIR/evidence.sarif"
    if [ "$i" -lt $((${#ALL_SARIF_RESULTS[@]} - 1)) ]; then
      echo "," >> "$EVIDENCE_DIR/evidence.sarif"
    fi
  done
  echo "]}" >> "$EVIDENCE_DIR/evidence.sarif"
  echo "Aggregated SARIF saved to $EVIDENCE_DIR/evidence.sarif"
else
  echo "No SARIF results to aggregate."
fi

# Create a dummy evidence.json for now (will be replaced with actual aggregation later)
cat << EOF > "$EVIDENCE_DIR/evidence.json"
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "status": "success",
  "message": "Evidence script ran successfully. SARIF output aggregated."
}
EOF

echo "Evidence generated in $EVIDENCE_DIR/evidence.json and $EVIDENCE_DIR/evidence.sarif"
