import pytest
from datetime import datetime
from weighted_means_algorithm import group_adjust

#UNIT TESTS

def test_three_groups():
    values = [4, 7, 13, 15, 20]
    group1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    group2 = ['CA', 'CA', 'MA', 'NY', 'NY']
    group3 = ['LOS ANGELES', 'LOS ANGELES', 'BOSTON', 'NEW YORK', 'BUFFALO']
    weights = [.2, .3, .5]

    print "Testing Three Groups:"
    group_adjust(values, [group1, group2, group3], weights)

def test_two_groups():
    values = [1, 2, 3, 8, 5]
    group1 = ['CAN', 'USA', 'CAN', 'USA', 'USA']
    group2 = ['ON', 'FL', 'QC', 'CT', 'CT']
    weights = [.6, .4]

    print "Testing Two Groups:"
    group_adjust(values, [group1, group2], weights)

def test_missing_vals():
    values = [1, None, 3, 5, 8, 7]
    group1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    group2 = ['MA', 'MA', 'CO', 'AL', 'CT', 'CT']
    weights = [.55, .45]

    print "Testing Missing Values:"
    group_adjust(values, [group1, group2], weights)

def test_weights_len_equals_group_len():
    values = [1, None, 3, 5, 8, 7]
    group1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    group2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65]

    # Handles the exception so the program continues to run
    # You can use this code in the other testing functions as well.
    # Example: If you want to make test_three_groups() fail and keep
    # the program running, then use this code.
    try:
        with pytest.raises(ValueError):
            print "Testing To Make Sure Weight Length == Group Length:"
            group_adjust(values, [group1, group2], weights)
    except Exception as e:
        print "test_weights_len_equals_group_len() threw an error: ", e
        print "Make sure the length of groups is equivalent to the length of weights\n"

def test_group_len_equals_vals_len():
    # The groups need to be same shape as vals
    values = [1, None, 3, 5, 8, 7]
    group1 = ['USA']
    group2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    weights = [.65]

    # Handles the exception so the program continues to run
    try:
        with pytest.raises(ValueError):
            print "Testing To Make Sure Group Length == Vals Length:"
            group_adjust(values, [group1, group2], weights)
    except Exception as e:
        print "test_group_length_equals_vals_len() threw an error: ", e
        print "Make sure the length of groups is equivalent to the length of vals\n"

def test_performance():
    values = 100 * [1, None, 3, 5, 8, 7]
    group1 = 100 * [1, 1, 1, 1, 1, 1]
    group2 = 100 * [1, 1, 1, 1, 2, 2]
    group3 = 100 * [1, 2, 2, 3, 4, 5]
    weights = [.20, .30, .50]

    print "Testing Performance:"
    start = datetime.now()
    group_adjust(values, [group1, group2, group3], weights)
    end = datetime.now()
    diff = end - start
    print 'Total performance test time: {}'.format(diff.total_seconds())

test_three_groups()
test_two_groups()
test_missing_vals()
test_weights_len_equals_group_len()
test_group_len_equals_vals_len()
test_performance()