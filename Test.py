from cmath import nan
import pandas as pd
import glob
import os

def M4_CSVUpdater(x1,x2,x3):
    inpath = x1
    winpath = x2
    finalpath = x3
    allFiles = glob.glob(inpath + "/*.csv")
    polefiles,wirefiles,guyfiles = 0,0,0
    noCSV = []

    for file in allFiles:
        newName = os.path.basename(file)
        newpath = f"{finalpath}/New_{newName}"
        
        if 'pole' in file.lower():
            poledata = pd.read_csv(file,index_col=False)
            poledata = poledata.sort_values(by='pole_name',
                ascending=False).drop_duplicates(subset=['x', 'y'],
                keep='first').replace({'pole_lengt': {0: 40},'pole_class':{nan: 5}})
            poledata.to_csv(newpath,index=False,header=False)
            polefiles = polefiles + 1

        elif 'wire' in file.lower():
            wiredata = pd.read_csv(file)
            wiredata = wiredata.replace(['REPLACE_ME.wir'],'periwinkle_poly_triplex_l.wir')
            wiredata['cable_file'] = winpath + '\\' + wiredata['cable_file']
            wiredata.to_csv(newpath,index=False,header=False)
            wirefiles = wirefiles + 1
        
        elif 'guy' in file.lower():
            guydata = pd.read_csv(file)
            guydata.to_csv(newpath,index=False,header=False)
            guyfiles = guyfiles + 1
        else:
            noCSV.append(newName)

    print(f'Pole Files Generated: {polefiles}')
    print(f'Wire Files Generated: {wirefiles}')
    print(f'Guye Files Generated: {guyfiles}')
    print(f'Files saved to {finalpath}')
    print('Files that did not get generated')
    for row in noCSV:
         print(row)

M4_CSVUpdater(input('csv file path: '),input('wire file path: '),input('to be saved path: '))
