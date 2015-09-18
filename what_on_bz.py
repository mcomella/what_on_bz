#!/usr/bin/env python2

from argparse import ArgumentParser
from datetime import datetime, timedelta
import urllib

URL = 'https://bugzilla.mozilla.org/buglist.cgi'

LAST_WEEK_PARAMS = {
    'query_format': 'advanced',
    'chfield': 'bug_status',
    'bug_status': 'RESOLVED',
    'chfieldvalue': 'RESOLVED',
    'chfieldto': 'Now',
    'emailtype1': 'equals',
    'emailassigned_to1': '1',
}

# TODO: Declare NEW or ASSIGNED bug status.
PRESENT_PARAMS = {
    'query_format': 'advanced',
    'emailtype1': 'equals',
    'emailassigned_to1': '1',
}

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('email', help='email address of changes')
    return parser.parse_args()


def get_date_str():
    """Returns YYYY-MM-DD"""
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    return str(seven_days_ago)


def get_url_for_params(static_params, dynamic_params):
    out_params = static_params.copy()
    out_params.update(dynamic_params)
    return URL + '?' + urllib.urlencode(out_params)


args = parse_arguments()
dynamic_params = {
    'email1': args.email,
    'chfieldfrom': get_date_str()
}

print('PAST: ' + get_url_for_params(LAST_WEEK_PARAMS, dynamic_params))
print('')  # newline.
print('PRESENT: ' + get_url_for_params(PRESENT_PARAMS, dynamic_params))
