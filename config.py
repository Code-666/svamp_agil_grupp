# file method. We could also do environment variable method
secret_key_file_path = "PATH TO SECRET KEY"

with open(secret_key_file_path, "r") as f:
    secret_key = f.read().strip()
