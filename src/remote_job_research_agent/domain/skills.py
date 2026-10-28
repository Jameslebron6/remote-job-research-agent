from dataclasses import dataclass


ALIASES: dict[str, str] = {
    "postgres": "postgresql",
    "k8s": "kubernetes",
    "golang": "go",
}


@dataclass(frozen=True, slots=True)
class SkillMention:
    canonical: str
    raw: str
    source_id: str


def normalize_skill(
    raw: str,
    source_id: str,
) -> SkillMention:
    cleaned = " ".join(raw.strip().casefold().split())

    if not cleaned:
        raise ValueError("skill must not be blank")

    return SkillMention(
        canonical=ALIASES.get(cleaned, cleaned),
        raw=raw,
        source_id=source_id,
    )
