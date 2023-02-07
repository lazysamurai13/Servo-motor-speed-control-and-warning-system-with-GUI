import pytest
from project import motion,delay_select, safety
def main():
    test_motion()
    test_delay_select()
    test_safety()
def test_delay_select():
    assert delay_select(2) == 0.09
    assert delay_select(3) == 0.06
    with pytest.raises(ValueError):
        delay_select(6)
def test_safety():
    assert safety(0.12) == True
    assert safety(0.01) == False
def test_motion():
    with pytest.raises(ValueError):
        motion(0.01,180)

if __name__ == "__main__":
    main()