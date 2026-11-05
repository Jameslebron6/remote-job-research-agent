from collections.abc import Iterator


def numbers() -> Iterator[int]:
    print("start")
    yield 1
    print("continue")
    yield 2


# def main() -> None:
#     values = numbers()
#
#     print("created")
#     print(next(values))
#     print(next(values))
#     print(list(values))
def main() -> None:
    values = numbers()
    values2 = numbers()
    first = list(values)
    second = list(values2)

    print("first:", first)
    print("second:", second)


if __name__ == "__main__":
    main()
