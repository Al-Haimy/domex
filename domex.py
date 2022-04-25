#!/usr/bin/python3
import sys
import re


def parse_args():
    import argparse
    parser = argparser.ArgumentParser()
    parser.add_argument('-f', '--file', type=str,
                        required=True, help='Target file')
    parser.add_argument('-r', '--remove', type=str, required=False,
                        help='exclude a word you want to delete')
    parser.add_arhument('')


def remove_double():
    double = []
    cleanlist = []
    with open(sys.argv[1], 'r',  encoding='utf-8') as file_domains:
        domains = file_domains.readlines()
        print('Total domains: ' + str(len(domains)))
        for domain in domains:
            if domain not in double:
                double.append(domain)


def banner():
    print(r"""________                                
\______ \   ____   _____   ____ ___  ___
 |    |  \ /  _ \ /     \_/ __ \\  \/  /
 |    `   (  <_> )  Y Y  \  ___/ >    < 
/_______  /\____/|__|_|  /\___  >__/\_ \
        \/             \/     \/      \/""")
    print("Good Luck")
    print("Happy Hacking")
