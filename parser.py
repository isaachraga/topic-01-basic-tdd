#parser
"""parse numerical strings"""

#broke here somewhere
def parse(s):
    "returns the number represented by the string, or none if no number is represented."
    n = 0
    d = 0
    decimal = False
    for c in s:
        if c == ".":
            assert not decimal
            decimal = True
        if not decimal:
            n = n * 10 + ord(c) - ord("0")
        else
            n = n + (ord(c) - ord("0") ) * d
            d = d /10
    return n
    
    

def test_single_digits():
    print("test single digits")
    assert parse("0") == 0
    assert parse("9") == 9
    

def test_multiple_digits():
    print("test multiple digits")
    assert parse("12") == 12
    assert parse("123") == 123
    assert parse("1234") == 1234
    assert parse("99999") == 99999

def test_decimal_numbers():
    print("test decimal numbers")
    assert parse("12.0") == 12.0
    assert parse("12.3") == 12.3
    assert parse("12.34") == 12.34
    assert parse("0.9999") == 0.99999

if __name__ == "__main__": 
    test_single_digits()
    test_multiple_digits()
    test_decimal_numbers()
    print("done.")