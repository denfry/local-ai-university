"""Objective mastery scoring.

The LLM never assigns its own mastery score (see docs/mastery.md). This
package is intended to compute mastery from observed evidence only:

- number of attempts and pass rate, weighted by problem difficulty;
- recency (older evidence decays in influence);
- performance on transfer tasks vs. tasks resembling studied examples;
- exam results (no memory/hints) weighted more heavily than practice;
- per-dimension sub-scores: understanding, implementation, debugging,
  explanation, transfer.

Confidence must stay low until enough independent evidence exists — a
single solved problem cannot produce high mastery. This invariant is
expected to be covered by tests once the formula is implemented.

No scoring logic exists yet in this package.
"""
