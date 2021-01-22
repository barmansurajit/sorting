from typing import List


def dnf(balls: List[str]):
    curr_ind = r_ind = 0
    b_ind = len(balls) - 1

    while curr_ind <= b_ind:
        if balls[curr_ind] == 'G':
            curr_ind += 1
        elif balls[curr_ind] == 'B':
            balls[curr_ind], balls[b_ind] = balls[b_ind], balls[curr_ind]
            b_ind -= 1
        elif balls[curr_ind] == 'R':
            balls[curr_ind], balls[r_ind] = balls[r_ind], balls[curr_ind]
            r_ind += 1
            curr_ind += 1


if __name__ == "__main__":
    array = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']
    dnf(array)
    print(f"{array}")
