#!/usr/bin/env python
# coding: utf-8

# 第一部分：程序说明###################################################################################
# coding=utf-8
# 药械不良事件工作平台
# 开发人：蔡权周

import tkinter as Tk #line:11
import os #line:12
import traceback #line:13
import ast #line:14
import re #line:15
import xlrd #line:16
import xlwt #line:17
import openpyxl #line:18
import pandas as pd #line:19
import numpy as np #line:20
import math #line:21
from tkinter import ttk ,Menu ,Frame ,Canvas ,StringVar ,LEFT ,RIGHT ,TOP ,BOTTOM ,BOTH ,Y ,X ,YES ,NO ,DISABLED ,END ,Button ,LabelFrame ,GROOVE ,Toplevel ,Label ,Entry ,Scrollbar ,Text ,filedialog ,dialog ,PhotoImage #line:23
import tkinter .font as tkFont #line:24
from tkinter .messagebox import showinfo #line:25
from tkinter .scrolledtext import ScrolledText #line:26
import matplotlib as plt #line:27
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:28
from matplotlib .figure import Figure #line:29
from matplotlib .backends .backend_tkagg import NavigationToolbar2Tk #line:30
import collections #line:31
from collections import Counter #line:32
import datetime #line:33
from datetime import datetime ,timedelta #line:34
import xlsxwriter #line:35
import time #line:36
import threading #line:37
import warnings #line:38
from matplotlib .ticker import PercentFormatter #line:39
import sqlite3 #line:40
from sqlalchemy import create_engine #line:41
from sqlalchemy import text as sqltext #line:42
import webbrowser #line:44
title_all ="药械妆不良反应报表统计分析工作站 2023-10-11 "#line:46
title_all2 ="药械妆不良反应报表统计分析工作站"#line:47
global ori #line:48
ori =0 #line:49
global auto_guize #line:50
global biaozhun #line:53
global dishi #line:54
biaozhun =""#line:55
dishi =""#line:56
global ini #line:60
ini ={}#line:61
ini ["四个品种"]=1 #line:62
import random #line:65
import requests #line:66
global version_now #line:67
global usergroup #line:68
global setting_cfg #line:69
global csdir #line:70
global peizhidir #line:71
version_now ="0.0.2"#line:72
usergroup ="用户组=0"#line:73
setting_cfg =""#line:74
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:75
if csdir =="":#line:76
    csdir =str (os .path .dirname (__file__ ))#line:77
    csdir =csdir +csdir .split ("adrmdr")[0 ][-1 ]#line:78
def extract_zip_file (OO0000OO00000O0OO ,O0OOO00OOO000O0O0 ):#line:86
    import zipfile #line:88
    if O0OOO00OOO000O0O0 =="":#line:89
        return 0 #line:90
    with zipfile .ZipFile (OO0000OO00000O0OO ,'r')as O0OOO0OOOO00OO0O0 :#line:91
        for O0OO0O0OO00OO0000 in O0OOO0OOOO00OO0O0 .infolist ():#line:92
            O0OO0O0OO00OO0000 .filename =O0OO0O0OO00OO0000 .filename .encode ('cp437').decode ('gbk')#line:94
            O0OOO0OOOO00OO0O0 .extract (O0OO0O0OO00OO0000 ,O0OOO00OOO000O0O0 )#line:95
def get_directory_path (O0OO00O000000O000 ):#line:101
    global csdir #line:103
    if not (os .path .isfile (os .path .join (O0OO00O000000O000 ,'0（范例）比例失衡关键字库.xls'))):#line:105
        extract_zip_file (csdir +"def.py",O0OO00O000000O000 )#line:110
    if O0OO00O000000O000 =="":#line:112
        quit ()#line:113
    return O0OO00O000000O000 #line:114
def convert_and_compare_dates (OO00OO0O0O0OO0000 ):#line:118
    import datetime #line:119
    O0OO00OO00OO00O0O =datetime .datetime .now ()#line:120
    try :#line:122
       O0OOOOO0000OO0O0O =datetime .datetime .strptime (str (int (int (OO00OO0O0O0OO0000 )/4 )),"%Y%m%d")#line:123
    except :#line:124
        print ("fail")#line:125
        return "已过期"#line:126
    if O0OOOOO0000OO0O0O >O0OO00OO00OO00O0O :#line:128
        return "未过期"#line:130
    else :#line:131
        return "已过期"#line:132
def read_setting_cfg ():#line:134
    global csdir #line:135
    if os .path .exists (csdir +'setting.cfg'):#line:137
        text .insert (END ,"已完成初始化\n")#line:138
        with open (csdir +'setting.cfg','r')as OOO00O0OO0O0O0O0O :#line:139
            O0O0000OO000OO00O =eval (OOO00O0OO0O0O0O0O .read ())#line:140
    else :#line:141
        O000O0O00OOO000OO =csdir +'setting.cfg'#line:143
        with open (O000O0O00OOO000OO ,'w')as OOO00O0OO0O0O0O0O :#line:144
            OOO00O0OO0O0O0O0O .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:145
        text .insert (END ,"未初始化，正在初始化...\n")#line:146
        O0O0000OO000OO00O =read_setting_cfg ()#line:147
    return O0O0000OO000OO00O #line:148
def open_setting_cfg ():#line:151
    global csdir #line:152
    with open (csdir +"setting.cfg","r")as O0OOOO00OOOOOO0O0 :#line:154
        O00O0O000O00O0OOO =eval (O0OOOO00OOOOOO0O0 .read ())#line:156
    return O00O0O000O00O0OOO #line:157
def update_setting_cfg (O00O0000OO0OO0OO0 ,OO00OO000000OOO00 ):#line:159
    global csdir #line:160
    with open (csdir +"setting.cfg","r")as O00O0OO0O0OO0OO0O :#line:162
        OO00O00O0O0OOOOOO =eval (O00O0OO0O0OO0OO0O .read ())#line:164
    if OO00O00O0O0OOOOOO [O00O0000OO0OO0OO0 ]==0 or OO00O00O0O0OOOOOO [O00O0000OO0OO0OO0 ]=="11111180000808":#line:166
        OO00O00O0O0OOOOOO [O00O0000OO0OO0OO0 ]=OO00OO000000OOO00 #line:167
        with open (csdir +"setting.cfg","w")as O00O0OO0O0OO0OO0O :#line:169
            O00O0OO0O0OO0OO0O .write (str (OO00O00O0O0OOOOOO ))#line:170
def generate_random_file ():#line:173
    OOOOO0O0OO0OOOO0O =random .randint (200000 ,299999 )#line:175
    update_setting_cfg ("sidori",OOOOO0O0OO0OOOO0O )#line:177
def display_random_number ():#line:179
    global csdir #line:180
    O0OOO0O0OOO0OOO0O =Toplevel ()#line:181
    O0OOO0O0OOO0OOO0O .title ("ID")#line:182
    O00O0O0O0O0OO0OO0 =O0OOO0O0OOO0OOO0O .winfo_screenwidth ()#line:184
    O000O00O000O00OO0 =O0OOO0O0OOO0OOO0O .winfo_screenheight ()#line:185
    O0OOO000O0O0OOO0O =80 #line:187
    O00000000OO00000O =70 #line:188
    OO0O0OOO0O00OO00O =(O00O0O0O0O0OO0OO0 -O0OOO000O0O0OOO0O )/2 #line:190
    O0OOOOOO00OO0OO00 =(O000O00O000O00OO0 -O00000000OO00000O )/2 #line:191
    O0OOO0O0OOO0OOO0O .geometry ("%dx%d+%d+%d"%(O0OOO000O0O0OOO0O ,O00000000OO00000O ,OO0O0OOO0O00OO00O ,O0OOOOOO00OO0OO00 ))#line:192
    with open (csdir +"setting.cfg","r")as OOO00OO0O0OO00OOO :#line:195
        OO00OO0OO0OO0OOOO =eval (OOO00OO0O0OO00OOO .read ())#line:197
    OOOOO0OOO0O0O0OOO =int (OO00OO0OO0OO0OOOO ["sidori"])#line:198
    OO000OO0O0000O00O =OOOOO0OOO0O0O0OOO *2 +183576 #line:199
    print (OO000OO0O0000O00O )#line:201
    O00O000OO0O0OOO0O =ttk .Label (O0OOO0O0OOO0OOO0O ,text =f"机器码: {OOOOO0OOO0O0O0OOO}")#line:203
    O00O00O00000OOO00 =ttk .Entry (O0OOO0O0OOO0OOO0O )#line:204
    O00O000OO0O0OOO0O .pack ()#line:207
    O00O00O00000OOO00 .pack ()#line:208
    ttk .Button (O0OOO0O0OOO0OOO0O ,text ="验证",command =lambda :check_input (O00O00O00000OOO00 .get (),OO000OO0O0000O00O )).pack ()#line:212
def check_input (O0O000O0000OOOO0O ,OOO00OOO0O000000O ):#line:214
    try :#line:218
        OO0O0000OOOO0O00O =int (str (O0O000O0000OOOO0O )[0 :6 ])#line:219
        O00000000O0O000O0 =convert_and_compare_dates (str (O0O000O0000OOOO0O )[6 :14 ])#line:220
    except :#line:221
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:222
        return 0 #line:223
    if OO0O0000OOOO0O00O ==OOO00OOO0O000000O and O00000000O0O000O0 =="未过期":#line:225
        update_setting_cfg ("sidfinal",O0O000O0000OOOO0O )#line:226
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:227
        quit ()#line:228
    else :#line:229
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:230
def update_software (O0O0O00O00OO0OOOO ):#line:235
    global version_now #line:237
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:238
    try :#line:239
        OO0OOO0O0OO00OO00 =requests .get (f"https://pypi.org/pypi/{O0O0O00O00OO0OOOO}/json",timeout =2 ).json ()["info"]["version"]#line:240
    except :#line:241
        return "...更新失败。"#line:242
    if OO0OOO0O0OO00OO00 >version_now :#line:243
        text .insert (END ,"\n最新版本为："+OO0OOO0O0OO00OO00 +",正在尝试自动更新....")#line:244
        pip .main (['install',O0O0O00O00OO0OOOO ,'--upgrade'])#line:246
        text .insert (END ,"\n您可以开展工作。")#line:247
        return "...更新成功。"#line:248
def TOOLS_ror_mode1 (O00O00O0O0O000O0O ,O0OOO0O00000OOOOO ):#line:265
	O0O0OO0000O0000O0 =[]#line:266
	for OO0OOOO00OO000OO0 in ("事件发生年份","性别","年龄段","报告类型-严重程度","停药减药后反应是否减轻或消失","再次使用可疑药是否出现同样反应","对原患疾病影响","不良反应结果","关联性评价"):#line:267
		O00O00O0O0O000O0O [OO0OOOO00OO000OO0 ]=O00O00O0O0O000O0O [OO0OOOO00OO000OO0 ].astype (str )#line:268
		O00O00O0O0O000O0O [OO0OOOO00OO000OO0 ]=O00O00O0O0O000O0O [OO0OOOO00OO000OO0 ].fillna ("不详")#line:269
		O0O00O00000OO00O0 =0 #line:271
		for OO00O000O000O0O0O in O00O00O0O0O000O0O [O0OOO0O00000OOOOO ].drop_duplicates ():#line:272
			O0O00O00000OO00O0 =O0O00O00000OO00O0 +1 #line:273
			OO0O00000000OOOO0 =O00O00O0O0O000O0O [(O00O00O0O0O000O0O [O0OOO0O00000OOOOO ]==OO00O000O000O0O0O )].copy ()#line:274
			OO0000OOO000OO0OO =str (OO00O000O000O0O0O )+"计数"#line:276
			OOOOO0OO0O000OOO0 =str (OO00O000O000O0O0O )+"构成比(%)"#line:277
			OOOOO000O0O0OOOOO =OO0O00000000OOOO0 .groupby (OO0OOOO00OO000OO0 ).agg (计数 =("报告编码","nunique")).sort_values (by =OO0OOOO00OO000OO0 ,ascending =[True ],na_position ="last").reset_index ()#line:278
			OOOOO000O0O0OOOOO [OOOOO0OO0O000OOO0 ]=round (100 *OOOOO000O0O0OOOOO ["计数"]/OOOOO000O0O0OOOOO ["计数"].sum (),2 )#line:279
			OOOOO000O0O0OOOOO =OOOOO000O0O0OOOOO .rename (columns ={OO0OOOO00OO000OO0 :"项目"})#line:280
			OOOOO000O0O0OOOOO =OOOOO000O0O0OOOOO .rename (columns ={"计数":OO0000OOO000OO0OO })#line:281
			if O0O00O00000OO00O0 >1 :#line:282
				O0O0OO00OO0OOOOO0 =pd .merge (O0O0OO00OO0OOOOO0 ,OOOOO000O0O0OOOOO ,on =["项目"],how ="outer")#line:283
			else :#line:284
				O0O0OO00OO0OOOOO0 =OOOOO000O0O0OOOOO .copy ()#line:285
		O0O0OO00OO0OOOOO0 ["类别"]=OO0OOOO00OO000OO0 #line:287
		O0O0OO0000O0000O0 .append (O0O0OO00OO0OOOOO0 .copy ().reset_index (drop =True ))#line:288
	OOOO00O00O000O00O =pd .concat (O0O0OO0000O0000O0 ,ignore_index =True ).fillna (0 )#line:291
	OOOO00O00O000O00O ["报表类型"]="KETI"#line:292
	TABLE_tree_Level_2 (OOOO00O00O000O00O ,1 ,OOOO00O00O000O00O )#line:293
def TOOLS_ror_mode2 (O0O0OO0O000O0O00O ,O0OO0O0OOO0OO00O0 ):#line:295
	O00000OOOOOO00000 =Countall (O0O0OO0O000O0O00O ).df_ror (["产品类别","产品名称"]).reset_index ()#line:296
	O00000OOOOOO00000 ["四分表"]=O00000OOOOOO00000 ["四分表"].str .replace ("(","")#line:297
	O00000OOOOOO00000 ["四分表"]=O00000OOOOOO00000 ["四分表"].str .replace (")","")#line:298
	O00000OOOOOO00000 ["ROR信号（0-否，1-是）"]=0 #line:299
	O00000OOOOOO00000 ["PRR信号（0-否，1-是）"]=0 #line:300
	for O00OOO0O00OOO0O0O ,OO0O0O000000OOOO0 in O00000OOOOOO00000 .iterrows ():#line:301
		OOOO0O00O00OOOOO0 =tuple (OO0O0O000000OOOO0 ["四分表"].split (","))#line:302
		O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"a"]=int (OOOO0O00O00OOOOO0 [0 ])#line:303
		O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"b"]=int (OOOO0O00O00OOOOO0 [1 ])#line:304
		O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"c"]=int (OOOO0O00O00OOOOO0 [2 ])#line:305
		O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"d"]=int (OOOO0O00O00OOOOO0 [3 ])#line:306
		if int (OOOO0O00O00OOOOO0 [1 ])*int (OOOO0O00O00OOOOO0 [2 ])*int (OOOO0O00O00OOOOO0 [3 ])*int (OOOO0O00O00OOOOO0 [0 ])==0 :#line:307
			O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"分母核验"]=1 #line:308
		if OO0O0O000000OOOO0 ['ROR值的95%CI下限']>1 and OO0O0O000000OOOO0 ['出现频次']>=3 :#line:309
			O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"ROR信号（0-否，1-是）"]=1 #line:310
		if OO0O0O000000OOOO0 ['PRR值的95%CI下限']>1 and OO0O0O000000OOOO0 ['出现频次']>=3 :#line:311
			O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"PRR信号（0-否，1-是）"]=1 #line:312
		O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"事件分类"]=str (TOOLS_get_list (O00000OOOOOO00000 .loc [O00OOO0O00OOO0O0O ,"特定关键字"])[0 ])#line:313
	O00000OOOOOO00000 =pd .pivot_table (O00000OOOOOO00000 ,values =["出现频次",'ROR值',"ROR值的95%CI下限","ROR信号（0-否，1-是）",'PRR值',"PRR值的95%CI下限","PRR信号（0-否，1-是）","a","b","c","d","分母核验","风险评分"],index ='事件分类',columns ="产品名称",aggfunc ='sum').reset_index ().fillna (0 )#line:315
	try :#line:318
		O0OOOO0O0O000OOO0 =peizhidir +"0（范例）比例失衡关键字库.xls"#line:319
		if "报告类型-新的"in O0O0OO0O000O0O00O .columns :#line:320
			OO0O00O00O0OO0O0O ="药品"#line:321
		else :#line:322
			OO0O00O00O0OO0O0O ="器械"#line:323
		OO00OO0O0OO000OO0 =pd .read_excel (O0OOOO0O0O000OOO0 ,header =0 ,sheet_name =OO0O00O00O0OO0O0O ).reset_index (drop =True )#line:324
	except :#line:325
		pass #line:326
	for O00OOO0O00OOO0O0O ,OO0O0O000000OOOO0 in OO00OO0O0OO000OO0 .iterrows ():#line:328
		O00000OOOOOO00000 .loc [O00000OOOOOO00000 ["事件分类"].str .contains (OO0O0O000000OOOO0 ["值"],na =False ),"器官系统损害"]=TOOLS_get_list (OO0O0O000000OOOO0 ["值"])[0 ]#line:329
	try :#line:332
		OO000OO0000000O00 =peizhidir +""+"0（范例）标准术语"+".xlsx"#line:333
		try :#line:334
			OOOO00OO00OO0OOOO =pd .read_excel (OO000OO0000000O00 ,sheet_name ="onept",header =0 ,index_col =0 ).reset_index ()#line:335
		except :#line:336
			showinfo (title ="错误信息",message ="标准术语集无法加载。")#line:337
		try :#line:339
			O00OO0000O000OOOO =pd .read_excel (OO000OO0000000O00 ,sheet_name ="my",header =0 ,index_col =0 ).reset_index ()#line:340
		except :#line:341
			showinfo (title ="错误信息",message ="自定义术语集无法加载。")#line:342
		OOOO00OO00OO0OOOO =pd .concat ([O00OO0000O000OOOO ,OOOO00OO00OO0OOOO ],ignore_index =True ).drop_duplicates ("code")#line:344
		OOOO00OO00OO0OOOO ["code"]=OOOO00OO00OO0OOOO ["code"].astype (str )#line:345
		O00000OOOOOO00000 ["事件分类"]=O00000OOOOOO00000 ["事件分类"].astype (str )#line:346
		OOOO00OO00OO0OOOO ["事件分类"]=OOOO00OO00OO0OOOO ["PT"]#line:347
		OOO0OO00000OOOO00 =pd .merge (O00000OOOOOO00000 ,OOOO00OO00OO0OOOO ,on =["事件分类"],how ="left")#line:348
		for O00OOO0O00OOO0O0O ,OO0O0O000000OOOO0 in OOO0OO00000OOOO00 .iterrows ():#line:349
			O00000OOOOOO00000 .loc [O00000OOOOOO00000 ["事件分类"]==OO0O0O000000OOOO0 ["事件分类"],"Chinese"]=OO0O0O000000OOOO0 ["Chinese"]#line:350
			O00000OOOOOO00000 .loc [O00000OOOOOO00000 ["事件分类"]==OO0O0O000000OOOO0 ["事件分类"],"PT"]=OO0O0O000000OOOO0 ["PT"]#line:351
			O00000OOOOOO00000 .loc [O00000OOOOOO00000 ["事件分类"]==OO0O0O000000OOOO0 ["事件分类"],"HLT"]=OO0O0O000000OOOO0 ["HLT"]#line:352
			O00000OOOOOO00000 .loc [O00000OOOOOO00000 ["事件分类"]==OO0O0O000000OOOO0 ["事件分类"],"HLGT"]=OO0O0O000000OOOO0 ["HLGT"]#line:353
			O00000OOOOOO00000 .loc [O00000OOOOOO00000 ["事件分类"]==OO0O0O000000OOOO0 ["事件分类"],"SOC"]=OO0O0O000000OOOO0 ["SOC"]#line:354
	except :#line:355
		pass #line:356
	data ["报表类型"]="KETI"#line:359
	TABLE_tree_Level_2 (O00000OOOOOO00000 ,1 ,O00000OOOOOO00000 )#line:360
def TOOLS_ror_mode3 (OO00O00OOOO000OO0 ,OOO0O0O0OOO0000O0 ):#line:362
	OO00O00OOOO000OO0 ["css"]=0 #line:363
	TOOLS_ror_mode2 (OO00O00OOOO000OO0 ,OOO0O0O0OOO0000O0 )#line:364
def STAT_pinzhong (O0OO00O0OOO0000O0 ,O00OOO0O0OO000OO0 ,O0O00O0OO00000O00 ):#line:366
	OOOOO0O0OO00OOO0O =[O00OOO0O0OO000OO0 ]#line:368
	if O0O00O0OO00000O00 ==-1 :#line:369
		O0OO00OOO0OO00OOO =O0OO00O0OOO0000O0 .drop_duplicates ("报告编码").copy ()#line:370
		OOOOOOO00O0000000 =O0OO00OOO0OO00OOO .groupby ([O00OOO0O0OO000OO0 ]).agg (计数 =("报告编码","nunique")).sort_values (by =O00OOO0O0OO000OO0 ,ascending =[True ],na_position ="last").reset_index ()#line:371
		OOOOOOO00O0000000 ["构成比(%)"]=round (100 *OOOOOOO00O0000000 ["计数"]/OOOOOOO00O0000000 ["计数"].sum (),2 )#line:372
		OOOOOOO00O0000000 [O00OOO0O0OO000OO0 ]=OOOOOOO00O0000000 [O00OOO0O0OO000OO0 ].astype (str )#line:373
		OOOOOOO00O0000000 ["报表类型"]="dfx_deepview"+"_"+str (OOOOO0O0OO00OOO0O )#line:374
		TABLE_tree_Level_2 (OOOOOOO00O0000000 ,1 ,O0OO00OOO0OO00OOO )#line:375
	if O0O00O0OO00000O00 ==1 :#line:377
		O0OO00OOO0OO00OOO =O0OO00O0OOO0000O0 .copy ()#line:378
		OOOOOOO00O0000000 =O0OO00OOO0OO00OOO .groupby ([O00OOO0O0OO000OO0 ]).agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:379
		OOOOOOO00O0000000 ["构成比(%)"]=round (100 *OOOOOOO00O0000000 ["计数"]/OOOOOOO00O0000000 ["计数"].sum (),2 )#line:380
		OOOOOOO00O0000000 ["报表类型"]="dfx_deepview"+"_"+str (OOOOO0O0OO00OOO0O )#line:381
		TABLE_tree_Level_2 (OOOOOOO00O0000000 ,1 ,O0OO00OOO0OO00OOO )#line:382
	if O0O00O0OO00000O00 ==4 :#line:384
		O0OO00OOO0OO00OOO =O0OO00O0OOO0000O0 .copy ()#line:385
		O0OO00OOO0OO00OOO .loc [O0OO00OOO0OO00OOO ["不良反应结果"].str .contains ("好转",na =False ),"不良反应结果2"]="好转"#line:386
		O0OO00OOO0OO00OOO .loc [O0OO00OOO0OO00OOO ["不良反应结果"].str .contains ("痊愈",na =False ),"不良反应结果2"]="痊愈"#line:387
		O0OO00OOO0OO00OOO .loc [O0OO00OOO0OO00OOO ["不良反应结果"].str .contains ("无进展",na =False ),"不良反应结果2"]="无进展"#line:388
		O0OO00OOO0OO00OOO .loc [O0OO00OOO0OO00OOO ["不良反应结果"].str .contains ("死亡",na =False ),"不良反应结果2"]="死亡"#line:389
		O0OO00OOO0OO00OOO .loc [O0OO00OOO0OO00OOO ["不良反应结果"].str .contains ("不详",na =False ),"不良反应结果2"]="不详"#line:390
		O0OO00OOO0OO00OOO .loc [O0OO00OOO0OO00OOO ["不良反应结果"].str .contains ("未好转",na =False ),"不良反应结果2"]="未好转"#line:391
		OOOOOOO00O0000000 =O0OO00OOO0OO00OOO .groupby (["不良反应结果2"]).agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:392
		OOOOOOO00O0000000 ["构成比(%)"]=round (100 *OOOOOOO00O0000000 ["计数"]/OOOOOOO00O0000000 ["计数"].sum (),2 )#line:393
		OOOOOOO00O0000000 ["报表类型"]="dfx_deepview"+"_"+str (["不良反应结果2"])#line:394
		TABLE_tree_Level_2 (OOOOOOO00O0000000 ,1 ,O0OO00OOO0OO00OOO )#line:395
	if O0O00O0OO00000O00 ==5 :#line:397
		O0OO00OOO0OO00OOO =O0OO00O0OOO0000O0 .copy ()#line:398
		O0OO00OOO0OO00OOO ["关联性评价汇总"]="("+O0OO00OOO0OO00OOO ["评价状态"].astype (str )+"("+O0OO00OOO0OO00OOO ["县评价"].astype (str )+"("+O0OO00OOO0OO00OOO ["市评价"].astype (str )+"("+O0OO00OOO0OO00OOO ["省评价"].astype (str )+"("+O0OO00OOO0OO00OOO ["国家评价"].astype (str )+")"#line:400
		O0OO00OOO0OO00OOO ["关联性评价汇总"]=O0OO00OOO0OO00OOO ["关联性评价汇总"].str .replace ("(nan","",regex =False )#line:401
		O0OO00OOO0OO00OOO ["关联性评价汇总"]=O0OO00OOO0OO00OOO ["关联性评价汇总"].str .replace ("nan)","",regex =False )#line:402
		O0OO00OOO0OO00OOO ["关联性评价汇总"]=O0OO00OOO0OO00OOO ["关联性评价汇总"].str .replace ("nan","",regex =False )#line:403
		O0OO00OOO0OO00OOO ['最终的关联性评价']=O0OO00OOO0OO00OOO ["关联性评价汇总"].str .extract ('.*\((.*)\).*',expand =False )#line:404
		OOOOOOO00O0000000 =O0OO00OOO0OO00OOO .groupby ('最终的关联性评价').agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:405
		OOOOOOO00O0000000 ["构成比(%)"]=round (100 *OOOOOOO00O0000000 ["计数"]/OOOOOOO00O0000000 ["计数"].sum (),2 )#line:406
		OOOOOOO00O0000000 ["报表类型"]="dfx_deepview"+"_"+str (['最终的关联性评价'])#line:407
		TABLE_tree_Level_2 (OOOOOOO00O0000000 ,1 ,O0OO00OOO0OO00OOO )#line:408
	if O0O00O0OO00000O00 ==0 :#line:410
		O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ]=O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ].fillna ("未填写")#line:411
		O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ]=O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ].str .replace ("*","",regex =False )#line:412
		OOO0OO0000O0OO00O ="use("+str (O00OOO0O0OO000OO0 )+").file"#line:413
		OOOO00000OO0O0O00 =str (Counter (TOOLS_get_list0 (OOO0OO0000O0OO00O ,O0OO00O0OOO0000O0 ,1000 ))).replace ("Counter({","{")#line:414
		OOOO00000OO0O0O00 =OOOO00000OO0O0O00 .replace ("})","}")#line:415
		OOOO00000OO0O0O00 =ast .literal_eval (OOOO00000OO0O0O00 )#line:416
		OOOOOOO00O0000000 =pd .DataFrame .from_dict (OOOO00000OO0O0O00 ,orient ="index",columns =["计数"]).reset_index ()#line:417
		OOOOOOO00O0000000 ["构成比(%)"]=round (100 *OOOOOOO00O0000000 ["计数"]/OOOOOOO00O0000000 ["计数"].sum (),2 )#line:419
		OOOOOOO00O0000000 ["报表类型"]="dfx_deepvie2"+"_"+str (OOOOO0O0OO00OOO0O )#line:420
		TABLE_tree_Level_2 (OOOOOOO00O0000000 ,1 ,O0OO00O0OOO0000O0 )#line:421
	if O0O00O0OO00000O00 ==2 or O0O00O0OO00000O00 ==3 :#line:425
		O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ]=O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ].astype (str )#line:426
		O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ]=O0OO00O0OOO0000O0 [O00OOO0O0OO000OO0 ].fillna ("未填写")#line:427
		OOO0OO0000O0OO00O ="use("+str (O00OOO0O0OO000OO0 )+").file"#line:429
		OOOO00000OO0O0O00 =str (Counter (TOOLS_get_list0 (OOO0OO0000O0OO00O ,O0OO00O0OOO0000O0 ,1000 ))).replace ("Counter({","{")#line:430
		OOOO00000OO0O0O00 =OOOO00000OO0O0O00 .replace ("})","}")#line:431
		OOOO00000OO0O0O00 =ast .literal_eval (OOOO00000OO0O0O00 )#line:432
		OOOOOOO00O0000000 =pd .DataFrame .from_dict (OOOO00000OO0O0O00 ,orient ="index",columns =["计数"]).reset_index ()#line:433
		print ("正在统计，请稍后...")#line:434
		O0000OO0OO0000O00 =peizhidir +""+"0（范例）标准术语"+".xlsx"#line:435
		try :#line:436
			O0OO0OOOO000O0000 =pd .read_excel (O0000OO0OO0000O00 ,sheet_name ="simple",header =0 ,index_col =0 ).reset_index ()#line:437
		except :#line:438
			showinfo (title ="错误信息",message ="标准术语集无法加载。")#line:439
			return 0 #line:440
		try :#line:441
			OO0OO00OO000OOO00 =pd .read_excel (O0000OO0OO0000O00 ,sheet_name ="my",header =0 ,index_col =0 ).reset_index ()#line:442
		except :#line:443
			showinfo (title ="错误信息",message ="自定义术语集无法加载。")#line:444
			return 0 #line:445
		O0OO0OOOO000O0000 =pd .concat ([OO0OO00OO000OOO00 ,O0OO0OOOO000O0000 ],ignore_index =True ).drop_duplicates ("code")#line:446
		O0OO0OOOO000O0000 ["code"]=O0OO0OOOO000O0000 ["code"].astype (str )#line:447
		OOOOOOO00O0000000 ["index"]=OOOOOOO00O0000000 ["index"].astype (str )#line:448
		OOOOOOO00O0000000 =OOOOOOO00O0000000 .rename (columns ={"index":"code"})#line:450
		OOOOOOO00O0000000 =pd .merge (OOOOOOO00O0000000 ,O0OO0OOOO000O0000 ,on =["code"],how ="left")#line:451
		OOOOOOO00O0000000 ["code构成比(%)"]=round (100 *OOOOOOO00O0000000 ["计数"]/OOOOOOO00O0000000 ["计数"].sum (),2 )#line:452
		O0OOO000000OO00O0 =OOOOOOO00O0000000 .groupby ("SOC").agg (SOC计数 =("计数","sum")).sort_values (by ="SOC计数",ascending =[False ],na_position ="last").reset_index ()#line:453
		O0OOO000000OO00O0 ["soc构成比(%)"]=round (100 *O0OOO000000OO00O0 ["SOC计数"]/O0OOO000000OO00O0 ["SOC计数"].sum (),2 )#line:454
		O0OOO000000OO00O0 ["SOC计数"]=O0OOO000000OO00O0 ["SOC计数"].astype (int )#line:455
		OOOOOOO00O0000000 =pd .merge (OOOOOOO00O0000000 ,O0OOO000000OO00O0 ,on =["SOC"],how ="left")#line:456
		if O0O00O0OO00000O00 ==3 :#line:458
			O0OOO000000OO00O0 ["具体名称"]=""#line:459
			for OOOO00000O0O00O0O ,O00000OOO0O0O0O00 in O0OOO000000OO00O0 .iterrows ():#line:460
				O0OOOO0O00000OO00 =""#line:461
				OOOO0O00OOOOO0O0O =OOOOOOO00O0000000 .loc [OOOOOOO00O0000000 ["SOC"].str .contains (O00000OOO0O0O0O00 ["SOC"],na =False )].copy ()#line:462
				for O0O00O0O000000O0O ,OO00OO0OOOOO00OOO in OOOO0O00OOOOO0O0O .iterrows ():#line:463
					O0OOOO0O00000OO00 =O0OOOO0O00000OO00 +str (OO00OO0OOOOO00OOO ["PT"])+"("+str (OO00OO0OOOOO00OOO ["计数"])+")、"#line:464
				O0OOO000000OO00O0 .loc [OOOO00000O0O00O0O ,"具体名称"]=O0OOOO0O00000OO00 #line:465
			O0OOO000000OO00O0 ["报表类型"]="dfx_deepvie2"+"_"+str (["SOC"])#line:466
			TABLE_tree_Level_2 (O0OOO000000OO00O0 ,1 ,OOOOOOO00O0000000 )#line:467
		if O0O00O0OO00000O00 ==2 :#line:469
			OOOOOOO00O0000000 ["报表类型"]="dfx_deepvie2"+"_"+str (OOOOO0O0OO00OOO0O )#line:470
			TABLE_tree_Level_2 (OOOOOOO00O0000000 ,1 ,O0OO00O0OOO0000O0 )#line:471
	pass #line:474
def DRAW_pre (OO000O0OOOOO0OOO0 ):#line:476
	""#line:477
	OOOOOO0000OO0O00O =list (OO000O0OOOOO0OOO0 ["报表类型"])[0 ].replace ("1","")#line:485
	if "dfx_org监测机构"in OOOOOO0000OO0O00O :#line:487
		OO000O0OOOOO0OOO0 =OO000O0OOOOO0OOO0 [:-1 ]#line:488
		DRAW_make_one (OO000O0OOOOO0OOO0 ,"报告图","监测机构","报告数量","超级托帕斯图(严重伤害数)")#line:489
	elif "dfx_org市级监测机构"in OOOOOO0000OO0O00O :#line:490
		OO000O0OOOOO0OOO0 =OO000O0OOOOO0OOO0 [:-1 ]#line:491
		DRAW_make_one (OO000O0OOOOO0OOO0 ,"报告图","市级监测机构","报告数量","超级托帕斯图(严重伤害数)")#line:492
	elif "dfx_user"in OOOOOO0000OO0O00O :#line:493
		OO000O0OOOOO0OOO0 =OO000O0OOOOO0OOO0 [:-1 ]#line:494
		DRAW_make_one (OO000O0OOOOO0OOO0 ,"报告单位图","单位名称","报告数量","超级托帕斯图(严重伤害数)")#line:495
	elif "dfx_deepview"in OOOOOO0000OO0O00O :#line:498
		DRAW_make_one (OO000O0OOOOO0OOO0 ,"柱状图",OO000O0OOOOO0OOO0 .columns [0 ],"计数","柱状图")#line:499
	elif "dfx_chiyouren"in OOOOOO0000OO0O00O :#line:501
		OO000O0OOOOO0OOO0 =OO000O0OOOOO0OOO0 [:-1 ]#line:502
		DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及持有人图","上市许可持有人名称","总报告数","超级托帕斯图(总待评价数量)")#line:503
	elif "dfx_zhenghao"in OOOOOO0000OO0O00O :#line:505
		OO000O0OOOOO0OOO0 ["产品"]=OO000O0OOOOO0OOO0 ["产品名称"]+"("+OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"]+")"#line:506
		DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及产品图","产品","证号计数","超级托帕斯图(严重伤害数)")#line:507
	elif "dfx_pihao"in OOOOOO0000OO0O00O :#line:509
		if len (OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:510
			OO000O0OOOOO0OOO0 ["产品"]=OO000O0OOOOO0OOO0 ["产品名称"]+"("+OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"]+"--"+OO000O0OOOOO0OOO0 ["产品批号"]+")"#line:511
			DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及批号图","产品","批号计数","超级托帕斯图(严重伤害数)")#line:512
		else :#line:513
			DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及批号图","产品批号","批号计数","超级托帕斯图(严重伤害数)")#line:514
	elif "dfx_xinghao"in OOOOOO0000OO0O00O :#line:516
		if len (OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:517
			OO000O0OOOOO0OOO0 ["产品"]=OO000O0OOOOO0OOO0 ["产品名称"]+"("+OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"]+"--"+OO000O0OOOOO0OOO0 ["型号"]+")"#line:518
			DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及型号图","产品","型号计数","超级托帕斯图(严重伤害数)")#line:519
		else :#line:520
			DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及型号图","型号","型号计数","超级托帕斯图(严重伤害数)")#line:521
	elif "dfx_guige"in OOOOOO0000OO0O00O :#line:523
		if len (OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:524
			OO000O0OOOOO0OOO0 ["产品"]=OO000O0OOOOO0OOO0 ["产品名称"]+"("+OO000O0OOOOO0OOO0 ["注册证编号/曾用注册证编号"]+"--"+OO000O0OOOOO0OOO0 ["规格"]+")"#line:525
			DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及规格图","产品","规格计数","超级托帕斯图(严重伤害数)")#line:526
		else :#line:527
			DRAW_make_one (OO000O0OOOOO0OOO0 ,"涉及规格图","规格","规格计数","超级托帕斯图(严重伤害数)")#line:528
	elif "PSUR"in OOOOOO0000OO0O00O :#line:530
		DRAW_make_mutibar (OO000O0OOOOO0OOO0 ,"总数量","严重","事件分类","总数量","严重","表现分类统计图")#line:531
	elif "keyword_findrisk"in OOOOOO0000OO0O00O :#line:533
		O0OOOO0O0O0OOOOO0 =OO000O0OOOOO0OOO0 .columns .to_list ()#line:535
		OOO0O0O00OOOOOOO0 =O0OOOO0O0O0OOOOO0 [O0OOOO0O0O0OOOOO0 .index ("关键字")+1 ]#line:536
		OOOO0OOO0OO0O0OO0 =pd .pivot_table (OO000O0OOOOO0OOO0 ,index =OOO0O0O00OOOOOOO0 ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:547
		OOOO0OOO0OO0O0OO0 .columns =OOOO0OOO0OO0O0OO0 .columns .droplevel (0 )#line:548
		OOOO0OOO0OO0O0OO0 =OOOO0OOO0OO0O0OO0 [:-1 ].reset_index ()#line:549
		OOOO0OOO0OO0O0OO0 =pd .merge (OOOO0OOO0OO0O0OO0 ,OO000O0OOOOO0OOO0 [[OOO0O0O00OOOOOOO0 ,"该元素总数量"]].drop_duplicates (OOO0O0O00OOOOOOO0 ),on =[OOO0O0O00OOOOOOO0 ],how ="left")#line:551
		del OOOO0OOO0OO0O0OO0 ["All"]#line:553
		DRAW_make_risk_plot (OOOO0OOO0OO0O0OO0 ,OOO0O0O00OOOOOOO0 ,[OO0OOO0OOO0O0000O for OO0OOO0OOO0O0000O in OOOO0OOO0OO0O0OO0 .columns if OO0OOO0OOO0O0000O !=OOO0O0O00OOOOOOO0 ],"关键字趋势图",100 )#line:558
def DRAW_make_risk_plot (O00O0000O00000OOO ,O0O0000000OO000OO ,OOOO00O00O0O0OOO0 ,OOO0O0O00O0OO00O0 ,O00000O00OO0O0000 ):#line:563
    ""#line:564
    OOOOOOO00000O0O00 =Toplevel ()#line:567
    OOOOOOO00000O0O00 .title (OOO0O0O00O0OO00O0 )#line:568
    OOOOO0OO0O000O00O =ttk .Frame (OOOOOOO00000O0O00 ,height =20 )#line:569
    OOOOO0OO0O000O00O .pack (side =TOP )#line:570
    O000OO00OO0O00O00 =Figure (figsize =(12 ,6 ),dpi =100 )#line:572
    O00OO00000OO00O0O =FigureCanvasTkAgg (O000OO00OO0O00O00 ,master =OOOOOOO00000O0O00 )#line:573
    O00OO00000OO00O0O .draw ()#line:574
    O00OO00000OO00O0O .get_tk_widget ().pack (expand =1 )#line:575
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:577
    plt .rcParams ['axes.unicode_minus']=False #line:578
    O0O00O0OOO0OO0000 =NavigationToolbar2Tk (O00OO00000OO00O0O ,OOOOOOO00000O0O00 )#line:580
    O0O00O0OOO0OO0000 .update ()#line:581
    O00OO00000OO00O0O .get_tk_widget ().pack ()#line:582
    O0O0O0O0OOO0000O0 =O000OO00OO0O00O00 .add_subplot (111 )#line:584
    O0O0O0O0OOO0000O0 .set_title (OOO0O0O00O0OO00O0 )#line:586
    OOOOOOOO000O0O0O0 =O00O0000O00000OOO [O0O0000000OO000OO ]#line:587
    if O00000O00OO0O0000 !=999 :#line:590
        O0O0O0O0OOO0000O0 .set_xticklabels (OOOOOOOO000O0O0O0 ,rotation =-90 ,fontsize =8 )#line:591
    OOO0OOO0OOOOO00OO =range (0 ,len (OOOOOOOO000O0O0O0 ),1 )#line:594
    try :#line:599
        O0O0O0O0OOO0000O0 .bar (OOOOOOOO000O0O0O0 ,O00O0000O00000OOO ["报告总数"],color ='skyblue',label ="报告总数")#line:600
        O0O0O0O0OOO0000O0 .bar (OOOOOOOO000O0O0O0 ,height =O00O0000O00000OOO ["严重伤害数"],color ="orangered",label ="严重伤害数")#line:601
    except :#line:602
        pass #line:603
    for OOO0000O000O0OO0O in OOOO00O00O0O0OOO0 :#line:606
        OOO00O00OO0OOO0O0 =O00O0000O00000OOO [OOO0000O000O0OO0O ].astype (float )#line:607
        if OOO0000O000O0OO0O =="关注区域":#line:609
            O0O0O0O0OOO0000O0 .plot (list (OOOOOOOO000O0O0O0 ),list (OOO00O00OO0OOO0O0 ),label =str (OOO0000O000O0OO0O ),color ="red")#line:610
        else :#line:611
            O0O0O0O0OOO0000O0 .plot (list (OOOOOOOO000O0O0O0 ),list (OOO00O00OO0OOO0O0 ),label =str (OOO0000O000O0OO0O ))#line:612
        if O00000O00OO0O0000 ==100 :#line:615
            for OO000OO0O0OO00O0O ,O00OOOOO0O0OO00OO in zip (OOOOOOOO000O0O0O0 ,OOO00O00OO0OOO0O0 ):#line:616
                if O00OOOOO0O0OO00OO ==max (OOO00O00OO0OOO0O0 )and O00OOOOO0O0OO00OO >=3 :#line:617
                     O0O0O0O0OOO0000O0 .text (OO000OO0O0OO00O0O ,O00OOOOO0O0OO00OO ,(str (OOO0000O000O0OO0O )+":"+str (int (O00OOOOO0O0OO00OO ))),color ='black',size =8 )#line:618
    if len (OOOO00O00O0O0OOO0 )==1 :#line:628
        O000O000OO0OOO000 =O00O0000O00000OOO [OOOO00O00O0O0OOO0 ].astype (float ).values #line:629
        OOO0O0O00O00OOO00 =O000O000OO0OOO000 .mean ()#line:630
        OOOOOOO0O0O00OOO0 =O000O000OO0OOO000 .std ()#line:631
        OOOO0O000O0OOOOOO =OOO0O0O00O00OOO00 +3 *OOOOOOO0O0O00OOO0 #line:632
        OO00O00OO0OO000O0 =OOOOOOO0O0O00OOO0 -3 *OOOOOOO0O0O00OOO0 #line:633
        O0O0O0O0OOO0000O0 .axhline (OOO0O0O00O00OOO00 ,color ='r',linestyle ='--',label ='Mean')#line:635
        O0O0O0O0OOO0000O0 .axhline (OOOO0O000O0OOOOOO ,color ='g',linestyle ='--',label ='UCL(μ+3σ)')#line:636
        O0O0O0O0OOO0000O0 .axhline (OO00O00OO0OO000O0 ,color ='g',linestyle ='--',label ='LCL(μ-3σ)')#line:637
    O0O0O0O0OOO0000O0 .set_title ("曲线图")#line:641
    O0O0O0O0OOO0000O0 .set_xlabel ("项")#line:642
    O000OO00OO0O00O00 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:643
    OO0OO0000O0OO0OO0 =O0O0O0O0OOO0000O0 .get_position ()#line:644
    O0O0O0O0OOO0000O0 .set_position ([OO0OO0000O0OO0OO0 .x0 ,OO0OO0000O0OO0OO0 .y0 ,OO0OO0000O0OO0OO0 .width *0.7 ,OO0OO0000O0OO0OO0 .height ])#line:645
    O0O0O0O0OOO0000O0 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:646
    O0000OOOOO000OO0O =StringVar ()#line:670
    OO00O00000O000O0O =ttk .Combobox (OOOOO0OO0O000O00O ,width =15 ,textvariable =O0000OOOOO000OO0O ,state ='readonly')#line:671
    OO00O00000O000O0O ['values']=OOOO00O00O0O0OOO0 #line:672
    OO00O00000O000O0O .pack (side =LEFT )#line:673
    OO00O00000O000O0O .current (0 )#line:674
    O00OOO00OO0000O0O =Button (OOOOO0OO0O000O00O ,text ="控制图（单项）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (O00O0000O00000OOO ,O0O0000000OO000OO ,[OOO00OOO0OOO0O000 for OOO00OOO0OOO0O000 in OOOO00O00O0O0OOO0 if O0000OOOOO000OO0O .get ()in OOO00OOO0OOO0O000 ],OOO0O0O00O0OO00O0 ,O00000O00OO0O0000 ))#line:682
    O00OOO00OO0000O0O .pack (side =LEFT ,anchor ="ne")#line:683
    O0OO0OOO00OO0O0OO =Button (OOOOO0OO0O000O00O ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (O00O0000O00000OOO ,O0O0000000OO000OO ,OOOO00O00O0O0OOO0 ,OOO0O0O00O0OO00O0 ,0 ))#line:691
    O0OO0OOO00OO0O0OO .pack (side =LEFT ,anchor ="ne")#line:692
    O00OO00000OO00O0O .draw ()#line:694
def DRAW_make_one (OOO000OOO00O0O0OO ,O0OOO0OO0OO0O00O0 ,O000O00O0O0OO0O00 ,O00OO0OO00000OOO0 ,O0OO00O0OO00O0O00 ):#line:697
    ""#line:698
    warnings .filterwarnings ("ignore")#line:699
    O0OO0OO0OOOO0OOOO =Toplevel ()#line:700
    O0OO0OO0OOOO0OOOO .title (O0OOO0OO0OO0O00O0 )#line:701
    O00OOOO000OO0000O =ttk .Frame (O0OO0OO0OOOO0OOOO ,height =20 )#line:702
    O00OOOO000OO0000O .pack (side =TOP )#line:703
    OOOO0OO0O000OO0O0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:705
    OOOO0O0OOO0OO0O00 =FigureCanvasTkAgg (OOOO0OO0O000OO0O0 ,master =O0OO0OO0OOOO0OOOO )#line:706
    OOOO0O0OOO0OO0O00 .draw ()#line:707
    OOOO0O0OOO0OO0O00 .get_tk_widget ().pack (expand =1 )#line:708
    OO000OOOOO00O0OOO =OOOO0OO0O000OO0O0 .add_subplot (111 )#line:709
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:711
    plt .rcParams ['axes.unicode_minus']=False #line:712
    O0O0OOOOO00OO0O00 =NavigationToolbar2Tk (OOOO0O0OOO0OO0O00 ,O0OO0OO0OOOO0OOOO )#line:714
    O0O0OOOOO00OO0O00 .update ()#line:715
    OOOO0O0OOO0OO0O00 .get_tk_widget ().pack ()#line:717
    try :#line:720
        O0OOOOOOOOOOO0OO0 =OOO000OOO00O0O0OO .columns #line:721
        OOO000OOO00O0O0OO =OOO000OOO00O0O0OO .sort_values (by =O00OO0OO00000OOO0 ,ascending =[False ],na_position ="last")#line:722
    except :#line:723
        O00000OO0000OO0OO =eval (OOO000OOO00O0O0OO )#line:724
        O00000OO0000OO0OO =pd .DataFrame .from_dict (O00000OO0000OO0OO ,orient =O000O00O0O0OO0O00 ,columns =[O00OO0OO00000OOO0 ]).reset_index ()#line:727
        OOO000OOO00O0O0OO =O00000OO0000OO0OO .sort_values (by =O00OO0OO00000OOO0 ,ascending =[False ],na_position ="last")#line:728
    if ("日期"in O0OOO0OO0OO0O00O0 or "时间"in O0OOO0OO0OO0O00O0 or "季度"in O0OOO0OO0OO0O00O0 )and "饼图"not in O0OO00O0OO00O0O00 :#line:732
        OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ]=pd .to_datetime (OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],format ="%Y/%m/%d").dt .date #line:733
        OOO000OOO00O0O0OO =OOO000OOO00O0O0OO .sort_values (by =O000O00O0O0OO0O00 ,ascending =[True ],na_position ="last")#line:734
    elif "批号"in O0OOO0OO0OO0O00O0 :#line:735
        OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ]=OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ].astype (str )#line:736
        OOO000OOO00O0O0OO =OOO000OOO00O0O0OO .sort_values (by =O000O00O0O0OO0O00 ,ascending =[True ],na_position ="last")#line:737
        OO000OOOOO00O0OOO .set_xticklabels (OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],rotation =-90 ,fontsize =8 )#line:738
    else :#line:739
        OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ]=OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ].astype (str )#line:740
        OO000OOOOO00O0OOO .set_xticklabels (OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],rotation =-90 ,fontsize =8 )#line:741
    O0OOOOO000OOO0OO0 =OOO000OOO00O0O0OO [O00OO0OO00000OOO0 ]#line:743
    O0OO0O0OOO00O00OO =range (0 ,len (O0OOOOO000OOO0OO0 ),1 )#line:744
    OO000OOOOO00O0OOO .set_title (O0OOO0OO0OO0O00O0 )#line:746
    if O0OO00O0OO00O0O00 =="柱状图":#line:750
        OO000OOOOO00O0OOO .bar (x =OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],height =O0OOOOO000OOO0OO0 ,width =0.2 ,color ="#87CEFA")#line:751
    elif O0OO00O0OO00O0O00 =="饼图":#line:752
        OO000OOOOO00O0OOO .pie (x =O0OOOOO000OOO0OO0 ,labels =OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],autopct ="%0.2f%%")#line:753
    elif O0OO00O0OO00O0O00 =="折线图":#line:754
        OO000OOOOO00O0OOO .plot (OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],O0OOOOO000OOO0OO0 ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:755
    elif "托帕斯图"in str (O0OO00O0OO00O0O00 ):#line:757
        OOO0OO000000O0OO0 =OOO000OOO00O0O0OO [O00OO0OO00000OOO0 ].fillna (0 )#line:758
        OO00O000OO00O0000 =OOO0OO000000O0OO0 .cumsum ()/OOO0OO000000O0OO0 .sum ()*100 #line:762
        OO0O0O0000000O00O =OO00O000OO00O0000 [OO00O000OO00O0000 >0.8 ].index [0 ]#line:764
        OOO00OO0000000OO0 =OOO0OO000000O0OO0 .index .tolist ().index (OO0O0O0000000O00O )#line:765
        OO000OOOOO00O0OOO .bar (x =OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],height =OOO0OO000000O0OO0 ,color ="C0",label =O00OO0OO00000OOO0 )#line:769
        OOOOOO0O00O0O0O0O =OO000OOOOO00O0OOO .twinx ()#line:770
        OOOOOO0O00O0O0O0O .plot (OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],OO00O000OO00O0000 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:771
        OOOOOO0O00O0O0O0O .yaxis .set_major_formatter (PercentFormatter ())#line:772
        OO000OOOOO00O0OOO .tick_params (axis ="y",colors ="C0")#line:777
        OOOOOO0O00O0O0O0O .tick_params (axis ="y",colors ="C1")#line:778
        if "超级托帕斯图"in str (O0OO00O0OO00O0O00 ):#line:781
            OOOOO00O00OOOOOOO =re .compile (r'[(](.*?)[)]',re .S )#line:782
            OOOOO000OO0O0O000 =re .findall (OOOOO00O00OOOOOOO ,O0OO00O0OO00O0O00 )[0 ]#line:783
            OO000OOOOO00O0OOO .bar (x =OOO000OOO00O0O0OO [O000O00O0O0OO0O00 ],height =OOO000OOO00O0O0OO [OOOOO000OO0O0O000 ],color ="orangered",label =OOOOO000OO0O0O000 )#line:784
    OOOO0OO0O000OO0O0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:786
    OO0OO00000O0O00O0 =OO000OOOOO00O0OOO .get_position ()#line:787
    OO000OOOOO00O0OOO .set_position ([OO0OO00000O0O00O0 .x0 ,OO0OO00000O0O00O0 .y0 ,OO0OO00000O0O00O0 .width *0.7 ,OO0OO00000O0O00O0 .height ])#line:788
    OO000OOOOO00O0OOO .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:789
    OOOO0O0OOO0OO0O00 .draw ()#line:792
    if len (O0OOOOO000OOO0OO0 )<=20 and O0OO00O0OO00O0O00 !="饼图":#line:795
        for O00OOO0O0O0OO0OO0 ,O000OO000O0OO00O0 in zip (O0OO0O0OOO00O00OO ,O0OOOOO000OOO0OO0 ):#line:796
            OO0OO0O0O0OOO0000 =str (O000OO000O0OO00O0 )#line:797
            OOOOO0O00O0000O00 =(O00OOO0O0O0OO0OO0 ,O000OO000O0OO00O0 +0.3 )#line:798
            OO000OOOOO00O0OOO .annotate (OO0OO0O0O0OOO0000 ,xy =OOOOO0O00O0000O00 ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:799
    O000OOO0OO0OO0OO0 =Button (O00OOOO000OO0000O ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OOO000OOO00O0O0OO ),)#line:809
    O000OOO0OO0OO0OO0 .pack (side =RIGHT )#line:810
    OOOOO0O000OOOOO00 =Button (O00OOOO000OO0000O ,relief =GROOVE ,text ="查看原始数据",command =lambda :TOOLS_view_dict (OOO000OOO00O0O0OO ,0 ))#line:814
    OOOOO0O000OOOOO00 .pack (side =RIGHT )#line:815
    O0O00000O0OO0OO0O =Button (O00OOOO000OO0000O ,relief =GROOVE ,text ="饼图",command =lambda :DRAW_make_one (OOO000OOO00O0O0OO ,O0OOO0OO0OO0O00O0 ,O000O00O0O0OO0O00 ,O00OO0OO00000OOO0 ,"饼图"),)#line:823
    O0O00000O0OO0OO0O .pack (side =LEFT )#line:824
    O0O00000O0OO0OO0O =Button (O00OOOO000OO0000O ,relief =GROOVE ,text ="柱状图",command =lambda :DRAW_make_one (OOO000OOO00O0O0OO ,O0OOO0OO0OO0O00O0 ,O000O00O0O0OO0O00 ,O00OO0OO00000OOO0 ,"柱状图"),)#line:831
    O0O00000O0OO0OO0O .pack (side =LEFT )#line:832
    O0O00000O0OO0OO0O =Button (O00OOOO000OO0000O ,relief =GROOVE ,text ="折线图",command =lambda :DRAW_make_one (OOO000OOO00O0O0OO ,O0OOO0OO0OO0O00O0 ,O000O00O0O0OO0O00 ,O00OO0OO00000OOO0 ,"折线图"),)#line:838
    O0O00000O0OO0OO0O .pack (side =LEFT )#line:839
    O0O00000O0OO0OO0O =Button (O00OOOO000OO0000O ,relief =GROOVE ,text ="托帕斯图",command =lambda :DRAW_make_one (OOO000OOO00O0O0OO ,O0OOO0OO0OO0O00O0 ,O000O00O0O0OO0O00 ,O00OO0OO00000OOO0 ,"托帕斯图"),)#line:846
    O0O00000O0OO0OO0O .pack (side =LEFT )#line:847
def DRAW_make_mutibar (OOOOO0O0O0000O0O0 ,O0O00OO0OO0OOOO0O ,O0OO000000O0000OO ,O000OO00OOOO000O0 ,OOOOOO0O00000OOOO ,O00OO0O00O000OOO0 ,OOOO0OO0OO0O0O0OO ):#line:848
    ""#line:849
    OOOOO0OO00O0000OO =Toplevel ()#line:850
    OOOOO0OO00O0000OO .title (OOOO0OO0OO0O0O0OO )#line:851
    O00OO0O0OO0O0OOOO =ttk .Frame (OOOOO0OO00O0000OO ,height =20 )#line:852
    O00OO0O0OO0O0OOOO .pack (side =TOP )#line:853
    O0O00O0O0O00O00OO =0.2 #line:855
    OO00O0O0O0O0O0OO0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:856
    O0000OOO0O0000000 =FigureCanvasTkAgg (OO00O0O0O0O0O0OO0 ,master =OOOOO0OO00O0000OO )#line:857
    O0000OOO0O0000000 .draw ()#line:858
    O0000OOO0O0000000 .get_tk_widget ().pack (expand =1 )#line:859
    O0O0O00OO0OO0O00O =OO00O0O0O0O0O0OO0 .add_subplot (111 )#line:860
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:862
    plt .rcParams ['axes.unicode_minus']=False #line:863
    OOOO00OOOOOO0O00O =NavigationToolbar2Tk (O0000OOO0O0000000 ,OOOOO0OO00O0000OO )#line:865
    OOOO00OOOOOO0O00O .update ()#line:866
    O0000OOO0O0000000 .get_tk_widget ().pack ()#line:868
    O0O00OO0OO0OOOO0O =OOOOO0O0O0000O0O0 [O0O00OO0OO0OOOO0O ]#line:869
    O0OO000000O0000OO =OOOOO0O0O0000O0O0 [O0OO000000O0000OO ]#line:870
    O000OO00OOOO000O0 =OOOOO0O0O0000O0O0 [O000OO00OOOO000O0 ]#line:871
    O0OO0OOO00000OOOO =range (0 ,len (O0O00OO0OO0OOOO0O ),1 )#line:873
    O0O0O00OO0OO0O00O .set_xticklabels (O000OO00OOOO000O0 ,rotation =-90 ,fontsize =8 )#line:874
    O0O0O00OO0OO0O00O .bar (O0OO0OOO00000OOOO ,O0O00OO0OO0OOOO0O ,align ="center",tick_label =O000OO00OOOO000O0 ,label =OOOOOO0O00000OOOO )#line:877
    O0O0O00OO0OO0O00O .bar (O0OO0OOO00000OOOO ,O0OO000000O0000OO ,align ="center",label =O00OO0O00O000OOO0 )#line:880
    O0O0O00OO0OO0O00O .set_title (OOOO0OO0OO0O0O0OO )#line:881
    O0O0O00OO0OO0O00O .set_xlabel ("项")#line:882
    O0O0O00OO0OO0O00O .set_ylabel ("数量")#line:883
    OO00O0O0O0O0O0OO0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:885
    O0O0OO0000OOOO0O0 =O0O0O00OO0OO0O00O .get_position ()#line:886
    O0O0O00OO0OO0O00O .set_position ([O0O0OO0000OOOO0O0 .x0 ,O0O0OO0000OOOO0O0 .y0 ,O0O0OO0000OOOO0O0 .width *0.7 ,O0O0OO0000OOOO0O0 .height ])#line:887
    O0O0O00OO0OO0O00O .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:888
    O0000OOO0O0000000 .draw ()#line:890
    O0O00OOOO0OO0OO00 =Button (O00OO0O0OO0O0OOOO ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OOOOO0O0O0000O0O0 ),)#line:897
    O0O00OOOO0OO0OO00 .pack (side =RIGHT )#line:898
def CLEAN_hzp (OO00O0OO00O00000O ):#line:903
    ""#line:904
    if "报告编码"not in OO00O0OO00O00000O .columns :#line:905
            OO00O0OO00O00000O ["特殊化妆品注册证书编号/普通化妆品备案编号"]=OO00O0OO00O00000O ["特殊化妆品注册证书编号/普通化妆品备案编号"].fillna ("-未填写-")#line:906
            OO00O0OO00O00000O ["省级评价结果"]=OO00O0OO00O00000O ["省级评价结果"].fillna ("-未填写-")#line:907
            OO00O0OO00O00000O ["生产企业"]=OO00O0OO00O00000O ["生产企业"].fillna ("-未填写-")#line:908
            OO00O0OO00O00000O ["提交人"]="不适用"#line:909
            OO00O0OO00O00000O ["医疗机构类别"]="不适用"#line:910
            OO00O0OO00O00000O ["经营企业或使用单位"]="不适用"#line:911
            OO00O0OO00O00000O ["报告状态"]="报告单位评价"#line:912
            OO00O0OO00O00000O ["所属地区"]="不适用"#line:913
            OO00O0OO00O00000O ["医院名称"]="不适用"#line:914
            OO00O0OO00O00000O ["报告地区名称"]="不适用"#line:915
            OO00O0OO00O00000O ["提交人"]="不适用"#line:916
            OO00O0OO00O00000O ["型号"]=OO00O0OO00O00000O ["化妆品分类"]#line:917
            OO00O0OO00O00000O ["关联性评价"]=OO00O0OO00O00000O ["上报单位评价结果"]#line:918
            OO00O0OO00O00000O ["规格"]="不适用"#line:919
            OO00O0OO00O00000O ["器械故障表现"]=OO00O0OO00O00000O ["初步判断"]#line:920
            OO00O0OO00O00000O ["伤害表现"]=OO00O0OO00O00000O ["自觉症状"]+OO00O0OO00O00000O ["皮损部位"]+OO00O0OO00O00000O ["皮损形态"]#line:921
            OO00O0OO00O00000O ["事件原因分析"]="不适用"#line:922
            OO00O0OO00O00000O ["事件原因分析描述"]="不适用"#line:923
            OO00O0OO00O00000O ["调查情况"]="不适用"#line:924
            OO00O0OO00O00000O ["具体控制措施"]="不适用"#line:925
            OO00O0OO00O00000O ["未采取控制措施原因"]="不适用"#line:926
            OO00O0OO00O00000O ["报告地区名称"]="不适用"#line:927
            OO00O0OO00O00000O ["上报单位所属地区"]="不适用"#line:928
            OO00O0OO00O00000O ["持有人报告状态"]="不适用"#line:929
            OO00O0OO00O00000O ["年龄类型"]="岁"#line:930
            OO00O0OO00O00000O ["经营企业使用单位报告状态"]="不适用"#line:931
            OO00O0OO00O00000O ["产品归属"]="化妆品"#line:932
            OO00O0OO00O00000O ["管理类别"]="不适用"#line:933
            OO00O0OO00O00000O ["超时标记"]="不适用"#line:934
            OO00O0OO00O00000O =OO00O0OO00O00000O .rename (columns ={"报告表编号":"报告编码","报告类型":"伤害","报告地区":"监测机构","报告单位名称":"单位名称","患者/消费者姓名":"姓名","不良反应发生日期":"事件发生日期","过程描述补充说明":"使用过程","化妆品名称":"产品名称","化妆品分类":"产品类别","生产企业":"上市许可持有人名称","生产批号":"产品批号","特殊化妆品注册证书编号/普通化妆品备案编号":"注册证编号/曾用注册证编号",})#line:953
            OO00O0OO00O00000O ["时隔"]=pd .to_datetime (OO00O0OO00O00000O ["事件发生日期"])-pd .to_datetime (OO00O0OO00O00000O ["开始使用日期"])#line:954
            OO00O0OO00O00000O .loc [(OO00O0OO00O00000O ["省级评价结果"]!="-未填写-"),"有效报告"]=1 #line:955
            OO00O0OO00O00000O ["伤害"]=OO00O0OO00O00000O ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:956
            try :#line:957
	            OO00O0OO00O00000O =TOOL_guizheng (OO00O0OO00O00000O ,4 ,True )#line:958
            except :#line:959
                pass #line:960
            return OO00O0OO00O00000O #line:961
def CLEAN_yp (OO00O0OOO0O0O0OO0 ):#line:966
    ""#line:967
    if "报告编码"not in OO00O0OOO0O0O0OO0 .columns :#line:968
        if "反馈码"in OO00O0OOO0O0O0OO0 .columns and "报告表编码"not in OO00O0OOO0O0O0OO0 .columns :#line:970
            OO00O0OOO0O0O0OO0 ["提交人"]="不适用"#line:972
            OO00O0OOO0O0O0OO0 ["经营企业或使用单位"]="不适用"#line:973
            OO00O0OOO0O0O0OO0 ["报告状态"]="报告单位评价"#line:974
            OO00O0OOO0O0O0OO0 ["所属地区"]="不适用"#line:975
            OO00O0OOO0O0O0OO0 ["产品类别"]="无源"#line:976
            OO00O0OOO0O0O0OO0 ["医院名称"]="不适用"#line:977
            OO00O0OOO0O0O0OO0 ["报告地区名称"]="不适用"#line:978
            OO00O0OOO0O0O0OO0 ["提交人"]="不适用"#line:979
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"反馈码":"报告表编码","序号":"药品序号","新的":"报告类型-新的","报告类型":"报告类型-严重程度","用药-日数":"用法-日","用药-次数":"用法-次",})#line:992
        if "唯一标识"not in OO00O0OOO0O0O0OO0 .columns :#line:997
            OO00O0OOO0O0O0OO0 ["报告编码"]=OO00O0OOO0O0O0OO0 ["报告表编码"].astype (str )+OO00O0OOO0O0O0OO0 ["患者姓名"].astype (str )#line:998
        if "唯一标识"in OO00O0OOO0O0O0OO0 .columns :#line:999
            OO00O0OOO0O0O0OO0 ["唯一标识"]=OO00O0OOO0O0O0OO0 ["唯一标识"].astype (str )#line:1000
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"唯一标识":"报告编码"})#line:1001
        if "医疗机构类别"not in OO00O0OOO0O0O0OO0 .columns :#line:1002
            OO00O0OOO0O0O0OO0 ["医疗机构类别"]="医疗机构"#line:1003
            OO00O0OOO0O0O0OO0 ["经营企业使用单位报告状态"]="已提交"#line:1004
        try :#line:1005
            OO00O0OOO0O0O0OO0 ["年龄和单位"]=OO00O0OOO0O0O0OO0 ["年龄"].astype (str )+OO00O0OOO0O0O0OO0 ["年龄单位"]#line:1006
        except :#line:1007
            OO00O0OOO0O0O0OO0 ["年龄和单位"]=OO00O0OOO0O0O0OO0 ["年龄"].astype (str )+OO00O0OOO0O0O0OO0 ["年龄类型"]#line:1008
        OO00O0OOO0O0O0OO0 .loc [(OO00O0OOO0O0O0OO0 ["报告类型-新的"]=="新的"),"管理类别"]="Ⅲ类"#line:1009
        OO00O0OOO0O0O0OO0 .loc [(OO00O0OOO0O0O0OO0 ["报告类型-严重程度"]=="严重"),"管理类别"]="Ⅲ类"#line:1010
        text .insert (END ,"剔除已删除报告和重复报告...")#line:1011
        if "删除标识"in OO00O0OOO0O0O0OO0 .columns :#line:1012
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 [(OO00O0OOO0O0O0OO0 ["删除标识"]!="删除")]#line:1013
        if "重复报告"in OO00O0OOO0O0O0OO0 .columns :#line:1014
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 [(OO00O0OOO0O0O0OO0 ["重复报告"]!="重复报告")]#line:1015
        OO00O0OOO0O0O0OO0 ["报告类型-新的"]=OO00O0OOO0O0O0OO0 ["报告类型-新的"].fillna (" ")#line:1018
        OO00O0OOO0O0O0OO0 .loc [(OO00O0OOO0O0O0OO0 ["报告类型-严重程度"]=="严重"),"伤害"]="严重伤害"#line:1019
        OO00O0OOO0O0O0OO0 ["伤害"]=OO00O0OOO0O0O0OO0 ["伤害"].fillna ("所有一般")#line:1020
        OO00O0OOO0O0O0OO0 ["伤害PSUR"]=OO00O0OOO0O0O0OO0 ["报告类型-新的"].astype (str )+OO00O0OOO0O0O0OO0 ["报告类型-严重程度"].astype (str )#line:1021
        OO00O0OOO0O0O0OO0 ["用量用量单位"]=OO00O0OOO0O0O0OO0 ["用量"].astype (str )+OO00O0OOO0O0O0OO0 ["用量单位"].astype (str )#line:1022
        OO00O0OOO0O0O0OO0 ["规格"]="不适用"#line:1024
        OO00O0OOO0O0O0OO0 ["事件原因分析"]="不适用"#line:1025
        OO00O0OOO0O0O0OO0 ["事件原因分析描述"]="不适用"#line:1026
        OO00O0OOO0O0O0OO0 ["初步处置情况"]="不适用"#line:1027
        OO00O0OOO0O0O0OO0 ["伤害表现"]=OO00O0OOO0O0O0OO0 ["不良反应名称"]#line:1028
        OO00O0OOO0O0O0OO0 ["产品类别"]="无源"#line:1029
        OO00O0OOO0O0O0OO0 ["调查情况"]="不适用"#line:1030
        OO00O0OOO0O0O0OO0 ["具体控制措施"]="不适用"#line:1031
        OO00O0OOO0O0O0OO0 ["上报单位所属地区"]=OO00O0OOO0O0O0OO0 ["报告地区名称"]#line:1032
        OO00O0OOO0O0O0OO0 ["未采取控制措施原因"]="不适用"#line:1033
        OO00O0OOO0O0O0OO0 ["报告单位评价"]=OO00O0OOO0O0O0OO0 ["报告类型-新的"].astype (str )+OO00O0OOO0O0O0OO0 ["报告类型-严重程度"].astype (str )#line:1034
        OO00O0OOO0O0O0OO0 .loc [(OO00O0OOO0O0O0OO0 ["报告类型-新的"]=="新的"),"持有人报告状态"]="待评价"#line:1035
        OO00O0OOO0O0O0OO0 ["用法temp日"]="日"#line:1036
        OO00O0OOO0O0O0OO0 ["用法temp次"]="次"#line:1037
        OO00O0OOO0O0O0OO0 ["用药频率"]=(OO00O0OOO0O0O0OO0 ["用法-日"].astype (str )+OO00O0OOO0O0O0OO0 ["用法temp日"]+OO00O0OOO0O0O0OO0 ["用法-次"].astype (str )+OO00O0OOO0O0O0OO0 ["用法temp次"])#line:1043
        try :#line:1044
            OO00O0OOO0O0O0OO0 ["相关疾病信息[疾病名称]-术语"]=OO00O0OOO0O0O0OO0 ["原患疾病"]#line:1045
            OO00O0OOO0O0O0OO0 ["治疗适应症-术语"]=OO00O0OOO0O0O0OO0 ["用药原因"]#line:1046
        except :#line:1047
            pass #line:1048
        try :#line:1050
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"提交日期":"报告日期"})#line:1051
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"提交人":"报告人"})#line:1052
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"报告状态":"持有人报告状态"})#line:1053
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"所属地区":"使用单位、经营企业所属监测机构"})#line:1054
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"医院名称":"单位名称"})#line:1055
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"批准文号":"注册证编号/曾用注册证编号"})#line:1056
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"通用名称":"产品名称"})#line:1057
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"生产厂家":"上市许可持有人名称"})#line:1058
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"不良反应发生时间":"事件发生日期"})#line:1059
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"不良反应名称":"器械故障表现"})#line:1060
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"不良反应过程描述":"使用过程"})#line:1061
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"生产批号":"产品批号"})#line:1062
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:1063
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"剂型":"型号"})#line:1064
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"报告人评价":"关联性评价"})#line:1065
            OO00O0OOO0O0O0OO0 =OO00O0OOO0O0O0OO0 .rename (columns ={"年龄单位":"年龄类型"})#line:1066
        except :#line:1067
            text .insert (END ,"数据规整失败。")#line:1068
            return 0 #line:1069
        OO00O0OOO0O0O0OO0 ['报告日期']=OO00O0OOO0O0O0OO0 ['报告日期'].str .strip ()#line:1072
        OO00O0OOO0O0O0OO0 ['事件发生日期']=OO00O0OOO0O0O0OO0 ['事件发生日期'].str .strip ()#line:1073
        OO00O0OOO0O0O0OO0 ['用药开始时间']=OO00O0OOO0O0O0OO0 ['用药开始时间'].str .strip ()#line:1074
        return OO00O0OOO0O0O0OO0 #line:1076
    if "报告编码"in OO00O0OOO0O0O0OO0 .columns :#line:1077
        return OO00O0OOO0O0O0OO0 #line:1078
def CLEAN_qx (O0O00OO00000O0O0O ):#line:1080
		""#line:1081
		if "使用单位、经营企业所属监测机构"not in O0O00OO00000O0O0O .columns and "监测机构"not in O0O00OO00000O0O0O .columns :#line:1083
			O0O00OO00000O0O0O ["使用单位、经营企业所属监测机构"]="本地"#line:1084
		if "上市许可持有人名称"not in O0O00OO00000O0O0O .columns :#line:1085
			O0O00OO00000O0O0O ["上市许可持有人名称"]=O0O00OO00000O0O0O ["单位名称"]#line:1086
		if "注册证编号/曾用注册证编号"not in O0O00OO00000O0O0O .columns :#line:1087
			O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]=O0O00OO00000O0O0O ["注册证编号"]#line:1088
		if "事件原因分析描述"not in O0O00OO00000O0O0O .columns :#line:1089
			O0O00OO00000O0O0O ["事件原因分析描述"]="  "#line:1090
		if "初步处置情况"not in O0O00OO00000O0O0O .columns :#line:1091
			O0O00OO00000O0O0O ["初步处置情况"]="  "#line:1092
		text .insert (END ,"\n正在执行格式规整和增加有关时间、年龄、性别等统计列...")#line:1095
		O0O00OO00000O0O0O =O0O00OO00000O0O0O .rename (columns ={"使用单位、经营企业所属监测机构":"监测机构"})#line:1096
		O0O00OO00000O0O0O ["报告编码"]=O0O00OO00000O0O0O ["报告编码"].astype ("str")#line:1097
		O0O00OO00000O0O0O ["产品批号"]=O0O00OO00000O0O0O ["产品批号"].astype ("str")#line:1098
		O0O00OO00000O0O0O ["型号"]=O0O00OO00000O0O0O ["型号"].astype ("str")#line:1099
		O0O00OO00000O0O0O ["规格"]=O0O00OO00000O0O0O ["规格"].astype ("str")#line:1100
		O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]=O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1101
		O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]=O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1102
		O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]=O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1103
		O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]=O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"].fillna ("-未填写-")#line:1104
		O0O00OO00000O0O0O ["产品名称"]=O0O00OO00000O0O0O ["产品名称"].str .replace ("*","※",regex =False )#line:1105
		O0O00OO00000O0O0O ["产品批号"]=O0O00OO00000O0O0O ["产品批号"].str .replace ("(","（",regex =False )#line:1106
		O0O00OO00000O0O0O ["产品批号"]=O0O00OO00000O0O0O ["产品批号"].str .replace (")","）",regex =False )#line:1107
		O0O00OO00000O0O0O ["产品批号"]=O0O00OO00000O0O0O ["产品批号"].str .replace ("*","※",regex =False )#line:1108
		O0O00OO00000O0O0O ["伤害与评价"]=O0O00OO00000O0O0O ["伤害"]+O0O00OO00000O0O0O ["持有人报告状态"]#line:1111
		O0O00OO00000O0O0O ["注册证备份"]=O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]#line:1112
		O0O00OO00000O0O0O ['报告日期']=pd .to_datetime (O0O00OO00000O0O0O ['报告日期'],format ='%Y-%m-%d',errors ='coerce')#line:1115
		O0O00OO00000O0O0O ['事件发生日期']=pd .to_datetime (O0O00OO00000O0O0O ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1116
		O0O00OO00000O0O0O ["报告月份"]=O0O00OO00000O0O0O ["报告日期"].dt .to_period ("M").astype (str )#line:1118
		O0O00OO00000O0O0O ["报告季度"]=O0O00OO00000O0O0O ["报告日期"].dt .to_period ("Q").astype (str )#line:1119
		O0O00OO00000O0O0O ["报告年份"]=O0O00OO00000O0O0O ["报告日期"].dt .to_period ("Y").astype (str )#line:1120
		O0O00OO00000O0O0O ["事件发生月份"]=O0O00OO00000O0O0O ["事件发生日期"].dt .to_period ("M").astype (str )#line:1121
		O0O00OO00000O0O0O ["事件发生季度"]=O0O00OO00000O0O0O ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1122
		O0O00OO00000O0O0O ["事件发生年份"]=O0O00OO00000O0O0O ["事件发生日期"].dt .to_period ("Y").astype (str )#line:1123
		if ini ["模式"]=="器械":#line:1127
			O0O00OO00000O0O0O ['发现或获知日期']=pd .to_datetime (O0O00OO00000O0O0O ['发现或获知日期'],format ='%Y-%m-%d',errors ='coerce')#line:1128
			O0O00OO00000O0O0O ["时隔"]=pd .to_datetime (O0O00OO00000O0O0O ["发现或获知日期"])-pd .to_datetime (O0O00OO00000O0O0O ["事件发生日期"])#line:1129
			O0O00OO00000O0O0O ["报告时限"]=pd .to_datetime (O0O00OO00000O0O0O ["报告日期"])-pd .to_datetime (O0O00OO00000O0O0O ["发现或获知日期"])#line:1130
			O0O00OO00000O0O0O ["报告时限"]=O0O00OO00000O0O0O ["报告时限"].dt .days #line:1131
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>20 )&(O0O00OO00000O0O0O ["伤害"]=="严重伤害"),"超时标记"]=1 #line:1132
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>30 )&(O0O00OO00000O0O0O ["伤害"]=="其他"),"超时标记"]=1 #line:1133
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>7 )&(O0O00OO00000O0O0O ["伤害"]=="死亡"),"超时标记"]=1 #line:1134
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["经营企业使用单位报告状态"]=="审核通过"),"有效报告"]=1 #line:1136
		if ini ["模式"]=="药品":#line:1139
			O0O00OO00000O0O0O ['用药开始时间']=pd .to_datetime (O0O00OO00000O0O0O ['用药开始时间'],format ='%Y-%m-%d',errors ='coerce')#line:1140
			O0O00OO00000O0O0O ["时隔"]=pd .to_datetime (O0O00OO00000O0O0O ["事件发生日期"])-pd .to_datetime (O0O00OO00000O0O0O ["用药开始时间"])#line:1141
			O0O00OO00000O0O0O ["报告时限"]=pd .to_datetime (O0O00OO00000O0O0O ["报告日期"])-pd .to_datetime (O0O00OO00000O0O0O ["事件发生日期"])#line:1142
			O0O00OO00000O0O0O ["报告时限"]=O0O00OO00000O0O0O ["报告时限"].dt .days #line:1143
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>15 )&(O0O00OO00000O0O0O ["报告类型-严重程度"]=="严重"),"超时标记"]=1 #line:1144
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>30 )&(O0O00OO00000O0O0O ["报告类型-严重程度"]=="一般"),"超时标记"]=1 #line:1145
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>15 )&(O0O00OO00000O0O0O ["报告类型-新的"]=="新的"),"超时标记"]=1 #line:1146
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["报告时限"]>1 )&(O0O00OO00000O0O0O ["报告类型-严重程度"]=="死亡"),"超时标记"]=1 #line:1147
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["评价状态"]!="未评价"),"有效报告"]=1 #line:1149
		O0O00OO00000O0O0O .loc [((O0O00OO00000O0O0O ["年龄"]=="未填写")|O0O00OO00000O0O0O ["年龄"].isnull ()),"年龄"]=-1 #line:1151
		O0O00OO00000O0O0O ["年龄"]=O0O00OO00000O0O0O ["年龄"].astype (float )#line:1152
		O0O00OO00000O0O0O ["年龄"]=O0O00OO00000O0O0O ["年龄"].fillna (-1 )#line:1153
		O0O00OO00000O0O0O ["性别"]=O0O00OO00000O0O0O ["性别"].fillna ("未填写")#line:1154
		O0O00OO00000O0O0O ["年龄段"]="未填写"#line:1155
		try :#line:1156
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄类型"]=="月"),"年龄"]=O0O00OO00000O0O0O ["年龄"].values /12 #line:1157
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄类型"]=="月"),"年龄类型"]="岁"#line:1158
		except :#line:1159
			pass #line:1160
		try :#line:1161
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄类型"]=="天"),"年龄"]=O0O00OO00000O0O0O ["年龄"].values /365 #line:1162
			O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄类型"]=="天"),"年龄类型"]="岁"#line:1163
		except :#line:1164
			pass #line:1165
		O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄"].values <=4 ),"年龄段"]="0-婴幼儿（0-4）"#line:1166
		O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄"].values >=5 ),"年龄段"]="1-少儿（5-14）"#line:1167
		O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄"].values >=15 ),"年龄段"]="2-青壮年（15-44）"#line:1168
		O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄"].values >=45 ),"年龄段"]="3-中年期（45-64）"#line:1169
		O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄"].values >=65 ),"年龄段"]="4-老年期（≥65）"#line:1170
		O0O00OO00000O0O0O .loc [(O0O00OO00000O0O0O ["年龄"].values ==-1 ),"年龄段"]="未填写"#line:1171
		O0O00OO00000O0O0O ["规整后品类"]="N"#line:1175
		O0O00OO00000O0O0O =TOOL_guizheng (O0O00OO00000O0O0O ,2 ,True )#line:1176
		if ini ['模式']in ["器械"]:#line:1179
			O0O00OO00000O0O0O =TOOL_guizheng (O0O00OO00000O0O0O ,3 ,True )#line:1180
		O0O00OO00000O0O0O =TOOL_guizheng (O0O00OO00000O0O0O ,"课题",True )#line:1184
		try :#line:1186
			O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"]=O0O00OO00000O0O0O ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1187
		except :#line:1188
			pass #line:1189
		O0O00OO00000O0O0O ["数据清洗完成标记"]="是"#line:1191
		O00O00OO0O0O000OO =O0O00OO00000O0O0O .loc [:]#line:1192
		return O0O00OO00000O0O0O #line:1193
def TOOLS_fileopen ():#line:1199
    ""#line:1200
    warnings .filterwarnings ('ignore')#line:1201
    O000O00000OOOOO0O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:1202
    O000OOOO0O0OO00O0 =Useful_tools_openfiles (O000O00000OOOOO0O ,0 )#line:1203
    try :#line:1204
        O000OOOO0O0OO00O0 =O000OOOO0O0OO00O0 .loc [:,~O000OOOO0O0OO00O0 .columns .str .contains ("^Unnamed")]#line:1205
    except :#line:1206
        pass #line:1207
    ini ["模式"]="其他"#line:1209
    O00O0O000O00OOO00 =O000OOOO0O0OO00O0 #line:1210
    TABLE_tree_Level_2 (O00O0O000O00OOO00 ,0 ,O00O0O000O00OOO00 )#line:1211
def TOOLS_pinzhong (O0OO0O0O00O0O0OO0 ):#line:1214
    ""#line:1215
    O0OO0O0O00O0O0OO0 ["患者姓名"]=O0OO0O0O00O0O0OO0 ["报告表编码"]#line:1216
    O0OO0O0O00O0O0OO0 ["用量"]=O0OO0O0O00O0O0OO0 ["用法用量"]#line:1217
    O0OO0O0O00O0O0OO0 ["评价状态"]=O0OO0O0O00O0O0OO0 ["报告单位评价"]#line:1218
    O0OO0O0O00O0O0OO0 ["用量单位"]=""#line:1219
    O0OO0O0O00O0O0OO0 ["单位名称"]="不适用"#line:1220
    O0OO0O0O00O0O0OO0 ["报告地区名称"]="不适用"#line:1221
    O0OO0O0O00O0O0OO0 ["用法-日"]="不适用"#line:1222
    O0OO0O0O00O0O0OO0 ["用法-次"]="不适用"#line:1223
    O0OO0O0O00O0O0OO0 ["不良反应发生时间"]=O0OO0O0O00O0O0OO0 ["不良反应发生时间"].str [0 :10 ]#line:1224
    O0OO0O0O00O0O0OO0 ["持有人报告状态"]="待评价"#line:1226
    O0OO0O0O00O0O0OO0 =O0OO0O0O00O0O0OO0 .rename (columns ={"是否非预期":"报告类型-新的","不良反应-术语":"不良反应名称","持有人/生产厂家":"上市许可持有人名称"})#line:1231
    return O0OO0O0O00O0O0OO0 #line:1232
def Useful_tools_openfiles (OOOOOO0O0O00000O0 ,O0O0OOO0O0OO0O0O0 ):#line:1237
    ""#line:1238
    OO00O0000OO0OOOO0 =[pd .read_excel (OO00OOO0O0000OOO0 ,header =0 ,sheet_name =O0O0OOO0O0OO0O0O0 )for OO00OOO0O0000OOO0 in OOOOOO0O0O00000O0 ]#line:1239
    OOOOOOO0000OOO00O =pd .concat (OO00O0000OO0OOOO0 ,ignore_index =True ).drop_duplicates ()#line:1240
    return OOOOOOO0000OOO00O #line:1241
def TOOLS_allfileopen ():#line:1243
    ""#line:1244
    global ori #line:1245
    global ini #line:1246
    global data #line:1247
    ini ["原始模式"]="否"#line:1248
    warnings .filterwarnings ('ignore')#line:1249
    OO000OOO00O0O0O00 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:1251
    ori =Useful_tools_openfiles (OO000OOO00O0O0O00 ,0 )#line:1252
    try :#line:1256
        O00O0000OOOO00OO0 =Useful_tools_openfiles (OO000OOO00O0O0O00 ,"报告信息")#line:1257
        if "是否非预期"in O00O0000OOOO00OO0 .columns :#line:1258
            ori =TOOLS_pinzhong (O00O0000OOOO00OO0 )#line:1259
    except :#line:1260
        pass #line:1261
    ini ["模式"]="其他"#line:1263
    try :#line:1265
        ori =Useful_tools_openfiles (OO000OOO00O0O0O00 ,"字典数据")#line:1266
        ini ["原始模式"]="是"#line:1267
        if "UDI"in ori .columns :#line:1268
            ini ["模式"]="器械"#line:1269
            data =ori #line:1270
        if "报告类型-新的"in ori .columns :#line:1271
            ini ["模式"]="药品"#line:1272
            data =ori #line:1273
        else :#line:1274
            ini ["模式"]="其他"#line:1275
    except :#line:1276
        pass #line:1277
    try :#line:1280
        ori =ori .loc [:,~ori .columns .str .contains ("^Unnamed")]#line:1281
    except :#line:1282
        pass #line:1283
    if "UDI"in ori .columns and ini ["原始模式"]!="是":#line:1287
        text .insert (END ,"识别出为器械报表,正在进行数据规整...")#line:1288
        ini ["模式"]="器械"#line:1289
        ori =CLEAN_qx (ori )#line:1290
        data =ori #line:1291
    if "报告类型-新的"in ori .columns and ini ["原始模式"]!="是":#line:1292
        text .insert (END ,"识别出为药品报表,正在进行数据规整...")#line:1293
        ini ["模式"]="药品"#line:1294
        ori =CLEAN_yp (ori )#line:1295
        ori =CLEAN_qx (ori )#line:1296
        data =ori #line:1297
    if "光斑贴试验"in ori .columns and ini ["原始模式"]!="是":#line:1298
        text .insert (END ,"识别出为化妆品报表,正在进行数据规整...")#line:1299
        ini ["模式"]="化妆品"#line:1300
        ori =CLEAN_hzp (ori )#line:1301
        ori =CLEAN_qx (ori )#line:1302
        data =ori #line:1303
    if ini ["模式"]=="其他":#line:1306
        text .insert (END ,"\n数据读取成功，行数："+str (len (ori )))#line:1307
        data =ori #line:1308
        O000OO0OO00OO000O =Menu (root )#line:1309
        root .config (menu =O000OO0OO00OO000O )#line:1310
        try :#line:1311
            ini ["button"][0 ].pack_forget ()#line:1312
            ini ["button"][1 ].pack_forget ()#line:1313
            ini ["button"][2 ].pack_forget ()#line:1314
            ini ["button"][3 ].pack_forget ()#line:1315
            ini ["button"][4 ].pack_forget ()#line:1316
        except :#line:1317
            pass #line:1318
    else :#line:1320
        ini ["清洗后的文件"]=data #line:1321
        ini ["证号"]=Countall (data ).df_zhenghao ()#line:1322
        text .insert (END ,"\n数据读取成功，行数："+str (len (data )))#line:1323
        PROGRAM_Menubar (root ,data ,0 ,data )#line:1324
        try :#line:1325
            ini ["button"][0 ].pack_forget ()#line:1326
            ini ["button"][1 ].pack_forget ()#line:1327
            ini ["button"][2 ].pack_forget ()#line:1328
            ini ["button"][3 ].pack_forget ()#line:1329
            ini ["button"][4 ].pack_forget ()#line:1330
        except :#line:1331
            pass #line:1332
        O0O0OO0O00OO00OO0 =Button (frame0 ,text ="地市统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_org ("市级监测机构"),1 ,ori ),)#line:1343
        O0O0OO0O00OO00OO0 .pack ()#line:1344
        O0O0OO0O0OO0OOO00 =Button (frame0 ,text ="县区统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_org ("监测机构"),1 ,ori ),)#line:1357
        O0O0OO0O0OO0OOO00 .pack ()#line:1358
        OOO0O000OOOOOO000 =Button (frame0 ,text ="上报单位",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_user (),1 ,ori ),)#line:1371
        OOO0O000OOOOOO000 .pack ()#line:1372
        OO0000OOO00O0OO00 =Button (frame0 ,text ="生产企业",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_chiyouren (),1 ,ori ),)#line:1383
        OO0000OOO00O0OO00 .pack ()#line:1384
        O0O0OOO000OO0O000 =Button (frame0 ,text ="产品统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (ini ["证号"],1 ,ori ,ori ,"dfx_zhenghao"),)#line:1395
        O0O0OOO000OO0O000 .pack ()#line:1396
        ini ["button"]=[O0O0OO0O00OO00OO0 ,O0O0OO0O0OO0OOO00 ,OOO0O000OOOOOO000 ,OO0000OOO00O0OO00 ,O0O0OOO000OO0O000 ]#line:1397
    text .insert (END ,"\n")#line:1399
def TOOLS_sql (O0000000OOO0O0OO0 ):#line:1401
    ""#line:1402
    warnings .filterwarnings ("ignore")#line:1403
    try :#line:1404
        OO0O0OO0OOO000000 =O0000000OOO0O0OO0 .columns #line:1405
    except :#line:1406
        return 0 #line:1407
    def OO0O0OO000OOOO00O (O0OO0O000O0O0O000 ):#line:1409
        try :#line:1410
            O0OOO0O00OO000OOO =pd .read_sql_query (sqltext (O0OO0O000O0O0O000 ),con =OO0OO0O0OOO0O00O0 )#line:1411
        except :#line:1412
            showinfo (title ="提示",message ="SQL语句有误。")#line:1413
            return 0 #line:1414
        try :#line:1415
            del O0OOO0O00OO000OOO ["level_0"]#line:1416
        except :#line:1417
            pass #line:1418
        TABLE_tree_Level_2 (O0OOO0O00OO000OOO ,1 ,O0000000OOO0O0OO0 )#line:1419
    O000OOOOO0000OOOO ='sqlite://'#line:1423
    OO00OO0O0OO0OO0O0 =create_engine (O000OOOOO0000OOOO )#line:1424
    try :#line:1425
        O0000000OOO0O0OO0 .to_sql ('data',con =OO00OO0O0OO0OO0O0 ,chunksize =10000 ,if_exists ='replace',index =True )#line:1426
    except :#line:1427
        showinfo (title ="提示",message ="不支持该表格。")#line:1428
        return 0 #line:1429
    OO0OO0O0OOO0O00O0 =OO00OO0O0OO0OO0O0 .connect ()#line:1431
    O0OO00000OO0OO000 ="select * from data"#line:1432
    OO0O00O0O0OOO0O0O =Toplevel ()#line:1435
    OO0O00O0O0OOO0O0O .title ("SQL查询")#line:1436
    OO0O00O0O0OOO0O0O .geometry ("700x500")#line:1437
    O0O0OO00O000OO0O0 =ttk .Frame (OO0O00O0O0OOO0O0O ,width =700 ,height =20 )#line:1439
    O0O0OO00O000OO0O0 .pack (side =TOP )#line:1440
    O0OOO00OOO0000O00 =ttk .Frame (OO0O00O0O0OOO0O0O ,width =700 ,height =20 )#line:1441
    O0OOO00OOO0000O00 .pack (side =BOTTOM )#line:1442
    try :#line:1445
        OO0O00000O000O0OO =StringVar ()#line:1446
        OO0O00000O000O0OO .set ("select * from data WHERE 单位名称='佛山市第一人民医院'")#line:1447
        OO0OOO0OOOOO0O0OO =Label (O0O0OO00O000OO0O0 ,text ="SQL查询",anchor ='w')#line:1449
        OO0OOO0OOOOO0O0OO .pack (side =LEFT )#line:1450
        OOOO0OO0OOO0OOO00 =Label (O0O0OO00O000OO0O0 ,text ="检索：")#line:1451
        OOOOO00OO0000O0O0 =Button (O0OOO00OOO0000O00 ,text ="执行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",width =700 ,command =lambda :OO0O0OO000OOOO00O (OO0OOO0O0OO0OOO0O .get ("1.0","end")),)#line:1465
        OOOOO00OO0000O0O0 .pack (side =LEFT )#line:1466
    except EE :#line:1469
        pass #line:1470
    OO0O0OO00000O0OOO =Scrollbar (OO0O00O0O0OOO0O0O )#line:1472
    OO0OOO0O0OO0OOO0O =Text (OO0O00O0O0OOO0O0O ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1473
    OO0O0OO00000O0OOO .pack (side =RIGHT ,fill =Y )#line:1474
    OO0OOO0O0OO0OOO0O .pack ()#line:1475
    OO0O0OO00000O0OOO .config (command =OO0OOO0O0OO0OOO0O .yview )#line:1476
    OO0OOO0O0OO0OOO0O .config (yscrollcommand =OO0O0OO00000O0OOO .set )#line:1477
    def O0O0000O000O0OOOO (event =None ):#line:1478
        OO0OOO0O0OO0OOO0O .event_generate ('<<Copy>>')#line:1479
    def O0OO00OOO00O00O00 (event =None ):#line:1480
        OO0OOO0O0OO0OOO0O .event_generate ('<<Paste>>')#line:1481
    def O00O0O0O0O0OO00O0 (O00OOOO000O00O0OO ,O0OO00OOO00O0000O ):#line:1482
         TOOLS_savetxt (O00OOOO000O00O0OO ,O0OO00OOO00O0000O ,1 )#line:1483
    OOOOO000O0O00OO00 =Menu (OO0OOO0O0OO0OOO0O ,tearoff =False ,)#line:1484
    OOOOO000O0O00OO00 .add_command (label ="复制",command =O0O0000O000O0OOOO )#line:1485
    OOOOO000O0O00OO00 .add_command (label ="粘贴",command =O0OO00OOO00O00O00 )#line:1486
    OOOOO000O0O00OO00 .add_command (label ="源文件列",command =lambda :PROGRAM_helper (O0000000OOO0O0OO0 .columns .to_list ()))#line:1487
    def O0O0OOO000OOOO00O (OO000OOO00OO0O000 ):#line:1488
         OOOOO000O0O00OO00 .post (OO000OOO00OO0O000 .x_root ,OO000OOO00OO0O000 .y_root )#line:1489
    OO0OOO0O0OO0OOO0O .bind ("<Button-3>",O0O0OOO000OOOO00O )#line:1490
    OO0OOO0O0OO0OOO0O .insert (END ,O0OO00000OO0OO000 )#line:1494
def TOOLS_view_dict (O0O00O0O00OOOO0O0 ,OO0O0O0OO0O00000O ):#line:1498
    ""#line:1499
    OOOO00000O000OO00 =Toplevel ()#line:1500
    OOOO00000O000OO00 .title ("查看数据")#line:1501
    OOOO00000O000OO00 .geometry ("700x500")#line:1502
    O0O0000OO0OO0OOO0 =Scrollbar (OOOO00000O000OO00 )#line:1504
    OOO00OOO0O0O0O0OO =Text (OOOO00000O000OO00 ,height =100 ,width =150 )#line:1505
    O0O0000OO0OO0OOO0 .pack (side =RIGHT ,fill =Y )#line:1506
    OOO00OOO0O0O0O0OO .pack ()#line:1507
    O0O0000OO0OO0OOO0 .config (command =OOO00OOO0O0O0O0OO .yview )#line:1508
    OOO00OOO0O0O0O0OO .config (yscrollcommand =O0O0000OO0OO0OOO0 .set )#line:1509
    if OO0O0O0OO0O00000O ==1 :#line:1510
        OOO00OOO0O0O0O0OO .insert (END ,O0O00O0O00OOOO0O0 )#line:1512
        OOO00OOO0O0O0O0OO .insert (END ,"\n\n")#line:1513
        return 0 #line:1514
    for O000OOOOOOO00O000 in range (len (O0O00O0O00OOOO0O0 )):#line:1515
        OOO00OOO0O0O0O0OO .insert (END ,O0O00O0O00OOOO0O0 .iloc [O000OOOOOOO00O000 ,0 ])#line:1516
        OOO00OOO0O0O0O0OO .insert (END ,":")#line:1517
        OOO00OOO0O0O0O0OO .insert (END ,O0O00O0O00OOOO0O0 .iloc [O000OOOOOOO00O000 ,1 ])#line:1518
        OOO00OOO0O0O0O0OO .insert (END ,"\n\n")#line:1519
def TOOLS_save_dict (O0OOO00OOOOOOOOO0 ):#line:1521
    ""#line:1522
    OO000O0OOOOOO0000 =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="排序后的原始数据",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1528
    try :#line:1529
        O0OOO00OOOOOOOOO0 ["详细描述T"]=O0OOO00OOOOOOOOO0 ["详细描述T"].astype (str )#line:1530
    except :#line:1531
        pass #line:1532
    try :#line:1533
        O0OOO00OOOOOOOOO0 ["报告编码"]=O0OOO00OOOOOOOOO0 ["报告编码"].astype (str )#line:1534
    except :#line:1535
        pass #line:1536
    O0O0O00O0O0O0OO00 =pd .ExcelWriter (OO000O0OOOOOO0000 ,engine ="xlsxwriter")#line:1538
    O0OOO00OOOOOOOOO0 .to_excel (O0O0O00O0O0O0OO00 ,sheet_name ="字典数据")#line:1539
    O0O0O00O0O0O0OO00 .close ()#line:1540
    showinfo (title ="提示",message ="文件写入成功。")#line:1541
def TOOLS_savetxt (O00OOO0OO0O00O00O ,OO0O00O0O0OOO0O00 ,O0OO000OOO000OOOO ):#line:1543
	""#line:1544
	O0OOO0OOOO0OO00OO =open (OO0O00O0O0OOO0O00 ,"w",encoding ='utf-8')#line:1545
	O0OOO0OOOO0OO00OO .write (O00OOO0OO0O00O00O )#line:1546
	O0OOO0OOOO0OO00OO .flush ()#line:1548
	if O0OO000OOO000OOOO ==1 :#line:1549
		showinfo (title ="提示信息",message ="保存成功。")#line:1550
def TOOLS_deep_view (OO000O00OO0OOOO00 ,O0O00O00O00O0O000 ,OO00O0OOO00OO00O0 ,O00O00O0O0OOOO000 ):#line:1553
    ""#line:1554
    if O00O00O0O0OOOO000 ==0 :#line:1555
        try :#line:1556
            OO000O00OO0OOOO00 [O0O00O00O00O0O000 ]=OO000O00OO0OOOO00 [O0O00O00O00O0O000 ].fillna ("这个没有填写")#line:1557
        except :#line:1558
            pass #line:1559
        O0O0OO00O00O00O0O =OO000O00OO0OOOO00 .groupby (O0O00O00O00O0O000 ).agg (计数 =(OO00O0OOO00OO00O0 [0 ],OO00O0OOO00OO00O0 [1 ]))#line:1560
    if O00O00O0O0OOOO000 ==1 :#line:1561
            O0O0OO00O00O00O0O =pd .pivot_table (OO000O00OO0OOOO00 ,index =O0O00O00O00O0O000 [:-1 ],columns =O0O00O00O00O0O000 [-1 ],values =[OO00O0OOO00OO00O0 [0 ]],aggfunc ={OO00O0OOO00OO00O0 [0 ]:OO00O0OOO00OO00O0 [1 ]},fill_value ="0",margins =True ,dropna =False ,)#line:1572
            O0O0OO00O00O00O0O .columns =O0O0OO00O00O00O0O .columns .droplevel (0 )#line:1573
            O0O0OO00O00O00O0O =O0O0OO00O00O00O0O .rename (columns ={"All":"计数"})#line:1574
    if "日期"in O0O00O00O00O0O000 or "时间"in O0O00O00O00O0O000 or "季度"in O0O00O00O00O0O000 :#line:1577
        O0O0OO00O00O00O0O =O0O0OO00O00O00O0O .sort_values ([O0O00O00O00O0O000 ],ascending =False ,na_position ="last")#line:1580
    else :#line:1581
        O0O0OO00O00O00O0O =O0O0OO00O00O00O0O .sort_values (by =["计数"],ascending =False ,na_position ="last")#line:1585
    O0O0OO00O00O00O0O =O0O0OO00O00O00O0O .reset_index ()#line:1586
    O0O0OO00O00O00O0O ["构成比(%)"]=round (100 *O0O0OO00O00O00O0O ["计数"]/O0O0OO00O00O00O0O ["计数"].sum (),2 )#line:1587
    if O00O00O0O0OOOO000 ==0 :#line:1588
        O0O0OO00O00O00O0O ["报表类型"]="dfx_deepview"+"_"+str (O0O00O00O00O0O000 )#line:1589
    if O00O00O0O0OOOO000 ==1 :#line:1590
        O0O0OO00O00O00O0O ["报表类型"]="dfx_deepview"+"_"+str (O0O00O00O00O0O000 [:-1 ])#line:1591
    return O0O0OO00O00O00O0O #line:1592
def TOOLS_easyreadT (O00O00OO00OOO0OO0 ):#line:1596
    ""#line:1597
    O00O00OO00OOO0OO0 ["#####分隔符#########"]="######################################################################"#line:1600
    O0O0OOOO0O0000O0O =O00O00OO00OOO0OO0 .stack (dropna =False )#line:1601
    O0O0OOOO0O0000O0O =pd .DataFrame (O0O0OOOO0O0000O0O ).reset_index ()#line:1602
    O0O0OOOO0O0000O0O .columns =["序号","条目","详细描述T"]#line:1603
    O0O0OOOO0O0000O0O ["逐条查看"]="逐条查看"#line:1604
    return O0O0OOOO0O0000O0O #line:1605
def TOOLS_data_masking (OOO0OO0O0O0OO00O0 ):#line:1607
    ""#line:1608
    from random import choices #line:1609
    from string import ascii_letters ,digits #line:1610
    OOO0OO0O0O0OO00O0 =OOO0OO0O0O0OO00O0 .reset_index (drop =True )#line:1612
    if "单位名称.1"in OOO0OO0O0O0OO00O0 .columns :#line:1613
        OOOO0O0OOOOOO00O0 ="器械"#line:1614
    else :#line:1615
        OOOO0O0OOOOOO00O0 ="药品"#line:1616
    O000O0OOO00OO000O =peizhidir +""+"0（范例）数据脱敏"+".xls"#line:1617
    try :#line:1618
        O00OO00000OOO0OO0 =pd .read_excel (O000O0OOO00OO000O ,sheet_name =OOOO0O0OOOOOO00O0 ,header =0 ,index_col =0 ).reset_index ()#line:1621
    except :#line:1622
        showinfo (title ="错误信息",message ="该功能需要配置文件才能使用！")#line:1623
        return 0 #line:1624
    O0OO00OO00O0OO0OO =0 #line:1625
    O00OO00000OOOOO00 =len (OOO0OO0O0O0OO00O0 )#line:1626
    OOO0OO0O0O0OO00O0 ["abcd"]="□"#line:1627
    for O0000OOOO0OO0O0OO in O00OO00000OOO0OO0 ["要脱敏的列"]:#line:1628
        O0OO00OO00O0OO0OO =O0OO00OO00O0OO0OO +1 #line:1629
        PROGRAM_change_schedule (O0OO00OO00O0OO0OO ,O00OO00000OOOOO00 )#line:1630
        text .insert (END ,"\n正在对以下列进行脱敏处理：")#line:1631
        text .see (END )#line:1632
        text .insert (END ,O0000OOOO0OO0O0OO )#line:1633
        try :#line:1634
            OOOOO00O0OO0O0000 =set (OOO0OO0O0O0OO00O0 [O0000OOOO0OO0O0OO ])#line:1635
        except :#line:1636
            showinfo (title ="提示",message ="脱敏文件配置错误，请修改配置表。")#line:1637
            return 0 #line:1638
        OOOOOO00OO00OOO00 ={OOO0O000OOO00O0O0 :"".join (choices (digits ,k =10 ))for OOO0O000OOO00O0O0 in OOOOO00O0OO0O0000 }#line:1639
        OOO0OO0O0O0OO00O0 [O0000OOOO0OO0O0OO ]=OOO0OO0O0O0OO00O0 [O0000OOOO0OO0O0OO ].map (OOOOOO00OO00OOO00 )#line:1640
        OOO0OO0O0O0OO00O0 [O0000OOOO0OO0O0OO ]=OOO0OO0O0O0OO00O0 ["abcd"]+OOO0OO0O0O0OO00O0 [O0000OOOO0OO0O0OO ].astype (str )#line:1641
    try :#line:1642
        PROGRAM_change_schedule (10 ,10 )#line:1643
        del OOO0OO0O0O0OO00O0 ["abcd"]#line:1644
        O000000O0OOOOO0OO =filedialog .asksaveasfilename (title =u"保存脱敏后的文件",initialfile ="脱敏后的文件",defaultextension ="xlsx",filetypes =[("Excel 工作簿","*.xlsx"),("Excel 97-2003 工作簿","*.xls")],)#line:1650
        O0OO0OOO0OO00OO00 =pd .ExcelWriter (O000000O0OOOOO0OO ,engine ="xlsxwriter")#line:1651
        OOO0OO0O0O0OO00O0 .to_excel (O0OO0OOO0OO00OO00 ,sheet_name ="sheet0")#line:1652
        O0OO0OOO0OO00OO00 .close ()#line:1653
    except :#line:1654
        text .insert (END ,"\n文件未保存，但导入的数据已按要求脱敏。")#line:1655
    text .insert (END ,"\n脱敏操作完成。")#line:1656
    text .see (END )#line:1657
    return OOO0OO0O0O0OO00O0 #line:1658
def TOOLS_get_new (O00000OO000OOO0OO ,OOO0000O0O00O000O ):#line:1660
	""#line:1661
	def O0O000OO00OO0OO0O (OO0O00O0OOO0OO0OO ):#line:1662
		""#line:1663
		OO0O00O0OOO0OO0OO =OO0O00O0OOO0OO0OO .drop_duplicates ("报告编码")#line:1664
		O0O0OO000OO0000OO =str (Counter (TOOLS_get_list0 ("use(器械故障表现).file",OO0O00O0OOO0OO0OO ,1000 ))).replace ("Counter({","{")#line:1665
		O0O0OO000OO0000OO =O0O0OO000OO0000OO .replace ("})","}")#line:1666
		import ast #line:1667
		OOO0O0O0O0OOOOOOO =ast .literal_eval (O0O0OO000OO0000OO )#line:1668
		OO00OOO0OO00OO000 =TOOLS_easyreadT (pd .DataFrame ([OOO0O0O0O0OOOOOOO ]))#line:1669
		OO00OOO0OO00OO000 =OO00OOO0OO00OO000 .rename (columns ={"逐条查看":"ADR名称规整"})#line:1670
		return OO00OOO0OO00OO000 #line:1671
	if OOO0000O0O00O000O =="证号":#line:1672
		root .attributes ("-topmost",True )#line:1673
		root .attributes ("-topmost",False )#line:1674
		O0OOO0O00OOO0O00O =O00000OO000OOO0OO .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]).agg (计数 =("报告编码","nunique")).reset_index ()#line:1675
		OOO0O0O000O0OO000 =O0OOO0O00OOO0O00O .drop_duplicates ("注册证编号/曾用注册证编号").copy ()#line:1676
		OOO0O0O000O0OO000 ["所有不良反应"]=""#line:1677
		OOO0O0O000O0OO000 ["关注建议"]=""#line:1678
		OOO0O0O000O0OO000 ["疑似新的"]=""#line:1679
		OOO0O0O000O0OO000 ["疑似旧的"]=""#line:1680
		OOO0O0O000O0OO000 ["疑似新的（高敏）"]=""#line:1681
		OOO0O0O000O0OO000 ["疑似旧的（高敏）"]=""#line:1682
		OOOO0O0000O0OOO0O =1 #line:1683
		O0OO0000OO000OO0O =int (len (OOO0O0O000O0OO000 ))#line:1684
		for O0O000O0OOOO00OOO ,O00OOOO0OO0O0OOO0 in OOO0O0O000O0OO000 .iterrows ():#line:1685
			OO0O00OO0O0O00OOO =O00000OO000OOO0OO [(O00000OO000OOO0OO ["注册证编号/曾用注册证编号"]==O00OOOO0OO0O0OOO0 ["注册证编号/曾用注册证编号"])]#line:1686
			O0O0OO0O00O0O00OO =OO0O00OO0O0O00OOO .loc [OO0O00OO0O0O00OOO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1687
			O0O000OOO00OOO0OO =OO0O00OO0O0O00OOO .loc [~OO0O00OO0O0O00OOO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1688
			O00000OOO0000O00O =O0O000OO00OO0OO0O (O0O0OO0O00O0O00OO )#line:1689
			OO00OOOOOOOOOO000 =O0O000OO00OO0OO0O (O0O000OOO00OOO0OO )#line:1690
			O000000O0000OO0OO =O0O000OO00OO0OO0O (OO0O00OO0O0O00OOO )#line:1691
			PROGRAM_change_schedule (OOOO0O0000O0OOO0O ,O0OO0000OO000OO0O )#line:1692
			OOOO0O0000O0OOO0O =OOOO0O0000O0OOO0O +1 #line:1693
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in O000000O0000OO0OO .iterrows ():#line:1695
					if "分隔符"not in OO0000O00OOOO000O ["条目"]:#line:1696
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1697
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"所有不良反应"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"所有不良反应"]+O0OOO0O00OOOOO00O #line:1698
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in OO00OOOOOOOOOO000 .iterrows ():#line:1700
					if "分隔符"not in OO0000O00OOOO000O ["条目"]:#line:1701
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1702
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的"]+O0OOO0O00OOOOO00O #line:1703
					if "分隔符"not in OO0000O00OOOO000O ["条目"]and int (OO0000O00OOOO000O ["详细描述T"])>=2 :#line:1705
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1706
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的（高敏）"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的（高敏）"]+O0OOO0O00OOOOO00O #line:1707
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in O00000OOO0000O00O .iterrows ():#line:1709
				if str (OO0000O00OOOO000O ["条目"]).strip ()not in str (OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的"])and "分隔符"not in str (OO0000O00OOOO000O ["条目"]):#line:1710
					O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1711
					OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的"]+O0OOO0O00OOOOO00O #line:1712
					if int (OO0000O00OOOO000O ["详细描述T"])>=3 :#line:1713
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]+"！"#line:1714
					if int (OO0000O00OOOO000O ["详细描述T"])>=5 :#line:1715
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]+"●"#line:1716
				if str (OO0000O00OOOO000O ["条目"]).strip ()not in str (OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的（高敏）"])and "分隔符"not in str (OO0000O00OOOO000O ["条目"])and int (OO0000O00OOOO000O ["详细描述T"])>=2 :#line:1718
					O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1719
					OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的（高敏）"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的（高敏）"]+O0OOO0O00OOOOO00O #line:1720
		OOO0O0O000O0OO000 ["疑似新的"]="{"+OOO0O0O000O0OO000 ["疑似新的"]+"}"#line:1722
		OOO0O0O000O0OO000 ["疑似旧的"]="{"+OOO0O0O000O0OO000 ["疑似旧的"]+"}"#line:1723
		OOO0O0O000O0OO000 ["所有不良反应"]="{"+OOO0O0O000O0OO000 ["所有不良反应"]+"}"#line:1724
		OOO0O0O000O0OO000 ["疑似新的（高敏）"]="{"+OOO0O0O000O0OO000 ["疑似新的（高敏）"]+"}"#line:1725
		OOO0O0O000O0OO000 ["疑似旧的（高敏）"]="{"+OOO0O0O000O0OO000 ["疑似旧的（高敏）"]+"}"#line:1726
		OOO0O0O000O0OO000 =OOO0O0O000O0OO000 .rename (columns ={"器械待评价(药品新的报告比例)":"新的报告比例"})#line:1728
		OOO0O0O000O0OO000 =OOO0O0O000O0OO000 .rename (columns ={"严重伤害待评价比例(药品严重中新的比例)":"严重报告中新的比例"})#line:1729
		OOO0O0O000O0OO000 ["报表类型"]="dfx_zhenghao"#line:1730
		TABLE_tree_Level_2 (OOO0O0O000O0OO000 .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,O00000OO000OOO0OO )#line:1731
	if OOO0000O0O00O000O =="品种":#line:1732
		root .attributes ("-topmost",True )#line:1733
		root .attributes ("-topmost",False )#line:1734
		O0OOO0O00OOO0O00O =O00000OO000OOO0OO .groupby (["产品类别","产品名称"]).agg (计数 =("报告编码","nunique")).reset_index ()#line:1735
		OOO0O0O000O0OO000 =O0OOO0O00OOO0O00O .drop_duplicates ("产品名称").copy ()#line:1736
		OOO0O0O000O0OO000 ["产品名称"]=OOO0O0O000O0OO000 ["产品名称"].str .replace ("*","",regex =False )#line:1737
		OOO0O0O000O0OO000 ["所有不良反应"]=""#line:1738
		OOO0O0O000O0OO000 ["关注建议"]=""#line:1739
		OOO0O0O000O0OO000 ["疑似新的"]=""#line:1740
		OOO0O0O000O0OO000 ["疑似旧的"]=""#line:1741
		OOO0O0O000O0OO000 ["疑似新的（高敏）"]=""#line:1742
		OOO0O0O000O0OO000 ["疑似旧的（高敏）"]=""#line:1743
		OOOO0O0000O0OOO0O =1 #line:1744
		O0OO0000OO000OO0O =int (len (OOO0O0O000O0OO000 ))#line:1745
		for O0O000O0OOOO00OOO ,O00OOOO0OO0O0OOO0 in OOO0O0O000O0OO000 .iterrows ():#line:1748
			OO0O00OO0O0O00OOO =O00000OO000OOO0OO [(O00000OO000OOO0OO ["产品名称"]==O00OOOO0OO0O0OOO0 ["产品名称"])]#line:1750
			O0O0OO0O00O0O00OO =OO0O00OO0O0O00OOO .loc [OO0O00OO0O0O00OOO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1752
			O0O000OOO00OOO0OO =OO0O00OO0O0O00OOO .loc [~OO0O00OO0O0O00OOO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1753
			O000000O0000OO0OO =O0O000OO00OO0OO0O (OO0O00OO0O0O00OOO )#line:1754
			O00000OOO0000O00O =O0O000OO00OO0OO0O (O0O0OO0O00O0O00OO )#line:1755
			OO00OOOOOOOOOO000 =O0O000OO00OO0OO0O (O0O000OOO00OOO0OO )#line:1756
			PROGRAM_change_schedule (OOOO0O0000O0OOO0O ,O0OO0000OO000OO0O )#line:1757
			OOOO0O0000O0OOO0O =OOOO0O0000O0OOO0O +1 #line:1758
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in O000000O0000OO0OO .iterrows ():#line:1760
					if "分隔符"not in OO0000O00OOOO000O ["条目"]:#line:1761
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1762
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"所有不良反应"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"所有不良反应"]+O0OOO0O00OOOOO00O #line:1763
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in OO00OOOOOOOOOO000 .iterrows ():#line:1766
					if "分隔符"not in OO0000O00OOOO000O ["条目"]:#line:1767
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1768
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的"]+O0OOO0O00OOOOO00O #line:1769
					if "分隔符"not in OO0000O00OOOO000O ["条目"]and int (OO0000O00OOOO000O ["详细描述T"])>=2 :#line:1771
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1772
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的（高敏）"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的（高敏）"]+O0OOO0O00OOOOO00O #line:1773
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in O00000OOO0000O00O .iterrows ():#line:1775
				if str (OO0000O00OOOO000O ["条目"]).strip ()not in str (OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的"])and "分隔符"not in str (OO0000O00OOOO000O ["条目"]):#line:1776
					O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1777
					OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的"]+O0OOO0O00OOOOO00O #line:1778
					if int (OO0000O00OOOO000O ["详细描述T"])>=3 :#line:1779
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]+"！"#line:1780
					if int (OO0000O00OOOO000O ["详细描述T"])>=5 :#line:1781
						OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"关注建议"]+"●"#line:1782
				if str (OO0000O00OOOO000O ["条目"]).strip ()not in str (OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似旧的（高敏）"])and "分隔符"not in str (OO0000O00OOOO000O ["条目"])and int (OO0000O00OOOO000O ["详细描述T"])>=2 :#line:1784
					O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1785
					OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的（高敏）"]=OOO0O0O000O0OO000 .loc [O0O000O0OOOO00OOO ,"疑似新的（高敏）"]+O0OOO0O00OOOOO00O #line:1786
		OOO0O0O000O0OO000 ["疑似新的"]="{"+OOO0O0O000O0OO000 ["疑似新的"]+"}"#line:1788
		OOO0O0O000O0OO000 ["疑似旧的"]="{"+OOO0O0O000O0OO000 ["疑似旧的"]+"}"#line:1789
		OOO0O0O000O0OO000 ["所有不良反应"]="{"+OOO0O0O000O0OO000 ["所有不良反应"]+"}"#line:1790
		OOO0O0O000O0OO000 ["疑似新的（高敏）"]="{"+OOO0O0O000O0OO000 ["疑似新的（高敏）"]+"}"#line:1791
		OOO0O0O000O0OO000 ["疑似旧的（高敏）"]="{"+OOO0O0O000O0OO000 ["疑似旧的（高敏）"]+"}"#line:1792
		OOO0O0O000O0OO000 ["报表类型"]="dfx_chanpin"#line:1793
		TABLE_tree_Level_2 (OOO0O0O000O0OO000 .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,O00000OO000OOO0OO )#line:1794
	if OOO0000O0O00O000O =="页面":#line:1796
		O0000O0O0OO00O0OO =""#line:1797
		OOO0OOOO00OO0O00O =""#line:1798
		O0O0OO0O00O0O00OO =O00000OO000OOO0OO .loc [O00000OO000OOO0OO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1799
		O0O000OOO00OOO0OO =O00000OO000OOO0OO .loc [~O00000OO000OOO0OO ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1800
		O00000OOO0000O00O =O0O000OO00OO0OO0O (O0O0OO0O00O0O00OO )#line:1801
		OO00OOOOOOOOOO000 =O0O000OO00OO0OO0O (O0O000OOO00OOO0OO )#line:1802
		if 1 ==1 :#line:1803
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in OO00OOOOOOOOOO000 .iterrows ():#line:1804
					if "分隔符"not in OO0000O00OOOO000O ["条目"]:#line:1805
						O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1806
						OOO0OOOO00OO0O00O =OOO0OOOO00OO0O00O +O0OOO0O00OOOOO00O #line:1807
			for O000O00OO0OO00000 ,OO0000O00OOOO000O in O00000OOO0000O00O .iterrows ():#line:1808
				if str (OO0000O00OOOO000O ["条目"]).strip ()not in OOO0OOOO00OO0O00O and "分隔符"not in str (OO0000O00OOOO000O ["条目"]):#line:1809
					O0OOO0O00OOOOO00O ="'"+str (OO0000O00OOOO000O ["条目"])+"':"+str (OO0000O00OOOO000O ["详细描述T"])+","#line:1810
					O0000O0O0OO00O0OO =O0000O0O0OO00O0OO +O0OOO0O00OOOOO00O #line:1811
		OOO0OOOO00OO0O00O ="{"+OOO0OOOO00OO0O00O +"}"#line:1812
		O0000O0O0OO00O0OO ="{"+O0000O0O0OO00O0OO +"}"#line:1813
		O00O0OO00OOO000O0 ="\n可能是新的不良反应：\n\n"+O0000O0O0OO00O0OO +"\n\n\n可能不是新的不良反应：\n\n"+OOO0OOOO00OO0O00O #line:1814
		TOOLS_view_dict (O00O0OO00OOO000O0 ,1 )#line:1815
def TOOLS_strdict_to_pd (OOOOOOOOO000O0000 ):#line:1817
	""#line:1818
	return pd .DataFrame .from_dict (eval (OOOOOOOOO000O0000 ),orient ="index",columns =["content"]).reset_index ()#line:1819
def TOOLS_xuanze (O0OOO0O0OOOOO00OO ,OO0OOOO0OOOOOOOO0 ):#line:1821
    ""#line:1822
    if OO0OOOO0OOOOOOOO0 ==0 :#line:1823
        OOO00O00O0O0O000O =pd .read_excel (filedialog .askopenfilename (filetypes =[("XLS",".xls")]),sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1824
    else :#line:1825
        OOO00O00O0O0O000O =pd .read_excel (peizhidir +"0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1826
    O0OOO0O0OOOOO00OO ["temppr"]=""#line:1827
    for O00O0OOOOOO0O000O in OOO00O00O0O0O000O .columns .tolist ():#line:1828
        O0OOO0O0OOOOO00OO ["temppr"]=O0OOO0O0OOOOO00OO ["temppr"]+"----"+O0OOO0O0OOOOO00OO [O00O0OOOOOO0O000O ]#line:1829
    O00OOO0O000O00O00 ="测试字段MMMMM"#line:1830
    for O00O0OOOOOO0O000O in OOO00O00O0O0O000O .columns .tolist ():#line:1831
        for O0OO0OO00000OOOO0 in OOO00O00O0O0O000O [O00O0OOOOOO0O000O ].drop_duplicates ():#line:1833
            if O0OO0OO00000OOOO0 :#line:1834
                O00OOO0O000O00O00 =O00OOO0O000O00O00 +"|"+str (O0OO0OO00000OOOO0 )#line:1835
    O0OOO0O0OOOOO00OO =O0OOO0O0OOOOO00OO .loc [O0OOO0O0OOOOO00OO ["temppr"].str .contains (O00OOO0O000O00O00 ,na =False )].copy ()#line:1836
    del O0OOO0O0OOOOO00OO ["temppr"]#line:1837
    O0OOO0O0OOOOO00OO =O0OOO0O0OOOOO00OO .reset_index (drop =True )#line:1838
    TABLE_tree_Level_2 (O0OOO0O0OOOOO00OO ,0 ,O0OOO0O0OOOOO00OO )#line:1840
def TOOLS_add_c (OO000O00OO0OO0O0O ,O0OO00000OO00OO00 ):#line:1842
			OO000O00OO0OO0O0O ["关键字查找列o"]=""#line:1843
			for O0O00O00O00OO000O in TOOLS_get_list (O0OO00000OO00OO00 ["查找列"]):#line:1844
				OO000O00OO0OO0O0O ["关键字查找列o"]=OO000O00OO0OO0O0O ["关键字查找列o"]+OO000O00OO0OO0O0O [O0O00O00O00OO000O ].astype ("str")#line:1845
			if O0OO00000OO00OO00 ["条件"]=="等于":#line:1846
				OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O [O0OO00000OO00OO00 ["查找列"]].astype (str )==str (O0OO00000OO00OO00 ["条件值"])),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1847
			if O0OO00000OO00OO00 ["条件"]=="大于":#line:1848
				OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O [O0OO00000OO00OO00 ["查找列"]].astype (float )>O0OO00000OO00OO00 ["条件值"]),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1849
			if O0OO00000OO00OO00 ["条件"]=="小于":#line:1850
				OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O [O0OO00000OO00OO00 ["查找列"]].astype (float )<O0OO00000OO00OO00 ["条件值"]),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1851
			if O0OO00000OO00OO00 ["条件"]=="介于":#line:1852
				OO0O000OO00OO0OOO =TOOLS_get_list (O0OO00000OO00OO00 ["条件值"])#line:1853
				OO000O00OO0OO0O0O .loc [((OO000O00OO0OO0O0O [O0OO00000OO00OO00 ["查找列"]].astype (float )<float (OO0O000OO00OO0OOO [1 ]))&(OO000O00OO0OO0O0O [O0OO00000OO00OO00 ["查找列"]].astype (float )>float (OO0O000OO00OO0OOO [0 ]))),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1854
			if O0OO00000OO00OO00 ["条件"]=="不含":#line:1855
				OO000O00OO0OO0O0O .loc [(~OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (O0OO00000OO00OO00 ["条件值"])),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1856
			if O0OO00000OO00OO00 ["条件"]=="包含":#line:1857
				OO000O00OO0OO0O0O .loc [OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (O0OO00000OO00OO00 ["条件值"],na =False ),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1858
			if O0OO00000OO00OO00 ["条件"]=="同时包含":#line:1859
				OO0OO000O0000O0O0 =TOOLS_get_list0 (O0OO00000OO00OO00 ["条件值"],0 )#line:1860
				if len (OO0OO000O0000O0O0 )==1 :#line:1861
				    OO000O00OO0OO0O0O .loc [OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [0 ],na =False ),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1862
				if len (OO0OO000O0000O0O0 )==2 :#line:1863
				    OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [0 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [1 ],na =False )),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1864
				if len (OO0OO000O0000O0O0 )==3 :#line:1865
				    OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [0 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [1 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [2 ],na =False )),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1866
				if len (OO0OO000O0000O0O0 )==4 :#line:1867
				    OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [0 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [1 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [2 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [3 ],na =False )),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1868
				if len (OO0OO000O0000O0O0 )==5 :#line:1869
				    OO000O00OO0OO0O0O .loc [(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [0 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [1 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [2 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [3 ],na =False ))&(OO000O00OO0OO0O0O ["关键字查找列o"].str .contains (OO0OO000O0000O0O0 [4 ],na =False )),O0OO00000OO00OO00 ["赋值列名"]]=O0OO00000OO00OO00 ["赋值"]#line:1870
			return OO000O00OO0OO0O0O #line:1871
def TOOL_guizheng (OO0OO0OO0O00OO00O ,OO0O00O0OO0O00O0O ,O0OO000OO0OOOOOO0 ):#line:1874
	""#line:1875
	if OO0O00O0OO0O00O0O ==0 :#line:1876
		OO00000OOOOOOO00O =pd .read_excel (filedialog .askopenfilename (filetypes =[("XLSX",".xlsx")]),sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1877
		OO00000OOOOOOO00O =OO00000OOOOOOO00O [(OO00000OOOOOOO00O ["执行标记"]=="是")].reset_index ()#line:1878
		for OOOOO0O00OOO0OOO0 ,O0000O0OO000O0OOO in OO00000OOOOOOO00O .iterrows ():#line:1879
			OO0OO0OO0O00OO00O =TOOLS_add_c (OO0OO0OO0O00OO00O ,O0000O0OO000O0OOO )#line:1880
		del OO0OO0OO0O00OO00O ["关键字查找列o"]#line:1881
	elif OO0O00O0OO0O00O0O ==1 :#line:1883
		OO00000OOOOOOO00O =pd .read_excel (peizhidir +"0（范例）数据规整.xlsx",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1884
		OO00000OOOOOOO00O =OO00000OOOOOOO00O [(OO00000OOOOOOO00O ["执行标记"]=="是")].reset_index ()#line:1885
		for OOOOO0O00OOO0OOO0 ,O0000O0OO000O0OOO in OO00000OOOOOOO00O .iterrows ():#line:1886
			OO0OO0OO0O00OO00O =TOOLS_add_c (OO0OO0OO0O00OO00O ,O0000O0OO000O0OOO )#line:1887
		del OO0OO0OO0O00OO00O ["关键字查找列o"]#line:1888
	elif OO0O00O0OO0O00O0O =="课题":#line:1890
		OO00000OOOOOOO00O =pd .read_excel (peizhidir +"0（范例）品类规整.xlsx",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1891
		OO00000OOOOOOO00O =OO00000OOOOOOO00O [(OO00000OOOOOOO00O ["执行标记"]=="是")].reset_index ()#line:1892
		for OOOOO0O00OOO0OOO0 ,O0000O0OO000O0OOO in OO00000OOOOOOO00O .iterrows ():#line:1893
			OO0OO0OO0O00OO00O =TOOLS_add_c (OO0OO0OO0O00OO00O ,O0000O0OO000O0OOO )#line:1894
		del OO0OO0OO0O00OO00O ["关键字查找列o"]#line:1895
	elif OO0O00O0OO0O00O0O ==2 :#line:1897
		text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:1898
		OOO0O00OOO0O0OO0O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:1899
		O0O0O000O000O0O00 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:1900
		OOOOO0O0O00OO00OO =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:1901
		for OOOOO0O00OOO0OOO0 ,O0000O0OO000O0OOO in OOO0O00OOO0O0OO0O .iterrows ():#line:1902
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["曾用名1"]),"单位名称"]=O0000O0OO000O0OOO ["单位名称"]#line:1903
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["曾用名2"]),"单位名称"]=O0000O0OO000O0OOO ["单位名称"]#line:1904
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["曾用名3"]),"单位名称"]=O0000O0OO000O0OOO ["单位名称"]#line:1905
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["曾用名4"]),"单位名称"]=O0000O0OO000O0OOO ["单位名称"]#line:1906
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["曾用名5"]),"单位名称"]=O0000O0OO000O0OOO ["单位名称"]#line:1907
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["单位名称"]),"医疗机构类别"]=O0000O0OO000O0OOO ["医疗机构类别"]#line:1909
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["单位名称"]),"监测机构"]=O0000O0OO000O0OOO ["监测机构"]#line:1910
		for OOOOO0O00OOO0OOO0 ,O0000O0OO000O0OOO in O0O0O000O000O0O00 .iterrows ():#line:1912
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["监测机构"]==O0000O0OO000O0OOO ["曾用名1"]),"监测机构"]=O0000O0OO000O0OOO ["监测机构"]#line:1913
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["监测机构"]==O0000O0OO000O0OOO ["曾用名2"]),"监测机构"]=O0000O0OO000O0OOO ["监测机构"]#line:1914
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["监测机构"]==O0000O0OO000O0OOO ["曾用名3"]),"监测机构"]=O0000O0OO000O0OOO ["监测机构"]#line:1915
		for OO00OOOOO0OO0OO0O in OOOOO0O0O00OO00OO ["地市列表"]:#line:1917
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["上报单位所属地区"].str .contains (OO00OOOOO0OO0OO0O ,na =False )),"市级监测机构"]=OO00OOOOO0OO0OO0O #line:1918
		OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:1921
		OO0OO0OO0O00OO00O ["市级监测机构"]=OO0OO0OO0O00OO00O ["市级监测机构"].fillna ("-未规整的-")#line:1922
	elif OO0O00O0OO0O00O0O ==3 :#line:1924
			OO00000OOO0OOOO0O =(OO0OO0OO0O00OO00O .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]).aggregate ({"报告编码":"count"}).reset_index ())#line:1929
			OO00000OOO0OOOO0O =OO00000OOO0OOOO0O .sort_values (by =["注册证编号/曾用注册证编号","报告编码"],ascending =[False ,False ],na_position ="last").reset_index ()#line:1932
			text .insert (END ,"\n开展产品名称规整..")#line:1933
			del OO00000OOO0OOOO0O ["报告编码"]#line:1934
			OO00000OOO0OOOO0O =OO00000OOO0OOOO0O .drop_duplicates (["注册证编号/曾用注册证编号"])#line:1935
			OO0OO0OO0O00OO00O =OO0OO0OO0O00OO00O .rename (columns ={"上市许可持有人名称":"上市许可持有人名称（规整前）","产品类别":"产品类别（规整前）","产品名称":"产品名称（规整前）"})#line:1937
			OO0OO0OO0O00OO00O =pd .merge (OO0OO0OO0O00OO00O ,OO00000OOO0OOOO0O ,on =["注册证编号/曾用注册证编号"],how ="left")#line:1938
	elif OO0O00O0OO0O00O0O ==4 :#line:1940
		text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:1941
		O0O0O000O000O0O00 =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:1942
		for OOOOO0O00OOO0OOO0 ,O0000O0OO000O0OOO in O0O0O000O000O0O00 .iterrows ():#line:1944
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["中文全称"]),"监测机构"]=O0000O0OO000O0OOO ["归属地区"]#line:1945
			OO0OO0OO0O00OO00O .loc [(OO0OO0OO0O00OO00O ["单位名称"]==O0000O0OO000O0OOO ["中文全称"]),"市级监测机构"]=O0000O0OO000O0OOO ["地市"]#line:1946
		OO0OO0OO0O00OO00O ["监测机构"]=OO0OO0OO0O00OO00O ["监测机构"].fillna ("未规整")#line:1947
		OO0OO0OO0O00OO00O ["市级监测机构"]=OO0OO0OO0O00OO00O ["市级监测机构"].fillna ("未规整")#line:1948
	if O0OO000OO0OOOOOO0 ==True :#line:1949
		return OO0OO0OO0O00OO00O #line:1950
	else :#line:1951
		TABLE_tree_Level_2 (OO0OO0OO0O00OO00O ,0 ,OO0OO0OO0O00OO00O )#line:1952
def TOOL_person (O0O0OO0O0000O0O0O ):#line:1954
	""#line:1955
	OO00O0O0000O0O0O0 =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="专家列表",header =0 ,index_col =0 ,).reset_index ()#line:1956
	for O000OOO0000O0OO00 ,O00OO0O000O0OO00O in OO00O0O0000O0O0O0 .iterrows ():#line:1957
		O0O0OO0O0000O0O0O .loc [(O0O0OO0O0000O0O0O ["市级监测机构"]==O00OO0O000O0OO00O ["市级监测机构"]),"评表人员"]=O00OO0O000O0OO00O ["评表人员"]#line:1958
		O0O0OO0O0000O0O0O ["评表人员"]=O0O0OO0O0000O0O0O ["评表人员"].fillna ("未规整")#line:1959
		O00OO0OOOO0O00O0O =O0O0OO0O0000O0O0O .groupby (["评表人员"]).agg (报告数量 =("报告编码","nunique"),地市 =("市级监测机构",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:1963
	TABLE_tree_Level_2 (O00OO0OOOO0O00O0O ,0 ,O00OO0OOOO0O00O0O )#line:1964
def TOOLS_get_list (O0OOOO0OO0OOOOO00 ):#line:1966
    ""#line:1967
    O0OOOO0OO0OOOOO00 =str (O0OOOO0OO0OOOOO00 )#line:1968
    O00O00O0O0OO00OO0 =[]#line:1969
    O00O00O0O0OO00OO0 .append (O0OOOO0OO0OOOOO00 )#line:1970
    O00O00O0O0OO00OO0 =",".join (O00O00O0O0OO00OO0 )#line:1971
    O00O00O0O0OO00OO0 =O00O00O0O0OO00OO0 .split ("|")#line:1972
    OO0OO0000OOOO000O =O00O00O0O0OO00OO0 [:]#line:1973
    O00O00O0O0OO00OO0 =list (set (O00O00O0O0OO00OO0 ))#line:1974
    O00O00O0O0OO00OO0 .sort (key =OO0OO0000OOOO000O .index )#line:1975
    return O00O00O0O0OO00OO0 #line:1976
def TOOLS_get_list0 (O0O00000OO000O000 ,OOOO00O0O0O0OOOOO ,*O0O000O0OO0OO0O0O ):#line:1978
    ""#line:1979
    O0O00000OO000O000 =str (O0O00000OO000O000 )#line:1980
    if pd .notnull (O0O00000OO000O000 ):#line:1982
        try :#line:1983
            if "use("in str (O0O00000OO000O000 ):#line:1984
                OOO0O00O00O00OOO0 =O0O00000OO000O000 #line:1985
                O0O00O0OO00O0O00O =re .compile (r"[(](.*?)[)]",re .S )#line:1986
                OOO0O00OO00O0OOO0 =re .findall (O0O00O0OO00O0O00O ,OOO0O00O00O00OOO0 )#line:1987
                O000000O0O0O0O0O0 =[]#line:1988
                if ").list"in O0O00000OO000O000 :#line:1989
                    O0O0O00O00O0OOOOO =peizhidir +""+str (OOO0O00OO00O0OOO0 [0 ])+".xls"#line:1990
                    O00OOO000000OOO0O =pd .read_excel (O0O0O00O00O0OOOOO ,sheet_name =OOO0O00OO00O0OOO0 [0 ],header =0 ,index_col =0 ).reset_index ()#line:1993
                    O00OOO000000OOO0O ["检索关键字"]=O00OOO000000OOO0O ["检索关键字"].astype (str )#line:1994
                    O000000O0O0O0O0O0 =O00OOO000000OOO0O ["检索关键字"].tolist ()+O000000O0O0O0O0O0 #line:1995
                if ").file"in O0O00000OO000O000 :#line:1996
                    O000000O0O0O0O0O0 =OOOO00O0O0O0OOOOO [OOO0O00OO00O0OOO0 [0 ]].astype (str ).tolist ()+O000000O0O0O0O0O0 #line:1998
                try :#line:2001
                    if "报告类型-新的"in OOOO00O0O0O0OOOOO .columns :#line:2002
                        O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2003
                        O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split (";")#line:2004
                        O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2005
                        O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split ("；")#line:2006
                        O000000O0O0O0O0O0 =[OO000O000OO00OO0O .replace ("（严重）","")for OO000O000OO00OO0O in O000000O0O0O0O0O0 ]#line:2007
                        O000000O0O0O0O0O0 =[OO0O0OOO0O00000OO .replace ("（一般）","")for OO0O0OOO0O00000OO in O000000O0O0O0O0O0 ]#line:2008
                except :#line:2009
                    pass #line:2010
                O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2013
                O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split ("、")#line:2014
                O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2015
                O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split ("，")#line:2016
                O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2017
                O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split (",")#line:2018
                O0OO00OOOOO00O0OO =O000000O0O0O0O0O0 [:]#line:2020
                try :#line:2021
                    if O0O000O0OO0OO0O0O [0 ]==1000 :#line:2022
                      pass #line:2023
                except :#line:2024
                      O000000O0O0O0O0O0 =list (set (O000000O0O0O0O0O0 ))#line:2025
                O000000O0O0O0O0O0 .sort (key =O0OO00OOOOO00O0OO .index )#line:2026
            else :#line:2028
                O0O00000OO000O000 =str (O0O00000OO000O000 )#line:2029
                O000000O0O0O0O0O0 =[]#line:2030
                O000000O0O0O0O0O0 .append (O0O00000OO000O000 )#line:2031
                O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2032
                O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split ("、")#line:2033
                O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2034
                O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split ("，")#line:2035
                O000000O0O0O0O0O0 =",".join (O000000O0O0O0O0O0 )#line:2036
                O000000O0O0O0O0O0 =O000000O0O0O0O0O0 .split (",")#line:2037
                O0OO00OOOOO00O0OO =O000000O0O0O0O0O0 [:]#line:2039
                try :#line:2040
                    if O0O000O0OO0OO0O0O [0 ]==1000 :#line:2041
                      O000000O0O0O0O0O0 =list (set (O000000O0O0O0O0O0 ))#line:2042
                except :#line:2043
                      pass #line:2044
                O000000O0O0O0O0O0 .sort (key =O0OO00OOOOO00O0OO .index )#line:2045
                O000000O0O0O0O0O0 .sort (key =O0OO00OOOOO00O0OO .index )#line:2046
        except ValueError2 :#line:2048
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:2049
            return False #line:2050
    return O000000O0O0O0O0O0 #line:2052
def TOOLS_easyread2 (O00OO0OO0O0000O00 ):#line:2054
    ""#line:2055
    O00OO0OO0O0000O00 ["分隔符"]="●"#line:2057
    O00OO0OO0O0000O00 ["上报机构描述"]=(O00OO0OO0O0000O00 ["使用过程"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["事件原因分析"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["事件原因分析描述"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["初步处置情况"].astype ("str"))#line:2066
    O00OO0OO0O0000O00 ["持有人处理描述"]=(O00OO0OO0O0000O00 ["关联性评价"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["调查情况"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["事件原因分析"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["具体控制措施"].astype ("str")+O00OO0OO0O0000O00 ["分隔符"]+O00OO0OO0O0000O00 ["未采取控制措施原因"].astype ("str"))#line:2077
    OOOO0000OO000OO0O =O00OO0OO0O0000O00 [["报告编码","事件发生日期","报告日期","单位名称","产品名称","注册证编号/曾用注册证编号","产品批号","型号","规格","上市许可持有人名称","管理类别","伤害","伤害表现","器械故障表现","上报机构描述","持有人处理描述","经营企业使用单位报告状态","监测机构","产品类别","医疗机构类别","年龄","年龄类型","性别"]]#line:2104
    OOOO0000OO000OO0O =OOOO0000OO000OO0O .sort_values (by =["事件发生日期"],ascending =[False ],na_position ="last",)#line:2109
    OOOO0000OO000OO0O =OOOO0000OO000OO0O .rename (columns ={"报告编码":"规整编码"})#line:2110
    return OOOO0000OO000OO0O #line:2111
def fenci0 (OOO0O0O0000O0O0OO ):#line:2114
	""#line:2115
	OO0O0OO0O00O0OOOO =Toplevel ()#line:2116
	OO0O0OO0O00O0OOOO .title ('词频统计')#line:2117
	O0OO0O0O0O000O0OO =OO0O0OO0O00O0OOOO .winfo_screenwidth ()#line:2118
	O00OO00O000000000 =OO0O0OO0O00O0OOOO .winfo_screenheight ()#line:2120
	O000O0O0OOOOO0O00 =400 #line:2122
	OO0O0O0O000000O00 =120 #line:2123
	O00O0OOOOO0OO0OOO =(O0OO0O0O0O000O0OO -O000O0O0OOOOO0O00 )/2 #line:2125
	O0OOOOO0OOO00OOOO =(O00OO00O000000000 -OO0O0O0O000000O00 )/2 #line:2126
	OO0O0OO0O00O0OOOO .geometry ("%dx%d+%d+%d"%(O000O0O0OOOOO0O00 ,OO0O0O0O000000O00 ,O00O0OOOOO0OO0OOO ,O0OOOOO0OOO00OOOO ))#line:2127
	OOO0000O00O000O00 =Label (OO0O0OO0O00O0OOOO ,text ="配置文件：")#line:2128
	OOO0000O00O000O00 .pack ()#line:2129
	O000OOOOO0000OOO0 =Label (OO0O0OO0O00O0OOOO ,text ="需要分词的列：")#line:2130
	OO0OO0000OO0OOO00 =Entry (OO0O0OO0O00O0OOOO ,width =80 )#line:2132
	OO0OO0000OO0OOO00 .insert (0 ,peizhidir +"0（范例）中文分词工作文件.xls")#line:2133
	O0O000O0O00O00000 =Entry (OO0O0OO0O00O0OOOO ,width =80 )#line:2134
	O0O000O0O00O00000 .insert (0 ,"器械故障表现，伤害表现")#line:2135
	OO0OO0000OO0OOO00 .pack ()#line:2136
	O000OOOOO0000OOO0 .pack ()#line:2137
	O0O000O0O00O00000 .pack ()#line:2138
	O00OOO0OO000OOO00 =LabelFrame (OO0O0OO0O00O0OOOO )#line:2139
	O0OO00000O0OOO0O0 =Button (O00OOO0OO000OOO00 ,text ="确定",width =10 ,command =lambda :PROGRAM_thread_it (tree_Level_2 ,fenci (OO0OO0000OO0OOO00 .get (),O0O000O0O00O00000 .get (),OOO0O0O0000O0O0OO ),1 ,0 ))#line:2140
	O0OO00000O0OOO0O0 .pack (side =LEFT ,padx =1 ,pady =1 )#line:2141
	O00OOO0OO000OOO00 .pack ()#line:2142
def fenci (O0O0OOO0OOOOO0OO0 ,OOO00O0O00000OOOO ,O0OO0O00000OO0000 ):#line:2144
    ""#line:2145
    import glob #line:2146
    import jieba #line:2147
    import random #line:2148
    try :#line:2150
        O0OO0O00000OO0000 =O0OO0O00000OO0000 .drop_duplicates (["报告编码"])#line:2151
    except :#line:2152
        pass #line:2153
    def OO0OOOO0OOO00OO00 (OOOO0O000O0OO0OOO ,O0O000OO0OO0000O0 ):#line:2154
        O0O0OO0O0OOOOO00O ={}#line:2155
        for OO0OOO000O0O0O00O in OOOO0O000O0OO0OOO :#line:2156
            O0O0OO0O0OOOOO00O [OO0OOO000O0O0O00O ]=O0O0OO0O0OOOOO00O .get (OO0OOO000O0O0O00O ,0 )+1 #line:2157
        return sorted (O0O0OO0O0OOOOO00O .items (),key =lambda O0O00O000OO0OOO00 :O0O00O000OO0OOO00 [1 ],reverse =True )[:O0O000OO0OO0000O0 ]#line:2158
    OO000O0000OO0O0O0 =pd .read_excel (O0O0OOO0OOOOO0OO0 ,sheet_name ="初始化",header =0 ,index_col =0 ).reset_index ()#line:2162
    OOOOO0O0O0O0000OO =OO000O0000OO0O0O0 .iloc [0 ,2 ]#line:2164
    OOOOO0O00O0OO0OO0 =pd .read_excel (O0O0OOO0OOOOO0OO0 ,sheet_name ="停用词",header =0 ,index_col =0 ).reset_index ()#line:2167
    OOOOO0O00O0OO0OO0 ["停用词"]=OOOOO0O00O0OO0OO0 ["停用词"].astype (str )#line:2169
    OOO00OO00O00O0000 =[OOO0O0O000O0OO0OO .strip ()for OOO0O0O000O0OO0OO in OOOOO0O00O0OO0OO0 ["停用词"]]#line:2170
    O0000OOOO0OO0000O =pd .read_excel (O0O0OOO0OOOOO0OO0 ,sheet_name ="本地词库",header =0 ,index_col =0 ).reset_index ()#line:2173
    O0OOO000O0O0OOOOO =O0000OOOO0OO0000O ["本地词库"]#line:2174
    jieba .load_userdict (O0OOO000O0O0OOOOO )#line:2175
    O0OO00O0000O000OO =""#line:2178
    OOOOOOOOOOOO000OO =get_list0 (OOO00O0O00000OOOO ,O0OO0O00000OO0000 )#line:2181
    try :#line:2182
        for O0OO0OO00O0000O0O in OOOOOOOOOOOO000OO :#line:2183
            for OOOOOOOOOO00O000O in O0OO0O00000OO0000 [O0OO0OO00O0000O0O ]:#line:2184
                O0OO00O0000O000OO =O0OO00O0000O000OO +str (OOOOOOOOOO00O000O )#line:2185
    except :#line:2186
        text .insert (END ,"分词配置文件未正确设置，将对整个表格进行分词。")#line:2187
        for O0OO0OO00O0000O0O in O0OO0O00000OO0000 .columns .tolist ():#line:2188
            for OOOOOOOOOO00O000O in O0OO0O00000OO0000 [O0OO0OO00O0000O0O ]:#line:2189
                O0OO00O0000O000OO =O0OO00O0000O000OO +str (OOOOOOOOOO00O000O )#line:2190
    O0OO0OOO0OO0OOO0O =[]#line:2191
    O0OO0OOO0OO0OOO0O =O0OO0OOO0OO0OOO0O +[O00OOO00OO0OOOO0O for O00OOO00OO0OOOO0O in jieba .cut (O0OO00O0000O000OO )if O00OOO00OO0OOOO0O not in OOO00OO00O00O0000 ]#line:2192
    OO00OO0000OO0O000 =dict (OO0OOOO0OOO00OO00 (O0OO0OOO0OO0OOO0O ,OOOOO0O0O0O0000OO ))#line:2193
    OO0OOO00O0O0OOOO0 =pd .DataFrame ([OO00OO0000OO0O000 ]).T #line:2194
    OO0OOO00O0O0OOOO0 =OO0OOO00O0O0OOOO0 .reset_index ()#line:2195
    return OO0OOO00O0O0OOOO0 #line:2196
def TOOLS_time (OOO00O0000OOOOOO0 ,O0000OO0OO0OOOOO0 ,O0O000000O000O00O ):#line:2198
	""#line:2199
	O0000OOO0O00OOOO0 =OOO00O0000OOOOOO0 .groupby ([O0000OO0OO0OOOOO0 ]).agg (报告总数 =("报告编码","nunique"),严重伤害数 =("伤害",lambda O0O0OOO0O000O00O0 :STAT_countpx (O0O0OOO0O000O00O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O000000O0O00000 :STAT_countpx (O0O000000O0O00000 .values ,"死亡")),).sort_values (by =O0000OO0OO0OOOOO0 ,ascending =[True ],na_position ="last").reset_index ()#line:2204
	O0000OOO0O00OOOO0 =O0000OOO0O00OOOO0 .set_index (O0000OO0OO0OOOOO0 )#line:2205
	O0000OOO0O00OOOO0 =O0000OOO0O00OOOO0 .resample ('D').asfreq (fill_value =0 )#line:2207
	O0000OOO0O00OOOO0 ["time"]=O0000OOO0O00OOOO0 .index .values #line:2209
	O0000OOO0O00OOOO0 ["time"]=pd .to_datetime (O0000OOO0O00OOOO0 ["time"],format ="%Y/%m/%d").dt .date #line:2210
	if O0O000000O000O00O ==1 :#line:2212
		return O0000OOO0O00OOOO0 .reset_index (drop =True )#line:2214
	O0000OOO0O00OOOO0 ["30天累计数"]=O0000OOO0O00OOOO0 ["报告总数"].rolling (30 ,min_periods =1 ).agg (lambda O000O0OO0O0OO0O0O :sum (O000O0OO0O0OO0O0O )).astype (int )#line:2216
	O0000OOO0O00OOOO0 ["30天严重伤害累计数"]=O0000OOO0O00OOOO0 ["严重伤害数"].rolling (30 ,min_periods =1 ).agg (lambda O0OO00O0O0000OO0O :sum (O0OO00O0O0000OO0O )).astype (int )#line:2217
	O0000OOO0O00OOOO0 ["30天死亡累计数"]=O0000OOO0O00OOOO0 ["死亡数量"].rolling (30 ,min_periods =1 ).agg (lambda O0O000O00OO00O000 :sum (O0O000O00OO00O000 )).astype (int )#line:2218
	O0000OOO0O00OOOO0 .loc [(((O0000OOO0O00OOOO0 ["30天累计数"]>=3 )&(O0000OOO0O00OOOO0 ["30天严重伤害累计数"]>=1 ))|(O0000OOO0O00OOOO0 ["30天累计数"]>=5 )|(O0000OOO0O00OOOO0 ["30天死亡累计数"]>=1 )),"关注区域"]=O0000OOO0O00OOOO0 ["30天累计数"]#line:2239
	DRAW_make_risk_plot (O0000OOO0O00OOOO0 ,"time",["30天累计数","30天严重伤害累计数","关注区域"],"折线图",999 )#line:2244
def TOOLS_keti (OOOO0O0OOO0O0O000 ):#line:2248
	""#line:2249
	import datetime #line:2250
	def OOOOOOO0OOOOOOO00 (O0OOO0OO0OO0OO0OO ,OOO000000O0OO000O ):#line:2252
		if ini ["模式"]=="药品":#line:2253
			O00O000O0O00OOOOO =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="药品").reset_index (drop =True )#line:2254
		if ini ["模式"]=="器械":#line:2255
			O00O000O0O00OOOOO =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="器械").reset_index (drop =True )#line:2256
		if ini ["模式"]=="化妆品":#line:2257
			O00O000O0O00OOOOO =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="化妆品").reset_index (drop =True )#line:2258
		O0O0O0O00O00O00OO =O00O000O0O00OOOOO ["权重"][0 ]#line:2259
		O0O00OO0O0O00O00O =O00O000O0O00OOOOO ["权重"][1 ]#line:2260
		O0OOO00O0OOO0O0O0 =O00O000O0O00OOOOO ["权重"][2 ]#line:2261
		OO0OO00OO0OO0O0O0 =O00O000O0O00OOOOO ["权重"][3 ]#line:2262
		O0000OOOO000OOOO0 =O00O000O0O00OOOOO ["值"][3 ]#line:2263
		OO00O00OO00000O0O =O00O000O0O00OOOOO ["权重"][4 ]#line:2265
		O00O000OO00OO0000 =O00O000O0O00OOOOO ["值"][4 ]#line:2266
		O00000000O0O0O0O0 =O00O000O0O00OOOOO ["权重"][5 ]#line:2268
		O0O0O0O0OO000000O =O00O000O0O00OOOOO ["值"][5 ]#line:2269
		O0O0OO000O0O0000O =O00O000O0O00OOOOO ["权重"][6 ]#line:2271
		OO0O0OOO0OO000O00 =O00O000O0O00OOOOO ["值"][6 ]#line:2272
		O0O0O000OO00O0O00 =pd .to_datetime (O0OOO0OO0OO0OO0OO )#line:2274
		O000O0000O00O00OO =OOO000000O0OO000O .copy ().set_index ('报告日期')#line:2275
		O000O0000O00O00OO =O000O0000O00O00OO .sort_index ()#line:2276
		if ini ["模式"]=="器械":#line:2277
			O000O0000O00O00OO ["关键字查找列"]=O000O0000O00O00OO ["器械故障表现"].astype (str )+O000O0000O00O00OO ["伤害表现"].astype (str )+O000O0000O00O00OO ["使用过程"].astype (str )+O000O0000O00O00OO ["事件原因分析描述"].astype (str )+O000O0000O00O00OO ["初步处置情况"].astype (str )#line:2278
		else :#line:2279
			O000O0000O00O00OO ["关键字查找列"]=O000O0000O00O00OO ["器械故障表现"].astype (str )#line:2280
		O000O0000O00O00OO .loc [O000O0000O00O00OO ["关键字查找列"].str .contains (O0000OOOO000OOOO0 ,na =False ),"高度关注关键字"]=1 #line:2281
		O000O0000O00O00OO .loc [O000O0000O00O00OO ["关键字查找列"].str .contains (O00O000OO00OO0000 ,na =False ),"二级敏感词"]=1 #line:2282
		O000O0000O00O00OO .loc [O000O0000O00O00OO ["关键字查找列"].str .contains (O0O0O0O0OO000000O ,na =False ),"减分项"]=1 #line:2283
		OOOOO0OOO0000O00O =O000O0000O00O00OO .loc [O0O0O000OO00O0O00 -pd .Timedelta (days =30 ):O0O0O000OO00O0O00 ].reset_index ()#line:2285
		OOO00OO000OOOO0OO =O000O0000O00O00OO .loc [O0O0O000OO00O0O00 -pd .Timedelta (days =365 ):O0O0O000OO00O0O00 ].reset_index ()#line:2286
		OOOOO0OO0O00O0OOO =OOOOO0OOO0000O00O .groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (证号计数 =("注册证编号/曾用注册证编号","count"),严重伤害数 =("伤害",lambda OO000OOO000OOO00O :STAT_countpx (OO000OOO000OOO00O .values ,"严重伤害")),死亡数量 =("伤害",lambda OO00OOOO0OO0O0OO0 :STAT_countpx (OO00OOOO0OO0O0OO0 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda OO00OOO00O0OOOOO0 :STAT_countpx (OO00OOO00O0OOOOO0 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O0OOO000OOO0O0OOO :STAT_countpx (O0OOO000OOO0O0OOO .values ,"严重伤害待评价")),高度关注关键字 =("高度关注关键字","sum"),二级敏感词 =("二级敏感词","sum"),减分项 =("减分项","sum"),).sort_values (by ="证号计数",ascending =[False ],na_position ="last").reset_index ()#line:2308
		OO0OOO0OO00OOOO00 =OOOOO0OOO0000O00O .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (型号计数 =("型号","count"),).sort_values (by ="型号计数",ascending =[False ],na_position ="last").reset_index ()#line:2313
		OO0OOO0OO00OOOO00 =OO0OOO0OO00OOOO00 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2314
		O0O0O00000000O000 =OOOOO0OOO0000O00O .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (批号计数 =("产品批号","count"),严重伤害数 =("伤害",lambda O00O000O0OOO0OOOO :STAT_countpx (O00O000O0OOO0OOOO .values ,"严重伤害")),).sort_values (by ="批号计数",ascending =[False ],na_position ="last").reset_index ()#line:2319
		O0O0O00000000O000 ["风险评分-影响"]=0 #line:2322
		O0O0O00000000O000 ["评分说明"]=""#line:2323
		O0O0O00000000O000 .loc [((O0O0O00000000O000 ["批号计数"]>=3 )&(O0O0O00000000O000 ["严重伤害数"]>=1 )&(O0O0O00000000O000 ["产品类别"]!="有源"))|((O0O0O00000000O000 ["批号计数"]>=5 )&(O0O0O00000000O000 ["产品类别"]!="有源")),"风险评分-影响"]=O0O0O00000000O000 ["风险评分-影响"]+3 #line:2324
		O0O0O00000000O000 .loc [(O0O0O00000000O000 ["风险评分-影响"]>=3 ),"评分说明"]=O0O0O00000000O000 ["评分说明"]+"●符合省中心无源规则+3;"#line:2325
		O0O0O00000000O000 =O0O0O00000000O000 .sort_values (by ="风险评分-影响",ascending =[False ],na_position ="last").reset_index (drop =True )#line:2329
		O0O0O00000000O000 =O0O0O00000000O000 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2330
		OO0OOO0OO00OOOO00 =OO0OOO0OO00OOOO00 [["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号","型号计数"]]#line:2331
		O0O0O00000000O000 =O0O0O00000000O000 [["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号","批号计数","风险评分-影响","评分说明"]]#line:2332
		OOOOO0OO0O00O0OOO =pd .merge (OOOOO0OO0O00O0OOO ,OO0OOO0OO00OOOO00 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2333
		OOOOO0OO0O00O0OOO =pd .merge (OOOOO0OO0O00O0OOO ,O0O0O00000000O000 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2335
		OOOOO0OO0O00O0OOO .loc [((OOOOO0OO0O00O0OOO ["证号计数"]>=3 )&(OOOOO0OO0O00O0OOO ["严重伤害数"]>=1 )&(OOOOO0OO0O00O0OOO ["产品类别"]=="有源"))|((OOOOO0OO0O00O0OOO ["证号计数"]>=5 )&(OOOOO0OO0O00O0OOO ["产品类别"]=="有源")),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+3 #line:2339
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-影响"]>=3 )&(OOOOO0OO0O00O0OOO ["产品类别"]=="有源"),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"●符合省中心有源规则+3;"#line:2340
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["死亡数量"]>=1 ),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+10 #line:2345
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-影响"]>=10 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"存在死亡报告;"#line:2346
		O0OOO000OOO0O00O0 =round (O0O0O0O00O00O00OO *(OOOOO0OO0O00O0OOO ["严重伤害数"]/OOOOO0OO0O00O0OOO ["证号计数"]),2 )#line:2349
		OOOOO0OO0O00O0OOO ["风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+O0OOO000OOO0O00O0 #line:2350
		OOOOO0OO0O00O0OOO ["评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"严重比评分"+O0OOO000OOO0O00O0 .astype (str )+";"#line:2351
		O0OOO0O0O0O0OO00O =round (O0O00OO0O0O00O00O *(np .log (OOOOO0OO0O00O0OOO ["单位个数"])),2 )#line:2354
		OOOOO0OO0O00O0OOO ["风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+O0OOO0O0O0O0OO00O #line:2355
		OOOOO0OO0O00O0OOO ["评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"报告单位评分"+O0OOO0O0O0O0OO00O .astype (str )+";"#line:2356
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["产品类别"]=="有源")&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+O0OOO00O0OOO0O0O0 *OOOOO0OO0O00O0OOO ["型号计数"]/OOOOO0OO0O00O0OOO ["证号计数"]#line:2359
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["产品类别"]=="有源")&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"型号集中度评分"+(round (O0OOO00O0OOO0O0O0 *OOOOO0OO0O00O0OOO ["型号计数"]/OOOOO0OO0O00O0OOO ["证号计数"],2 )).astype (str )+";"#line:2360
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["产品类别"]!="有源")&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+O0OOO00O0OOO0O0O0 *OOOOO0OO0O00O0OOO ["批号计数"]/OOOOO0OO0O00O0OOO ["证号计数"]#line:2361
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["产品类别"]!="有源")&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"批号集中度评分"+(round (O0OOO00O0OOO0O0O0 *OOOOO0OO0O00O0OOO ["批号计数"]/OOOOO0OO0O00O0OOO ["证号计数"],2 )).astype (str )+";"#line:2362
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["高度关注关键字"]>=1 ),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+OO0OO00OO0OO0O0O0 #line:2365
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["高度关注关键字"]>=1 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"●含有高度关注关键字评分"+str (OO0OO00OO0OO0O0O0 )+"；"#line:2366
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["二级敏感词"]>=1 ),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+OO00O00OO00000O0O #line:2369
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["二级敏感词"]>=1 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"含有二级敏感词评分"+str (OO00O00OO00000O0O )+"；"#line:2370
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["减分项"]>=1 ),"风险评分-影响"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]+O00000000O0O0O0O0 #line:2373
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["减分项"]>=1 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"减分项评分"+str (O00000000O0O0O0O0 )+"；"#line:2374
		O00O0OO00OOO0O0OO =Countall (OOO00OO000OOOO0OO ).df_findrisk ("事件发生月份")#line:2377
		O00O0OO00OOO0O0OO =O00O0OO00OOO0O0OO .drop_duplicates ("注册证编号/曾用注册证编号")#line:2378
		O00O0OO00OOO0O0OO =O00O0OO00OOO0O0OO [["注册证编号/曾用注册证编号","均值","标准差","CI上限"]]#line:2379
		OOOOO0OO0O00O0OOO =pd .merge (OOOOO0OO0O00O0OOO ,O00O0OO00OOO0O0OO ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2380
		OOOOO0OO0O00O0OOO ["风险评分-月份"]=1 #line:2382
		OOOOO0OO0O00O0OOO ["mfc"]=""#line:2383
		OOOOO0OO0O00O0OOO .loc [((OOOOO0OO0O00O0OOO ["证号计数"]>OOOOO0OO0O00O0OOO ["均值"])&(OOOOO0OO0O00O0OOO ["标准差"].astype (str )=="nan")),"风险评分-月份"]=OOOOO0OO0O00O0OOO ["风险评分-月份"]+1 #line:2384
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>OOOOO0OO0O00O0OOO ["均值"]),"mfc"]="月份计数超过历史均值"+OOOOO0OO0O00O0OOO ["均值"].astype (str )+"；"#line:2385
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=(OOOOO0OO0O00O0OOO ["均值"]+OOOOO0OO0O00O0OOO ["标准差"]))&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"风险评分-月份"]=OOOOO0OO0O00O0OOO ["风险评分-月份"]+1 #line:2387
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=(OOOOO0OO0O00O0OOO ["均值"]+OOOOO0OO0O00O0OOO ["标准差"]))&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"mfc"]="月份计数超过3例超过历史均值一个标准差("+OOOOO0OO0O00O0OOO ["标准差"].astype (str )+")；"#line:2388
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"风险评分-月份"]=OOOOO0OO0O00O0OOO ["风险评分-月份"]+2 #line:2390
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=3 ),"mfc"]="月份计数超过3例且超过历史95%CI上限("+OOOOO0OO0O00O0OOO ["CI上限"].astype (str )+")；"#line:2391
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=5 ),"风险评分-月份"]=OOOOO0OO0O00O0OOO ["风险评分-月份"]+1 #line:2393
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=5 ),"mfc"]="月份计数超过5例且超过历史95%CI上限("+OOOOO0OO0O00O0OOO ["CI上限"].astype (str )+")；"#line:2394
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=7 ),"风险评分-月份"]=OOOOO0OO0O00O0OOO ["风险评分-月份"]+1 #line:2396
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=7 ),"mfc"]="月份计数超过7例且超过历史95%CI上限("+OOOOO0OO0O00O0OOO ["CI上限"].astype (str )+")；"#line:2397
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=9 ),"风险评分-月份"]=OOOOO0OO0O00O0OOO ["风险评分-月份"]+1 #line:2399
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["证号计数"]>=9 ),"mfc"]="月份计数超过9例且超过历史95%CI上限("+OOOOO0OO0O00O0OOO ["CI上限"].astype (str )+")；"#line:2400
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=3 )&(OOOOO0OO0O00O0OOO ["标准差"].astype (str )=="nan"),"风险评分-月份"]=3 #line:2404
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["证号计数"]>=3 )&(OOOOO0OO0O00O0OOO ["标准差"].astype (str )=="nan"),"mfc"]="无历史数据但数量超过3例；"#line:2405
		OOOOO0OO0O00O0OOO ["评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"●●证号数量："+OOOOO0OO0O00O0OOO ["证号计数"].astype (str )+";"+OOOOO0OO0O00O0OOO ["mfc"]#line:2408
		del OOOOO0OO0O00O0OOO ["mfc"]#line:2409
		OOOOO0OO0O00O0OOO =OOOOO0OO0O00O0OOO .rename (columns ={"均值":"月份均值","标准差":"月份标准差","CI上限":"月份CI上限"})#line:2410
		O00O0OO00OOO0O0OO =Countall (OOO00OO000OOOO0OO ).df_findrisk ("产品批号")#line:2414
		O00O0OO00OOO0O0OO =O00O0OO00OOO0O0OO .drop_duplicates ("注册证编号/曾用注册证编号")#line:2415
		O00O0OO00OOO0O0OO =O00O0OO00OOO0O0OO [["注册证编号/曾用注册证编号","均值","标准差","CI上限"]]#line:2416
		OOOOO0OO0O00O0OOO =pd .merge (OOOOO0OO0O00O0OOO ,O00O0OO00OOO0O0OO ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2417
		OOOOO0OO0O00O0OOO ["风险评分-批号"]=1 #line:2419
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["产品类别"]!="有源"),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"●●高峰批号数量："+OOOOO0OO0O00O0OOO ["批号计数"].astype (str )+";"#line:2420
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>OOOOO0OO0O00O0OOO ["均值"]),"风险评分-批号"]=OOOOO0OO0O00O0OOO ["风险评分-批号"]+1 #line:2422
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>OOOOO0OO0O00O0OOO ["均值"]),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"高峰批号计数超过历史均值"+OOOOO0OO0O00O0OOO ["均值"].astype (str )+"；"#line:2423
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>(OOOOO0OO0O00O0OOO ["均值"]+OOOOO0OO0O00O0OOO ["标准差"]))&(OOOOO0OO0O00O0OOO ["批号计数"]>=3 ),"风险评分-批号"]=OOOOO0OO0O00O0OOO ["风险评分-批号"]+1 #line:2424
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>(OOOOO0OO0O00O0OOO ["均值"]+OOOOO0OO0O00O0OOO ["标准差"]))&(OOOOO0OO0O00O0OOO ["批号计数"]>=3 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"高峰批号计数超过3例超过历史均值一个标准差("+OOOOO0OO0O00O0OOO ["标准差"].astype (str )+")；"#line:2425
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["批号计数"]>=3 ),"风险评分-批号"]=OOOOO0OO0O00O0OOO ["风险评分-批号"]+1 #line:2426
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>OOOOO0OO0O00O0OOO ["CI上限"])&(OOOOO0OO0O00O0OOO ["批号计数"]>=3 ),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"高峰批号计数超过3例且超过历史95%CI上限("+OOOOO0OO0O00O0OOO ["CI上限"].astype (str )+")；"#line:2427
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>=3 )&(OOOOO0OO0O00O0OOO ["标准差"].astype (str )=="nan"),"风险评分-月份"]=3 #line:2429
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["批号计数"]>=3 )&(OOOOO0OO0O00O0OOO ["标准差"].astype (str )=="nan"),"评分说明"]=OOOOO0OO0O00O0OOO ["评分说明"]+"无历史数据但数量超过3例；"#line:2430
		OOOOO0OO0O00O0OOO =OOOOO0OO0O00O0OOO .rename (columns ={"均值":"高峰批号均值","标准差":"高峰批号标准差","CI上限":"高峰批号CI上限"})#line:2431
		OOOOO0OO0O00O0OOO ["风险评分-影响"]=round (OOOOO0OO0O00O0OOO ["风险评分-影响"],2 )#line:2434
		OOOOO0OO0O00O0OOO ["风险评分-月份"]=round (OOOOO0OO0O00O0OOO ["风险评分-月份"],2 )#line:2435
		OOOOO0OO0O00O0OOO ["风险评分-批号"]=round (OOOOO0OO0O00O0OOO ["风险评分-批号"],2 )#line:2436
		OOOOO0OO0O00O0OOO ["总体评分"]=OOOOO0OO0O00O0OOO ["风险评分-影响"].copy ()#line:2438
		OOOOO0OO0O00O0OOO ["关注建议"]=""#line:2439
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-影响"]>=3 ),"关注建议"]=OOOOO0OO0O00O0OOO ["关注建议"]+"●建议关注(影响范围)；"#line:2440
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-月份"]>=3 ),"关注建议"]=OOOOO0OO0O00O0OOO ["关注建议"]+"●建议关注(当月数量异常)；"#line:2441
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-批号"]>=3 ),"关注建议"]=OOOOO0OO0O00O0OOO ["关注建议"]+"●建议关注(高峰批号数量异常)。"#line:2442
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-月份"]>=OOOOO0OO0O00O0OOO ["风险评分-批号"]),"总体评分"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]*OOOOO0OO0O00O0OOO ["风险评分-月份"]#line:2446
		OOOOO0OO0O00O0OOO .loc [(OOOOO0OO0O00O0OOO ["风险评分-月份"]<OOOOO0OO0O00O0OOO ["风险评分-批号"]),"总体评分"]=OOOOO0OO0O00O0OOO ["风险评分-影响"]*OOOOO0OO0O00O0OOO ["风险评分-批号"]#line:2447
		OOOOO0OO0O00O0OOO ["总体评分"]=round (OOOOO0OO0O00O0OOO ["总体评分"],2 )#line:2449
		OOOOO0OO0O00O0OOO ["评分说明"]=OOOOO0OO0O00O0OOO ["关注建议"]+OOOOO0OO0O00O0OOO ["评分说明"]#line:2450
		OOOOO0OO0O00O0OOO =OOOOO0OO0O00O0OOO .sort_values (by =["总体评分","风险评分-影响"],ascending =[False ,False ],na_position ="last").reset_index (drop =True )#line:2451
		OOOOO0OO0O00O0OOO ["主要故障分类"]=""#line:2454
		for O00OO00OO0O0OO000 ,OOOO0O0O0O0OOO0OO in OOOOO0OO0O00O0OOO .iterrows ():#line:2455
			O00OO000O0OO0OOO0 =OOOOO0OOO0000O00O [(OOOOO0OOO0000O00O ["注册证编号/曾用注册证编号"]==OOOO0O0O0O0OOO0OO ["注册证编号/曾用注册证编号"])].copy ()#line:2456
			if OOOO0O0O0O0OOO0OO ["总体评分"]>=float (O0O0OO000O0O0000O ):#line:2457
				if OOOO0O0O0O0OOO0OO ["规整后品类"]!="N":#line:2458
					O0OO0OOO0O0OO00OO =Countall (O00OO000O0OO0OOO0 ).df_psur ("特定品种",OOOO0O0O0O0OOO0OO ["规整后品类"])#line:2459
				elif OOOO0O0O0O0OOO0OO ["产品类别"]=="无源":#line:2460
					O0OO0OOO0O0OO00OO =Countall (O00OO000O0OO0OOO0 ).df_psur ("通用无源")#line:2461
				elif OOOO0O0O0O0OOO0OO ["产品类别"]=="有源":#line:2462
					O0OO0OOO0O0OO00OO =Countall (O00OO000O0OO0OOO0 ).df_psur ("通用有源")#line:2463
				elif OOOO0O0O0O0OOO0OO ["产品类别"]=="体外诊断试剂":#line:2464
					O0OO0OOO0O0OO00OO =Countall (O00OO000O0OO0OOO0 ).df_psur ("体外诊断试剂")#line:2465
				OOO00000OO0O000O0 =O0OO0OOO0O0OO00OO [["事件分类","总数量"]].copy ()#line:2467
				O00OO0O000OO00OO0 =""#line:2468
				for OOOOO00O0000OO0OO ,OOOO00O00O0O000OO in OOO00000OO0O000O0 .iterrows ():#line:2469
					O00OO0O000OO00OO0 =O00OO0O000OO00OO0 +str (OOOO00O00O0O000OO ["事件分类"])+":"+str (OOOO00O00O0O000OO ["总数量"])+";"#line:2470
				OOOOO0OO0O00O0OOO .loc [O00OO00OO0O0OO000 ,"主要故障分类"]=O00OO0O000OO00OO0 #line:2471
			else :#line:2472
				break #line:2473
		OOOOO0OO0O00O0OOO =OOOOO0OO0O00O0OOO [["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","证号计数","严重伤害数","死亡数量","总体评分","风险评分-影响","风险评分-月份","风险评分-批号","主要故障分类","评分说明","单位个数","单位列表","批号个数","批号列表","型号个数","型号列表","规格个数","规格列表","待评价数","严重伤害待评价数","高度关注关键字","二级敏感词","月份均值","月份标准差","月份CI上限","高峰批号均值","高峰批号标准差","高峰批号CI上限","型号","型号计数","产品批号","批号计数"]]#line:2477
		OOOOO0OO0O00O0OOO ["报表类型"]="dfx_zhenghao"#line:2478
		TABLE_tree_Level_2 (OOOOO0OO0O00O0OOO ,1 ,OOOOO0OOO0000O00O ,OOO00OO000OOOO0OO )#line:2479
		pass #line:2480
	O00OOOOO0OO00OOO0 =Toplevel ()#line:2483
	O00OOOOO0OO00OOO0 .title ('风险预警')#line:2484
	O0OOO0OOOO0O0O0OO =O00OOOOO0OO00OOO0 .winfo_screenwidth ()#line:2485
	O00OO0OO0O00OOO00 =O00OOOOO0OO00OOO0 .winfo_screenheight ()#line:2487
	OOO000OO0OOO0OO00 =350 #line:2489
	O0OO0O0OO0OOOO00O =35 #line:2490
	O0OO00O000O0OO0OO =(O0OOO0OOOO0O0O0OO -OOO000OO0OOO0OO00 )/2 #line:2492
	OOO000OOO0O00O00O =(O00OO0OO0O00OOO00 -O0OO0O0OO0OOOO00O )/2 #line:2493
	O00OOOOO0OO00OOO0 .geometry ("%dx%d+%d+%d"%(OOO000OO0OOO0OO00 ,O0OO0O0OO0OOOO00O ,O0OO00O000O0OO0OO ,OOO000OOO0O00O00O ))#line:2494
	O00OOO00O0O00OOOO =Label (O00OOOOO0OO00OOO0 ,text ="预警日期：")#line:2496
	O00OOO00O0O00OOOO .grid (row =1 ,column =0 ,sticky ="w")#line:2497
	OOOO0OO0OOOOOO00O =Entry (O00OOOOO0OO00OOO0 ,width =30 )#line:2498
	OOOO0OO0OOOOOO00O .insert (0 ,datetime .date .today ())#line:2499
	OOOO0OO0OOOOOO00O .grid (row =1 ,column =1 ,sticky ="w")#line:2500
	OO00000000O0OO0OO =Button (O00OOOOO0OO00OOO0 ,text ="确定",width =10 ,command =lambda :TABLE_tree_Level_2 (OOOOOOO0OOOOOOO00 (OOOO0OO0OOOOOO00O .get (),OOOO0O0OOO0O0O000 ),1 ,OOOO0O0OOO0O0O000 ))#line:2504
	OO00000000O0OO0OO .grid (row =1 ,column =3 ,sticky ="w")#line:2505
	pass #line:2507
def TOOLS_autocount (OO0O0O00OO0000000 ,O00O0000OO0OOO0OO ):#line:2509
    ""#line:2510
    O0O0O000OO0OOO00O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ).reset_index ()#line:2513
    O0O00OOO000O0OO0O =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ).reset_index ()#line:2516
    OO0OO0O000OOOOOOO =O0O00OOO000O0OO0O [(O0O00OOO000O0OO0O ["是否属于二级以上医疗机构"]=="是")]#line:2517
    if O00O0000OO0OOO0OO =="药品":#line:2520
        OO0O0O00OO0000000 =OO0O0O00OO0000000 .reset_index (drop =True )#line:2521
        if "再次使用可疑药是否出现同样反应"not in OO0O0O00OO0000000 .columns :#line:2522
            showinfo (title ="错误信息",message ="导入的疑似不是药品报告表。")#line:2523
            return 0 #line:2524
        OO00OO0O0O0O00OO0 =Countall (OO0O0O00OO0000000 ).df_org ("监测机构")#line:2526
        OO00OO0O0O0O00OO0 =pd .merge (OO00OO0O0O0O00OO0 ,O0O0O000OO0OOO00O ,on ="监测机构",how ="left")#line:2527
        OO00OO0O0O0O00OO0 =OO00OO0O0O0O00OO0 [["监测机构序号","监测机构","药品数量指标","报告数量","审核通过数","新严比","严重比","超时比"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2528
        OO00OO0000OOOO0OO =["药品数量指标","审核通过数","报告数量"]#line:2529
        OO00OO0O0O0O00OO0 [OO00OO0000OOOO0OO ]=OO00OO0O0O0O00OO0 [OO00OO0000OOOO0OO ].apply (lambda O00OO00O0OOOOOO00 :O00OO00O0OOOOOO00 .astype (int ))#line:2530
        O0O00OO0OO0O0OO0O =Countall (OO0O0O00OO0000000 ).df_user ()#line:2532
        O0O00OO0OO0O0OO0O =pd .merge (O0O00OO0OO0O0OO0O ,O0O00OOO000O0OO0O ,on =["监测机构","单位名称"],how ="left")#line:2533
        O0O00OO0OO0O0OO0O =pd .merge (O0O00OO0OO0O0OO0O ,O0O0O000OO0OOO00O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2534
        O0O00OO0OO0O0OO0O =O0O00OO0OO0O0OO0O [["监测机构序号","监测机构","单位名称","药品数量指标","报告数量","审核通过数","新严比","严重比","超时比"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2536
        OO00OO0000OOOO0OO =["药品数量指标","审核通过数","报告数量"]#line:2537
        O0O00OO0OO0O0OO0O [OO00OO0000OOOO0OO ]=O0O00OO0OO0O0OO0O [OO00OO0000OOOO0OO ].apply (lambda O0000O0OOOO0O0O0O :O0000O0OOOO0O0O0O .astype (int ))#line:2538
        OO0OO00O0O0O000OO =pd .merge (OO0OO0O000OOOOOOO ,O0O00OO0OO0O0OO0O ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2540
        OO0OO00O0O0O000OO =OO0OO00O0O0O000OO [(OO0OO00O0O0O000OO ["审核通过数"]<1 )]#line:2541
        OO0OO00O0O0O000OO =OO0OO00O0O0O000OO [["监测机构","单位名称","报告数量","审核通过数","严重比","超时比"]]#line:2542
    if O00O0000OO0OOO0OO =="器械":#line:2544
        OO0O0O00OO0000000 =OO0O0O00OO0000000 .reset_index (drop =True )#line:2545
        if "产品编号"not in OO0O0O00OO0000000 .columns :#line:2546
            showinfo (title ="错误信息",message ="导入的疑似不是器械报告表。")#line:2547
            return 0 #line:2548
        OO00OO0O0O0O00OO0 =Countall (OO0O0O00OO0000000 ).df_org ("监测机构")#line:2550
        OO00OO0O0O0O00OO0 =pd .merge (OO00OO0O0O0O00OO0 ,O0O0O000OO0OOO00O ,on ="监测机构",how ="left")#line:2551
        OO00OO0O0O0O00OO0 =OO00OO0O0O0O00OO0 [["监测机构序号","监测机构","器械数量指标","报告数量","审核通过数","严重比","超时比"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2552
        OO00OO0000OOOO0OO =["器械数量指标","审核通过数","报告数量"]#line:2553
        OO00OO0O0O0O00OO0 [OO00OO0000OOOO0OO ]=OO00OO0O0O0O00OO0 [OO00OO0000OOOO0OO ].apply (lambda O00O0O0OO000OOOO0 :O00O0O0OO000OOOO0 .astype (int ))#line:2554
        O0O00OO0OO0O0OO0O =Countall (OO0O0O00OO0000000 ).df_user ()#line:2556
        O0O00OO0OO0O0OO0O =pd .merge (O0O00OO0OO0O0OO0O ,O0O00OOO000O0OO0O ,on =["监测机构","单位名称"],how ="left")#line:2557
        O0O00OO0OO0O0OO0O =pd .merge (O0O00OO0OO0O0OO0O ,O0O0O000OO0OOO00O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2558
        O0O00OO0OO0O0OO0O =O0O00OO0OO0O0OO0O [["监测机构序号","监测机构","单位名称","器械数量指标","报告数量","审核通过数","严重比","超时比"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2560
        OO00OO0000OOOO0OO =["器械数量指标","审核通过数","报告数量"]#line:2561
        O0O00OO0OO0O0OO0O [OO00OO0000OOOO0OO ]=O0O00OO0OO0O0OO0O [OO00OO0000OOOO0OO ].apply (lambda OOOOOO0OO0OO00O00 :OOOOOO0OO0OO00O00 .astype (int ))#line:2562
        OO0OO00O0O0O000OO =pd .merge (OO0OO0O000OOOOOOO ,O0O00OO0OO0O0OO0O ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2564
        OO0OO00O0O0O000OO =OO0OO00O0O0O000OO [(OO0OO00O0O0O000OO ["审核通过数"]<1 )]#line:2565
        OO0OO00O0O0O000OO =OO0OO00O0O0O000OO [["监测机构","单位名称","报告数量","审核通过数","严重比","超时比"]]#line:2566
    if O00O0000OO0OOO0OO =="化妆品":#line:2569
        OO0O0O00OO0000000 =OO0O0O00OO0000000 .reset_index (drop =True )#line:2570
        if "初步判断"not in OO0O0O00OO0000000 .columns :#line:2571
            showinfo (title ="错误信息",message ="导入的疑似不是化妆品报告表。")#line:2572
            return 0 #line:2573
        OO00OO0O0O0O00OO0 =Countall (OO0O0O00OO0000000 ).df_org ("监测机构")#line:2575
        OO00OO0O0O0O00OO0 =pd .merge (OO00OO0O0O0O00OO0 ,O0O0O000OO0OOO00O ,on ="监测机构",how ="left")#line:2576
        OO00OO0O0O0O00OO0 =OO00OO0O0O0O00OO0 [["监测机构序号","监测机构","化妆品数量指标","报告数量","审核通过数"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2577
        OO00OO0000OOOO0OO =["化妆品数量指标","审核通过数","报告数量"]#line:2578
        OO00OO0O0O0O00OO0 [OO00OO0000OOOO0OO ]=OO00OO0O0O0O00OO0 [OO00OO0000OOOO0OO ].apply (lambda O0OOOO0O0O0OOO0O0 :O0OOOO0O0O0OOO0O0 .astype (int ))#line:2579
        O0O00OO0OO0O0OO0O =Countall (OO0O0O00OO0000000 ).df_user ()#line:2581
        O0O00OO0OO0O0OO0O =pd .merge (O0O00OO0OO0O0OO0O ,O0O00OOO000O0OO0O ,on =["监测机构","单位名称"],how ="left")#line:2582
        O0O00OO0OO0O0OO0O =pd .merge (O0O00OO0OO0O0OO0O ,O0O0O000OO0OOO00O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2583
        O0O00OO0OO0O0OO0O =O0O00OO0OO0O0OO0O [["监测机构序号","监测机构","单位名称","化妆品数量指标","报告数量","审核通过数"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2584
        OO00OO0000OOOO0OO =["化妆品数量指标","审核通过数","报告数量"]#line:2585
        O0O00OO0OO0O0OO0O [OO00OO0000OOOO0OO ]=O0O00OO0OO0O0OO0O [OO00OO0000OOOO0OO ].apply (lambda OOOO0OO0000OOOO00 :OOOO0OO0000OOOO00 .astype (int ))#line:2586
        OO0OO00O0O0O000OO =pd .merge (OO0OO0O000OOOOOOO ,O0O00OO0OO0O0OO0O ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2588
        OO0OO00O0O0O000OO =OO0OO00O0O0O000OO [(OO0OO00O0O0O000OO ["审核通过数"]<1 )]#line:2589
        OO0OO00O0O0O000OO =OO0OO00O0O0O000OO [["监测机构","单位名称","报告数量","审核通过数"]]#line:2590
    O00OO00OO0OO0OO00 =filedialog .asksaveasfilename (title =u"保存文件",initialfile =O00O0000OO0OOO0OO ,defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:2597
    O00O0OO0O0000O0O0 =pd .ExcelWriter (O00OO00OO0OO0OO00 )#line:2598
    OO00OO0O0O0O00OO0 .to_excel (O00O0OO0O0000O0O0 ,sheet_name ="监测机构")#line:2599
    O0O00OO0OO0O0OO0O .to_excel (O00O0OO0O0000O0O0 ,sheet_name ="上报单位")#line:2600
    OO0OO00O0O0O000OO .to_excel (O00O0OO0O0000O0O0 ,sheet_name ="未上报的二级以上医疗机构")#line:2601
    O00O0OO0O0000O0O0 .close ()#line:2602
    showinfo (title ="提示",message ="文件写入成功。")#line:2603
def TOOLS_web_view (O0000OO0O0O00OO00 ):#line:2605
    ""#line:2606
    import pybi as pbi #line:2607
    OO00OOOO0OO0000OO =pd .ExcelWriter ("temp_webview.xls")#line:2608
    O0000OO0O0O00OO00 .to_excel (OO00OOOO0OO0000OO ,sheet_name ="temp_webview")#line:2609
    OO00OOOO0OO0000OO .close ()#line:2610
    O0000OO0O0O00OO00 =pd .read_excel ("temp_webview.xls",header =0 ,sheet_name =0 ).reset_index (drop =True )#line:2611
    OO0OO000000O0O0O0 =pbi .set_source (O0000OO0O0O00OO00 )#line:2612
    with pbi .flowBox ():#line:2613
        for O00O000OOO0O0O0O0 in O0000OO0O0O00OO00 .columns :#line:2614
            pbi .add_slicer (OO0OO000000O0O0O0 [O00O000OOO0O0O0O0 ])#line:2615
    pbi .add_table (OO0OO000000O0O0O0 )#line:2616
    OOOOO0O00O0OO00O0 ="temp_webview.html"#line:2617
    pbi .to_html (OOOOO0O00O0OO00O0 )#line:2618
    webbrowser .open_new_tab (OOOOO0O00O0OO00O0 )#line:2619
def TOOLS_Autotable_0 (O0OOO0OOO000O0O00 ,O0O0O00OO0000000O ,*O00O00OO0OOO0OO00 ):#line:2624
    ""#line:2625
    OOOOOO0O0OOOO0O0O =[O00O00OO0OOO0OO00 [0 ],O00O00OO0OOO0OO00 [1 ],O00O00OO0OOO0OO00 [2 ]]#line:2627
    O0O000OO000OO0O00 =list (set ([OOOOO000000OO0O00 for OOOOO000000OO0O00 in OOOOOO0O0OOOO0O0O if OOOOO000000OO0O00 !='']))#line:2629
    O0O000OO000OO0O00 .sort (key =OOOOOO0O0OOOO0O0O .index )#line:2630
    if len (O0O000OO000OO0O00 )==0 :#line:2631
        showinfo (title ="提示信息",message ="分组项请选择至少一列。")#line:2632
        return 0 #line:2633
    O0O00OOOO0O00O000 =[O00O00OO0OOO0OO00 [3 ],O00O00OO0OOO0OO00 [4 ]]#line:2634
    if (O00O00OO0OOO0OO00 [3 ]==""or O00O00OO0OOO0OO00 [4 ]=="")and O0O0O00OO0000000O in ["数据透视","分组统计"]:#line:2635
        if "报告编码"in O0OOO0OOO000O0O00 .columns :#line:2636
            O0O00OOOO0O00O000 [0 ]="报告编码"#line:2637
            O0O00OOOO0O00O000 [1 ]="nunique"#line:2638
            text .insert (END ,"值项未配置,将使用报告编码进行唯一值计数。")#line:2639
        else :#line:2640
            showinfo (title ="提示信息",message ="值项未配置。")#line:2641
            return 0 #line:2642
    if O00O00OO0OOO0OO00 [4 ]=="计数":#line:2644
        O0O00OOOO0O00O000 [1 ]="count"#line:2645
    elif O00O00OO0OOO0OO00 [4 ]=="求和":#line:2646
        O0O00OOOO0O00O000 [1 ]="sum"#line:2647
    elif O00O00OO0OOO0OO00 [4 ]=="唯一值计数":#line:2648
        O0O00OOOO0O00O000 [1 ]="nunique"#line:2649
    if O0O0O00OO0000000O =="分组统计":#line:2652
        TABLE_tree_Level_2 (TOOLS_deep_view (O0OOO0OOO000O0O00 ,O0O000OO000OO0O00 ,O0O00OOOO0O00O000 ,0 ),1 ,O0OOO0OOO000O0O00 )#line:2653
    if O0O0O00OO0000000O =="数据透视":#line:2655
        TABLE_tree_Level_2 (TOOLS_deep_view (O0OOO0OOO000O0O00 ,O0O000OO000OO0O00 ,O0O00OOOO0O00O000 ,1 ),1 ,O0OOO0OOO000O0O00 )#line:2656
    if O0O0O00OO0000000O =="描述性统计":#line:2658
        TABLE_tree_Level_2 (O0OOO0OOO000O0O00 [O0O000OO000OO0O00 ].describe ().reset_index (),1 ,O0OOO0OOO000O0O00 )#line:2659
    if O0O0O00OO0000000O =="追加外部表格信息":#line:2662
        OO00OOO00O0OO00O0 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:2665
        OOOO0OOOO00O000O0 =[pd .read_excel (O0000OO00000O00OO ,header =0 ,sheet_name =0 )for O0000OO00000O00OO in OO00OOO00O0OO00O0 ]#line:2666
        OOOOO0O00O000OOO0 =pd .concat (OOOO0OOOO00O000O0 ,ignore_index =True ).drop_duplicates (O0O000OO000OO0O00 )#line:2667
        OOOO00O0O0OO000OO =pd .merge (O0OOO0OOO000O0O00 ,OOOOO0O00O000OOO0 ,on =O0O000OO000OO0O00 ,how ="left")#line:2668
        TABLE_tree_Level_2 (OOOO00O0O0OO000OO ,1 ,OOOO00O0O0OO000OO )#line:2669
    if O0O0O00OO0000000O =="添加到外部表格":#line:2671
        OO00OOO00O0OO00O0 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:2674
        OOOO0OOOO00O000O0 =[pd .read_excel (OOOO0O0OOOO0OOOOO ,header =0 ,sheet_name =0 )for OOOO0O0OOOO0OOOOO in OO00OOO00O0OO00O0 ]#line:2675
        OOOOO0O00O000OOO0 =pd .concat (OOOO0OOOO00O000O0 ,ignore_index =True ).drop_duplicates ()#line:2676
        OOOO00O0O0OO000OO =pd .merge (OOOOO0O00O000OOO0 ,O0OOO0OOO000O0O00 .drop_duplicates (O0O000OO000OO0O00 ),on =O0O000OO000OO0O00 ,how ="left")#line:2677
        TABLE_tree_Level_2 (OOOO00O0O0OO000OO ,1 ,OOOO00O0O0OO000OO )#line:2678
    if O0O0O00OO0000000O =="饼图(XY)":#line:2681
        DRAW_make_one (O0OOO0OOO000O0O00 ,"饼图",O00O00OO0OOO0OO00 [0 ],O00O00OO0OOO0OO00 [1 ],"饼图")#line:2682
    if O0O0O00OO0000000O =="柱状图(XY)":#line:2683
        DRAW_make_one (O0OOO0OOO000O0O00 ,"柱状图",O00O00OO0OOO0OO00 [0 ],O00O00OO0OOO0OO00 [1 ],"柱状图")#line:2684
    if O0O0O00OO0000000O =="折线图(XY)":#line:2685
        DRAW_make_one (O0OOO0OOO000O0O00 ,"折线图",O00O00OO0OOO0OO00 [0 ],O00O00OO0OOO0OO00 [1 ],"折线图")#line:2686
    if O0O0O00OO0000000O =="托帕斯图(XY)":#line:2687
        DRAW_make_one (O0OOO0OOO000O0O00 ,"托帕斯图",O00O00OO0OOO0OO00 [0 ],O00O00OO0OOO0OO00 [1 ],"托帕斯图")#line:2688
    if O0O0O00OO0000000O =="堆叠柱状图（X-YZ）":#line:2689
        DRAW_make_mutibar (O0OOO0OOO000O0O00 ,OOOOOO0O0OOOO0O0O [1 ],OOOOOO0O0OOOO0O0O [2 ],OOOOOO0O0OOOO0O0O [0 ],OOOOOO0O0OOOO0O0O [1 ],OOOOOO0O0OOOO0O0O [2 ],"堆叠柱状图")#line:2690
def STAT_countx (OOOOO0O00OO000O00 ):#line:2700
	""#line:2701
	return OOOOO0O00OO000O00 .value_counts ().to_dict ()#line:2702
def STAT_countpx (O0O0O00O0OO000OO0 ,O00OO0O000000O0O0 ):#line:2704
	""#line:2705
	return len (O0O0O00O0OO000OO0 [(O0O0O00O0OO000OO0 ==O00OO0O000000O0O0 )])#line:2706
def STAT_countnpx (O00O00O0O00O0O00O ,OO00O0OOO0OO00OO0 ):#line:2708
	""#line:2709
	return len (O00O00O0O00O0O00O [(O00O00O0O00O0O00O not in OO00O0OOO0OO00OO0 )])#line:2710
def STAT_get_max (OO000000OOOO000OO ):#line:2712
	""#line:2713
	return OO000000OOOO000OO .value_counts ().max ()#line:2714
def STAT_get_mean (O0O0OOOOO0000O00O ):#line:2716
	""#line:2717
	return round (O0O0OOOOO0000O00O .value_counts ().mean (),2 )#line:2718
def STAT_get_std (O0000OO0OO0OOO0O0 ):#line:2720
	""#line:2721
	return round (O0000OO0OO0OOO0O0 .value_counts ().std (ddof =1 ),2 )#line:2722
def STAT_get_95ci (OO0OOOOOO00OOO0O0 ):#line:2724
	""#line:2725
	return round (np .percentile (OO0OOOOOO00OOO0O0 .value_counts (),97.5 ),2 )#line:2726
def STAT_get_mean_std_ci (OOO00O0OOOOO000OO ,OOO00O0OO0O0O0000 ):#line:2728
	""#line:2729
	warnings .filterwarnings ("ignore")#line:2730
	O00OOOO0O00O0000O =TOOLS_strdict_to_pd (str (OOO00O0OOOOO000OO ))["content"].values /OOO00O0OO0O0O0000 #line:2731
	OOOOOO0O0OOO0OOOO =round (O00OOOO0O00O0000O .mean (),2 )#line:2732
	OO0OO00O0O0O0OOOO =round (O00OOOO0O00O0000O .std (ddof =1 ),2 )#line:2733
	O0O00OO0OO0OOO0OO =round (np .percentile (O00OOOO0O00O0000O ,97.5 ),2 )#line:2734
	return pd .Series ((OOOOOO0O0OOO0OOOO ,OO0OO00O0O0O0OOOO ,O0O00OO0OO0OOO0OO ))#line:2735
def STAT_findx_value (O00OOO0OO00OO00O0 ,O00OO000O0O00O0OO ):#line:2737
	""#line:2738
	warnings .filterwarnings ("ignore")#line:2739
	O0O00000O00OOOO0O =TOOLS_strdict_to_pd (str (O00OOO0OO00OO00O0 ))#line:2740
	O0O0O000OO0O00O0O =O0O00000O00OOOO0O .where (O0O00000O00OOOO0O ["index"]==str (O00OO000O0O00O0OO ))#line:2742
	print (O0O0O000OO0O00O0O )#line:2743
	return O0O0O000OO0O00O0O #line:2744
def STAT_judge_x (O000OOOOO000000OO ,OO0O0O0OO0O000O0O ):#line:2746
	""#line:2747
	for O0O000000OO00OOOO in OO0O0O0OO0O000O0O :#line:2748
		if O000OOOOO000000OO .find (O0O000000OO00OOOO )>-1 :#line:2749
			return 1 #line:2750
def STAT_recent30 (O00000O00O0O0OOOO ,O00O0OO0OO0000O00 ):#line:2752
	""#line:2753
	import datetime #line:2754
	O00O0OOOOOO00O00O =O00000O00O0O0OOOO [(O00000O00O0O0OOOO ["报告日期"].dt .date >(datetime .date .today ()-datetime .timedelta (days =30 )))]#line:2758
	O000OO0OOO00O000O =O00O0OOOOOO00O00O .groupby (O00O0OO0OO0000O00 ).agg (最近30天报告数 =("报告编码","nunique"),最近30天报告严重伤害数 =("伤害",lambda OOO000000OO0OO0O0 :STAT_countpx (OOO000000OO0OO0O0 .values ,"严重伤害")),最近30天报告死亡数量 =("伤害",lambda OOO00O0O00O0O0O00 :STAT_countpx (OOO00O0O00O0O0O00 .values ,"死亡")),最近30天报告单位个数 =("单位名称","nunique"),).reset_index ()#line:2765
	O000OO0OOO00O000O =STAT_basic_risk (O000OO0OOO00O000O ,"最近30天报告数","最近30天报告严重伤害数","最近30天报告死亡数量","最近30天报告单位个数").fillna (0 )#line:2766
	O000OO0OOO00O000O =O000OO0OOO00O000O .rename (columns ={"风险评分":"最近30天风险评分"})#line:2768
	return O000OO0OOO00O000O #line:2769
def STAT_PPR_ROR_1 (O0O00OOO000O00O00 ,O0OO0OOOOO0000O00 ,OOO000000000O0000 ,O00OO0000OO000O0O ,OO0O0O0OO0O00OOO0 ):#line:2772
    ""#line:2773
    OOOO0000OOOOO0O0O =OO0O0O0OO0O00OOO0 [(OO0O0O0OO0O00OOO0 [O0O00OOO000O00O00 ]==O0OO0OOOOO0000O00 )]#line:2776
    O0OOOO0O00O0OO00O =OOOO0000OOOOO0O0O .loc [OOOO0000OOOOO0O0O [OOO000000000O0000 ].str .contains (O00OO0000OO000O0O ,na =False )]#line:2777
    OO00OOOOO00000OO0 =OO0O0O0OO0O00OOO0 [(OO0O0O0OO0O00OOO0 [O0O00OOO000O00O00 ]!=O0OO0OOOOO0000O00 )]#line:2778
    OOO0OOOO0O0OOO0O0 =OO00OOOOO00000OO0 .loc [OO00OOOOO00000OO0 [OOO000000000O0000 ].str .contains (O00OO0000OO000O0O ,na =False )]#line:2779
    O00OO00OO0OOOO0OO =(len (O0OOOO0O00O0OO00O ),(len (OOOO0000OOOOO0O0O )-len (O0OOOO0O00O0OO00O )),len (OOO0OOOO0O0OOO0O0 ),(len (OO00OOOOO00000OO0 )-len (OOO0OOOO0O0OOO0O0 )))#line:2780
    if len (O0OOOO0O00O0OO00O )>0 :#line:2781
        OOO000OO0O00O0O0O =STAT_PPR_ROR_0 (len (O0OOOO0O00O0OO00O ),(len (OOOO0000OOOOO0O0O )-len (O0OOOO0O00O0OO00O )),len (OOO0OOOO0O0OOO0O0 ),(len (OO00OOOOO00000OO0 )-len (OOO0OOOO0O0OOO0O0 )))#line:2782
    else :#line:2783
        OOO000OO0O00O0O0O =(0 ,0 ,0 ,0 ,0 )#line:2784
    O000OO0O0O000000O =len (OOOO0000OOOOO0O0O )#line:2787
    if O000OO0O0O000000O ==0 :#line:2788
        O000OO0O0O000000O =0.5 #line:2789
    return (O00OO0000OO000O0O ,len (O0OOOO0O00O0OO00O ),round (len (O0OOOO0O00O0OO00O )/O000OO0O0O000000O *100 ,2 ),round (OOO000OO0O00O0O0O [0 ],2 ),round (OOO000OO0O00O0O0O [1 ],2 ),round (OOO000OO0O00O0O0O [2 ],2 ),round (OOO000OO0O00O0O0O [3 ],2 ),round (OOO000OO0O00O0O0O [4 ],2 ),str (O00OO00OO0OOOO0OO ),)#line:2800
def STAT_basic_risk (O00O000OOO0OOO0O0 ,O0000O0OOO0OOOOOO ,OO000000000OOO00O ,OO000O0O000OOOO00 ,O0000OO00O00OOO0O ):#line:2804
	""#line:2805
	O00O000OOO0OOO0O0 ["风险评分"]=0 #line:2806
	O00O000OOO0OOO0O0 .loc [((O00O000OOO0OOO0O0 [O0000O0OOO0OOOOOO ]>=3 )&(O00O000OOO0OOO0O0 [OO000000000OOO00O ]>=1 ))|(O00O000OOO0OOO0O0 [O0000O0OOO0OOOOOO ]>=5 ),"风险评分"]=O00O000OOO0OOO0O0 ["风险评分"]+5 #line:2807
	O00O000OOO0OOO0O0 .loc [(O00O000OOO0OOO0O0 [OO000000000OOO00O ]>=3 ),"风险评分"]=O00O000OOO0OOO0O0 ["风险评分"]+1 #line:2808
	O00O000OOO0OOO0O0 .loc [(O00O000OOO0OOO0O0 [OO000O0O000OOOO00 ]>=1 ),"风险评分"]=O00O000OOO0OOO0O0 ["风险评分"]+10 #line:2809
	O00O000OOO0OOO0O0 ["风险评分"]=O00O000OOO0OOO0O0 ["风险评分"]+O00O000OOO0OOO0O0 [O0000OO00O00OOO0O ]/100 #line:2810
	return O00O000OOO0OOO0O0 #line:2811
def STAT_PPR_ROR_0 (OOO0OO0OO00O0O00O ,OOOOO000OOOO00O00 ,O0OO0O0OOOO0OOOOO ,O0O00000000O000O0 ):#line:2814
    ""#line:2815
    if OOO0OO0OO00O0O00O *OOOOO000OOOO00O00 *O0OO0O0OOOO0OOOOO *O0O00000000O000O0 ==0 :#line:2820
        OOO0OO0OO00O0O00O =OOO0OO0OO00O0O00O +1 #line:2821
        OOOOO000OOOO00O00 =OOOOO000OOOO00O00 +1 #line:2822
        O0OO0O0OOOO0OOOOO =O0OO0O0OOOO0OOOOO +1 #line:2823
        O0O00000000O000O0 =O0O00000000O000O0 +1 #line:2824
    OOOOO0O00OO0OOOOO =(OOO0OO0OO00O0O00O /(OOO0OO0OO00O0O00O +OOOOO000OOOO00O00 ))/(O0OO0O0OOOO0OOOOO /(O0OO0O0OOOO0OOOOO +O0O00000000O000O0 ))#line:2825
    O00OOOO0O0O00O000 =math .sqrt (1 /OOO0OO0OO00O0O00O -1 /(OOO0OO0OO00O0O00O +OOOOO000OOOO00O00 )+1 /O0OO0O0OOOO0OOOOO -1 /(O0OO0O0OOOO0OOOOO +O0O00000000O000O0 ))#line:2826
    OO000000000000000 =(math .exp (math .log (OOOOO0O00OO0OOOOO )-1.96 *O00OOOO0O0O00O000 ),math .exp (math .log (OOOOO0O00OO0OOOOO )+1.96 *O00OOOO0O0O00O000 ),)#line:2830
    OOOOO0OOOO0000O00 =(OOO0OO0OO00O0O00O /O0OO0O0OOOO0OOOOO )/(OOOOO000OOOO00O00 /O0O00000000O000O0 )#line:2831
    OO00O00O000OO0O00 =math .sqrt (1 /OOO0OO0OO00O0O00O +1 /OOOOO000OOOO00O00 +1 /O0OO0O0OOOO0OOOOO +1 /O0O00000000O000O0 )#line:2832
    O0OO0O0OOO0O00OOO =(math .exp (math .log (OOOOO0OOOO0000O00 )-1.96 *OO00O00O000OO0O00 ),math .exp (math .log (OOOOO0OOOO0000O00 )+1.96 *OO00O00O000OO0O00 ),)#line:2836
    OO0OO00OOOOO0OO00 =((OOO0OO0OO00O0O00O *OOOOO000OOOO00O00 -OOOOO000OOOO00O00 *O0OO0O0OOOO0OOOOO )*(OOO0OO0OO00O0O00O *OOOOO000OOOO00O00 -OOOOO000OOOO00O00 *O0OO0O0OOOO0OOOOO )*(OOO0OO0OO00O0O00O +OOOOO000OOOO00O00 +O0OO0O0OOOO0OOOOO +O0O00000000O000O0 ))/((OOO0OO0OO00O0O00O +OOOOO000OOOO00O00 )*(O0OO0O0OOOO0OOOOO +O0O00000000O000O0 )*(OOO0OO0OO00O0O00O +O0OO0O0OOOO0OOOOO )*(OOOOO000OOOO00O00 +O0O00000000O000O0 ))#line:2839
    return OOOOO0OOOO0000O00 ,O0OO0O0OOO0O00OOO [0 ],OOOOO0O00OO0OOOOO ,OO000000000000000 [0 ],OO0OO00OOOOO0OO00 #line:2840
def STAT_find_keyword_risk (O0OOOOO0OO000O0O0 ,O000000OOO0O00OOO ,OO000OO00O0O00000 ,OOO0OO000000OOOO0 ,OOO0OO0O00OO0OO0O ):#line:2842
		""#line:2843
		OO000O000O0OO0O0O =O0OOOOO0OO000O0O0 .groupby (O000000OOO0O00OOO ).agg (证号关键字总数量 =(OO000OO00O0O00000 ,"count"),包含元素个数 =(OOO0OO000000OOOO0 ,"nunique"),包含元素 =(OOO0OO000000OOOO0 ,STAT_countx ),).reset_index ()#line:2848
		OOOO000000OO00O0O =O000000OOO0O00OOO .copy ()#line:2850
		OOOO000000OO00O0O .append (OOO0OO000000OOOO0 )#line:2851
		OOO0OO0OO0O00O0OO =O0OOOOO0OO000O0O0 .groupby (OOOO000000OO00O0O ).agg (计数 =(OOO0OO000000OOOO0 ,"count"),严重伤害数 =("伤害",lambda OOO0OO000OO0O000O :STAT_countpx (OOO0OO000OO0O000O .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0O000O0O0O00OO :STAT_countpx (O0O0O000O0O0O00OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:2858
		O00OOOO000O0O0000 =OOOO000000OO00O0O .copy ()#line:2861
		O00OOOO000O0O0000 .remove ("关键字")#line:2862
		O0O000OO0000OOO0O =O0OOOOO0OO000O0O0 .groupby (O00OOOO000O0O0000 ).agg (该元素总数 =(OOO0OO000000OOOO0 ,"count"),).reset_index ()#line:2865
		OOO0OO0OO0O00O0OO ["证号总数"]=OOO0OO0O00OO0OO0O #line:2867
		OOO0OO0OO0000O0O0 =pd .merge (OOO0OO0OO0O00O0OO ,OO000O000O0OO0O0O ,on =O000000OOO0O00OOO ,how ="left")#line:2868
		if len (OOO0OO0OO0000O0O0 )>0 :#line:2873
			OOO0OO0OO0000O0O0 [['数量均值','数量标准差','数量CI']]=OOO0OO0OO0000O0O0 .包含元素 .apply (lambda OO0OOO00O00O00OOO :STAT_get_mean_std_ci (OO0OOO00O00O00OOO ,1 ))#line:2874
		return OOO0OO0OO0000O0O0 #line:2877
def STAT_find_risk (OOO0OOOOOOO0O0O00 ,O000OOOOO0000O00O ,O0OOOO0O00000OOO0 ,OOOOOO0OOOO0OOOOO ):#line:2883
		""#line:2884
		OO00O0000OO0O00O0 =OOO0OOOOOOO0O0O00 .groupby (O000OOOOO0000O00O ).agg (证号总数量 =(O0OOOO0O00000OOO0 ,"count"),包含元素个数 =(OOOOOO0OOOO0OOOOO ,"nunique"),包含元素 =(OOOOOO0OOOO0OOOOO ,STAT_countx ),均值 =(OOOOOO0OOOO0OOOOO ,STAT_get_mean ),标准差 =(OOOOOO0OOOO0OOOOO ,STAT_get_std ),CI上限 =(OOOOOO0OOOO0OOOOO ,STAT_get_95ci ),).reset_index ()#line:2892
		O00O0O0O0OO000OO0 =O000OOOOO0000O00O .copy ()#line:2894
		O00O0O0O0OO000OO0 .append (OOOOOO0OOOO0OOOOO )#line:2895
		OOOOOOO0OOO00OO0O =OOO0OOOOOOO0O0O00 .groupby (O00O0O0O0OO000OO0 ).agg (计数 =(OOOOOO0OOOO0OOOOO ,"count"),严重伤害数 =("伤害",lambda OOOOOOO0000O00OO0 :STAT_countpx (OOOOOOO0000O00OO0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0O0OO0OO0OO000 :STAT_countpx (O0O0O0OO0OO0OO000 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:2902
		OOO0OO0OO0OO0O0O0 =pd .merge (OOOOOOO0OOO00OO0O ,OO00O0000OO0O00O0 ,on =O000OOOOO0000O00O ,how ="left")#line:2904
		OOO0OO0OO0OO0O0O0 ["风险评分"]=0 #line:2906
		OOO0OO0OO0OO0O0O0 ["报表类型"]="dfx_findrisk"+OOOOOO0OOOO0OOOOO #line:2907
		OOO0OO0OO0OO0O0O0 .loc [((OOO0OO0OO0OO0O0O0 ["计数"]>=3 )&(OOO0OO0OO0OO0O0O0 ["严重伤害数"]>=1 )|(OOO0OO0OO0OO0O0O0 ["计数"]>=5 )),"风险评分"]=OOO0OO0OO0OO0O0O0 ["风险评分"]+5 #line:2908
		OOO0OO0OO0OO0O0O0 .loc [(OOO0OO0OO0OO0O0O0 ["计数"]>=(OOO0OO0OO0OO0O0O0 ["均值"]+OOO0OO0OO0OO0O0O0 ["标准差"])),"风险评分"]=OOO0OO0OO0OO0O0O0 ["风险评分"]+1 #line:2909
		OOO0OO0OO0OO0O0O0 .loc [(OOO0OO0OO0OO0O0O0 ["计数"]>=OOO0OO0OO0OO0O0O0 ["CI上限"]),"风险评分"]=OOO0OO0OO0OO0O0O0 ["风险评分"]+1 #line:2910
		OOO0OO0OO0OO0O0O0 .loc [(OOO0OO0OO0OO0O0O0 ["严重伤害数"]>=3 )&(OOO0OO0OO0OO0O0O0 ["风险评分"]>=7 ),"风险评分"]=OOO0OO0OO0OO0O0O0 ["风险评分"]+1 #line:2911
		OOO0OO0OO0OO0O0O0 .loc [(OOO0OO0OO0OO0O0O0 ["死亡数量"]>=1 ),"风险评分"]=OOO0OO0OO0OO0O0O0 ["风险评分"]+10 #line:2912
		OOO0OO0OO0OO0O0O0 ["风险评分"]=OOO0OO0OO0OO0O0O0 ["风险评分"]+OOO0OO0OO0OO0O0O0 ["单位个数"]/100 #line:2913
		OOO0OO0OO0OO0O0O0 =OOO0OO0OO0OO0O0O0 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:2914
		return OOO0OO0OO0OO0O0O0 #line:2916
def TABLE_tree_Level_2 (OOO00000O0000O00O ,O0OO0OO0000OO00O0 ,OO0O0O00OOO0O0OOO ,*O000OOOOOO00OO0OO ):#line:2923
    ""#line:2924
    try :#line:2926
        O00OOOO00O00OOO00 =OOO00000O0000O00O .columns #line:2927
    except :#line:2928
        return 0 #line:2929
    if "报告编码"in OOO00000O0000O00O .columns :#line:2931
        O0OO0OO0000OO00O0 =0 #line:2932
    try :#line:2933
        OO00OO0OOOO0OOO0O =len (np .unique (OOO00000O0000O00O ["注册证编号/曾用注册证编号"].values ))#line:2934
    except :#line:2935
        OO00OO0OOOO0OOO0O =10 #line:2936
    OO0O00OO0OO0OO0OO =Toplevel ()#line:2939
    OO0O00OO0OO0OO0OO .title ("报表查看器")#line:2940
    OO000000000OOOOO0 =OO0O00OO0OO0OO0OO .winfo_screenwidth ()#line:2941
    O0OOO0O00OO0OO00O =OO0O00OO0OO0OO0OO .winfo_screenheight ()#line:2943
    O0O00O0O0OO00OO0O =1310 #line:2945
    OOO0OOOO0OOOO00O0 =600 #line:2946
    OO0OO0OO0O00O00OO =(OO000000000OOOOO0 -O0O00O0O0OO00OO0O )/2 #line:2948
    O0O00OOOOOOO0O00O =(O0OOO0O00OO0OO00O -OOO0OOOO0OOOO00O0 )/2 #line:2949
    OO0O00OO0OO0OO0OO .geometry ("%dx%d+%d+%d"%(O0O00O0O0OO00OO0O ,OOO0OOOO0OOOO00O0 ,OO0OO0OO0O00O00OO ,O0O00OOOOOOO0O00O ))#line:2950
    OO0O0O00000OO0O00 =ttk .Frame (OO0O00OO0OO0OO0OO ,width =1310 ,height =20 )#line:2953
    OO0O0O00000OO0O00 .pack (side =TOP )#line:2954
    O00OOOO00O00O0000 =ttk .Frame (OO0O00OO0OO0OO0OO ,width =1310 ,height =20 )#line:2955
    O00OOOO00O00O0000 .pack (side =BOTTOM )#line:2956
    OO00O00O0OO0OO00O =ttk .Frame (OO0O00OO0OO0OO0OO ,width =1310 ,height =600 )#line:2957
    OO00O00O0OO0OO00O .pack (fill ="both",expand ="false")#line:2958
    if O0OO0OO0000OO00O0 ==0 :#line:2962
        PROGRAM_Menubar (OO0O00OO0OO0OO0OO ,OOO00000O0000O00O ,O0OO0OO0000OO00O0 ,OO0O0O00OOO0O0OOO )#line:2963
    try :#line:2966
        OO000OOO000OOOOO0 =StringVar ()#line:2967
        OO000OOO000OOOOO0 .set ("产品类别")#line:2968
        def OOOOO00O00O0OO000 (*O0O0O0OO000OOOOO0 ):#line:2969
            OO000OOO000OOOOO0 .set (OO0O0O0O0O0OOO0O0 .get ())#line:2970
        OO000O0O0OO00O0O0 =StringVar ()#line:2971
        OO000O0O0OO00O0O0 .set ("无源|诊断试剂")#line:2972
        OOO00O0OO00O0OOOO =Label (OO0O0O00000OO0O00 ,text ="")#line:2973
        OOO00O0OO00O0OOOO .pack (side =LEFT )#line:2974
        OOO00O0OO00O0OOOO =Label (OO0O0O00000OO0O00 ,text ="位置：")#line:2975
        OOO00O0OO00O0OOOO .pack (side =LEFT )#line:2976
        O00OO0OOO0000OOOO =StringVar ()#line:2977
        OO0O0O0O0O0OOO0O0 =ttk .Combobox (OO0O0O00000OO0O00 ,width =12 ,height =30 ,state ="readonly",textvariable =O00OO0OOO0000OOOO )#line:2980
        OO0O0O0O0O0OOO0O0 ["values"]=OOO00000O0000O00O .columns .tolist ()#line:2981
        OO0O0O0O0O0OOO0O0 .current (0 )#line:2982
        OO0O0O0O0O0OOO0O0 .bind ("<<ComboboxSelected>>",OOOOO00O00O0OO000 )#line:2983
        OO0O0O0O0O0OOO0O0 .pack (side =LEFT )#line:2984
        O00000OO0OO0000O0 =Label (OO0O0O00000OO0O00 ,text ="检索：")#line:2985
        O00000OO0OO0000O0 .pack (side =LEFT )#line:2986
        O00O00OOOO0O00O00 =Entry (OO0O0O00000OO0O00 ,width =12 ,textvariable =OO000O0O0OO00O0O0 ).pack (side =LEFT )#line:2987
        def OO0OO00OO0OO0OO00 ():#line:2989
            pass #line:2990
        O0000OOO00O0O0OOO =Button (OO0O0O00000OO0O00 ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (OOO00000O0000O00O ),)#line:3004
        O0000OOO00O0O0OOO .pack (side =LEFT )#line:3005
        O00O000O00O0000OO =Button (OO0O0O00000OO0O00 ,text ="视图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_easyreadT (OOO00000O0000O00O ),1 ,OO0O0O00OOO0O0OOO ),)#line:3014
        if "详细描述T"not in OOO00000O0000O00O .columns :#line:3015
            O00O000O00O0000OO .pack (side =LEFT )#line:3016
        O00O000O00O0000OO =Button (OO0O0O00000OO0O00 ,text ="网",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_web_view (OOO00000O0000O00O ),)#line:3026
        if "详细描述T"not in OOO00000O0000O00O .columns :#line:3027
            O00O000O00O0000OO .pack (side =LEFT )#line:3028
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="含",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .loc [OOO00000O0000O00O [OO000OOO000OOOOO0 .get ()].astype (str ).str .contains (str (OO000O0O0OO00O0O0 .get ()),na =False )],1 ,OO0O0O00OOO0O0OOO ,),)#line:3046
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3047
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="无",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .loc [~OOO00000O0000O00O [OO000OOO000OOOOO0 .get ()].astype (str ).str .contains (str (OO000O0O0OO00O0O0 .get ()),na =False )],1 ,OO0O0O00OOO0O0OOO ,),)#line:3064
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3065
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="大",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .loc [OOO00000O0000O00O [OO000OOO000OOOOO0 .get ()].astype (float )>float (OO000O0O0OO00O0O0 .get ())],1 ,OO0O0O00OOO0O0OOO ,),)#line:3080
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3081
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="小",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .loc [OOO00000O0000O00O [OO000OOO000OOOOO0 .get ()].astype (float )<float (OO000O0O0OO00O0O0 .get ())],1 ,OO0O0O00OOO0O0OOO ,),)#line:3096
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3097
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="等",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .loc [OOO00000O0000O00O [OO000OOO000OOOOO0 .get ()].astype (float )==float (OO000O0O0OO00O0O0 .get ())],1 ,OO0O0O00OOO0O0OOO ,),)#line:3112
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3113
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="式",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_findin (OOO00000O0000O00O ,OO0O0O00OOO0O0OOO ))#line:3122
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3123
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="前",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .head (int (OO000O0O0OO00O0O0 .get ())),1 ,OO0O0O00OOO0O0OOO ,),)#line:3138
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3139
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="升",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .sort_values (by =(OO000OOO000OOOOO0 .get ()),ascending =[True ],na_position ="last"),1 ,OO0O0O00OOO0O0OOO ,),)#line:3154
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3155
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="降",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O .sort_values (by =(OO000OOO000OOOOO0 .get ()),ascending =[False ],na_position ="last"),1 ,OO0O0O00OOO0O0OOO ,),)#line:3170
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3171
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="SQL",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_sql (OOO00000O0000O00O ),)#line:3181
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3182
    except :#line:3185
        pass #line:3186
    if ini ["模式"]!="其他":#line:3189
        O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="近月",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O [(OOO00000O0000O00O ["最近30天报告单位个数"]>=1 )],1 ,OO0O0O00OOO0O0OOO ,),)#line:3202
        if "最近30天报告数"in OOO00000O0000O00O .columns :#line:3203
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3204
        OO0OOO00OO0OO000O =Button (OO0O0O00000OO0O00 ,text ="图表",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (OOO00000O0000O00O ),)#line:3216
        if O0OO0OO0000OO00O0 !=0 :#line:3217
            OO0OOO00OO0OO000O .pack (side =LEFT )#line:3218
        def OOO000OOO0O0000O0 ():#line:3223
            pass #line:3224
        if O0OO0OO0000OO00O0 ==0 :#line:3227
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="精简",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_easyread2 (OOO00000O0000O00O ),1 ,OO0O0O00OOO0O0OOO ,),)#line:3241
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3242
        if O0OO0OO0000OO00O0 ==0 :#line:3245
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="证号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_zhenghao (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3259
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3260
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OOO00000O0000O00O ).df_zhenghao ()))#line:3269
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3270
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="批号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_pihao (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3285
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3286
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OOO00000O0000O00O ).df_pihao ()))#line:3295
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3296
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="型号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_xinghao (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3311
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3312
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OOO00000O0000O00O ).df_xinghao ()))#line:3321
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3322
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="规格",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_guige (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3337
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3338
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OOO00000O0000O00O ).df_guige ()))#line:3347
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3348
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="企业",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_chiyouren (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3363
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3364
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="县区",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_org ("监测机构"),1 ,OO0O0O00OOO0O0OOO ,),)#line:3380
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3381
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="单位",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_user (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3394
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3395
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="年龄",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_age (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3409
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3410
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="时隔",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_deep_view (OOO00000O0000O00O ,["时隔"],["报告编码","nunique"],0 ),1 ,OO0O0O00OOO0O0OOO ,),)#line:3424
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3425
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="表现",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OOO00000O0000O00O ).df_psur (),1 ,OO0O0O00OOO0O0OOO ,),)#line:3439
            if "UDI"not in OOO00000O0000O00O .columns :#line:3440
                O000OOO0OOOOO0000 .pack (side =LEFT )#line:3441
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="表现",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_get_guize2 (OOO00000O0000O00O ),1 ,OO0O0O00OOO0O0OOO ,),)#line:3454
            if "UDI"in OOO00000O0000O00O .columns :#line:3455
                O000OOO0OOOOO0000 .pack (side =LEFT )#line:3456
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="发生时间",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_time (OOO00000O0000O00O ,"事件发生日期",0 ),)#line:3465
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3466
            O000OOO0OOOOO0000 =Button (OO0O0O00000OO0O00 ,text ="报告时间",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_one (TOOLS_time (OOO00000O0000O00O ,"报告日期",1 ),"时间托帕斯图","time","报告总数","超级托帕斯图(严重伤害数)"),)#line:3476
            O000OOO0OOOOO0000 .pack (side =LEFT )#line:3477
    try :#line:3483
        OO000OO00O0O000OO =ttk .Label (O00OOOO00O00O0000 ,text ="方法：")#line:3485
        OO000OO00O0O000OO .pack (side =LEFT )#line:3486
        OO0O0O0O0OOOOO00O =StringVar ()#line:3487
        O0000O00000000OOO =ttk .Combobox (O00OOOO00O00O0000 ,width =15 ,textvariable =OO0O0O0O0OOOOO00O ,state ='readonly')#line:3488
        O0000O00000000OOO ['values']=("分组统计","数据透视","描述性统计","饼图(XY)","柱状图(XY)","折线图(XY)","托帕斯图(XY)","堆叠柱状图（X-YZ）","追加外部表格信息","添加到外部表格")#line:3489
        O0000O00000000OOO .pack (side =LEFT )#line:3493
        O0000O00000000OOO .current (0 )#line:3494
        O000000OOOO00O00O =ttk .Label (O00OOOO00O00O0000 ,text ="分组列（X-Y-Z）:")#line:3495
        O000000OOOO00O00O .pack (side =LEFT )#line:3496
        OO0O0OOOO000O0OO0 =StringVar ()#line:3499
        OOO00O0000000OOO0 =ttk .Combobox (O00OOOO00O00O0000 ,width =15 ,textvariable =OO0O0OOOO000O0OO0 ,state ='readonly')#line:3500
        OOO00O0000000OOO0 ['values']=OOO00000O0000O00O .columns .tolist ()#line:3501
        OOO00O0000000OOO0 .pack (side =LEFT )#line:3502
        O00OOO0O0O00OOOOO =StringVar ()#line:3503
        O0O000OOO00000O00 =ttk .Combobox (O00OOOO00O00O0000 ,width =15 ,textvariable =O00OOO0O0O00OOOOO ,state ='readonly')#line:3504
        O0O000OOO00000O00 ['values']=OOO00000O0000O00O .columns .tolist ()#line:3505
        O0O000OOO00000O00 .pack (side =LEFT )#line:3506
        O00O0OO0O0O0000O0 =StringVar ()#line:3507
        O0000O0O00000O00O =ttk .Combobox (O00OOOO00O00O0000 ,width =15 ,textvariable =O00O0OO0O0O0000O0 ,state ='readonly')#line:3508
        O0000O0O00000O00O ['values']=OOO00000O0000O00O .columns .tolist ()#line:3509
        O0000O0O00000O00O .pack (side =LEFT )#line:3510
        OO0O0O00O0OOOO0O0 =StringVar ()#line:3511
        OOOO000OOOOO00OOO =StringVar ()#line:3512
        O000000OOOO00O00O =ttk .Label (O00OOOO00O00O0000 ,text ="计算列（V-M）:")#line:3513
        O000000OOOO00O00O .pack (side =LEFT )#line:3514
        OO00O0OO00OOOOOO0 =ttk .Combobox (O00OOOO00O00O0000 ,width =10 ,textvariable =OO0O0O00O0OOOO0O0 ,state ='readonly')#line:3516
        OO00O0OO00OOOOOO0 ['values']=OOO00000O0000O00O .columns .tolist ()#line:3517
        OO00O0OO00OOOOOO0 .pack (side =LEFT )#line:3518
        O0OO000O0O00000OO =ttk .Combobox (O00OOOO00O00O0000 ,width =10 ,textvariable =OOOO000OOOOO00OOO ,state ='readonly')#line:3519
        O0OO000O0O00000OO ['values']=["计数","求和","唯一值计数"]#line:3520
        O0OO000O0O00000OO .pack (side =LEFT )#line:3521
        OOO0OOO000OO0000O =Button (O00OOOO00O00O0000 ,text ="自助报表",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_Autotable_0 (OOO00000O0000O00O ,O0000O00000000OOO .get (),OO0O0OOOO000O0OO0 .get (),O00OOO0O0O00OOOOO .get (),O00O0OO0O0O0000O0 .get (),OO0O0O00O0OOOO0O0 .get (),OOOO000OOOOO00OOO .get (),OOO00000O0000O00O ))#line:3523
        OOO0OOO000OO0000O .pack (side =LEFT )#line:3524
        OO0OOO00OO0OO000O =Button (O00OOOO00O00O0000 ,text ="去首行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O [1 :],1 ,OO0O0O00OOO0O0OOO ,))#line:3541
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3542
        OO0OOO00OO0OO000O =Button (O00OOOO00O00O0000 ,text ="去尾行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OOO00000O0000O00O [:-1 ],1 ,OO0O0O00OOO0O0OOO ,),)#line:3557
        OO0OOO00OO0OO000O .pack (side =LEFT )#line:3558
        O000OOO0OOOOO0000 =Button (O00OOOO00O00O0000 ,text ="行数:"+str (len (OOO00000O0000O00O )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:3568
        O000OOO0OOOOO0000 .pack (side =LEFT )#line:3569
    except :#line:3572
        showinfo (title ="提示信息",message ="界面初始化失败。")#line:3573
    O0OOOO000OOOOO00O =OOO00000O0000O00O .values .tolist ()#line:3579
    O0O00O0O0O00OO000 =OOO00000O0000O00O .columns .values .tolist ()#line:3580
    O0O00O000000OO000 =ttk .Treeview (OO00O00O0OO0OO00O ,columns =O0O00O0O0O00OO000 ,show ="headings",height =45 )#line:3581
    for OOO000O00O0O0O000 in O0O00O0O0O00OO000 :#line:3584
        O0O00O000000OO000 .heading (OOO000O00O0O0O000 ,text =OOO000O00O0O0O000 )#line:3585
    for O00O0OO0O000O00O0 in O0OOOO000OOOOO00O :#line:3586
        O0O00O000000OO000 .insert ("","end",values =O00O0OO0O000O00O0 )#line:3587
    for O0000000000O00O0O in O0O00O0O0O00OO000 :#line:3589
        try :#line:3590
            O0O00O000000OO000 .column (O0000000000O00O0O ,minwidth =0 ,width =80 ,stretch =NO )#line:3591
            if "只剩"in O0000000000O00O0O :#line:3592
                O0O00O000000OO000 .column (O0000000000O00O0O ,minwidth =0 ,width =150 ,stretch =NO )#line:3593
        except :#line:3594
            pass #line:3595
    OOO00O0O000OOOOO0 =["评分说明"]#line:3599
    OOOO00OO0O0OO0O00 =["该单位喜好上报的品种统计","报告编码","产品名称","上报机构描述","持有人处理描述","该注册证编号/曾用注册证编号报告数量","通用名称","该批准文号报告数量","上市许可持有人名称",]#line:3612
    O00OOO00OO00O0OO0 =["注册证编号/曾用注册证编号","监测机构","报告月份","报告季度","单位列表","单位名称",]#line:3620
    OO00O00OOO0000OO0 =["管理类别",]#line:3624
    for O0000000000O00O0O in OOOO00OO0O0OO0O00 :#line:3627
        try :#line:3628
            O0O00O000000OO000 .column (O0000000000O00O0O ,minwidth =0 ,width =200 ,stretch =NO )#line:3629
        except :#line:3630
            pass #line:3631
    for O0000000000O00O0O in O00OOO00OO00O0OO0 :#line:3634
        try :#line:3635
            O0O00O000000OO000 .column (O0000000000O00O0O ,minwidth =0 ,width =140 ,stretch =NO )#line:3636
        except :#line:3637
            pass #line:3638
    for O0000000000O00O0O in OO00O00OOO0000OO0 :#line:3639
        try :#line:3640
            O0O00O000000OO000 .column (O0000000000O00O0O ,minwidth =0 ,width =40 ,stretch =NO )#line:3641
        except :#line:3642
            pass #line:3643
    for O0000000000O00O0O in OOO00O0O000OOOOO0 :#line:3644
        try :#line:3645
            O0O00O000000OO000 .column (O0000000000O00O0O ,minwidth =0 ,width =800 ,stretch =NO )#line:3646
        except :#line:3647
            pass #line:3648
    try :#line:3650
        O0O00O000000OO000 .column ("请选择需要查看的表格",minwidth =1 ,width =300 ,stretch =NO )#line:3653
    except :#line:3654
        pass #line:3655
    try :#line:3657
        O0O00O000000OO000 .column ("详细描述T",minwidth =1 ,width =2300 ,stretch =NO )#line:3660
    except :#line:3661
        pass #line:3662
    OO0O0OO000000OOOO =Scrollbar (OO00O00O0OO0OO00O ,orient ="vertical")#line:3664
    OO0O0OO000000OOOO .pack (side =RIGHT ,fill =Y )#line:3665
    OO0O0OO000000OOOO .config (command =O0O00O000000OO000 .yview )#line:3666
    O0O00O000000OO000 .config (yscrollcommand =OO0O0OO000000OOOO .set )#line:3667
    OO000OO0OOOOOO00O =Scrollbar (OO00O00O0OO0OO00O ,orient ="horizontal")#line:3669
    OO000OO0OOOOOO00O .pack (side =BOTTOM ,fill =X )#line:3670
    OO000OO0OOOOOO00O .config (command =O0O00O000000OO000 .xview )#line:3671
    O0O00O000000OO000 .config (yscrollcommand =OO0O0OO000000OOOO .set )#line:3672
    def OOO0000000O0OO000 (OO0O00O0O000O00O0 ,O000O0OOOOOO0OOO0 ,O00000OOOOO0OO000 ):#line:3675
        for O0O0OO00OOO0O0OOO in O0O00O000000OO000 .selection ():#line:3677
            O0OOOO0OO0O00OOOO =O0O00O000000OO000 .item (O0O0OO00OOO0O0OOO ,"values")#line:3678
        O00000O00O0O0O000 =dict (zip (O000O0OOOOOO0OOO0 ,O0OOOO0OO0O00OOOO ))#line:3679
        if "详细描述T"in O000O0OOOOOO0OOO0 and "{"in O00000O00O0O0O000 ["详细描述T"]:#line:3683
            OOOO000O000OO0000 =eval (O00000O00O0O0O000 ["详细描述T"])#line:3684
            OOOO000O000OO0000 =pd .DataFrame .from_dict (OOOO000O000OO0000 ,orient ="index",columns =["content"]).reset_index ()#line:3685
            OOOO000O000OO0000 =OOOO000O000OO0000 .sort_values (by ="content",ascending =[False ],na_position ="last")#line:3686
            DRAW_make_one (OOOO000O000OO0000 ,O00000O00O0O0O000 ["条目"],"index","content","饼图")#line:3687
            return 0 #line:3688
        if "dfx_deepview"in O00000O00O0O0O000 ["报表类型"]:#line:3693
            O0OO000OOOOO0OO0O =eval (O00000O00O0O0O000 ["报表类型"][13 :])#line:3694
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 .copy ()#line:3695
            for O0OO0O0O0000OO0O0 in O0OO000OOOOO0OO0O :#line:3696
                OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 [(OO0O0OOO0OOOOOOO0 [O0OO0O0O0000OO0O0 ]==O0OOOO0OO0O00OOOO [O0OO000OOOOO0OO0O .index (O0OO0O0O0000OO0O0 )])].copy ()#line:3697
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_deepview"#line:3698
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3699
            return 0 #line:3700
        if "dfx_deepvie2"in O00000O00O0O0O000 ["报表类型"]:#line:3703
            O0OO000OOOOO0OO0O =eval (O00000O00O0O0O000 ["报表类型"][13 :])#line:3704
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 .copy ()#line:3705
            for O0OO0O0O0000OO0O0 in O0OO000OOOOO0OO0O :#line:3706
                OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 [OO0O0OOO0OOOOOOO0 [O0OO0O0O0000OO0O0 ].str .contains (O0OOOO0OO0O00OOOO [O0OO000OOOOO0OO0O .index (O0OO0O0O0000OO0O0 )],na =False )].copy ()#line:3707
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_deepview"#line:3708
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3709
            return 0 #line:3710
        if "dfx_zhenghao"in O00000O00O0O0O000 ["报表类型"]:#line:3714
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["注册证编号/曾用注册证编号"]==O00000O00O0O0O000 ["注册证编号/曾用注册证编号"])].copy ()#line:3715
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_zhenghao"#line:3716
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3717
            return 0 #line:3718
        if ("dfx_pihao"in O00000O00O0O0O000 ["报表类型"]or "dfx_findrisk"in O00000O00O0O0O000 ["报表类型"]or "dfx_xinghao"in O00000O00O0O0O000 ["报表类型"]or "dfx_guige"in O00000O00O0O0O000 ["报表类型"])and OO00OO0OOOO0OOO0O ==1 :#line:3722
            O00000000O00000OO ="CLT"#line:3723
            if "pihao"in O00000O00O0O0O000 ["报表类型"]or "产品批号"in O00000O00O0O0O000 ["报表类型"]:#line:3724
                O00000000O00000OO ="产品批号"#line:3725
            if "xinghao"in O00000O00O0O0O000 ["报表类型"]or "型号"in O00000O00O0O0O000 ["报表类型"]:#line:3726
                O00000000O00000OO ="型号"#line:3727
            if "guige"in O00000O00O0O0O000 ["报表类型"]or "规格"in O00000O00O0O0O000 ["报表类型"]:#line:3728
                O00000000O00000OO ="规格"#line:3729
            if "事件发生季度"in O00000O00O0O0O000 ["报表类型"]:#line:3730
                O00000000O00000OO ="事件发生季度"#line:3731
            if "事件发生月份"in O00000O00O0O0O000 ["报表类型"]:#line:3732
                O00000000O00000OO ="事件发生月份"#line:3733
            if "性别"in O00000O00O0O0O000 ["报表类型"]:#line:3734
                O00000000O00000OO ="性别"#line:3735
            if "年龄段"in O00000O00O0O0O000 ["报表类型"]:#line:3736
                O00000000O00000OO ="年龄段"#line:3737
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["注册证编号/曾用注册证编号"]==O00000O00O0O0O000 ["注册证编号/曾用注册证编号"])&(O00000OOOOO0OO000 [O00000000O00000OO ]==O00000O00O0O0O000 [O00000000O00000OO ])].copy ()#line:3738
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_pihao"#line:3739
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3740
            return 0 #line:3741
        if ("findrisk"in O00000O00O0O0O000 ["报表类型"]or "dfx_pihao"in O00000O00O0O0O000 ["报表类型"]or "dfx_xinghao"in O00000O00O0O0O000 ["报表类型"]or "dfx_guige"in O00000O00O0O0O000 ["报表类型"])and OO00OO0OOOO0OOO0O !=1 :#line:3745
            OO0O0OOO0OOOOOOO0 =OOO00000O0000O00O [(OOO00000O0000O00O ["注册证编号/曾用注册证编号"]==O00000O00O0O0O000 ["注册证编号/曾用注册证编号"])].copy ()#line:3746
            OO0O0OOO0OOOOOOO0 ["报表类型"]=O00000O00O0O0O000 ["报表类型"]+"1"#line:3747
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,1 ,O00000OOOOO0OO000 )#line:3748
            return 0 #line:3750
        if "dfx_org监测机构"in O00000O00O0O0O000 ["报表类型"]:#line:3753
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["监测机构"]==O00000O00O0O0O000 ["监测机构"])].copy ()#line:3754
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_org"#line:3755
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3756
            return 0 #line:3757
        if "dfx_org市级监测机构"in O00000O00O0O0O000 ["报表类型"]:#line:3759
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["市级监测机构"]==O00000O00O0O0O000 ["市级监测机构"])].copy ()#line:3760
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_org"#line:3761
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3762
            return 0 #line:3763
        if "dfx_user"in O00000O00O0O0O000 ["报表类型"]:#line:3766
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["单位名称"]==O00000O00O0O0O000 ["单位名称"])].copy ()#line:3767
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_user"#line:3768
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3769
            return 0 #line:3770
        if "dfx_chiyouren"in O00000O00O0O0O000 ["报表类型"]:#line:3774
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["上市许可持有人名称"]==O00000O00O0O0O000 ["上市许可持有人名称"])].copy ()#line:3775
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_chiyouren"#line:3776
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3777
            return 0 #line:3778
        if "dfx_chanpin"in O00000O00O0O0O000 ["报表类型"]:#line:3780
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["产品名称"]==O00000O00O0O0O000 ["产品名称"])].copy ()#line:3781
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_chanpin"#line:3782
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3783
            return 0 #line:3784
        if "dfx_findrisk事件发生季度1"in O00000O00O0O0O000 ["报表类型"]:#line:3789
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["注册证编号/曾用注册证编号"]==O00000O00O0O0O000 ["注册证编号/曾用注册证编号"])&(O00000OOOOO0OO000 ["事件发生季度"]==O00000O00O0O0O000 ["事件发生季度"])].copy ()#line:3790
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_findrisk事件发生季度"#line:3791
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3792
            return 0 #line:3793
        if "dfx_findrisk事件发生月份1"in O00000O00O0O0O000 ["报表类型"]:#line:3796
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["注册证编号/曾用注册证编号"]==O00000O00O0O0O000 ["注册证编号/曾用注册证编号"])&(O00000OOOOO0OO000 ["事件发生月份"]==O00000O00O0O0O000 ["事件发生月份"])].copy ()#line:3797
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_dfx_findrisk事件发生月份"#line:3798
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3799
            return 0 #line:3800
        if ("keyword_findrisk"in O00000O00O0O0O000 ["报表类型"])and OO00OO0OOOO0OOO0O ==1 :#line:3803
            O00000000O00000OO ="CLT"#line:3804
            if "批号"in O00000O00O0O0O000 ["报表类型"]:#line:3805
                O00000000O00000OO ="产品批号"#line:3806
            if "事件发生季度"in O00000O00O0O0O000 ["报表类型"]:#line:3807
                O00000000O00000OO ="事件发生季度"#line:3808
            if "事件发生月份"in O00000O00O0O0O000 ["报表类型"]:#line:3809
                O00000000O00000OO ="事件发生月份"#line:3810
            if "性别"in O00000O00O0O0O000 ["报表类型"]:#line:3811
                O00000000O00000OO ="性别"#line:3812
            if "年龄段"in O00000O00O0O0O000 ["报表类型"]:#line:3813
                O00000000O00000OO ="年龄段"#line:3814
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 [(O00000OOOOO0OO000 ["注册证编号/曾用注册证编号"]==O00000O00O0O0O000 ["注册证编号/曾用注册证编号"])&(O00000OOOOO0OO000 [O00000000O00000OO ]==O00000O00O0O0O000 [O00000000O00000OO ])].copy ()#line:3815
            OO0O0OOO0OOOOOOO0 ["关键字查找列"]=""#line:3816
            for O00OO0OOOOO000OO0 in TOOLS_get_list (O00000O00O0O0O000 ["关键字查找列"]):#line:3817
                OO0O0OOO0OOOOOOO0 ["关键字查找列"]=OO0O0OOO0OOOOOOO0 ["关键字查找列"]+OO0O0OOO0OOOOOOO0 [O00OO0OOOOO000OO0 ].astype ("str")#line:3818
            OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 [(OO0O0OOO0OOOOOOO0 ["关键字查找列"].str .contains (O00000O00O0O0O000 ["关键字组合"],na =False ))]#line:3819
            if str (O00000O00O0O0O000 ["排除值"])!="nan":#line:3821
                OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 .loc [~OO0O0OOO0OOOOOOO0 ["关键字查找列"].str .contains (O00000O00O0O0O000 ["排除值"],na =False )]#line:3822
            OO0O0OOO0OOOOOOO0 ["报表类型"]="ori_"+O00000O00O0O0O000 ["报表类型"]#line:3824
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3825
            return 0 #line:3826
        if ("PSUR"in O00000O00O0O0O000 ["报表类型"]):#line:3831
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 .copy ()#line:3832
            if ini ["模式"]=="器械":#line:3833
                OO0O0OOO0OOOOOOO0 ["关键字查找列"]=OO0O0OOO0OOOOOOO0 ["器械故障表现"].astype (str )+OO0O0OOO0OOOOOOO0 ["伤害表现"].astype (str )+OO0O0OOO0OOOOOOO0 ["使用过程"].astype (str )+OO0O0OOO0OOOOOOO0 ["事件原因分析描述"].astype (str )+OO0O0OOO0OOOOOOO0 ["初步处置情况"].astype (str )#line:3834
            else :#line:3835
                OO0O0OOO0OOOOOOO0 ["关键字查找列"]=OO0O0OOO0OOOOOOO0 ["器械故障表现"]#line:3836
            if "-其他关键字-"in str (O00000O00O0O0O000 ["关键字标记"]):#line:3838
                OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 .loc [~OO0O0OOO0OOOOOOO0 ["关键字查找列"].str .contains (O00000O00O0O0O000 ["关键字标记"],na =False )].copy ()#line:3839
                TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3840
                return 0 #line:3841
            OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 [(OO0O0OOO0OOOOOOO0 ["关键字查找列"].str .contains (O00000O00O0O0O000 ["关键字标记"],na =False ))]#line:3844
            if str (O00000O00O0O0O000 ["排除值"])!="没有排除值":#line:3845
                OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 .loc [~OO0O0OOO0OOOOOOO0 ["关键字查找列"].str .contains (O00000O00O0O0O000 ["排除值"],na =False )]#line:3846
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3850
            return 0 #line:3851
        if ("ROR"in O00000O00O0O0O000 ["报表类型"]):#line:3854
            O0000O0OO00OO00OO ={'nan':"-未定义-"}#line:3855
            OOOOO0O00OO0OOO0O =eval (O00000O00O0O0O000 ["报表定位"],O0000O0OO00OO00OO )#line:3856
            OO0O0OOO0OOOOOOO0 =O00000OOOOO0OO000 .copy ()#line:3857
            for O0OO0000000OOOOOO ,OO00OO0O0OOO0O0O0 in OOOOO0O00OO0OOO0O .items ():#line:3859
                if O0OO0000000OOOOOO =="合并列"and OO00OO0O0OOO0O0O0 !={}:#line:3861
                    for OOO0OOO0O000000OO ,O00O0OO0O0OOOOOO0 in OO00OO0O0OOO0O0O0 .items ():#line:3862
                        if O00O0OO0O0OOOOOO0 !="-未定义-":#line:3863
                            O0000O0O00OO0O000 =TOOLS_get_list (O00O0OO0O0OOOOOO0 )#line:3864
                            OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ]=""#line:3865
                            for O00O00OO00OO00000 in O0000O0O00OO0O000 :#line:3866
                                OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ]=OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ]+OO0O0OOO0OOOOOOO0 [O00O00OO00OO00000 ].astype ("str")#line:3867
                if O0OO0000000OOOOOO =="等于"and OO00OO0O0OOO0O0O0 !={}:#line:3869
                    for OOO0OOO0O000000OO ,O00O0OO0O0OOOOOO0 in OO00OO0O0OOO0O0O0 .items ():#line:3870
                        OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 [(OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ]==O00O0OO0O0OOOOOO0 )]#line:3871
                if O0OO0000000OOOOOO =="不等于"and OO00OO0O0OOO0O0O0 !={}:#line:3873
                    for OOO0OOO0O000000OO ,O00O0OO0O0OOOOOO0 in OO00OO0O0OOO0O0O0 .items ():#line:3874
                        if O00O0OO0O0OOOOOO0 !="-未定义-":#line:3875
                            OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 [(OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ]!=O00O0OO0O0OOOOOO0 )]#line:3876
                if O0OO0000000OOOOOO =="包含"and OO00OO0O0OOO0O0O0 !={}:#line:3878
                    for OOO0OOO0O000000OO ,O00O0OO0O0OOOOOO0 in OO00OO0O0OOO0O0O0 .items ():#line:3879
                        if O00O0OO0O0OOOOOO0 !="-未定义-":#line:3880
                            OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 .loc [OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ].str .contains (O00O0OO0O0OOOOOO0 ,na =False )]#line:3881
                if O0OO0000000OOOOOO =="不包含"and OO00OO0O0OOO0O0O0 !={}:#line:3883
                    for OOO0OOO0O000000OO ,O00O0OO0O0OOOOOO0 in OO00OO0O0OOO0O0O0 .items ():#line:3884
                        if O00O0OO0O0OOOOOO0 !="-未定义-":#line:3885
                            OO0O0OOO0OOOOOOO0 =OO0O0OOO0OOOOOOO0 .loc [~OO0O0OOO0OOOOOOO0 [OOO0OOO0O000000OO ].str .contains (O00O0OO0O0OOOOOO0 ,na =False )]#line:3886
            TABLE_tree_Level_2 (OO0O0OOO0OOOOOOO0 ,0 ,OO0O0OOO0OOOOOOO0 )#line:3888
            return 0 #line:3889
    try :#line:3893
        if O000OOOOOO00OO0OO [1 ]=="dfx_zhenghao":#line:3894
            OOO00O00O0O0OOO00 ="dfx_zhenghao"#line:3895
            O0OOOO0O0OOO000O0 =""#line:3896
    except :#line:3897
            OOO00O00O0O0OOO00 =""#line:3898
            O0OOOO0O0OOO000O0 ="近一年"#line:3899
    if (("总体评分"in OO0O0O0O0O0OOO0O0 ["values"])and ("高峰批号均值"in OO0O0O0O0O0OOO0O0 ["values"])and ("月份均值"in OO0O0O0O0O0OOO0O0 ["values"]))or OOO00O00O0O0OOO00 =="dfx_zhenghao":#line:3900
            def O00000OOO00O0OO0O (event =None ):#line:3903
                for OO0OO00O00O0000O0 in O0O00O000000OO000 .selection ():#line:3904
                    OOOOO0OO0000O0OOO =O0O00O000000OO000 .item (OO0OO00O00O0000O0 ,"values")#line:3905
                O0000O000O000O000 =dict (zip (O0O00O0O0O00OO000 ,OOOOO0OO0000O0OOO ))#line:3906
                OOOO00O000O0OOO00 =OO0O0O00OOO0O0OOO [(OO0O0O00OOO0O0OOO ["注册证编号/曾用注册证编号"]==O0000O000O000O000 ["注册证编号/曾用注册证编号"])].copy ()#line:3907
                OOOO00O000O0OOO00 ["报表类型"]=O0000O000O000O000 ["报表类型"]+"1"#line:3908
                TABLE_tree_Level_2 (OOOO00O000O0OOO00 ,1 ,OO0O0O00OOO0O0OOO )#line:3909
            def O0OO00O00OOO0O0OO (event =None ):#line:3910
                for OO0OO0O00O0O00OOO in O0O00O000000OO000 .selection ():#line:3911
                    O00000OOOOO00O000 =O0O00O000000OO000 .item (OO0OO0O00O0O00OOO ,"values")#line:3912
                O0O00OOO0OOO0O00O =dict (zip (O0O00O0O0O00OO000 ,O00000OOOOO00O000 ))#line:3913
                OOO0O0O0000OOO000 =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==O0O00OOO0OOO0O00O ["注册证编号/曾用注册证编号"])].copy ()#line:3914
                OOO0O0O0000OOO000 ["报表类型"]=O0O00OOO0OOO0O00O ["报表类型"]+"1"#line:3915
                TABLE_tree_Level_2 (OOO0O0O0000OOO000 ,1 ,O000OOOOOO00OO0OO [0 ])#line:3916
            def O0O00OO00000OOOO0 (OO00OO0OO000000OO ):#line:3917
                for OOOO0000O00O0OO0O in O0O00O000000OO000 .selection ():#line:3918
                    OO00O0OO0000OO000 =O0O00O000000OO000 .item (OOOO0000O00O0OO0O ,"values")#line:3919
                OOO00O0O00OO0O0O0 =dict (zip (O0O00O0O0O00OO000 ,OO00O0OO0000OO000 ))#line:3920
                O0OO0O000O00O000O =OO0O0O00OOO0O0OOO [(OO0O0O00OOO0O0OOO ["注册证编号/曾用注册证编号"]==OOO00O0O00OO0O0O0 ["注册证编号/曾用注册证编号"])].copy ()#line:3923
                O0OO0O000O00O000O ["报表类型"]=OOO00O0O00OO0O0O0 ["报表类型"]+"1"#line:3924
                OO0O0O0O0000O000O =Countall (O0OO0O000O00O000O ).df_psur (OO00OO0OO000000OO ,OOO00O0O00OO0O0O0 ["规整后品类"])[["关键字标记","总数量","严重比"]]#line:3925
                OO0O0O0O0000O000O =OO0O0O0O0000O000O .rename (columns ={"总数量":"最近30天总数量"})#line:3926
                OO0O0O0O0000O000O =OO0O0O0O0000O000O .rename (columns ={"严重比":"最近30天严重比"})#line:3927
                O0OO0O000O00O000O =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==OOO00O0O00OO0O0O0 ["注册证编号/曾用注册证编号"])].copy ()#line:3929
                O0OO0O000O00O000O ["报表类型"]=OOO00O0O00OO0O0O0 ["报表类型"]+"1"#line:3930
                OOOOO000OO00000OO =Countall (O0OO0O000O00O000O ).df_psur (OO00OO0OO000000OO ,OOO00O0O00OO0O0O0 ["规整后品类"])#line:3931
                OOOO0O0O0000O0OOO =pd .merge (OOOOO000OO00000OO ,OO0O0O0O0000O000O ,on ="关键字标记",how ="left")#line:3933
                del OOOO0O0O0000O0OOO ["报表类型"]#line:3934
                OOOO0O0O0000O0OOO ["报表类型"]="PSUR"#line:3935
                TABLE_tree_Level_2 (OOOO0O0O0000O0OOO ,1 ,O0OO0O000O00O000O )#line:3937
            def O0OOO00O0000OOO00 (O0O0000OO00O00OO0 ):#line:3940
                for O0O0O0O0O0000O000 in O0O00O000000OO000 .selection ():#line:3941
                    O00O00000OOOO0000 =O0O00O000000OO000 .item (O0O0O0O0O0000O000 ,"values")#line:3942
                O0O0000OOOOOOOOO0 =dict (zip (O0O00O0O0O00OO000 ,O00O00000OOOO0000 ))#line:3943
                OO00OO0O00OO0O000 =O000OOOOOO00OO0OO [0 ]#line:3944
                if O0O0000OOOOOOOOO0 ["规整后品类"]=="N":#line:3945
                    if O0O0000OO00O00OO0 =="特定品种":#line:3946
                        showinfo (title ="关于",message ="未能适配该品种规则，可能未制定或者数据规整不完善。")#line:3947
                        return 0 #line:3948
                    OO00OO0O00OO0O000 =OO00OO0O00OO0O000 .loc [OO00OO0O00OO0O000 ["产品名称"].str .contains (O0O0000OOOOOOOOO0 ["产品名称"],na =False )].copy ()#line:3949
                else :#line:3950
                    OO00OO0O00OO0O000 =OO00OO0O00OO0O000 .loc [OO00OO0O00OO0O000 ["规整后品类"].str .contains (O0O0000OOOOOOOOO0 ["规整后品类"],na =False )].copy ()#line:3951
                OO00OO0O00OO0O000 =OO00OO0O00OO0O000 .loc [OO00OO0O00OO0O000 ["产品类别"].str .contains (O0O0000OOOOOOOOO0 ["产品类别"],na =False )].copy ()#line:3952
                OO00OO0O00OO0O000 ["报表类型"]=O0O0000OOOOOOOOO0 ["报表类型"]+"1"#line:3954
                if O0O0000OO00O00OO0 =="特定品种":#line:3955
                    TABLE_tree_Level_2 (Countall (OO00OO0O00OO0O000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],O0O0000OOOOOOOOO0 ["规整后品类"],O0O0000OOOOOOOOO0 ["注册证编号/曾用注册证编号"]),1 ,OO00OO0O00OO0O000 )#line:3956
                else :#line:3957
                    TABLE_tree_Level_2 (Countall (OO00OO0O00OO0O000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],O0O0000OO00O00OO0 ,O0O0000OOOOOOOOO0 ["注册证编号/曾用注册证编号"]),1 ,OO00OO0O00OO0O000 )#line:3958
            def OO0OO0OOO000OOOO0 (event =None ):#line:3960
                for O0O000O0O00O0OO0O in O0O00O000000OO000 .selection ():#line:3961
                    O0000O0O00O00OO00 =O0O00O000000OO000 .item (O0O000O0O00O0OO0O ,"values")#line:3962
                OOOO0000O00000O00 =dict (zip (O0O00O0O0O00OO000 ,O0000O0O00O00OO00 ))#line:3963
                OO0OOOOO0O0000O00 =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==OOOO0000O00000O00 ["注册证编号/曾用注册证编号"])].copy ()#line:3964
                OO0OOOOO0O0000O00 ["报表类型"]=OOOO0000O00000O00 ["报表类型"]+"1"#line:3965
                TABLE_tree_Level_2 (Countall (OO0OOOOO0O0000O00 ).df_pihao (),1 ,OO0OOOOO0O0000O00 ,)#line:3970
            def O000OO0O00O0OOOO0 (event =None ):#line:3972
                for O000OO0OOO000O00O in O0O00O000000OO000 .selection ():#line:3973
                    O00000OO0O00O0OO0 =O0O00O000000OO000 .item (O000OO0OOO000O00O ,"values")#line:3974
                OOOO0O0OOO000O0O0 =dict (zip (O0O00O0O0O00OO000 ,O00000OO0O00O0OO0 ))#line:3975
                O0O0OO00OOOO000OO =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==OOOO0O0OOO000O0O0 ["注册证编号/曾用注册证编号"])].copy ()#line:3976
                O0O0OO00OOOO000OO ["报表类型"]=OOOO0O0OOO000O0O0 ["报表类型"]+"1"#line:3977
                TABLE_tree_Level_2 (Countall (O0O0OO00OOOO000OO ).df_xinghao (),1 ,O0O0OO00OOOO000OO ,)#line:3982
            def OOOOOO000OO0O0000 (event =None ):#line:3984
                for OOOOOOOO0OOO0OO00 in O0O00O000000OO000 .selection ():#line:3985
                    O00OOO00OOO0OO000 =O0O00O000000OO000 .item (OOOOOOOO0OOO0OO00 ,"values")#line:3986
                OOOOOO000OOOOO0O0 =dict (zip (O0O00O0O0O00OO000 ,O00OOO00OOO0OO000 ))#line:3987
                O0O00O00000OOO000 =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==OOOOOO000OOOOO0O0 ["注册证编号/曾用注册证编号"])].copy ()#line:3988
                O0O00O00000OOO000 ["报表类型"]=OOOOOO000OOOOO0O0 ["报表类型"]+"1"#line:3989
                TABLE_tree_Level_2 (Countall (O0O00O00000OOO000 ).df_user (),1 ,O0O00O00000OOO000 ,)#line:3994
            def OO000O0OO0O000O00 (event =None ):#line:3996
                for O000OOOO0OO0OO0O0 in O0O00O000000OO000 .selection ():#line:3998
                    O0OOO0O0OO00OOOO0 =O0O00O000000OO000 .item (O000OOOO0OO0OO0O0 ,"values")#line:3999
                OO000OO000O000OO0 =dict (zip (O0O00O0O0O00OO000 ,O0OOO0O0OO00OOOO0 ))#line:4000
                OOO00O0O00O00OO00 =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==OO000OO000O000OO0 ["注册证编号/曾用注册证编号"])].copy ()#line:4001
                OOO00O0O00O00OO00 ["报表类型"]=OO000OO000O000OO0 ["报表类型"]+"1"#line:4002
                OOOOO0O0OOO0O0O0O =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name =0 ).reset_index (drop =True )#line:4003
                if ini ["模式"]=="药品":#line:4004
                    OOOOO0O0OOO0O0O0O =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="药品").reset_index (drop =True )#line:4005
                if ini ["模式"]=="器械":#line:4006
                    OOOOO0O0OOO0O0O0O =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="器械").reset_index (drop =True )#line:4007
                if ini ["模式"]=="化妆品":#line:4008
                    OOOOO0O0OOO0O0O0O =pd .read_excel (peizhidir +"0（范例）预警参数.xlsx",header =0 ,sheet_name ="化妆品").reset_index (drop =True )#line:4009
                O0O0OO0OO000OO00O =OOOOO0O0OOO0O0O0O ["值"][3 ]+"|"+OOOOO0O0OOO0O0O0O ["值"][4 ]#line:4010
                if ini ["模式"]=="器械":#line:4011
                    OOO00O0O00O00OO00 ["关键字查找列"]=OOO00O0O00O00OO00 ["器械故障表现"].astype (str )+OOO00O0O00O00OO00 ["伤害表现"].astype (str )+OOO00O0O00O00OO00 ["使用过程"].astype (str )+OOO00O0O00O00OO00 ["事件原因分析描述"].astype (str )+OOO00O0O00O00OO00 ["初步处置情况"].astype (str )#line:4012
                else :#line:4013
                    OOO00O0O00O00OO00 ["关键字查找列"]=OOO00O0O00O00OO00 ["器械故障表现"].astype (str )#line:4014
                OOO00O0O00O00OO00 =OOO00O0O00O00OO00 .loc [OOO00O0O00O00OO00 ["关键字查找列"].str .contains (O0O0OO0OO000OO00O ,na =False )].copy ().reset_index (drop =True )#line:4015
                TABLE_tree_Level_2 (OOO00O0O00O00OO00 ,0 ,OOO00O0O00O00OO00 ,)#line:4021
            def O00OOO00O0000000O (event =None ):#line:4024
                for OO00000OOOO0OOOOO in O0O00O000000OO000 .selection ():#line:4025
                    O0O00OOO00O000000 =O0O00O000000OO000 .item (OO00000OOOO0OOOOO ,"values")#line:4026
                O0OO000O0OOO000O0 =dict (zip (O0O00O0O0O00OO000 ,O0O00OOO00O000000 ))#line:4027
                O0OOO0OOOOO0OO0OO =O000OOOOOO00OO0OO [0 ][(O000OOOOOO00OO0OO [0 ]["注册证编号/曾用注册证编号"]==O0OO000O0OOO000O0 ["注册证编号/曾用注册证编号"])].copy ()#line:4028
                O0OOO0OOOOO0OO0OO ["报表类型"]=O0OO000O0OOO000O0 ["报表类型"]+"1"#line:4029
                TOOLS_time (O0OOO0OOOOO0OO0OO ,"事件发生日期",0 )#line:4030
            def O0OOO000O0O00000O (O0O00OO0OO0OOOO00 ,O0OO00O00000OO0O0 ):#line:4032
                for OO0O0O00O0000000O in O0O00O000000OO000 .selection ():#line:4034
                    O00OO0000O00OO000 =O0O00O000000OO000 .item (OO0O0O00O0000000O ,"values")#line:4035
                OO00OOO0000OO00O0 =dict (zip (O0O00O0O0O00OO000 ,O00OO0000O00OO000 ))#line:4036
                O00000O0O0OOO0OO0 =O000OOOOOO00OO0OO [0 ]#line:4037
                if OO00OOO0000OO00O0 ["规整后品类"]=="N":#line:4038
                    if O0O00OO0OO0OOOO00 =="特定品种":#line:4039
                        showinfo (title ="关于",message ="未能适配该品种规则，可能未制定或者数据规整不完善。")#line:4040
                        return 0 #line:4041
                O00000O0O0OOO0OO0 =O00000O0O0OOO0OO0 .loc [O00000O0O0OOO0OO0 ["注册证编号/曾用注册证编号"].str .contains (OO00OOO0000OO00O0 ["注册证编号/曾用注册证编号"],na =False )].copy ()#line:4042
                O00000O0O0OOO0OO0 ["报表类型"]=OO00OOO0000OO00O0 ["报表类型"]+"1"#line:4043
                if O0O00OO0OO0OOOO00 =="特定品种":#line:4044
                    TABLE_tree_Level_2 (Countall (O00000O0O0OOO0OO0 ).df_find_all_keword_risk (O0OO00O00000OO0O0 ,OO00OOO0000OO00O0 ["规整后品类"]),1 ,O00000O0O0OOO0OO0 )#line:4045
                else :#line:4046
                    TABLE_tree_Level_2 (Countall (O00000O0O0OOO0OO0 ).df_find_all_keword_risk (O0OO00O00000OO0O0 ,O0O00OO0OO0OOOO00 ),1 ,O00000O0O0OOO0OO0 )#line:4047
            OO0OO000OO0OOOO00 =Menu (OO0O00OO0OO0OO0OO ,tearoff =False ,)#line:4051
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"故障表现分类（无源）",command =lambda :O0O00OO00000OOOO0 ("通用无源"))#line:4052
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"故障表现分类（有源）",command =lambda :O0O00OO00000OOOO0 ("通用有源"))#line:4053
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"故障表现分类（特定品种）",command =lambda :O0O00OO00000OOOO0 ("特定品种"))#line:4054
            OO0OO000OO0OOOO00 .add_separator ()#line:4056
            if OOO00O00O0O0OOO00 =="":#line:4057
                OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"同类比较(ROR-无源)",command =lambda :O0OOO00O0000OOO00 ("无源"))#line:4058
                OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"同类比较(ROR-有源)",command =lambda :O0OOO00O0000OOO00 ("有源"))#line:4059
                OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"同类比较(ROR-特定品种)",command =lambda :O0OOO00O0000OOO00 ("特定品种"))#line:4060
            OO0OO000OO0OOOO00 .add_separator ()#line:4062
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(批号-无源)",command =lambda :O0OOO000O0O00000O ("无源","产品批号"))#line:4063
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(批号-特定品种)",command =lambda :O0OOO000O0O00000O ("特定品种","产品批号"))#line:4064
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(月份-无源)",command =lambda :O0OOO000O0O00000O ("无源","事件发生月份"))#line:4065
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(月份-有源)",command =lambda :O0OOO000O0O00000O ("有源","事件发生月份"))#line:4066
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(月份-特定品种)",command =lambda :O0OOO000O0O00000O ("特定品种","事件发生月份"))#line:4067
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(季度-无源)",command =lambda :O0OOO000O0O00000O ("无源","事件发生季度"))#line:4068
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(季度-有源)",command =lambda :O0OOO000O0O00000O ("有源","事件发生季度"))#line:4069
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"关键字趋势(季度-特定品种)",command =lambda :O0OOO000O0O00000O ("特定品种","事件发生季度"))#line:4070
            OO0OO000OO0OOOO00 .add_separator ()#line:4072
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"各批号报送情况",command =OO0OO0OOO000OOOO0 )#line:4073
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"各型号报送情况",command =O000OO0O00O0OOOO0 )#line:4074
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"报告单位情况",command =OOOOOO000OO0O0000 )#line:4075
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"事件发生时间曲线",command =O00OOO00O0000000O )#line:4076
            OO0OO000OO0OOOO00 .add_separator ()#line:4077
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"原始数据",command =O0OO00O00OOO0O0OO )#line:4078
            if OOO00O00O0O0OOO00 =="":#line:4079
                OO0OO000OO0OOOO00 .add_command (label ="近30天原始数据",command =O00000OOO00O0OO0O )#line:4080
            OO0OO000OO0OOOO00 .add_command (label =O0OOOO0O0OOO000O0 +"高度关注(一级和二级)",command =OO000O0OO0O000O00 )#line:4081
            def OO0000O0000OO00OO (OOO0O00O00O0O00O0 ):#line:4083
                OO0OO000OO0OOOO00 .post (OOO0O00O00O0O00O0 .x_root ,OOO0O00O00O0O00O0 .y_root )#line:4084
            OO0O00OO0OO0OO0OO .bind ("<Button-3>",OO0000O0000OO00OO )#line:4085
    if O0OO0OO0000OO00O0 ==0 or "规整编码"in OOO00000O0000O00O .columns :#line:4088
        O0O00O000000OO000 .bind ("<Double-1>",lambda O000OOOO00O00OO0O :OOO0O00OOOOO0OOOO (O000OOOO00O00OO0O ,OOO00000O0000O00O ))#line:4089
    if O0OO0OO0000OO00O0 ==1 and "规整编码"not in OOO00000O0000O00O .columns :#line:4090
        O0O00O000000OO000 .bind ("<Double-1>",lambda O0O0000O00000O0OO :OOO0000000O0OO000 (O0O0000O00000O0OO ,O0O00O0O0O00OO000 ,OO0O0O00OOO0O0OOO ))#line:4091
    def OOO0OOO0OOO000O0O (OO000000OOO0OO00O ,OOOO00OO0O0O0O000 ,OO00O00OO0OO00OOO ):#line:4094
        OOOO0O000OOO000O0 =[(OO000000OOO0OO00O .set (O0O0OO0000OO00O0O ,OOOO00OO0O0O0O000 ),O0O0OO0000OO00O0O )for O0O0OO0000OO00O0O in OO000000OOO0OO00O .get_children ("")]#line:4095
        OOOO0O000OOO000O0 .sort (reverse =OO00O00OO0OO00OOO )#line:4096
        for OO0O0O00000OOO0O0 ,(OOOO000O0OO0OOOO0 ,O0O00000OO0O0OOOO )in enumerate (OOOO0O000OOO000O0 ):#line:4098
            OO000000OOO0OO00O .move (O0O00000OO0O0OOOO ,"",OO0O0O00000OOO0O0 )#line:4099
        OO000000OOO0OO00O .heading (OOOO00OO0O0O0O000 ,command =lambda :OOO0OOO0OOO000O0O (OO000000OOO0OO00O ,OOOO00OO0O0O0O000 ,not OO00O00OO0OO00OOO ))#line:4102
    for O000OOO00O0O0000O in O0O00O0O0O00OO000 :#line:4104
        O0O00O000000OO000 .heading (O000OOO00O0O0000O ,text =O000OOO00O0O0000O ,command =lambda _col =O000OOO00O0O0000O :OOO0OOO0OOO000O0O (O0O00O000000OO000 ,_col ,False ),)#line:4109
    def OOO0O00OOOOO0OOOO (O00O00O000O0OO0OO ,O0OO000OO0O00O000 ):#line:4113
        if "规整编码"in O0OO000OO0O00O000 .columns :#line:4115
            O0OO000OO0O00O000 =O0OO000OO0O00O000 .rename (columns ={"规整编码":"报告编码"})#line:4116
        for OOO0O0000O00O0O0O in O0O00O000000OO000 .selection ():#line:4118
            OOOOOOOO0O00O0000 =O0O00O000000OO000 .item (OOO0O0000O00O0O0O ,"values")#line:4119
            O0O0OO0O00O0000OO =Toplevel ()#line:4122
            OOOOO0000O000OO00 =O0O0OO0O00O0000OO .winfo_screenwidth ()#line:4124
            O0O0O0O0O0O0O00OO =O0O0OO0O00O0000OO .winfo_screenheight ()#line:4126
            O0OO0O0OOO0O000OO =800 #line:4128
            OO00000000OO0OO00 =600 #line:4129
            OO000O0O000OOO000 =(OOOOO0000O000OO00 -O0OO0O0OOO0O000OO )/2 #line:4131
            O00000000OO00O0O0 =(O0O0O0O0O0O0O00OO -OO00000000OO0OO00 )/2 #line:4132
            O0O0OO0O00O0000OO .geometry ("%dx%d+%d+%d"%(O0OO0O0OOO0O000OO ,OO00000000OO0OO00 ,OO000O0O000OOO000 ,O00000000OO00O0O0 ))#line:4133
            O00OO0O000000OOOO =ScrolledText (O0O0OO0O00O0000OO ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:4137
            O00OO0O000000OOOO .pack (padx =10 ,pady =10 )#line:4138
            def O0O0000O0OOOOO00O (event =None ):#line:4139
                O00OO0O000000OOOO .event_generate ('<<Copy>>')#line:4140
            def O0OOOOOO0O00O0OOO (OOO000OOO0OO0O00O ,O0OOO000OOOO0O000 ):#line:4141
                TOOLS_savetxt (OOO000OOO0OO0O00O ,O0OOO000OOOO0O000 ,1 )#line:4142
            O0OO00O0OO0O00O0O =Menu (O00OO0O000000OOOO ,tearoff =False ,)#line:4143
            O0OO00O0OO0O00O0O .add_command (label ="复制",command =O0O0000O0OOOOO00O )#line:4144
            O0OO00O0OO0O00O0O .add_command (label ="导出",command =lambda :PROGRAM_thread_it (O0OOOOOO0O00O0OOO ,O00OO0O000000OOOO .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =O0OO000OO0O00O000 .iloc [0 ,0 ],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:4145
            def OOOO0OOOOO000O00O (O0OOOOOOO0OO000OO ):#line:4147
                O0OO00O0OO0O00O0O .post (O0OOOOOOO0OO000OO .x_root ,O0OOOOOOO0OO000OO .y_root )#line:4148
            O00OO0O000000OOOO .bind ("<Button-3>",OOOO0OOOOO000O00O )#line:4149
            try :#line:4151
                O0O0OO0O00O0000OO .title (str (OOOOOOOO0O00O0000 [0 ]))#line:4152
                O0OO000OO0O00O000 ["报告编码"]=O0OO000OO0O00O000 ["报告编码"].astype ("str")#line:4153
                OO0OO0O00OOO0O0O0 =O0OO000OO0O00O000 [(O0OO000OO0O00O000 ["报告编码"]==str (OOOOOOOO0O00O0000 [0 ]))]#line:4154
            except :#line:4155
                pass #line:4156
            O0O0OOO0O0O0OO000 =O0OO000OO0O00O000 .columns .values .tolist ()#line:4158
            for O00OOO0O0OO0O0O0O in range (len (O0O0OOO0O0O0OO000 )):#line:4159
                try :#line:4161
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="报告编码.1":#line:4162
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4163
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="产品名称":#line:4164
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4165
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="事件发生日期":#line:4166
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4167
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="是否开展了调查":#line:4168
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4169
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="市级监测机构":#line:4170
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4171
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="上报机构描述":#line:4172
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4173
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]=="持有人处理描述":#line:4174
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4175
                    if O00OOO0O0OO0O0O0O >1 and O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O -1 ]=="持有人处理描述":#line:4176
                        O00OO0O000000OOOO .insert (END ,"\n\n")#line:4177
                except :#line:4179
                    pass #line:4180
                try :#line:4181
                    if O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ]in ["单位名称","产品名称ori","上报机构描述","持有人处理描述","产品名称","注册证编号/曾用注册证编号","型号","规格","产品批号","上市许可持有人名称ori","上市许可持有人名称","伤害","伤害表现","器械故障表现","使用过程","事件原因分析描述","初步处置情况","调查情况","关联性评价","事件原因分析.1","具体控制措施"]:#line:4182
                        O00OO0O000000OOOO .insert (END ,"●")#line:4183
                except :#line:4184
                    pass #line:4185
                O00OO0O000000OOOO .insert (END ,O0O0OOO0O0O0OO000 [O00OOO0O0OO0O0O0O ])#line:4186
                O00OO0O000000OOOO .insert (END ,"：")#line:4187
                try :#line:4188
                    O00OO0O000000OOOO .insert (END ,OO0OO0O00OOO0O0O0 .iloc [0 ,O00OOO0O0OO0O0O0O ])#line:4189
                except :#line:4190
                    O00OO0O000000OOOO .insert (END ,OOOOOOOO0O00O0000 [O00OOO0O0OO0O0O0O ])#line:4191
                O00OO0O000000OOOO .insert (END ,"\n")#line:4192
            O00OO0O000000OOOO .config (state =DISABLED )#line:4193
    O0O00O000000OO000 .pack ()#line:4195
def TOOLS_get_guize2 (O00OO0OO00OOOO0OO ):#line:4198
	""#line:4199
	O00OO0OO0OO0OO0OO =peizhidir +"0（范例）比例失衡关键字库.xls"#line:4200
	OO00O00OO0O00O00O =pd .read_excel (O00OO0OO0OO0OO0OO ,header =0 ,sheet_name ="器械")#line:4201
	OO0O00O00O00OO0O0 =OO00O00OO0O00O00O [["适用范围列","适用范围"]].drop_duplicates ("适用范围")#line:4202
	text .insert (END ,OO0O00O00O00OO0O0 )#line:4203
	text .see (END )#line:4204
	OO00OO0O0OOO00O0O =Toplevel ()#line:4205
	OO00OO0O0OOO00O0O .title ('切换通用规则')#line:4206
	OOO00O0OOO0OO0OO0 =OO00OO0O0OOO00O0O .winfo_screenwidth ()#line:4207
	O0OO00OOOOO0OOO0O =OO00OO0O0OOO00O0O .winfo_screenheight ()#line:4209
	OO00O00O0O0O00OOO =450 #line:4211
	OOO0OO000OOOO00OO =100 #line:4212
	O00O0OOO0OOO0000O =(OOO00O0OOO0OO0OO0 -OO00O00O0O0O00OOO )/2 #line:4214
	O000000000O0OOO00 =(O0OO00OOOOO0OOO0O -OOO0OO000OOOO00OO )/2 #line:4215
	OO00OO0O0OOO00O0O .geometry ("%dx%d+%d+%d"%(OO00O00O0O0O00OOO ,OOO0OO000OOOO00OO ,O00O0OOO0OOO0000O ,O000000000O0OOO00 ))#line:4216
	OOOO0O0OO0OOO0OOO =Label (OO00OO0O0OOO00O0O ,text ="查找位置：器械故障表现+伤害表现+使用过程+事件原因分析描述+初步处置情况")#line:4217
	OOOO0O0OO0OOO0OOO .pack ()#line:4218
	O0000OOO000OO0O00 =Label (OO00OO0O0OOO00O0O ,text ="请选择您所需要的通用规则关键字：")#line:4219
	O0000OOO000OO0O00 .pack ()#line:4220
	def O0O0OOOO0O0000OO0 (*O0O0000OO0OO00O0O ):#line:4221
		OOO00O0OO000O0O0O .set (O00OOO0OOOOO00O0O .get ())#line:4222
	OOO00O0OO000O0O0O =StringVar ()#line:4223
	O00OOO0OOOOO00O0O =ttk .Combobox (OO00OO0O0OOO00O0O ,width =14 ,height =30 ,state ="readonly",textvariable =OOO00O0OO000O0O0O )#line:4224
	O00OOO0OOOOO00O0O ["values"]=OO0O00O00O00OO0O0 ["适用范围"].to_list ()#line:4225
	O00OOO0OOOOO00O0O .current (0 )#line:4226
	O00OOO0OOOOO00O0O .bind ("<<ComboboxSelected>>",O0O0OOOO0O0000OO0 )#line:4227
	O00OOO0OOOOO00O0O .pack ()#line:4228
	OOOO000OOOOO0OO00 =LabelFrame (OO00OO0O0OOO00O0O )#line:4231
	O0O0O0000OOOO0O00 =Button (OOOO000OOOOO0OO00 ,text ="确定",width =10 ,command =lambda :O0O000OOO00O0OO00 (OO00O00OO0O00O00O ,OOO00O0OO000O0O0O .get ()))#line:4232
	O0O0O0000OOOO0O00 .pack (side =LEFT ,padx =1 ,pady =1 )#line:4233
	OOOO000OOOOO0OO00 .pack ()#line:4234
	def O0O000OOO00O0OO00 (OOOOOOOO00000O000 ,OOO0OOOO0O0OO0O00 ):#line:4236
		OO00OO0OO0000OO0O =OOOOOOOO00000O000 .loc [OOOOOOOO00000O000 ["适用范围"].str .contains (OOO0OOOO0O0OO0O00 ,na =False )].copy ().reset_index (drop =True )#line:4237
		TABLE_tree_Level_2 (Countall (O00OO0OO00OOOO0OO ).df_psur ("特定品种作为通用关键字",OO00OO0OO0000OO0O ),1 ,O00OO0OO00OOOO0OO )#line:4238
def TOOLS_findin (OO00O0OO0000O0000 ,OOO00O0O0OO0O0O00 ):#line:4239
	""#line:4240
	O0OOOOOO00OOO0OO0 =Toplevel ()#line:4241
	O0OOOOOO00OOO0OO0 .title ('高级查找')#line:4242
	OO0OOOOOO00O00O0O =O0OOOOOO00OOO0OO0 .winfo_screenwidth ()#line:4243
	OOO0O0O00O0O00OOO =O0OOOOOO00OOO0OO0 .winfo_screenheight ()#line:4245
	O0O0OO00O0OO0O000 =400 #line:4247
	OO00O0OO0O0OOOOOO =120 #line:4248
	O0O0OO00O00OOOO0O =(OO0OOOOOO00O00O0O -O0O0OO00O0OO0O000 )/2 #line:4250
	OO00OOO00O0O0OOOO =(OOO0O0O00O0O00OOO -OO00O0OO0O0OOOOOO )/2 #line:4251
	O0OOOOOO00OOO0OO0 .geometry ("%dx%d+%d+%d"%(O0O0OO00O0OO0O000 ,OO00O0OO0O0OOOOOO ,O0O0OO00O00OOOO0O ,OO00OOO00O0O0OOOO ))#line:4252
	O00OOO0O0000OOOOO =Label (O0OOOOOO00OOO0OO0 ,text ="需要查找的关键字（用|隔开）：")#line:4253
	O00OOO0O0000OOOOO .pack ()#line:4254
	OO0O0O000O0O0O00O =Label (O0OOOOOO00OOO0OO0 ,text ="在哪些列查找（用|隔开）：")#line:4255
	O0OOOO0000OO000O0 =Entry (O0OOOOOO00OOO0OO0 ,width =80 )#line:4257
	O0OOOO0000OO000O0 .insert (0 ,"破裂|断裂")#line:4258
	OO000000OO0000O00 =Entry (O0OOOOOO00OOO0OO0 ,width =80 )#line:4259
	OO000000OO0000O00 .insert (0 ,"器械故障表现|伤害表现")#line:4260
	O0OOOO0000OO000O0 .pack ()#line:4261
	OO0O0O000O0O0O00O .pack ()#line:4262
	OO000000OO0000O00 .pack ()#line:4263
	O0O00000OO0O000OO =LabelFrame (O0OOOOOO00OOO0OO0 )#line:4264
	OOOOO00O0OO00O0OO =Button (O0O00000OO0O000OO ,text ="确定",width =10 ,command =lambda :PROGRAM_thread_it (TABLE_tree_Level_2 ,O0O00OOOO0OOO00O0 (O0OOOO0000OO000O0 .get (),OO000000OO0000O00 .get (),OO00O0OO0000O0000 ),1 ,OOO00O0O0OO0O0O00 ))#line:4265
	OOOOO00O0OO00O0OO .pack (side =LEFT ,padx =1 ,pady =1 )#line:4266
	O0O00000OO0O000OO .pack ()#line:4267
	def O0O00OOOO0OOO00O0 (O0000OOOOOO0O0O00 ,OOO0O0O0OO00O00OO ,O0O0O000O0O00OO0O ):#line:4270
		O0O0O000O0O00OO0O ["关键字查找列10"]="######"#line:4271
		for O0OO0O0O00OOOOO00 in TOOLS_get_list (OOO0O0O0OO00O00OO ):#line:4272
			O0O0O000O0O00OO0O ["关键字查找列10"]=O0O0O000O0O00OO0O ["关键字查找列10"].astype (str )+O0O0O000O0O00OO0O [O0OO0O0O00OOOOO00 ].astype (str )#line:4273
		O0O0O000O0O00OO0O =O0O0O000O0O00OO0O .loc [O0O0O000O0O00OO0O ["关键字查找列10"].str .contains (O0000OOOOOO0O0O00 ,na =False )]#line:4274
		del O0O0O000O0O00OO0O ["关键字查找列10"]#line:4275
		return O0O0O000O0O00OO0O #line:4276
def PROGRAM_about ():#line:4278
    ""#line:4279
    OOOO00O000O00000O =" 佛山市食品药品检验检测中心 \n(佛山市药品不良反应监测中心)\n蔡权周（QQ或微信411703730）\n仅供政府设立的不良反应监测机构使用。"#line:4280
    showinfo (title ="关于",message =OOOO00O000O00000O )#line:4281
def PROGRAM_thread_it (O000OOOOO00000O0O ,*OO0O0OOO000OO00O0 ):#line:4284
    ""#line:4285
    O0O0000O0OOOO0OOO =threading .Thread (target =O000OOOOO00000O0O ,args =OO0O0OOO000OO00O0 )#line:4287
    O0O0000O0OOOO0OOO .setDaemon (True )#line:4289
    O0O0000O0OOOO0OOO .start ()#line:4291
def PROGRAM_Menubar (O0OO0O0OOOO0OOO0O ,O0O00O000OO0OOOO0 ,O0O0O0000OOOO0OO0 ,O00O0O0OOOOO0OO00 ):#line:4292
	""#line:4293
	if ini ["模式"]=="其他":#line:4294
		return 0 #line:4295
	O000O0O0OO0OO0O0O =Menu (O0OO0O0OOOO0OOO0O )#line:4296
	O0OO0O0OOOO0OOO0O .config (menu =O000O0O0OO0OO0O0O )#line:4298
	OO000OO0O0O00OOOO =Menu (O000O0O0OO0OO0O0O ,tearoff =0 )#line:4302
	O000O0O0OO0OO0O0O .add_cascade (label ="信号检测",menu =OO000OO0O0O00OOOO )#line:4303
	OO000OO0O0O00OOOO .add_command (label ="数量比例失衡监测-证号内批号",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_findrisk ("产品批号"),1 ,O00O0O0OOOOO0OO00 ))#line:4306
	OO000OO0O0O00OOOO .add_command (label ="数量比例失衡监测-证号内季度",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_findrisk ("事件发生季度"),1 ,O00O0O0OOOOO0OO00 ))#line:4308
	OO000OO0O0O00OOOO .add_command (label ="数量比例失衡监测-证号内月份",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_findrisk ("事件发生月份"),1 ,O00O0O0OOOOO0OO00 ))#line:4310
	OO000OO0O0O00OOOO .add_command (label ="数量比例失衡监测-证号内性别",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_findrisk ("性别"),1 ,O00O0O0OOOOO0OO00 ))#line:4312
	OO000OO0O0O00OOOO .add_command (label ="数量比例失衡监测-证号内年龄段",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_findrisk ("年龄段"),1 ,O00O0O0OOOOO0OO00 ))#line:4314
	OO000OO0O0O00OOOO .add_separator ()#line:4316
	OO000OO0O0O00OOOO .add_command (label ="关键字检测（同证号内不同批号比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_find_all_keword_risk ("产品批号"),1 ,O00O0O0OOOOO0OO00 ))#line:4318
	OO000OO0O0O00OOOO .add_command (label ="关键字检测（同证号内不同月份比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_find_all_keword_risk ("事件发生月份"),1 ,O00O0O0OOOOO0OO00 ))#line:4320
	OO000OO0O0O00OOOO .add_command (label ="关键字检测（同证号内不同季度比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_find_all_keword_risk ("事件发生季度"),1 ,O00O0O0OOOOO0OO00 ))#line:4322
	OO000OO0O0O00OOOO .add_command (label ="关键字检测（同证号内不同性别比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_find_all_keword_risk ("性别"),1 ,O00O0O0OOOOO0OO00 ))#line:4324
	OO000OO0O0O00OOOO .add_command (label ="关键字检测（同证号内不同年龄段比对）",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_find_all_keword_risk ("年龄段"),1 ,O00O0O0OOOOO0OO00 ))#line:4326
	OO000OO0O0O00OOOO .add_separator ()#line:4328
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同证号的批号间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","产品批号"]),1 ,O00O0O0OOOOO0OO00 ))#line:4330
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同证号的月份间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","事件发生月份"]),1 ,O00O0O0OOOOO0OO00 ))#line:4332
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同证号的季度间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","事件发生季度"]),1 ,O00O0O0OOOOO0OO00 ))#line:4334
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同证号的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","年龄段"]),1 ,O00O0O0OOOOO0OO00 ))#line:4336
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同证号的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","性别"]),1 ,O00O0O0OOOOO0OO00 ))#line:4338
	OO000OO0O0O00OOOO .add_separator ()#line:4340
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同品名的证号间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]),1 ,O00O0O0OOOOO0OO00 ))#line:4342
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同品名的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["产品类别","规整后品类","产品名称","年龄段"]),1 ,O00O0O0OOOOO0OO00 ))#line:4344
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同品名的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["产品类别","规整后品类","产品名称","性别"]),1 ,O00O0O0OOOOO0OO00 ))#line:4346
	OO000OO0O0O00OOOO .add_separator ()#line:4348
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同类别的名称间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["产品类别","产品名称"]),1 ,O00O0O0OOOOO0OO00 ))#line:4350
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同类别的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["产品类别","年龄段"]),1 ,O00O0O0OOOOO0OO00 ))#line:4352
	OO000OO0O0O00OOOO .add_command (label ="关键字ROR-页面内同类别的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_ror (["产品类别","性别"]),1 ,O00O0O0OOOOO0OO00 ))#line:4354
	OO000OO0O0O00OOOO .add_separator ()#line:4365
	if ini ["模式"]=="药品":#line:4366
		OO000OO0O0O00OOOO .add_command (label ="新的不良反应检测(证号)",command =lambda :PROGRAM_thread_it (TOOLS_get_new ,O00O0O0OOOOO0OO00 ,"证号"))#line:4369
		OO000OO0O0O00OOOO .add_command (label ="新的不良反应检测(品种)",command =lambda :PROGRAM_thread_it (TOOLS_get_new ,O00O0O0OOOOO0OO00 ,"品种"))#line:4372
	O00OOO0OO0OOO0O00 =Menu (O000O0O0OO0OO0O0O ,tearoff =0 )#line:4375
	O000O0O0OO0OO0O0O .add_cascade (label ="简报制作",menu =O00OOO0OO0OOO0O00 )#line:4376
	O00OOO0OO0OOO0O00 .add_command (label ="药品简报",command =lambda :TOOLS_autocount (O0O00O000OO0OOOO0 ,"药品"))#line:4379
	O00OOO0OO0OOO0O00 .add_command (label ="器械简报",command =lambda :TOOLS_autocount (O0O00O000OO0OOOO0 ,"器械"))#line:4381
	O00OOO0OO0OOO0O00 .add_command (label ="化妆品简报",command =lambda :TOOLS_autocount (O0O00O000OO0OOOO0 ,"化妆品"))#line:4383
	O0OO0O0OOOOO00000 =Menu (O000O0O0OO0OO0O0O ,tearoff =0 )#line:4387
	O000O0O0OO0OO0O0O .add_cascade (label ="品种评价",menu =O0OO0O0OOOOO00000 )#line:4388
	O0OO0O0OOOOO00000 .add_command (label ="报告年份",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"报告年份",-1 ))#line:4390
	O0OO0O0OOOOO00000 .add_command (label ="发生年份",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"事件发生年份",-1 ))#line:4392
	O0OO0O0OOOOO00000 .add_separator ()#line:4393
	O0OO0O0OOOOO00000 .add_command (label ="怀疑/并用",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"怀疑/并用",1 ))#line:4395
	O0OO0O0OOOOO00000 .add_command (label ="涉及企业",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"上市许可持有人名称",1 ))#line:4397
	O0OO0O0OOOOO00000 .add_command (label ="产品名称",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"产品名称",1 ))#line:4399
	O0OO0O0OOOOO00000 .add_command (label ="注册证号",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_zhenghao (),1 ,O00O0O0OOOOO0OO00 ))#line:4401
	O0OO0O0OOOOO00000 .add_separator ()#line:4402
	O0OO0O0OOOOO00000 .add_command (label ="年龄段分布",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"年龄段",1 ))#line:4404
	O0OO0O0OOOOO00000 .add_command (label ="性别分布",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"性别",1 ))#line:4406
	O0OO0O0OOOOO00000 .add_command (label ="年龄性别分布",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_age (),1 ,O00O0O0OOOOO0OO00 ,))#line:4408
	O0OO0O0OOOOO00000 .add_separator ()#line:4409
	O0OO0O0OOOOO00000 .add_command (label ="不良反应发生时间",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"时隔",1 ))#line:4411
	O0OO0O0OOOOO00000 .add_command (label ="报告类型-严重程度",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"报告类型-严重程度",1 ))#line:4414
	O0OO0O0OOOOO00000 .add_command (label ="停药减药后反应是否减轻或消失",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"停药减药后反应是否减轻或消失",1 ))#line:4416
	O0OO0O0OOOOO00000 .add_command (label ="再次使用可疑药是否出现同样反应",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"再次使用可疑药是否出现同样反应",1 ))#line:4418
	O0OO0O0OOOOO00000 .add_command (label ="对原患疾病影响",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"对原患疾病影响",1 ))#line:4420
	O0OO0O0OOOOO00000 .add_command (label ="不良反应结果",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"不良反应结果",1 ))#line:4422
	O0OO0O0OOOOO00000 .add_command (label ="报告单位关联性评价",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"关联性评价",1 ))#line:4424
	O0OO0O0OOOOO00000 .add_separator ()#line:4425
	O0OO0O0OOOOO00000 .add_command (label ="不良反应转归情况",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"不良反应结果2",4 ))#line:4427
	O0OO0O0OOOOO00000 .add_command (label ="关联性评价汇总",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"关联性评价汇总",5 ))#line:4429
	O0OO0O0OOOOO00000 .add_separator ()#line:4433
	O0OO0O0OOOOO00000 .add_command (label ="不良反应-术语",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"器械故障表现",0 ))#line:4435
	O0OO0O0OOOOO00000 .add_command (label ="不良反应器官系统-术语",command =lambda :TABLE_tree_Level_2 (Countall (O0O00O000OO0OOOO0 ).df_psur (),1 ,O00O0O0OOOOO0OO00 ))#line:4437
	O0OO0O0OOOOO00000 .add_command (label ="不良反应-由code转化",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"不良反应-code",2 ))#line:4439
	O0OO0O0OOOOO00000 .add_command (label ="不良反应器官系统-由code转化",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"不良反应-code",3 ))#line:4441
	O0OO0O0OOOOO00000 .add_separator ()#line:4443
	O0OO0O0OOOOO00000 .add_command (label ="疾病名称-术语",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"相关疾病信息[疾病名称]-术语",0 ))#line:4445
	O0OO0O0OOOOO00000 .add_command (label ="疾病名称-由code转化",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"相关疾病信息[疾病名称]-code",2 ))#line:4447
	O0OO0O0OOOOO00000 .add_command (label ="疾病器官系统-由code转化",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"相关疾病信息[疾病名称]-code",3 ))#line:4449
	O0OO0O0OOOOO00000 .add_separator ()#line:4450
	O0OO0O0OOOOO00000 .add_command (label ="适应症-术语",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"治疗适应症-术语",0 ))#line:4452
	O0OO0O0OOOOO00000 .add_command (label ="适应症-由code转化",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"治疗适应症-code",2 ))#line:4454
	O0OO0O0OOOOO00000 .add_command (label ="适应症器官系统-由code转化",command =lambda :STAT_pinzhong (O0O00O000OO0OOOO0 ,"治疗适应症-code",3 ))#line:4456
	OOOOO0000OOO0000O =Menu (O000O0O0OO0OO0O0O ,tearoff =0 )#line:4458
	O000O0O0OO0OO0O0O .add_cascade (label ="基础研究",menu =OOOOO0000OOO0000O )#line:4459
	OOOOO0000OOO0000O .add_command (label ="基础信息批量操作（品名）",command =lambda :TOOLS_ror_mode1 (O0O00O000OO0OOOO0 ,"产品名称"))#line:4461
	OOOOO0000OOO0000O .add_command (label ="器官系统ROR批量操作（品名）",command =lambda :TOOLS_ror_mode2 (O0O00O000OO0OOOO0 ,"产品名称"))#line:4463
	OOOOO0000OOO0000O .add_command (label ="ADR-ROR批量操作（品名）",command =lambda :TOOLS_ror_mode3 (O0O00O000OO0OOOO0 ,"产品名称"))#line:4465
	O0O0O0OOO00O00O00 =Menu (O000O0O0OO0OO0O0O ,tearoff =0 )#line:4466
	O000O0O0OO0OO0O0O .add_cascade (label ="风险预警",menu =O0O0O0OOO00O00O00 )#line:4467
	O0O0O0OOO00O00O00 .add_command (label ="预警（单日）",command =lambda :TOOLS_keti (O0O00O000OO0OOOO0 ))#line:4469
	O0O0O0OOO00O00O00 .add_command (label ="事件分布（器械）",command =lambda :TOOLS_get_guize2 (O0O00O000OO0OOOO0 ))#line:4472
	O0O0OOO0OO00OO00O =Menu (O000O0O0OO0OO0O0O ,tearoff =0 )#line:4479
	O000O0O0OO0OO0O0O .add_cascade (label ="实用工具",menu =O0O0OOO0OO00OO00O )#line:4480
	O0O0OOO0OO00OO00O .add_command (label ="数据规整（报告单位）",command =lambda :TOOL_guizheng (O0O00O000OO0OOOO0 ,2 ,False ))#line:4484
	O0O0OOO0OO00OO00O .add_command (label ="数据规整（产品名称）",command =lambda :TOOL_guizheng (O0O00O000OO0OOOO0 ,3 ,False ))#line:4486
	O0O0OOO0OO00OO00O .add_command (label ="数据规整（自定义）",command =lambda :TOOL_guizheng (O0O00O000OO0OOOO0 ,0 ,False ))#line:4488
	O0O0OOO0OO00OO00O .add_separator ()#line:4490
	O0O0OOO0OO00OO00O .add_command (label ="原始导入",command =TOOLS_fileopen )#line:4492
	O0O0OOO0OO00OO00O .add_command (label ="脱敏保存",command =lambda :TOOLS_data_masking (O0O00O000OO0OOOO0 ))#line:4494
	O0O0OOO0OO00OO00O .add_separator ()#line:4495
	O0O0OOO0OO00OO00O .add_command (label ="批量筛选（默认）",command =lambda :TOOLS_xuanze (O0O00O000OO0OOOO0 ,1 ))#line:4497
	O0O0OOO0OO00OO00O .add_command (label ="批量筛选（自定义）",command =lambda :TOOLS_xuanze (O0O00O000OO0OOOO0 ,0 ))#line:4499
	O0O0OOO0OO00OO00O .add_separator ()#line:4500
	O0O0OOO0OO00OO00O .add_command (label ="评价人员（广东化妆品）",command =lambda :TOOL_person (O0O00O000OO0OOOO0 ))#line:4502
	O0O0OOO0OO00OO00O .add_separator ()#line:4503
	O0O0OOO0OO00OO00O .add_command (label ="意见反馈",command =lambda :PROGRAM_helper (["","  药械妆不良反应报表统计分析工作站","  开发者：蔡权周","  邮箱：411703730@qq.com","  微信号：sysucai","  手机号：18575757461"]))#line:4507
	O0O0OOO0OO00OO00O .add_command (label ="更改用户组",command =lambda :PROGRAM_thread_it (display_random_number ))#line:4509
def PROGRAM_helper (OOOO0O0O00000O0O0 ):#line:4513
    ""#line:4514
    O0O0OO0000000O0O0 =Toplevel ()#line:4515
    O0O0OO0000000O0O0 .title ("信息查看")#line:4516
    O0O0OO0000000O0O0 .geometry ("700x500")#line:4517
    OOO0OO0OO0OOO00OO =Scrollbar (O0O0OO0000000O0O0 )#line:4519
    OOOO00OO0OOOO0O00 =Text (O0O0OO0000000O0O0 ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:4520
    OOO0OO0OO0OOO00OO .pack (side =RIGHT ,fill =Y )#line:4521
    OOOO00OO0OOOO0O00 .pack ()#line:4522
    OOO0OO0OO0OOO00OO .config (command =OOOO00OO0OOOO0O00 .yview )#line:4523
    OOOO00OO0OOOO0O00 .config (yscrollcommand =OOO0OO0OO0OOO00OO .set )#line:4524
    for OOO000000O0OO0000 in OOOO0O0O00000O0O0 :#line:4526
        OOOO00OO0OOOO0O00 .insert (END ,OOO000000O0OO0000 )#line:4527
        OOOO00OO0OOOO0O00 .insert (END ,"\n")#line:4528
    def O00OOOO0O00O0O0OO (event =None ):#line:4531
        OOOO00OO0OOOO0O00 .event_generate ('<<Copy>>')#line:4532
    OO0OOO0OOOOO000OO =Menu (OOOO00OO0OOOO0O00 ,tearoff =False ,)#line:4535
    OO0OOO0OOOOO000OO .add_command (label ="复制",command =O00OOOO0O00O0O0OO )#line:4536
    def OOOOO00O000OOO00O (OOOOO0OOO000OO0OO ):#line:4537
         OO0OOO0OOOOO000OO .post (OOOOO0OOO000OO0OO .x_root ,OOOOO0OOO000OO0OO .y_root )#line:4538
    OOOO00OO0OOOO0O00 .bind ("<Button-3>",OOOOO00O000OOO00O )#line:4539
    OOOO00OO0OOOO0O00 .config (state =DISABLED )#line:4541
def PROGRAM_change_schedule (O00OOOOO0O0O0O00O ,OO0O00OOO0OO0OO00 ):#line:4543
    ""#line:4544
    canvas .coords (fill_rec ,(5 ,5 ,(O00OOOOO0O0O0O00O /OO0O00OOO0OO0OO00 )*680 ,25 ))#line:4546
    root .update ()#line:4547
    x .set (str (round (O00OOOOO0O0O0O00O /OO0O00OOO0OO0OO00 *100 ,2 ))+"%")#line:4548
    if round (O00OOOOO0O0O0O00O /OO0O00OOO0OO0OO00 *100 ,2 )==100.00 :#line:4549
        x .set ("完成")#line:4550
def PROGRAM_showWelcome ():#line:4553
    ""#line:4554
    OOO0O000O00O0OOO0 =roox .winfo_screenwidth ()#line:4555
    O0OO0000000O000O0 =roox .winfo_screenheight ()#line:4557
    roox .overrideredirect (True )#line:4559
    roox .attributes ("-alpha",1 )#line:4560
    OOO00OO0OOO0OOOOO =(OOO0O000O00O0OOO0 -475 )/2 #line:4561
    OO00O00O0O00000O0 =(O0OO0000000O000O0 -200 )/2 #line:4562
    roox .geometry ("675x130+%d+%d"%(OOO00OO0OOO0OOOOO ,OO00O00O0O00000O0 ))#line:4564
    roox ["bg"]="green"#line:4565
    O000O0000O0O000O0 =Label (roox ,text =title_all2 ,fg ="white",bg ="green",font =("微软雅黑",20 ))#line:4568
    O000O0000O0O000O0 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:4569
    O00O000OO00O0OO00 =Label (roox ,text ="仅供监测机构使用 ",fg ="white",bg ="black",font =("微软雅黑",15 ))#line:4572
    O00O000OO00O0OO00 .place (x =0 ,y =90 ,width =675 ,height =40 )#line:4573
def PROGRAM_closeWelcome ():#line:4576
    ""#line:4577
    for OO00OO0OO00O0OO0O in range (2 ):#line:4578
        root .attributes ("-alpha",0 )#line:4579
        time .sleep (1 )#line:4580
    root .attributes ("-alpha",1 )#line:4581
    roox .destroy ()#line:4582
class Countall ():#line:4597
	""#line:4598
	def __init__ (OO000O0O000OOOO0O ,O0O0000OO0OO0O0OO ):#line:4599
		""#line:4600
		OO000O0O000OOOO0O .df =O0O0000OO0OO0O0OO #line:4601
		OO000O0O000OOOO0O .mode =ini ["模式"]#line:4602
	def df_org (OOO0OOOOO0000OO0O ,OO0O0OO000000OO0O ):#line:4604
		""#line:4605
		O0000OOOO0O0O0000 =OOO0OOOOO0000OO0O .df .drop_duplicates (["报告编码"]).groupby ([OO0O0OO000000OO0O ]).agg (报告数量 =("注册证编号/曾用注册证编号","count"),审核通过数 =("有效报告","sum"),严重伤害数 =("伤害",lambda OO000OO0O00O0OOOO :STAT_countpx (OO000OO0O00O0OOOO .values ,"严重伤害")),死亡数量 =("伤害",lambda OO0OOOOO0OOO00O0O :STAT_countpx (OO0OOOOO0OOO00O0O .values ,"死亡")),超时报告数 =("超时标记",lambda O00OOOOO00OO00O0O :STAT_countpx (O00OOOOO00OO00O0O .values ,1 )),有源 =("产品类别",lambda O000000O0OO0OOOO0 :STAT_countpx (O000000O0OO0OOOO0 .values ,"有源")),无源 =("产品类别",lambda O0OOOO0O000O000OO :STAT_countpx (O0OOOO0O000O000OO .values ,"无源")),体外诊断试剂 =("产品类别",lambda O0OOOOO00O0O0OOO0 :STAT_countpx (O0OOOOO00O0O0OOO0 .values ,"体外诊断试剂")),三类数量 =("管理类别",lambda O0O00OOO000OOO0OO :STAT_countpx (O0O00OOO000OOO0OO .values ,"Ⅲ类")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),报告季度 =("报告季度",STAT_countx ),报告月份 =("报告月份",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:4620
		O00OO000O000O0OO0 =["报告数量","审核通过数","严重伤害数","死亡数量","超时报告数","有源","无源","体外诊断试剂","三类数量","单位个数"]#line:4622
		O0000OOOO0O0O0000 .loc ["合计"]=O0000OOOO0O0O0000 [O00OO000O000O0OO0 ].apply (lambda OOO0OO00000O00O0O :OOO0OO00000O00O0O .sum ())#line:4623
		O0000OOOO0O0O0000 [O00OO000O000O0OO0 ]=O0000OOOO0O0O0000 [O00OO000O000O0OO0 ].apply (lambda O000O0O0O00O0O0O0 :O000O0O0O00O0O0O0 .astype (int ))#line:4624
		O0000OOOO0O0O0000 .iloc [-1 ,0 ]="合计"#line:4625
		O0000OOOO0O0O0000 ["严重比"]=round ((O0000OOOO0O0O0000 ["严重伤害数"]+O0000OOOO0O0O0000 ["死亡数量"])/O0000OOOO0O0O0000 ["报告数量"]*100 ,2 )#line:4627
		O0000OOOO0O0O0000 ["Ⅲ类比"]=round ((O0000OOOO0O0O0000 ["三类数量"])/O0000OOOO0O0O0000 ["报告数量"]*100 ,2 )#line:4628
		O0000OOOO0O0O0000 ["超时比"]=round ((O0000OOOO0O0O0000 ["超时报告数"])/O0000OOOO0O0O0000 ["报告数量"]*100 ,2 )#line:4629
		O0000OOOO0O0O0000 ["报表类型"]="dfx_org"+OO0O0OO000000OO0O #line:4630
		if ini ["模式"]=="药品":#line:4633
			del O0000OOOO0O0O0000 ["有源"]#line:4635
			del O0000OOOO0O0O0000 ["无源"]#line:4636
			del O0000OOOO0O0O0000 ["体外诊断试剂"]#line:4637
			O0000OOOO0O0O0000 =O0000OOOO0O0O0000 .rename (columns ={"三类数量":"新的和严重的数量"})#line:4638
			O0000OOOO0O0O0000 =O0000OOOO0O0O0000 .rename (columns ={"Ⅲ类比":"新严比"})#line:4639
		return O0000OOOO0O0O0000 #line:4641
	def df_user (OO0OOOO0OOOO0000O ):#line:4645
		""#line:4646
		OO0OOOO0OOOO0000O .df ["医疗机构类别"]=OO0OOOO0OOOO0000O .df ["医疗机构类别"].fillna ("未填写")#line:4647
		O0OOO0OOOO0OO000O =OO0OOOO0OOOO0000O .df .drop_duplicates (["报告编码"]).groupby (["监测机构","单位名称","医疗机构类别"]).agg (报告数量 =("注册证编号/曾用注册证编号","count"),审核通过数 =("有效报告","sum"),严重伤害数 =("伤害",lambda O0O0O0O0O0O000OO0 :STAT_countpx (O0O0O0O0O0O000OO0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0OO00O000OO00O :STAT_countpx (O0O0OO00O000OO00O .values ,"死亡")),超时报告数 =("超时标记",lambda O0OO0O0O0O0O0O000 :STAT_countpx (O0OO0O0O0O0O0O000 .values ,1 )),有源 =("产品类别",lambda OOOOO0O00O00O0OO0 :STAT_countpx (OOOOO0O00O00O0OO0 .values ,"有源")),无源 =("产品类别",lambda O0O0OOOO000O000O0 :STAT_countpx (O0O0OOOO000O000O0 .values ,"无源")),体外诊断试剂 =("产品类别",lambda O0O00O0OO0000O00O :STAT_countpx (O0O00O0OO0000O00O .values ,"体外诊断试剂")),三类数量 =("管理类别",lambda O0000O0O0O0O0OO0O :STAT_countpx (O0000O0O0O0O0OO0O .values ,"Ⅲ类")),产品数量 =("产品名称","nunique"),产品清单 =("产品名称",STAT_countx ),报告季度 =("报告季度",STAT_countx ),报告月份 =("报告月份",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:4662
		O0OOOOOO00O00OOO0 =["报告数量","审核通过数","严重伤害数","死亡数量","超时报告数","有源","无源","体外诊断试剂","三类数量"]#line:4665
		O0OOO0OOOO0OO000O .loc ["合计"]=O0OOO0OOOO0OO000O [O0OOOOOO00O00OOO0 ].apply (lambda O000OO0O00OOOO00O :O000OO0O00OOOO00O .sum ())#line:4666
		O0OOO0OOOO0OO000O [O0OOOOOO00O00OOO0 ]=O0OOO0OOOO0OO000O [O0OOOOOO00O00OOO0 ].apply (lambda O0O0O00O0O0000O00 :O0O0O00O0O0000O00 .astype (int ))#line:4667
		O0OOO0OOOO0OO000O .iloc [-1 ,0 ]="合计"#line:4668
		O0OOO0OOOO0OO000O ["严重比"]=round ((O0OOO0OOOO0OO000O ["严重伤害数"]+O0OOO0OOOO0OO000O ["死亡数量"])/O0OOO0OOOO0OO000O ["报告数量"]*100 ,2 )#line:4670
		O0OOO0OOOO0OO000O ["Ⅲ类比"]=round ((O0OOO0OOOO0OO000O ["三类数量"])/O0OOO0OOOO0OO000O ["报告数量"]*100 ,2 )#line:4671
		O0OOO0OOOO0OO000O ["超时比"]=round ((O0OOO0OOOO0OO000O ["超时报告数"])/O0OOO0OOOO0OO000O ["报告数量"]*100 ,2 )#line:4672
		O0OOO0OOOO0OO000O ["报表类型"]="dfx_user"#line:4673
		if ini ["模式"]=="药品":#line:4675
			del O0OOO0OOOO0OO000O ["有源"]#line:4677
			del O0OOO0OOOO0OO000O ["无源"]#line:4678
			del O0OOO0OOOO0OO000O ["体外诊断试剂"]#line:4679
			O0OOO0OOOO0OO000O =O0OOO0OOOO0OO000O .rename (columns ={"三类数量":"新的和严重的数量"})#line:4680
			O0OOO0OOOO0OO000O =O0OOO0OOOO0OO000O .rename (columns ={"Ⅲ类比":"新严比"})#line:4681
		return O0OOO0OOOO0OO000O #line:4683
	def df_zhenghao (OOO0O00OOO0O0O00O ):#line:4688
		""#line:4689
		O000000OO00O0O0O0 =OOO0O00OOO0O0O00O .df .groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (证号计数 =("注册证编号/曾用注册证编号","count"),严重伤害数 =("伤害",lambda OO000O00OOO00000O :STAT_countpx (OO000O00OOO00000O .values ,"严重伤害")),死亡数量 =("伤害",lambda O0OOOOO0OOOO0O0O0 :STAT_countpx (O0OOOOO0OOOO0O0O0 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda OO0O0O0O0OO0O0OO0 :STAT_countpx (OO0O0O0O0OO0O0OO0 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OO0OO0OO0O00OO0OO :STAT_countpx (OO0OO0OO0O00OO0OO .values ,"严重伤害待评价")),).sort_values (by ="证号计数",ascending =[False ],na_position ="last").reset_index ()#line:4704
		O000000OO00O0O0O0 =STAT_basic_risk (O000000OO00O0O0O0 ,"证号计数","严重伤害数","死亡数量","单位个数")#line:4705
		O000000OO00O0O0O0 =pd .merge (O000000OO00O0O0O0 ,STAT_recent30 (OOO0O00OOO0O0O00O .df ,["注册证编号/曾用注册证编号"]),on =["注册证编号/曾用注册证编号"],how ="left")#line:4707
		O000000OO00O0O0O0 ["最近30天报告数"]=O000000OO00O0O0O0 ["最近30天报告数"].fillna (0 ).astype (int )#line:4708
		O000000OO00O0O0O0 ["最近30天报告严重伤害数"]=O000000OO00O0O0O0 ["最近30天报告严重伤害数"].fillna (0 ).astype (int )#line:4709
		O000000OO00O0O0O0 ["最近30天报告死亡数量"]=O000000OO00O0O0O0 ["最近30天报告死亡数量"].fillna (0 ).astype (int )#line:4710
		O000000OO00O0O0O0 ["最近30天报告单位个数"]=O000000OO00O0O0O0 ["最近30天报告单位个数"].fillna (0 ).astype (int )#line:4711
		O000000OO00O0O0O0 ["最近30天风险评分"]=O000000OO00O0O0O0 ["最近30天风险评分"].fillna (0 ).astype (int )#line:4712
		O000000OO00O0O0O0 ["报表类型"]="dfx_zhenghao"#line:4714
		if ini ["模式"]=="药品":#line:4716
			O000000OO00O0O0O0 =O000000OO00O0O0O0 .rename (columns ={"待评价数":"新的数量"})#line:4717
			O000000OO00O0O0O0 =O000000OO00O0O0O0 .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4718
		return O000000OO00O0O0O0 #line:4720
	def df_pihao (O0OOO00OO000O0OOO ):#line:4722
		""#line:4723
		O00OO000OO00O0OOO =O0OOO00OO000O0OOO .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (批号计数 =("产品批号","count"),严重伤害数 =("伤害",lambda OOO00OOOO00O0O000 :STAT_countpx (OOO00OOOO00O0O000 .values ,"严重伤害")),死亡数量 =("伤害",lambda OOOOO0O000OOO0O0O :STAT_countpx (OOOOO0O000OOO0O0O .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda O0OO00000OO0O0OOO :STAT_countpx (O0OO00000OO0O0OOO .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OOOO000OOO0OOO000 :STAT_countpx (OOOO000OOO0OOO000 .values ,"严重伤害待评价")),).sort_values (by ="批号计数",ascending =[False ],na_position ="last").reset_index ()#line:4736
		O00OO000OO00O0OOO =STAT_basic_risk (O00OO000OO00O0OOO ,"批号计数","严重伤害数","死亡数量","单位个数")#line:4739
		O00OO000OO00O0OOO =pd .merge (O00OO000OO00O0OOO ,STAT_recent30 (O0OOO00OO000O0OOO .df ,["注册证编号/曾用注册证编号","产品批号"]),on =["注册证编号/曾用注册证编号","产品批号"],how ="left")#line:4741
		O00OO000OO00O0OOO ["最近30天报告数"]=O00OO000OO00O0OOO ["最近30天报告数"].fillna (0 ).astype (int )#line:4742
		O00OO000OO00O0OOO ["最近30天报告严重伤害数"]=O00OO000OO00O0OOO ["最近30天报告严重伤害数"].fillna (0 ).astype (int )#line:4743
		O00OO000OO00O0OOO ["最近30天报告死亡数量"]=O00OO000OO00O0OOO ["最近30天报告死亡数量"].fillna (0 ).astype (int )#line:4744
		O00OO000OO00O0OOO ["最近30天报告单位个数"]=O00OO000OO00O0OOO ["最近30天报告单位个数"].fillna (0 ).astype (int )#line:4745
		O00OO000OO00O0OOO ["最近30天风险评分"]=O00OO000OO00O0OOO ["最近30天风险评分"].fillna (0 ).astype (int )#line:4746
		O00OO000OO00O0OOO ["报表类型"]="dfx_pihao"#line:4748
		if ini ["模式"]=="药品":#line:4749
			O00OO000OO00O0OOO =O00OO000OO00O0OOO .rename (columns ={"待评价数":"新的数量"})#line:4750
			O00OO000OO00O0OOO =O00OO000OO00O0OOO .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4751
		return O00OO000OO00O0OOO #line:4752
	def df_xinghao (O0O00O0O0O0OOO00O ):#line:4754
		""#line:4755
		OOO0OO0OOO00OO0OO =O0O00O0O0O0OOO00O .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (型号计数 =("型号","count"),严重伤害数 =("伤害",lambda O0O000OO00O000OO0 :STAT_countpx (O0O000OO00O000OO0 .values ,"严重伤害")),死亡数量 =("伤害",lambda OO0OOOO0O000OOO0O :STAT_countpx (OO0OOOO0O000OOO0O .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda O000000O000O0O00O :STAT_countpx (O000000O000O0O00O .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OOO0O00OO0O0O0O00 :STAT_countpx (OOO0O00OO0O0O0O00 .values ,"严重伤害待评价")),).sort_values (by ="型号计数",ascending =[False ],na_position ="last").reset_index ()#line:4768
		OOO0OO0OOO00OO0OO ["报表类型"]="dfx_xinghao"#line:4769
		if ini ["模式"]=="药品":#line:4770
			OOO0OO0OOO00OO0OO =OOO0OO0OOO00OO0OO .rename (columns ={"待评价数":"新的数量"})#line:4771
			OOO0OO0OOO00OO0OO =OOO0OO0OOO00OO0OO .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4772
		return OOO0OO0OOO00OO0OO #line:4774
	def df_guige (O00OOOOOO00000000 ):#line:4776
		""#line:4777
		O000O0OOOO0000O00 =O00OOOOOO00000000 .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","规格"]).agg (规格计数 =("规格","count"),严重伤害数 =("伤害",lambda O0O0OOO00O00O00O0 :STAT_countpx (O0O0OOO00O00O00O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O00O00O00000OOOO0 :STAT_countpx (O00O00O00000OOOO0 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),待评价数 =("持有人报告状态",lambda O0O0O0O00000OOO0O :STAT_countpx (O0O0O0O00000OOO0O .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O0OO00O00O00OOO0O :STAT_countpx (O0OO00O00O00OOO0O .values ,"严重伤害待评价")),).sort_values (by ="规格计数",ascending =[False ],na_position ="last").reset_index ()#line:4790
		O000O0OOOO0000O00 ["报表类型"]="dfx_guige"#line:4791
		if ini ["模式"]=="药品":#line:4792
			O000O0OOOO0000O00 =O000O0OOOO0000O00 .rename (columns ={"待评价数":"新的数量"})#line:4793
			O000O0OOOO0000O00 =O000O0OOOO0000O00 .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4794
		return O000O0OOOO0000O00 #line:4796
	def df_findrisk (OOOO0OO0O0O0OO0O0 ,OOO00O0OO00O000O0 ):#line:4798
		""#line:4799
		if OOO00O0OO00O000O0 =="产品批号":#line:4800
			return STAT_find_risk (OOOO0OO0O0O0OO0O0 .df [(OOOO0OO0O0O0OO0O0 .df ["产品类别"]!="有源")],["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],"注册证编号/曾用注册证编号",OOO00O0OO00O000O0 )#line:4801
		else :#line:4802
			return STAT_find_risk (OOOO0OO0O0O0OO0O0 .df ,["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],"注册证编号/曾用注册证编号",OOO00O0OO00O000O0 )#line:4803
	def df_find_all_keword_risk (O0OO0000OOOO0OO00 ,O00O000OO000OOO00 ,*O000OOOOOO0O0000O ):#line:4805
		""#line:4806
		OO00OOOOO0000OO0O =O0OO0000OOOO0OO00 .df .copy ()#line:4808
		O0O000OOOOOO0OOO0 =time .time ()#line:4809
		O0O00OO0O0O0000OO =peizhidir +"0（范例）比例失衡关键字库.xls"#line:4810
		if "报告类型-新的"in OO00OOOOO0000OO0O .columns :#line:4811
			OOOO0O0OOO0OOOOO0 ="药品"#line:4812
		else :#line:4813
			OOOO0O0OOO0OOOOO0 ="器械"#line:4814
		O0O0O0OOO0OOOO000 =pd .read_excel (O0O00OO0O0O0000OO ,header =0 ,sheet_name =OOOO0O0OOO0OOOOO0 ).reset_index (drop =True )#line:4815
		try :#line:4818
			if len (O000OOOOOO0O0000O [0 ])>0 :#line:4819
				O0O0O0OOO0OOOO000 =O0O0O0OOO0OOOO000 .loc [O0O0O0OOO0OOOO000 ["适用范围"].str .contains (O000OOOOOO0O0000O [0 ],na =False )].copy ().reset_index (drop =True )#line:4820
		except :#line:4821
			pass #line:4822
		O0OOOOOO00OOO00OO =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]#line:4824
		OO00000O0O0OOOO0O =O0OOOOOO00OOO00OO [-1 ]#line:4825
		OOOOO0OO0OOOO0OOO =OO00OOOOO0000OO0O .groupby (O0OOOOOO00OOO00OO ).agg (总数量 =(OO00000O0O0OOOO0O ,"count"),严重伤害数 =("伤害",lambda OOO00OOOOO0O0O000 :STAT_countpx (OOO00OOOOO0O0O000 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0OOO0O000O0000 :STAT_countpx (O0O0OOO0O000O0000 .values ,"死亡")),)#line:4830
		OO00000O0O0OOOO0O =O0OOOOOO00OOO00OO [-1 ]#line:4831
		O000O0OOOO00OOO00 =O0OOOOOO00OOO00OO .copy ()#line:4833
		O000O0OOOO00OOO00 .append (O00O000OO000OOO00 )#line:4834
		O00OOOO00O00000O0 =OO00OOOOO0000OO0O .groupby (O000O0OOOO00OOO00 ).agg (该元素总数量 =(OO00000O0O0OOOO0O ,"count"),).reset_index ()#line:4837
		OOOOO0OO0OOOO0OOO =OOOOO0OO0OOOO0OOO [(OOOOO0OO0OOOO0OOO ["总数量"]>=3 )].reset_index ()#line:4840
		O0OO0O00OO0O0OOO0 =[]#line:4841
		O00OO0O0OOO0O0OOO =0 #line:4845
		O00O0O00O000O00O0 =int (len (OOOOO0OO0OOOO0OOO ))#line:4846
		for O0OOOO000OOOO00OO ,OO0OOO00O00OOOO0O ,O0OOOO0000000OOO0 ,O0OOO0O0OO00OO00O in zip (OOOOO0OO0OOOO0OOO ["产品名称"].values ,OOOOO0OO0OOOO0OOO ["产品类别"].values ,OOOOO0OO0OOOO0OOO [OO00000O0O0OOOO0O ].values ,OOOOO0OO0OOOO0OOO ["总数量"].values ):#line:4847
			O00OO0O0OOO0O0OOO +=1 #line:4848
			if (time .time ()-O0O000OOOOOO0OOO0 )>3 :#line:4850
				root .attributes ("-topmost",True )#line:4851
				PROGRAM_change_schedule (O00OO0O0OOO0O0OOO ,O00O0O00O000O00O0 )#line:4852
				root .attributes ("-topmost",False )#line:4853
			O0OO0O00O0OOOO0O0 =OO00OOOOO0000OO0O [(OO00OOOOO0000OO0O [OO00000O0O0OOOO0O ]==O0OOOO0000000OOO0 )].copy ()#line:4854
			O0O0O0OOO0OOOO000 ["SELECT"]=O0O0O0OOO0OOOO000 .apply (lambda OOOO0OOO0O0OOOO0O :(OOOO0OOO0O0OOOO0O ["适用范围"]in O0OOOO000OOOO00OO )or (OOOO0OOO0O0OOOO0O ["适用范围"]in OO0OOO00O00OOOO0O )or (OOOO0OOO0O0OOOO0O ["适用范围"]=="通用"),axis =1 )#line:4855
			OO00O00O000OO000O =O0O0O0OOO0OOOO000 [(O0O0O0OOO0OOOO000 ["SELECT"]==True )].reset_index ()#line:4856
			if len (OO00O00O000OO000O )>0 :#line:4857
				for OO00O000OOO0OOOOO ,OO00O0O0O00OO0OO0 ,OOO000O00OO000OO0 in zip (OO00O00O000OO000O ["值"].values ,OO00O00O000OO000O ["查找位置"].values ,OO00O00O000OO000O ["排除值"].values ):#line:4859
					OO0O0O000O0OOO000 =O0OO0O00O0OOOO0O0 .copy ()#line:4860
					OOOO000O0OOOOOO00 =TOOLS_get_list (OO00O000OOO0OOOOO )[0 ]#line:4861
					OO0O0O000O0OOO000 ["关键字查找列"]=""#line:4863
					for O00O0OO00OOOOO000 in TOOLS_get_list (OO00O0O0O00OO0OO0 ):#line:4864
						OO0O0O000O0OOO000 ["关键字查找列"]=OO0O0O000O0OOO000 ["关键字查找列"]+OO0O0O000O0OOO000 [O00O0OO00OOOOO000 ].astype ("str")#line:4865
					OO0O0O000O0OOO000 .loc [OO0O0O000O0OOO000 ["关键字查找列"].str .contains (OO00O000OOO0OOOOO ,na =False ),"关键字"]=OOOO000O0OOOOOO00 #line:4867
					if str (OOO000O00OO000OO0 )!="nan":#line:4870
						OO0O0O000O0OOO000 =OO0O0O000O0OOO000 .loc [~OO0O0O000O0OOO000 ["关键字查找列"].str .contains (OOO000O00OO000OO0 ,na =False )].copy ()#line:4871
					if (len (OO0O0O000O0OOO000 ))<1 :#line:4873
						continue #line:4874
					OO0OO0OOOO0O0OOOO =STAT_find_keyword_risk (OO0O0O000O0OOO000 ,["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","关键字"],"关键字",O00O000OO000OOO00 ,int (O0OOO0O0OO00OO00O ))#line:4876
					if len (OO0OO0OOOO0O0OOOO )>0 :#line:4877
						OO0OO0OOOO0O0OOOO ["关键字组合"]=OO00O000OOO0OOOOO #line:4878
						OO0OO0OOOO0O0OOOO ["排除值"]=OOO000O00OO000OO0 #line:4879
						OO0OO0OOOO0O0OOOO ["关键字查找列"]=OO00O0O0O00OO0OO0 #line:4880
						O0OO0O00OO0O0OOO0 .append (OO0OO0OOOO0O0OOOO )#line:4881
		O00O0O0OOOOOOOOOO =pd .concat (O0OO0O00OO0O0OOO0 )#line:4885
		O00O0O0OOOOOOOOOO =pd .merge (O00O0O0OOOOOOOOOO ,O00OOOO00O00000O0 ,on =O000O0OOOO00OOO00 ,how ="left")#line:4888
		O00O0O0OOOOOOOOOO ["关键字数量比例"]=round (O00O0O0OOOOOOOOOO ["计数"]/O00O0O0OOOOOOOOOO ["该元素总数量"],2 )#line:4889
		O00O0O0OOOOOOOOOO =O00O0O0OOOOOOOOOO .reset_index (drop =True )#line:4891
		if len (O00O0O0OOOOOOOOOO )>0 :#line:4892
			O00O0O0OOOOOOOOOO ["风险评分"]=0 #line:4893
			O00O0O0OOOOOOOOOO ["报表类型"]="keyword_findrisk"+O00O000OO000OOO00 #line:4894
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["计数"]>=3 ),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+3 #line:4895
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["计数"]>=(O00O0O0OOOOOOOOOO ["数量均值"]+O00O0O0OOOOOOOOOO ["数量标准差"])),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+1 #line:4896
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["计数"]>=O00O0O0OOOOOOOOOO ["数量CI"]),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+1 #line:4897
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["关键字数量比例"]>0.5 )&(O00O0O0OOOOOOOOOO ["计数"]>=3 ),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+1 #line:4898
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["严重伤害数"]>=3 ),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+1 #line:4899
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["单位个数"]>=3 ),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+1 #line:4900
			O00O0O0OOOOOOOOOO .loc [(O00O0O0OOOOOOOOOO ["死亡数量"]>=1 ),"风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+10 #line:4901
			O00O0O0OOOOOOOOOO ["风险评分"]=O00O0O0OOOOOOOOOO ["风险评分"]+O00O0O0OOOOOOOOOO ["单位个数"]/100 #line:4902
			O00O0O0OOOOOOOOOO =O00O0O0OOOOOOOOOO .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:4903
		print ("耗时：",(time .time ()-O0O000OOOOOO0OOO0 ))#line:4909
		return O00O0O0OOOOOOOOOO #line:4910
	def df_ror (O00OO0O0O000OO0OO ,OOO000000O000OO0O ,*O0OO0OO0OO00O00OO ):#line:4913
		""#line:4914
		O00OOOOO00O000OOO =O00OO0O0O000OO0OO .df .copy ()#line:4916
		O0OOOOOO0OOOO00O0 =time .time ()#line:4917
		O0OO00O00000OO00O =peizhidir +"0（范例）比例失衡关键字库.xls"#line:4918
		if "报告类型-新的"in O00OOOOO00O000OOO .columns :#line:4919
			OO0O0OO0O000000OO ="药品"#line:4920
		else :#line:4922
			OO0O0OO0O000000OO ="器械"#line:4923
		OOO0OO00000000O0O =pd .read_excel (O0OO00O00000OO00O ,header =0 ,sheet_name =OO0O0OO0O000000OO ).reset_index (drop =True )#line:4924
		if "css"in O00OOOOO00O000OOO .columns :#line:4927
			OO0OOO00OOOOOOOO0 =O00OOOOO00O000OOO .copy ()#line:4928
			OO0OOO00OOOOOOOO0 ["器械故障表现"]=OO0OOO00OOOOOOOO0 ["器械故障表现"].fillna ("未填写")#line:4929
			OO0OOO00OOOOOOOO0 ["器械故障表现"]=OO0OOO00OOOOOOOO0 ["器械故障表现"].str .replace ("*","",regex =False )#line:4930
			OOOO000OOO00O0OOO ="use("+str ("器械故障表现")+").file"#line:4931
			O0O00OO0OOO0O000O =str (Counter (TOOLS_get_list0 (OOOO000OOO00O0OOO ,OO0OOO00OOOOOOOO0 ,1000 ))).replace ("Counter({","{")#line:4932
			O0O00OO0OOO0O000O =O0O00OO0OOO0O000O .replace ("})","}")#line:4933
			O0O00OO0OOO0O000O =ast .literal_eval (O0O00OO0OOO0O000O )#line:4934
			OOO0OO00000000O0O =pd .DataFrame .from_dict (O0O00OO0OOO0O000O ,orient ="index",columns =["计数"]).reset_index ()#line:4935
			OOO0OO00000000O0O ["适用范围列"]="产品类别"#line:4936
			OOO0OO00000000O0O ["适用范围"]="无源"#line:4937
			OOO0OO00000000O0O ["查找位置"]="伤害表现"#line:4938
			OOO0OO00000000O0O ["值"]=OOO0OO00000000O0O ["index"]#line:4939
			OOO0OO00000000O0O ["排除值"]="-没有排除值-"#line:4940
			del OOO0OO00000000O0O ["index"]#line:4941
		O0O0O00OO00OO0O00 =OOO000000O000OO0O [-2 ]#line:4944
		OOO0OO0O00O0OOOOO =OOO000000O000OO0O [-1 ]#line:4945
		OOOO0O0O0OOO0O00O =OOO000000O000OO0O [:-1 ]#line:4946
		try :#line:4949
			if len (O0OO0OO0OO00O00OO [0 ])>0 :#line:4950
				O0O0O00OO00OO0O00 =OOO000000O000OO0O [-3 ]#line:4951
				OOO0OO00000000O0O =OOO0OO00000000O0O .loc [OOO0OO00000000O0O ["适用范围"].str .contains (O0OO0OO0OO00O00OO [0 ],na =False )].copy ().reset_index (drop =True )#line:4952
				O00O00000O00O00OO =O00OOOOO00O000OOO .groupby (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (该元素总数量 =(OOO0OO0O00O0OOOOO ,"count"),该元素严重伤害数 =("伤害",lambda O00OO00OOOO0O0OOO :STAT_countpx (O00OO00OOOO0O0OOO .values ,"严重伤害")),该元素死亡数量 =("伤害",lambda O00O00O0O00OOOOOO :STAT_countpx (O00O00O0O00OOOOOO .values ,"死亡")),该元素单位个数 =("单位名称","nunique"),该元素单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:4959
				O0O00OOO00O000O0O =O00OOOOO00O000OOO .groupby (["产品类别","规整后品类"]).agg (所有元素总数量 =(O0O0O00OO00OO0O00 ,"count"),所有元素严重伤害数 =("伤害",lambda O00O0OO00OO000O0O :STAT_countpx (O00O0OO00OO000O0O .values ,"严重伤害")),所有元素死亡数量 =("伤害",lambda OOO0O000OO0O0OOO0 :STAT_countpx (OOO0O000OO0O0OOO0 .values ,"死亡")),)#line:4964
				if len (O0O00OOO00O000O0O )>1 :#line:4965
					text .insert (END ,"注意，产品类别有两种，产品名称规整疑似不正确！")#line:4966
				O00O00000O00O00OO =pd .merge (O00O00000O00O00OO ,O0O00OOO00O000O0O ,on =["产品类别","规整后品类"],how ="left").reset_index ()#line:4968
		except :#line:4970
			text .insert (END ,"\n目前结果为未进行名称规整的结果！\n")#line:4971
			O00O00000O00O00OO =O00OOOOO00O000OOO .groupby (OOO000000O000OO0O ).agg (该元素总数量 =(OOO0OO0O00O0OOOOO ,"count"),该元素严重伤害数 =("伤害",lambda O000O000OO0OO0O00 :STAT_countpx (O000O000OO0OO0O00 .values ,"严重伤害")),该元素死亡数量 =("伤害",lambda O0OOO0000OO00O0OO :STAT_countpx (O0OOO0000OO00O0OO .values ,"死亡")),该元素单位个数 =("单位名称","nunique"),该元素单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:4978
			O0O00OOO00O000O0O =O00OOOOO00O000OOO .groupby (OOOO0O0O0OOO0O00O ).agg (所有元素总数量 =(O0O0O00OO00OO0O00 ,"count"),所有元素严重伤害数 =("伤害",lambda O00OO0O00O0000O0O :STAT_countpx (O00OO0O00O0000O0O .values ,"严重伤害")),所有元素死亡数量 =("伤害",lambda OOOO00O0O0OO0OOOO :STAT_countpx (OOOO00O0O0OO0OOOO .values ,"死亡")),)#line:4984
			O00O00000O00O00OO =pd .merge (O00O00000O00O00OO ,O0O00OOO00O000O0O ,on =OOOO0O0O0OOO0O00O ,how ="left").reset_index ()#line:4988
		O0O00OOO00O000O0O =O0O00OOO00O000O0O [(O0O00OOO00O000O0O ["所有元素总数量"]>=3 )].reset_index ()#line:4990
		O00OO0OO0OO0OOOOO =[]#line:4991
		if ("产品名称"not in O0O00OOO00O000O0O .columns )and ("规整后品类"not in O0O00OOO00O000O0O .columns ):#line:4993
			O0O00OOO00O000O0O ["产品名称"]=O0O00OOO00O000O0O ["产品类别"]#line:4994
		if "规整后品类"not in O0O00OOO00O000O0O .columns :#line:5000
			O0O00OOO00O000O0O ["规整后品类"]="不适用"#line:5001
		O00000000O000000O =0 #line:5004
		OO00OOO0O0000O000 =int (len (O0O00OOO00O000O0O ))#line:5005
		for O0O0000OOO000000O ,O00OOO00O0O000OO0 ,O0OOOOO0O0OO00000 ,OO0OO0O000OO00O00 in zip (O0O00OOO00O000O0O ["规整后品类"],O0O00OOO00O000O0O ["产品类别"],O0O00OOO00O000O0O [O0O0O00OO00OO0O00 ],O0O00OOO00O000O0O ["所有元素总数量"]):#line:5006
			O00000000O000000O +=1 #line:5007
			if (time .time ()-O0OOOOOO0OOOO00O0 )>3 :#line:5008
				root .attributes ("-topmost",True )#line:5009
				PROGRAM_change_schedule (O00000000O000000O ,OO00OOO0O0000O000 )#line:5010
				root .attributes ("-topmost",False )#line:5011
			OOO0OO000OO00O000 =O00OOOOO00O000OOO [(O00OOOOO00O000OOO [O0O0O00OO00OO0O00 ]==O0OOOOO0O0OO00000 )].copy ()#line:5012
			OOO0OO00000000O0O ["SELECT"]=OOO0OO00000000O0O .apply (lambda OO0O0O00000OO0O0O :((O0O0000OOO000000O in OO0O0O00000OO0O0O ["适用范围"])or (OO0O0O00000OO0O0O ["适用范围"]in O00OOO00O0O000OO0 )),axis =1 )#line:5013
			O000OOOOOOOO0OOOO =OOO0OO00000000O0O [(OOO0OO00000000O0O ["SELECT"]==True )].reset_index ()#line:5014
			if len (O000OOOOOOOO0OOOO )>0 :#line:5015
				for O0O0O00O00OOO00OO ,O0OOO000O0OOOOOO0 ,O000000O00OO000OO in zip (O000OOOOOOOO0OOOO ["值"].values ,O000OOOOOOOO0OOOO ["查找位置"].values ,O000OOOOOOOO0OOOO ["排除值"].values ):#line:5017
					O0OO00O0OO000O000 =OOO0OO000OO00O000 .copy ()#line:5018
					O0O00OOOO000OO000 =TOOLS_get_list (O0O0O00O00OOO00OO )[0 ]#line:5019
					O0O00OO000O0O0O00 ="关键字查找列"#line:5020
					O0OO00O0OO000O000 [O0O00OO000O0O0O00 ]=""#line:5021
					for OO00O00000O0O0O00 in TOOLS_get_list (O0OOO000O0OOOOOO0 ):#line:5022
						O0OO00O0OO000O000 [O0O00OO000O0O0O00 ]=O0OO00O0OO000O000 [O0O00OO000O0O0O00 ]+O0OO00O0OO000O000 [OO00O00000O0O0O00 ].astype ("str")#line:5023
					O0OO00O0OO000O000 .loc [O0OO00O0OO000O000 [O0O00OO000O0O0O00 ].str .contains (O0O0O00O00OOO00OO ,na =False ),"关键字"]=O0O00OOOO000OO000 #line:5025
					if str (O000000O00OO000OO )!="nan":#line:5028
						O0OO00O0OO000O000 =O0OO00O0OO000O000 .loc [~O0OO00O0OO000O000 ["关键字查找列"].str .contains (O000000O00OO000OO ,na =False )].copy ()#line:5029
					if (len (O0OO00O0OO000O000 ))<1 :#line:5032
						continue #line:5033
					for OO0OOO0OOO00000OO in zip (O0OO00O0OO000O000 [OOO0OO0O00O0OOOOO ].drop_duplicates ()):#line:5035
						try :#line:5038
							if OO0OOO0OOO00000OO [0 ]!=O0OO0OO0OO00O00OO [1 ]:#line:5039
								continue #line:5040
						except :#line:5041
							pass #line:5042
						O00000OOO0OO0O000 ={"合并列":{O0O00OO000O0O0O00 :O0OOO000O0OOOOOO0 },"等于":{O0O0O00OO00OO0O00 :O0OOOOO0O0OO00000 ,OOO0OO0O00O0OOOOO :OO0OOO0OOO00000OO [0 ]},"不等于":{},"包含":{O0O00OO000O0O0O00 :O0O0O00O00OOO00OO },"不包含":{O0O00OO000O0O0O00 :O000000O00OO000OO }}#line:5050
						O00OO0OOOO0000000 =STAT_PPR_ROR_1 (OOO0OO0O00O0OOOOO ,str (OO0OOO0OOO00000OO [0 ]),"关键字查找列",O0O0O00O00OOO00OO ,O0OO00O0OO000O000 )+(O0O0O00O00OOO00OO ,O000000O00OO000OO ,O0OOO000O0OOOOOO0 ,O0OOOOO0O0OO00000 ,OO0OOO0OOO00000OO [0 ],str (O00000OOO0OO0O000 ))#line:5052
						if O00OO0OOOO0000000 [1 ]>0 :#line:5054
							OO0O00OOO0OO00000 =pd .DataFrame (columns =["特定关键字","出现频次","占比","ROR值","ROR值的95%CI下限","PRR值","PRR值的95%CI下限","卡方值","四分表","关键字组合","排除值","关键字查找列",O0O0O00OO00OO0O00 ,OOO0OO0O00O0OOOOO ,"报表定位"])#line:5056
							OO0O00OOO0OO00000 .loc [0 ]=O00OO0OOOO0000000 #line:5057
							O00OO0OO0OO0OOOOO .append (OO0O00OOO0OO00000 )#line:5058
		OO00O0O000O00OOO0 =pd .concat (O00OO0OO0OO0OOOOO )#line:5062
		OO00O0O000O00OOO0 =pd .merge (O00O00000O00O00OO ,OO00O0O000O00OOO0 ,on =[O0O0O00OO00OO0O00 ,OOO0OO0O00O0OOOOO ],how ="right")#line:5066
		OO00O0O000O00OOO0 =OO00O0O000O00OOO0 .reset_index (drop =True )#line:5067
		del OO00O0O000O00OOO0 ["index"]#line:5068
		if len (OO00O0O000O00OOO0 )>0 :#line:5069
			OO00O0O000O00OOO0 ["风险评分"]=0 #line:5070
			OO00O0O000O00OOO0 ["报表类型"]="ROR"#line:5071
			OO00O0O000O00OOO0 .loc [(OO00O0O000O00OOO0 ["出现频次"]>=3 ),"风险评分"]=OO00O0O000O00OOO0 ["风险评分"]+3 #line:5072
			OO00O0O000O00OOO0 .loc [(OO00O0O000O00OOO0 ["ROR值的95%CI下限"]>1 ),"风险评分"]=OO00O0O000O00OOO0 ["风险评分"]+1 #line:5073
			OO00O0O000O00OOO0 .loc [(OO00O0O000O00OOO0 ["PRR值的95%CI下限"]>1 ),"风险评分"]=OO00O0O000O00OOO0 ["风险评分"]+1 #line:5074
			OO00O0O000O00OOO0 ["风险评分"]=OO00O0O000O00OOO0 ["风险评分"]+OO00O0O000O00OOO0 ["该元素单位个数"]/100 #line:5075
			OO00O0O000O00OOO0 =OO00O0O000O00OOO0 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:5076
		print ("耗时：",(time .time ()-O0OOOOOO0OOOO00O0 ))#line:5082
		return OO00O0O000O00OOO0 #line:5083
	def df_chiyouren (OO00O000O00OO00OO ):#line:5089
		""#line:5090
		OO0O0OO0OO0O0O0O0 =OO00O000O00OO00OO .df .copy ().reset_index (drop =True )#line:5091
		OO0O0OO0OO0O0O0O0 ["总报告数"]=data ["报告编码"].copy ()#line:5092
		OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"总待评价数量"]=data ["报告编码"]#line:5093
		OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害"),"严重伤害报告数"]=data ["报告编码"]#line:5094
		OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价")&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害"),"严重伤害待评价数量"]=data ["报告编码"]#line:5095
		OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价")&(OO0O0OO0OO0O0O0O0 ["伤害"]=="其他"),"其他待评价数量"]=data ["报告编码"]#line:5096
		O0OOO00000O0O0OOO =OO0O0OO0OO0O0O0O0 .groupby (["上市许可持有人名称"]).aggregate ({"总报告数":"nunique","总待评价数量":"nunique","严重伤害报告数":"nunique","严重伤害待评价数量":"nunique","其他待评价数量":"nunique"})#line:5099
		O0OOO00000O0O0OOO ["严重伤害待评价比例"]=round (O0OOO00000O0O0OOO ["严重伤害待评价数量"]/O0OOO00000O0O0OOO ["严重伤害报告数"]*100 ,2 )#line:5104
		O0OOO00000O0O0OOO ["总待评价比例"]=round (O0OOO00000O0O0OOO ["总待评价数量"]/O0OOO00000O0O0OOO ["总报告数"]*100 ,2 )#line:5107
		O0OOO00000O0O0OOO ["总报告数"]=O0OOO00000O0O0OOO ["总报告数"].fillna (0 )#line:5108
		O0OOO00000O0O0OOO ["总待评价比例"]=O0OOO00000O0O0OOO ["总待评价比例"].fillna (0 )#line:5109
		O0OOO00000O0O0OOO ["严重伤害报告数"]=O0OOO00000O0O0OOO ["严重伤害报告数"].fillna (0 )#line:5110
		O0OOO00000O0O0OOO ["严重伤害待评价比例"]=O0OOO00000O0O0OOO ["严重伤害待评价比例"].fillna (0 )#line:5111
		O0OOO00000O0O0OOO ["总报告数"]=O0OOO00000O0O0OOO ["总报告数"].astype (int )#line:5112
		O0OOO00000O0O0OOO ["总待评价比例"]=O0OOO00000O0O0OOO ["总待评价比例"].astype (int )#line:5113
		O0OOO00000O0O0OOO ["严重伤害报告数"]=O0OOO00000O0O0OOO ["严重伤害报告数"].astype (int )#line:5114
		O0OOO00000O0O0OOO ["严重伤害待评价比例"]=O0OOO00000O0O0OOO ["严重伤害待评价比例"].astype (int )#line:5115
		O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .sort_values (by =["总报告数","总待评价比例"],ascending =[False ,False ],na_position ="last")#line:5118
		if "场所名称"in OO0O0OO0OO0O0O0O0 .columns :#line:5120
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["审核日期"]=="未填写"),"审核日期"]=3000 -12 -12 #line:5121
			OO0O0OO0OO0O0O0O0 ["报告时限"]=pd .Timestamp .today ()-pd .to_datetime (OO0O0OO0OO0O0O0O0 ["审核日期"])#line:5122
			OO0O0OO0OO0O0O0O0 ["报告时限2"]=45 -(pd .Timestamp .today ()-pd .to_datetime (OO0O0OO0OO0O0O0O0 ["审核日期"])).dt .days #line:5123
			OO0O0OO0OO0O0O0O0 ["报告时限"]=OO0O0OO0OO0O0O0O0 ["报告时限"].dt .days #line:5124
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限"]>45 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"待评价且超出当前日期45天（严重）"]=1 #line:5125
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限"]>45 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="其他")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"待评价且超出当前日期45天（其他）"]=1 #line:5126
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限"]>30 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="死亡")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"待评价且超出当前日期30天（死亡）"]=1 #line:5127
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=1 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["报告时限2"]>0 )&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩1天"]=1 #line:5129
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]>1 )&(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=3 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩1-3天"]=1 #line:5130
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]>3 )&(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=5 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩3-5天"]=1 #line:5131
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]>5 )&(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=10 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩5-10天"]=1 #line:5132
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]>10 )&(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=20 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩10-20天"]=1 #line:5133
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]>20 )&(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=30 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩20-30天"]=1 #line:5134
			OO0O0OO0OO0O0O0O0 .loc [(OO0O0OO0OO0O0O0O0 ["报告时限2"]>30 )&(OO0O0OO0OO0O0O0O0 ["报告时限2"]<=45 )&(OO0O0OO0OO0O0O0O0 ["伤害"]=="严重伤害")&(OO0O0OO0OO0O0O0O0 ["持有人报告状态"]=="待评价"),"严重待评价且只剩30-45天"]=1 #line:5135
			del OO0O0OO0OO0O0O0O0 ["报告时限2"]#line:5136
			OO0OOO000O00O0000 =(OO0O0OO0OO0O0O0O0 .groupby (["上市许可持有人名称"]).aggregate ({"待评价且超出当前日期45天（严重）":"sum","待评价且超出当前日期45天（其他）":"sum","待评价且超出当前日期30天（死亡）":"sum","严重待评价且只剩1天":"sum","严重待评价且只剩1-3天":"sum","严重待评价且只剩3-5天":"sum","严重待评价且只剩5-10天":"sum","严重待评价且只剩10-20天":"sum","严重待评价且只剩20-30天":"sum","严重待评价且只剩30-45天":"sum"}).reset_index ())#line:5138
			O0OOO00000O0O0OOO =pd .merge (O0OOO00000O0O0OOO ,OO0OOO000O00O0000 ,on =["上市许可持有人名称"],how ="outer",)#line:5139
			O0OOO00000O0O0OOO ["待评价且超出当前日期45天（严重）"]=O0OOO00000O0O0OOO ["待评价且超出当前日期45天（严重）"].fillna (0 )#line:5140
			O0OOO00000O0O0OOO ["待评价且超出当前日期45天（严重）"]=O0OOO00000O0O0OOO ["待评价且超出当前日期45天（严重）"].astype (int )#line:5141
			O0OOO00000O0O0OOO ["待评价且超出当前日期45天（其他）"]=O0OOO00000O0O0OOO ["待评价且超出当前日期45天（其他）"].fillna (0 )#line:5142
			O0OOO00000O0O0OOO ["待评价且超出当前日期45天（其他）"]=O0OOO00000O0O0OOO ["待评价且超出当前日期45天（其他）"].astype (int )#line:5143
			O0OOO00000O0O0OOO ["待评价且超出当前日期30天（死亡）"]=O0OOO00000O0O0OOO ["待评价且超出当前日期30天（死亡）"].fillna (0 )#line:5144
			O0OOO00000O0O0OOO ["待评价且超出当前日期30天（死亡）"]=O0OOO00000O0O0OOO ["待评价且超出当前日期30天（死亡）"].astype (int )#line:5145
			O0OOO00000O0O0OOO ["严重待评价且只剩1天"]=O0OOO00000O0O0OOO ["严重待评价且只剩1天"].fillna (0 )#line:5147
			O0OOO00000O0O0OOO ["严重待评价且只剩1天"]=O0OOO00000O0O0OOO ["严重待评价且只剩1天"].astype (int )#line:5148
			O0OOO00000O0O0OOO ["严重待评价且只剩1-3天"]=O0OOO00000O0O0OOO ["严重待评价且只剩1-3天"].fillna (0 )#line:5149
			O0OOO00000O0O0OOO ["严重待评价且只剩1-3天"]=O0OOO00000O0O0OOO ["严重待评价且只剩1-3天"].astype (int )#line:5150
			O0OOO00000O0O0OOO ["严重待评价且只剩3-5天"]=O0OOO00000O0O0OOO ["严重待评价且只剩3-5天"].fillna (0 )#line:5151
			O0OOO00000O0O0OOO ["严重待评价且只剩3-5天"]=O0OOO00000O0O0OOO ["严重待评价且只剩3-5天"].astype (int )#line:5152
			O0OOO00000O0O0OOO ["严重待评价且只剩5-10天"]=O0OOO00000O0O0OOO ["严重待评价且只剩5-10天"].fillna (0 )#line:5153
			O0OOO00000O0O0OOO ["严重待评价且只剩5-10天"]=O0OOO00000O0O0OOO ["严重待评价且只剩5-10天"].astype (int )#line:5154
			O0OOO00000O0O0OOO ["严重待评价且只剩10-20天"]=O0OOO00000O0O0OOO ["严重待评价且只剩10-20天"].fillna (0 )#line:5155
			O0OOO00000O0O0OOO ["严重待评价且只剩10-20天"]=O0OOO00000O0O0OOO ["严重待评价且只剩10-20天"].astype (int )#line:5156
			O0OOO00000O0O0OOO ["严重待评价且只剩20-30天"]=O0OOO00000O0O0OOO ["严重待评价且只剩20-30天"].fillna (0 )#line:5157
			O0OOO00000O0O0OOO ["严重待评价且只剩20-30天"]=O0OOO00000O0O0OOO ["严重待评价且只剩20-30天"].astype (int )#line:5158
			O0OOO00000O0O0OOO ["严重待评价且只剩30-45天"]=O0OOO00000O0O0OOO ["严重待评价且只剩30-45天"].fillna (0 )#line:5159
			O0OOO00000O0O0OOO ["严重待评价且只剩30-45天"]=O0OOO00000O0O0OOO ["严重待评价且只剩30-45天"].astype (int )#line:5160
		O0OOO00000O0O0OOO ["总待评价数量"]=O0OOO00000O0O0OOO ["总待评价数量"].fillna (0 )#line:5162
		O0OOO00000O0O0OOO ["总待评价数量"]=O0OOO00000O0O0OOO ["总待评价数量"].astype (int )#line:5163
		O0OOO00000O0O0OOO ["严重伤害待评价数量"]=O0OOO00000O0O0OOO ["严重伤害待评价数量"].fillna (0 )#line:5164
		O0OOO00000O0O0OOO ["严重伤害待评价数量"]=O0OOO00000O0O0OOO ["严重伤害待评价数量"].astype (int )#line:5165
		O0OOO00000O0O0OOO ["其他待评价数量"]=O0OOO00000O0O0OOO ["其他待评价数量"].fillna (0 )#line:5166
		O0OOO00000O0O0OOO ["其他待评价数量"]=O0OOO00000O0O0OOO ["其他待评价数量"].astype (int )#line:5167
		OOO00O00O0O000000 =["总报告数","总待评价数量","严重伤害报告数","严重伤害待评价数量","其他待评价数量"]#line:5170
		O0OOO00000O0O0OOO .loc ["合计"]=O0OOO00000O0O0OOO [OOO00O00O0O000000 ].apply (lambda OOO0OO0O00O00O0O0 :OOO0OO0O00O00O0O0 .sum ())#line:5171
		O0OOO00000O0O0OOO [OOO00O00O0O000000 ]=O0OOO00000O0O0OOO [OOO00O00O0O000000 ].apply (lambda OO0O00000OOOOOOO0 :OO0O00000OOOOOOO0 .astype (int ))#line:5172
		O0OOO00000O0O0OOO .iloc [-1 ,0 ]="合计"#line:5173
		if "场所名称"in OO0O0OO0OO0O0O0O0 .columns :#line:5175
			O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .reset_index (drop =True )#line:5176
		else :#line:5177
			O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .reset_index ()#line:5178
		if ini ["模式"]=="药品":#line:5180
			O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .rename (columns ={"总待评价数量":"新的数量"})#line:5181
			O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .rename (columns ={"严重伤害待评价数量":"新的严重的数量"})#line:5182
			O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .rename (columns ={"严重伤害待评价比例":"新的严重的比例"})#line:5183
			O0OOO00000O0O0OOO =O0OOO00000O0O0OOO .rename (columns ={"总待评价比例":"新的比例"})#line:5184
			del O0OOO00000O0O0OOO ["其他待评价数量"]#line:5186
		O0OOO00000O0O0OOO ["报表类型"]="dfx_chiyouren"#line:5187
		return O0OOO00000O0O0OOO #line:5188
	def df_age (OO000O00O0OO0O00O ):#line:5190
		""#line:5191
		O00O0000OOO000000 =OO000O00O0OO0O00O .df .copy ()#line:5192
		O00O0000OOO000000 =O00O0000OOO000000 .drop_duplicates ("报告编码").copy ()#line:5193
		OOOO000OO0O0OO000 =pd .pivot_table (O00O0000OOO000000 .drop_duplicates ("报告编码"),values =["报告编码"],index ="年龄段",columns ="性别",aggfunc ={"报告编码":"nunique"},fill_value ="0",margins =True ,dropna =False ,).rename (columns ={"报告编码":"数量"}).reset_index ()#line:5194
		OOOO000OO0O0OO000 .columns =OOOO000OO0O0OO000 .columns .droplevel (0 )#line:5195
		OOOO000OO0O0OO000 ["构成比(%)"]=round (100 *OOOO000OO0O0OO000 ["All"]/len (O00O0000OOO000000 ),2 )#line:5196
		OOOO000OO0O0OO000 ["累计构成比(%)"]=OOOO000OO0O0OO000 ["构成比(%)"].cumsum ()#line:5197
		OOOO000OO0O0OO000 ["报表类型"]="年龄性别表"#line:5198
		return OOOO000OO0O0OO000 #line:5199
	def df_psur (O0O000O000OOO0OO0 ,*O0OOO00O000O00OO0 ):#line:5201
		""#line:5202
		O00O00OO000OO0OO0 =O0O000O000OOO0OO0 .df .copy ()#line:5203
		O00O0O0OOO0O0OO00 =peizhidir +"0（范例）比例失衡关键字库.xls"#line:5204
		OO0O00O00OOO000OO =len (O00O00OO000OO0OO0 .drop_duplicates ("报告编码"))#line:5205
		if "报告类型-新的"in O00O00OO000OO0OO0 .columns :#line:5209
			O000OO0OOOO0OO0OO ="药品"#line:5210
		elif "皮损形态"in O00O00OO000OO0OO0 .columns :#line:5211
			O000OO0OOOO0OO0OO ="化妆品"#line:5212
		else :#line:5213
			O000OO0OOOO0OO0OO ="器械"#line:5214
		O0OO0OOO0OOO00OO0 =pd .read_excel (O00O0O0OOO0O0OO00 ,header =0 ,sheet_name =O000OO0OOOO0OO0OO )#line:5217
		O00O0O0O00000OO0O =(O0OO0OOO0OOO00OO0 .loc [O0OO0OOO0OOO00OO0 ["适用范围"].str .contains ("通用监测关键字|无源|有源",na =False )].copy ().reset_index (drop =True ))#line:5220
		try :#line:5223
			if O0OOO00O000O00OO0 [0 ]in ["特定品种","通用无源","通用有源"]:#line:5224
				OO0O0OO0O0OO00000 =""#line:5225
				if O0OOO00O000O00OO0 [0 ]=="特定品种":#line:5226
					OO0O0OO0O0OO00000 =O0OO0OOO0OOO00OO0 .loc [O0OO0OOO0OOO00OO0 ["适用范围"].str .contains (O0OOO00O000O00OO0 [1 ],na =False )].copy ().reset_index (drop =True )#line:5227
				if O0OOO00O000O00OO0 [0 ]=="通用无源":#line:5229
					OO0O0OO0O0OO00000 =O0OO0OOO0OOO00OO0 .loc [O0OO0OOO0OOO00OO0 ["适用范围"].str .contains ("通用监测关键字|无源",na =False )].copy ().reset_index (drop =True )#line:5230
				if O0OOO00O000O00OO0 [0 ]=="通用有源":#line:5231
					OO0O0OO0O0OO00000 =O0OO0OOO0OOO00OO0 .loc [O0OO0OOO0OOO00OO0 ["适用范围"].str .contains ("通用监测关键字|有源",na =False )].copy ().reset_index (drop =True )#line:5232
				if O0OOO00O000O00OO0 [0 ]=="体外诊断试剂":#line:5233
					OO0O0OO0O0OO00000 =O0OO0OOO0OOO00OO0 .loc [O0OO0OOO0OOO00OO0 ["适用范围"].str .contains ("体外诊断试剂",na =False )].copy ().reset_index (drop =True )#line:5234
				if len (OO0O0OO0O0OO00000 )<1 :#line:5235
					showinfo (title ="提示",message ="未找到相应的自定义规则，任务结束。")#line:5236
					return 0 #line:5237
				else :#line:5238
					O00O0O0O00000OO0O =OO0O0OO0O0OO00000 #line:5239
		except :#line:5241
			pass #line:5242
		try :#line:5246
			if O000OO0OOOO0OO0OO =="器械"and O0OOO00O000O00OO0 [0 ]=="特定品种作为通用关键字":#line:5247
				O00O0O0O00000OO0O =O0OOO00O000O00OO0 [1 ]#line:5248
		except dddd :#line:5250
			pass #line:5251
		O00OO0O0OO000O0OO =""#line:5254
		O00OOO00OO0OOOOOO ="-其他关键字-不含："#line:5255
		for OOO000O00OO0O0O00 ,OO0OOOOO0OOO00OOO in O00O0O0O00000OO0O .iterrows ():#line:5256
			O00OOO00OO0OOOOOO =O00OOO00OO0OOOOOO +"|"+str (OO0OOOOO0OOO00OOO ["值"])#line:5257
			O00O0O00OOO0O0OOO =OO0OOOOO0OOO00OOO #line:5258
		O00O0O00OOO0O0OOO [2 ]="通用监测关键字"#line:5259
		O00O0O00OOO0O0OOO [4 ]=O00OOO00OO0OOOOOO #line:5260
		O00O0O0O00000OO0O .loc [len (O00O0O0O00000OO0O )]=O00O0O00OOO0O0OOO #line:5261
		O00O0O0O00000OO0O =O00O0O0O00000OO0O .reset_index (drop =True )#line:5262
		if ini ["模式"]=="器械":#line:5266
			O00O00OO000OO0OO0 ["关键字查找列"]=O00O00OO000OO0OO0 ["器械故障表现"].astype (str )+O00O00OO000OO0OO0 ["伤害表现"].astype (str )+O00O00OO000OO0OO0 ["使用过程"].astype (str )+O00O00OO000OO0OO0 ["事件原因分析描述"].astype (str )+O00O00OO000OO0OO0 ["初步处置情况"].astype (str )#line:5267
		else :#line:5268
			O00O00OO000OO0OO0 ["关键字查找列"]=O00O00OO000OO0OO0 ["器械故障表现"]#line:5269
		text .insert (END ,"\n药品查找列默认为不良反应表现,药品规则默认为通用规则。\n器械默认查找列为器械故障表现+伤害表现+使用过程+事件原因分析描述+初步处置情况，器械默认规则为无源通用规则+有源通用规则。\n")#line:5270
		O0O0O0000OO0OO0OO =[]#line:5272
		for OOO000O00OO0O0O00 ,OO0OOOOO0OOO00OOO in O00O0O0O00000OO0O .iterrows ():#line:5274
			O0000O0O000OO0OO0 =OO0OOOOO0OOO00OOO ["值"]#line:5275
			if "-其他关键字-"not in O0000O0O000OO0OO0 :#line:5277
				O0OOOO000O0OO0OOO =O00O00OO000OO0OO0 .loc [O00O00OO000OO0OO0 ["关键字查找列"].str .contains (O0000O0O000OO0OO0 ,na =False )].copy ()#line:5280
				if str (OO0OOOOO0OOO00OOO ["排除值"])!="nan":#line:5281
					O0OOOO000O0OO0OOO =O0OOOO000O0OO0OOO .loc [~O0OOOO000O0OO0OOO ["关键字查找列"].str .contains (str (OO0OOOOO0OOO00OOO ["排除值"]),na =False )].copy ()#line:5283
			else :#line:5285
				O0OOOO000O0OO0OOO =O00O00OO000OO0OO0 .loc [~O00O00OO000OO0OO0 ["关键字查找列"].str .contains (O0000O0O000OO0OO0 ,na =False )].copy ()#line:5288
			O0OOOO000O0OO0OOO ["关键字标记"]=str (O0000O0O000OO0OO0 )#line:5289
			O0OOOO000O0OO0OOO ["关键字计数"]=1 #line:5290
			if len (O0OOOO000O0OO0OOO )>0 :#line:5296
				try :#line:5297
					O00OO000OO00OOO00 =pd .pivot_table (O0OOOO000O0OO0OOO .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns ="伤害PSUR",aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5307
				except :#line:5309
					O00OO000OO00OOO00 =pd .pivot_table (O0OOOO000O0OO0OOO .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns ="伤害",aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5319
				O00OO000OO00OOO00 =O00OO000OO00OOO00 [:-1 ]#line:5320
				O00OO000OO00OOO00 .columns =O00OO000OO00OOO00 .columns .droplevel (0 )#line:5321
				O00OO000OO00OOO00 =O00OO000OO00OOO00 .reset_index ()#line:5322
				if len (O00OO000OO00OOO00 )>0 :#line:5325
					OOO00O0OO0OOO00OO =str (Counter (TOOLS_get_list0 ("use(器械故障表现).file",O0OOOO000O0OO0OOO ,1000 ))).replace ("Counter({","{")#line:5326
					OOO00O0OO0OOO00OO =OOO00O0OO0OOO00OO .replace ("})","}")#line:5327
					OOO00O0OO0OOO00OO =ast .literal_eval (OOO00O0OO0OOO00OO )#line:5328
					O00OO000OO00OOO00 .loc [0 ,"事件分类"]=str (TOOLS_get_list (O00OO000OO00OOO00 .loc [0 ,"关键字标记"])[0 ])#line:5330
					O00OO000OO00OOO00 .loc [0 ,"不良事件名称1"]=str ({O00OO00OO00O0OOO0 :OOOO0OO0O00OOO0OO for O00OO00OO00O0OOO0 ,OOOO0OO0O00OOO0OO in OOO00O0OO0OOO00OO .items ()if STAT_judge_x (str (O00OO00OO00O0OOO0 ),TOOLS_get_list (O0000O0O000OO0OO0 ))==1 })#line:5331
					O00OO000OO00OOO00 .loc [0 ,"不良事件名称2"]=str ({OOOO0OO0O000O0OO0 :OO0O000000OOOOO00 for OOOO0OO0O000O0OO0 ,OO0O000000OOOOO00 in OOO00O0OO0OOO00OO .items ()if STAT_judge_x (str (OOOO0OO0O000O0OO0 ),TOOLS_get_list (O0000O0O000OO0OO0 ))!=1 })#line:5332
					if ini ["模式"]=="药品":#line:5343
						for O00O0O0000OO0OO00 in ["SOC","HLGT","HLT","PT"]:#line:5344
							O00OO000OO00OOO00 [O00O0O0000OO0OO00 ]=OO0OOOOO0OOO00OOO [O00O0O0000OO0OO00 ]#line:5345
					if ini ["模式"]=="器械":#line:5346
						for O00O0O0000OO0OO00 in ["国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]:#line:5347
							O00OO000OO00OOO00 [O00O0O0000OO0OO00 ]=OO0OOOOO0OOO00OOO [O00O0O0000OO0OO00 ]#line:5348
					O0O0O0000OO0OO0OO .append (O00OO000OO00OOO00 )#line:5351
		O00OO0O0OO000O0OO =pd .concat (O0O0O0000OO0OO0OO )#line:5352
		O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:5357
		O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .reset_index ()#line:5358
		O00OO0O0OO000O0OO ["All占比"]=round (O00OO0O0OO000O0OO ["All"]/OO0O00O00OOO000OO *100 ,2 )#line:5360
		O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:5361
		try :#line:5362
			O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .rename (columns ={"其他":"一般"})#line:5363
		except :#line:5364
			pass #line:5365
		try :#line:5367
			O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .rename (columns ={" 一般":"一般"})#line:5368
		except :#line:5369
			pass #line:5370
		try :#line:5371
			O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .rename (columns ={" 严重":"严重"})#line:5372
		except :#line:5373
			pass #line:5374
		try :#line:5375
			O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .rename (columns ={"严重伤害":"严重"})#line:5376
		except :#line:5377
			pass #line:5378
		try :#line:5379
			O00OO0O0OO000O0OO =O00OO0O0OO000O0OO .rename (columns ={"死亡":"死亡(仅支持器械)"})#line:5380
		except :#line:5381
			pass #line:5382
		for OO0OO00O00000OO0O in ["一般","新的一般","严重","新的严重"]:#line:5385
			if OO0OO00O00000OO0O not in O00OO0O0OO000O0OO .columns :#line:5386
				O00OO0O0OO000O0OO [OO0OO00O00000OO0O ]=0 #line:5387
		try :#line:5389
			O00OO0O0OO000O0OO ["严重比"]=round ((O00OO0O0OO000O0OO ["严重"].fillna (0 )+O00OO0O0OO000O0OO ["死亡(仅支持器械)"].fillna (0 ))/O00OO0O0OO000O0OO ["总数量"]*100 ,2 )#line:5390
		except :#line:5391
			O00OO0O0OO000O0OO ["严重比"]=round ((O00OO0O0OO000O0OO ["严重"].fillna (0 )+O00OO0O0OO000O0OO ["新的严重"].fillna (0 ))/O00OO0O0OO000O0OO ["总数量"]*100 ,2 )#line:5392
		O00OO0O0OO000O0OO ["构成比"]=round ((O00OO0O0OO000O0OO ["总数量"].fillna (0 ))/O00OO0O0OO000O0OO ["总数量"].sum ()*100 ,2 )#line:5394
		if ini ["模式"]=="药品":#line:5396
			try :#line:5397
				O00OO0O0OO000O0OO =O00OO0O0OO000O0OO [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)","SOC","HLGT","HLT","PT"]]#line:5398
			except :#line:5399
				O00OO0O0OO000O0OO =O00OO0O0OO000O0OO [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","SOC","HLGT","HLT","PT"]]#line:5400
		elif ini ["模式"]=="器械":#line:5401
			try :#line:5402
				O00OO0O0OO000O0OO =O00OO0O0OO000O0OO [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)","国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]]#line:5403
			except :#line:5404
				O00OO0O0OO000O0OO =O00OO0O0OO000O0OO [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]]#line:5405
		else :#line:5407
			try :#line:5408
				O00OO0O0OO000O0OO =O00OO0O0OO000O0OO [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)"]]#line:5409
			except :#line:5410
				O00OO0O0OO000O0OO =O00OO0O0OO000O0OO [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2"]]#line:5411
		for OOO00O0OOO00O0O0O ,O00O0O00O0000O000 in O00O0O0O00000OO0O .iterrows ():#line:5413
			O00OO0O0OO000O0OO .loc [(O00OO0O0OO000O0OO ["关键字标记"].astype (str )==str (O00O0O00O0000O000 ["值"])),"排除值"]=O00O0O00O0000O000 ["排除值"]#line:5414
		O00OO0O0OO000O0OO ["排除值"]=O00OO0O0OO000O0OO ["排除值"].fillna ("没有排除值")#line:5416
		for OOO0000O00OOO0OOO in ["一般","新的一般","严重","新的严重","总数量","总数量占比","严重比"]:#line:5420
			O00OO0O0OO000O0OO [OOO0000O00OOO0OOO ]=O00OO0O0OO000O0OO [OOO0000O00OOO0OOO ].fillna (0 )#line:5421
		for OOO0000O00OOO0OOO in ["一般","新的一般","严重","新的严重","总数量"]:#line:5423
			O00OO0O0OO000O0OO [OOO0000O00OOO0OOO ]=O00OO0O0OO000O0OO [OOO0000O00OOO0OOO ].astype (int )#line:5424
		O00OO0O0OO000O0OO ["RPN"]="未定义"#line:5427
		O00OO0O0OO000O0OO ["故障原因"]="未定义"#line:5428
		O00OO0O0OO000O0OO ["可造成的伤害"]="未定义"#line:5429
		O00OO0O0OO000O0OO ["应采取的措施"]="未定义"#line:5430
		O00OO0O0OO000O0OO ["发生率"]="未定义"#line:5431
		O00OO0O0OO000O0OO ["报表类型"]="PSUR"#line:5433
		return O00OO0O0OO000O0OO #line:5434
def A0000_Main ():#line:5444
	print ("")#line:5445
if __name__ =='__main__':#line:5447
	root =Tk .Tk ()#line:5450
	root .title (title_all )#line:5451
	try :#line:5452
		root .iconphoto (True ,PhotoImage (file =peizhidir +"0（范例）ico.png"))#line:5453
	except :#line:5454
		pass #line:5455
	sw_root =root .winfo_screenwidth ()#line:5456
	sh_root =root .winfo_screenheight ()#line:5458
	ww_root =700 #line:5460
	wh_root =620 #line:5461
	x_root =(sw_root -ww_root )/2 #line:5463
	y_root =(sh_root -wh_root )/2 #line:5464
	root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:5465
	framecanvas =Frame (root )#line:5470
	canvas =Canvas (framecanvas ,width =680 ,height =30 )#line:5471
	canvas .pack ()#line:5472
	x =StringVar ()#line:5473
	out_rec =canvas .create_rectangle (5 ,5 ,680 ,25 ,outline ="silver",width =1 )#line:5474
	fill_rec =canvas .create_rectangle (5 ,5 ,5 ,25 ,outline ="",width =0 ,fill ="silver")#line:5475
	canvas .create_text (350 ,15 ,text ="总执行进度")#line:5476
	framecanvas .pack ()#line:5477
	try :#line:5484
		frame0 =ttk .Frame (root ,width =90 ,height =20 )#line:5485
		frame0 .pack (side =LEFT )#line:5486
		B_open_files1 =Button (frame0 ,text ="导入数据",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =TOOLS_allfileopen ,)#line:5497
		B_open_files1 .pack ()#line:5498
		B_open_files3 =Button (frame0 ,text ="数据查看",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (ori ,0 ,ori ),)#line:5513
		B_open_files3 .pack ()#line:5514
	except KEY :#line:5517
		pass #line:5518
	text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF")#line:5522
	text .pack (padx =5 ,pady =5 )#line:5523
	text .insert (END ,"\n 本程序适用于整理和分析国家医疗器械不良事件信息系统、国家药品不良反应监测系统和国家化妆品不良反应监测系统中导出的监测数据。如您有改进建议，请点击实用工具-意见反馈。\n")#line:5526
	text .insert (END ,"\n\n")#line:5527
	setting_cfg =read_setting_cfg ()#line:5530
	generate_random_file ()#line:5531
	setting_cfg =open_setting_cfg ()#line:5532
	if setting_cfg ["settingdir"]==0 :#line:5533
		showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:5534
		filepathu =filedialog .askdirectory ()#line:5535
		path =get_directory_path (filepathu )#line:5536
		update_setting_cfg ("settingdir",path )#line:5537
	setting_cfg =open_setting_cfg ()#line:5538
	random_number =int (setting_cfg ["sidori"])#line:5539
	input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:5540
	day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:5541
	sid =random_number *2 +183576 #line:5542
	if input_number ==sid and day_end =="未过期":#line:5543
		usergroup ="用户组=1"#line:5544
		text .insert (END ,usergroup +"   有效期至：")#line:5545
		text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:5546
	else :#line:5547
		text .insert (END ,usergroup )#line:5548
	text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:5549
	peizhidir =str (setting_cfg ["settingdir"])+csdir .split ("pinggutools")[0 ][-1 ]#line:5550
	roox =Toplevel ()#line:5554
	tMain =threading .Thread (target =PROGRAM_showWelcome )#line:5555
	tMain .start ()#line:5556
	t1 =threading .Thread (target =PROGRAM_closeWelcome )#line:5557
	t1 .start ()#line:5558
	root .lift ()#line:5560
	root .attributes ("-topmost",True )#line:5561
	root .attributes ("-topmost",False )#line:5562
	root .mainloop ()#line:5566
	print ("done.")#line:5567
