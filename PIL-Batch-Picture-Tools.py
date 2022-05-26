from PIL import Image,ImageEnhance
from glob import glob
from tqdm import tqdm
from sys import argv
from os.path import exists,abspath,dirname
from os import makedirs
from copy import deepcopy
from time import time
helpmessage="No option selected, entering passive mode.\nOptions: [input folder] [output folder] [picture format or * for all possible formats]\n\
You can also put anywhere the option 'r' for a recursive folder scan.\nPro tip: on Windows you can either right-click and 'copy as path' your directories or \
drag & drop your folders in this window."
passivemode=False
alltypes=['jpg','jpeg','png','ico','gif','webp','bmp','tiff','tga']
if len(argv)==1:
    print(helpmessage)
    passivemode=True
    types=alltypes
    rec=False
else:
    if 'r' in argv:
        rec=True
        argv.pop(argv.index('r'))
    else:rec=False
    if argv[3]!='*':types=argv[3:]
    else:types=alltypes
if passivemode:actions=['negative','contrast:3','color:7','brightness:3','sharpness:0.3']
else:actions=input('What do you want to do to these pictures?\nEnter your actions separated by commas among this list:\n - negative;\n - contrast:[factor];\n - color:[factor];\n - brightness:[factor];\n - sharpness:[factor].\n').replace(' ','').split(',')
if len(actions)>1 and not passivemode:
    choice=input('Multiple actions chosen. Output to one directory for each action or rename files for each action? You can also just add the effects on a single picture.\n    (folders/files/add): ')
    individualfolders=True if choice=='folders' else False
    add=True if choice=='add' else False
else:
    individualfolders=False
    add=False
ne,cn,cl,br,sh=[0]*5
def negative(gvn_img):
    global ne
    ne+=1
    # Get the width and height of the image using size attribute
    width,height = gvn_img.size
    sample=gvn_img.getpixel((0,0))
    single=(type(sample) is int)
    alpha=(type(sample) is tuple and len(sample)>3)
    # Loop till the width of the image using the for loop
    for m in tqdm(range(width)):
        # Loop again till the height of the image using another nested for loop
        for n in range(height):
            # Get the r, g, b pixels of the image using getpixel() function
            if single:r,g,b=gvn_img.getpixel((m,n)),gvn_img.getpixel((m,n)),gvn_img.getpixel((m,n))
            elif alpha:r,g,b,a=gvn_img.getpixel((m,n))
            else:r,g,b=gvn_img.getpixel((m,n))
            # Subtract 255 from the given r to get its exact value. 
            # Similarly do the same for g and b
            r=255-r
            g=255-g
            b=255-b
            # Pass the modified r, g, b values to the putpixel() function(converting into negative image)
            if alpha:gvn_img.putpixel((m,n),(r,g,b,a))
            elif single:gvn_img.putpixel((m,n),(r))
            else:gvn_img.putpixel((m,n),(r,g,b))
    if ne-1:return 'negative'+str(ne-1),gvn_img
    return 'negative',gvn_img

def contrast(img,factor):
    global cn
    cn+=1
    if cn-1:return 'contrast'+str(cn-1),ImageEnhance.Contrast(img).enhance(factor)
    return 'contrast',ImageEnhance.Contrast(img).enhance(factor)

def brightness(img,factor):
    global br
    br+=1
    if br-1:return 'brightness'+str(br-1),ImageEnhance.Brightness(img).enhance(factor)
    return 'brightness',ImageEnhance.Brightness(img).enhance(factor)

def color(img,factor):
    global cl
    cl+=1
    if cl-1:return 'color'+str(cl-1),ImageEnhance.Color(img).enhance(factor)
    return 'color',ImageEnhance.Color(img).enhance(factor)

def sharpness(img,factor):
    global sh
    sh+=1
    if sh-1:return 'sharpness'+str(sh-1),ImageEnhance.Sharpness(img).enhance(factor)
    return 'sharpness',ImageEnhance.Sharpness(img).enhance(factor)

for filetype in types:
    if passivemode:pics=[p.replace("\\", "/") for p in glob(dirname(abspath(__file__)).replace('\\','/')+'/**'*rec+'/*.'+filetype, recursive=rec)]
    else:pics=[p.replace("\\", "/") for p in glob(argv[1]+'/**'*rec+'/*.'+filetype, recursive=rec)]
    if not pics:continue
    print(f'{len(pics)} {filetype} pictures found, performing tasks:')
    for pic in pics:
        piclist=[]
        ne,cn,cl,br,sh=[0]*5
        if passivemode:path=''
        else:path=argv[2].replace("\\", "/")+'/'
        img=Image.open(pic)
        if add:
            img=0,img
            for action in actions:
                print(action,end=' ')
                start=time()
                img=negative(img[1]) if action=='negative' else contrast(img[1],float(action.split(':')[-1])) if 'contrast' in action else brightness(img[1],float(action.split(':')[-1])) if 'brightness' in action else color(img[1],float(action.split(':')[-1])) if 'color' in action else sharpness(img[1],float(action.split(':')[-1]))
                print(time()-start)
            piclist.append(img)
        else:
            copies=[]# removing this deepcopy part can show you a third mode: step-by-step of adding effects together
            for i in range(len(actions)):copies.append(deepcopy(img))
            for i,action in enumerate(actions):
                print(action,end=' ')
                start=time()
                try:
                    piclist.append(negative(copies[i]) if action=='negative' else contrast(copies[i],float(action.split(':')[-1])) if 'contrast' in action else brightness(copies[i],float(action.split(':')[-1])) if 'brightness' in action else color(copies[i],float(action.split(':')[-1])) if 'color' in action else sharpness(copies[i],float(action.split(':')[-1])))
                    if piclist[-1]==None:piclist.pop(-1)
                except ValueError:
                    print('\nCannot operate on picture '+path+pic.split('/')[-1]+' : Value Error.')
                    piclist.pop(-1)
                print(time()-start)
        if path and not exists(path):
            if input('\nOutput directory does not exists. Create?\n    (y/n): ').upper()=='Y':makedirs(path)
            else:raise FileNotFoundError('\nCannot output, task aborted.')
        if individualfolders:
            for action in actions:
                if (not ':' in action) and (not exists(path+action)):makedirs(path+action)
                elif not exists(path+action.split(':')[0]):makedirs(path+action.split(':')[0])
        if len(actions)==1:
            for picture in piclist:
                picture[1].save(path+pic.split('/')[-1])
                picture[1].close()
        elif individualfolders:
            for picture in piclist:
                picture[1].save(path+picture[0]+'/'+pic.split('/')[-1])
                picture[1].close()
        else:
            for picture in piclist:
                fullname=pic.split('/')[-1].split('.')[0]
                for i in pic.split('/')[-1].split('.')[1:-1]:fullname+=i
                picture[1].save(path+fullname+(' '+picture[0])*(not add)+'.'+pic.split('/')[-1].split('.')[-1])
                picture[1].close()
