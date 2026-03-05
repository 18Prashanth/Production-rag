import re


def validate_citations(answer: str):
    pattern = r"\[Source: .*?, Page: \d+\]"
    matches = re.findall(pattern, answer)
    return len(matches) > 0