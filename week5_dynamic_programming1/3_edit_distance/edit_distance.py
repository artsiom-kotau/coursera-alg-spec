# Uses python3
def edit_distance(s, t):
    distances = []
    for i in range(0, len(s)+1):
        distances.append((len(t) + 1) * [0])

    for i in range(0, len(s)+1):
        distances[i][0] = i

    for i in range(0, len(t)+1):
        distances[0][i] = i

    for s_i in range(1, len(s)+1):
        for t_i in range(1, len(t)+1):
            if s[s_i-1] != t[t_i-1]:
                distances[s_i][t_i] = min(distances[s_i][t_i - 1] + 1,
                                          distances[s_i-1][t_i] + 1,
                                          distances[s_i-1][t_i-1] + 1)
            else:
                distances[s_i][t_i] = min(distances[s_i][t_i - 1] + 1,
                                          distances[s_i-1][t_i] + 1,
                                          distances[s_i-1][t_i-1])

    return distances[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
