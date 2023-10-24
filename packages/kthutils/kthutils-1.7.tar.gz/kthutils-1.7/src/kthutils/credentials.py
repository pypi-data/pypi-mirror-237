import os
import sys

def get_credentials():
  """
  Returns tuple (username, password).
  """
  try:
    username = os.environ["KTH_LOGIN"]
    password = os.environ["KTH_PASSWD"]
    return username, password
  except:
    pass
  try:
    username = config.get("credentials.username")
    password = config.get("credentials.password")
    return username, password
  except:
    pass
  logging.error("Couldn't load credentials: "
                "Supply credentials by environment variables "
                "KTH_LOGIN and KTH_PASSWD. "
                "Or set them in the config: "
                "kthutils config credentials.username --set <the username>; "
                "kthutils config credentials.password --set <the password>")
  sys.exit(1)
