def dbs_agent(command):
    import config
    import mysql.connector as msc
    with msc.connect(
            host=config.host,
            user=config.user,
            password=config.passwd
    ) as dbs:
        cursor = dbs.cursor()
        cursor.execute(f"{command}")
        dbs.commit()


def header(banner):
    import pyfiglet, colorama
    printer = pyfiglet.figlet_format(banner, font="banner3")
    print(colorama.Fore.GREEN + printer)
    colorama.Style.RESET_ALL


def current_time(time_parameter):
    """ Parameters : full_time, hour, minute, now """
    import datetime
    clock = datetime.datetime.now()
    result = None
    if time_parameter == "full_time":
        result = f"{clock.hour} : {clock.minute}"
    elif time_parameter == "hour":
        result = clock.hour
    elif time_parameter == "minute":
        result = clock.minute
    elif time_parameter == "now":
        result = clock
    return result


def logs(log):
    """ Writes logs. """
    log_file = open(".logs", "a")
    log_file.write(f"=> {current_time('now')} : {log}\n")
    log_file.close()
