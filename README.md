# The Issue

[https://bugs.freedesktop.org/show_bug.cgi?id=33644]()

# Solution

- Write fonts.conf as "usual", which contains multiple values in `<test>`.
- Use a separate script to convert those kind of tests into single-value test.

# Usage

Generate local.conf:

```
./conv.py
```

Copy "local.conf" to one of following path:

- /etc/fonts/local.conf
- /usr/local/etc/fonts/local.conf
- ~/.fonts.conf
