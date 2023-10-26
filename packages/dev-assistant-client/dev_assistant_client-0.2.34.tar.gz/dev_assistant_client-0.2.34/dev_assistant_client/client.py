import os
import json
import asyncio
import socket
from colorama import Fore, Style
import requests
from dev_assistant_client.client_auth import ClientAuth
from dev_assistant_client.api_client import APIClient
from dev_assistant_client.ably_handler import AblyHandler
from dev_assistant_client.utils import (
    CERT_FILE,
    CLIENT_ID_FILE,
    KEY_FILE,
    TOKEN_FILE,
    CLIENT_ID,
    API_URL,
    dd,
    now,
    read_token,   
)

async def connect_client():
    """
    Tries to connect the client to the server. It starts by reading a token, creates
    a client payload and makes a POST call to the server. If the call is successful,
    the client is connected and the CLIENT ID is saved locally. Then, it tries to establish
    a WebSocket connection using the ably_connect() function from auth.py.
    """
    print(now(), "Connecting...\t", sep="\t", end="\t")
    
    auth_client = ClientAuth()
    api_client = APIClient(f"{API_URL}")
    
    # -------------------
    
    payload = {
        "id": CLIENT_ID or "",
        "name": socket.gethostname(),
        "type": "CLI",
    }    
    response = api_client.post("/clients", data=payload)
    if response.status_code == 401:  # Chamada não autorizada
        return auth_client.reauthenticate()
        
    # -------------------
    
    client_id = json.loads(response.content).get("id")
 
    if response.status_code in [200, 201]:
        print(Fore.LIGHTGREEN_EX + "Connected!" + Style.RESET_ALL, sep="\t")
        with open(CLIENT_ID_FILE, "w") as f:
            f.write(client_id)

        print(now(), "CLIENT ID: \t", Fore.LIGHTYELLOW_EX + client_id + Style.RESET_ALL, sep="\t")
        await AblyHandler().ably_connect()
    else:
        print(Fore.LIGHTRED_EX + "Failed to connect!" + Style.RESET_ALL, sep="\t")
        if response.status_code == 401:
            print( Fore.LIGHTRED_EX + "Error: " + Style.RESET_ALL, json.loads(response.content).get('error'), sep="\t")
            print( Fore.LIGHTRED_EX + "Please log in again." + Style.RESET_ALL, sep="\t")
            os.remove(TOKEN_FILE)
            
            # authenticate client again
            auth_client = ClientAuth()
            auth_client.reauthenticate()
            if auth_client.authenticate():
                # If a loop is already running, create a new task in the running loop
                if asyncio.get_event_loop().is_running():
                    asyncio.create_task(connect_client())
                else:
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(connect_client())          

        else:
            print(now(), "Status code: ", response.status_code, sep="\t")
            print(now(), "Response: ", response.content, sep="\t")