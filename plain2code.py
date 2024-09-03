import argparse
import requests
import os
import logging
import shutil

logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def health_check(api_url):
    """Perform a health check on the given API URL."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print(f"Health check successful! Status code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

def clear_folder(address):
    for item in os.listdir(address):
        item = address + f'\\{item}'
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.unlink(item)
    
    
    
def main():

    parser = argparse.ArgumentParser(description="API Health Check Script")
    parser.add_argument('plain_file')
    parser.add_argument('-v', '--verbose', action='store_true', required = False, help = 'Get extra messeges!')
    parser.add_argument('-b', '--Build_folder', type = str, default = 'build', help = 'Build folder location')
    args = parser.parse_args()
    
    plain_source_file = args.plain_file
    try:
        act_file = open(file = plain_source_file, mode = 'r')
    except FileNotFoundError:
        logger.error('No such file')
    verbose = args.verbose
    if verbose:
        logger.setLevel('INFO')
    built = args.build_folder
    build_folder = os.path.abspath(built)
    if os.path.exists(build_folder) and os.path.isdir(build_folder):
        contents = os.listdir(build_folder)
        if contents != []:
            clear_folder(build_folder)
        else:
            logger.info('The folder is ready!')
    else:
        logger.info(f"The folder '{build_folder}' will be created.")
        os.makedirs(build_folder)
    
    
if __name__ == '__main__':
    main()
