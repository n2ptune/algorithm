print(
    len(
        list(
            filter(
                lambda x: x in ['a', 'e', 'i', 'o', 'u'],
                list(input().rstrip())
            )
        )
    )
)
