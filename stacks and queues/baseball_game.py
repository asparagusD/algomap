def cal_points(operations):
    result = []

    for operation in operations:
        if operation == "C":
            result.pop()
        elif operation == "D":
            result.append(result[-1] * 2)
        elif operation == "+":
            result.append(result[-1] + result[-2])    
        else:
            result.append(int(operation))

    sum = 0
    for score in result:
        sum += score

    return sum                    


print(cal_points(["1","C"]))