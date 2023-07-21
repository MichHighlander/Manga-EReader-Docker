import os

# Accessing the custom option in the container
custom_option = os.environ.get('CUSTOM_OPTION')
print(custom_option)
