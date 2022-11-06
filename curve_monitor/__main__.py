import threading
from dotenv import load_dotenv
# Looks for .env file in current working directory
load_dotenv()


from curve_monitor.alerts import AlertsProcess


if __name__ == '__main__':
    # Run the alerts process
    AlertsProcess().run()