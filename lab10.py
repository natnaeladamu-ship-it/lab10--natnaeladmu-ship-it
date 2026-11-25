# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # Restate: scan left to right; numbers are saved, operators combine
    # the two most recent numbers into one.
    # Example: ["4","13","5","/","+"] -> push 4,13,5; "/" -> 2; "+" -> 6
    # Approach: stack. On operator, pop b then a, push a op b.
    #   ...

    stack = []
    for t in tokens:
        if t in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncates toward zero
        else:
            stack.append(int(t))
    return stack[0]

    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    pass


def decode_string(s):
    # Outline:
    # Restate: expand k[encoded] by repeating encoded k times; can nest.
    # Example: "3[a2[c]]" -> "acc" -> "accaccacc"
    # Approach: stack of (previous_text, k). On "[" push and reset;
    # on "]" pop and set cur = previous_text + cur * k.
    #   ...

    stack = []
    cur = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)  # handles multi-digit like "12[a]"
        elif ch == "[":
            stack.append((cur, num))
            cur = ""
            num = 0
        elif ch == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur

    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    pass


def daily_temperatures(temps):
    # Outline:
    # Restate: for each day, days until a warmer temperature, else 0.
    # Example: [30,40,50,60] -> [1,1,1,0]
    # Approach: stack of indexes still waiting. When today is warmer than
    # the top day, pop it and answer = today - popped. Push today.
    #   ...

     answer = [0] * len(temps)
     stack = []
     for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
     return answer

    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
     pass


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    # Restate: count groups of "1" connected up/down/left/right.
    # Example: ["11000","11000","00100","00011"] -> 3
    # Approach: scan cells; on unvisited "1", count += 1 and use a stack
    # to mark every connected "1" as visited.
    #   ...

    if not grid:
        return 0 
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                visited.add((r, c))
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < rows and 0 <= nc < cols
                                and grid[nr][nc] == "1"
                                and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            stack.append((nr, nc))
    return count

    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
