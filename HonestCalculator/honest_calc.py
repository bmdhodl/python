# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

end2 = False
memory = 0
msg_index = 10
answer = ""
countM = 0


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
        return output
    else:
        output = False
        return output


def check(v1, v2, v3):
    global countM
    msg = ""

    if v1 / v2 == 1:
        if countM == 1:
            pass
        else:
            msg += msg_6
            countM += 1
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
    else:
        return v1, v2, v3


def Results():
    end1 = False
    print(msg_4)
    msg_index = 10

    while not end1:
        global answer
        answer = input()
        try:
            # store results
            if answer == "y":
                if is_one_digit(result):

                    # ask to add the number until y or n
                    if answer == "y":
                        if msg_index < 13:
                            print(msg_[msg_index])
                            msg_index += 1
                        elif answer == "n":
                            end1 = True
                        else:
                            print(msg_5)
                            answer = input()
                            if answer == "y":
                                end1 = True

                else:
                    # store memory
                    global memory
                    memory = result
                    print(msg_5)
                    answer = input()
                    if answer == "y":
                        end1 = True

            elif answer == "n":
                print(msg_5)
                answer = input()

                # decide whether to end or continue
                if answer == "y":
                    break
                else:
                    exit()
            else:
                print(msg_5)
        except ValueError:
            pass


while not end2:
    try:
        print(msg_0)
        calc = input()
        calc = calc.split()
        z = ["+", "-", "*", "/"]

        x = calc[0]
        oper = calc[1]
        y = calc[2]

        # store in memory
        if x == "M":
            x = memory
            pass

        if y == "M":
            y = memory
            pass

        x = float(x)
        y = float(y)

        # verify calculations
        if oper in z:
            if oper == "/":
                check(x, y, oper)
                pass

            if oper == "+":
                result = x + y
                check(x, y, oper)
                print(result)
                Results()
            elif oper == "-":
                result = x - y
                check(x, y, oper)
                print(result)
                Results()
            elif oper == "*":
                result = x * y
                check(x, y, oper)
                print(result)
                Results()
            elif oper == "/" and y != 0:
                result = x / y
                check(x, y, oper)
                print(result)
                Results()
            else:
                print(msg_3)
        else:
            print(msg_2)

    except ValueError:
        print(msg_1)
