# Curve Config
NETWORK_IDS = ["ethereum", "avalanche", "fantom", "arbitrum", "optimism", "polygon", "xdai"]
TAG_IDS = ["crypto", "factory", "factory-crypto"]

# Endpoints:
GETPOOLS_BASE_ENDPOINT = "https://api.curve.fi/api/getPools/{network_id}/{tag_id}"

# Process:
POLLING_PERIOD = 5  # Poll balances every 5 seconds