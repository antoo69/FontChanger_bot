from email.policy import default

from environs import Env

# Using the environs library
env = Env()
env.read_env()

# Reading the following from the .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # List of admins
# IP = env.str("ip")  # Hosting IP address
BACKEND_URL = env.str("BACKEND_URL", default="http://localhost:8000")  # Default value for BACKEND_URL
ADMIN_TOKEN = env.str("ADMIN_TOKEN")  # Admin token

CHANNELS = env.list("CHANNELS", default=[])  # Channels
