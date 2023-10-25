import click
import subprocess

@click.command()
def start():
    """Start your VM."""
    try:
        subprocess.run(['gcloud', 'compute', 'instances', 'start', '--zone=europe-west9-a', 'lewagon-data-eng-vm-alexcanc'], check=True)
        click.echo("VM started.")
    except subprocess.CalledProcessError as e:
        click.echo(f"An error occurred while starting the VM: {e}", err=True)

@click.command()
def stop():
    """Stop your VM."""
    try:
        subprocess.run(['gcloud', 'compute', 'instances', 'stop', '--zone=europe-west9-a', 'lewagon-data-eng-vm-alexcanc'], check=True)
        click.echo("VM stopped.")
    except subprocess.CalledProcessError as e:
        click.echo(f"An error occurred while stopping the VM: {e}", err=True)

@click.command()
def connect():
    """Connect to your VM in VSCode inside your specified folder."""
    try:
        # Construct the URI for the VSCode remote connection. You might need to replace 'username' with your actual username on the VM.
        vscode_uri = "vscode-remote://ssh-remote+alexcanc@34.155.47.49/home/alexcanc/code/alexcanc/data-engineering-challenges/"
        # Command to open VSCode with the specific folder URI. The 'code' command must be available in your system's PATH.
        subprocess.run(['code', '--folder-uri', vscode_uri], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"An error occurred while trying to connect to the VM using VSCode: {e}", err=True)
