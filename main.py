import re

# ---------------------------------------------------------------------
#  is_a_valid_**** :
#  Are collection of function to validate the target parameter
# ---------------------------------------------------------------------
def is_a_valid_hostname(target_string: str) -> bool:
    # Regular expression to match a valid hostname
    pattern = re.compile(
        r'^(?!\d+$)[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')

    # Split the hostname by dots and validate each label
    if len(target_string) <= 253:
        hostnames = target_string.split('.')
        return all(pattern.match(host) for host in hostnames)

    return False


def is_a_valid_ipv4_addr(ip_str):
    # Validate the ip octets are in between 0 and 255
    try:
        octets = map(int, ip_str.split("."))
        return all( 0 <= octet <= 255 for octet in octets)
    except ValueError:
        return False


def is_a_valid_prefix_length(prefix_str):
    # Validate that the prefix of CIDR is between 0 and 32
    try:
        prefix = int(prefix_str)
        return 0 <= prefix <= 32
    except ValueError:
        return False


def is_a_valid_cdir_notation(target_string):
    # Validate that target contain the ip and suffix part
    try:
        ip_adrr_str, prefix_length_str = target_string.split('/')
        return is_a_valid_ipv4_addr(ip_adrr_str) and is_a_valid_prefix_length(prefix_length_str)
    except ValueError:
        return False


def is_a_valid_ipv4_octet(octet_str):

    try:
        bite = int(octet_str)
        return 0 <= bite <= 255
    except ValueError:
        return False


def is_a_valid_ipv4_octet_range(range_str):
    # Validate that values of the range is between 0 and 255 and from minor to mayor
    try:
        low_number, high_number = map(int, range_str.split('-'))
        return 0 <= low_number <= high_number <= 255
    except (ValueError, IndexError):
        return False


def is_a_valid_ipv4_with_range(ip_str):
    # Validate is the ip have valid octet or range
    try:
        octets = ip_str.split('.')
        for octet in octets:
            if not is_a_valid_ipv4_octet(octet) and not is_a_valid_ipv4_octet_range(octet):
                raise ValueError
        return True
    except ValueError:
        return False

# =====================================================================


def type_of_target(target_string):
    # Deteminate with type of notation is on the target parameter
    type_target = 0
    if is_a_valid_hostname(target_string):
        type_target = 1
    elif is_a_valid_cdir_notation(target_string):
        type_target = 2
    elif is_a_valid_ipv4_with_range(target_string):
        type_target = 3
    return type_target


# -----------------
# MAIN PROGRAM
# -----------------

target_string = "192.168.f0.1/24"

match type_of_target(target_string):
    case 1:
        pass
    case 2:
        pass
    case 3:
        pass
    case other:
        print("Incorrect target; Use CIDR (192.168.1.0/24) or range (192.168.1.0-100)")

