import os
import shutil
import subprocess

class ConfigTranslator:
    def translate(self, parsed_commands):
        shell_commands = []
        for cmd in parsed_commands:
            action = cmd['action']
            target = cmd.get('target')
            parameters = cmd['parameters']

            if action == "create":
                if target == "directory" and "name" in parameters:
                    shell_commands.append(f"mkdir -p '{parameters['name']}'")
                elif target == "file" and "name" in parameters:
                    shell_commands.append(f"touch '{parameters['name']}'")
                else:
                    print(f"Warning: Invalid 'create' command: {cmd}")
            elif action == "copy":
                if target == "file" and "source" in parameters and "destination" in parameters:
                    shell_commands.append(f"cp '{parameters['source']}' '{parameters['destination']}'")
                else:
                    print(f"Warning: Invalid 'copy' command: {cmd}")
            elif action == "delete":
                if target == "file" and "name" in parameters:
                    shell_commands.append(f"rm '{parameters['name']}'")
                elif target == "directory" and "name" in parameters:
                    shell_commands.append(f"rm -rf '{parameters['name']}'")
                else:
                    print(f"Warning: Invalid 'delete' command: {cmd}")
            else:
                print(f"Warning: Unknown action '{action}': {cmd}")
        return shell_commands

    def execute(self, shell_commands):
        print("\nExecuting Shell Commands:")
        for cmd in shell_commands:
            print(f">> {cmd}")
            try:
                subprocess.run(cmd, shell=True, check=False)  # Be cautious when executing arbitrary shell commands
            except Exception as e:
                print(f"Error executing '{cmd}': {e}")

if __name__ == "__main__":
    from config_parser import ConfigParser

    parser = ConfigParser()
    translator = ConfigTranslator()

    with open("example_config.txt", "r") as f:
        config_content = f.read()

    parsed_commands = parser.parse(config_content)
    print("Parsed Commands:")
    for cmd in parsed_commands:
        print(cmd)

    shell_commands = translator.translate(parsed_commands)
    print("\nGenerated Shell Commands:")
    for cmd in shell_commands:
        print(cmd)

    # translator.execute(shell_commands) # Uncomment this to actually execute the commands