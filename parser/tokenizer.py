def tokenize(text: str) -> list[str]:
    tokens = []
    current = []

    i = 0
    while i < len(text):
        c = text[i]

        if c.isspace():
            if current:
                tokens.append("".join(current))
                current = []
            i += 1
            continue

        if text.startswith("//", i):
            if current:
                tokens.append("".join(current))
                current = []
            while i < len(text) and text[i] != "\n":
                i += 1
            continue

        if c in "{}=":
            if current:
                tokens.append("".join(current))
                current = []
            tokens.append(c)
            i += 1
            continue

        if c == '"':
            if current:
                tokens.append("".join(current))
                current = []
            i += 1
            start = i
            while i < len(text) and text[i] != '"':
                i += 1
            tokens.append(text[start:i])
            i += 1
            continue

        current.append(c)
        i += 1

    if current:
        tokens.append("".join(current))

    return tokens