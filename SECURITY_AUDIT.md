# Security Audit — poojakira (GitHub profile README)

**Date:** 2026-08-06  
**Classification:** DOCUMENTATION — profile README linking to project repos

---

## Findings

### HIGH-1 (FIXED): adversarial-ml-lab metrics presented as measured values

**Issue:** Profile linked "0.31% → 44.87% PGD-40 robust acc (Madry AT)" as evidence, but the result JSON file in that repo has been classified as synthetic (no model weights committed).  
**Fix:** Changed to "Literature-consistent results (no weights committed)"

### MEDIUM-1: model-privacy-attacks "MIA advantage=0.42" is synthetic-data result

**Status:** Already marked "(synthetic data)" in the description column. Acceptable.

---

## Evidence Standard (documented in profile)

The README states: "All metrics link to committed JSON artifacts in their respective repositories. Synthetic data results are marked as such."

This is accurate after the adversarial-ml-lab fix.
