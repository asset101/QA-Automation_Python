# Task 2 for [((())()(())]] sequence

def is_valid_sequence(sequence: str) -> bool:
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in sequence:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if not stack or matching_bracket[char] != stack.pop():
                return False
    return not stack

def generate_valid_sequences(sequence: str):
    def backtrack(s, start, lcount, rcount, lremove, rremove):
        if lremove == 0 and rremove == 0:
            if is_valid_sequence(s):
                valid_sequences.add(s)
            return
        
        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]:
                continue
            if s[i] in '([' and lremove > 0:
                backtrack(s[:i] + s[i+1:], i, lcount-1, rcount, lremove-1, rremove)
            elif s[i] in ')]' and rremove > 0:
                backtrack(s[:i] + s[i+1:], i, lcount, rcount-1, lremove, rremove-1)

    lremove = rremove = 0
    balance_round = balance_square = 0
    for char in sequence:
        if char == '(':
            balance_round += 1
        elif char == ')':
            if balance_round > 0:
                balance_round -= 1
            else:
                rremove += 1
        elif char == '[':
            balance_square += 1
        elif char == ']':
            if balance_square > 0:
                balance_square -= 1
            else:
                rremove += 1

    lremove = balance_round + balance_square
    valid_sequences = set()
    backtrack(sequence, 0, balance_round, balance_square, lremove, rremove)
    
    return valid_sequences

sequence = "[((())()(())]]"

if is_valid_sequence(sequence):
    print("Последовательность правильная")
else:
    print("Последовательность неправильная")
    valid_sequences = generate_valid_sequences(sequence)
    if valid_sequences:
        print("Все возможные правильные последовательности:")
        for seq in sorted(valid_sequences):
            print(seq)
    else:
        print("Не удалось найти правильные последовательности")
