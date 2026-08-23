import json
from pathlib import Path

import pytest

from remote_job_research_agent.cli import (
    load_input,
    main,
)


def write_job_input(tmp_path: Path) -> Path:
    payload: dict[str, object] = {
        "job": {
            "title": "Remote AI Backend Engineer",
            "requirements": [
                {
                    "name": "Python",
                    "level": "required",
                },
                {
                    "name": "FastAPI",
                    "level": "required",
                },
                {
                    "name": "Go",
                    "level": "preferred",
                },
            ],
        },
        "candidate": {
            "skills": [
                "Java",
                "Go",
                " Python ",
            ]
        },
    }

    path = tmp_path / "job.json"
    path.write_text(
        json.dumps(payload),
        encoding="utf-8",
    )
    return path


def test_load_input_builds_domain_objects(
    tmp_path: Path,
) -> None:
    job, candidate = load_input(write_job_input(tmp_path))

    assert job.title == "Remote AI Backend Engineer"
    assert tuple(requirement.name for requirement in job.requirements) == (
        "python",
        "fastapi",
        "go",
    )
    assert candidate.skills == frozenset({"java", "go", "python"})


def test_main_prints_json_result(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main([str(write_job_input(tmp_path))])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == ('{"matched": ["python"], "missing": ["fastapi"], "score": 0.5}\n')
    assert captured.err == ""


def test_main_rejects_wrong_number_of_arguments(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main([])

    captured = capsys.readouterr()

    assert exit_code == 2
    assert captured.out == ""
    assert captured.err == ("usage: remote-job-research-agent <input.json>\n")


def test_main_reports_invalid_json(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    path = tmp_path / "invalid.json"
    path.write_text(
        "{",
        encoding="utf-8",
    )

    exit_code = main([str(path)])

    captured = capsys.readouterr()

    assert exit_code == 2
    assert captured.out == ""
    assert captured.err.startswith("error:")
