# DSA Day 04 – Pseudocode

## 1. Power of Two Check

```text
FUNCTION isTwoPower(n)

    IF n <= 0
        RETURN false

    WHILE n % 2 == 0
        n = n / 2

    RETURN n == 1

END FUNCTION
```

---

# 2. Stars in a Single Line

```text
FUNCTION patternPrinting1(n)

    s = ""

    FOR i = 1 TO n
        s = s + "*"

    PRINT s

END FUNCTION
```

---

# 3. Square Pattern

```text
FUNCTION patternPrinting2(n)

    FOR i = 1 TO n

        s = ""

        FOR j = 1 TO n
            s = s + "*"

        PRINT s

END FUNCTION
```

---

# 4. Right-Angled Star Triangle

```text
FUNCTION patternPrinting3(n)

    FOR i = 1 TO n

        s = ""

        FOR j = 1 TO i
            s = s + "*"

        PRINT s

END FUNCTION
```

---

# 5. Inverted Right-Angled Star Triangle

```text
FUNCTION patternPrinting4(n)

    FOR i = n DOWN TO 1

        s = ""

        FOR j = 1 TO i
            s = s + "*"

        PRINT s

END FUNCTION
```

---

# 6. Floyd's Triangle

```text
FUNCTION patternPrinting5(n)

    sum = 1

    FOR i = 1 TO n

        FOR j = 1 TO i

            PRINT sum

            sum = sum + 1

        MOVE TO NEXT LINE

END FUNCTION
```