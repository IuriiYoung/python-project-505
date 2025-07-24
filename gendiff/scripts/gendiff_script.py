#!/usr/bin/env python3

import json

from gendiff import gendiff
from gendiff import gendiff_pars

def start_gendiff():
    args = gendiff_pars.get_args()
    file_1 = json.load(open(args.first_file))
    file_2 = json.load(open(args.second_file))
    result = gendiff.gendiff(file_1, file_2)
    print(result)
    


def main():
    start_gendiff()


if __name__ == '__main__':
    main()