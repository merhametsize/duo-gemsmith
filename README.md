# **💎DUO-GEMSMITH -- DUOLINGO GEM HACK⛏️**
The energy mechanic won't be a pain anymore should you wanna do more than 2 lessons a day.

```bash
merhametsize@ziopera:~/duo-gemsmith$ echo "eyJhbGciOiJ6aW9wZXJhIiwidHlwIjoib25jbGVwb2lyZSJ9.eyJzdWIiOiIyMS4zNyIsIm5hbWUiOiJKb2huIFBhdWwgSUIiLCJpYXQiOjB9.V4W14t-6tsEr5hwzFYlM0_XTHOyFCloudNM4LRo6TgI" > jwt.txt
merhametsize@ziopera:~/duo-gemsmith$ python3 duo-gemsmith.py
======================================================================
💎 D U O - G E M S M I T H    -    D U O L I N G O   G E M   H A C K ⛏️
  The energy mechanic wont be a pain anymore should you wanna
                have more than 2 lesson a day
======================================================================

[*] Successfuly read jwt.txt
[*] JWT: eyJhbGciOiJ6aW9wZXJhIiwidHlwIjoib25jbGVwb2lyZSJ9.eyJzdWIiOiIyMS4zNyIsIm5hbWUiOiJKb2huIFBhdWwgSUIiLCJpYXQiOjB9.[signature]
[*] Userid: 123456789
[*] URL: https://www.duolingo.com/2017-06-30/users/123456789/rewards/SKILL_COMPLETION_BALANCED-merhametsizeDoesntLikeEnergy-2-GEMS
[*] Time interval: 1-60
[*] User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
[*] Press Ctrl+C to stop the script.

Request #1: [10:31:49] Status: 200 - +30💎
Request #2: [10:32:37] Status: 200 - +60💎
Request #3: [10:32:49] Status: 200 - +90💎
Request #4: [10:32:52] Status: 200 - +120💎
Request #5: [10:33:20] Status: 200 - +150💎
Request #6: [10:34:08] Status: 200 - +180💎
Request #7: [10:34:47] Status: 200 - +210💎
Request #8: [10:35:39] Status: 200 - +240💎
Request #9: [10:36:05] Status: 200 - +270💎
Request #10: [10:36:09] Status: 200 - +300💎
```

## **💻Usage**

The script needs your JWT (Json Web Token) to function. You can capture your JWT by signing in to Duolingo, opening web developer tools (F12), and executing this command in the console:

```javascript
document.cookie.split('; ').find(row => row.startsWith('jwt_token=')).split('=')[1]
```
If your browser doesn't allow you to paste a command, first execute:

```javascript
allow pasting
```
The console will print a token like:
```eyJhbGciOiJ6aW9wZXJhIiwidHlwIjoib25jbGVwb2lyZSJ9.eyJzdWIiOiIyMS4zNyIsIm5hbWUiOiJKb2huIFBhdWwgSUIiLCJpYXQiOjB9.V4W14t-6tsEr5hwzFYlM0_XTHOyFCloudNM4LRo6TgI```

Clone the repo, install dependencies, copy and paste the token inside jwt.txt:

```bash
git clone https://github.com/merhametsize/duo-gemsmith.git
cd duo-gemsmith
pip install requests
echo 'eyJhbGci...L5kM' > jwt.txt
```

By executing the script, a PATCH request will be sent (on average) every 30 seconds, each of them increasing gems by 30.
```bash
python3 duo-gemsmith.py
```

## **📜 License**

This project is licensed under the **MIT License**. See the LICENSE file for details.

## **⚠️ DISCLAIMER ⚠️**

This tool is intended for educational purposes only, such as learning about API security, HTTP requests, and Python scripting. Unauthorized access, use, or modification of any third-party service (including Duolingo) is strictly prohibited and may violate their Terms of Service and applicable law. The user assumes all risk and responsibility for running this script.

