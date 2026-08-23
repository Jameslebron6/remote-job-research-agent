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


def test_analyze_match_reports_matched_missing_and_score() -> None:
    job = JobDescription(
        "Remote AI Backend Engineer",
        (
            SkillRequirement(
                "Python",
                RequirementLevel.REQUIRED,
            ),
            SkillRequirement(
                "FastAPI",
                RequirementLevel.REQUIRED,
            ),
            SkillRequirement(
                "Go",
                RequirementLevel.PREFERRED,
            ),
        ),
    )
    candidate = CandidateProfile(frozenset({" Python ", "Go"}))

    result = analyze_match(job, candidate)

    assert result == MatchResult(
        score=0.5,
        matched=("python",),
        missing=("fastapi",),
    )


def test_analyze_match_ignores_preferred_requirements() -> None:
    job = JobDescription(
        "AI Agent Engineer",
        (
            SkillRequirement(
                "MCP",
                RequirementLevel.PREFERRED,
            ),
        ),
    )

    result = analyze_match(
        job,
        CandidateProfile(frozenset()),
    )

    assert result == MatchResult(
        score=1.0,
        matched=(),
        missing=(),
    )


def test_analyze_match_returns_zero_when_all_required_skills_are_missing() -> None:
    job = JobDescription(
        "Python Engineer",
        (
            SkillRequirement(
                "Python",
                RequirementLevel.REQUIRED,
            ),
        ),
    )

    result = analyze_match(
        job,
        CandidateProfile(frozenset({"Java"})),
    )

    assert result.score == 0.0
    assert result.matched == ()
    assert result.missing == ("python",)
