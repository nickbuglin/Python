import multiprocessing
import os, time, random
import pandas as pd


def work():
    pid = multiprocessing.current_process().pid
    print (pid)

if __name__ == '__main__':
    p = multiprocessing
    print(p.cpu_count())

    tes = pd.read_excel('stockXls\\twse.xlsx', 'BWIBBU', index_col=None, parse_cols=0, na_values=['NA'])
    print (tes.count())

    for j in tes.index:
        lis = multiprocessing.Process(target=work)
        lis.start()
        lis.join()
