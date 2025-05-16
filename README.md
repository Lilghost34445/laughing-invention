# ConfigTranslator

## Description

The `ConfigTranslator` class is a Python utility that translates high-level configuration commands into executable shell commands. It supports actions like creating directories and files, copying files, and deleting files or directories.  This is useful for automating system configuration tasks based on a simple, declarative configuration format.

## Features

* **Command Translation:** Translates configuration commands into standard shell commands (`mkdir`, `touch`, `cp`, `rm`).
* **File and Directory Operations:** Supports creating, copying, and deleting both files and directories.
* **Error Handling:** Provides warnings for invalid or unknown commands and handles errors during shell command execution.
* **Dry Run Capability:** Includes a `dry_run` mode to preview the shell commands that would be executed without actually running them.
* **Secure Command Execution:** Uses `shlex.split()` to prevent shell injection vulnerabilities when executing commands.
* **Detailed Output:** When executing commands, the script prints the command, return code, standard output, and standard error.

## Usage

### Installation

No special installation is required.  The `ConfigTranslator` class is a self-contained Python class.  Simply include it in your project.

### Class Definition

```python
import os
import shutil
import subprocess
import shlex

class ConfigTranslator:
    def __init__(self, dry_run=False):
        """
        Initializes the ConfigTranslator.

        Args:
            dry_run (bool, optional): If True, prints the shell commands but
                does not execute them. Defaults to False.
        """
        self.dry_run = dry_run

    def translate(self, parsed_commands):
        """
        Translates parsed configuration commands into a list of shell commands.

        Args:
            parsed_commands (list): A list of dictionaries, where each dictionary
                represents a parsed configuration command.
        Returns:
            list: A list of strings, where each string is a shell command.
        """
        # ... (code as provided)

    def execute(self, shell_commands):
        """
        Executes the generated shell commands.

        Args:
            shell_commands (list): A list of shell commands to execute.
        """
        # ... (code as provided)
Examplefrom config_translator import ConfigTranslator

# Example usage with a mock ConfigParser
class ConfigParser:
    def parse(self, config_content):
        return [
            {'action': 'create', 'target': 'directory', 'parameters': {'name': '/tmp/my_dir'}},
            {'action': 'create', 'target': 'file', 'parameters': {'name': '/tmp/my_file.txt'}},
            {'action': 'copy', 'target': 'file', 'parameters': {'source': '/tmp/my_file.txt', 'destination': '/tmp/my_file_copy.txt'}},
            {'action': 'delete', 'target': 'directory', 'parameters': {'name': '/tmp/my_dir'}},
            {'action': 'delete', 'target': 'file', 'parameters': {'name': '/tmp/my_file.txt'}},
        ]

parser = ConfigParser()  #  Mock parser
translator = ConfigTranslator(dry_run=False) # Set to True for a dry run

config_content = """
create directory name=/tmp/my_dir
create file name=/tmp/my_file.txt
copy file source=/tmp/my_file.txt destination=/tmp/my_file_copy.txt
delete directory name=/tmp/my_dir
delete file name=/tmp/my_file.txt
"""

parsed_commands = parser.parse(config_content)
shell_commands = translator.translate(parsed_commands)

print("Parsed Commands:")
for cmd in parsed_commands:
    print(cmd)

print("\nGenerated Shell Commands:")
for cmd in shell_commands:
    print(cmd)

translator.execute(shell_commands)
Configuration FormatThe ConfigTranslator expects a list of dictionaries as input, where each dictionary represents a configuration command.  The dictionary should have the following keys:action (str): The action to perform.  Valid values are "create", "copy", and "delete".target (str): The type of object to act on.  Valid values are "file" and "directory".parameters (dict): A dictionary of parameters for the action.  The required parameters depend on the action and target.Parameterscreate directory:name (str): The name of the directory to create.create file:name (str): The name of the file to create.copy file:source (str): The path to the source file.destination (str): The path to the destination file.delete file:name (str): The name of the file to delete.delete directory:name (str): The name of the directory to delete.  The directory will be deleted recursively (i.e., including its contents).Error HandlingThe ConfigTranslator provides the following error handling:Invalid Action/Target: If an invalid action or target is specified, a warning message is printed.Missing Parameters: If a required parameter is missing for a given action, a warning message is printed.Shell Command Errors: If a shell command fails to execute, the error message from the shell is printed, including the return code, stdout, and stderr.Dry RunThe dry_run option allows you to preview the shell commands that would be executed without actually running them.  To use dry run, set the dry_run parameter to True when creating a ConfigTranslator instance:translator = ConfigTranslator(dry_run=True)
DependenciesPython 3.x
