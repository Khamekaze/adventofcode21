def count_steps(current_pos, steps):
    final_pos = current_pos
    for i in range(steps):
        final_pos += 1
        if final_pos > 10:
            final_pos = 1

    return final_pos


def throw_die(current_die_val, current_pos):
    final_pos = current_pos
    die_val = current_die_val
    for i in range(3):
        final_pos = count_steps(final_pos, die_val)
        die_val += 1
        if die_val > 100:
            die_val = 1

    return final_pos, die_val


if __name__ == '__main__':
    p1_score = 0
    p2_score = 0
    p1_pos = 4
    p2_pos = 8
    die_val = 1
    die_rolls = 0
    game_over = False
    while not game_over:
        p1_pos, die_val = throw_die(die_val, p1_pos)
        die_rolls += 3
        p1_score += p1_pos
        if p1_score >= 1000:
            print('P1 WINS')
            print(p2_score)
            print(die_rolls)
            final_score = p2_score * die_rolls
            print(final_score)
            game_over = True
        p2_pos, die_val = throw_die(die_val, p2_pos)
        die_rolls += 3
        p2_score += p2_pos
        if p2_score >= 1000:
            print('P2 WINS')
            print(p1_score)
            print(die_rolls)
            final_score = p1_score * die_rolls
            print(final_score)
            game_over = True
