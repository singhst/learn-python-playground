import configparser


full_config_file_path = "./config.ini"

config = configparser.ConfigParser()
config.read(full_config_file_path)
print(config["sqlite"].get("test_connection_str"))