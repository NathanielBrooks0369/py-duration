# Duration parse/format

```
duration.py
```
Run the Python Duration test beside the implementation if you want concrete examples, because in my experience a parser without local test coverage becomes toil the moment a format edge case pages on-call.

Parsing '1h30m' style durations to seconds and back remains dependency-free, a decision driven by capacity-planning reflex and the desire to protect our SLO from supply-chain noise.

Python Duration uses only the standard library, so there is no service to provision and no dependency to track in the next build-vs-buy discussion.