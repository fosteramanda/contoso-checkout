# Checkout v2.3

Public-facing docs for the new checkout experience.

## What's new

- **Cart summary panel** — items, totals, and applicable promos are now
  visible on every step of checkout.
- **Faster payment confirmation** — payment intent handling is now async,
  reducing perceived latency on the confirm step.
- **Improved telemetry** — every checkout step now emits a structured
  event for funnel analysis.

## Migration notes

No customer action required. The new experience rolls out behind the
`checkout.v2.enabled` feature flag, defaulting on per ring.

## Known limitations

- Gift-card payments still route through the legacy confirm path.
  Tracked in #4.
