from dataclasses import dataclass

from .jobs import CandidateProfile, JobDescription, RequirementLevel


@dataclass(frozen=True, slots=True)
class MatchResult:
    score: float
    matched: tuple[str, ...]
    missing: tuple[str, ...]


def analyze_match(
    job: JobDescription,
    candidate: CandidateProfile,
) -> MatchResult:
    required = frozenset(
        requirement.name
        for requirement in job.requirements
        if requirement.level is RequirementLevel.REQUIRED
    )

    matched = required & candidate.skills
    missing = required - candidate.skills

    score = 1.0 if not required else len(matched) / len(required)

    return MatchResult(
        score=round(score, 4),
        matched=tuple(sorted(matched)),
        missing=tuple(sorted(missing)),
    )
