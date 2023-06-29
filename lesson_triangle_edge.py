def calculate_third_edge(first_edge, second_edge, include_long_edge=False):
    # 我們只能算直角三角形
    possible_answer = list()
    ## 不含長邊
    if include_long_edge == False:  # if !include_long_edge
        # get long edge
        answer = (first_edge * first_edge + second_edge * second_edge) ** 0.5
        possible_answer.append(answer)
    ## 有含長邊
    elif first_edge != second_edge:
        # get another short edge
        longer_one = max(first_edge, second_edge) 
        shorter_one = min(first_edge, second_edge)
        answer_2 = (longer_one * longer_one - shorter_one * shorter_one) ** 0.5
        possible_answer.append(answer_2)
    return possible_answer

if __name__ == '__main__':
    print(calculate_third_edge(3, 4))
    print(calculate_third_edge(5, 12))
    print(calculate_third_edge(13, 12, True))