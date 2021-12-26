import sys
import traceback
from os import remove


def delete_duplicate_line(file_path):
    """ """
    lines_seen = set()  # holds lines already seen
    outfile = open(file_path + "_tmp_", "w")
    for line in open(file_path, "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    with open(file_path + "_tmp_", "r+") as filet:
        with open(file_path, "w") as filet2:
            filet2.write(filet.read())

    # We delete the tempory file
    remove(file_path + "_tmp_")


def record_or_not(record_mode, line, start_block, end_block):
    """ """
    if not record_mode:
        if start_block in line:
            record_mode = True
    elif end_block in line:
        record_mode = False
    return record_mode


def returnStateMentIfMessageIsEmpty(msg, statement):
    """ """
    if msg is None:
        return statement + ":"
    else:
        return msg + ":\n| >> " + statement


def selfOnParams(check, self_on_function_params, add_semicolon=False):
    """ """
    if self_on_function_params:
        comma = ""
        if add_semicolon:
            comma = ","
        if len(check) > 2:
            return check + comma
    else:
        return ""


def get_trace():
    print("Exception in code:")
    print("-" * 60)
    traceback.print_exc(file=sys.stdout)
    print("-" * 60)
