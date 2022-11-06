# Curve Config
NETWORK_IDS = ["ethereum", "avalanche", "fantom", "arbitrum", "optimism", "polygon", "xdai"]
TAG_IDS = ["main", "crypto", "factory", "factory-crypto"]
CONDITIONS = ["ABOVE", "BELOW"]

# Endpoints:
GETPOOLS_BASE_ENDPOINT = "https://api.curve.fi/api/getPools/{network_id}/{tag_id}"
CURVE_POOL_BASEURL = "https://curve.fi/#/{network_id}/pools/{pool_id}"

# Process:
POLLING_PERIOD = 10  # Poll pools every 10 seconds

# TELEGRAM SETUP:
TELEGRAM_CHAT_IDS = [-623989512]  # Telegram channels that will receive alerts
TELEGRAM_LOG_CHAT_ID = [1823852648]  # Telegram channels that will receive logs
# Telegram bot token should be stored as TELEGRAM_BOT_TOKEN environment var