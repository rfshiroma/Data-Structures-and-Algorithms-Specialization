# python3

'''Approach: Queue'''
  # Firstly, map openning parentheses to respective closing parentheses. Then, iterate through the given expression using 'i'. If 'i' is an open parentheses, append it in queue; if 'i' is close parentheses, check whether queue is empty or 'i' is the top element of queue, if yes, return "Unbalanced", otherwise "Balanced".
  # FIFO principle: First-In First-out


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def check(text):
    # Very important that parentheses need to be declared in correct order
    open_char = tuple("([{")
    close_char = tuple(")]}")
    map = dict(zip(open_char, close_char))
    queue = []

    for i in text:
        if i in open_char:
            queue.append(map[i])
        elif i in close_char:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"



if __name__ == "__main__":
    string_1 = "{[]{()}}"
    print(string_1, "-", check(string_1))

    string_2 = "[{}{})(]"
    print(string_2, "-", check(string_2))

    string_3 = "((()"
    print(string_3, "-",check(string_3))
