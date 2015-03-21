import subprocess
import os
import time

proselint_tests_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "corpus")

start = time.time()
for file in os.listdir(proselint_tests_path):
    filepath = os.path.join(proselint_tests_path, file)
    if ".md" == filepath[-3:]:
        subprocess.call("proselint --debug {}".format(filepath), shell=True)

print time.time() - start
