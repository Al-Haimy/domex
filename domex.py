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


def write_file(file_name, domains):
    with open(file_name, 'w') as file:
        for domain in domains:
            file.write(domain+"\n")


def remove_double(file_name):
    double = []
    cleanlist = []
    with open(file_name, 'r',  encoding='utf-8') as file_domains:
        domains = file_domains.readlines()
        print('Total domains: ' + str(len(domains)))
        for domain in domains:
            if domain not in double:
                double.append(domain.strip())
    return double


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str,
                        required=True, help='target file')
    parser.add_argument('-e', '--exclude', type=str,
                        required=False, help='a word to remove from the file')
    parser.add_argument('-o', '--output', type=str, required=False,
                        help='if not specified will overrwrite the original')
    return parser.parse_args()


def banner():
    print(r"""________
\______ \   ____   _____   ____ ___  ___
 |    |  \ /  _ \ /     \_/ __ \\  \/  /
 |    `   (  <_> )  Y Y  \  ___/ >    <
/_______  /\____/|__|_|  /\___  >__/\_ \
        \/             \/     \/      \/""")
    print("Good Luck")
    print("Happy Hacking")


def exclude(domains, ex):
    new_domains = [domain.replace(ex, '') for domain in domains]
    return new_domains


def main():
    banner()
    args = parse_args()
    clean_list = remove_double(args.file)
    if args.exclude:
        clean = exclude(clean_list, args.exclude)
        clean_file = args.output if args.output else args.file
        write_file(clean_file, clean)
    else:
        clean_file = args.output if args.output else args.file
        write_file(clean_file, clean_list)


if __name__ == '__main__':
    main()
