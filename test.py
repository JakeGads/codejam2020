from os.path import getmtime as gen_time
from time import ctime
import test_imports
import q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11

def run(ins, outs, num, fun):
    time_stamp = 0
    try:
        time_stamp = ctime(gen_time("q" + str(num) + ".py"))
    except:
        time_stamp = "unavailable"

    correct = 0
    for i in range(len(ins)):
        try:
            if isinstance(ins[i], list) or isinstance(ins[i], tuple):
                if fun(*ins[i]) == outs[i]:
                    correct += 1
            else:
                if fun(ins[i]) == outs[i]:
                    correct += 1
        except BaseException as e:
            correct = e
    with open("report.md", "a+") as f:
        f.write("""
# {}

<br>

## {} of {} correct

<br>

### Time: {}

<br><br>        

""".format(num, correct, len(ins), {time_stamp}))


def test_test():
    ins = ['Jake', 'Mick', 'Ryan']
    outs = ['Hello Jake', 'Hello Mick', 'Hello Ryan']

    run(ins, outs, 0, test_imports.hello_world)
   
def test_q1():
    ins = ("computers", "commuters"), ("research", "searches")
    outs = "There are 3 differences", "There are 7 differences"    
    
    run(ins, outs, 1, q1.main)

def test_q2():
    run(
        ("CDLIX","MCMXCVII"), 
        ("Answer is 1998", "Answer is 459"),
        2,
        q2.main
    )

def test_q3():
    run(
        ((18, 12), (18, 16)),
        ("The reduced fraction is: 3/2","The reduced fraction is: 9/8"),
        3,
        q3.main
    )


def test_q4():
    run(
        ("paris", "amazon", "nth"),
        ("Output: arispay", "Output: amazonay", "Output: nthay"),
        4,
        q4.main
    )
    
def test_q6():
    run(
        (("13:59", "14:02", 100, 150), ),
        ("No delay necessary"),
        6,
        q6.main
    )

def test_q7():
    run(
        ("[][[]]", "[]][[]", "Jacob Daniel Paul Eugene Folkes Gadaleta"),
        ("Balanced.", "Not balanced.", "Invalid Character."),
        7,
        q7.main
    ) 

def test_q8():
    # print(*(1, 1, 2, 2, 3, 3, 4, 4))
    # input()
    run(
        ((1, 1, 2, 2, 3, 3, 4, 4), (1, 4, 4, 4, 4, 1, 2100, -3)),
        ("Output: The points are collinear", "Output: The points are not collinear"),
        8,
        q8.main
    )
    
def test_q9():
    run(
        (("algorithm", "logarithm"), ("research", "searches")),
        ("The strings are anagrams.", "The strings are not anagrams."),
        9,
        q9.main
    )
    
    
def test_q10():
    run(
        (("AAANNN", "SAM123", 1), ("AAAAAA", "ABCDEF", 2), ("AAANAA", "AA99ZZ", 3)),
        ( "SAM124", "ABCDEH", "Invalid plate number"), 
        10,
        q10.main
    )
    
def test_q11():
    run(
        (("ababa", "ba"), ("ccc", "cc")),
        (4,4),
        11,
        q11.main
    )

with open("report.md", "w+") as f:
    f.write("# " + ctime(gen_time("test.py")))

for i in (test_test, test_q1, test_q2, test_q3, test_q4, test_q6, test_q7, test_q8, test_q9, test_q10, test_q11):
    i()