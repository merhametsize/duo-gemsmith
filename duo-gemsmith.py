'''
💎 duo-gemsmith - A Duolingo Gem Hack 💎
-----------------------------------------------------------------------------------
Description: A utility script designed to repeatedly claim a specific Duolingo
             in-app reward (Gems) via an API PATCH request. It uses JWT decoding,
             randomized User-Agents.
Author: Gabriele Cassetta (@merhametsize)
Date: 2025-11-01

DISCLAIMER: This tool is intended for educational purposes only, such as learning
            about API security, HTTP requests, and Python scripting.
            Unauthorized access, use, or modification of any third-party service
            (including Duolingo) is strictly prohibited and may violate their
            Terms of Service and applicable law. The user assumes all risk and
            responsibility for running this script.
-----------------------------------------------------------------------------------
'''

import requests
import getpass
import random
import base64
import time
import json
import sys
import os

MIN_INTERVAL = 1
MAX_INTERVAL = 60

#We claim the reward from the EN->FR course
PAYLOAD = {
    'consumed':True,
    'fromLanguage':'en',
    'learningLanguage':'fr',
}

#We randomize the user-agent field of the PATCH request when the script is launched, this makes for more stealth
USER_AGENTS = [
    # Chrome (Desktop)
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    # Linux Desktop
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:118.0) Gecko/20100101 Firefox/118.0', # Firefox on Ubuntu
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36', # Chrome on generic Linux (often Arch/Debian/Fedora)
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 (ArchLinux)', # Specific Chrome on Arch (for diversity)
    # Firefox (Desktop)
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:118.0) Gecko/20100101 Firefox/118.0',
    # Edge (Desktop)
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Edge/128.0',
    # Safari (Desktop)
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    # Mobile (iOS/Safari)
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1.15',
    # Mobile (Android/Chrome)
    'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
]

HEADERS = {
    'Host': 'www.duolingo.com',
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'application/json; charset=UTF-8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json; charset=UTF-8',
    'Referer': 'https://www.duolingo.com/learn',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.duolingo.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Sec-GPC': '1',
    'Priority': 'u=0',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer TOKEN_PLACEHOLDER',
    'Connection': 'keep-alive',
    'TE': 'trailers'
}

def send_patch_request(url, headers, data):
    try:
        response = requests.patch(url, headers=headers, json=data, timeout=10)

        print(f'[{time.strftime("%H:%M:%S")}] Status: {response.status_code}', end='')

        # Check for non-successful status codes
        response.raise_for_status()

    except requests.exceptions.RequestException as err:
        # Catch all errors (HTTP errors, connection, timeout, etc.)
        print(f'[{time.strftime("%H:%M:%S")}] ERROR: {err}', file=sys.stderr)

def read_jwt(filepath: str) -> str:
    if not os.path.exists(filepath):
        print(f'Error: Token file {filepath} not found.', file=sys.stderr)
        sys.exit(1)

    try:
        with open(filepath, 'r') as f:
            token = f.read().strip()

            # Check if it's a full JWT token (contains dots)
            if '.' in token:
                # JWT format: HEADER.PAYLOAD.SIGNATURE. We need the second part (index 1).
                parts = token.split('.')
                if len(parts) == 3:
                    # Return the base64-encoded userid
                    return token, parts[1]
                else:
                    print('Error: File contains a malformed JWT. Expected 3 parts.', file=sys.stderr)
                sys.exit(1)

    except IOError as e:
        print(f'Error reading token file: {e}', file=sys.stderr)
        sys.exit(1)

def decode_token(base64_userid: str) -> str:
    try:
        padded = base64_userid + '=' * (-len(base64_userid) % 4)
        userid = json.loads(base64.urlsafe_b64decode(padded))['sub']
    except Exception as e:
        print(f'Error decoding token: {str(e)}[/]', file=sys.stderr)
        sys.exit(1)
    return userid

if __name__ == '__main__':
    username = getpass.getuser() #The user running this script, for easter egg purposes

    #You can write literally anything in between the dashes...
    reward = f'SKILL_COMPLETION_BALANCED-{username}DoesntLikeEnergy-2-GEMS'

    try:
        print('=' * 70)
        print('💎 D U O - G E M S M I T H    -    D U O L I N G O   G E M   H A C K ⛏️')
        print('  The energy mechanic won\'t be a pain anymore should you wanna\n\t\tdo more than 2 lesson a day')
        print('=' * 70, end='\n\n')

        token, base64_userid = read_jwt('./jwt.txt')
        userid = decode_token(base64_userid)

        api_url = f'https://www.duolingo.com/2017-06-30/users/{userid}/rewards/{reward}'
        HEADERS['Authorization'] = HEADERS['Authorization'].replace('TOKEN_PLACEHOLDER', token)

        print('[*] Successfuly read jtw.txt')
        print(f'[*] JWT: {token.split(".")[0] + "." + token.split(".")[1] + ".[signature]"}')
        print(f'[*] Userid: {userid}')
        print(f'[*] URL: {api_url}')
        print(f'[*] Time interval: {MIN_INTERVAL}-{MAX_INTERVAL}')
        print(f'[*] User-Agent: {HEADERS["User-Agent"]}')
        print('[*] Press Ctrl+C to stop the script.', end='\n\n')
        #print('-' * 70, end ='\n\n')

        request_count = 0
        gems = 0

        while True:
            request_count += 1
            print(f'Request #{request_count}: ', end='', flush=True)

            send_patch_request(api_url, HEADERS, PAYLOAD)
            gems += 30
            print(f' - +{gems}💎')

            current_interval = random.uniform(MIN_INTERVAL, MAX_INTERVAL)
            time.sleep(current_interval)

    except KeyboardInterrupt:
        print('\nScript terminated by user.')
