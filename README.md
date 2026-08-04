# Duration parse/format

```
duration.py
```

Parses and formats human-friendly durations like `1h30m` into seconds and back again, with zero dependencies. The standard library covers everything needed here, so there's no external service to stand up and no lock-in to worry about.

For usage, check the test file sitting right next to the source. It's short and shows the exact shapes the parser accepts and what `Format` returns for edge cases like zero or negative values.

I've kept the implementation deliberately small. You can read the whole thing in a minute, which matters when you're on call and need to reason about what a given string will resolve to under load. The conversion logic is straightforward: parse each unit token, accumulate seconds, and format by breaking seconds back into hours, minutes, and seconds.

If you're weighing whether to pull in a heavier time library, consider the tradeoff. A dependency adds review overhead, potential supply-chain risk, and another thing to patch. For a utility this narrow, the cost usually outweighs the benefit unless you already have the library in your dependency tree for other reasons.

One thing I'll note from a capacity-planning angle: the parser is strict about malformed input — it returns an error rather than guessing. That's intentional. Silent misparses of durations can cause bad retry backoffs or incorrect timeouts, which show up as SLO violations later. Better to fail fast and surface the problem in logs.