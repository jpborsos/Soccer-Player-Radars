import csv
import json

squadData = {}

with open('squad_std.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    for line in data:
        squadData[line[0]] = {}
        squadData[line[0]]['Standard'] = {
        '# Pl': line[1],
        'Poss': line[2]
        }
        squadData[line[0]]['Standard']['Performance'] = {
        'Gls': line[6],
        'Ast': line[7],
        'PK': line[8],
        'PKatt': line[9],
        'CrdY': line[10],
        'CrdR': line[11]
        }
        squadData[line[0]]['Standard']['Per 90 Minutes'] = {
        'Gls': line[12],
        'Ast': line[13],
        'G+A': line[14],
        'G-PK': line[15],
        'G+A-PK': line[16]
        }
        squadData[line[0]]['Standard']['Expected'] = {
        'xG': line[17],
        'npxG': line[18],
        'xA': line[19]
        }
        squadData[line[0]]['Standard']['Expected Per 90 Minutes'] = {
        'xG': line[20],
        'xA': line[21],
        'xG+xA': line[22],
        'npxG': line[23],
        'npxG+xA': line[24]
        }

with open('squad_sht.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    for line in data:
        squadData[line[0]]['Shooting'] = {}
        squadData[line[0]]['Shooting']['Standard'] = {
        'Gls': line[2],
        'PK': line[3],
        'PKatt': line[4],
        'Sh': line[5],
        'SoT': line[6],
        'FK': line[7],
        'SoT%': line[8],
        'Sh/90': line[9],
        'SoT/90': line[10],
        'G/Sh': line[11],
        'G/SoT': line[12]
        }
        squadData[line[0]]['Shooting']['Expected'] = {
        'xG': line[13],
        'npxG': line[14],
        'npxG/Sh': line[15],
        'G-xG': line[16],
        'np:G-xG': line[17]
        }

with open('squad_posstn.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)
    for line in data:
        squadData[line[0]]['Possession'] = {
        'Poss': line[2],
        'Miscon': line[21],
        'Dispos': line[22]
        }
        squadData[line[0]]['Possession']['Touches'] = {
        'Touches': line[3],
        'Def Pen': line[4],
        'Def 3rd': line[5],
        'Mid 3rd': line[6],
        'Att 3rd': line[7],
        'Att Pen': line[8],
        'Live': line[9],
        }
        squadData[line[0]]['Possession']['Dribbles'] = {
        'succ': line[10],
        'att': line[11],
        'succ%': line[12],
        'numPlDribbledPast': line[13],
        'megs': line[14],
        }
        squadData[line[0]]['Possession']['Carries'] = {
        'Carries': line[15],
        'TotDist': line[16],
        'PrgDist': line[17],
        }
        squadData[line[0]]['Possession']['Receiving'] = {
        'Targ': line[18],
        'Rec': line[19],
        'Rec%': line[20],
        }

with open('squad_plytm.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)
    for line in data:
        squadData[line[0]]['Standard']['Subs'] = {
        'Subs': line[8],
        'Mn/Sub': line[9],
        'unSub': line[10]
        }
        squadData[line[0]]['Standard']['Team Success'] = {
        'PPM': line[11],
        'onG': line[12],
        'onGA': line[13],
        '+/-': line[14],
        '+/-90': line[15]
        }

with open('squad_passtype.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)
    for line in data:
        squadData[line[0]]['Passing'] = {
        'Att': line[2]
        }
        squadData[line[0]]['Passing']['Pass Types'] = {
        'Live': line[3],
        'Dead': line[4],
        'FK': line[5],
        'TB': line[6],
        'Press': line[7],
        'Sw': line[8],
        'Crs': line[9],
        'CK': line[10]
        }
        squadData[line[0]]['Passing']['Pass Types']['Corners'] = {
        'In': line[11],
        'Out': line[12],
        'Str': line[13]
        }
        squadData[line[0]]['Passing']['Pass Types']['Height'] = {
        'Ground': line[14],
        'Low': line[15],
        'High': line[16]
        }
        squadData[line[0]]['Passing']['Pass Types']['Body Parts'] = {
        'Left': line[17],
        'Right': line[18],
        'Head': line[19],
        'TI': line[20],
        'Other': line[21]
        }
        squadData[line[0]]['Passing']['Pass Types']['Outcomes'] = {
        'Cmp': line[22],
        'Off': line[23],
        'Out': line[24],
        'Int': line[25],
        'Blocks': line[26]
        }

with open('squad_pass.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)
    for line in data:
        squadData[line[0]]['Passing']['Total'] = {
        'Cmp': line[2],
        'Cmp%': line[4],
        'TotDist': line[5],
        'PrgDist': line[6]
        }
        squadData[line[0]]['Passing'].update({
        'Ast': line[16],
        'xA': line[17],
        'A-xA%': line[18],
        'KP': line[19],
        '1/3': line[20],
        'PPA': line[21],
        'CrsPA': line[22],
        'Prog': line[23]
        })
        squadData[line[0]]['Passing']['Short'] = {
        'Cmp': line[7],
        'Att': line[8],
        'Cmp%': line[9],
        }
        squadData[line[0]]['Passing']['Medium'] = {
        'Cmp': line[10],
        'Att': line[11],
        'Cmp%': line[12],
        }
        squadData[line[0]]['Passing']['Long'] = {
        'Cmp': line[13],
        'Att': line[14],
        'Cmp%': line[15],
        }

with open('squad_misc.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)
    for line in data:
        #print(line)
        squadData[line[0]]['Miscellaneous'] = {}
        squadData[line[0]]['Miscellaneous']['Performance'] = {
        'CrdY': line[2],
        'CrdR': line[3],
        '2CrdY': line[4],
        'Fls': line[5],
        'Fld': line[6],
        'Off': line[7],
        'Crs': line[8],
        'Int': line[9],
        'TklW': line[10],
        'PKwon': line[11],
        'PKcon': line[12],
        'OG': line[13],
        'Recov': line[14]
        }
        squadData[line[0]]['Miscellaneous']['Aerial Duels'] = {
        'Won': line[15],
        'Lost': line[16],
        'Won%': line[17],
        }

with open('squad_glshtcreation.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)

    for line in data:
        #print(line)
        squadData[line[0]]['Goal and Shot Creation'] = {}
        squadData[line[0]]['Goal and Shot Creation']['SCA'] = {
        'SCA': line[2],
        'SCA90': line[3],
        'PassLive': line[4],
        'PassDead': line[5],
        'Drib': line[6],
        'Sh': line[7],
        'Fld': line[8]
        }
        squadData[line[0]]['Goal and Shot Creation']['GCA'] = {
        'GCA': line[9],
        'GCA90': line[10],
        }
        squadData[line[0]]['Goal and Shot Creation']['GCA Types'] = {
        'PassLive': line[11],
        'PassDead': line[12],
        'Drib': line[13],
        'Sh': line[14],
        'Fld': line[15],
        'OG': line[16],
        }

with open('squad_df.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)

    for line in data:
        #print(line)
        squadData[line[0]]['Goal and Shot Creation'] = {}
        squadData[line[0]]['Goal and Shot Creation']['Tackles'] = {
        'Tkl': line[2],
        'TklW': line[3],
        'Def 3rd': line[4],
        'Mid 3rd': line[5],
        'Att 3rd': line[6],
        }
        squadData[line[0]]['Goal and Shot Creation']['Vs Dribbles'] = {
        'Tkl': line[7],
        'Att': line[8],
        'Tkl%': line[9],
        'Past': line[10],
        }
        squadData[line[0]]['Goal and Shot Creation']['Pressures'] = {
        'Press': line[11],
        'Succ': line[12],
        '%': line[13],
        'Def 3rd': line[14],
        'Mid 3rd': line[15],
        'Att 3rd': line[16],
        }
        squadData[line[0]]['Goal and Shot Creation']['Blocks'] = {
        'Blocks': line[17],
        'Sh': line[18],
        'ShSv': line[19],
        'Pass': line[20],
        }
        squadData[line[0]]['Goal and Shot Creation'].update({
            'Int': line[21],
            'Clr': line[22],
            'Err': line[23]
            })



'''
    next(data)
    i = 0
    for line in data:
        team = line[0]
        if i == 0:
            header = line
            i = 1
            continue

        squadData[team]['Goal and Shot Creation'] = {}

        for j in range(1,16):
            print(header[j])
            print(line[j])
            squadData[line[0]]['Goal and Shot Creation'].update({
            '{}'.format(header[j]): line[j]
            })
'''

        #squadData[line[0]][]
        #print(line)

#print(squadData)

playerData = {}

with open('player_advgk.csv') as csv_file:
    data = csv.reader(csv_file)
    next(data)
    next(data)

    playerData['Goalkeepers'] = {}
    for line in data:
        print(line[1])
        playerData['Goalkeepers'][line[1]] = {
        'Nation': line[2],
        'Squad': line[4],
        'Age': line[5],
        '90s': line[7],
        }
        playerData['Goalkeepers'][line[1]]['Goals'] = {
        'GA': line[8],
        'PKA': line[9],
        'FK': line[10],
        'CK': line[11],
        'OG': line[12],
        }
        playerData['Goalkeepers'][line[1]]['Expected'] = {
        'PSxG': line[13],
        'PSxG/SoT': line[14],
        'PSxG+/-': line[15],
        'PSxG+/- /90': line[16],
        }
        playerData['Goalkeepers'][line[1]]['Launched'] = {
        'Cmp': line[17],
        'Att': line[18],
        'Cmp%': line[19],
        }
        playerData['Goalkeepers'][line[1]]['Passes'] = {
        'Att': line[20],
        'Thr': line[21],
        'Launch%': line[22],
        'AvgLen': line[23],
        }

print(playerData)
