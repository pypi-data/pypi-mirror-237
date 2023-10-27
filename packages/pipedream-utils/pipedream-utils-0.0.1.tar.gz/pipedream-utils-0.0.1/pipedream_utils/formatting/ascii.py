from typing import Dict

import prettytable as prettytable


def create_key_value_table(data, column_config: Dict):
    tables = []

    for row in data:
        table = prettytable.PrettyTable(['Event', 'Details'])
        table._max_width = {"Event": 10, "Details": 10}
        for column, config in column_config.items():
            key = config['display_name']
            value = config['formatter'](getattr(row, column))
            table.add_row((key, value))

        table = table.get_string()
        tables.append(table)

    return '\n\n'.join(tables)


def with_table_footer(table):
    list_of_table_lines = table.get_string().split('\n')
    horizontal_line = list_of_table_lines[0]
    result_lines = 1
    msg = "\n".join(list_of_table_lines[:-(result_lines + 1)])
    msg += f'{horizontal_line}\n'
    msg += "\n".join(list_of_table_lines[-(result_lines + 1):])
    return msg


def default_formatter(x):
    return x


def date_formatter(x):
    try:
        return x.strftime('%d %b')
    except AttributeError:
        return x
