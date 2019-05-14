# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(old_path, new_path):
    try:
        f_read = open(old_path)
        content = f_read.readlines()
        f_write = open(new_path, "w+")
        for i in content:
            f_write.write(i)
        f_read.close()
        f_write.close()
    except FileNotFoundError:
        print("The original file does not exist.")
    
copy_file("tic_tac_toe.py", "copy-tic_tac_toe.py")
     