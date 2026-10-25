from collections.abc import Iterator


def numbers() -> Iterator[int]:
    print("start")
    yield 1

    print("continue")
    yield 2


def main() -> None:
    skills = ["python", "go", "java"]

    iterator = iter(skills)

    first = next(iterator)
    second = next(iterator)
    remaining = list(iterator)
    again = list(iterator)

    print(first)
    print(second)
    print(remaining)
    print(again)

    generated_numbers = numbers()

    print("generator created")
    print(next(generated_numbers))
    print(next(generated_numbers))


if __name__ == "__main__":
    main()
