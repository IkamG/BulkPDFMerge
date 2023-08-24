from PyPDF2 import PdfMerger
from natsort import os_sorted
import os
import PySimpleGUI as sg
import os.path

menu_def = [['Help', ['Info', '---', 'Exit']]]

file_list_column = [
    [
        sg.Menu(menu_def),
    ],
    [
        sg.Text("PDFs will be combined in lexicographic order based on how it appears in OS",font='Any 8'),
    ],
    [
        sg.Text("PDF Folder",font='Any 12'),
        sg.In(size=(32, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Destination File Name",font='Any 12'),
        sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
        sg.Text(".pdf"),
        
    ],
    [
        sg.HSeparator(),
    ],
    [
        sg.Text("File List - ENSURE ORDER IS CORRECT",p=0,font='Any 9'),
    ],
    [
        
        sg.Listbox(
            values=[], enable_events=True, size=(55, 20), key="-FILE LIST-", p=0
        )
    ],
    [
        sg.Button(button_text="Merge",disabled=True,key="-SUBMIT-",p=((0, 2), (5, 1))),
        sg.ProgressBar(key="Progress",max_value=100,expand_y=True,s=32,p=((3, 0), (5, 1)))
        
    ],
    [
    ]
    
]



# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("Bulk PDF Merge Tool", layout)


#Create an instance of PdfFileMerger() class
merger = PdfMerger()

# Run the Event Loop
while True:
    event, values = window.read()
    dis = not(values["-FOLDER-"] and values["-FILE-"])
    window["-SUBMIT-"].update(disabled=(dis))
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in os_sorted(file_list)
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".pdf"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-SUBMIT-":  
        try:
            folder_len = len(os.listdir(values["-FOLDER-"])) + 1 # your directory path
            
            
            current = 0
            #Define the path to the folder with the PDF files
            path_to_files = values["-FOLDER-"]+r'/'

            #Get the file names in the directory
            for root, dirs, file_names in os.walk(path_to_files):
                #Iterate over the list of the file names
                for file_name in os_sorted(file_names):
                    #Append PDF files
                    merger.append(path_to_files + file_name)
                    current += 1
                    window["Progress"].update((current/folder_len)*100)

            window.set_title("Merging PDFs Please Wait...")
            #Write out the merged PDF file
            merger.write(values["-FILE-"]+".pdf")
            window["Progress"].update(100)
            
            merger.close()
            finishText = "Thank you for using Bulk PDF Merge Tool.\n Your file is ready at "+values["-FILE-"]+".pdf"
            sg.popup(finishText,title='Merging Complete')
            break

        except:
            pass
    elif event == "exit":
        break
    elif event == "Info":
        sg.popup('The program may become unresponsive when merging large datasets.'
                 +' This is normal and indicates that the application is functioning as intended.'
                 +' Please be patient\n\nVersion 0.1.0\nhttps://github.com/IkamG/BulkPDFMergeTool',title='Info')  

window.close()
