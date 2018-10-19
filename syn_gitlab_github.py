#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    File Name: syn_gitlab_github.py
    Author: Carson Wang
    mail: r03944040@g.ntu.edu.tw
    Created Time: 2018-10-18 13:46:58
'''

import os
import fileinput
import subprocess
from argparse import ArgumentParser

def checkArgs():
    parser = ArgumentParser(usage='python ' + os.path.basename(__file__) + '\n'
                                  '-github: Github account'
                                  '-gitlab: Gitlab account\n',
                            description='Sync gitlab projects to github projects.')
    parser.add_argument('-github', '-gh', type=str, help='what your github account to be named', required=True)
    parser.add_argument('-gitlab', '-gl', type=str, help='what your gitlab account to be named', required=True)
    parser.add_argument('-url', '-u', type=str, help='where url to be replaced gitlab server.', required=True)
    args = parser.parse_args()
    return args


def replacement(file_name, text_to_search, replacement_text):
    with fileinput.FileInput(file_name, inplace=True) as _file:
        for line in _file:
            print(line.replace(text_to_search, replacement_text), end='')


def runCommand(commands):
    try:
        output = subprocess.check_output(commands)
    except subprocess.CalledProcessError:
        print('Exception handled')
    return output


if __name__ == '__main__':
    args = checkArgs()
    github_account, gitlab_account, gitlab_url = (
            args.github, args.gitlab, args.url)
    git_file = '.git/config'
    github = 'git@github.com:{0}/'.format(github_account)
    gitlab = '{0}/{1}/'.format(gitlab_url, gitlab_account)
    print(github, gitlab)

    all_dirs = next(os.walk('.'))[1]
    for _dir in all_dirs:
        os.chdir(_dir)
        print('Sync', _dir, 'project')
        print(runCommand(['git', 'pull', '--rebase']))
        replacement(git_file, gitlab, github)
        print(runCommand(['git', 'push', '--force']))
        replacement(git_file, github, gitlab)
        print(runCommand(['git', 'fetch', '-p']))
        os.chdir('..')
        print('---------------------------------------')
