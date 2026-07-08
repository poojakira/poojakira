#!/bin/bash
set -euo pipefail
echo "Running smoke tests for poojakira..."
# Machine-readable output generation. This is a profile-repo smoke check only;
# it must not claim repo security controls were verified.
cat << 'SARIF_EOF' > sarif_output.json
{
  "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": { "driver": { "name": "poojakira Smoke Test" } },
      "results": [
        {
          "message": {
            "text": "Profile smoke test only. Repository security controls require each linked repo's own tests and audit gates."
          },
          "level": "note"
        }
      ]
    }
  ]
}
SARIF_EOF
echo "SARIF generated: sarif_output.json"
