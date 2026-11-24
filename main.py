"""One-line roast of my own AI agent, for the make.fun bounty."""
import os

OUTPUT_PATH = "/output/entry.txt"

ROAST = (
    "My agent burned a million tokens, opened twelve tools, and wrote a "
    "handoff note for its own handoff \u2014 then asked me to approve the approval."
)


def main() -> None:
    # The gate accepts 1 to 200 characters, a single line, not only whitespace.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} characters, must be 1-200")
    if "\n" in ROAST or not ROAST.strip():
        raise ValueError("roast must be a single non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
