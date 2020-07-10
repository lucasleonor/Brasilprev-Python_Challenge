from python_challenge.helpers.status_code import code as status_code_dict

common_errors = {}
get_by = update = {}
delete = {}
create = {}


def add_code(status_code, add_to, is_list=False):
    if not is_list:
        status_code = [status_code]
    for code in status_code:
        add_to[code] = status_code_dict[code]
    return add_to


add_code([400, 401, 500], is_list=True, add_to=common_errors)
add_code([200, 404], is_list=True, add_to=get_by)
add_code([204, 404], is_list=True, add_to=delete)
add_code([201], is_list=True, add_to=create)
