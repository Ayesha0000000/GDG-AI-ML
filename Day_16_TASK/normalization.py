REPLACEMENTS = {
    "kia": "kya",
    "kr": "kar",
    "krta": "karta",
    "krti": "karti",
    "he": "hai",
    "hy": "hai",
    "mje": "mujhe",
    "muje": "mujhe",
}


def normalize_roman_urdu(text):
    text = text.lower().strip()
    words = text.split()

    normalized = []
    for w in words:
        normalized.append(REPLACEMENTS.get(w, w))

    return " ".join(normalized)
