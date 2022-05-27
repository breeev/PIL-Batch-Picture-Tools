# ![alt text](https://github.com/breeev/PIL-Batch-Picture-Tools/blob/main/picture%20icon%20edited.png) PIL-Batch-Picture-Tools
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

#### Examples :
Getting all the png and bmp pictures from the folder 'dossier/pouët/' to negative and mildly contrasted clones in the folder 'modified/pouët/negative+contrast/' in recursive mode (using PowerShell) :  
```powershell
.\PILBPT 'dossier/pouët/' r 'modified/pouët/negative+contrast/' png bmp
negative, contrast:2
add
```
OUTPUT :  
```
What do you want to do to these pictures?
Enter your actions separated by commas among this list:
 - negative;                                                                 
 - contrast:[factor];                                                                                               
 - color:[factor];
 - brightness:[factor];           
 - sharpness:[factor].
negative, contrast:2
Multiple actions chosen. Output to one directory for each action or rename files for each action? You can also just add the effects on a single picture.
    (folders/files/add): add
2 png pictures found, performing tasks:
100%|██████████████████████████████████████████████████████████████████████████████| 256/256 [00:00<00:00, 1857.79it/s]
0.14710569381713867
contrast:2 0.0015316009521484375

Output directory does not exists. Create?
    (y/n): y
100%|██████████████████████████████████████████████████████████████████████████████| 256/256 [00:00<00:00, 1876.79it/s]
0.13994789123535156
contrast:2 0.0010097026824951172
```

### Passive Mode
1. Put your python ~~or exe file~~[^1] in a folder with pictures;  
2. See every picture being cloned with edited version of themselves.  

Very simple  
[^1]: Looks like the passive mode does not work with the exe, both inline and standalone. Weird.  

## 5. Compiling to exe
use auto-py-to-exe or pyinstaller
