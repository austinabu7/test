from app import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 1) == 4
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 5) == 0

print("Running tests...")
test_add()
print("✅ add tests passed!")
test_subtract()
print("✅ subtract tests passed!")
test_multiply()
print("✅ multiply tests passed!")
print("🎉 All tests passed!")