# peterparser.py

import os

class PeterParser:
    """A parser for managing configuration settings stored in .ini files.

        ini format: no quotes

            [section_name]
            key = value


        Example read usage:

            >>> parser = PeterParser()
            >>> parser.read('ini_path')
            >>> config = parser.settings
            >>> if parser.has_section('section')
            >>>     data = config['section']
            >>>     data.get('section', 'key')
        """
    def __init__(self):
        self.settings = {}
        self.current_section = self.settings


    def write(self, file_path, title, comment="Auto Generated with PeterParser"):

        file_exists = os.path.exists(file_path)
        mode = 'a+' if file_exists else 'w+'

        with open(file_path, mode) as file:
            if not file_exists:
                file.write("#" * 45 + "\n")
                file.write(f"############ {title} ############\n")
                file.write("#" * 45 + "\n")
                file.write(f'#  """ {comment} """#\n\n\n')


            file.seek(0)
            existing_content = file.read()
            file.seek(0, os.SEEK_END)

            if 'add_my_contracts' in self.settings:
                file.write('[add_my_contracts]\n')
                my_contracts_names_list = self._format_value(self.settings['add_my_contracts']['my_contracts_names_list'])
                file.write(f'my_contracts_names_list = {my_contracts_names_list}\n\n')

            for section, section_values in self.settings.items():
                if section == 'add_my_contracts':  # Skip writing 'add_my_contracts' section again
                    continue

                new_section_name = section
                counter = 1
                while f'[{new_section_name}]' in existing_content:
                    counter += 1
                    new_section_name = f"{section}_{counter}"

                file.write(f'[{new_section_name}]\n')

                for key, value in section_values.items():
                    value_str = self._format_value(value)
                    file.write(f'{key} = {value_str}\n')

                file.write('\n')


    def _format_value(self, value):
        if isinstance(value, list):
            return '[' + ', '.join(self._format_value(item) for item in value) + ']'
        elif isinstance(value, dict):
            return '{' + ', '.join(f'{key}:{self._format_value(val)}' for key, val in value.items()) + '}'
        else:
            return str(value)

    def read(self, file_path):
        with open(file_path, 'r') as file:
            multiline_comment = False

            for line in file:
                line = line.strip()

                if line.startswith('"""'):
                    multiline_comment = not multiline_comment
                    continue

                if multiline_comment or line.startswith('#') or not line:
                    continue

                self._process_line(line)

    def _process_line(self, line):
        if line.startswith('[') and line.endswith(']'):
            self._handle_section(line[1:-1])
        elif '=' in line:
            key, value = map(str.strip, line.split('=', 1))
            value = self._parse_value(value)
            self.current_section[key] = value

    def _handle_section(self, section_name):
        self.settings[section_name] = {}
        self.current_section = self.settings[section_name]

    def _parse_value(self, value):
        if value.startswith('[') and value.endswith(']'):
            return self._parse_list(value)
        elif value.startswith('{') and value.endswith('}'):
            return self._parse_dict(value)
        else:
            return value

    def _parse_list(self, value):
        items = value[1:-1].split(',')
        return [self._parse_value(item.strip()) for item in items]

    def _parse_dict(self, value):
        pairs = value[1:-1].split(',')
        result = {}

        for pair in pairs:
            key, value = map(str.strip, pair.split('=', 1))
            result[key] = self._parse_value(value)

        return result


    def sections(self):
        return self.settings.keys()

    def get(self, section, key):
        return self.settings[section][key]

    def items(self, section):
        if self.has_section(section):
            return self.settings[section].items()
        else:
            return []

    def add_section(self, section):
        if not self.has_section(section):
            self.settings[section] = {}
            return True
        else:
            return False

    def has_section(self, section):
        return section in self.settings

    def remove_section(self, section):
        if self.has_section(section):
            del self.settings[section]
            return True
        else:
            return False

    def set(self, section, key, value):
        if not self.has_section(section):
            self.add_section(section)
        self.settings[section][key] = value

    def unset(self, section, key):
        if self.has_section(section) and self.has_key(section, key):
            del self.settings[section][key]
            return True
        else:
            return False

    def has_key(self, section, key):
        return self.has_section(section) and key in self.settings[section]

    def clear(self):
        self.settings.clear()
