# Curve Config
NETWORK_IDS = ["ethereum", "avalanche", "fantom", "arbitrum", "optimism", "polygon", "xdai"]
TAG_IDS = ["main", "crypto", "factory", "factory-crypto"]
CONDITIONS = ["ABOVE", "BELOW"]

# Endpoints:
GETPOOLS_BASE_ENDPOINT = "https://api.curve.fi/api/getPools/{network_id}/{tag_id}"
CURVE_POOL_BASEURL = "https://curve.fi/#/{network_id}/pools/{pool_id}"

# Process:
POLLING_PERIOD = 5  # Poll balances every 5 seconds