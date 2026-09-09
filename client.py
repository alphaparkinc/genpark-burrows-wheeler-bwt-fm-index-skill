class BurrowsWheelerTransform:
    """Burrows-Wheeler Transform (BWT) & Inversion engine."""
    def transform(self, text: str) -> dict:
        if not text.endswith("$"):
            s = text + "$"
        else:
            s = text

        rotations = sorted(s[i:] + s[:i] for i in range(len(s)))
        bwt_str = "".join(r[-1] for r in rotations)
        first_col = "".join(r[0] for r in rotations)

        return {
            "original_length": len(text),
            "bwt_string": bwt_str,
            "first_column": first_col
        }

    def inverse_transform(self, bwt_str: str) -> str:
        n = len(bwt_str)
        table = [""] * n
        for _ in range(n):
            table = sorted(bwt_str[i] + table[i] for i in range(n))
        for row in table:
            if row.endswith("$"):
                return row[:-1]
        return ""
