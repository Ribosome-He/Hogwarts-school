import pytest
import random

def add(x,y):
    return x+y

# def test_add():
#     assert add(1,1)==2


@pytest.mark.parametrize(
    "x,y",
    [
        (1,1),
        (2,2),
        (3,6),
    ]
)
def test_paraadd(x,y):
    assert add(x,y)==x+y+1



def a(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return random.choice([nums,None,10])

nums = [5,2,45,6,8,2,1]
