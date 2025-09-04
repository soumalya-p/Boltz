# Boltz
**How to Convert .json file to .pdb file**

**Step 1:** 

Install the latest version of [Python](https://www.python.org/downloads/). (Ignore if you have already)

**Step 2:Biopython installation**

Open your terminal/command line

Type: `pip3 install biopython`

**Step 3:File Preparation**

Create a folder in your computer where two files are present:

(i) Your .json file downloaded from [BOLTZ](https://labs.rowansci.com/) model.

(ii) This python [script](https://github.com/soumalya-p/Boltz/blob/9bb07d825b65f9a622e7f8a7308a46aaa56303ba/converter.py) -- Download and save it in the same folder as 'converter.py'

 **Step 4:Folder Selection in Terminal**

 ~ `cd <file_path>`

 **Step 5: Generate .pdb file & Check**

 Type in terminal: `python3 converter.py <file.json> <outputfile.pdb>`

 e.g., `python3 converter.py structure.json output.pdb`

**Check your local folder :) The last command line should create the .pdb file**