import re

class ConfigParser:
    def parse(self, config_string):
        commands = []
        lines = config_string.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):  # Ignore empty lines and comments
                continue

            parts = line.split()
            if not parts:
                continue

            action = parts[0]
            target = None
            parameters = {}
            i = 1
            while i < len(parts):
                if parts[i].startswith('--'):
                    if i + 1 < len(parts):
                        param_name = parts[i][2:]
                        param_value = parts[i + 1]
                        parameters[param_name] = param_value
                        i += 2
                    else:
                        raise ValueError(f"Missing value for parameter '{parts[i]}' in line: {line}")
                else:
                    if target is None:
                        target = parts[i]
                        i += 1
                    else:
                        raise ValueError(f"Unexpected token '{parts[i]}' in line: {line}")

            commands.append({'action': action, 'target': target, 'parameters': parameters})
        return commands

if __name__ == "__main__":
    parser = ConfigParser()
    example_config = """
    create directory --name my_new_folder
    copy file --source original.txt --destination backup.txt
    delete file --name temp.log
    # This is a comment
    """
    parsed_commands = parser.parse(example_config)
    for cmd in parsed_commands:
        print(cmd)