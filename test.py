import test_imports;
import q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11

def test_test():
    assert test_imports.hello_world('Jake') == "Hello Jake"
    assert test_imports.hello_world('Ryan') == "Hello Ryan"

def test_q1():
    assert q1.main("computers", "commuters") == "There are 3 differences"    
    assert q1.main("research", "searches") == "There are 7 differences"

def test_q2():
    assert q2.main("MCMXCVII") == "Answer is 1998"
    assert q2.main("CDLIX") == "Answer is 459"

def test_q3():
    assert q3.main(18, 12) == "The reduced fraction is: 3/2"
    assert q3.main(18, 16) == "The reduced fraction is: 9/8"

def test_q4():
    assert q4.main("paris") == "Output: arispay"
    assert q4.main("amazon") == "Output: amazonay"
    assert q4.main("nth") == "Output: nthay"

def test_q5():
    """ REQUIRES MANUAL GRADING """
    assert 1 == 1

def test_q6():
    assert q6.main("13:59", "14:02", 100, 150) == "No delay necessary"

def test_q7():
    assert q7.main("[][[]]") == "Balanced."
    assert q7.main("[]][[]") == "Not balanced."
    assert q7.main("Jacob Daniel Paul Eugene Folkes Gadaleta") == "Invalid Character."

def test_q8():
    assert q8.main(1, 1, 2, 2, 3, 3, 4, 4) == "Output: The points are collinear"
    assert q8.main(1, 4, 4, 4, 4, 1, 2100, -3) == "Output: The points are not collinear"

def test_q9():
    assert q9.main("algorithm", "logarithm") == "The strings are anagrams."
    assert q9.main("research", "searches") == "The strings are not anagrams."
    
def test_q10():
    assert q10.main("AAANNN", "SAM123", 1) == "SAM124"
    assert q10.main("AAAAAA", "ABCDEF", 2) == "ABCDEH"
    assert q10.main("AAANAA", "AA99ZZ", 3) == "Invalid plate number"

def test_q11():
    assert q11.main("ababa", "ba") == 4
    assert q11.main("ccc", "cc") == 4