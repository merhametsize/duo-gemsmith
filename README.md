# **💎DUO-GEMSMITH -- DUOLINGO GEM HACK⛏️**
The energy mechanic won't be a pain anymore should you wanna do more than 2 lessons a day.

## **💻Usage**

The script needs your JWT (Json Web Token) to function. You can capture your JWT by signing in to Duolingo, opening web developer tools (F12), and executing this command in the console:

```javascript
document.cookie.split('; ').find(row => row.startsWith('jwt_token=')).split('=')[1]
```
If your browser doesn't allow you to paste a command, first execute:

```javascript
allow pasting
```
The console will print a token like (mock token):
```eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjY1NTAyMTA4MCwiaWF0IjoxNzYyMTk4MDczLCJleHAiOjE3NjIyMDE2NzN9.e7w0xT1u-hK_5M2c4R9j0sT6pQ8vB7yD3fA1gF2iL5kM```

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

