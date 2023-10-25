import os
import click
import logging
import pyperclip
from colorama import init, Fore

init(autoreset=True)

# Setup logging
logging.basicConfig(filename='./codebasedutils.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


@click.group()
def util():
    """Utility commands."""
    pass

@util.command(name="tree")
@click.argument('path', default='.')
@click.option('--exclude', default='', help='File patterns to exclude (e.g. *.log)')

def dirprint(path, exclude):
    """Prints a directory structure, ignoring nonessential files and copies it to clipboard."""
    output_buffer = []

    def should_exclude(file_name):
        patterns_to_exclude = ['.pyc', '__pycache__', 'venv', '.venv', 'node_modules', 'test_env',
        'test_venv', 'testenv']
        return (
            file_name.startswith('.') or
            any(file_name.endswith(pattern) or file_name == pattern for pattern in patterns_to_exclude) or
            (exclude and file_name.endswith(exclude))
        )

    def print_and_copy_directory_structure(startpath):
        for root, dirs, files in os.walk(startpath):
            dirs[:] = [d for d in dirs if not should_exclude(d)]
            files = [f for f in files if not should_exclude(f)]

            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            line = f'{indent}{os.path.basename(root)}/'
            print(f'{Fore.BLUE}{line}')
            output_buffer.append(line)

            subindent = ' ' * 4 * (level + 1)
            for file in files:
                line = f'{subindent}{file}'
                print(f'{Fore.GREEN}{line}')
                output_buffer.append(line)

    try:
        print_and_copy_directory_structure(path)
        pyperclip.copy('\n'.join(output_buffer))
        click.echo(f"{Fore.YELLOW}Directory structure copied to clipboard.")
    except FileNotFoundError:
        logging.error("The specified directory doesn't exist.")
        click.echo(f"{Fore.RED}Error: The specified directory doesn't exist.")
    except PermissionError:
        logging.error("Permission denied for reading the directory.")
        click.echo(f"{Fore.RED}Error: Permission denied for reading the directory.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        click.echo(f"{Fore.RED}An unexpected error occurred. Check logs for details.")

if __name__ == "__main__":
    util()
