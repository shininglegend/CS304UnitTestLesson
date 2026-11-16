# swap/chunks.py
from itertools import batched
 
 
def pairs(names):
    """Split a class list into lab pairs; an odd student out works alone."""
    return [list(group) for group in batched(names, 2)]
# swap/test_chunks.py
from chunks import pairs
 
 
def test_pairs_with_odd_student_out():
    assert pairs(["Ada", "Alan", "Grace"]) == [["Ada", "Alan"], ["Grace"]]
