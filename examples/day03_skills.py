def normalize_skills(skills: list[str]) -> list[str]:
    result: list[str] = []

    for raw in skills:
        cleaned = raw.strip().lower()

        if cleaned:
            result.append(cleaned)

    return result


def normalize_skills_comprehension(skills: list[str]) -> list[str]:
    return [raw.strip().lower() for raw in skills if raw.strip()]


def main() -> None:
    raw_skills = [" Python ", "GO", "", "python"]
    before = raw_skills.copy()

    result = normalize_skills(raw_skills)

    # 正常输入，同时检查顺序与重复项。
    assert result == ["python", "go", "python"]

    # 空列表。
    assert normalize_skills([]) == []

    # 空字符串、空格、制表符和换行符。
    assert normalize_skills(["", "   ", "\t", "\n"]) == []

    # 大小写。
    assert normalize_skills(["PYTHON", "Go", "FastAPI"]) == [
        "python",
        "go",
        "fastapi",
    ]

    # 输入内容没有被修改。
    assert raw_skills == before

    # 返回的是另一个列表对象。
    assert result is not raw_skills

    samples = [
        [" Python ", "GO", "", "python"],
        [],
        ["", "   ", "\t", "\n"],
        ["PYTHON", "Go", "FastAPI"],
    ]

    for sample in samples:
        snapshot = sample.copy()

        loop_result = normalize_skills(sample)
        comprehension_result = normalize_skills_comprehension(sample)

        assert comprehension_result == loop_result
        assert sample == snapshot
        assert comprehension_result is not sample

    print("原始输入：", raw_skills)
    print("清洗结果：", result)
    print("Day 3：循环版本检查通过")


if __name__ == "__main__":
    main()
