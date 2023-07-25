# ReportingScriptFileSizes Pro

Python script in a single file that will traverse the filesystem finding the largest files in a path.

I create a new Github repository with a README and a single python file.

The Python script accept an argument to traverse any path.

I was use different options in the script for reporting, like:

    *No more than 20 files.

    *Files larger  than a specific size in megabytes.

I completed a project in GitHub with a README.md and a video reference in my GitHub Project.

# Watch the video tutorial
![FileSizes](https://github.com/macumegan/ReportingScriptFileSizes/blob/6be30918b086551e9cd78f04cbddd3b3dc4bcd45/Untitled.jpg)
[FileSizes](https://youtu.be/AqoIP_I8T0U)



This Python code uses the standard library os to traverse a directory and its subdirectories, obtaining the size of each file, and then displaying the top 20 largest file paths along with their sizes.

# Step-by-step breakdown:

1.Import the necessary libraries:

    import os
    from os.path import abspath, join, getsize

The code imports the functions abspath, join, and getsize from the os.path module. These functions will be used later to work with file paths and obtain their sizes.

2.Initialize an empty dictionary to store file sizes:
   
    sizes = {}

The dictionary "sizes" will be used to store the full file paths as keys and their sizes as values.

3.Traverse the directory and its subdirectories using os.walk():
    
    for top_dir, directories, files in os.walk('.'):

The os.walk() function is a convenient way to recursively traverse a directory and obtain the names of its subdirectories and files. In this case, it starts in the current directory ('.') and traverses all its subdirectories and files.

4.Get the full path and size of each file:
   
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size

Within the loop, it gets the current file's name (_file) and constructs the full path by combining the current directory (top_dir) with the file name using os.path.join(). Then, it obtains the file size using os.path.getsize() and stores it in the "sizes" dictionary using the full path as the key.

5.Sort the results by size in descending order:
    
    sorted_results = sorted(sizes, key=sizes.get, reverse=True)

The sorted() function is used to sort the "sizes" dictionary based on its values (file sizes) in descending order. The key=sizes.get parameter indicates that the values of the dictionary should be used for sorting.

6.Display the top 20 file paths along with their sizes:
   
    for path in sorted_results[:20]:
        print("Path: {0}, size: {1}".format(path, sizes[path]))

Finally, it iterates through the top 10 file paths obtained after sorting the dictionary. It displays the file path along with its size using print(). The output will show the top 20 largest file paths and their corresponding sizes.