from day03_skills import normalize_skills


def count_skills(skills: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for skill in skills:
        counts[skill] = counts.get(skill, 0) + 1

    return counts


def unique_skills_keep_order(skills: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []

    for skill in skills:
        if skill not in seen:
            seen.add(skill)
            result.append(skill)

    return result


def unique_skills_sorted(skills: list[str]) -> list[str]:
    return sorted(set(skills))


def main() -> None:
    raw_skills = [" Python ", "GO", "", "python"]
    raw_before = raw_skills.copy()

    skills = normalize_skills(raw_skills)
    skills_before = skills.copy()

    counts = count_skills(skills)
    unique_ordered = unique_skills_keep_order(skills)
    unique_sorted = unique_skills_sorted(skills)

    # 1. 正常输入。
    assert skills == ["python", "go", "python"]
    assert counts == {"python": 2, "go": 1}
    assert unique_ordered == ["python", "go"]
    assert unique_sorted == ["go", "python"]

    # 2. 空列表。
    assert count_skills([]) == {}
    assert unique_skills_keep_order([]) == []
    assert unique_skills_sorted([]) == []

    # 3. 全部重复。
    repeated = ["go", "go", "go"]

    assert count_skills(repeated) == {"go": 3}
    assert unique_skills_keep_order(repeated) == ["go"]
    assert unique_skills_sorted(repeated) == ["go"]

    # 4. 重复项不相邻，并且两种顺序明显不同。
    mixed = ["go", "python", "go", "docker", "python"]

    assert unique_skills_keep_order(mixed) == [
        "go",
        "python",
        "docker",
    ]
    assert unique_skills_sorted(mixed) == [
        "docker",
        "go",
        "python",
    ]

    # 5. 输入没有被修改。
    assert raw_skills == raw_before
    assert skills == skills_before

    print("清洗后：", skills)
    print("技能计数：", counts)
    print("保序去重：", unique_ordered)
    print("排序去重：", unique_sorted)
    print("Day 4：全部检查通过")


if __name__ == "__main__":
    main()
