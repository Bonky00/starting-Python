Now that you have Python and VS Code installed, let's create a simple workspace to keep your files organized and write your first Python script.

### Step 1: Create a Project Folder

It's a good practice to create a dedicated folder for each of your programming projects. This keeps your files tidy and makes it easy to find everything.
1. **Create a New Folder:** Go to a location on your computer where you want to store your projects (e.g., your Documents folder, or create a new "Projects" folder on your Desktop).    
2. **Name Your Folder:** Create a new folder and name it something descriptive, like `my_first_python_project` or `data_script_tutorial`.    
    - **Pro Tip:** Avoid spaces in your folder names. If you need to separate words, use underscores (e.g., `my_project` instead of `my project`). This can prevent issues with some tools later on.
        

### Step 2: Open Your Project Folder in VS Code

Now, let's tell VS Code about this new project folder.
1. **Open VS Code:** If it's not already open, launch Visual Studio Code.    
2. **Open Folder:**    
    - Go to **File > Open Folder...**         
    - Navigate to the folder you just created (`my_first_python_project`).        
    - Click **"Select Folder"** (or **"Open"** on macOS).        
3. **Trust the Workspace (if prompted):** VS Code might ask if you "trust the authors of the files in this folder." Since you just created it, you can safely click **"Yes, I trust the authors"** or **"Trust Folder and Enable All Features."** This allows VS Code to enable full functionality for your project.
    
You'll now see your project folder listed in the **Explorer** sidebar on the left side of VS Code. This is where you'll see all your project files and folders.
![Pasted image 20250703004707](https://github.com/user-attachments/assets/312a30c7-698d-4555-b43f-211ad157b2ca)

### Step 3: Create Your First Python File

Now let's create the actual Python file where you'll write your code.

1. **Create New File:** In the VS Code Explorer sidebar (where you see your `my_first_python_project` folder), hover over your folder name. You'll see a few icons appear. Click on the **"New File"** icon (it looks like a piece of paper with a plus sign).    
    - Alternatively, you can go to **File > New File...** and then save it into your project folder.        
2. **Name Your File:** A text box will appear in the Explorer. Type a name for your Python file.   
    - **Important!** Python files always end with the `.py` extension. This tells your computer (and VS Code) that it's a Python script.        
    - Let's name our first file `hello_world.py`.        
    - Press Enter.
        

You'll now see `hello_world.py` listed under your `my_first_python_project` folder in the Explorer, and a new empty editor tab will open on the right, ready for you to type your Python code!
![Pasted image 20250703004842](https://github.com/user-attachments/assets/8b6692eb-9152-4807-b064-19f20896e4c6)

### Step 4:  Select Your Python Interpreter

VS Code needs to know _which_ Python installation to use for your project, especially if you have multiple versions on your system.

NOTE: This may be detected automatically, but always good to make sure when starting a new work area.

1. **Check the Status Bar:** Look at the bottom-right corner of your VS Code window, in the blue status bar. You should see "Python" followed by a version number (e.g., `Python 3.13.5 64-bit`).
    
2. **Select Interpreter (if needed):** If you don't see a Python version, or if you want to explicitly choose one:
    
    - Click on the Python version displayed (the numbers) in the status bar (e.g., `Python 3.13.5 64-bit`).        
    - A list of detected Python interpreters will appear at the top of your VS Code window. Select the one you just installed (it will likely be the latest version of Python 3, often labeled as `Recommended`).        

This step ensures that VS Code is using the correct Python installation to run your scripts.
![Pasted image 20250703005136](https://github.com/user-attachments/assets/f451cb05-3b4f-493d-ab2e-1db63fe53b92)

### Step 5: Optional but Recommended to keep work neat and clean - Create a Python Virtual Environment

**What is a Virtual Environment and Why Do We Need It?**

Imagine you're building different LEGO sets. Each set needs specific types and quantities of LEGO bricks. If you just dump all your bricks into one giant pile, it gets messy, and pieces from one set might accidentally get mixed up with another, causing problems.

A Python **virtual environment** is like creating a separate, isolated box for each of your Python projects.

- **Isolation:** Each box (virtual environment) gets its own set of Python "tools" (libraries/packages) that are specific to _that_ project.    
- **No Conflicts:** This prevents different projects from interfering with each other. If Project A needs an older version of a tool and Project B needs a newer version, they can both have what they need without conflicts.    
- **Cleanliness:** It keeps your main Python installation clean and free from clutter.    
- **Sharing:** It makes it easier to share your project with others, as they can easily set up the exact same environment you used.
    

**How to Create a Virtual Environment in VS Code:**

1. At the top of the window there is a search/command bar. In the bar type a greater than symbol (>) to look through commands
2. Start to type "Python: Create Environment..." unil the command shows up. Click this option. 
![Pasted image 20250703005530](https://github.com/user-attachments/assets/ae6b0cc6-7a1f-4650-b46e-694f37b37a76)

3. Click the option that says "Venv"
![Pasted image 20250703005626](https://github.com/user-attachments/assets/33781b57-f6c7-450b-9872-a9c6f4a067bc)

4. Click the python version you want to use. (you will likely only have the one version that you installed from Part 1)
![Pasted image 20250703005730](https://github.com/user-attachments/assets/1f5e1f5a-0f5c-499c-b4b1-58dba7f95ebf)

5. The virtual environment should be automatically detected once it is done being created. 
	- You will see a new colder in the working folder. This is where all of the project specific '.venv' files will be stored. You will not need to touch anything in there.
	- Additionally you will know you are working in the virtual environment because the python interpreter will have changed to the version you selected with (venv) in the name

![Pasted image 20250703005955](https://github.com/user-attachments/assets/3b1aae1a-6c11-4644-858c-17766afa87b4)

![Pasted image 20250703010116](https://github.com/user-attachments/assets/f9b9825e-5443-4dad-85b6-4f25e8e26dd6)



