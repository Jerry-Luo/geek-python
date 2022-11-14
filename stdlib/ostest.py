import os
for root, directory, files in os.walk("/Users/Jerry/Downloads"):
    print(root, directory, files)
