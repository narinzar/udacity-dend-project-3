import configparser

config = configparser.ConfigParser()
config.read('./redshift/dwh.cfg')

try:
    print(config.sections())  # Debug: print sections
    access_key = config.get('S3', 'aws_access_key_id')
    secret_key = config.get('S3', 'aws_secret_access_key')
except configparser.NoSectionError:
    print("Error: No section 'S3' found in the configuration file.")
except configparser.NoOptionError as e:
    print(f"Error: Unable to find expected option in 'S3' section - {str(e)}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
