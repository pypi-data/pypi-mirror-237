import click
import sys
from pathlib import Path
from kurde.core import serialize

@click.command()
@click.argument('script', type=click.Path(), default='')
def main(script):
    """Simple configuration language based on Python.
    
    SCRIPT - path to your script [default: stdin]
    """
    if script == '':
        script_path = None
        code = sys.stdin.read()
    else:
        script_path = Path(script)
        code = script_path.read_text()

    serialize(code, script_path)

if __name__ == '__main__':
    main()
