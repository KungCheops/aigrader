import logging
def sublist(s_list):
    for i in range(len(s_list)):
        logging.debug(f"i:{i}")
        yield [s_list[i]]
        for j in range(i+1, len(s_list)):
            logging.debug(f"{j}")
            if s_list[j] >= s_list[j-1]:
                sub = s_list[i:j+1]
                logging.debug(f"{sub}")
                yield sub
def longest_common_list(s_list):
    subs = sublist(s_list)
    sublists = [i for i in subs]
    logging.info(f'ascending sublists of input: {sublists}')
    rev = s_list
    rev.reverse()
    rev_subs = sublist(rev)
    rev_sublists = [i for i in rev_subs]
    logging.info(f'ascending sublists of reversed input: {rev_sublists}')
    longest_list = []
    for i in sublists:
        for j in rev_sublists:
            logging.debug(i,',',j)
            if ( (i==j) and (len(i) > len(longest_list)) ):
                longest_list = i
            logging.debug(longest_list)
    logging.info(f'longest common sublist: {longest_list}')
    return longest_list
if __name__ == "__main__":
    log = logging.getLogger()
    log.setLevel(logging.WARN)
    assert longest_common_list([1,1,2,3,0,0,3,4,5,7,1,3,2,1,1,2]) == [1,1, 2, 3]
    assert longest_common_list([0,1,2,3,2,1,0]) == [0,1,2,3]
    assert longest_common_list([0,1,2,1,0]) == [0,1,2]
    assert longest_common_list([1,1,1]) == [1,1,1]
    assert longest_common_list([0,1,2,3]) == [0]