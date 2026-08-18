# Duration parse/format

```
duration.py
```
We keep the Python Duration test colocated with the implementation so the examples stay honest about edge cases instead of drifting into docs that lie.

Parsing `1h30m` style strings into seconds and formatting them back is a solved problem if you stay inside the standard library, and that is the only constraint we accept here: no extra dependency to vet, patch, or page someone about at 3am.

Python Duration pulls from nothing but the standard library, so there is no service to provision, no version matrix to track, and no lock-in to weigh against the next renewal cycle.