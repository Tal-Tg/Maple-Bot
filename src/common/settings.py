

def validate_nonnegative_int(value):


    if int(value) >= 1:
        return int(value)
    raise ValueError(f"'{value}' is not a valid non-negative integer.")


def validate_boolean(value):


    value = value.lower()
    if value in {'true', 'false'}:
        return True if value == 'true' else False
    elif int(value) in {0, 1}:
        return bool(int(value))
    raise ValueError(f"'{value}' is not a valid boolean.")


def validate_arrows(key):

    if isinstance(key, str):
        key = key.lower()
        if key in ['up', 'down', 'left', 'right']:
            return key
    raise ValueError(f"'{key}' is not a valid arrow key.")


def validate_horizontal_arrows(key):


    if isinstance(key, str):
        key = key.lower()
        if key in ['left', 'right']:
            return key
    raise ValueError(f"'{key}' is not a valid horizontal arrow key.")



SETTING_VALIDATORS = {
    'move_tolerance': float,
    'adjust_tolerance': float,
    'record_layout': validate_boolean,
    'buff_cooldown': validate_nonnegative_int
}


def reset():


    global move_tolerance, adjust_tolerance, record_layout, buff_cooldown
    move_tolerance = 0.1
    adjust_tolerance = 0.01
    record_layout = False
    buff_cooldown = 180



move_tolerance = 0.1


adjust_tolerance = 0.01


record_layout = False


buff_cooldown = 180

reset()
