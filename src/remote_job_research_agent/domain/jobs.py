from dataclasses import dataclass
from enum import StrEnum


class RequirementLevel(StrEnum):
    REQUIRED = "required"
    PREFERRED = "preferred"


@dataclass(frozen=True, slots=True)
class SkillRequirement:
    name: str
    level: RequirementLevel

    def __post_init__(self) -> None:
        normalized = self.name.strip().casefold()
        if not normalized:
            raise ValueError("skill name must not be blank")
        object.__setattr__(self, "name", normalized)


@dataclass(frozen=True, slots=True)
class JobDescription:
    title: str
    requirements: tuple[SkillRequirement, ...]

    def __post_init__(self) -> None:
        normalized_title = self.title.strip()
        if not normalized_title:
            raise ValueError("job title must not be blank")
        object.__setattr__(self, "title", normalized_title)


@dataclass(frozen=True, slots=True)
class CandidateProfile:
    skills: frozenset[str]

    def __post_init__(self) -> None:
        normalized = tuple(skill.strip().casefold() for skill in self.skills)
        if any(not skill for skill in normalized):
            raise ValueError("candidate skill must not be blank")
        object.__setattr__(self, "skills", frozenset(normalized))
