def dbs_agent(command):
  import config
  import mysql.connector as msc
  with msc.connect(
    host = config.host,
    user = config.user,
    password = config.passwd
  ) as dbs:
    cursor = dbs.cursor()
    cursor.execute(f"{command}")
    dbs.commit()

def header(header):
  import pyfiglet, colorama
  printer = pyfiglet.figlet_format(header, font="banner3")
  print(colorama.Fore.GREEN + printer)
  colorama.Style.RESET_ALL
