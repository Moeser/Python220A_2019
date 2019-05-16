"""
check good works the same, and is faster
"""

import src.poor_perf as p
import src.good_perf as g


def test_assess_preformance():
    """ compare """
    poor = p.analyze('data/exercise.csv')
    good = g.analyze('data/exercise.csv')
    poor_elapsed = poor[1] - poor[0]
    good_elapsed = good[1] - good[0]
    assert good_elapsed < poor_elapsed
    assert poor[2] == good[2]
    assert poor[3] == good[3]
