from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "24509589"))
API_HASH = getenv("API_HASH", "717cf21d94c4934bcbe1eaa1ad86ae75")

BOT_TOKEN = getenv("BOT_TOKEN", "7493562717:AAH9DGdNRk5g_kCQ6hxLR39szY-WacI8At0")
OWNER_ID = int(getenv("OWNER_ID", "7427691214"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "gitwizardbypass")
DAXX_API = getenv("DAXX_API", "daxx-1490?api+key:free")
