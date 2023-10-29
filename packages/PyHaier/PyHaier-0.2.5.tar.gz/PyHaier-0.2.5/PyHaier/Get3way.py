def Get3Way(payload):
    """
    Function for displaying if pump is on or off
    payload - register from 141 to 157
    :return:
    """
    tmp = divmod(int(hex(payload[0]), 16), 256)[0]
    if tmp == 4:
        threeway = 'CH'
    elif tmp == 6:
        threeway = 'DHW'
    else:
        threeway = 'ERR'
    return threeway
