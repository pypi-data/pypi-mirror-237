import os
import requests

class DiscordTTP:
    def __init__(self) -> None:
        self.token = ''

    def setToken(self, token):
        self.token = token
        return True

    def readAllMessages(self, channelid):
        url = f"https://discord.com/api/v10/channels/{channelid}/messages"

        headers = {
            "Authorization": str(self.token)
        }

        response = requests.get(url, headers=headers)
        messages = response.json()

        for message in messages:
            return message["content"]

    def SendMessage(self, channelid, message):
        url = f"https://discord.com/api/v10/channels/{channelid}/messages"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        
        message_content = str(message)
        payload = {
            "content": message_content
        }
        
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return True
        else:
            return False

    def PullServerInfo(self, guildid):
        url = f"https://discord.com/api/v10/guilds/{guildid}"
        
        headers = {
            "Authorization": self.token
        }
        
        response = requests.get(url, headers=headers)
        server_info = response.json()
        
        server_name = server_info["name"]
        member_count = server_info["approximate_member_count"]
        
        return server_name, member_count

    def PullChannelInfo(self, channelid):
        url = f"https://discord.com/api/v10/channels/{channelid}"
        headers = {
            "Authorization": self.token
        }
            
        response = requests.get(url, headers=headers)
        channel_info = response.json()
        
        channel_name = channel_info["name"]
        channel_type = channel_info["type"]
        
        return channel_name, channel_type

    def PullUserInfo(self, userid):
        url = f"https://discord.com/api/v10/users/{userid}"
        headers = {
            "Authorization": self.token
        }
        
        response = requests.get(url, headers=headers)
        user_info = response.json()
        
        username = user_info["username"]
        discriminator = user_info["discriminator"]

        return username, discriminator

    def PullRoleInfo(self, roleid, guildid):
        url = f"https://discord.com/api/v10/guilds/{server_id}/roles/{role_id}"
        headers = {
            "Authorization": self.token
        }
        
        response = requests.get(url, headers=headers)
        role_info = response.json()
        
        role_name = role_info["name"]
        role_color = role_info["color"]

        return role_name, role_color

    def CreateChannel(self, serverid, channeln):
        url = f"https://discord.com/api/v10/guilds/{serverid}/channels"
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        
        payload = {
            "name": channeln,
            "type": 0
        }
        
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 201:
            return True
        else:
            return False

    def DeleteChannel(self, channelid):
        url = "https://discord.com/api/v10/channels/CHANNEL_ID"
        headers = {
            "Authorization": self.token
        }
        
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            return True
        else:
            return False