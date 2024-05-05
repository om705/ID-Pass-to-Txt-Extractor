import os

api_id = 28660719
api_hash = os.environ.get("API_HASH", "34ade52147ebcaf4bc0b88aa3dfc7e1a")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6723621303")
sudo_users = [int(num) for num in auth_users.split("6723621303")]
osowner_users = os.environ.get("OWNER_USERS", "6723621303")
owner_users = [int(num) for num in osowner_users.split("6723621303")]
