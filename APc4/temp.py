#open file for writing
#	creates file if it does not exist
#	overwrites file if it exists
temp_file = open("temp.txt","w")
print("first line", file=temp_file)
print("second line", file=temp_file)
temp_file.close()
