test_cases = int(input())
while test_cases > 0:
    total_robots = int(input())
    robot_list = list(map(int, input().split()))
    robot_list.sort(reverse=True)

    if total_robots == 1 and robot_list[0] != 0:
        print("no")
        test_cases -= 1
        continue

    x = 0
    for i in range(total_robots-1):
        x = robot_list[i]
        if x == -1:
            continue
        for j in range(i+1, total_robots):
            if robot_list[j] == x-1:
                robot_list[j] = -1
                x -= 1
            if x == 0:
                break

        if x != 0:
            print("no")
            test_cases -= 1
            break
    else:
        print("yes")
        test_cases -= 1
