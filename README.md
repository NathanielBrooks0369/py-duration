# Duration parse/format

```
duration.py
```

If you want to see how this behaves in practice, run the Python Duration test file right next to the implementation. It gives you concrete examples of what parses and what doesn't.

The core job here is turning strings like '1h30m' into a plain number of seconds, and then formatting that number back into the same human-readable shape. No external packages involved.

Python Duration is built entirely on the standard library. There's no service to spin up, no dependency to vendor, nothing to install beyond the interpreter itself. That keeps the operational surface small, which matters when you're deciding whether this stays in your image or gets pulled out later.