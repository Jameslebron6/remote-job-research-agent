import pytest

from remote_job_research_agent.domain.jobs import (
    CandidateProfile,
    JobDescription,
    RequirementLevel,
    SkillRequirement,
)


def test_skill_requirement_normalizes_name() -> None:
    requirement = SkillRequirement(
        "  PyThOn  ",
        RequirementLevel.REQUIRED,
    )

    assert requirement.name == "python"


def test_skill_requirement_rejects_blank_name() -> None:
    with pytest.raises(
        ValueError,
        match="skill name must not be blank",
    ):
        SkillRequirement(
            "   ",
            RequirementLevel.REQUIRED,
        )


def test_job_description_normalizes_title() -> None:
    job = JobDescription(
        "  AI Agent Engineer  ",
        (),
    )

    assert job.title == "AI Agent Engineer"


def test_job_description_rejects_blank_title() -> None:
    with pytest.raises(
        ValueError,
        match="job title must not be blank",
    ):
        JobDescription("   ", ())


def test_candidate_profile_normalizes_and_deduplicates_skills() -> None:
    candidate = CandidateProfile(frozenset({" Python ", "PYTHON", "Go"}))

    assert candidate.skills == frozenset({"python", "go"})


def test_candidate_profile_rejects_blank_skill() -> None:
    with pytest.raises(
        ValueError,
        match="candidate skill must not be blank",
    ):
        CandidateProfile(frozenset({"Python", "   "}))
