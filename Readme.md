# Bulk PDF Merge Tool
The Bulk PDF Merge Tool is a lightweight application designed to facilitate the merging of a large number of PDFs, particularly useful when dealing with resulting PDFs that have a total page count surpassing Adobe's limit of 1500 pages.
## Usage
Utilizing the BPM Tool is straightforward. Simply specify the directory containing your source PDFs, and indicate the desired name for the resultant final PDF.

To run the BPM Tool on Windows systems, use the packaged `BPM_Tool.exe`. Alternatively, you can run it from the source code by executing `python BPM_Tool.py`.

BPM Tool merges your PDFs based on the lexicographic order defined by your Operating System.

![](images/StartScreen.png?raw=true "Start Screen")
!["Windows Explorer Ordering"](images/OSLexicographic.png?raw=true "Windows Explorer Ordering")

Once you've verified that your merge ordering is correct, click the merge button and wait for the PDF to be generated.

- Please note BPM Tool may become unresponsive when merging large datasets. This is normal and indicates that the application is functioning as intended.

## Requirements

Python requirements can be found in `requirements.txt`