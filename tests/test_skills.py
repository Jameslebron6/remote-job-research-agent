import pytest

from remote_job_research_agent.domain.skills import (
    SkillMention,
    normalize_skill,
)


def test_normalize_skill_case_and_spaces() -> None:
    result = normalize_skill(
        "  Machine   Learning  ",
        "job-001",
    )

    assert result == SkillMention(
        canonical="machine learning",
        raw="  Machine   Learning  ",
        source_id="job-001",
    )


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Postgres", "postgresql"),
        ("K8S", "kubernetes"),
        ("Golang", "go"),
        ("FastAPI", "fastapi"),
    ],
)
def test_normalize_skill_aliases(
    raw: str,
    expected: str,
) -> None:
    result = normalize_skill(raw, "job-001")

    assert result.canonical == expected


def test_normalize_skill_rejects_blank_value() -> None:
    with pytest.raises(
        ValueError,
        match="skill must not be blank",
    ):
        normalize_skill("   ", "job-001")


def test_normalize_skill_keeps_provenance() -> None:
    result = normalize_skill(
        " Python ",
        "job-042",
    )

    assert result.raw == " Python "
    assert result.source_id == "job-042"
