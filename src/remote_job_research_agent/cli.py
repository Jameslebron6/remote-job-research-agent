import json
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import cast

from remote_job_research_agent.domain.jobs import (
    CandidateProfile,
    JobDescription,
    RequirementLevel,
    SkillRequirement,
)
from remote_job_research_agent.domain.matching import (
    MatchResult,
    analyze_match,
)


def require_object(value: object, field: str) -> Mapping[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")

    candidate = cast(dict[object, object], value)

    if not all(isinstance(key, str) for key in candidate):
        raise ValueError(f"{field} keys must be strings")

    return cast(dict[str, object], candidate)


def require_list(value: object, field: str) -> list[object]:
    if not isinstance(value, list):
        raise ValueError(f"{field} must be a list")
    return cast(list[object], value)


def require_string(value: object, field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    return value


def load_input(path: Path) -> tuple[JobDescription, CandidateProfile]:
    raw = cast(object, json.loads(path.read_text(encoding="utf-8")))
    root = require_object(raw, "root")

    job_data = require_object(root.get("job"), "job")
    candidate_data = require_object(root.get("candidate"), "candidate")

    requirements = tuple(
        SkillRequirement(
            name=require_string(
                require_object(item, "requirement").get("name"),
                "requirement.name",
            ),
            level=RequirementLevel(
                require_string(
                    require_object(item, "requirement").get("level"),
                    "requirement.level",
                )
            ),
        )
        for item in require_list(job_data.get("requirements"), "job.requirements")
    )

    job = JobDescription(
        title=require_string(job_data.get("title"), "job.title"),
        requirements=requirements,
    )

    candidate = CandidateProfile(
        skills=frozenset(
            require_string(item, "candidate.skills[]")
            for item in require_list(
                candidate_data.get("skills"),
                "candidate.skills",
            )
        )
    )

    return job, candidate


def result_payload(result: MatchResult) -> dict[str, object]:
    return {
        "score": result.score,
        "matched": list(result.matched),
        "missing": list(result.missing),
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)

    if len(args) != 1:
        print(
            "usage: remote-job-research-agent <input.json>",
            file=sys.stderr,
        )
        return 2

    try:
        job, candidate = load_input(Path(args[0]))
        result = analyze_match(job, candidate)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(
        json.dumps(
            result_payload(result),
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
