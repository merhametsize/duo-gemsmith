# **💎DUO-GEMSMITH -- DUOLINGO GEM HACK⛏️**
The energy mechanic won't be a pain anymore should you wanna do more than 2 lesson a day.

## **💻Usage**

The script needs your JWT (Json Web Token) to function. You can capture your JWT by signing in to Duolingo, opening web devloper tools (F12), and executing this command in the console:

```javascript
document.cookie.split('; ').find(row => row.startsWith('jwt_token=')).split('=')[1]
```
If your browser doesn't allow you to paste a command, first execute:

```javascript
allow pasting
```

Paste your token inside jwt.txt and execute the script.

## **🛠️ Setup and Installation**

Clone the repository  

```bash
git clone https://github.com/merhametsize/duo-gemsmith.git
cd duo-gemsmith
```

Install dependencies  

```bash
pip install requests
```

## **📜 License**

This project is licensed under the **MIT License**. See the LICENSE file for details.

## **⚠️ DISCLAIMER ⚠️**

This tool is intended for educational purposes only, such as learning about API security, HTTP requests, and Python scripting. Unauthorized access, use, or modification of any third-party service (including Duolingo) is strictly prohibited and may violate their Terms of Service and applicable law. The user assumes all risk and responsibility for running this script.

