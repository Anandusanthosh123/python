# 🗨️ Python Chat App

A simple real‑time chat application built with **Python**, **asyncio**, and **websockets**.  
Multiple clients can connect to a server and exchange messages with usernames and timestamps.

---

## 🚀 Features
- Real‑time communication using WebSockets
- Multiple clients supported simultaneously
- Messages tagged with **username + timestamp**
- Modular design (separate server and client scripts)
- Easy to extend with logging, databases, or GUI

---

## 📂 Project Structure
chat-app/
 ├── server.py 
        # WebSocket server
         ├── client.py 
                # WebSocket client
                 ├── requirements.txt # Dependencies 

---

## ⚙️ Setup

1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install websockets
##

3. Run the server:

     python server.py

##    

4. In separate terminals, run clients:

python client.py

##
💬 Usage Example

 Client 1 types:

 hello everyone


 both clients see:

 [client1] hello everyone

 ## 🔧 Troubleshooting

 - If you see ModuleNotFoundError: No module named 'websockets', install it:

pip install websockets


- If port 8765 is busy, change it in both server.py and client.py.




