# <img src="logo.png" width="100" /> PIL-Batch-Picture-Tools
PILBPT is a tool using Python's PIL library to quickly modify brightness, contrast... in a lot of pictures at once and even make them negative.

## 1. Features
- Scan entire **directories** with a **recursive** option ;  
- **Inline** options ;  
- **Progressbars** and function **timers** ;  
- **Wacky** script structure ;  
- Interactive and stackable actions, per-action output choices ;  
- **Passive Mode** to make things easier and *quicker* !  

## 2. Actions
The tool basically supports every picture enhancement that PIL permits, such as :  
- brightness ;  
- contrast ;  
- color ;  
- sharpness...  

Plus a bonus one: negative rendering! Yay  

## 3. **Dependencies** (for the python script)
(just go see the module import section lol)  

## 4. ***Usage***
### Interactive Mode
```
python PIL-Batch-Picture-Tools.py [input folder] [output folder] [extensions to look for ('*' for all)]
```  
```
PILBPT [input folder] [output folder] [extensions to look for ('*' for all)]
```  
Put a ' r ' anywhere to enable recursive mode.  
After that, you will need to type your actions separated by commas. You can theorically combine them, didn't try tho. Tell me if it works.  
You may also have to choose how to name files and arange them depending on your actions and can be asked to confirm the creation of folders.  
And then, zippy zip, yippy yey, you got yourself some time to make tea or whatever uh  

### Passive Mode
1. Put your python or exe file in a folder with pictures;  
2. See every picture being cloned with edited version of themselves.  

Very simple  

## 5. Compiling to exe
use auto-py-to-exe or pyinstaller
