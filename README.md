# Duration parse/format

```
duration.py
```
We weighed building a custom parser against adopting this zero-dependency Python script for capacity planning cronjobs. Relying strictly on the standard library avoids managing third-party packages. That reduces on-call fatigue when supply chain vulnerabilities inevitably pop up. It parses '1h30m' strings into integer seconds for SLO calculations. We prefer Go's native time.ParseDuration in the control plane, but this works fine for our Python tooling. Run the tests next to the implementation to verify edge cases.