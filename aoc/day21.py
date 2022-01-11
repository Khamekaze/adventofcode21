def throw_die():
    p1_start = 4
    p2_start = 8
    p1_throws = 0
    p1_total = 0
    die_val = 1
    for i in range(3):
        p1_throws += die_val
        die_val += 1
        if die_val > 100:
            die_val = 1
    p1_score = p1_start + p1_throws
    p1_score = p1_score % 11
    print(p1_score)


if __name__ == '__main__':
    throw_die()
