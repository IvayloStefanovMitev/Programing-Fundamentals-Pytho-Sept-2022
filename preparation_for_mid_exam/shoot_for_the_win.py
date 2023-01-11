def shoot(targets):
    shot_count = 0
    while True:
        command = input()
        if command == 'End':
            break
        index = int(command)
        if 0 <= index < len(targets) and targets[index] != -1:
            shot_count += 1
            save_index = targets[index]
            targets[index] = -1
            for target in range(len(targets)):
                if targets[target] == -1:
                    continue
                if save_index >= targets[target]:
                    targets[target] += save_index
                else:
                    targets[target] -= save_index
    result = f"Shot targets: {shot_count} -> {' '.join(str(num) for num in targets)}"
    return result


targets_value = list(map(int, input().split()))
print(shoot(targets_value))