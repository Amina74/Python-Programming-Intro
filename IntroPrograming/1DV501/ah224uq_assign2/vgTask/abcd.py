for a in range(9):  # 1-->>10
    for b in range(0, 10):  # 0-->>10
        for c in range(0, 10):  # 0-->>10
            for d in range(1, 10):
                if 4 * (1000 * a + 100 * b + 10 * c + d) == \
                        (a + 10 * b + 100 * c + 1000 * d):
                    print("a=", a, ", b=", b, ",c=", c, ", d=", d)
# The Number is 2178
