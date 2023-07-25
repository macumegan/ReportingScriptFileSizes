import os
for path_info in os.walk('.'):
    print(path_info)
    break

import os
from os.path import abspath, join

import os
from os.path import abspath, join

# producing absolute paths, instead of a tuple of three items
for top_dir, directories, files in os.walk('.'):
    for directory in directories:
        print(abspath(join(top_dir, directory)))
    for _file in files:
        print(abspath(join(top_dir, _file)))
    break

# Now we can examine them for file data

import os 
from os.path import abspath, join, getsize

sizes = {}

for top_dir, directories, files in os.walk('.'):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
        #break
sorted_results = sorted(sizes, key=sizes.get, reverse=True)

for path in sorted_results[:20]:
    print("Path:{0}, size: {1}".format(path,sizes[path]))

