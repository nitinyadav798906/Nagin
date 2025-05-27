"""
from os import getenv


API_ID = int(getenv("API_ID", "12475131"))
API_HASH = getenv("API_HASH", "719171e38be5a1f500613837b79c536f")
BOT_TOKEN = getenv("BOT_TOKEN", "7706778428:AAG2uLYZm84_PLP9IFAWiXr6aTOwVkhUBJA")
OWNER_ID = int(getenv("OWNER_ID", "1714266885"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1714266885").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://nitinyadav798906:CClOsRu0f90aluAC@cluster0.t6r8x57.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002542634912"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002542634912"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "12475131"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "719171e38be5a1f500613837b79c536f")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7706778428:AAG2uLYZm84_PLP9IFAWiXr6aTOwVkhUBJA")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Raftaar_speedskybot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1714266885"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1714266885").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002542634912"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://nitinyadav798906:CClOsRu0f90aluAC@cluster0.t6r8x57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002542634912"))

