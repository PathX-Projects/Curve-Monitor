import threading
from dotenv import load_dotenv

from curve_monitor.alerts import AlertsProcess

# Looks for .env file in current working directory
load_dotenv()

# Run the alerts process
AlertsProcess().run()