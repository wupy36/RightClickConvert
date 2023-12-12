import sys
from application import blender as bl
import time

print("************ TASK HAS STARTED ************")

time.sleep(1)

# File location and breakdown information
model = sys.argv[1]

# Processing the files
print('Blend file set up for: %s', model)
bl.blendFile(model)

# print("************ NEXT TASK EXPORT ************")

# time.sleep(1)

# Exporting the file in the opposite format
# print('Exporting the file in the opposite format: %s', model)
# bl.blendExportSingle(model)

print("************ TASK HAS FINISHED ************")
