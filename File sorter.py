import time 
import shutil
import os 

def file_sorter():
    path = input(r"Path Users\kasim\Desktop\Folder1 ")
    os.chdir(path)

    #File Location
    csv_file = r"C:\Users\kasim\Desktop\Folder1\csv"
    xlsx_file = r"C:\Users\kasim\Desktop\Folder1\xlsx"
    pdf_file = r"C:\Users\kasim\Desktop\Folder1\pdf"
    sql_file = r"C:\Users\kasim\Desktop\Folder1\sql"
    txt_file = r"C:\Users\kasim\Desktop\Folder1\text"

    #Delay process by 1 second
    print("Sorting File into folder..")
    time.sleep(1)

    list_dir = os.listdir(path)

    #Sort each file into the correct location
    for file in list_dir:
        if(file.lower().endswith(".csv")):
            shutil.move(file,csv_file)
        elif(file.lower().endswith(".pdf")):
            shutil.move(file, pdf_file)
        elif(file.lower().endswith(".sql")):
            shutil.move(file, sql_file)
        elif(file.lower().endswith(".txt")):
            shutil.move(file, txt_file)
        elif(file.lower().endswith(".xlsx")):
            shutil.move(file, xlsx_file)                

file_sorter()