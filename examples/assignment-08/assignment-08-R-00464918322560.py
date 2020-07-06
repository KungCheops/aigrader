from GDPvsLE import *
import matplotlib.pyplot as plt


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    """
    Compute summary statistics for a list with only real numbers, i.e. 
    return
    - sum of all values
    - minimum value
    - maximum value
    - averege of all values
    """
    sum_values = 0
    min_value = l[0]
    max_value = l[0]
    for i, val in enumerate(l):
        if type(val) not in [float, int]:
            print(
                f'The value {val} in the list is not an integer or float. Exiting!'
                )
            exit(0)
        sum_values += val
        avg_value = sum_values / (i + 1)
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    """
    Creates a histogram list with "bin_amount" ranges from a list of real 
    numbers, i.e.the histogram list is a list with the number of occasions
    of a number (in list l) in a certain range. The range being:
    (max_value(l)-min_value(l))/bin_amount
    In case of a number in l being at the boundary between two ranges, 
    the number is placed into the closest lower range bin. 
    """
    sum_values, min_value, max_value, avg_value = stats(l)
    bin_amount = 10
    bins = [[] for x in range(bin_amount)]
    for val in l:
        if type(val) not in [float, int]:
            print(f'The value {val} in this list is not of float- or int-type.'
                )
            print('Exiting!')
            exit(0)
        if min_value <= val <= min_value + (max_value - min_value
            ) * 1 / bin_amount:
            bins[0].append(val)
        else:
            i = 1
            while i <= bin_amount - 1:
                if min_value + (max_value - min_value
                    ) * i / bin_amount < val <= min_value + (max_value -
                    min_value) * (i + 1) / bin_amount:
                    bins[i].append(val)
                i += 1
    bin_count = [len(x) for x in bins]
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert sum(histogram([0, 0.1, 0.3, 1.5, 10])) == len([0, 0.1, 0.3, 1.5, 10]
        )
    gdp_sum, gdp_min, gdp_max, gdp_avg_value = stats(gdp)
    print(50 * '-')
    print('Summary statistics:')
    print(f'Tot sum: {gdp_sum:.2f}')
    print(f'Min value: {gdp_min:.2f}')
    print(f'Max value: {gdp_max:.2f}')
    print(f'Avg value: {gdp_avg_value:.2f}')
    print(50 * '-')
    buckets = histogram(gdp)
    for bucket in buckets:
        print(bucket * '*' + str(bucket))
    plt.hist(gdp)
    plt.show()
