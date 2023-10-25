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
version_now ="0.0.1"#line:72
usergroup ="用户组=0"#line:73
setting_cfg =""#line:74
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:75
if csdir =="":#line:76
    csdir =str (os .path .dirname (__file__ ))#line:77
    csdir =csdir +csdir .split ("adrmdr")[0 ][-1 ]#line:78
def extract_zip_file (O0000O00O00O00OOO ,O000O00OO000O0OO0 ):#line:86
    import zipfile #line:88
    if O000O00OO000O0OO0 =="":#line:89
        return 0 #line:90
    with zipfile .ZipFile (O0000O00O00O00OOO ,'r')as O00O000OOO00OO0O0 :#line:91
        for O00000OO00O000O00 in O00O000OOO00OO0O0 .infolist ():#line:92
            O00000OO00O000O00 .filename =O00000OO00O000O00 .filename .encode ('cp437').decode ('gbk')#line:94
            O00O000OOO00OO0O0 .extract (O00000OO00O000O00 ,O000O00OO000O0OO0 )#line:95
def get_directory_path (O0OOOOOOOOO00O0O0 ):#line:101
    global csdir #line:103
    if not (os .path .isfile (os .path .join (O0OOOOOOOOO00O0O0 ,'0（范例）比例失衡关键字库.xls'))):#line:105
        extract_zip_file (csdir +"def.py",O0OOOOOOOOO00O0O0 )#line:110
    if O0OOOOOOOOO00O0O0 =="":#line:112
        quit ()#line:113
    return O0OOOOOOOOO00O0O0 #line:114
def convert_and_compare_dates (O0OO00OO0OO0OOOOO ):#line:118
    import datetime #line:119
    OOOO00000O00OO000 =datetime .datetime .now ()#line:120
    try :#line:122
       O0O0O00000O000OOO =datetime .datetime .strptime (str (int (int (O0OO00OO0OO0OOOOO )/4 )),"%Y%m%d")#line:123
    except :#line:124
        print ("fail")#line:125
        return "已过期"#line:126
    if O0O0O00000O000OOO >OOOO00000O00OO000 :#line:128
        return "未过期"#line:130
    else :#line:131
        return "已过期"#line:132
def read_setting_cfg ():#line:134
    global csdir #line:135
    if os .path .exists (csdir +'setting.cfg'):#line:137
        text .insert (END ,"已完成初始化\n")#line:138
        with open (csdir +'setting.cfg','r')as OO0O000O00O000000 :#line:139
            OO0OO00O0O0O0O0O0 =eval (OO0O000O00O000000 .read ())#line:140
    else :#line:141
        OOO0O000OOO0000O0 =csdir +'setting.cfg'#line:143
        with open (OOO0O000OOO0000O0 ,'w')as OO0O000O00O000000 :#line:144
            OO0O000O00O000000 .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:145
        text .insert (END ,"未初始化，正在初始化...\n")#line:146
        OO0OO00O0O0O0O0O0 =read_setting_cfg ()#line:147
    return OO0OO00O0O0O0O0O0 #line:148
def open_setting_cfg ():#line:151
    global csdir #line:152
    with open (csdir +"setting.cfg","r")as OOO00O0OO00OO00OO :#line:154
        OO000O00OO00O0OOO =eval (OOO00O0OO00OO00OO .read ())#line:156
    return OO000O00OO00O0OOO #line:157
def update_setting_cfg (OO00O0O000OOO0OOO ,OO00OO00OO0OOOO0O ):#line:159
    global csdir #line:160
    with open (csdir +"setting.cfg","r")as O00O0OOOOOOOO0OO0 :#line:162
        OOOOOO000O0OO0OOO =eval (O00O0OOOOOOOO0OO0 .read ())#line:164
    if OOOOOO000O0OO0OOO [OO00O0O000OOO0OOO ]==0 or OOOOOO000O0OO0OOO [OO00O0O000OOO0OOO ]=="11111180000808":#line:166
        OOOOOO000O0OO0OOO [OO00O0O000OOO0OOO ]=OO00OO00OO0OOOO0O #line:167
        with open (csdir +"setting.cfg","w")as O00O0OOOOOOOO0OO0 :#line:169
            O00O0OOOOOOOO0OO0 .write (str (OOOOOO000O0OO0OOO ))#line:170
def generate_random_file ():#line:173
    OO0OO000OOOOOOO0O =random .randint (200000 ,299999 )#line:175
    update_setting_cfg ("sidori",OO0OO000OOOOOOO0O )#line:177
def display_random_number ():#line:179
    global csdir #line:180
    O0OOO000O00O0O0O0 =Toplevel ()#line:181
    O0OOO000O00O0O0O0 .title ("ID")#line:182
    OOO0OO0OOO0OOOOO0 =O0OOO000O00O0O0O0 .winfo_screenwidth ()#line:184
    O0OOO00OO00OOOO00 =O0OOO000O00O0O0O0 .winfo_screenheight ()#line:185
    OO000OO00O0OO0O00 =80 #line:187
    O00O000O00OOOO0OO =70 #line:188
    OO00O0OO0000O0O00 =(OOO0OO0OOO0OOOOO0 -OO000OO00O0OO0O00 )/2 #line:190
    OOOOO0O0O0O0O0OO0 =(O0OOO00OO00OOOO00 -O00O000O00OOOO0OO )/2 #line:191
    O0OOO000O00O0O0O0 .geometry ("%dx%d+%d+%d"%(OO000OO00O0OO0O00 ,O00O000O00OOOO0OO ,OO00O0OO0000O0O00 ,OOOOO0O0O0O0O0OO0 ))#line:192
    with open (csdir +"setting.cfg","r")as O0OOO00OO0O00O0OO :#line:195
        O00000OOO000OOO00 =eval (O0OOO00OO0O00O0OO .read ())#line:197
    OOO0O00O0OO00O00O =int (O00000OOO000OOO00 ["sidori"])#line:198
    OOOO0OOOO000OOO0O =OOO0O00O0OO00O00O *2 +183576 #line:199
    print (OOOO0OOOO000OOO0O )#line:201
    O00O0O0OOOO00000O =ttk .Label (O0OOO000O00O0O0O0 ,text =f"机器码: {OOO0O00O0OO00O00O}")#line:203
    O00O00O0OO00OO00O =ttk .Entry (O0OOO000O00O0O0O0 )#line:204
    O00O0O0OOOO00000O .pack ()#line:207
    O00O00O0OO00OO00O .pack ()#line:208
    ttk .Button (O0OOO000O00O0O0O0 ,text ="验证",command =lambda :check_input (O00O00O0OO00OO00O .get (),OOOO0OOOO000OOO0O )).pack ()#line:212
def check_input (O00O0OO0O00OOO0OO ,O00O00OO00O00O00O ):#line:214
    try :#line:218
        OOO00O000000O0OOO =int (str (O00O0OO0O00OOO0OO )[0 :6 ])#line:219
        O0O0OO0OOO000O0O0 =convert_and_compare_dates (str (O00O0OO0O00OOO0OO )[6 :14 ])#line:220
    except :#line:221
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:222
        return 0 #line:223
    if OOO00O000000O0OOO ==O00O00OO00O00O00O and O0O0OO0OOO000O0O0 =="未过期":#line:225
        update_setting_cfg ("sidfinal",O00O0OO0O00OOO0OO )#line:226
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:227
        quit ()#line:228
    else :#line:229
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:230
def update_software (OO0O0OOO00OOOO000 ):#line:235
    global version_now #line:237
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:238
    try :#line:239
        O000OOO0O0OO00000 =requests .get (f"https://pypi.org/pypi/{OO0O0OOO00OOOO000}/json",timeout =2 ).json ()["info"]["version"]#line:240
    except :#line:241
        return "...更新失败。"#line:242
    if O000OOO0O0OO00000 >version_now :#line:243
        text .insert (END ,"\n最新版本为："+O000OOO0O0OO00000 +",正在尝试自动更新....")#line:244
        pip .main (['install',OO0O0OOO00OOOO000 ,'--upgrade'])#line:246
        text .insert (END ,"\n您可以开展工作。")#line:247
        return "...更新成功。"#line:248
def TOOLS_ror_mode1 (OOOO0000OO00OOO00 ,O000O0OOOOO0OOO00 ):#line:265
	O0000OOO000O000O0 =[]#line:266
	for OO0O0O00O0000000O in ("事件发生年份","性别","年龄段","报告类型-严重程度","停药减药后反应是否减轻或消失","再次使用可疑药是否出现同样反应","对原患疾病影响","不良反应结果","关联性评价"):#line:267
		OOOO0000OO00OOO00 [OO0O0O00O0000000O ]=OOOO0000OO00OOO00 [OO0O0O00O0000000O ].astype (str )#line:268
		OOOO0000OO00OOO00 [OO0O0O00O0000000O ]=OOOO0000OO00OOO00 [OO0O0O00O0000000O ].fillna ("不详")#line:269
		O0O00000O0O0OO0OO =0 #line:271
		for O00OOO0OOOOOOO0OO in OOOO0000OO00OOO00 [O000O0OOOOO0OOO00 ].drop_duplicates ():#line:272
			O0O00000O0O0OO0OO =O0O00000O0O0OO0OO +1 #line:273
			O0000O00000OO0000 =OOOO0000OO00OOO00 [(OOOO0000OO00OOO00 [O000O0OOOOO0OOO00 ]==O00OOO0OOOOOOO0OO )].copy ()#line:274
			O0O0OOOOO0O00O0O0 =str (O00OOO0OOOOOOO0OO )+"计数"#line:276
			O0O00OO00O0000000 =str (O00OOO0OOOOOOO0OO )+"构成比(%)"#line:277
			O0000000O0OOO0O00 =O0000O00000OO0000 .groupby (OO0O0O00O0000000O ).agg (计数 =("报告编码","nunique")).sort_values (by =OO0O0O00O0000000O ,ascending =[True ],na_position ="last").reset_index ()#line:278
			O0000000O0OOO0O00 [O0O00OO00O0000000 ]=round (100 *O0000000O0OOO0O00 ["计数"]/O0000000O0OOO0O00 ["计数"].sum (),2 )#line:279
			O0000000O0OOO0O00 =O0000000O0OOO0O00 .rename (columns ={OO0O0O00O0000000O :"项目"})#line:280
			O0000000O0OOO0O00 =O0000000O0OOO0O00 .rename (columns ={"计数":O0O0OOOOO0O00O0O0 })#line:281
			if O0O00000O0O0OO0OO >1 :#line:282
				O00O0O00000000O0O =pd .merge (O00O0O00000000O0O ,O0000000O0OOO0O00 ,on =["项目"],how ="outer")#line:283
			else :#line:284
				O00O0O00000000O0O =O0000000O0OOO0O00 .copy ()#line:285
		O00O0O00000000O0O ["类别"]=OO0O0O00O0000000O #line:287
		O0000OOO000O000O0 .append (O00O0O00000000O0O .copy ().reset_index (drop =True ))#line:288
	O0OOO00O0OOOO00OO =pd .concat (O0000OOO000O000O0 ,ignore_index =True ).fillna (0 )#line:291
	O0OOO00O0OOOO00OO ["报表类型"]="KETI"#line:292
	TABLE_tree_Level_2 (O0OOO00O0OOOO00OO ,1 ,O0OOO00O0OOOO00OO )#line:293
def TOOLS_ror_mode2 (OO0O0OOO00OO0O0O0 ,OOO00OO000OOO000O ):#line:295
	O0000OO0OOOOOOO0O =Countall (OO0O0OOO00OO0O0O0 ).df_ror (["产品类别","产品名称"]).reset_index ()#line:296
	O0000OO0OOOOOOO0O ["四分表"]=O0000OO0OOOOOOO0O ["四分表"].str .replace ("(","")#line:297
	O0000OO0OOOOOOO0O ["四分表"]=O0000OO0OOOOOOO0O ["四分表"].str .replace (")","")#line:298
	O0000OO0OOOOOOO0O ["ROR信号（0-否，1-是）"]=0 #line:299
	O0000OO0OOOOOOO0O ["PRR信号（0-否，1-是）"]=0 #line:300
	for OOOO0OO000OOO0OOO ,OO0OOO000OO0O0O0O in O0000OO0OOOOOOO0O .iterrows ():#line:301
		OO000O00O00O00000 =tuple (OO0OOO000OO0O0O0O ["四分表"].split (","))#line:302
		O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"a"]=int (OO000O00O00O00000 [0 ])#line:303
		O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"b"]=int (OO000O00O00O00000 [1 ])#line:304
		O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"c"]=int (OO000O00O00O00000 [2 ])#line:305
		O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"d"]=int (OO000O00O00O00000 [3 ])#line:306
		if int (OO000O00O00O00000 [1 ])*int (OO000O00O00O00000 [2 ])*int (OO000O00O00O00000 [3 ])*int (OO000O00O00O00000 [0 ])==0 :#line:307
			O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"分母核验"]=1 #line:308
		if OO0OOO000OO0O0O0O ['ROR值的95%CI下限']>1 and OO0OOO000OO0O0O0O ['出现频次']>=3 :#line:309
			O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"ROR信号（0-否，1-是）"]=1 #line:310
		if OO0OOO000OO0O0O0O ['PRR值的95%CI下限']>1 and OO0OOO000OO0O0O0O ['出现频次']>=3 :#line:311
			O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"PRR信号（0-否，1-是）"]=1 #line:312
		O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"事件分类"]=str (TOOLS_get_list (O0000OO0OOOOOOO0O .loc [OOOO0OO000OOO0OOO ,"特定关键字"])[0 ])#line:313
	O0000OO0OOOOOOO0O =pd .pivot_table (O0000OO0OOOOOOO0O ,values =["出现频次",'ROR值',"ROR值的95%CI下限","ROR信号（0-否，1-是）",'PRR值',"PRR值的95%CI下限","PRR信号（0-否，1-是）","a","b","c","d","分母核验","风险评分"],index ='事件分类',columns ="产品名称",aggfunc ='sum').reset_index ().fillna (0 )#line:315
	try :#line:318
		O00000000O00O00O0 ="配置表/0（范例）比例失衡关键字库.xls"#line:319
		if "报告类型-新的"in OO0O0OOO00OO0O0O0 .columns :#line:320
			O000OO00O000O0OOO ="药品"#line:321
		else :#line:322
			O000OO00O000O0OOO ="器械"#line:323
		OO0OO0O0OO00OO0O0 =pd .read_excel (O00000000O00O00O0 ,header =0 ,sheet_name =O000OO00O000O0OOO ).reset_index (drop =True )#line:324
	except :#line:325
		pass #line:326
	for OOOO0OO000OOO0OOO ,OO0OOO000OO0O0O0O in OO0OO0O0OO00OO0O0 .iterrows ():#line:328
		O0000OO0OOOOOOO0O .loc [O0000OO0OOOOOOO0O ["事件分类"].str .contains (OO0OOO000OO0O0O0O ["值"],na =False ),"器官系统损害"]=TOOLS_get_list (OO0OOO000OO0O0O0O ["值"])[0 ]#line:329
	try :#line:332
		OOO00O00O000O000O ="配置表/"+"0（范例）标准术语"+".xlsx"#line:333
		try :#line:334
			OO0OOOO0O0OOOO000 =pd .read_excel (OOO00O00O000O000O ,sheet_name ="onept",header =0 ,index_col =0 ).reset_index ()#line:335
		except :#line:336
			showinfo (title ="错误信息",message ="标准术语集无法加载。")#line:337
		try :#line:339
			OO0OOOOOOOO0000O0 =pd .read_excel (OOO00O00O000O000O ,sheet_name ="my",header =0 ,index_col =0 ).reset_index ()#line:340
		except :#line:341
			showinfo (title ="错误信息",message ="自定义术语集无法加载。")#line:342
		OO0OOOO0O0OOOO000 =pd .concat ([OO0OOOOOOOO0000O0 ,OO0OOOO0O0OOOO000 ],ignore_index =True ).drop_duplicates ("code")#line:344
		OO0OOOO0O0OOOO000 ["code"]=OO0OOOO0O0OOOO000 ["code"].astype (str )#line:345
		O0000OO0OOOOOOO0O ["事件分类"]=O0000OO0OOOOOOO0O ["事件分类"].astype (str )#line:346
		OO0OOOO0O0OOOO000 ["事件分类"]=OO0OOOO0O0OOOO000 ["PT"]#line:347
		O0O000O0OO00OOO00 =pd .merge (O0000OO0OOOOOOO0O ,OO0OOOO0O0OOOO000 ,on =["事件分类"],how ="left")#line:348
		for OOOO0OO000OOO0OOO ,OO0OOO000OO0O0O0O in O0O000O0OO00OOO00 .iterrows ():#line:349
			O0000OO0OOOOOOO0O .loc [O0000OO0OOOOOOO0O ["事件分类"]==OO0OOO000OO0O0O0O ["事件分类"],"Chinese"]=OO0OOO000OO0O0O0O ["Chinese"]#line:350
			O0000OO0OOOOOOO0O .loc [O0000OO0OOOOOOO0O ["事件分类"]==OO0OOO000OO0O0O0O ["事件分类"],"PT"]=OO0OOO000OO0O0O0O ["PT"]#line:351
			O0000OO0OOOOOOO0O .loc [O0000OO0OOOOOOO0O ["事件分类"]==OO0OOO000OO0O0O0O ["事件分类"],"HLT"]=OO0OOO000OO0O0O0O ["HLT"]#line:352
			O0000OO0OOOOOOO0O .loc [O0000OO0OOOOOOO0O ["事件分类"]==OO0OOO000OO0O0O0O ["事件分类"],"HLGT"]=OO0OOO000OO0O0O0O ["HLGT"]#line:353
			O0000OO0OOOOOOO0O .loc [O0000OO0OOOOOOO0O ["事件分类"]==OO0OOO000OO0O0O0O ["事件分类"],"SOC"]=OO0OOO000OO0O0O0O ["SOC"]#line:354
	except :#line:355
		pass #line:356
	data ["报表类型"]="KETI"#line:359
	TABLE_tree_Level_2 (O0000OO0OOOOOOO0O ,1 ,O0000OO0OOOOOOO0O )#line:360
def TOOLS_ror_mode3 (O0000O0OOOO00O00O ,O00O0OOO00O00OOOO ):#line:362
	O0000O0OOOO00O00O ["css"]=0 #line:363
	TOOLS_ror_mode2 (O0000O0OOOO00O00O ,O00O0OOO00O00OOOO )#line:364
def STAT_pinzhong (O0O0000O0OO00000O ,O00000000OO0OOOO0 ,OO0O0000O00O00000 ):#line:366
	O0000OOO0000O000O =[O00000000OO0OOOO0 ]#line:368
	if OO0O0000O00O00000 ==-1 :#line:369
		OO00O0OO0OOO00OOO =O0O0000O0OO00000O .drop_duplicates ("报告编码").copy ()#line:370
		O0OOOOO000OO00OOO =OO00O0OO0OOO00OOO .groupby ([O00000000OO0OOOO0 ]).agg (计数 =("报告编码","nunique")).sort_values (by =O00000000OO0OOOO0 ,ascending =[True ],na_position ="last").reset_index ()#line:371
		O0OOOOO000OO00OOO ["构成比(%)"]=round (100 *O0OOOOO000OO00OOO ["计数"]/O0OOOOO000OO00OOO ["计数"].sum (),2 )#line:372
		O0OOOOO000OO00OOO [O00000000OO0OOOO0 ]=O0OOOOO000OO00OOO [O00000000OO0OOOO0 ].astype (str )#line:373
		O0OOOOO000OO00OOO ["报表类型"]="dfx_deepview"+"_"+str (O0000OOO0000O000O )#line:374
		TABLE_tree_Level_2 (O0OOOOO000OO00OOO ,1 ,OO00O0OO0OOO00OOO )#line:375
	if OO0O0000O00O00000 ==1 :#line:377
		OO00O0OO0OOO00OOO =O0O0000O0OO00000O .copy ()#line:378
		O0OOOOO000OO00OOO =OO00O0OO0OOO00OOO .groupby ([O00000000OO0OOOO0 ]).agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:379
		O0OOOOO000OO00OOO ["构成比(%)"]=round (100 *O0OOOOO000OO00OOO ["计数"]/O0OOOOO000OO00OOO ["计数"].sum (),2 )#line:380
		O0OOOOO000OO00OOO ["报表类型"]="dfx_deepview"+"_"+str (O0000OOO0000O000O )#line:381
		TABLE_tree_Level_2 (O0OOOOO000OO00OOO ,1 ,OO00O0OO0OOO00OOO )#line:382
	if OO0O0000O00O00000 ==4 :#line:384
		OO00O0OO0OOO00OOO =O0O0000O0OO00000O .copy ()#line:385
		OO00O0OO0OOO00OOO .loc [OO00O0OO0OOO00OOO ["不良反应结果"].str .contains ("好转",na =False ),"不良反应结果2"]="好转"#line:386
		OO00O0OO0OOO00OOO .loc [OO00O0OO0OOO00OOO ["不良反应结果"].str .contains ("痊愈",na =False ),"不良反应结果2"]="痊愈"#line:387
		OO00O0OO0OOO00OOO .loc [OO00O0OO0OOO00OOO ["不良反应结果"].str .contains ("无进展",na =False ),"不良反应结果2"]="无进展"#line:388
		OO00O0OO0OOO00OOO .loc [OO00O0OO0OOO00OOO ["不良反应结果"].str .contains ("死亡",na =False ),"不良反应结果2"]="死亡"#line:389
		OO00O0OO0OOO00OOO .loc [OO00O0OO0OOO00OOO ["不良反应结果"].str .contains ("不详",na =False ),"不良反应结果2"]="不详"#line:390
		OO00O0OO0OOO00OOO .loc [OO00O0OO0OOO00OOO ["不良反应结果"].str .contains ("未好转",na =False ),"不良反应结果2"]="未好转"#line:391
		O0OOOOO000OO00OOO =OO00O0OO0OOO00OOO .groupby (["不良反应结果2"]).agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:392
		O0OOOOO000OO00OOO ["构成比(%)"]=round (100 *O0OOOOO000OO00OOO ["计数"]/O0OOOOO000OO00OOO ["计数"].sum (),2 )#line:393
		O0OOOOO000OO00OOO ["报表类型"]="dfx_deepview"+"_"+str (["不良反应结果2"])#line:394
		TABLE_tree_Level_2 (O0OOOOO000OO00OOO ,1 ,OO00O0OO0OOO00OOO )#line:395
	if OO0O0000O00O00000 ==5 :#line:397
		OO00O0OO0OOO00OOO =O0O0000O0OO00000O .copy ()#line:398
		OO00O0OO0OOO00OOO ["关联性评价汇总"]="("+OO00O0OO0OOO00OOO ["评价状态"].astype (str )+"("+OO00O0OO0OOO00OOO ["县评价"].astype (str )+"("+OO00O0OO0OOO00OOO ["市评价"].astype (str )+"("+OO00O0OO0OOO00OOO ["省评价"].astype (str )+"("+OO00O0OO0OOO00OOO ["国家评价"].astype (str )+")"#line:400
		OO00O0OO0OOO00OOO ["关联性评价汇总"]=OO00O0OO0OOO00OOO ["关联性评价汇总"].str .replace ("(nan","",regex =False )#line:401
		OO00O0OO0OOO00OOO ["关联性评价汇总"]=OO00O0OO0OOO00OOO ["关联性评价汇总"].str .replace ("nan)","",regex =False )#line:402
		OO00O0OO0OOO00OOO ["关联性评价汇总"]=OO00O0OO0OOO00OOO ["关联性评价汇总"].str .replace ("nan","",regex =False )#line:403
		OO00O0OO0OOO00OOO ['最终的关联性评价']=OO00O0OO0OOO00OOO ["关联性评价汇总"].str .extract ('.*\((.*)\).*',expand =False )#line:404
		O0OOOOO000OO00OOO =OO00O0OO0OOO00OOO .groupby ('最终的关联性评价').agg (计数 =("报告编码","nunique")).sort_values (by ="计数",ascending =[False ],na_position ="last").reset_index ()#line:405
		O0OOOOO000OO00OOO ["构成比(%)"]=round (100 *O0OOOOO000OO00OOO ["计数"]/O0OOOOO000OO00OOO ["计数"].sum (),2 )#line:406
		O0OOOOO000OO00OOO ["报表类型"]="dfx_deepview"+"_"+str (['最终的关联性评价'])#line:407
		TABLE_tree_Level_2 (O0OOOOO000OO00OOO ,1 ,OO00O0OO0OOO00OOO )#line:408
	if OO0O0000O00O00000 ==0 :#line:410
		O0O0000O0OO00000O [O00000000OO0OOOO0 ]=O0O0000O0OO00000O [O00000000OO0OOOO0 ].fillna ("未填写")#line:411
		O0O0000O0OO00000O [O00000000OO0OOOO0 ]=O0O0000O0OO00000O [O00000000OO0OOOO0 ].str .replace ("*","",regex =False )#line:412
		OO0O0000OOOOOO0OO ="use("+str (O00000000OO0OOOO0 )+").file"#line:413
		OO000000O000O000O =str (Counter (TOOLS_get_list0 (OO0O0000OOOOOO0OO ,O0O0000O0OO00000O ,1000 ))).replace ("Counter({","{")#line:414
		OO000000O000O000O =OO000000O000O000O .replace ("})","}")#line:415
		OO000000O000O000O =ast .literal_eval (OO000000O000O000O )#line:416
		O0OOOOO000OO00OOO =pd .DataFrame .from_dict (OO000000O000O000O ,orient ="index",columns =["计数"]).reset_index ()#line:417
		O0OOOOO000OO00OOO ["构成比(%)"]=round (100 *O0OOOOO000OO00OOO ["计数"]/O0OOOOO000OO00OOO ["计数"].sum (),2 )#line:419
		O0OOOOO000OO00OOO ["报表类型"]="dfx_deepvie2"+"_"+str (O0000OOO0000O000O )#line:420
		TABLE_tree_Level_2 (O0OOOOO000OO00OOO ,1 ,O0O0000O0OO00000O )#line:421
	if OO0O0000O00O00000 ==2 or OO0O0000O00O00000 ==3 :#line:425
		O0O0000O0OO00000O [O00000000OO0OOOO0 ]=O0O0000O0OO00000O [O00000000OO0OOOO0 ].astype (str )#line:426
		O0O0000O0OO00000O [O00000000OO0OOOO0 ]=O0O0000O0OO00000O [O00000000OO0OOOO0 ].fillna ("未填写")#line:427
		OO0O0000OOOOOO0OO ="use("+str (O00000000OO0OOOO0 )+").file"#line:429
		OO000000O000O000O =str (Counter (TOOLS_get_list0 (OO0O0000OOOOOO0OO ,O0O0000O0OO00000O ,1000 ))).replace ("Counter({","{")#line:430
		OO000000O000O000O =OO000000O000O000O .replace ("})","}")#line:431
		OO000000O000O000O =ast .literal_eval (OO000000O000O000O )#line:432
		O0OOOOO000OO00OOO =pd .DataFrame .from_dict (OO000000O000O000O ,orient ="index",columns =["计数"]).reset_index ()#line:433
		print ("正在统计，请稍后...")#line:434
		O00OOOOO000OOO000 ="配置表/"+"0（范例）标准术语"+".xlsx"#line:435
		try :#line:436
			O0OO0OO00O0OO000O =pd .read_excel (O00OOOOO000OOO000 ,sheet_name ="simple",header =0 ,index_col =0 ).reset_index ()#line:437
		except :#line:438
			showinfo (title ="错误信息",message ="标准术语集无法加载。")#line:439
			return 0 #line:440
		try :#line:441
			OOO0OOO0OO00O0O00 =pd .read_excel (O00OOOOO000OOO000 ,sheet_name ="my",header =0 ,index_col =0 ).reset_index ()#line:442
		except :#line:443
			showinfo (title ="错误信息",message ="自定义术语集无法加载。")#line:444
			return 0 #line:445
		O0OO0OO00O0OO000O =pd .concat ([OOO0OOO0OO00O0O00 ,O0OO0OO00O0OO000O ],ignore_index =True ).drop_duplicates ("code")#line:446
		O0OO0OO00O0OO000O ["code"]=O0OO0OO00O0OO000O ["code"].astype (str )#line:447
		O0OOOOO000OO00OOO ["index"]=O0OOOOO000OO00OOO ["index"].astype (str )#line:448
		O0OOOOO000OO00OOO =O0OOOOO000OO00OOO .rename (columns ={"index":"code"})#line:450
		O0OOOOO000OO00OOO =pd .merge (O0OOOOO000OO00OOO ,O0OO0OO00O0OO000O ,on =["code"],how ="left")#line:451
		O0OOOOO000OO00OOO ["code构成比(%)"]=round (100 *O0OOOOO000OO00OOO ["计数"]/O0OOOOO000OO00OOO ["计数"].sum (),2 )#line:452
		OO0O00O0OO0O0OOO0 =O0OOOOO000OO00OOO .groupby ("SOC").agg (SOC计数 =("计数","sum")).sort_values (by ="SOC计数",ascending =[False ],na_position ="last").reset_index ()#line:453
		OO0O00O0OO0O0OOO0 ["soc构成比(%)"]=round (100 *OO0O00O0OO0O0OOO0 ["SOC计数"]/OO0O00O0OO0O0OOO0 ["SOC计数"].sum (),2 )#line:454
		OO0O00O0OO0O0OOO0 ["SOC计数"]=OO0O00O0OO0O0OOO0 ["SOC计数"].astype (int )#line:455
		O0OOOOO000OO00OOO =pd .merge (O0OOOOO000OO00OOO ,OO0O00O0OO0O0OOO0 ,on =["SOC"],how ="left")#line:456
		if OO0O0000O00O00000 ==3 :#line:458
			OO0O00O0OO0O0OOO0 ["具体名称"]=""#line:459
			for O00O0O00O0O000O00 ,O00OO0000O00O00O0 in OO0O00O0OO0O0OOO0 .iterrows ():#line:460
				O00OOOO000O00O000 =""#line:461
				O00O00OO00O00OO00 =O0OOOOO000OO00OOO .loc [O0OOOOO000OO00OOO ["SOC"].str .contains (O00OO0000O00O00O0 ["SOC"],na =False )].copy ()#line:462
				for OO00OO00OO0OOO0O0 ,O000O0OO00OOOOO00 in O00O00OO00O00OO00 .iterrows ():#line:463
					O00OOOO000O00O000 =O00OOOO000O00O000 +str (O000O0OO00OOOOO00 ["PT"])+"("+str (O000O0OO00OOOOO00 ["计数"])+")、"#line:464
				OO0O00O0OO0O0OOO0 .loc [O00O0O00O0O000O00 ,"具体名称"]=O00OOOO000O00O000 #line:465
			OO0O00O0OO0O0OOO0 ["报表类型"]="dfx_deepvie2"+"_"+str (["SOC"])#line:466
			TABLE_tree_Level_2 (OO0O00O0OO0O0OOO0 ,1 ,O0OOOOO000OO00OOO )#line:467
		if OO0O0000O00O00000 ==2 :#line:469
			O0OOOOO000OO00OOO ["报表类型"]="dfx_deepvie2"+"_"+str (O0000OOO0000O000O )#line:470
			TABLE_tree_Level_2 (O0OOOOO000OO00OOO ,1 ,O0O0000O0OO00000O )#line:471
	pass #line:474
def DRAW_pre (OOOO0OO00O0O000O0 ):#line:476
	""#line:477
	O0OO0000OOO0O00OO =list (OOOO0OO00O0O000O0 ["报表类型"])[0 ].replace ("1","")#line:485
	if "dfx_org监测机构"in O0OO0000OOO0O00OO :#line:487
		OOOO0OO00O0O000O0 =OOOO0OO00O0O000O0 [:-1 ]#line:488
		DRAW_make_one (OOOO0OO00O0O000O0 ,"报告图","监测机构","报告数量","超级托帕斯图(严重伤害数)")#line:489
	elif "dfx_org市级监测机构"in O0OO0000OOO0O00OO :#line:490
		OOOO0OO00O0O000O0 =OOOO0OO00O0O000O0 [:-1 ]#line:491
		DRAW_make_one (OOOO0OO00O0O000O0 ,"报告图","市级监测机构","报告数量","超级托帕斯图(严重伤害数)")#line:492
	elif "dfx_user"in O0OO0000OOO0O00OO :#line:493
		OOOO0OO00O0O000O0 =OOOO0OO00O0O000O0 [:-1 ]#line:494
		DRAW_make_one (OOOO0OO00O0O000O0 ,"报告单位图","单位名称","报告数量","超级托帕斯图(严重伤害数)")#line:495
	elif "dfx_deepview"in O0OO0000OOO0O00OO :#line:498
		DRAW_make_one (OOOO0OO00O0O000O0 ,"柱状图",OOOO0OO00O0O000O0 .columns [0 ],"计数","柱状图")#line:499
	elif "dfx_chiyouren"in O0OO0000OOO0O00OO :#line:501
		OOOO0OO00O0O000O0 =OOOO0OO00O0O000O0 [:-1 ]#line:502
		DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及持有人图","上市许可持有人名称","总报告数","超级托帕斯图(总待评价数量)")#line:503
	elif "dfx_zhenghao"in O0OO0000OOO0O00OO :#line:505
		OOOO0OO00O0O000O0 ["产品"]=OOOO0OO00O0O000O0 ["产品名称"]+"("+OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"]+")"#line:506
		DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及产品图","产品","证号计数","超级托帕斯图(严重伤害数)")#line:507
	elif "dfx_pihao"in O0OO0000OOO0O00OO :#line:509
		if len (OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:510
			OOOO0OO00O0O000O0 ["产品"]=OOOO0OO00O0O000O0 ["产品名称"]+"("+OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"]+"--"+OOOO0OO00O0O000O0 ["产品批号"]+")"#line:511
			DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及批号图","产品","批号计数","超级托帕斯图(严重伤害数)")#line:512
		else :#line:513
			DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及批号图","产品批号","批号计数","超级托帕斯图(严重伤害数)")#line:514
	elif "dfx_xinghao"in O0OO0000OOO0O00OO :#line:516
		if len (OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:517
			OOOO0OO00O0O000O0 ["产品"]=OOOO0OO00O0O000O0 ["产品名称"]+"("+OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"]+"--"+OOOO0OO00O0O000O0 ["型号"]+")"#line:518
			DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及型号图","产品","型号计数","超级托帕斯图(严重伤害数)")#line:519
		else :#line:520
			DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及型号图","型号","型号计数","超级托帕斯图(严重伤害数)")#line:521
	elif "dfx_guige"in O0OO0000OOO0O00OO :#line:523
		if len (OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"].drop_duplicates ())>1 :#line:524
			OOOO0OO00O0O000O0 ["产品"]=OOOO0OO00O0O000O0 ["产品名称"]+"("+OOOO0OO00O0O000O0 ["注册证编号/曾用注册证编号"]+"--"+OOOO0OO00O0O000O0 ["规格"]+")"#line:525
			DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及规格图","产品","规格计数","超级托帕斯图(严重伤害数)")#line:526
		else :#line:527
			DRAW_make_one (OOOO0OO00O0O000O0 ,"涉及规格图","规格","规格计数","超级托帕斯图(严重伤害数)")#line:528
	elif "PSUR"in O0OO0000OOO0O00OO :#line:530
		DRAW_make_mutibar (OOOO0OO00O0O000O0 ,"总数量","严重","事件分类","总数量","严重","表现分类统计图")#line:531
	elif "keyword_findrisk"in O0OO0000OOO0O00OO :#line:533
		OOO0O00O00O00O00O =OOOO0OO00O0O000O0 .columns .to_list ()#line:535
		O00O0OOOO00O0O000 =OOO0O00O00O00O00O [OOO0O00O00O00O00O .index ("关键字")+1 ]#line:536
		O000OOO000O000OOO =pd .pivot_table (OOOO0OO00O0O000O0 ,index =O00O0OOOO00O0O000 ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:547
		O000OOO000O000OOO .columns =O000OOO000O000OOO .columns .droplevel (0 )#line:548
		O000OOO000O000OOO =O000OOO000O000OOO [:-1 ].reset_index ()#line:549
		O000OOO000O000OOO =pd .merge (O000OOO000O000OOO ,OOOO0OO00O0O000O0 [[O00O0OOOO00O0O000 ,"该元素总数量"]].drop_duplicates (O00O0OOOO00O0O000 ),on =[O00O0OOOO00O0O000 ],how ="left")#line:551
		del O000OOO000O000OOO ["All"]#line:553
		DRAW_make_risk_plot (O000OOO000O000OOO ,O00O0OOOO00O0O000 ,[O0O0OOO00O0OO0OOO for O0O0OOO00O0OO0OOO in O000OOO000O000OOO .columns if O0O0OOO00O0OO0OOO !=O00O0OOOO00O0O000 ],"关键字趋势图",100 )#line:558
def DRAW_make_risk_plot (OOOOO00OOO0O000OO ,OOOOO0OOO0O0OO00O ,O0OO0O0OOOO00O00O ,OO000O0O0O00000O0 ,O0000O0000O00O0O0 ):#line:563
    ""#line:564
    OO0OOO0OOOOOO0O0O =Toplevel ()#line:567
    OO0OOO0OOOOOO0O0O .title (OO000O0O0O00000O0 )#line:568
    OO00OO0OO0OOOOOO0 =ttk .Frame (OO0OOO0OOOOOO0O0O ,height =20 )#line:569
    OO00OO0OO0OOOOOO0 .pack (side =TOP )#line:570
    OO0000O0O00O0OOOO =Figure (figsize =(12 ,6 ),dpi =100 )#line:572
    OOO000O0OOO000OO0 =FigureCanvasTkAgg (OO0000O0O00O0OOOO ,master =OO0OOO0OOOOOO0O0O )#line:573
    OOO000O0OOO000OO0 .draw ()#line:574
    OOO000O0OOO000OO0 .get_tk_widget ().pack (expand =1 )#line:575
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:577
    plt .rcParams ['axes.unicode_minus']=False #line:578
    O0O0O0000OO0OOO0O =NavigationToolbar2Tk (OOO000O0OOO000OO0 ,OO0OOO0OOOOOO0O0O )#line:580
    O0O0O0000OO0OOO0O .update ()#line:581
    OOO000O0OOO000OO0 .get_tk_widget ().pack ()#line:582
    OOOO0O0OOO0OO000O =OO0000O0O00O0OOOO .add_subplot (111 )#line:584
    OOOO0O0OOO0OO000O .set_title (OO000O0O0O00000O0 )#line:586
    OO000000O0O0O0OO0 =OOOOO00OOO0O000OO [OOOOO0OOO0O0OO00O ]#line:587
    if O0000O0000O00O0O0 !=999 :#line:590
        OOOO0O0OOO0OO000O .set_xticklabels (OO000000O0O0O0OO0 ,rotation =-90 ,fontsize =8 )#line:591
    O0000O0OOO0OO00O0 =range (0 ,len (OO000000O0O0O0OO0 ),1 )#line:594
    try :#line:599
        OOOO0O0OOO0OO000O .bar (OO000000O0O0O0OO0 ,OOOOO00OOO0O000OO ["报告总数"],color ='skyblue',label ="报告总数")#line:600
        OOOO0O0OOO0OO000O .bar (OO000000O0O0O0OO0 ,height =OOOOO00OOO0O000OO ["严重伤害数"],color ="orangered",label ="严重伤害数")#line:601
    except :#line:602
        pass #line:603
    for OOO0O0OOOOO00OOOO in O0OO0O0OOOO00O00O :#line:606
        O0OO0O00O00OOO00O =OOOOO00OOO0O000OO [OOO0O0OOOOO00OOOO ].astype (float )#line:607
        if OOO0O0OOOOO00OOOO =="关注区域":#line:609
            OOOO0O0OOO0OO000O .plot (list (OO000000O0O0O0OO0 ),list (O0OO0O00O00OOO00O ),label =str (OOO0O0OOOOO00OOOO ),color ="red")#line:610
        else :#line:611
            OOOO0O0OOO0OO000O .plot (list (OO000000O0O0O0OO0 ),list (O0OO0O00O00OOO00O ),label =str (OOO0O0OOOOO00OOOO ))#line:612
        if O0000O0000O00O0O0 ==100 :#line:615
            for O0O00OO0OOO000OOO ,O000O0O0O00000OOO in zip (OO000000O0O0O0OO0 ,O0OO0O00O00OOO00O ):#line:616
                if O000O0O0O00000OOO ==max (O0OO0O00O00OOO00O )and O000O0O0O00000OOO >=3 :#line:617
                     OOOO0O0OOO0OO000O .text (O0O00OO0OOO000OOO ,O000O0O0O00000OOO ,(str (OOO0O0OOOOO00OOOO )+":"+str (int (O000O0O0O00000OOO ))),color ='black',size =8 )#line:618
    if len (O0OO0O0OOOO00O00O )==1 :#line:628
        O0O00OOO000O0OO0O =OOOOO00OOO0O000OO [O0OO0O0OOOO00O00O ].astype (float ).values #line:629
        OOOOOOO000000O0O0 =O0O00OOO000O0OO0O .mean ()#line:630
        OOOOOO000000O0OOO =O0O00OOO000O0OO0O .std ()#line:631
        O0OO0O0OOOOO0O0OO =OOOOOOO000000O0O0 +3 *OOOOOO000000O0OOO #line:632
        O00OOOO0OO00O0O0O =OOOOOO000000O0OOO -3 *OOOOOO000000O0OOO #line:633
        OOOO0O0OOO0OO000O .axhline (OOOOOOO000000O0O0 ,color ='r',linestyle ='--',label ='Mean')#line:635
        OOOO0O0OOO0OO000O .axhline (O0OO0O0OOOOO0O0OO ,color ='g',linestyle ='--',label ='UCL(μ+3σ)')#line:636
        OOOO0O0OOO0OO000O .axhline (O00OOOO0OO00O0O0O ,color ='g',linestyle ='--',label ='LCL(μ-3σ)')#line:637
    OOOO0O0OOO0OO000O .set_title ("曲线图")#line:641
    OOOO0O0OOO0OO000O .set_xlabel ("项")#line:642
    OO0000O0O00O0OOOO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:643
    OO0OO000O00OOOOOO =OOOO0O0OOO0OO000O .get_position ()#line:644
    OOOO0O0OOO0OO000O .set_position ([OO0OO000O00OOOOOO .x0 ,OO0OO000O00OOOOOO .y0 ,OO0OO000O00OOOOOO .width *0.7 ,OO0OO000O00OOOOOO .height ])#line:645
    OOOO0O0OOO0OO000O .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:646
    O00000OOOOOO000O0 =StringVar ()#line:670
    O0OO000O00000O00O =ttk .Combobox (OO00OO0OO0OOOOOO0 ,width =15 ,textvariable =O00000OOOOOO000O0 ,state ='readonly')#line:671
    O0OO000O00000O00O ['values']=O0OO0O0OOOO00O00O #line:672
    O0OO000O00000O00O .pack (side =LEFT )#line:673
    O0OO000O00000O00O .current (0 )#line:674
    OOOOO0O0O0O0OO000 =Button (OO00OO0OO0OOOOOO0 ,text ="控制图（单项）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (OOOOO00OOO0O000OO ,OOOOO0OOO0O0OO00O ,[OOOOO0OOOOOO00OOO for OOOOO0OOOOOO00OOO in O0OO0O0OOOO00O00O if O00000OOOOOO000O0 .get ()in OOOOO0OOOOOO00OOO ],OO000O0O0O00000O0 ,O0000O0000O00O0O0 ))#line:682
    OOOOO0O0O0O0OO000 .pack (side =LEFT ,anchor ="ne")#line:683
    O0000O0000OOO0000 =Button (OO00OO0OO0OOOOOO0 ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_risk_plot (OOOOO00OOO0O000OO ,OOOOO0OOO0O0OO00O ,O0OO0O0OOOO00O00O ,OO000O0O0O00000O0 ,0 ))#line:691
    O0000O0000OOO0000 .pack (side =LEFT ,anchor ="ne")#line:692
    OOO000O0OOO000OO0 .draw ()#line:694
def DRAW_make_one (O0OOOO0O0OO00OO00 ,O0OO0OOO000O0OO0O ,OOO0O000OO00000O0 ,OOOO0OO0O000O0000 ,OO0000000O0OO0OO0 ):#line:697
    ""#line:698
    warnings .filterwarnings ("ignore")#line:699
    O00O000O0OOOOO0OO =Toplevel ()#line:700
    O00O000O0OOOOO0OO .title (O0OO0OOO000O0OO0O )#line:701
    OO00OOOO0O0OO00O0 =ttk .Frame (O00O000O0OOOOO0OO ,height =20 )#line:702
    OO00OOOO0O0OO00O0 .pack (side =TOP )#line:703
    OO00OO00OOO0O0OO0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:705
    O0OOOOOO0O0O0O000 =FigureCanvasTkAgg (OO00OO00OOO0O0OO0 ,master =O00O000O0OOOOO0OO )#line:706
    O0OOOOOO0O0O0O000 .draw ()#line:707
    O0OOOOOO0O0O0O000 .get_tk_widget ().pack (expand =1 )#line:708
    OOO0O0OO0OOO00000 =OO00OO00OOO0O0OO0 .add_subplot (111 )#line:709
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:711
    plt .rcParams ['axes.unicode_minus']=False #line:712
    O000OOOOOOOOOO0OO =NavigationToolbar2Tk (O0OOOOOO0O0O0O000 ,O00O000O0OOOOO0OO )#line:714
    O000OOOOOOOOOO0OO .update ()#line:715
    O0OOOOOO0O0O0O000 .get_tk_widget ().pack ()#line:717
    try :#line:720
        OO000O00O0O0OO000 =O0OOOO0O0OO00OO00 .columns #line:721
        O0OOOO0O0OO00OO00 =O0OOOO0O0OO00OO00 .sort_values (by =OOOO0OO0O000O0000 ,ascending =[False ],na_position ="last")#line:722
    except :#line:723
        OO00OO0OOO0OO0OOO =eval (O0OOOO0O0OO00OO00 )#line:724
        OO00OO0OOO0OO0OOO =pd .DataFrame .from_dict (OO00OO0OOO0OO0OOO ,orient =OOO0O000OO00000O0 ,columns =[OOOO0OO0O000O0000 ]).reset_index ()#line:727
        O0OOOO0O0OO00OO00 =OO00OO0OOO0OO0OOO .sort_values (by =OOOO0OO0O000O0000 ,ascending =[False ],na_position ="last")#line:728
    if ("日期"in O0OO0OOO000O0OO0O or "时间"in O0OO0OOO000O0OO0O or "季度"in O0OO0OOO000O0OO0O )and "饼图"not in OO0000000O0OO0OO0 :#line:732
        O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ]=pd .to_datetime (O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],format ="%Y/%m/%d").dt .date #line:733
        O0OOOO0O0OO00OO00 =O0OOOO0O0OO00OO00 .sort_values (by =OOO0O000OO00000O0 ,ascending =[True ],na_position ="last")#line:734
    elif "批号"in O0OO0OOO000O0OO0O :#line:735
        O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ]=O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ].astype (str )#line:736
        O0OOOO0O0OO00OO00 =O0OOOO0O0OO00OO00 .sort_values (by =OOO0O000OO00000O0 ,ascending =[True ],na_position ="last")#line:737
        OOO0O0OO0OOO00000 .set_xticklabels (O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],rotation =-90 ,fontsize =8 )#line:738
    else :#line:739
        O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ]=O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ].astype (str )#line:740
        OOO0O0OO0OOO00000 .set_xticklabels (O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],rotation =-90 ,fontsize =8 )#line:741
    OOOOOOO000O0OOO0O =O0OOOO0O0OO00OO00 [OOOO0OO0O000O0000 ]#line:743
    O00O00O0O000O00OO =range (0 ,len (OOOOOOO000O0OOO0O ),1 )#line:744
    OOO0O0OO0OOO00000 .set_title (O0OO0OOO000O0OO0O )#line:746
    if OO0000000O0OO0OO0 =="柱状图":#line:750
        OOO0O0OO0OOO00000 .bar (x =O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],height =OOOOOOO000O0OOO0O ,width =0.2 ,color ="#87CEFA")#line:751
    elif OO0000000O0OO0OO0 =="饼图":#line:752
        OOO0O0OO0OOO00000 .pie (x =OOOOOOO000O0OOO0O ,labels =O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],autopct ="%0.2f%%")#line:753
    elif OO0000000O0OO0OO0 =="折线图":#line:754
        OOO0O0OO0OOO00000 .plot (O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],OOOOOOO000O0OOO0O ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:755
    elif "托帕斯图"in str (OO0000000O0OO0OO0 ):#line:757
        OOOOO0000OOOOO00O =O0OOOO0O0OO00OO00 [OOOO0OO0O000O0000 ].fillna (0 )#line:758
        O0O0OOO00O0OOO0O0 =OOOOO0000OOOOO00O .cumsum ()/OOOOO0000OOOOO00O .sum ()*100 #line:762
        O0OO0O00OO0O000O0 =O0O0OOO00O0OOO0O0 [O0O0OOO00O0OOO0O0 >0.8 ].index [0 ]#line:764
        O00OO0OOO0OO000O0 =OOOOO0000OOOOO00O .index .tolist ().index (O0OO0O00OO0O000O0 )#line:765
        OOO0O0OO0OOO00000 .bar (x =O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],height =OOOOO0000OOOOO00O ,color ="C0",label =OOOO0OO0O000O0000 )#line:769
        O0OO00OOO0O0O0OOO =OOO0O0OO0OOO00000 .twinx ()#line:770
        O0OO00OOO0O0O0OOO .plot (O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],O0O0OOO00O0OOO0O0 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:771
        O0OO00OOO0O0O0OOO .yaxis .set_major_formatter (PercentFormatter ())#line:772
        OOO0O0OO0OOO00000 .tick_params (axis ="y",colors ="C0")#line:777
        O0OO00OOO0O0O0OOO .tick_params (axis ="y",colors ="C1")#line:778
        if "超级托帕斯图"in str (OO0000000O0OO0OO0 ):#line:781
            OO00O00OOOOO0O0OO =re .compile (r'[(](.*?)[)]',re .S )#line:782
            O00OO0OO0OO000O00 =re .findall (OO00O00OOOOO0O0OO ,OO0000000O0OO0OO0 )[0 ]#line:783
            OOO0O0OO0OOO00000 .bar (x =O0OOOO0O0OO00OO00 [OOO0O000OO00000O0 ],height =O0OOOO0O0OO00OO00 [O00OO0OO0OO000O00 ],color ="orangered",label =O00OO0OO0OO000O00 )#line:784
    OO00OO00OOO0O0OO0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:786
    OOOO0O0000OO000O0 =OOO0O0OO0OOO00000 .get_position ()#line:787
    OOO0O0OO0OOO00000 .set_position ([OOOO0O0000OO000O0 .x0 ,OOOO0O0000OO000O0 .y0 ,OOOO0O0000OO000O0 .width *0.7 ,OOOO0O0000OO000O0 .height ])#line:788
    OOO0O0OO0OOO00000 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:789
    O0OOOOOO0O0O0O000 .draw ()#line:792
    if len (OOOOOOO000O0OOO0O )<=20 and OO0000000O0OO0OO0 !="饼图":#line:795
        for O000O000O0O000O0O ,O00O0OO0OO00O00O0 in zip (O00O00O0O000O00OO ,OOOOOOO000O0OOO0O ):#line:796
            O0O0OOO00O0OO0OO0 =str (O00O0OO0OO00O00O0 )#line:797
            OOOOOO0OOOO00O0OO =(O000O000O0O000O0O ,O00O0OO0OO00O00O0 +0.3 )#line:798
            OOO0O0OO0OOO00000 .annotate (O0O0OOO00O0OO0OO0 ,xy =OOOOOO0OOOO00O0OO ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:799
    OOOO00OO000O0O0OO =Button (OO00OOOO0O0OO00O0 ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (O0OOOO0O0OO00OO00 ),)#line:809
    OOOO00OO000O0O0OO .pack (side =RIGHT )#line:810
    OO0O00OO0O00OOOO0 =Button (OO00OOOO0O0OO00O0 ,relief =GROOVE ,text ="查看原始数据",command =lambda :TOOLS_view_dict (O0OOOO0O0OO00OO00 ,0 ))#line:814
    OO0O00OO0O00OOOO0 .pack (side =RIGHT )#line:815
    O0OOO00O00OO00O0O =Button (OO00OOOO0O0OO00O0 ,relief =GROOVE ,text ="饼图",command =lambda :DRAW_make_one (O0OOOO0O0OO00OO00 ,O0OO0OOO000O0OO0O ,OOO0O000OO00000O0 ,OOOO0OO0O000O0000 ,"饼图"),)#line:823
    O0OOO00O00OO00O0O .pack (side =LEFT )#line:824
    O0OOO00O00OO00O0O =Button (OO00OOOO0O0OO00O0 ,relief =GROOVE ,text ="柱状图",command =lambda :DRAW_make_one (O0OOOO0O0OO00OO00 ,O0OO0OOO000O0OO0O ,OOO0O000OO00000O0 ,OOOO0OO0O000O0000 ,"柱状图"),)#line:831
    O0OOO00O00OO00O0O .pack (side =LEFT )#line:832
    O0OOO00O00OO00O0O =Button (OO00OOOO0O0OO00O0 ,relief =GROOVE ,text ="折线图",command =lambda :DRAW_make_one (O0OOOO0O0OO00OO00 ,O0OO0OOO000O0OO0O ,OOO0O000OO00000O0 ,OOOO0OO0O000O0000 ,"折线图"),)#line:838
    O0OOO00O00OO00O0O .pack (side =LEFT )#line:839
    O0OOO00O00OO00O0O =Button (OO00OOOO0O0OO00O0 ,relief =GROOVE ,text ="托帕斯图",command =lambda :DRAW_make_one (O0OOOO0O0OO00OO00 ,O0OO0OOO000O0OO0O ,OOO0O000OO00000O0 ,OOOO0OO0O000O0000 ,"托帕斯图"),)#line:846
    O0OOO00O00OO00O0O .pack (side =LEFT )#line:847
def DRAW_make_mutibar (OO0000O0O0O0OOOO0 ,O000O00O00O0O0OOO ,OOO0O00OO000OO00O ,OOOO00OOOO0OOO000 ,O0O000O00OOOOOO00 ,OO0OOO0OO0OO0OO00 ,OOO0O0OOOO0O0OO00 ):#line:848
    ""#line:849
    OOO0O00O0OO0O00O0 =Toplevel ()#line:850
    OOO0O00O0OO0O00O0 .title (OOO0O0OOOO0O0OO00 )#line:851
    O00O00OO0O0O000O0 =ttk .Frame (OOO0O00O0OO0O00O0 ,height =20 )#line:852
    O00O00OO0O0O000O0 .pack (side =TOP )#line:853
    O0OOOOO0OOO0OO0OO =0.2 #line:855
    O00OOO00OOO0O000O =Figure (figsize =(12 ,6 ),dpi =100 )#line:856
    OO0OO0O00OOOOO00O =FigureCanvasTkAgg (O00OOO00OOO0O000O ,master =OOO0O00O0OO0O00O0 )#line:857
    OO0OO0O00OOOOO00O .draw ()#line:858
    OO0OO0O00OOOOO00O .get_tk_widget ().pack (expand =1 )#line:859
    OOO0O0O0OO0O00O0O =O00OOO00OOO0O000O .add_subplot (111 )#line:860
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:862
    plt .rcParams ['axes.unicode_minus']=False #line:863
    O0O000O0O000O0O00 =NavigationToolbar2Tk (OO0OO0O00OOOOO00O ,OOO0O00O0OO0O00O0 )#line:865
    O0O000O0O000O0O00 .update ()#line:866
    OO0OO0O00OOOOO00O .get_tk_widget ().pack ()#line:868
    O000O00O00O0O0OOO =OO0000O0O0O0OOOO0 [O000O00O00O0O0OOO ]#line:869
    OOO0O00OO000OO00O =OO0000O0O0O0OOOO0 [OOO0O00OO000OO00O ]#line:870
    OOOO00OOOO0OOO000 =OO0000O0O0O0OOOO0 [OOOO00OOOO0OOO000 ]#line:871
    OOO000OOOO000OO0O =range (0 ,len (O000O00O00O0O0OOO ),1 )#line:873
    OOO0O0O0OO0O00O0O .set_xticklabels (OOOO00OOOO0OOO000 ,rotation =-90 ,fontsize =8 )#line:874
    OOO0O0O0OO0O00O0O .bar (OOO000OOOO000OO0O ,O000O00O00O0O0OOO ,align ="center",tick_label =OOOO00OOOO0OOO000 ,label =O0O000O00OOOOOO00 )#line:877
    OOO0O0O0OO0O00O0O .bar (OOO000OOOO000OO0O ,OOO0O00OO000OO00O ,align ="center",label =OO0OOO0OO0OO0OO00 )#line:880
    OOO0O0O0OO0O00O0O .set_title (OOO0O0OOOO0O0OO00 )#line:881
    OOO0O0O0OO0O00O0O .set_xlabel ("项")#line:882
    OOO0O0O0OO0O00O0O .set_ylabel ("数量")#line:883
    O00OOO00OOO0O000O .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:885
    OO0O0O000OO0000O0 =OOO0O0O0OO0O00O0O .get_position ()#line:886
    OOO0O0O0OO0O00O0O .set_position ([OO0O0O000OO0000O0 .x0 ,OO0O0O000OO0000O0 .y0 ,OO0O0O000OO0000O0 .width *0.7 ,OO0O0O000OO0000O0 .height ])#line:887
    OOO0O0O0OO0O00O0O .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:888
    OO0OO0O00OOOOO00O .draw ()#line:890
    OOO00O00O0O000OOO =Button (O00O00OO0O0O000O0 ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OO0000O0O0O0OOOO0 ),)#line:897
    OOO00O00O0O000OOO .pack (side =RIGHT )#line:898
def CLEAN_hzp (OOO000000O000OOOO ):#line:903
    ""#line:904
    if "报告编码"not in OOO000000O000OOOO .columns :#line:905
            OOO000000O000OOOO ["特殊化妆品注册证书编号/普通化妆品备案编号"]=OOO000000O000OOOO ["特殊化妆品注册证书编号/普通化妆品备案编号"].fillna ("-未填写-")#line:906
            OOO000000O000OOOO ["省级评价结果"]=OOO000000O000OOOO ["省级评价结果"].fillna ("-未填写-")#line:907
            OOO000000O000OOOO ["生产企业"]=OOO000000O000OOOO ["生产企业"].fillna ("-未填写-")#line:908
            OOO000000O000OOOO ["提交人"]="不适用"#line:909
            OOO000000O000OOOO ["医疗机构类别"]="不适用"#line:910
            OOO000000O000OOOO ["经营企业或使用单位"]="不适用"#line:911
            OOO000000O000OOOO ["报告状态"]="报告单位评价"#line:912
            OOO000000O000OOOO ["所属地区"]="不适用"#line:913
            OOO000000O000OOOO ["医院名称"]="不适用"#line:914
            OOO000000O000OOOO ["报告地区名称"]="不适用"#line:915
            OOO000000O000OOOO ["提交人"]="不适用"#line:916
            OOO000000O000OOOO ["型号"]=OOO000000O000OOOO ["化妆品分类"]#line:917
            OOO000000O000OOOO ["关联性评价"]=OOO000000O000OOOO ["上报单位评价结果"]#line:918
            OOO000000O000OOOO ["规格"]="不适用"#line:919
            OOO000000O000OOOO ["器械故障表现"]=OOO000000O000OOOO ["初步判断"]#line:920
            OOO000000O000OOOO ["伤害表现"]=OOO000000O000OOOO ["自觉症状"]+OOO000000O000OOOO ["皮损部位"]+OOO000000O000OOOO ["皮损形态"]#line:921
            OOO000000O000OOOO ["事件原因分析"]="不适用"#line:922
            OOO000000O000OOOO ["事件原因分析描述"]="不适用"#line:923
            OOO000000O000OOOO ["调查情况"]="不适用"#line:924
            OOO000000O000OOOO ["具体控制措施"]="不适用"#line:925
            OOO000000O000OOOO ["未采取控制措施原因"]="不适用"#line:926
            OOO000000O000OOOO ["报告地区名称"]="不适用"#line:927
            OOO000000O000OOOO ["上报单位所属地区"]="不适用"#line:928
            OOO000000O000OOOO ["持有人报告状态"]="不适用"#line:929
            OOO000000O000OOOO ["年龄类型"]="岁"#line:930
            OOO000000O000OOOO ["经营企业使用单位报告状态"]="不适用"#line:931
            OOO000000O000OOOO ["产品归属"]="化妆品"#line:932
            OOO000000O000OOOO ["管理类别"]="不适用"#line:933
            OOO000000O000OOOO ["超时标记"]="不适用"#line:934
            OOO000000O000OOOO =OOO000000O000OOOO .rename (columns ={"报告表编号":"报告编码","报告类型":"伤害","报告地区":"监测机构","报告单位名称":"单位名称","患者/消费者姓名":"姓名","不良反应发生日期":"事件发生日期","过程描述补充说明":"使用过程","化妆品名称":"产品名称","化妆品分类":"产品类别","生产企业":"上市许可持有人名称","生产批号":"产品批号","特殊化妆品注册证书编号/普通化妆品备案编号":"注册证编号/曾用注册证编号",})#line:953
            OOO000000O000OOOO ["时隔"]=pd .to_datetime (OOO000000O000OOOO ["事件发生日期"])-pd .to_datetime (OOO000000O000OOOO ["开始使用日期"])#line:954
            OOO000000O000OOOO .loc [(OOO000000O000OOOO ["省级评价结果"]!="-未填写-"),"有效报告"]=1 #line:955
            OOO000000O000OOOO ["伤害"]=OOO000000O000OOOO ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:956
            try :#line:957
	            OOO000000O000OOOO =TOOL_guizheng (OOO000000O000OOOO ,4 ,True )#line:958
            except :#line:959
                pass #line:960
            return OOO000000O000OOOO #line:961
def CLEAN_yp (OOOOOO000O00000O0 ):#line:966
    ""#line:967
    if "报告编码"not in OOOOOO000O00000O0 .columns :#line:968
        if "反馈码"in OOOOOO000O00000O0 .columns and "报告表编码"not in OOOOOO000O00000O0 .columns :#line:970
            OOOOOO000O00000O0 ["提交人"]="不适用"#line:972
            OOOOOO000O00000O0 ["经营企业或使用单位"]="不适用"#line:973
            OOOOOO000O00000O0 ["报告状态"]="报告单位评价"#line:974
            OOOOOO000O00000O0 ["所属地区"]="不适用"#line:975
            OOOOOO000O00000O0 ["产品类别"]="无源"#line:976
            OOOOOO000O00000O0 ["医院名称"]="不适用"#line:977
            OOOOOO000O00000O0 ["报告地区名称"]="不适用"#line:978
            OOOOOO000O00000O0 ["提交人"]="不适用"#line:979
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"反馈码":"报告表编码","序号":"药品序号","新的":"报告类型-新的","报告类型":"报告类型-严重程度","用药-日数":"用法-日","用药-次数":"用法-次",})#line:992
        if "唯一标识"not in OOOOOO000O00000O0 .columns :#line:997
            OOOOOO000O00000O0 ["报告编码"]=OOOOOO000O00000O0 ["报告表编码"].astype (str )+OOOOOO000O00000O0 ["患者姓名"].astype (str )#line:998
        if "唯一标识"in OOOOOO000O00000O0 .columns :#line:999
            OOOOOO000O00000O0 ["唯一标识"]=OOOOOO000O00000O0 ["唯一标识"].astype (str )#line:1000
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"唯一标识":"报告编码"})#line:1001
        if "医疗机构类别"not in OOOOOO000O00000O0 .columns :#line:1002
            OOOOOO000O00000O0 ["医疗机构类别"]="医疗机构"#line:1003
            OOOOOO000O00000O0 ["经营企业使用单位报告状态"]="已提交"#line:1004
        try :#line:1005
            OOOOOO000O00000O0 ["年龄和单位"]=OOOOOO000O00000O0 ["年龄"].astype (str )+OOOOOO000O00000O0 ["年龄单位"]#line:1006
        except :#line:1007
            OOOOOO000O00000O0 ["年龄和单位"]=OOOOOO000O00000O0 ["年龄"].astype (str )+OOOOOO000O00000O0 ["年龄类型"]#line:1008
        OOOOOO000O00000O0 .loc [(OOOOOO000O00000O0 ["报告类型-新的"]=="新的"),"管理类别"]="Ⅲ类"#line:1009
        OOOOOO000O00000O0 .loc [(OOOOOO000O00000O0 ["报告类型-严重程度"]=="严重"),"管理类别"]="Ⅲ类"#line:1010
        text .insert (END ,"剔除已删除报告和重复报告...")#line:1011
        if "删除标识"in OOOOOO000O00000O0 .columns :#line:1012
            OOOOOO000O00000O0 =OOOOOO000O00000O0 [(OOOOOO000O00000O0 ["删除标识"]!="删除")]#line:1013
        if "重复报告"in OOOOOO000O00000O0 .columns :#line:1014
            OOOOOO000O00000O0 =OOOOOO000O00000O0 [(OOOOOO000O00000O0 ["重复报告"]!="重复报告")]#line:1015
        OOOOOO000O00000O0 ["报告类型-新的"]=OOOOOO000O00000O0 ["报告类型-新的"].fillna (" ")#line:1018
        OOOOOO000O00000O0 .loc [(OOOOOO000O00000O0 ["报告类型-严重程度"]=="严重"),"伤害"]="严重伤害"#line:1019
        OOOOOO000O00000O0 ["伤害"]=OOOOOO000O00000O0 ["伤害"].fillna ("所有一般")#line:1020
        OOOOOO000O00000O0 ["伤害PSUR"]=OOOOOO000O00000O0 ["报告类型-新的"].astype (str )+OOOOOO000O00000O0 ["报告类型-严重程度"].astype (str )#line:1021
        OOOOOO000O00000O0 ["用量用量单位"]=OOOOOO000O00000O0 ["用量"].astype (str )+OOOOOO000O00000O0 ["用量单位"].astype (str )#line:1022
        OOOOOO000O00000O0 ["规格"]="不适用"#line:1024
        OOOOOO000O00000O0 ["事件原因分析"]="不适用"#line:1025
        OOOOOO000O00000O0 ["事件原因分析描述"]="不适用"#line:1026
        OOOOOO000O00000O0 ["初步处置情况"]="不适用"#line:1027
        OOOOOO000O00000O0 ["伤害表现"]=OOOOOO000O00000O0 ["不良反应名称"]#line:1028
        OOOOOO000O00000O0 ["产品类别"]="无源"#line:1029
        OOOOOO000O00000O0 ["调查情况"]="不适用"#line:1030
        OOOOOO000O00000O0 ["具体控制措施"]="不适用"#line:1031
        OOOOOO000O00000O0 ["上报单位所属地区"]=OOOOOO000O00000O0 ["报告地区名称"]#line:1032
        OOOOOO000O00000O0 ["未采取控制措施原因"]="不适用"#line:1033
        OOOOOO000O00000O0 ["报告单位评价"]=OOOOOO000O00000O0 ["报告类型-新的"].astype (str )+OOOOOO000O00000O0 ["报告类型-严重程度"].astype (str )#line:1034
        OOOOOO000O00000O0 .loc [(OOOOOO000O00000O0 ["报告类型-新的"]=="新的"),"持有人报告状态"]="待评价"#line:1035
        OOOOOO000O00000O0 ["用法temp日"]="日"#line:1036
        OOOOOO000O00000O0 ["用法temp次"]="次"#line:1037
        OOOOOO000O00000O0 ["用药频率"]=(OOOOOO000O00000O0 ["用法-日"].astype (str )+OOOOOO000O00000O0 ["用法temp日"]+OOOOOO000O00000O0 ["用法-次"].astype (str )+OOOOOO000O00000O0 ["用法temp次"])#line:1043
        try :#line:1044
            OOOOOO000O00000O0 ["相关疾病信息[疾病名称]-术语"]=OOOOOO000O00000O0 ["原患疾病"]#line:1045
            OOOOOO000O00000O0 ["治疗适应症-术语"]=OOOOOO000O00000O0 ["用药原因"]#line:1046
        except :#line:1047
            pass #line:1048
        try :#line:1050
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"提交日期":"报告日期"})#line:1051
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"提交人":"报告人"})#line:1052
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"报告状态":"持有人报告状态"})#line:1053
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"所属地区":"使用单位、经营企业所属监测机构"})#line:1054
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"医院名称":"单位名称"})#line:1055
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"批准文号":"注册证编号/曾用注册证编号"})#line:1056
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"通用名称":"产品名称"})#line:1057
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"生产厂家":"上市许可持有人名称"})#line:1058
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"不良反应发生时间":"事件发生日期"})#line:1059
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"不良反应名称":"器械故障表现"})#line:1060
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"不良反应过程描述":"使用过程"})#line:1061
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"生产批号":"产品批号"})#line:1062
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:1063
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"剂型":"型号"})#line:1064
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"报告人评价":"关联性评价"})#line:1065
            OOOOOO000O00000O0 =OOOOOO000O00000O0 .rename (columns ={"年龄单位":"年龄类型"})#line:1066
        except :#line:1067
            text .insert (END ,"数据规整失败。")#line:1068
            return 0 #line:1069
        OOOOOO000O00000O0 ['报告日期']=OOOOOO000O00000O0 ['报告日期'].str .strip ()#line:1072
        OOOOOO000O00000O0 ['事件发生日期']=OOOOOO000O00000O0 ['事件发生日期'].str .strip ()#line:1073
        OOOOOO000O00000O0 ['用药开始时间']=OOOOOO000O00000O0 ['用药开始时间'].str .strip ()#line:1074
        return OOOOOO000O00000O0 #line:1076
    if "报告编码"in OOOOOO000O00000O0 .columns :#line:1077
        return OOOOOO000O00000O0 #line:1078
def CLEAN_qx (O0OOO0000O000OO00 ):#line:1080
		""#line:1081
		if "使用单位、经营企业所属监测机构"not in O0OOO0000O000OO00 .columns and "监测机构"not in O0OOO0000O000OO00 .columns :#line:1083
			O0OOO0000O000OO00 ["使用单位、经营企业所属监测机构"]="本地"#line:1084
		if "上市许可持有人名称"not in O0OOO0000O000OO00 .columns :#line:1085
			O0OOO0000O000OO00 ["上市许可持有人名称"]=O0OOO0000O000OO00 ["单位名称"]#line:1086
		if "注册证编号/曾用注册证编号"not in O0OOO0000O000OO00 .columns :#line:1087
			O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]=O0OOO0000O000OO00 ["注册证编号"]#line:1088
		if "事件原因分析描述"not in O0OOO0000O000OO00 .columns :#line:1089
			O0OOO0000O000OO00 ["事件原因分析描述"]="  "#line:1090
		if "初步处置情况"not in O0OOO0000O000OO00 .columns :#line:1091
			O0OOO0000O000OO00 ["初步处置情况"]="  "#line:1092
		text .insert (END ,"\n正在执行格式规整和增加有关时间、年龄、性别等统计列...")#line:1095
		O0OOO0000O000OO00 =O0OOO0000O000OO00 .rename (columns ={"使用单位、经营企业所属监测机构":"监测机构"})#line:1096
		O0OOO0000O000OO00 ["报告编码"]=O0OOO0000O000OO00 ["报告编码"].astype ("str")#line:1097
		O0OOO0000O000OO00 ["产品批号"]=O0OOO0000O000OO00 ["产品批号"].astype ("str")#line:1098
		O0OOO0000O000OO00 ["型号"]=O0OOO0000O000OO00 ["型号"].astype ("str")#line:1099
		O0OOO0000O000OO00 ["规格"]=O0OOO0000O000OO00 ["规格"].astype ("str")#line:1100
		O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]=O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1101
		O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]=O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1102
		O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]=O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1103
		O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]=O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"].fillna ("-未填写-")#line:1104
		O0OOO0000O000OO00 ["产品名称"]=O0OOO0000O000OO00 ["产品名称"].str .replace ("*","※",regex =False )#line:1105
		O0OOO0000O000OO00 ["产品批号"]=O0OOO0000O000OO00 ["产品批号"].str .replace ("(","（",regex =False )#line:1106
		O0OOO0000O000OO00 ["产品批号"]=O0OOO0000O000OO00 ["产品批号"].str .replace (")","）",regex =False )#line:1107
		O0OOO0000O000OO00 ["产品批号"]=O0OOO0000O000OO00 ["产品批号"].str .replace ("*","※",regex =False )#line:1108
		O0OOO0000O000OO00 ["伤害与评价"]=O0OOO0000O000OO00 ["伤害"]+O0OOO0000O000OO00 ["持有人报告状态"]#line:1111
		O0OOO0000O000OO00 ["注册证备份"]=O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]#line:1112
		O0OOO0000O000OO00 ['报告日期']=pd .to_datetime (O0OOO0000O000OO00 ['报告日期'],format ='%Y-%m-%d',errors ='coerce')#line:1115
		O0OOO0000O000OO00 ['事件发生日期']=pd .to_datetime (O0OOO0000O000OO00 ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1116
		O0OOO0000O000OO00 ["报告月份"]=O0OOO0000O000OO00 ["报告日期"].dt .to_period ("M").astype (str )#line:1118
		O0OOO0000O000OO00 ["报告季度"]=O0OOO0000O000OO00 ["报告日期"].dt .to_period ("Q").astype (str )#line:1119
		O0OOO0000O000OO00 ["报告年份"]=O0OOO0000O000OO00 ["报告日期"].dt .to_period ("Y").astype (str )#line:1120
		O0OOO0000O000OO00 ["事件发生月份"]=O0OOO0000O000OO00 ["事件发生日期"].dt .to_period ("M").astype (str )#line:1121
		O0OOO0000O000OO00 ["事件发生季度"]=O0OOO0000O000OO00 ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1122
		O0OOO0000O000OO00 ["事件发生年份"]=O0OOO0000O000OO00 ["事件发生日期"].dt .to_period ("Y").astype (str )#line:1123
		if ini ["模式"]=="器械":#line:1127
			O0OOO0000O000OO00 ['发现或获知日期']=pd .to_datetime (O0OOO0000O000OO00 ['发现或获知日期'],format ='%Y-%m-%d',errors ='coerce')#line:1128
			O0OOO0000O000OO00 ["时隔"]=pd .to_datetime (O0OOO0000O000OO00 ["发现或获知日期"])-pd .to_datetime (O0OOO0000O000OO00 ["事件发生日期"])#line:1129
			O0OOO0000O000OO00 ["报告时限"]=pd .to_datetime (O0OOO0000O000OO00 ["报告日期"])-pd .to_datetime (O0OOO0000O000OO00 ["发现或获知日期"])#line:1130
			O0OOO0000O000OO00 ["报告时限"]=O0OOO0000O000OO00 ["报告时限"].dt .days #line:1131
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>20 )&(O0OOO0000O000OO00 ["伤害"]=="严重伤害"),"超时标记"]=1 #line:1132
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>30 )&(O0OOO0000O000OO00 ["伤害"]=="其他"),"超时标记"]=1 #line:1133
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>7 )&(O0OOO0000O000OO00 ["伤害"]=="死亡"),"超时标记"]=1 #line:1134
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["经营企业使用单位报告状态"]=="审核通过"),"有效报告"]=1 #line:1136
		if ini ["模式"]=="药品":#line:1139
			O0OOO0000O000OO00 ['用药开始时间']=pd .to_datetime (O0OOO0000O000OO00 ['用药开始时间'],format ='%Y-%m-%d',errors ='coerce')#line:1140
			O0OOO0000O000OO00 ["时隔"]=pd .to_datetime (O0OOO0000O000OO00 ["事件发生日期"])-pd .to_datetime (O0OOO0000O000OO00 ["用药开始时间"])#line:1141
			O0OOO0000O000OO00 ["报告时限"]=pd .to_datetime (O0OOO0000O000OO00 ["报告日期"])-pd .to_datetime (O0OOO0000O000OO00 ["事件发生日期"])#line:1142
			O0OOO0000O000OO00 ["报告时限"]=O0OOO0000O000OO00 ["报告时限"].dt .days #line:1143
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>15 )&(O0OOO0000O000OO00 ["报告类型-严重程度"]=="严重"),"超时标记"]=1 #line:1144
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>30 )&(O0OOO0000O000OO00 ["报告类型-严重程度"]=="一般"),"超时标记"]=1 #line:1145
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>15 )&(O0OOO0000O000OO00 ["报告类型-新的"]=="新的"),"超时标记"]=1 #line:1146
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["报告时限"]>1 )&(O0OOO0000O000OO00 ["报告类型-严重程度"]=="死亡"),"超时标记"]=1 #line:1147
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["评价状态"]!="未评价"),"有效报告"]=1 #line:1149
		O0OOO0000O000OO00 .loc [((O0OOO0000O000OO00 ["年龄"]=="未填写")|O0OOO0000O000OO00 ["年龄"].isnull ()),"年龄"]=-1 #line:1151
		O0OOO0000O000OO00 ["年龄"]=O0OOO0000O000OO00 ["年龄"].astype (float )#line:1152
		O0OOO0000O000OO00 ["年龄"]=O0OOO0000O000OO00 ["年龄"].fillna (-1 )#line:1153
		O0OOO0000O000OO00 ["性别"]=O0OOO0000O000OO00 ["性别"].fillna ("未填写")#line:1154
		O0OOO0000O000OO00 ["年龄段"]="未填写"#line:1155
		try :#line:1156
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄类型"]=="月"),"年龄"]=O0OOO0000O000OO00 ["年龄"].values /12 #line:1157
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄类型"]=="月"),"年龄类型"]="岁"#line:1158
		except :#line:1159
			pass #line:1160
		try :#line:1161
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄类型"]=="天"),"年龄"]=O0OOO0000O000OO00 ["年龄"].values /365 #line:1162
			O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄类型"]=="天"),"年龄类型"]="岁"#line:1163
		except :#line:1164
			pass #line:1165
		O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄"].values <=4 ),"年龄段"]="0-婴幼儿（0-4）"#line:1166
		O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄"].values >=5 ),"年龄段"]="1-少儿（5-14）"#line:1167
		O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄"].values >=15 ),"年龄段"]="2-青壮年（15-44）"#line:1168
		O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄"].values >=45 ),"年龄段"]="3-中年期（45-64）"#line:1169
		O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄"].values >=65 ),"年龄段"]="4-老年期（≥65）"#line:1170
		O0OOO0000O000OO00 .loc [(O0OOO0000O000OO00 ["年龄"].values ==-1 ),"年龄段"]="未填写"#line:1171
		O0OOO0000O000OO00 ["规整后品类"]="N"#line:1175
		O0OOO0000O000OO00 =TOOL_guizheng (O0OOO0000O000OO00 ,2 ,True )#line:1176
		if ini ['模式']in ["器械"]:#line:1179
			O0OOO0000O000OO00 =TOOL_guizheng (O0OOO0000O000OO00 ,3 ,True )#line:1180
		O0OOO0000O000OO00 =TOOL_guizheng (O0OOO0000O000OO00 ,"课题",True )#line:1184
		try :#line:1186
			O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"]=O0OOO0000O000OO00 ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1187
		except :#line:1188
			pass #line:1189
		O0OOO0000O000OO00 ["数据清洗完成标记"]="是"#line:1191
		OOO00O00OOOO0OO00 =O0OOO0000O000OO00 .loc [:]#line:1192
		return O0OOO0000O000OO00 #line:1193
def TOOLS_fileopen ():#line:1199
    ""#line:1200
    warnings .filterwarnings ('ignore')#line:1201
    OOOOOO0O0O0O0O000 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:1202
    OO0OOOOO000O00000 =Useful_tools_openfiles (OOOOOO0O0O0O0O000 ,0 )#line:1203
    try :#line:1204
        OO0OOOOO000O00000 =OO0OOOOO000O00000 .loc [:,~OO0OOOOO000O00000 .columns .str .contains ("^Unnamed")]#line:1205
    except :#line:1206
        pass #line:1207
    ini ["模式"]="其他"#line:1209
    O0000OOO0OO000O0O =OO0OOOOO000O00000 #line:1210
    TABLE_tree_Level_2 (O0000OOO0OO000O0O ,0 ,O0000OOO0OO000O0O )#line:1211
def TOOLS_pinzhong (O000OOO00O00OOOOO ):#line:1214
    ""#line:1215
    O000OOO00O00OOOOO ["患者姓名"]=O000OOO00O00OOOOO ["报告表编码"]#line:1216
    O000OOO00O00OOOOO ["用量"]=O000OOO00O00OOOOO ["用法用量"]#line:1217
    O000OOO00O00OOOOO ["评价状态"]=O000OOO00O00OOOOO ["报告单位评价"]#line:1218
    O000OOO00O00OOOOO ["用量单位"]=""#line:1219
    O000OOO00O00OOOOO ["单位名称"]="不适用"#line:1220
    O000OOO00O00OOOOO ["报告地区名称"]="不适用"#line:1221
    O000OOO00O00OOOOO ["用法-日"]="不适用"#line:1222
    O000OOO00O00OOOOO ["用法-次"]="不适用"#line:1223
    O000OOO00O00OOOOO ["不良反应发生时间"]=O000OOO00O00OOOOO ["不良反应发生时间"].str [0 :10 ]#line:1224
    O000OOO00O00OOOOO ["持有人报告状态"]="待评价"#line:1226
    O000OOO00O00OOOOO =O000OOO00O00OOOOO .rename (columns ={"是否非预期":"报告类型-新的","不良反应-术语":"不良反应名称","持有人/生产厂家":"上市许可持有人名称"})#line:1231
    return O000OOO00O00OOOOO #line:1232
def Useful_tools_openfiles (OO00O00OO0O00OOOO ,OOOOO000OO0000OOO ):#line:1237
    ""#line:1238
    OOOOO000OO0OOO00O =[pd .read_excel (OO0OOO0OOO00O0O00 ,header =0 ,sheet_name =OOOOO000OO0000OOO )for OO0OOO0OOO00O0O00 in OO00O00OO0O00OOOO ]#line:1239
    OO0O0OO0OOOOOOOO0 =pd .concat (OOOOO000OO0OOO00O ,ignore_index =True ).drop_duplicates ()#line:1240
    return OO0O0OO0OOOOOOOO0 #line:1241
def TOOLS_allfileopen ():#line:1243
    ""#line:1244
    global ori #line:1245
    global ini #line:1246
    global data #line:1247
    ini ["原始模式"]="否"#line:1248
    warnings .filterwarnings ('ignore')#line:1249
    O000OOO0OO0O0O000 =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:1251
    ori =Useful_tools_openfiles (O000OOO0OO0O0O000 ,0 )#line:1252
    try :#line:1256
        OO0OO0OOOO00OOO00 =Useful_tools_openfiles (O000OOO0OO0O0O000 ,"报告信息")#line:1257
        if "是否非预期"in OO0OO0OOOO00OOO00 .columns :#line:1258
            ori =TOOLS_pinzhong (OO0OO0OOOO00OOO00 )#line:1259
    except :#line:1260
        pass #line:1261
    ini ["模式"]="其他"#line:1263
    try :#line:1265
        ori =Useful_tools_openfiles (O000OOO0OO0O0O000 ,"字典数据")#line:1266
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
        O00O0OO0OOO0O00OO =Menu (root )#line:1309
        root .config (menu =O00O0OO0OOO0O00OO )#line:1310
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
        OOO0000OOO0O00O0O =Button (frame0 ,text ="地市统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_org ("市级监测机构"),1 ,ori ),)#line:1343
        OOO0000OOO0O00O0O .pack ()#line:1344
        O000O0O000O0O0O0O =Button (frame0 ,text ="县区统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_org ("监测机构"),1 ,ori ),)#line:1357
        O000O0O000O0O0O0O .pack ()#line:1358
        O0OO0OO00OOO0O00O =Button (frame0 ,text ="上报单位",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_user (),1 ,ori ),)#line:1371
        O0OO0OO00OOO0O00O .pack ()#line:1372
        O0O00O0OO00OO00OO =Button (frame0 ,text ="生产企业",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (data ).df_chiyouren (),1 ,ori ),)#line:1383
        O0O00O0OO00OO00OO .pack ()#line:1384
        OOOO0O00O0OOO000O =Button (frame0 ,text ="产品统计",bg ="white",height =2 ,width =12 ,font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (ini ["证号"],1 ,ori ,ori ,"dfx_zhenghao"),)#line:1395
        OOOO0O00O0OOO000O .pack ()#line:1396
        ini ["button"]=[OOO0000OOO0O00O0O ,O000O0O000O0O0O0O ,O0OO0OO00OOO0O00O ,O0O00O0OO00OO00OO ,OOOO0O00O0OOO000O ]#line:1397
    text .insert (END ,"\n")#line:1399
def TOOLS_sql (O0OOOOO00OOOOO000 ):#line:1401
    ""#line:1402
    warnings .filterwarnings ("ignore")#line:1403
    try :#line:1404
        OOO0OO0000O0OOO00 =O0OOOOO00OOOOO000 .columns #line:1405
    except :#line:1406
        return 0 #line:1407
    def OOOOO0OOO0OO0000O (O0OOOOOO000OOO000 ):#line:1409
        try :#line:1410
            O000OO00O0OO0O0OO =pd .read_sql_query (sqltext (O0OOOOOO000OOO000 ),con =O0O0000O000OO0000 )#line:1411
        except :#line:1412
            showinfo (title ="提示",message ="SQL语句有误。")#line:1413
            return 0 #line:1414
        try :#line:1415
            del O000OO00O0OO0O0OO ["level_0"]#line:1416
        except :#line:1417
            pass #line:1418
        TABLE_tree_Level_2 (O000OO00O0OO0O0OO ,1 ,O0OOOOO00OOOOO000 )#line:1419
    O00OOOO000O0OOOOO ='sqlite://'#line:1423
    O00000O0O000O00O0 =create_engine (O00OOOO000O0OOOOO )#line:1424
    try :#line:1425
        O0OOOOO00OOOOO000 .to_sql ('data',con =O00000O0O000O00O0 ,chunksize =10000 ,if_exists ='replace',index =True )#line:1426
    except :#line:1427
        showinfo (title ="提示",message ="不支持该表格。")#line:1428
        return 0 #line:1429
    O0O0000O000OO0000 =O00000O0O000O00O0 .connect ()#line:1431
    O0O00OO0O0O0OO0OO ="select * from data"#line:1432
    OOOO000OO0OOO000O =Toplevel ()#line:1435
    OOOO000OO0OOO000O .title ("SQL查询")#line:1436
    OOOO000OO0OOO000O .geometry ("700x500")#line:1437
    O00OOOO0OO000OOO0 =ttk .Frame (OOOO000OO0OOO000O ,width =700 ,height =20 )#line:1439
    O00OOOO0OO000OOO0 .pack (side =TOP )#line:1440
    O0O0OO0000OO0000O =ttk .Frame (OOOO000OO0OOO000O ,width =700 ,height =20 )#line:1441
    O0O0OO0000OO0000O .pack (side =BOTTOM )#line:1442
    try :#line:1445
        O0OO0OO0OOO0OOO00 =StringVar ()#line:1446
        O0OO0OO0OOO0OOO00 .set ("select * from data WHERE 单位名称='佛山市第一人民医院'")#line:1447
        O0OO00OO0OO000O0O =Label (O00OOOO0OO000OOO0 ,text ="SQL查询",anchor ='w')#line:1449
        O0OO00OO0OO000O0O .pack (side =LEFT )#line:1450
        OO0OO0OOO0O0O000O =Label (O00OOOO0OO000OOO0 ,text ="检索：")#line:1451
        O0OO0OOO0O0OOO000 =Button (O0O0OO0000OO0000O ,text ="执行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",width =700 ,command =lambda :OOOOO0OOO0OO0000O (O0O00O0O0O0OO0OO0 .get ("1.0","end")),)#line:1465
        O0OO0OOO0O0OOO000 .pack (side =LEFT )#line:1466
    except EE :#line:1469
        pass #line:1470
    O00OOOOO0O0000OO0 =Scrollbar (OOOO000OO0OOO000O )#line:1472
    O0O00O0O0O0OO0OO0 =Text (OOOO000OO0OOO000O ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1473
    O00OOOOO0O0000OO0 .pack (side =RIGHT ,fill =Y )#line:1474
    O0O00O0O0O0OO0OO0 .pack ()#line:1475
    O00OOOOO0O0000OO0 .config (command =O0O00O0O0O0OO0OO0 .yview )#line:1476
    O0O00O0O0O0OO0OO0 .config (yscrollcommand =O00OOOOO0O0000OO0 .set )#line:1477
    def O0000OO0OO00OO000 (event =None ):#line:1478
        O0O00O0O0O0OO0OO0 .event_generate ('<<Copy>>')#line:1479
    def O000O00000000000O (event =None ):#line:1480
        O0O00O0O0O0OO0OO0 .event_generate ('<<Paste>>')#line:1481
    def OO0O00000O0O0OO00 (OOOOO0OOOOOOOOOO0 ,OOOO0O000O000000O ):#line:1482
         TOOLS_savetxt (OOOOO0OOOOOOOOOO0 ,OOOO0O000O000000O ,1 )#line:1483
    O0O00O000OOO0OOO0 =Menu (O0O00O0O0O0OO0OO0 ,tearoff =False ,)#line:1484
    O0O00O000OOO0OOO0 .add_command (label ="复制",command =O0000OO0OO00OO000 )#line:1485
    O0O00O000OOO0OOO0 .add_command (label ="粘贴",command =O000O00000000000O )#line:1486
    O0O00O000OOO0OOO0 .add_command (label ="源文件列",command =lambda :PROGRAM_helper (O0OOOOO00OOOOO000 .columns .to_list ()))#line:1487
    def O0OO00OO0OOOO0000 (O00O00000OO000OOO ):#line:1488
         O0O00O000OOO0OOO0 .post (O00O00000OO000OOO .x_root ,O00O00000OO000OOO .y_root )#line:1489
    O0O00O0O0O0OO0OO0 .bind ("<Button-3>",O0OO00OO0OOOO0000 )#line:1490
    O0O00O0O0O0OO0OO0 .insert (END ,O0O00OO0O0O0OO0OO )#line:1494
def TOOLS_view_dict (O0000O000OOOO000O ,OOOO00O00O00O0O00 ):#line:1498
    ""#line:1499
    OOO000O0O0OO0O0O0 =Toplevel ()#line:1500
    OOO000O0O0OO0O0O0 .title ("查看数据")#line:1501
    OOO000O0O0OO0O0O0 .geometry ("700x500")#line:1502
    O00OO00OO00O000O0 =Scrollbar (OOO000O0O0OO0O0O0 )#line:1504
    OO0O00O0000O0000O =Text (OOO000O0O0OO0O0O0 ,height =100 ,width =150 )#line:1505
    O00OO00OO00O000O0 .pack (side =RIGHT ,fill =Y )#line:1506
    OO0O00O0000O0000O .pack ()#line:1507
    O00OO00OO00O000O0 .config (command =OO0O00O0000O0000O .yview )#line:1508
    OO0O00O0000O0000O .config (yscrollcommand =O00OO00OO00O000O0 .set )#line:1509
    if OOOO00O00O00O0O00 ==1 :#line:1510
        OO0O00O0000O0000O .insert (END ,O0000O000OOOO000O )#line:1512
        OO0O00O0000O0000O .insert (END ,"\n\n")#line:1513
        return 0 #line:1514
    for O0O00O0OO0000OOO0 in range (len (O0000O000OOOO000O )):#line:1515
        OO0O00O0000O0000O .insert (END ,O0000O000OOOO000O .iloc [O0O00O0OO0000OOO0 ,0 ])#line:1516
        OO0O00O0000O0000O .insert (END ,":")#line:1517
        OO0O00O0000O0000O .insert (END ,O0000O000OOOO000O .iloc [O0O00O0OO0000OOO0 ,1 ])#line:1518
        OO0O00O0000O0000O .insert (END ,"\n\n")#line:1519
def TOOLS_save_dict (OOOOOO0OO00OOO000 ):#line:1521
    ""#line:1522
    O0O0O0OOO0O0O00OO =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="排序后的原始数据",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1528
    try :#line:1529
        OOOOOO0OO00OOO000 ["详细描述T"]=OOOOOO0OO00OOO000 ["详细描述T"].astype (str )#line:1530
    except :#line:1531
        pass #line:1532
    try :#line:1533
        OOOOOO0OO00OOO000 ["报告编码"]=OOOOOO0OO00OOO000 ["报告编码"].astype (str )#line:1534
    except :#line:1535
        pass #line:1536
    O0OOO00OOOOOO0OOO =pd .ExcelWriter (O0O0O0OOO0O0O00OO ,engine ="xlsxwriter")#line:1538
    OOOOOO0OO00OOO000 .to_excel (O0OOO00OOOOOO0OOO ,sheet_name ="字典数据")#line:1539
    O0OOO00OOOOOO0OOO .close ()#line:1540
    showinfo (title ="提示",message ="文件写入成功。")#line:1541
def TOOLS_savetxt (O0OO000O0000000OO ,O0O000O0OOO000OOO ,O0000O0OOOO00OOOO ):#line:1543
	""#line:1544
	O0OOO00OO00OOO0OO =open (O0O000O0OOO000OOO ,"w",encoding ='utf-8')#line:1545
	O0OOO00OO00OOO0OO .write (O0OO000O0000000OO )#line:1546
	O0OOO00OO00OOO0OO .flush ()#line:1548
	if O0000O0OOOO00OOOO ==1 :#line:1549
		showinfo (title ="提示信息",message ="保存成功。")#line:1550
def TOOLS_deep_view (OOO0OOOO0OO0OOOOO ,OOO000OO0OOO0OO0O ,O00O00000O0OOO0OO ,OOO00OO0OO00O0OO0 ):#line:1553
    ""#line:1554
    if OOO00OO0OO00O0OO0 ==0 :#line:1555
        try :#line:1556
            OOO0OOOO0OO0OOOOO [OOO000OO0OOO0OO0O ]=OOO0OOOO0OO0OOOOO [OOO000OO0OOO0OO0O ].fillna ("这个没有填写")#line:1557
        except :#line:1558
            pass #line:1559
        O00OOO00O00OO00OO =OOO0OOOO0OO0OOOOO .groupby (OOO000OO0OOO0OO0O ).agg (计数 =(O00O00000O0OOO0OO [0 ],O00O00000O0OOO0OO [1 ]))#line:1560
    if OOO00OO0OO00O0OO0 ==1 :#line:1561
            O00OOO00O00OO00OO =pd .pivot_table (OOO0OOOO0OO0OOOOO ,index =OOO000OO0OOO0OO0O [:-1 ],columns =OOO000OO0OOO0OO0O [-1 ],values =[O00O00000O0OOO0OO [0 ]],aggfunc ={O00O00000O0OOO0OO [0 ]:O00O00000O0OOO0OO [1 ]},fill_value ="0",margins =True ,dropna =False ,)#line:1572
            O00OOO00O00OO00OO .columns =O00OOO00O00OO00OO .columns .droplevel (0 )#line:1573
            O00OOO00O00OO00OO =O00OOO00O00OO00OO .rename (columns ={"All":"计数"})#line:1574
    if "日期"in OOO000OO0OOO0OO0O or "时间"in OOO000OO0OOO0OO0O or "季度"in OOO000OO0OOO0OO0O :#line:1577
        O00OOO00O00OO00OO =O00OOO00O00OO00OO .sort_values ([OOO000OO0OOO0OO0O ],ascending =False ,na_position ="last")#line:1580
    else :#line:1581
        O00OOO00O00OO00OO =O00OOO00O00OO00OO .sort_values (by =["计数"],ascending =False ,na_position ="last")#line:1585
    O00OOO00O00OO00OO =O00OOO00O00OO00OO .reset_index ()#line:1586
    O00OOO00O00OO00OO ["构成比(%)"]=round (100 *O00OOO00O00OO00OO ["计数"]/O00OOO00O00OO00OO ["计数"].sum (),2 )#line:1587
    if OOO00OO0OO00O0OO0 ==0 :#line:1588
        O00OOO00O00OO00OO ["报表类型"]="dfx_deepview"+"_"+str (OOO000OO0OOO0OO0O )#line:1589
    if OOO00OO0OO00O0OO0 ==1 :#line:1590
        O00OOO00O00OO00OO ["报表类型"]="dfx_deepview"+"_"+str (OOO000OO0OOO0OO0O [:-1 ])#line:1591
    return O00OOO00O00OO00OO #line:1592
def TOOLS_easyreadT (OOO00O00O000O0O0O ):#line:1596
    ""#line:1597
    OOO00O00O000O0O0O ["#####分隔符#########"]="######################################################################"#line:1600
    OOOO0O00O0OO0OOO0 =OOO00O00O000O0O0O .stack (dropna =False )#line:1601
    OOOO0O00O0OO0OOO0 =pd .DataFrame (OOOO0O00O0OO0OOO0 ).reset_index ()#line:1602
    OOOO0O00O0OO0OOO0 .columns =["序号","条目","详细描述T"]#line:1603
    OOOO0O00O0OO0OOO0 ["逐条查看"]="逐条查看"#line:1604
    return OOOO0O00O0OO0OOO0 #line:1605
def TOOLS_data_masking (OOOOO00OO0O00O0O0 ):#line:1607
    ""#line:1608
    from random import choices #line:1609
    from string import ascii_letters ,digits #line:1610
    OOOOO00OO0O00O0O0 =OOOOO00OO0O00O0O0 .reset_index (drop =True )#line:1612
    if "单位名称.1"in OOOOO00OO0O00O0O0 .columns :#line:1613
        OO0OO0O00OO00O0OO ="器械"#line:1614
    else :#line:1615
        OO0OO0O00OO00O0OO ="药品"#line:1616
    OOO00OOO0O0O0OO00 ="配置表/"+"0（范例）数据脱敏"+".xls"#line:1617
    try :#line:1618
        OOO00O00OO0OOOOOO =pd .read_excel (OOO00OOO0O0O0OO00 ,sheet_name =OO0OO0O00OO00O0OO ,header =0 ,index_col =0 ).reset_index ()#line:1621
    except :#line:1622
        showinfo (title ="错误信息",message ="该功能需要配置文件才能使用！")#line:1623
        return 0 #line:1624
    O0O0O00000O0O00OO =0 #line:1625
    O0OOO00OOOOOO00O0 =len (OOOOO00OO0O00O0O0 )#line:1626
    OOOOO00OO0O00O0O0 ["abcd"]="□"#line:1627
    for O000OOOOO00000O00 in OOO00O00OO0OOOOOO ["要脱敏的列"]:#line:1628
        O0O0O00000O0O00OO =O0O0O00000O0O00OO +1 #line:1629
        PROGRAM_change_schedule (O0O0O00000O0O00OO ,O0OOO00OOOOOO00O0 )#line:1630
        text .insert (END ,"\n正在对以下列进行脱敏处理：")#line:1631
        text .see (END )#line:1632
        text .insert (END ,O000OOOOO00000O00 )#line:1633
        try :#line:1634
            O0OO0000OOO0000OO =set (OOOOO00OO0O00O0O0 [O000OOOOO00000O00 ])#line:1635
        except :#line:1636
            showinfo (title ="提示",message ="脱敏文件配置错误，请修改配置表。")#line:1637
            return 0 #line:1638
        O0O0O0OOOOO0O0000 ={O000OOOO000OO0O00 :"".join (choices (digits ,k =10 ))for O000OOOO000OO0O00 in O0OO0000OOO0000OO }#line:1639
        OOOOO00OO0O00O0O0 [O000OOOOO00000O00 ]=OOOOO00OO0O00O0O0 [O000OOOOO00000O00 ].map (O0O0O0OOOOO0O0000 )#line:1640
        OOOOO00OO0O00O0O0 [O000OOOOO00000O00 ]=OOOOO00OO0O00O0O0 ["abcd"]+OOOOO00OO0O00O0O0 [O000OOOOO00000O00 ].astype (str )#line:1641
    try :#line:1642
        PROGRAM_change_schedule (10 ,10 )#line:1643
        del OOOOO00OO0O00O0O0 ["abcd"]#line:1644
        O0O000000OOO0OO00 =filedialog .asksaveasfilename (title =u"保存脱敏后的文件",initialfile ="脱敏后的文件",defaultextension ="xlsx",filetypes =[("Excel 工作簿","*.xlsx"),("Excel 97-2003 工作簿","*.xls")],)#line:1650
        O0O0000000000OO00 =pd .ExcelWriter (O0O000000OOO0OO00 ,engine ="xlsxwriter")#line:1651
        OOOOO00OO0O00O0O0 .to_excel (O0O0000000000OO00 ,sheet_name ="sheet0")#line:1652
        O0O0000000000OO00 .close ()#line:1653
    except :#line:1654
        text .insert (END ,"\n文件未保存，但导入的数据已按要求脱敏。")#line:1655
    text .insert (END ,"\n脱敏操作完成。")#line:1656
    text .see (END )#line:1657
    return OOOOO00OO0O00O0O0 #line:1658
def TOOLS_get_new (O00OO000O0O0O0O00 ,OOO00O000OO00OO00 ):#line:1660
	""#line:1661
	def O00O000O0000OOOOO (O00OO000OO000O00O ):#line:1662
		""#line:1663
		O00OO000OO000O00O =O00OO000OO000O00O .drop_duplicates ("报告编码")#line:1664
		OOO0O0O000OO0OO0O =str (Counter (TOOLS_get_list0 ("use(器械故障表现).file",O00OO000OO000O00O ,1000 ))).replace ("Counter({","{")#line:1665
		OOO0O0O000OO0OO0O =OOO0O0O000OO0OO0O .replace ("})","}")#line:1666
		import ast #line:1667
		OO000O00OOOO000O0 =ast .literal_eval (OOO0O0O000OO0OO0O )#line:1668
		OOO000O0OOO00O000 =TOOLS_easyreadT (pd .DataFrame ([OO000O00OOOO000O0 ]))#line:1669
		OOO000O0OOO00O000 =OOO000O0OOO00O000 .rename (columns ={"逐条查看":"ADR名称规整"})#line:1670
		return OOO000O0OOO00O000 #line:1671
	if OOO00O000OO00OO00 =="证号":#line:1672
		root .attributes ("-topmost",True )#line:1673
		root .attributes ("-topmost",False )#line:1674
		O0OO00O0OOO000OO0 =O00OO000O0O0O0O00 .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]).agg (计数 =("报告编码","nunique")).reset_index ()#line:1675
		O000000OO0O0OO0OO =O0OO00O0OOO000OO0 .drop_duplicates ("注册证编号/曾用注册证编号").copy ()#line:1676
		O000000OO0O0OO0OO ["所有不良反应"]=""#line:1677
		O000000OO0O0OO0OO ["关注建议"]=""#line:1678
		O000000OO0O0OO0OO ["疑似新的"]=""#line:1679
		O000000OO0O0OO0OO ["疑似旧的"]=""#line:1680
		O000000OO0O0OO0OO ["疑似新的（高敏）"]=""#line:1681
		O000000OO0O0OO0OO ["疑似旧的（高敏）"]=""#line:1682
		O0OO0O0OOO00OO000 =1 #line:1683
		O00O0OOOO0OO0OOOO =int (len (O000000OO0O0OO0OO ))#line:1684
		for O0O0OOO0OO0O0OO0O ,O0OOOO000O00OOO0O in O000000OO0O0OO0OO .iterrows ():#line:1685
			O00O0O00OO0OO00O0 =O00OO000O0O0O0O00 [(O00OO000O0O0O0O00 ["注册证编号/曾用注册证编号"]==O0OOOO000O00OOO0O ["注册证编号/曾用注册证编号"])]#line:1686
			OO0OOO0O0OOO0OOO0 =O00O0O00OO0OO00O0 .loc [O00O0O00OO0OO00O0 ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1687
			O00O0O0OO00O000O0 =O00O0O00OO0OO00O0 .loc [~O00O0O00OO0OO00O0 ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1688
			O00OO0O0O00O0O00O =O00O000O0000OOOOO (OO0OOO0O0OOO0OOO0 )#line:1689
			O000OOOO000O0O00O =O00O000O0000OOOOO (O00O0O0OO00O000O0 )#line:1690
			O0OO00000O0OO00O0 =O00O000O0000OOOOO (O00O0O00OO0OO00O0 )#line:1691
			PROGRAM_change_schedule (O0OO0O0OOO00OO000 ,O00O0OOOO0OO0OOOO )#line:1692
			O0OO0O0OOO00OO000 =O0OO0O0OOO00OO000 +1 #line:1693
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O0OO00000O0OO00O0 .iterrows ():#line:1695
					if "分隔符"not in O00O000OOO00OO000 ["条目"]:#line:1696
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1697
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"所有不良反应"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"所有不良反应"]+O0OO00OOOOOOO0O0O #line:1698
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O000OOOO000O0O00O .iterrows ():#line:1700
					if "分隔符"not in O00O000OOO00OO000 ["条目"]:#line:1701
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1702
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的"]+O0OO00OOOOOOO0O0O #line:1703
					if "分隔符"not in O00O000OOO00OO000 ["条目"]and int (O00O000OOO00OO000 ["详细描述T"])>=2 :#line:1705
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1706
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的（高敏）"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的（高敏）"]+O0OO00OOOOOOO0O0O #line:1707
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O00OO0O0O00O0O00O .iterrows ():#line:1709
				if str (O00O000OOO00OO000 ["条目"]).strip ()not in str (O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的"])and "分隔符"not in str (O00O000OOO00OO000 ["条目"]):#line:1710
					O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1711
					O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的"]+O0OO00OOOOOOO0O0O #line:1712
					if int (O00O000OOO00OO000 ["详细描述T"])>=3 :#line:1713
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]+"！"#line:1714
					if int (O00O000OOO00OO000 ["详细描述T"])>=5 :#line:1715
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]+"●"#line:1716
				if str (O00O000OOO00OO000 ["条目"]).strip ()not in str (O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的（高敏）"])and "分隔符"not in str (O00O000OOO00OO000 ["条目"])and int (O00O000OOO00OO000 ["详细描述T"])>=2 :#line:1718
					O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1719
					O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的（高敏）"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的（高敏）"]+O0OO00OOOOOOO0O0O #line:1720
		O000000OO0O0OO0OO ["疑似新的"]="{"+O000000OO0O0OO0OO ["疑似新的"]+"}"#line:1722
		O000000OO0O0OO0OO ["疑似旧的"]="{"+O000000OO0O0OO0OO ["疑似旧的"]+"}"#line:1723
		O000000OO0O0OO0OO ["所有不良反应"]="{"+O000000OO0O0OO0OO ["所有不良反应"]+"}"#line:1724
		O000000OO0O0OO0OO ["疑似新的（高敏）"]="{"+O000000OO0O0OO0OO ["疑似新的（高敏）"]+"}"#line:1725
		O000000OO0O0OO0OO ["疑似旧的（高敏）"]="{"+O000000OO0O0OO0OO ["疑似旧的（高敏）"]+"}"#line:1726
		O000000OO0O0OO0OO =O000000OO0O0OO0OO .rename (columns ={"器械待评价(药品新的报告比例)":"新的报告比例"})#line:1728
		O000000OO0O0OO0OO =O000000OO0O0OO0OO .rename (columns ={"严重伤害待评价比例(药品严重中新的比例)":"严重报告中新的比例"})#line:1729
		O000000OO0O0OO0OO ["报表类型"]="dfx_zhenghao"#line:1730
		TABLE_tree_Level_2 (O000000OO0O0OO0OO .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,O00OO000O0O0O0O00 )#line:1731
	if OOO00O000OO00OO00 =="品种":#line:1732
		root .attributes ("-topmost",True )#line:1733
		root .attributes ("-topmost",False )#line:1734
		O0OO00O0OOO000OO0 =O00OO000O0O0O0O00 .groupby (["产品类别","产品名称"]).agg (计数 =("报告编码","nunique")).reset_index ()#line:1735
		O000000OO0O0OO0OO =O0OO00O0OOO000OO0 .drop_duplicates ("产品名称").copy ()#line:1736
		O000000OO0O0OO0OO ["产品名称"]=O000000OO0O0OO0OO ["产品名称"].str .replace ("*","",regex =False )#line:1737
		O000000OO0O0OO0OO ["所有不良反应"]=""#line:1738
		O000000OO0O0OO0OO ["关注建议"]=""#line:1739
		O000000OO0O0OO0OO ["疑似新的"]=""#line:1740
		O000000OO0O0OO0OO ["疑似旧的"]=""#line:1741
		O000000OO0O0OO0OO ["疑似新的（高敏）"]=""#line:1742
		O000000OO0O0OO0OO ["疑似旧的（高敏）"]=""#line:1743
		O0OO0O0OOO00OO000 =1 #line:1744
		O00O0OOOO0OO0OOOO =int (len (O000000OO0O0OO0OO ))#line:1745
		for O0O0OOO0OO0O0OO0O ,O0OOOO000O00OOO0O in O000000OO0O0OO0OO .iterrows ():#line:1748
			O00O0O00OO0OO00O0 =O00OO000O0O0O0O00 [(O00OO000O0O0O0O00 ["产品名称"]==O0OOOO000O00OOO0O ["产品名称"])]#line:1750
			OO0OOO0O0OOO0OOO0 =O00O0O00OO0OO00O0 .loc [O00O0O00OO0OO00O0 ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1752
			O00O0O0OO00O000O0 =O00O0O00OO0OO00O0 .loc [~O00O0O00OO0OO00O0 ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1753
			O0OO00000O0OO00O0 =O00O000O0000OOOOO (O00O0O00OO0OO00O0 )#line:1754
			O00OO0O0O00O0O00O =O00O000O0000OOOOO (OO0OOO0O0OOO0OOO0 )#line:1755
			O000OOOO000O0O00O =O00O000O0000OOOOO (O00O0O0OO00O000O0 )#line:1756
			PROGRAM_change_schedule (O0OO0O0OOO00OO000 ,O00O0OOOO0OO0OOOO )#line:1757
			O0OO0O0OOO00OO000 =O0OO0O0OOO00OO000 +1 #line:1758
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O0OO00000O0OO00O0 .iterrows ():#line:1760
					if "分隔符"not in O00O000OOO00OO000 ["条目"]:#line:1761
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1762
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"所有不良反应"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"所有不良反应"]+O0OO00OOOOOOO0O0O #line:1763
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O000OOOO000O0O00O .iterrows ():#line:1766
					if "分隔符"not in O00O000OOO00OO000 ["条目"]:#line:1767
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1768
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的"]+O0OO00OOOOOOO0O0O #line:1769
					if "分隔符"not in O00O000OOO00OO000 ["条目"]and int (O00O000OOO00OO000 ["详细描述T"])>=2 :#line:1771
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1772
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的（高敏）"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的（高敏）"]+O0OO00OOOOOOO0O0O #line:1773
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O00OO0O0O00O0O00O .iterrows ():#line:1775
				if str (O00O000OOO00OO000 ["条目"]).strip ()not in str (O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的"])and "分隔符"not in str (O00O000OOO00OO000 ["条目"]):#line:1776
					O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1777
					O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的"]+O0OO00OOOOOOO0O0O #line:1778
					if int (O00O000OOO00OO000 ["详细描述T"])>=3 :#line:1779
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]+"！"#line:1780
					if int (O00O000OOO00OO000 ["详细描述T"])>=5 :#line:1781
						O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"关注建议"]+"●"#line:1782
				if str (O00O000OOO00OO000 ["条目"]).strip ()not in str (O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似旧的（高敏）"])and "分隔符"not in str (O00O000OOO00OO000 ["条目"])and int (O00O000OOO00OO000 ["详细描述T"])>=2 :#line:1784
					O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1785
					O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的（高敏）"]=O000000OO0O0OO0OO .loc [O0O0OOO0OO0O0OO0O ,"疑似新的（高敏）"]+O0OO00OOOOOOO0O0O #line:1786
		O000000OO0O0OO0OO ["疑似新的"]="{"+O000000OO0O0OO0OO ["疑似新的"]+"}"#line:1788
		O000000OO0O0OO0OO ["疑似旧的"]="{"+O000000OO0O0OO0OO ["疑似旧的"]+"}"#line:1789
		O000000OO0O0OO0OO ["所有不良反应"]="{"+O000000OO0O0OO0OO ["所有不良反应"]+"}"#line:1790
		O000000OO0O0OO0OO ["疑似新的（高敏）"]="{"+O000000OO0O0OO0OO ["疑似新的（高敏）"]+"}"#line:1791
		O000000OO0O0OO0OO ["疑似旧的（高敏）"]="{"+O000000OO0O0OO0OO ["疑似旧的（高敏）"]+"}"#line:1792
		O000000OO0O0OO0OO ["报表类型"]="dfx_chanpin"#line:1793
		TABLE_tree_Level_2 (O000000OO0O0OO0OO .sort_values (by ="计数",ascending =[False ],na_position ="last"),1 ,O00OO000O0O0O0O00 )#line:1794
	if OOO00O000OO00OO00 =="页面":#line:1796
		OO0O000O00O0OOO0O =""#line:1797
		O00O000O0O00O0OOO =""#line:1798
		OO0OOO0O0OOO0OOO0 =O00OO000O0O0O0O00 .loc [O00OO000O0O0O0O00 ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1799
		O00O0O0OO00O000O0 =O00OO000O0O0O0O00 .loc [~O00OO000O0O0O0O00 ["报告类型-新的"].str .contains ("新",na =False )].copy ()#line:1800
		O00OO0O0O00O0O00O =O00O000O0000OOOOO (OO0OOO0O0OOO0OOO0 )#line:1801
		O000OOOO000O0O00O =O00O000O0000OOOOO (O00O0O0OO00O000O0 )#line:1802
		if 1 ==1 :#line:1803
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O000OOOO000O0O00O .iterrows ():#line:1804
					if "分隔符"not in O00O000OOO00OO000 ["条目"]:#line:1805
						O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1806
						O00O000O0O00O0OOO =O00O000O0O00O0OOO +O0OO00OOOOOOO0O0O #line:1807
			for O0O000OO0OO0O0OOO ,O00O000OOO00OO000 in O00OO0O0O00O0O00O .iterrows ():#line:1808
				if str (O00O000OOO00OO000 ["条目"]).strip ()not in O00O000O0O00O0OOO and "分隔符"not in str (O00O000OOO00OO000 ["条目"]):#line:1809
					O0OO00OOOOOOO0O0O ="'"+str (O00O000OOO00OO000 ["条目"])+"':"+str (O00O000OOO00OO000 ["详细描述T"])+","#line:1810
					OO0O000O00O0OOO0O =OO0O000O00O0OOO0O +O0OO00OOOOOOO0O0O #line:1811
		O00O000O0O00O0OOO ="{"+O00O000O0O00O0OOO +"}"#line:1812
		OO0O000O00O0OOO0O ="{"+OO0O000O00O0OOO0O +"}"#line:1813
		OOOO0OOOO000OOO00 ="\n可能是新的不良反应：\n\n"+OO0O000O00O0OOO0O +"\n\n\n可能不是新的不良反应：\n\n"+O00O000O0O00O0OOO #line:1814
		TOOLS_view_dict (OOOO0OOOO000OOO00 ,1 )#line:1815
def TOOLS_strdict_to_pd (O0OO00OO0000O0OO0 ):#line:1817
	""#line:1818
	return pd .DataFrame .from_dict (eval (O0OO00OO0000O0OO0 ),orient ="index",columns =["content"]).reset_index ()#line:1819
def TOOLS_xuanze (O0OOOO0OO0OOO0000 ,OOOO000O0O0O000OO ):#line:1821
    ""#line:1822
    if OOOO000O0O0O000OO ==0 :#line:1823
        O00O0O000OOOO00O0 =pd .read_excel (filedialog .askopenfilename (filetypes =[("XLS",".xls")]),sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1824
    else :#line:1825
        O00O0O000OOOO00O0 =pd .read_excel ("配置表/0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1826
    O0OOOO0OO0OOO0000 ["temppr"]=""#line:1827
    for O0000OO00O00O00OO in O00O0O000OOOO00O0 .columns .tolist ():#line:1828
        O0OOOO0OO0OOO0000 ["temppr"]=O0OOOO0OO0OOO0000 ["temppr"]+"----"+O0OOOO0OO0OOO0000 [O0000OO00O00O00OO ]#line:1829
    OO0O00O00OO0O0O00 ="测试字段MMMMM"#line:1830
    for O0000OO00O00O00OO in O00O0O000OOOO00O0 .columns .tolist ():#line:1831
        for O00O00OOO00O0000O in O00O0O000OOOO00O0 [O0000OO00O00O00OO ].drop_duplicates ():#line:1833
            if O00O00OOO00O0000O :#line:1834
                OO0O00O00OO0O0O00 =OO0O00O00OO0O0O00 +"|"+str (O00O00OOO00O0000O )#line:1835
    O0OOOO0OO0OOO0000 =O0OOOO0OO0OOO0000 .loc [O0OOOO0OO0OOO0000 ["temppr"].str .contains (OO0O00O00OO0O0O00 ,na =False )].copy ()#line:1836
    del O0OOOO0OO0OOO0000 ["temppr"]#line:1837
    O0OOOO0OO0OOO0000 =O0OOOO0OO0OOO0000 .reset_index (drop =True )#line:1838
    TABLE_tree_Level_2 (O0OOOO0OO0OOO0000 ,0 ,O0OOOO0OO0OOO0000 )#line:1840
def TOOLS_add_c (O0OO00O00O000OOOO ,OO00O00O0O0OOO000 ):#line:1842
			O0OO00O00O000OOOO ["关键字查找列o"]=""#line:1843
			for O0OO00O00OO00O0O0 in TOOLS_get_list (OO00O00O0O0OOO000 ["查找列"]):#line:1844
				O0OO00O00O000OOOO ["关键字查找列o"]=O0OO00O00O000OOOO ["关键字查找列o"]+O0OO00O00O000OOOO [O0OO00O00OO00O0O0 ].astype ("str")#line:1845
			if OO00O00O0O0OOO000 ["条件"]=="等于":#line:1846
				O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO [OO00O00O0O0OOO000 ["查找列"]].astype (str )==str (OO00O00O0O0OOO000 ["条件值"])),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1847
			if OO00O00O0O0OOO000 ["条件"]=="大于":#line:1848
				O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO [OO00O00O0O0OOO000 ["查找列"]].astype (float )>OO00O00O0O0OOO000 ["条件值"]),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1849
			if OO00O00O0O0OOO000 ["条件"]=="小于":#line:1850
				O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO [OO00O00O0O0OOO000 ["查找列"]].astype (float )<OO00O00O0O0OOO000 ["条件值"]),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1851
			if OO00O00O0O0OOO000 ["条件"]=="介于":#line:1852
				OO0OO0O00OOOOOOO0 =TOOLS_get_list (OO00O00O0O0OOO000 ["条件值"])#line:1853
				O0OO00O00O000OOOO .loc [((O0OO00O00O000OOOO [OO00O00O0O0OOO000 ["查找列"]].astype (float )<float (OO0OO0O00OOOOOOO0 [1 ]))&(O0OO00O00O000OOOO [OO00O00O0O0OOO000 ["查找列"]].astype (float )>float (OO0OO0O00OOOOOOO0 [0 ]))),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1854
			if OO00O00O0O0OOO000 ["条件"]=="不含":#line:1855
				O0OO00O00O000OOOO .loc [(~O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OO00O00O0O0OOO000 ["条件值"])),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1856
			if OO00O00O0O0OOO000 ["条件"]=="包含":#line:1857
				O0OO00O00O000OOOO .loc [O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OO00O00O0O0OOO000 ["条件值"],na =False ),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1858
			if OO00O00O0O0OOO000 ["条件"]=="同时包含":#line:1859
				OOOO00OO000000OOO =TOOLS_get_list0 (OO00O00O0O0OOO000 ["条件值"],0 )#line:1860
				if len (OOOO00OO000000OOO )==1 :#line:1861
				    O0OO00O00O000OOOO .loc [O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [0 ],na =False ),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1862
				if len (OOOO00OO000000OOO )==2 :#line:1863
				    O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [0 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [1 ],na =False )),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1864
				if len (OOOO00OO000000OOO )==3 :#line:1865
				    O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [0 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [1 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [2 ],na =False )),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1866
				if len (OOOO00OO000000OOO )==4 :#line:1867
				    O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [0 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [1 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [2 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [3 ],na =False )),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1868
				if len (OOOO00OO000000OOO )==5 :#line:1869
				    O0OO00O00O000OOOO .loc [(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [0 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [1 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [2 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [3 ],na =False ))&(O0OO00O00O000OOOO ["关键字查找列o"].str .contains (OOOO00OO000000OOO [4 ],na =False )),OO00O00O0O0OOO000 ["赋值列名"]]=OO00O00O0O0OOO000 ["赋值"]#line:1870
			return O0OO00O00O000OOOO #line:1871
def TOOL_guizheng (O00O000O000O00000 ,O00O0O0OOOOO00O00 ,O0OOO0OO00OO00000 ):#line:1874
	""#line:1875
	if O00O0O0OOOOO00O00 ==0 :#line:1876
		O000000OOOOOOOOOO =pd .read_excel (filedialog .askopenfilename (filetypes =[("XLSX",".xlsx")]),sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1877
		O000000OOOOOOOOOO =O000000OOOOOOOOOO [(O000000OOOOOOOOOO ["执行标记"]=="是")].reset_index ()#line:1878
		for O00O0OO0OO00OOO00 ,OO0OO0O0OOO0OO0OO in O000000OOOOOOOOOO .iterrows ():#line:1879
			O00O000O000O00000 =TOOLS_add_c (O00O000O000O00000 ,OO0OO0O0OOO0OO0OO )#line:1880
		del O00O000O000O00000 ["关键字查找列o"]#line:1881
	elif O00O0O0OOOOO00O00 ==1 :#line:1883
		O000000OOOOOOOOOO =pd .read_excel ("配置表/0（范例）数据规整.xlsx",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1884
		O000000OOOOOOOOOO =O000000OOOOOOOOOO [(O000000OOOOOOOOOO ["执行标记"]=="是")].reset_index ()#line:1885
		for O00O0OO0OO00OOO00 ,OO0OO0O0OOO0OO0OO in O000000OOOOOOOOOO .iterrows ():#line:1886
			O00O000O000O00000 =TOOLS_add_c (O00O000O000O00000 ,OO0OO0O0OOO0OO0OO )#line:1887
		del O00O000O000O00000 ["关键字查找列o"]#line:1888
	elif O00O0O0OOOOO00O00 =="课题":#line:1890
		O000000OOOOOOOOOO =pd .read_excel ("配置表/0（范例）品类规整.xlsx",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1891
		O000000OOOOOOOOOO =O000000OOOOOOOOOO [(O000000OOOOOOOOOO ["执行标记"]=="是")].reset_index ()#line:1892
		for O00O0OO0OO00OOO00 ,OO0OO0O0OOO0OO0OO in O000000OOOOOOOOOO .iterrows ():#line:1893
			O00O000O000O00000 =TOOLS_add_c (O00O000O000O00000 ,OO0OO0O0OOO0OO0OO )#line:1894
		del O00O000O000O00000 ["关键字查找列o"]#line:1895
	elif O00O0O0OOOOO00O00 ==2 :#line:1897
		text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:1898
		OOO000O0O0O00OOOO =pd .read_excel ("配置表/0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:1899
		OO00OO0OOO00OOO0O =pd .read_excel ("配置表/0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:1900
		O0000OO0O00000000 =pd .read_excel ("配置表/0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:1901
		for O00O0OO0OO00OOO00 ,OO0OO0O0OOO0OO0OO in OOO000O0O0O00OOOO .iterrows ():#line:1902
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["曾用名1"]),"单位名称"]=OO0OO0O0OOO0OO0OO ["单位名称"]#line:1903
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["曾用名2"]),"单位名称"]=OO0OO0O0OOO0OO0OO ["单位名称"]#line:1904
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["曾用名3"]),"单位名称"]=OO0OO0O0OOO0OO0OO ["单位名称"]#line:1905
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["曾用名4"]),"单位名称"]=OO0OO0O0OOO0OO0OO ["单位名称"]#line:1906
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["曾用名5"]),"单位名称"]=OO0OO0O0OOO0OO0OO ["单位名称"]#line:1907
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["单位名称"]),"医疗机构类别"]=OO0OO0O0OOO0OO0OO ["医疗机构类别"]#line:1909
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["单位名称"]),"监测机构"]=OO0OO0O0OOO0OO0OO ["监测机构"]#line:1910
		for O00O0OO0OO00OOO00 ,OO0OO0O0OOO0OO0OO in OO00OO0OOO00OOO0O .iterrows ():#line:1912
			O00O000O000O00000 .loc [(O00O000O000O00000 ["监测机构"]==OO0OO0O0OOO0OO0OO ["曾用名1"]),"监测机构"]=OO0OO0O0OOO0OO0OO ["监测机构"]#line:1913
			O00O000O000O00000 .loc [(O00O000O000O00000 ["监测机构"]==OO0OO0O0OOO0OO0OO ["曾用名2"]),"监测机构"]=OO0OO0O0OOO0OO0OO ["监测机构"]#line:1914
			O00O000O000O00000 .loc [(O00O000O000O00000 ["监测机构"]==OO0OO0O0OOO0OO0OO ["曾用名3"]),"监测机构"]=OO0OO0O0OOO0OO0OO ["监测机构"]#line:1915
		for O00O0O000O00OO0OO in O0000OO0O00000000 ["地市列表"]:#line:1917
			O00O000O000O00000 .loc [(O00O000O000O00000 ["上报单位所属地区"].str .contains (O00O0O000O00OO0OO ,na =False )),"市级监测机构"]=O00O0O000O00OO0OO #line:1918
		O00O000O000O00000 .loc [(O00O000O000O00000 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:1921
		O00O000O000O00000 ["市级监测机构"]=O00O000O000O00000 ["市级监测机构"].fillna ("-未规整的-")#line:1922
	elif O00O0O0OOOOO00O00 ==3 :#line:1924
			O0O0OOO000O0OOO0O =(O00O000O000O00000 .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]).aggregate ({"报告编码":"count"}).reset_index ())#line:1929
			O0O0OOO000O0OOO0O =O0O0OOO000O0OOO0O .sort_values (by =["注册证编号/曾用注册证编号","报告编码"],ascending =[False ,False ],na_position ="last").reset_index ()#line:1932
			text .insert (END ,"\n开展产品名称规整..")#line:1933
			del O0O0OOO000O0OOO0O ["报告编码"]#line:1934
			O0O0OOO000O0OOO0O =O0O0OOO000O0OOO0O .drop_duplicates (["注册证编号/曾用注册证编号"])#line:1935
			O00O000O000O00000 =O00O000O000O00000 .rename (columns ={"上市许可持有人名称":"上市许可持有人名称（规整前）","产品类别":"产品类别（规整前）","产品名称":"产品名称（规整前）"})#line:1937
			O00O000O000O00000 =pd .merge (O00O000O000O00000 ,O0O0OOO000O0OOO0O ,on =["注册证编号/曾用注册证编号"],how ="left")#line:1938
	elif O00O0O0OOOOO00O00 ==4 :#line:1940
		text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:1941
		OO00OO0OOO00OOO0O =pd .read_excel ("配置表/0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:1942
		for O00O0OO0OO00OOO00 ,OO0OO0O0OOO0OO0OO in OO00OO0OOO00OOO0O .iterrows ():#line:1944
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["中文全称"]),"监测机构"]=OO0OO0O0OOO0OO0OO ["归属地区"]#line:1945
			O00O000O000O00000 .loc [(O00O000O000O00000 ["单位名称"]==OO0OO0O0OOO0OO0OO ["中文全称"]),"市级监测机构"]=OO0OO0O0OOO0OO0OO ["地市"]#line:1946
		O00O000O000O00000 ["监测机构"]=O00O000O000O00000 ["监测机构"].fillna ("未规整")#line:1947
		O00O000O000O00000 ["市级监测机构"]=O00O000O000O00000 ["市级监测机构"].fillna ("未规整")#line:1948
	if O0OOO0OO00OO00000 ==True :#line:1949
		return O00O000O000O00000 #line:1950
	else :#line:1951
		TABLE_tree_Level_2 (O00O000O000O00000 ,0 ,O00O000O000O00000 )#line:1952
def TOOL_person (OO000O0OO0O000000 ):#line:1954
	""#line:1955
	O0OOOOOO0000O0O0O =pd .read_excel ("配置表/0（范例）注册单位.xlsx",sheet_name ="专家列表",header =0 ,index_col =0 ,).reset_index ()#line:1956
	for OO0OOOO0OO0OO0000 ,O0O000OOOO00OO00O in O0OOOOOO0000O0O0O .iterrows ():#line:1957
		OO000O0OO0O000000 .loc [(OO000O0OO0O000000 ["市级监测机构"]==O0O000OOOO00OO00O ["市级监测机构"]),"评表人员"]=O0O000OOOO00OO00O ["评表人员"]#line:1958
		OO000O0OO0O000000 ["评表人员"]=OO000O0OO0O000000 ["评表人员"].fillna ("未规整")#line:1959
		O0O0O0O0OOOO0OOO0 =OO000O0OO0O000000 .groupby (["评表人员"]).agg (报告数量 =("报告编码","nunique"),地市 =("市级监测机构",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:1963
	TABLE_tree_Level_2 (O0O0O0O0OOOO0OOO0 ,0 ,O0O0O0O0OOOO0OOO0 )#line:1964
def TOOLS_get_list (OOOO0O0O00O00000O ):#line:1966
    ""#line:1967
    OOOO0O0O00O00000O =str (OOOO0O0O00O00000O )#line:1968
    O0O000OO0O0O00O0O =[]#line:1969
    O0O000OO0O0O00O0O .append (OOOO0O0O00O00000O )#line:1970
    O0O000OO0O0O00O0O =",".join (O0O000OO0O0O00O0O )#line:1971
    O0O000OO0O0O00O0O =O0O000OO0O0O00O0O .split ("|")#line:1972
    O0O000O0OO0O0OO00 =O0O000OO0O0O00O0O [:]#line:1973
    O0O000OO0O0O00O0O =list (set (O0O000OO0O0O00O0O ))#line:1974
    O0O000OO0O0O00O0O .sort (key =O0O000O0OO0O0OO00 .index )#line:1975
    return O0O000OO0O0O00O0O #line:1976
def TOOLS_get_list0 (OOOO0OO0O000OO0OO ,O000000OO00OO000O ,*O0000OOOOO000O0O0 ):#line:1978
    ""#line:1979
    OOOO0OO0O000OO0OO =str (OOOO0OO0O000OO0OO )#line:1980
    if pd .notnull (OOOO0OO0O000OO0OO ):#line:1982
        try :#line:1983
            if "use("in str (OOOO0OO0O000OO0OO ):#line:1984
                OOOO0OO0OOO00O0OO =OOOO0OO0O000OO0OO #line:1985
                OOOOO0O0O000O0O0O =re .compile (r"[(](.*?)[)]",re .S )#line:1986
                OO0O000OOOO0O000O =re .findall (OOOOO0O0O000O0O0O ,OOOO0OO0OOO00O0OO )#line:1987
                OOOOO00O0O00O00OO =[]#line:1988
                if ").list"in OOOO0OO0O000OO0OO :#line:1989
                    O000OO0O0O0OO0000 ="配置表/"+str (OO0O000OOOO0O000O [0 ])+".xls"#line:1990
                    OO00OOOOOO0OOOOOO =pd .read_excel (O000OO0O0O0OO0000 ,sheet_name =OO0O000OOOO0O000O [0 ],header =0 ,index_col =0 ).reset_index ()#line:1993
                    OO00OOOOOO0OOOOOO ["检索关键字"]=OO00OOOOOO0OOOOOO ["检索关键字"].astype (str )#line:1994
                    OOOOO00O0O00O00OO =OO00OOOOOO0OOOOOO ["检索关键字"].tolist ()+OOOOO00O0O00O00OO #line:1995
                if ").file"in OOOO0OO0O000OO0OO :#line:1996
                    OOOOO00O0O00O00OO =O000000OO00OO000O [OO0O000OOOO0O000O [0 ]].astype (str ).tolist ()+OOOOO00O0O00O00OO #line:1998
                try :#line:2001
                    if "报告类型-新的"in O000000OO00OO000O .columns :#line:2002
                        OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2003
                        OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split (";")#line:2004
                        OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2005
                        OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split ("；")#line:2006
                        OOOOO00O0O00O00OO =[O000OO0OO000OOOOO .replace ("（严重）","")for O000OO0OO000OOOOO in OOOOO00O0O00O00OO ]#line:2007
                        OOOOO00O0O00O00OO =[OO000OOOOOO0O0OO0 .replace ("（一般）","")for OO000OOOOOO0O0OO0 in OOOOO00O0O00O00OO ]#line:2008
                except :#line:2009
                    pass #line:2010
                OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2013
                OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split ("、")#line:2014
                OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2015
                OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split ("，")#line:2016
                OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2017
                OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split (",")#line:2018
                O00OOO0OO0OOO000O =OOOOO00O0O00O00OO [:]#line:2020
                try :#line:2021
                    if O0000OOOOO000O0O0 [0 ]==1000 :#line:2022
                      pass #line:2023
                except :#line:2024
                      OOOOO00O0O00O00OO =list (set (OOOOO00O0O00O00OO ))#line:2025
                OOOOO00O0O00O00OO .sort (key =O00OOO0OO0OOO000O .index )#line:2026
            else :#line:2028
                OOOO0OO0O000OO0OO =str (OOOO0OO0O000OO0OO )#line:2029
                OOOOO00O0O00O00OO =[]#line:2030
                OOOOO00O0O00O00OO .append (OOOO0OO0O000OO0OO )#line:2031
                OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2032
                OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split ("、")#line:2033
                OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2034
                OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split ("，")#line:2035
                OOOOO00O0O00O00OO =",".join (OOOOO00O0O00O00OO )#line:2036
                OOOOO00O0O00O00OO =OOOOO00O0O00O00OO .split (",")#line:2037
                O00OOO0OO0OOO000O =OOOOO00O0O00O00OO [:]#line:2039
                try :#line:2040
                    if O0000OOOOO000O0O0 [0 ]==1000 :#line:2041
                      OOOOO00O0O00O00OO =list (set (OOOOO00O0O00O00OO ))#line:2042
                except :#line:2043
                      pass #line:2044
                OOOOO00O0O00O00OO .sort (key =O00OOO0OO0OOO000O .index )#line:2045
                OOOOO00O0O00O00OO .sort (key =O00OOO0OO0OOO000O .index )#line:2046
        except ValueError2 :#line:2048
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:2049
            return False #line:2050
    return OOOOO00O0O00O00OO #line:2052
def TOOLS_easyread2 (OO0OOOOOOO0OOO00O ):#line:2054
    ""#line:2055
    OO0OOOOOOO0OOO00O ["分隔符"]="●"#line:2057
    OO0OOOOOOO0OOO00O ["上报机构描述"]=(OO0OOOOOOO0OOO00O ["使用过程"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["事件原因分析"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["事件原因分析描述"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["初步处置情况"].astype ("str"))#line:2066
    OO0OOOOOOO0OOO00O ["持有人处理描述"]=(OO0OOOOOOO0OOO00O ["关联性评价"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["调查情况"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["事件原因分析"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["具体控制措施"].astype ("str")+OO0OOOOOOO0OOO00O ["分隔符"]+OO0OOOOOOO0OOO00O ["未采取控制措施原因"].astype ("str"))#line:2077
    OOOOOO00000O00OOO =OO0OOOOOOO0OOO00O [["报告编码","事件发生日期","报告日期","单位名称","产品名称","注册证编号/曾用注册证编号","产品批号","型号","规格","上市许可持有人名称","管理类别","伤害","伤害表现","器械故障表现","上报机构描述","持有人处理描述","经营企业使用单位报告状态","监测机构","产品类别","医疗机构类别","年龄","年龄类型","性别"]]#line:2104
    OOOOOO00000O00OOO =OOOOOO00000O00OOO .sort_values (by =["事件发生日期"],ascending =[False ],na_position ="last",)#line:2109
    OOOOOO00000O00OOO =OOOOOO00000O00OOO .rename (columns ={"报告编码":"规整编码"})#line:2110
    return OOOOOO00000O00OOO #line:2111
def fenci0 (OOO00OO00O00O00O0 ):#line:2114
	""#line:2115
	OO0OO000000OOOOOO =Toplevel ()#line:2116
	OO0OO000000OOOOOO .title ('词频统计')#line:2117
	OOO0000O00000OO0O =OO0OO000000OOOOOO .winfo_screenwidth ()#line:2118
	OOOOOOOO0OOO00OOO =OO0OO000000OOOOOO .winfo_screenheight ()#line:2120
	OO00000O000000O0O =400 #line:2122
	O00O00OO0O000000O =120 #line:2123
	OOOO0O00OOO00O0O0 =(OOO0000O00000OO0O -OO00000O000000O0O )/2 #line:2125
	OO00OO0OO0O00O00O =(OOOOOOOO0OOO00OOO -O00O00OO0O000000O )/2 #line:2126
	OO0OO000000OOOOOO .geometry ("%dx%d+%d+%d"%(OO00000O000000O0O ,O00O00OO0O000000O ,OOOO0O00OOO00O0O0 ,OO00OO0OO0O00O00O ))#line:2127
	O00OO00O000O0O00O =Label (OO0OO000000OOOOOO ,text ="配置文件：")#line:2128
	O00OO00O000O0O00O .pack ()#line:2129
	O00O00OOO0O0OO0OO =Label (OO0OO000000OOOOOO ,text ="需要分词的列：")#line:2130
	O0O0OO000O0000OOO =Entry (OO0OO000000OOOOOO ,width =80 )#line:2132
	O0O0OO000O0000OOO .insert (0 ,"配置表/0（范例）中文分词工作文件.xls")#line:2133
	O00O0OO0OOOO000O0 =Entry (OO0OO000000OOOOOO ,width =80 )#line:2134
	O00O0OO0OOOO000O0 .insert (0 ,"器械故障表现，伤害表现")#line:2135
	O0O0OO000O0000OOO .pack ()#line:2136
	O00O00OOO0O0OO0OO .pack ()#line:2137
	O00O0OO0OOOO000O0 .pack ()#line:2138
	O000O0O0OOO000O0O =LabelFrame (OO0OO000000OOOOOO )#line:2139
	O0OO00000O0OO0000 =Button (O000O0O0OOO000O0O ,text ="确定",width =10 ,command =lambda :PROGRAM_thread_it (tree_Level_2 ,fenci (O0O0OO000O0000OOO .get (),O00O0OO0OOOO000O0 .get (),OOO00OO00O00O00O0 ),1 ,0 ))#line:2140
	O0OO00000O0OO0000 .pack (side =LEFT ,padx =1 ,pady =1 )#line:2141
	O000O0O0OOO000O0O .pack ()#line:2142
def fenci (O0OOOOO00OO0000OO ,OOO000O0OO0OOOO0O ,O0OOO000OO0O0OOO0 ):#line:2144
    ""#line:2145
    import glob #line:2146
    import jieba #line:2147
    import random #line:2148
    try :#line:2150
        O0OOO000OO0O0OOO0 =O0OOO000OO0O0OOO0 .drop_duplicates (["报告编码"])#line:2151
    except :#line:2152
        pass #line:2153
    def O0OO0O0OOOO0OOO00 (O00OOOO0OO0OO0000 ,O0OOO00OOOO0O000O ):#line:2154
        OO0O000OO000OO0O0 ={}#line:2155
        for OOO0OO0OOO00OOO0O in O00OOOO0OO0OO0000 :#line:2156
            OO0O000OO000OO0O0 [OOO0OO0OOO00OOO0O ]=OO0O000OO000OO0O0 .get (OOO0OO0OOO00OOO0O ,0 )+1 #line:2157
        return sorted (OO0O000OO000OO0O0 .items (),key =lambda OO0000OO00O00O0O0 :OO0000OO00O00O0O0 [1 ],reverse =True )[:O0OOO00OOOO0O000O ]#line:2158
    O0O0O0OOOOO000000 =pd .read_excel (O0OOOOO00OO0000OO ,sheet_name ="初始化",header =0 ,index_col =0 ).reset_index ()#line:2162
    OO0O0O000OOO0OO0O =O0O0O0OOOOO000000 .iloc [0 ,2 ]#line:2164
    O0000000OOOOOOO0O =pd .read_excel (O0OOOOO00OO0000OO ,sheet_name ="停用词",header =0 ,index_col =0 ).reset_index ()#line:2167
    O0000000OOOOOOO0O ["停用词"]=O0000000OOOOOOO0O ["停用词"].astype (str )#line:2169
    OOOOOOOOOO00OO000 =[OOO0OOO0OO0O00OO0 .strip ()for OOO0OOO0OO0O00OO0 in O0000000OOOOOOO0O ["停用词"]]#line:2170
    O00O0OOOOOOOO0000 =pd .read_excel (O0OOOOO00OO0000OO ,sheet_name ="本地词库",header =0 ,index_col =0 ).reset_index ()#line:2173
    O0OOO000O0O0O0OO0 =O00O0OOOOOOOO0000 ["本地词库"]#line:2174
    jieba .load_userdict (O0OOO000O0O0O0OO0 )#line:2175
    O0O000O0O00O0OO0O =""#line:2178
    OO0OOO0OO00OO0000 =get_list0 (OOO000O0OO0OOOO0O ,O0OOO000OO0O0OOO0 )#line:2181
    try :#line:2182
        for OOOO0O00OO0O000O0 in OO0OOO0OO00OO0000 :#line:2183
            for OO0OO000O000OOO00 in O0OOO000OO0O0OOO0 [OOOO0O00OO0O000O0 ]:#line:2184
                O0O000O0O00O0OO0O =O0O000O0O00O0OO0O +str (OO0OO000O000OOO00 )#line:2185
    except :#line:2186
        text .insert (END ,"分词配置文件未正确设置，将对整个表格进行分词。")#line:2187
        for OOOO0O00OO0O000O0 in O0OOO000OO0O0OOO0 .columns .tolist ():#line:2188
            for OO0OO000O000OOO00 in O0OOO000OO0O0OOO0 [OOOO0O00OO0O000O0 ]:#line:2189
                O0O000O0O00O0OO0O =O0O000O0O00O0OO0O +str (OO0OO000O000OOO00 )#line:2190
    OO0OO00O0OOOO000O =[]#line:2191
    OO0OO00O0OOOO000O =OO0OO00O0OOOO000O +[O0OO000O0O0000O0O for O0OO000O0O0000O0O in jieba .cut (O0O000O0O00O0OO0O )if O0OO000O0O0000O0O not in OOOOOOOOOO00OO000 ]#line:2192
    OO0O0OOO00OO0O00O =dict (O0OO0O0OOOO0OOO00 (OO0OO00O0OOOO000O ,OO0O0O000OOO0OO0O ))#line:2193
    O0O00O0O0OOO00OOO =pd .DataFrame ([OO0O0OOO00OO0O00O ]).T #line:2194
    O0O00O0O0OOO00OOO =O0O00O0O0OOO00OOO .reset_index ()#line:2195
    return O0O00O0O0OOO00OOO #line:2196
def TOOLS_time (OO0O00OOO00OO00O0 ,OOOO000O0O00O0000 ,O000O0OOOOOOOOO0O ):#line:2198
	""#line:2199
	OOO00OO0O00000O00 =OO0O00OOO00OO00O0 .groupby ([OOOO000O0O00O0000 ]).agg (报告总数 =("报告编码","nunique"),严重伤害数 =("伤害",lambda OOOOO0OO000O00OO0 :STAT_countpx (OOOOO0OO000O00OO0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0O0OOO000O0000 :STAT_countpx (O0O0O0OOO000O0000 .values ,"死亡")),).sort_values (by =OOOO000O0O00O0000 ,ascending =[True ],na_position ="last").reset_index ()#line:2204
	OOO00OO0O00000O00 =OOO00OO0O00000O00 .set_index (OOOO000O0O00O0000 )#line:2205
	OOO00OO0O00000O00 =OOO00OO0O00000O00 .resample ('D').asfreq (fill_value =0 )#line:2207
	OOO00OO0O00000O00 ["time"]=OOO00OO0O00000O00 .index .values #line:2209
	OOO00OO0O00000O00 ["time"]=pd .to_datetime (OOO00OO0O00000O00 ["time"],format ="%Y/%m/%d").dt .date #line:2210
	if O000O0OOOOOOOOO0O ==1 :#line:2212
		return OOO00OO0O00000O00 .reset_index (drop =True )#line:2214
	OOO00OO0O00000O00 ["30天累计数"]=OOO00OO0O00000O00 ["报告总数"].rolling (30 ,min_periods =1 ).agg (lambda OO000000O000OOOO0 :sum (OO000000O000OOOO0 )).astype (int )#line:2216
	OOO00OO0O00000O00 ["30天严重伤害累计数"]=OOO00OO0O00000O00 ["严重伤害数"].rolling (30 ,min_periods =1 ).agg (lambda O00OOOOOOOOOOO00O :sum (O00OOOOOOOOOOO00O )).astype (int )#line:2217
	OOO00OO0O00000O00 ["30天死亡累计数"]=OOO00OO0O00000O00 ["死亡数量"].rolling (30 ,min_periods =1 ).agg (lambda OOO00OO000O0O0O00 :sum (OOO00OO000O0O0O00 )).astype (int )#line:2218
	OOO00OO0O00000O00 .loc [(((OOO00OO0O00000O00 ["30天累计数"]>=3 )&(OOO00OO0O00000O00 ["30天严重伤害累计数"]>=1 ))|(OOO00OO0O00000O00 ["30天累计数"]>=5 )|(OOO00OO0O00000O00 ["30天死亡累计数"]>=1 )),"关注区域"]=OOO00OO0O00000O00 ["30天累计数"]#line:2239
	DRAW_make_risk_plot (OOO00OO0O00000O00 ,"time",["30天累计数","30天严重伤害累计数","关注区域"],"折线图",999 )#line:2244
def TOOLS_keti (OOOOO0O00000OOOOO ):#line:2248
	""#line:2249
	import datetime #line:2250
	def OO0OOOO0OOO0O00O0 (OOOO0O00000000O0O ,OOOO0OOOOO0O000OO ):#line:2252
		if ini ["模式"]=="药品":#line:2253
			OO000000O000OO00O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name ="药品").reset_index (drop =True )#line:2254
		if ini ["模式"]=="器械":#line:2255
			OO000000O000OO00O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name ="器械").reset_index (drop =True )#line:2256
		if ini ["模式"]=="化妆品":#line:2257
			OO000000O000OO00O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name ="化妆品").reset_index (drop =True )#line:2258
		O00O000O0OOO0O0O0 =OO000000O000OO00O ["权重"][0 ]#line:2259
		OO0O0OOOO000OOOO0 =OO000000O000OO00O ["权重"][1 ]#line:2260
		O0O0OO000OO0OOO00 =OO000000O000OO00O ["权重"][2 ]#line:2261
		OOOOO0OOO0O000O00 =OO000000O000OO00O ["权重"][3 ]#line:2262
		OO00OO00O000OOO0O =OO000000O000OO00O ["值"][3 ]#line:2263
		OOO0O00O0OOO00O0O =OO000000O000OO00O ["权重"][4 ]#line:2265
		O0OO0OO0000OOO0OO =OO000000O000OO00O ["值"][4 ]#line:2266
		OOOOOO00OOO000000 =OO000000O000OO00O ["权重"][5 ]#line:2268
		O00000O000O0O00OO =OO000000O000OO00O ["值"][5 ]#line:2269
		O0O0OO00OOOOOOOOO =OO000000O000OO00O ["权重"][6 ]#line:2271
		O0O0OOOO000O0OOO0 =OO000000O000OO00O ["值"][6 ]#line:2272
		OOOOOO0O0OO0OOOOO =pd .to_datetime (OOOO0O00000000O0O )#line:2274
		O000O0OOOOO0OO0O0 =OOOO0OOOOO0O000OO .copy ().set_index ('报告日期')#line:2275
		O000O0OOOOO0OO0O0 =O000O0OOOOO0OO0O0 .sort_index ()#line:2276
		if ini ["模式"]=="器械":#line:2277
			O000O0OOOOO0OO0O0 ["关键字查找列"]=O000O0OOOOO0OO0O0 ["器械故障表现"].astype (str )+O000O0OOOOO0OO0O0 ["伤害表现"].astype (str )+O000O0OOOOO0OO0O0 ["使用过程"].astype (str )+O000O0OOOOO0OO0O0 ["事件原因分析描述"].astype (str )+O000O0OOOOO0OO0O0 ["初步处置情况"].astype (str )#line:2278
		else :#line:2279
			O000O0OOOOO0OO0O0 ["关键字查找列"]=O000O0OOOOO0OO0O0 ["器械故障表现"].astype (str )#line:2280
		O000O0OOOOO0OO0O0 .loc [O000O0OOOOO0OO0O0 ["关键字查找列"].str .contains (OO00OO00O000OOO0O ,na =False ),"高度关注关键字"]=1 #line:2281
		O000O0OOOOO0OO0O0 .loc [O000O0OOOOO0OO0O0 ["关键字查找列"].str .contains (O0OO0OO0000OOO0OO ,na =False ),"二级敏感词"]=1 #line:2282
		O000O0OOOOO0OO0O0 .loc [O000O0OOOOO0OO0O0 ["关键字查找列"].str .contains (O00000O000O0O00OO ,na =False ),"减分项"]=1 #line:2283
		O0OO0OOOOO0O00O00 =O000O0OOOOO0OO0O0 .loc [OOOOOO0O0OO0OOOOO -pd .Timedelta (days =30 ):OOOOOO0O0OO0OOOOO ].reset_index ()#line:2285
		OO00O00O0O0O00OO0 =O000O0OOOOO0OO0O0 .loc [OOOOOO0O0OO0OOOOO -pd .Timedelta (days =365 ):OOOOOO0O0OO0OOOOO ].reset_index ()#line:2286
		O0OO0OO000O00O0OO =O0OO0OOOOO0O00O00 .groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (证号计数 =("注册证编号/曾用注册证编号","count"),严重伤害数 =("伤害",lambda O0000O0OO0000O0OO :STAT_countpx (O0000O0OO0000O0OO .values ,"严重伤害")),死亡数量 =("伤害",lambda OOOO0O00000O0OO0O :STAT_countpx (OOOO0O00000O0OO0O .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda O00O0O0OOO0O00OO0 :STAT_countpx (O00O0O0OOO0O00OO0 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OO0000O0OO0OO0OOO :STAT_countpx (OO0000O0OO0OO0OOO .values ,"严重伤害待评价")),高度关注关键字 =("高度关注关键字","sum"),二级敏感词 =("二级敏感词","sum"),减分项 =("减分项","sum"),).sort_values (by ="证号计数",ascending =[False ],na_position ="last").reset_index ()#line:2308
		O0O0OOO00OOO0OO00 =O0OO0OOOOO0O00O00 .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (型号计数 =("型号","count"),).sort_values (by ="型号计数",ascending =[False ],na_position ="last").reset_index ()#line:2313
		O0O0OOO00OOO0OO00 =O0O0OOO00OOO0OO00 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2314
		O0OO00OOO0OOOO0OO =O0OO0OOOOO0O00O00 .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (批号计数 =("产品批号","count"),严重伤害数 =("伤害",lambda O0000OOO0O000OOOO :STAT_countpx (O0000OOO0O000OOOO .values ,"严重伤害")),).sort_values (by ="批号计数",ascending =[False ],na_position ="last").reset_index ()#line:2319
		O0OO00OOO0OOOO0OO ["风险评分-影响"]=0 #line:2322
		O0OO00OOO0OOOO0OO ["评分说明"]=""#line:2323
		O0OO00OOO0OOOO0OO .loc [((O0OO00OOO0OOOO0OO ["批号计数"]>=3 )&(O0OO00OOO0OOOO0OO ["严重伤害数"]>=1 )&(O0OO00OOO0OOOO0OO ["产品类别"]!="有源"))|((O0OO00OOO0OOOO0OO ["批号计数"]>=5 )&(O0OO00OOO0OOOO0OO ["产品类别"]!="有源")),"风险评分-影响"]=O0OO00OOO0OOOO0OO ["风险评分-影响"]+3 #line:2324
		O0OO00OOO0OOOO0OO .loc [(O0OO00OOO0OOOO0OO ["风险评分-影响"]>=3 ),"评分说明"]=O0OO00OOO0OOOO0OO ["评分说明"]+"●符合省中心无源规则+3;"#line:2325
		O0OO00OOO0OOOO0OO =O0OO00OOO0OOOO0OO .sort_values (by ="风险评分-影响",ascending =[False ],na_position ="last").reset_index (drop =True )#line:2329
		O0OO00OOO0OOOO0OO =O0OO00OOO0OOOO0OO .drop_duplicates ("注册证编号/曾用注册证编号")#line:2330
		O0O0OOO00OOO0OO00 =O0O0OOO00OOO0OO00 [["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号","型号计数"]]#line:2331
		O0OO00OOO0OOOO0OO =O0OO00OOO0OOOO0OO [["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号","批号计数","风险评分-影响","评分说明"]]#line:2332
		O0OO0OO000O00O0OO =pd .merge (O0OO0OO000O00O0OO ,O0O0OOO00OOO0OO00 ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2333
		O0OO0OO000O00O0OO =pd .merge (O0OO0OO000O00O0OO ,O0OO00OOO0OOOO0OO ,on =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],how ="left")#line:2335
		O0OO0OO000O00O0OO .loc [((O0OO0OO000O00O0OO ["证号计数"]>=3 )&(O0OO0OO000O00O0OO ["严重伤害数"]>=1 )&(O0OO0OO000O00O0OO ["产品类别"]=="有源"))|((O0OO0OO000O00O0OO ["证号计数"]>=5 )&(O0OO0OO000O00O0OO ["产品类别"]=="有源")),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+3 #line:2339
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-影响"]>=3 )&(O0OO0OO000O00O0OO ["产品类别"]=="有源"),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"●符合省中心有源规则+3;"#line:2340
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["死亡数量"]>=1 ),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+10 #line:2345
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-影响"]>=10 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"存在死亡报告;"#line:2346
		O00000OO0O0OO000O =round (O00O000O0OOO0O0O0 *(O0OO0OO000O00O0OO ["严重伤害数"]/O0OO0OO000O00O0OO ["证号计数"]),2 )#line:2349
		O0OO0OO000O00O0OO ["风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+O00000OO0O0OO000O #line:2350
		O0OO0OO000O00O0OO ["评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"严重比评分"+O00000OO0O0OO000O .astype (str )+";"#line:2351
		OOO00O0000O0O0O0O =round (OO0O0OOOO000OOOO0 *(np .log (O0OO0OO000O00O0OO ["单位个数"])),2 )#line:2354
		O0OO0OO000O00O0OO ["风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+OOO00O0000O0O0O0O #line:2355
		O0OO0OO000O00O0OO ["评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"报告单位评分"+OOO00O0000O0O0O0O .astype (str )+";"#line:2356
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["产品类别"]=="有源")&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+O0O0OO000OO0OOO00 *O0OO0OO000O00O0OO ["型号计数"]/O0OO0OO000O00O0OO ["证号计数"]#line:2359
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["产品类别"]=="有源")&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"型号集中度评分"+(round (O0O0OO000OO0OOO00 *O0OO0OO000O00O0OO ["型号计数"]/O0OO0OO000O00O0OO ["证号计数"],2 )).astype (str )+";"#line:2360
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["产品类别"]!="有源")&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+O0O0OO000OO0OOO00 *O0OO0OO000O00O0OO ["批号计数"]/O0OO0OO000O00O0OO ["证号计数"]#line:2361
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["产品类别"]!="有源")&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"批号集中度评分"+(round (O0O0OO000OO0OOO00 *O0OO0OO000O00O0OO ["批号计数"]/O0OO0OO000O00O0OO ["证号计数"],2 )).astype (str )+";"#line:2362
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["高度关注关键字"]>=1 ),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+OOOOO0OOO0O000O00 #line:2365
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["高度关注关键字"]>=1 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"●含有高度关注关键字评分"+str (OOOOO0OOO0O000O00 )+"；"#line:2366
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["二级敏感词"]>=1 ),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+OOO0O00O0OOO00O0O #line:2369
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["二级敏感词"]>=1 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"含有二级敏感词评分"+str (OOO0O00O0OOO00O0O )+"；"#line:2370
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["减分项"]>=1 ),"风险评分-影响"]=O0OO0OO000O00O0OO ["风险评分-影响"]+OOOOOO00OOO000000 #line:2373
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["减分项"]>=1 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"减分项评分"+str (OOOOOO00OOO000000 )+"；"#line:2374
		O00O000OO0OOOO0O0 =Countall (OO00O00O0O0O00OO0 ).df_findrisk ("事件发生月份")#line:2377
		O00O000OO0OOOO0O0 =O00O000OO0OOOO0O0 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2378
		O00O000OO0OOOO0O0 =O00O000OO0OOOO0O0 [["注册证编号/曾用注册证编号","均值","标准差","CI上限"]]#line:2379
		O0OO0OO000O00O0OO =pd .merge (O0OO0OO000O00O0OO ,O00O000OO0OOOO0O0 ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2380
		O0OO0OO000O00O0OO ["风险评分-月份"]=1 #line:2382
		O0OO0OO000O00O0OO ["mfc"]=""#line:2383
		O0OO0OO000O00O0OO .loc [((O0OO0OO000O00O0OO ["证号计数"]>O0OO0OO000O00O0OO ["均值"])&(O0OO0OO000O00O0OO ["标准差"].astype (str )=="nan")),"风险评分-月份"]=O0OO0OO000O00O0OO ["风险评分-月份"]+1 #line:2384
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>O0OO0OO000O00O0OO ["均值"]),"mfc"]="月份计数超过历史均值"+O0OO0OO000O00O0OO ["均值"].astype (str )+"；"#line:2385
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=(O0OO0OO000O00O0OO ["均值"]+O0OO0OO000O00O0OO ["标准差"]))&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"风险评分-月份"]=O0OO0OO000O00O0OO ["风险评分-月份"]+1 #line:2387
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=(O0OO0OO000O00O0OO ["均值"]+O0OO0OO000O00O0OO ["标准差"]))&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"mfc"]="月份计数超过3例超过历史均值一个标准差("+O0OO0OO000O00O0OO ["标准差"].astype (str )+")；"#line:2388
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"风险评分-月份"]=O0OO0OO000O00O0OO ["风险评分-月份"]+2 #line:2390
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=3 ),"mfc"]="月份计数超过3例且超过历史95%CI上限("+O0OO0OO000O00O0OO ["CI上限"].astype (str )+")；"#line:2391
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=5 ),"风险评分-月份"]=O0OO0OO000O00O0OO ["风险评分-月份"]+1 #line:2393
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=5 ),"mfc"]="月份计数超过5例且超过历史95%CI上限("+O0OO0OO000O00O0OO ["CI上限"].astype (str )+")；"#line:2394
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=7 ),"风险评分-月份"]=O0OO0OO000O00O0OO ["风险评分-月份"]+1 #line:2396
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=7 ),"mfc"]="月份计数超过7例且超过历史95%CI上限("+O0OO0OO000O00O0OO ["CI上限"].astype (str )+")；"#line:2397
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=9 ),"风险评分-月份"]=O0OO0OO000O00O0OO ["风险评分-月份"]+1 #line:2399
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["证号计数"]>=9 ),"mfc"]="月份计数超过9例且超过历史95%CI上限("+O0OO0OO000O00O0OO ["CI上限"].astype (str )+")；"#line:2400
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=3 )&(O0OO0OO000O00O0OO ["标准差"].astype (str )=="nan"),"风险评分-月份"]=3 #line:2404
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["证号计数"]>=3 )&(O0OO0OO000O00O0OO ["标准差"].astype (str )=="nan"),"mfc"]="无历史数据但数量超过3例；"#line:2405
		O0OO0OO000O00O0OO ["评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"●●证号数量："+O0OO0OO000O00O0OO ["证号计数"].astype (str )+";"+O0OO0OO000O00O0OO ["mfc"]#line:2408
		del O0OO0OO000O00O0OO ["mfc"]#line:2409
		O0OO0OO000O00O0OO =O0OO0OO000O00O0OO .rename (columns ={"均值":"月份均值","标准差":"月份标准差","CI上限":"月份CI上限"})#line:2410
		O00O000OO0OOOO0O0 =Countall (OO00O00O0O0O00OO0 ).df_findrisk ("产品批号")#line:2414
		O00O000OO0OOOO0O0 =O00O000OO0OOOO0O0 .drop_duplicates ("注册证编号/曾用注册证编号")#line:2415
		O00O000OO0OOOO0O0 =O00O000OO0OOOO0O0 [["注册证编号/曾用注册证编号","均值","标准差","CI上限"]]#line:2416
		O0OO0OO000O00O0OO =pd .merge (O0OO0OO000O00O0OO ,O00O000OO0OOOO0O0 ,on =["注册证编号/曾用注册证编号"],how ="left")#line:2417
		O0OO0OO000O00O0OO ["风险评分-批号"]=1 #line:2419
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["产品类别"]!="有源"),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"●●高峰批号数量："+O0OO0OO000O00O0OO ["批号计数"].astype (str )+";"#line:2420
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>O0OO0OO000O00O0OO ["均值"]),"风险评分-批号"]=O0OO0OO000O00O0OO ["风险评分-批号"]+1 #line:2422
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>O0OO0OO000O00O0OO ["均值"]),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"高峰批号计数超过历史均值"+O0OO0OO000O00O0OO ["均值"].astype (str )+"；"#line:2423
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>(O0OO0OO000O00O0OO ["均值"]+O0OO0OO000O00O0OO ["标准差"]))&(O0OO0OO000O00O0OO ["批号计数"]>=3 ),"风险评分-批号"]=O0OO0OO000O00O0OO ["风险评分-批号"]+1 #line:2424
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>(O0OO0OO000O00O0OO ["均值"]+O0OO0OO000O00O0OO ["标准差"]))&(O0OO0OO000O00O0OO ["批号计数"]>=3 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"高峰批号计数超过3例超过历史均值一个标准差("+O0OO0OO000O00O0OO ["标准差"].astype (str )+")；"#line:2425
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["批号计数"]>=3 ),"风险评分-批号"]=O0OO0OO000O00O0OO ["风险评分-批号"]+1 #line:2426
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>O0OO0OO000O00O0OO ["CI上限"])&(O0OO0OO000O00O0OO ["批号计数"]>=3 ),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"高峰批号计数超过3例且超过历史95%CI上限("+O0OO0OO000O00O0OO ["CI上限"].astype (str )+")；"#line:2427
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>=3 )&(O0OO0OO000O00O0OO ["标准差"].astype (str )=="nan"),"风险评分-月份"]=3 #line:2429
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["批号计数"]>=3 )&(O0OO0OO000O00O0OO ["标准差"].astype (str )=="nan"),"评分说明"]=O0OO0OO000O00O0OO ["评分说明"]+"无历史数据但数量超过3例；"#line:2430
		O0OO0OO000O00O0OO =O0OO0OO000O00O0OO .rename (columns ={"均值":"高峰批号均值","标准差":"高峰批号标准差","CI上限":"高峰批号CI上限"})#line:2431
		O0OO0OO000O00O0OO ["风险评分-影响"]=round (O0OO0OO000O00O0OO ["风险评分-影响"],2 )#line:2434
		O0OO0OO000O00O0OO ["风险评分-月份"]=round (O0OO0OO000O00O0OO ["风险评分-月份"],2 )#line:2435
		O0OO0OO000O00O0OO ["风险评分-批号"]=round (O0OO0OO000O00O0OO ["风险评分-批号"],2 )#line:2436
		O0OO0OO000O00O0OO ["总体评分"]=O0OO0OO000O00O0OO ["风险评分-影响"].copy ()#line:2438
		O0OO0OO000O00O0OO ["关注建议"]=""#line:2439
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-影响"]>=3 ),"关注建议"]=O0OO0OO000O00O0OO ["关注建议"]+"●建议关注(影响范围)；"#line:2440
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-月份"]>=3 ),"关注建议"]=O0OO0OO000O00O0OO ["关注建议"]+"●建议关注(当月数量异常)；"#line:2441
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-批号"]>=3 ),"关注建议"]=O0OO0OO000O00O0OO ["关注建议"]+"●建议关注(高峰批号数量异常)。"#line:2442
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-月份"]>=O0OO0OO000O00O0OO ["风险评分-批号"]),"总体评分"]=O0OO0OO000O00O0OO ["风险评分-影响"]*O0OO0OO000O00O0OO ["风险评分-月份"]#line:2446
		O0OO0OO000O00O0OO .loc [(O0OO0OO000O00O0OO ["风险评分-月份"]<O0OO0OO000O00O0OO ["风险评分-批号"]),"总体评分"]=O0OO0OO000O00O0OO ["风险评分-影响"]*O0OO0OO000O00O0OO ["风险评分-批号"]#line:2447
		O0OO0OO000O00O0OO ["总体评分"]=round (O0OO0OO000O00O0OO ["总体评分"],2 )#line:2449
		O0OO0OO000O00O0OO ["评分说明"]=O0OO0OO000O00O0OO ["关注建议"]+O0OO0OO000O00O0OO ["评分说明"]#line:2450
		O0OO0OO000O00O0OO =O0OO0OO000O00O0OO .sort_values (by =["总体评分","风险评分-影响"],ascending =[False ,False ],na_position ="last").reset_index (drop =True )#line:2451
		O0OO0OO000O00O0OO ["主要故障分类"]=""#line:2454
		for OO0OOOOO0OOO00OO0 ,OO0O000O0OO0OOO0O in O0OO0OO000O00O0OO .iterrows ():#line:2455
			OOOOOOO00000OO0O0 =O0OO0OOOOO0O00O00 [(O0OO0OOOOO0O00O00 ["注册证编号/曾用注册证编号"]==OO0O000O0OO0OOO0O ["注册证编号/曾用注册证编号"])].copy ()#line:2456
			if OO0O000O0OO0OOO0O ["总体评分"]>=float (O0O0OO00OOOOOOOOO ):#line:2457
				if OO0O000O0OO0OOO0O ["规整后品类"]!="N":#line:2458
					O000OOO0000O0000O =Countall (OOOOOOO00000OO0O0 ).df_psur ("特定品种",OO0O000O0OO0OOO0O ["规整后品类"])#line:2459
				elif OO0O000O0OO0OOO0O ["产品类别"]=="无源":#line:2460
					O000OOO0000O0000O =Countall (OOOOOOO00000OO0O0 ).df_psur ("通用无源")#line:2461
				elif OO0O000O0OO0OOO0O ["产品类别"]=="有源":#line:2462
					O000OOO0000O0000O =Countall (OOOOOOO00000OO0O0 ).df_psur ("通用有源")#line:2463
				elif OO0O000O0OO0OOO0O ["产品类别"]=="体外诊断试剂":#line:2464
					O000OOO0000O0000O =Countall (OOOOOOO00000OO0O0 ).df_psur ("体外诊断试剂")#line:2465
				OOOOOO000000OOOO0 =O000OOO0000O0000O [["事件分类","总数量"]].copy ()#line:2467
				O00O0O00O00OO00O0 =""#line:2468
				for OOO00O0OO000O0OOO ,OOOOOO00O0OO0OO0O in OOOOOO000000OOOO0 .iterrows ():#line:2469
					O00O0O00O00OO00O0 =O00O0O00O00OO00O0 +str (OOOOOO00O0OO0OO0O ["事件分类"])+":"+str (OOOOOO00O0OO0OO0O ["总数量"])+";"#line:2470
				O0OO0OO000O00O0OO .loc [OO0OOOOO0OOO00OO0 ,"主要故障分类"]=O00O0O00O00OO00O0 #line:2471
			else :#line:2472
				break #line:2473
		O0OO0OO000O00O0OO =O0OO0OO000O00O0OO [["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","证号计数","严重伤害数","死亡数量","总体评分","风险评分-影响","风险评分-月份","风险评分-批号","主要故障分类","评分说明","单位个数","单位列表","批号个数","批号列表","型号个数","型号列表","规格个数","规格列表","待评价数","严重伤害待评价数","高度关注关键字","二级敏感词","月份均值","月份标准差","月份CI上限","高峰批号均值","高峰批号标准差","高峰批号CI上限","型号","型号计数","产品批号","批号计数"]]#line:2477
		O0OO0OO000O00O0OO ["报表类型"]="dfx_zhenghao"#line:2478
		TABLE_tree_Level_2 (O0OO0OO000O00O0OO ,1 ,O0OO0OOOOO0O00O00 ,OO00O00O0O0O00OO0 )#line:2479
		pass #line:2480
	OOO0OO0O0O0OO0O0O =Toplevel ()#line:2483
	OOO0OO0O0O0OO0O0O .title ('风险预警')#line:2484
	O0OOO0O00OO0O00OO =OOO0OO0O0O0OO0O0O .winfo_screenwidth ()#line:2485
	OO0OOO00OO00OOOOO =OOO0OO0O0O0OO0O0O .winfo_screenheight ()#line:2487
	O000O0OO00000OOOO =350 #line:2489
	O0O0OO000OOO00O0O =35 #line:2490
	O000OOOO0O00OO000 =(O0OOO0O00OO0O00OO -O000O0OO00000OOOO )/2 #line:2492
	O00O0000OOO0O0O00 =(OO0OOO00OO00OOOOO -O0O0OO000OOO00O0O )/2 #line:2493
	OOO0OO0O0O0OO0O0O .geometry ("%dx%d+%d+%d"%(O000O0OO00000OOOO ,O0O0OO000OOO00O0O ,O000OOOO0O00OO000 ,O00O0000OOO0O0O00 ))#line:2494
	O0000O0000OOOO000 =Label (OOO0OO0O0O0OO0O0O ,text ="预警日期：")#line:2496
	O0000O0000OOOO000 .grid (row =1 ,column =0 ,sticky ="w")#line:2497
	OO0O00OOO000OOOOO =Entry (OOO0OO0O0O0OO0O0O ,width =30 )#line:2498
	OO0O00OOO000OOOOO .insert (0 ,datetime .date .today ())#line:2499
	OO0O00OOO000OOOOO .grid (row =1 ,column =1 ,sticky ="w")#line:2500
	O00OO000O0OO00000 =Button (OOO0OO0O0O0OO0O0O ,text ="确定",width =10 ,command =lambda :TABLE_tree_Level_2 (OO0OOOO0OOO0O00O0 (OO0O00OOO000OOOOO .get (),OOOOO0O00000OOOOO ),1 ,OOOOO0O00000OOOOO ))#line:2504
	O00OO000O0OO00000 .grid (row =1 ,column =3 ,sticky ="w")#line:2505
	pass #line:2507
def TOOLS_autocount (OOOOO000O0000OOOO ,OO000000O0OO00OO0 ):#line:2509
    ""#line:2510
    OO0O000OO0O00OO0O =pd .read_excel ("配置表/0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ).reset_index ()#line:2513
    OO00O00O0O0O00000 =pd .read_excel ("配置表/0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ).reset_index ()#line:2516
    O0OO000000O0O00O0 =OO00O00O0O0O00000 [(OO00O00O0O0O00000 ["是否属于二级以上医疗机构"]=="是")]#line:2517
    if OO000000O0OO00OO0 =="药品":#line:2520
        OOOOO000O0000OOOO =OOOOO000O0000OOOO .reset_index (drop =True )#line:2521
        if "再次使用可疑药是否出现同样反应"not in OOOOO000O0000OOOO .columns :#line:2522
            showinfo (title ="错误信息",message ="导入的疑似不是药品报告表。")#line:2523
            return 0 #line:2524
        O00OO0OO00OO0O0O0 =Countall (OOOOO000O0000OOOO ).df_org ("监测机构")#line:2526
        O00OO0OO00OO0O0O0 =pd .merge (O00OO0OO00OO0O0O0 ,OO0O000OO0O00OO0O ,on ="监测机构",how ="left")#line:2527
        O00OO0OO00OO0O0O0 =O00OO0OO00OO0O0O0 [["监测机构序号","监测机构","药品数量指标","报告数量","审核通过数","新严比","严重比","超时比"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2528
        O00OOOO0O0O0O0O00 =["药品数量指标","审核通过数","报告数量"]#line:2529
        O00OO0OO00OO0O0O0 [O00OOOO0O0O0O0O00 ]=O00OO0OO00OO0O0O0 [O00OOOO0O0O0O0O00 ].apply (lambda OOO0O0OO0OO0OO0O0 :OOO0O0OO0OO0OO0O0 .astype (int ))#line:2530
        OOO00O0O00O00000O =Countall (OOOOO000O0000OOOO ).df_user ()#line:2532
        OOO00O0O00O00000O =pd .merge (OOO00O0O00O00000O ,OO00O00O0O0O00000 ,on =["监测机构","单位名称"],how ="left")#line:2533
        OOO00O0O00O00000O =pd .merge (OOO00O0O00O00000O ,OO0O000OO0O00OO0O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2534
        OOO00O0O00O00000O =OOO00O0O00O00000O [["监测机构序号","监测机构","单位名称","药品数量指标","报告数量","审核通过数","新严比","严重比","超时比"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2536
        O00OOOO0O0O0O0O00 =["药品数量指标","审核通过数","报告数量"]#line:2537
        OOO00O0O00O00000O [O00OOOO0O0O0O0O00 ]=OOO00O0O00O00000O [O00OOOO0O0O0O0O00 ].apply (lambda O0O0OOO0OO0000OOO :O0O0OOO0OO0000OOO .astype (int ))#line:2538
        O0000O0O00O00000O =pd .merge (O0OO000000O0O00O0 ,OOO00O0O00O00000O ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2540
        O0000O0O00O00000O =O0000O0O00O00000O [(O0000O0O00O00000O ["审核通过数"]<1 )]#line:2541
        O0000O0O00O00000O =O0000O0O00O00000O [["监测机构","单位名称","报告数量","审核通过数","严重比","超时比"]]#line:2542
    if OO000000O0OO00OO0 =="器械":#line:2544
        OOOOO000O0000OOOO =OOOOO000O0000OOOO .reset_index (drop =True )#line:2545
        if "产品编号"not in OOOOO000O0000OOOO .columns :#line:2546
            showinfo (title ="错误信息",message ="导入的疑似不是器械报告表。")#line:2547
            return 0 #line:2548
        O00OO0OO00OO0O0O0 =Countall (OOOOO000O0000OOOO ).df_org ("监测机构")#line:2550
        O00OO0OO00OO0O0O0 =pd .merge (O00OO0OO00OO0O0O0 ,OO0O000OO0O00OO0O ,on ="监测机构",how ="left")#line:2551
        O00OO0OO00OO0O0O0 =O00OO0OO00OO0O0O0 [["监测机构序号","监测机构","器械数量指标","报告数量","审核通过数","严重比","超时比"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2552
        O00OOOO0O0O0O0O00 =["器械数量指标","审核通过数","报告数量"]#line:2553
        O00OO0OO00OO0O0O0 [O00OOOO0O0O0O0O00 ]=O00OO0OO00OO0O0O0 [O00OOOO0O0O0O0O00 ].apply (lambda OO00OO00OO0OOO0OO :OO00OO00OO0OOO0OO .astype (int ))#line:2554
        OOO00O0O00O00000O =Countall (OOOOO000O0000OOOO ).df_user ()#line:2556
        OOO00O0O00O00000O =pd .merge (OOO00O0O00O00000O ,OO00O00O0O0O00000 ,on =["监测机构","单位名称"],how ="left")#line:2557
        OOO00O0O00O00000O =pd .merge (OOO00O0O00O00000O ,OO0O000OO0O00OO0O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2558
        OOO00O0O00O00000O =OOO00O0O00O00000O [["监测机构序号","监测机构","单位名称","器械数量指标","报告数量","审核通过数","严重比","超时比"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2560
        O00OOOO0O0O0O0O00 =["器械数量指标","审核通过数","报告数量"]#line:2561
        OOO00O0O00O00000O [O00OOOO0O0O0O0O00 ]=OOO00O0O00O00000O [O00OOOO0O0O0O0O00 ].apply (lambda OO00O0OO00OO0OOOO :OO00O0OO00OO0OOOO .astype (int ))#line:2562
        O0000O0O00O00000O =pd .merge (O0OO000000O0O00O0 ,OOO00O0O00O00000O ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2564
        O0000O0O00O00000O =O0000O0O00O00000O [(O0000O0O00O00000O ["审核通过数"]<1 )]#line:2565
        O0000O0O00O00000O =O0000O0O00O00000O [["监测机构","单位名称","报告数量","审核通过数","严重比","超时比"]]#line:2566
    if OO000000O0OO00OO0 =="化妆品":#line:2569
        OOOOO000O0000OOOO =OOOOO000O0000OOOO .reset_index (drop =True )#line:2570
        if "初步判断"not in OOOOO000O0000OOOO .columns :#line:2571
            showinfo (title ="错误信息",message ="导入的疑似不是化妆品报告表。")#line:2572
            return 0 #line:2573
        O00OO0OO00OO0O0O0 =Countall (OOOOO000O0000OOOO ).df_org ("监测机构")#line:2575
        O00OO0OO00OO0O0O0 =pd .merge (O00OO0OO00OO0O0O0 ,OO0O000OO0O00OO0O ,on ="监测机构",how ="left")#line:2576
        O00OO0OO00OO0O0O0 =O00OO0OO00OO0O0O0 [["监测机构序号","监测机构","化妆品数量指标","报告数量","审核通过数"]].sort_values (by =["监测机构序号"],ascending =True ,na_position ="last").fillna (0 )#line:2577
        O00OOOO0O0O0O0O00 =["化妆品数量指标","审核通过数","报告数量"]#line:2578
        O00OO0OO00OO0O0O0 [O00OOOO0O0O0O0O00 ]=O00OO0OO00OO0O0O0 [O00OOOO0O0O0O0O00 ].apply (lambda O00O000O0OOO000O0 :O00O000O0OOO000O0 .astype (int ))#line:2579
        OOO00O0O00O00000O =Countall (OOOOO000O0000OOOO ).df_user ()#line:2581
        OOO00O0O00O00000O =pd .merge (OOO00O0O00O00000O ,OO00O00O0O0O00000 ,on =["监测机构","单位名称"],how ="left")#line:2582
        OOO00O0O00O00000O =pd .merge (OOO00O0O00O00000O ,OO0O000OO0O00OO0O [["监测机构序号","监测机构"]],on ="监测机构",how ="left")#line:2583
        OOO00O0O00O00000O =OOO00O0O00O00000O [["监测机构序号","监测机构","单位名称","化妆品数量指标","报告数量","审核通过数"]].sort_values (by =["监测机构序号","报告数量"],ascending =[True ,False ],na_position ="last").fillna (0 )#line:2584
        O00OOOO0O0O0O0O00 =["化妆品数量指标","审核通过数","报告数量"]#line:2585
        OOO00O0O00O00000O [O00OOOO0O0O0O0O00 ]=OOO00O0O00O00000O [O00OOOO0O0O0O0O00 ].apply (lambda OO00O0O00O0O00O00 :OO00O0O00O0O00O00 .astype (int ))#line:2586
        O0000O0O00O00000O =pd .merge (O0OO000000O0O00O0 ,OOO00O0O00O00000O ,on =["监测机构","单位名称"],how ="left").sort_values (by =["监测机构"],ascending =True ,na_position ="last").fillna (0 )#line:2588
        O0000O0O00O00000O =O0000O0O00O00000O [(O0000O0O00O00000O ["审核通过数"]<1 )]#line:2589
        O0000O0O00O00000O =O0000O0O00O00000O [["监测机构","单位名称","报告数量","审核通过数"]]#line:2590
    OOO000O0OO00000O0 =filedialog .asksaveasfilename (title =u"保存文件",initialfile =OO000000O0OO00OO0 ,defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:2597
    O0O00O0OOO0OO0000 =pd .ExcelWriter (OOO000O0OO00000O0 )#line:2598
    O00OO0OO00OO0O0O0 .to_excel (O0O00O0OOO0OO0000 ,sheet_name ="监测机构")#line:2599
    OOO00O0O00O00000O .to_excel (O0O00O0OOO0OO0000 ,sheet_name ="上报单位")#line:2600
    O0000O0O00O00000O .to_excel (O0O00O0OOO0OO0000 ,sheet_name ="未上报的二级以上医疗机构")#line:2601
    O0O00O0OOO0OO0000 .close ()#line:2602
    showinfo (title ="提示",message ="文件写入成功。")#line:2603
def TOOLS_web_view (OO0000O0OOOOO0OOO ):#line:2605
    ""#line:2606
    import pybi as pbi #line:2607
    OOOO00O00OOOOO0OO =pd .ExcelWriter ("temp_webview.xls")#line:2608
    OO0000O0OOOOO0OOO .to_excel (OOOO00O00OOOOO0OO ,sheet_name ="temp_webview")#line:2609
    OOOO00O00OOOOO0OO .close ()#line:2610
    OO0000O0OOOOO0OOO =pd .read_excel ("temp_webview.xls",header =0 ,sheet_name =0 ).reset_index (drop =True )#line:2611
    OOOOO0000OO0OOO00 =pbi .set_source (OO0000O0OOOOO0OOO )#line:2612
    with pbi .flowBox ():#line:2613
        for O0O00OOOO0000OO00 in OO0000O0OOOOO0OOO .columns :#line:2614
            pbi .add_slicer (OOOOO0000OO0OOO00 [O0O00OOOO0000OO00 ])#line:2615
    pbi .add_table (OOOOO0000OO0OOO00 )#line:2616
    OO00000OO000O0O0O ="temp_webview.html"#line:2617
    pbi .to_html (OO00000OO000O0O0O )#line:2618
    webbrowser .open_new_tab (OO00000OO000O0O0O )#line:2619
def TOOLS_Autotable_0 (O00O0OOO0000O0000 ,OO0000OO0OOOOOO0O ,*O000O0O0OO00OOOOO ):#line:2624
    ""#line:2625
    OOOOO0O0O0000O0OO =[O000O0O0OO00OOOOO [0 ],O000O0O0OO00OOOOO [1 ],O000O0O0OO00OOOOO [2 ]]#line:2627
    O00OOOO0O00O0OOOO =list (set ([O0O0OOOOOO00OOO00 for O0O0OOOOOO00OOO00 in OOOOO0O0O0000O0OO if O0O0OOOOOO00OOO00 !='']))#line:2629
    O00OOOO0O00O0OOOO .sort (key =OOOOO0O0O0000O0OO .index )#line:2630
    if len (O00OOOO0O00O0OOOO )==0 :#line:2631
        showinfo (title ="提示信息",message ="分组项请选择至少一列。")#line:2632
        return 0 #line:2633
    OO0OO0000OOO0O000 =[O000O0O0OO00OOOOO [3 ],O000O0O0OO00OOOOO [4 ]]#line:2634
    if (O000O0O0OO00OOOOO [3 ]==""or O000O0O0OO00OOOOO [4 ]=="")and OO0000OO0OOOOOO0O in ["数据透视","分组统计"]:#line:2635
        if "报告编码"in O00O0OOO0000O0000 .columns :#line:2636
            OO0OO0000OOO0O000 [0 ]="报告编码"#line:2637
            OO0OO0000OOO0O000 [1 ]="nunique"#line:2638
            text .insert (END ,"值项未配置,将使用报告编码进行唯一值计数。")#line:2639
        else :#line:2640
            showinfo (title ="提示信息",message ="值项未配置。")#line:2641
            return 0 #line:2642
    if O000O0O0OO00OOOOO [4 ]=="计数":#line:2644
        OO0OO0000OOO0O000 [1 ]="count"#line:2645
    elif O000O0O0OO00OOOOO [4 ]=="求和":#line:2646
        OO0OO0000OOO0O000 [1 ]="sum"#line:2647
    elif O000O0O0OO00OOOOO [4 ]=="唯一值计数":#line:2648
        OO0OO0000OOO0O000 [1 ]="nunique"#line:2649
    if OO0000OO0OOOOOO0O =="分组统计":#line:2652
        TABLE_tree_Level_2 (TOOLS_deep_view (O00O0OOO0000O0000 ,O00OOOO0O00O0OOOO ,OO0OO0000OOO0O000 ,0 ),1 ,O00O0OOO0000O0000 )#line:2653
    if OO0000OO0OOOOOO0O =="数据透视":#line:2655
        TABLE_tree_Level_2 (TOOLS_deep_view (O00O0OOO0000O0000 ,O00OOOO0O00O0OOOO ,OO0OO0000OOO0O000 ,1 ),1 ,O00O0OOO0000O0000 )#line:2656
    if OO0000OO0OOOOOO0O =="描述性统计":#line:2658
        TABLE_tree_Level_2 (O00O0OOO0000O0000 [O00OOOO0O00O0OOOO ].describe ().reset_index (),1 ,O00O0OOO0000O0000 )#line:2659
    if OO0000OO0OOOOOO0O =="追加外部表格信息":#line:2662
        O00OOOO00O0OO0O0O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:2665
        OOOO0OOO000O00O0O =[pd .read_excel (OOO0O00OO0OO0OOO0 ,header =0 ,sheet_name =0 )for OOO0O00OO0OO0OOO0 in O00OOOO00O0OO0O0O ]#line:2666
        O0000O00O00O0000O =pd .concat (OOOO0OOO000O00O0O ,ignore_index =True ).drop_duplicates (O00OOOO0O00O0OOOO )#line:2667
        OOO00O0O00OO0OOOO =pd .merge (O00O0OOO0000O0000 ,O0000O00O00O0000O ,on =O00OOOO0O00O0OOOO ,how ="left")#line:2668
        TABLE_tree_Level_2 (OOO00O0O00OO0OOOO ,1 ,OOO00O0O00OO0OOOO )#line:2669
    if OO0000OO0OOOOOO0O =="添加到外部表格":#line:2671
        O00OOOO00O0OO0O0O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:2674
        OOOO0OOO000O00O0O =[pd .read_excel (OOO000OO0O00OO000 ,header =0 ,sheet_name =0 )for OOO000OO0O00OO000 in O00OOOO00O0OO0O0O ]#line:2675
        O0000O00O00O0000O =pd .concat (OOOO0OOO000O00O0O ,ignore_index =True ).drop_duplicates ()#line:2676
        OOO00O0O00OO0OOOO =pd .merge (O0000O00O00O0000O ,O00O0OOO0000O0000 .drop_duplicates (O00OOOO0O00O0OOOO ),on =O00OOOO0O00O0OOOO ,how ="left")#line:2677
        TABLE_tree_Level_2 (OOO00O0O00OO0OOOO ,1 ,OOO00O0O00OO0OOOO )#line:2678
    if OO0000OO0OOOOOO0O =="饼图(XY)":#line:2681
        DRAW_make_one (O00O0OOO0000O0000 ,"饼图",O000O0O0OO00OOOOO [0 ],O000O0O0OO00OOOOO [1 ],"饼图")#line:2682
    if OO0000OO0OOOOOO0O =="柱状图(XY)":#line:2683
        DRAW_make_one (O00O0OOO0000O0000 ,"柱状图",O000O0O0OO00OOOOO [0 ],O000O0O0OO00OOOOO [1 ],"柱状图")#line:2684
    if OO0000OO0OOOOOO0O =="折线图(XY)":#line:2685
        DRAW_make_one (O00O0OOO0000O0000 ,"折线图",O000O0O0OO00OOOOO [0 ],O000O0O0OO00OOOOO [1 ],"折线图")#line:2686
    if OO0000OO0OOOOOO0O =="托帕斯图(XY)":#line:2687
        DRAW_make_one (O00O0OOO0000O0000 ,"托帕斯图",O000O0O0OO00OOOOO [0 ],O000O0O0OO00OOOOO [1 ],"托帕斯图")#line:2688
    if OO0000OO0OOOOOO0O =="堆叠柱状图（X-YZ）":#line:2689
        DRAW_make_mutibar (O00O0OOO0000O0000 ,OOOOO0O0O0000O0OO [1 ],OOOOO0O0O0000O0OO [2 ],OOOOO0O0O0000O0OO [0 ],OOOOO0O0O0000O0OO [1 ],OOOOO0O0O0000O0OO [2 ],"堆叠柱状图")#line:2690
def STAT_countx (OO0O00000O0OOO0O0 ):#line:2700
	""#line:2701
	return OO0O00000O0OOO0O0 .value_counts ().to_dict ()#line:2702
def STAT_countpx (OOO0OO000O00O0O00 ,OOOO00O000O000O0O ):#line:2704
	""#line:2705
	return len (OOO0OO000O00O0O00 [(OOO0OO000O00O0O00 ==OOOO00O000O000O0O )])#line:2706
def STAT_countnpx (OO00OOO0O0000000O ,OOOO00O00000OOO00 ):#line:2708
	""#line:2709
	return len (OO00OOO0O0000000O [(OO00OOO0O0000000O not in OOOO00O00000OOO00 )])#line:2710
def STAT_get_max (O0O0000O0000O0O0O ):#line:2712
	""#line:2713
	return O0O0000O0000O0O0O .value_counts ().max ()#line:2714
def STAT_get_mean (O00OOOO0O0OOOO00O ):#line:2716
	""#line:2717
	return round (O00OOOO0O0OOOO00O .value_counts ().mean (),2 )#line:2718
def STAT_get_std (O0O000000000000O0 ):#line:2720
	""#line:2721
	return round (O0O000000000000O0 .value_counts ().std (ddof =1 ),2 )#line:2722
def STAT_get_95ci (OO0O0OOO00OOOO00O ):#line:2724
	""#line:2725
	return round (np .percentile (OO0O0OOO00OOOO00O .value_counts (),97.5 ),2 )#line:2726
def STAT_get_mean_std_ci (O00OOO00OOOO0O00O ,O0O000OOO00000OOO ):#line:2728
	""#line:2729
	warnings .filterwarnings ("ignore")#line:2730
	O000OOOOO00O0OO0O =TOOLS_strdict_to_pd (str (O00OOO00OOOO0O00O ))["content"].values /O0O000OOO00000OOO #line:2731
	OO00OOOOO0OOOO0O0 =round (O000OOOOO00O0OO0O .mean (),2 )#line:2732
	OO0OOO0O0OO000O00 =round (O000OOOOO00O0OO0O .std (ddof =1 ),2 )#line:2733
	OOO0OO00OO0O0O0O0 =round (np .percentile (O000OOOOO00O0OO0O ,97.5 ),2 )#line:2734
	return pd .Series ((OO00OOOOO0OOOO0O0 ,OO0OOO0O0OO000O00 ,OOO0OO00OO0O0O0O0 ))#line:2735
def STAT_findx_value (O00000O000O0OO00O ,OO00OO0OO0OOOO00O ):#line:2737
	""#line:2738
	warnings .filterwarnings ("ignore")#line:2739
	OOOO000O00OO0O00O =TOOLS_strdict_to_pd (str (O00000O000O0OO00O ))#line:2740
	OO00OO00OOO0OOOO0 =OOOO000O00OO0O00O .where (OOOO000O00OO0O00O ["index"]==str (OO00OO0OO0OOOO00O ))#line:2742
	print (OO00OO00OOO0OOOO0 )#line:2743
	return OO00OO00OOO0OOOO0 #line:2744
def STAT_judge_x (O0O0O0OOOO0OOOO0O ,O0O0OO00O0O0000O0 ):#line:2746
	""#line:2747
	for OO00OOO0O00000O0O in O0O0OO00O0O0000O0 :#line:2748
		if O0O0O0OOOO0OOOO0O .find (OO00OOO0O00000O0O )>-1 :#line:2749
			return 1 #line:2750
def STAT_recent30 (O000OO0O00O0OOOO0 ,O000000O00O000O0O ):#line:2752
	""#line:2753
	import datetime #line:2754
	OO00000O00OOO0O00 =O000OO0O00O0OOOO0 [(O000OO0O00O0OOOO0 ["报告日期"].dt .date >(datetime .date .today ()-datetime .timedelta (days =30 )))]#line:2758
	O00O0000O0OO00000 =OO00000O00OOO0O00 .groupby (O000000O00O000O0O ).agg (最近30天报告数 =("报告编码","nunique"),最近30天报告严重伤害数 =("伤害",lambda OOO00OOOOO0O0O00O :STAT_countpx (OOO00OOOOO0O0O00O .values ,"严重伤害")),最近30天报告死亡数量 =("伤害",lambda O0O0OO00000O0OO0O :STAT_countpx (O0O0OO00000O0OO0O .values ,"死亡")),最近30天报告单位个数 =("单位名称","nunique"),).reset_index ()#line:2765
	O00O0000O0OO00000 =STAT_basic_risk (O00O0000O0OO00000 ,"最近30天报告数","最近30天报告严重伤害数","最近30天报告死亡数量","最近30天报告单位个数").fillna (0 )#line:2766
	O00O0000O0OO00000 =O00O0000O0OO00000 .rename (columns ={"风险评分":"最近30天风险评分"})#line:2768
	return O00O0000O0OO00000 #line:2769
def STAT_PPR_ROR_1 (O0000000OOO0000O0 ,O00O00O00OOOO00OO ,OOOOOO00O0O0000O0 ,OOO00OOOO000O0O00 ,O0OOO00O00OOO00O0 ):#line:2772
    ""#line:2773
    O0O0O0OOO0O0OO00O =O0OOO00O00OOO00O0 [(O0OOO00O00OOO00O0 [O0000000OOO0000O0 ]==O00O00O00OOOO00OO )]#line:2776
    OO0O000OOOO0OOOOO =O0O0O0OOO0O0OO00O .loc [O0O0O0OOO0O0OO00O [OOOOOO00O0O0000O0 ].str .contains (OOO00OOOO000O0O00 ,na =False )]#line:2777
    O00OOOO00OOO000O0 =O0OOO00O00OOO00O0 [(O0OOO00O00OOO00O0 [O0000000OOO0000O0 ]!=O00O00O00OOOO00OO )]#line:2778
    OO0O000O0000OOOOO =O00OOOO00OOO000O0 .loc [O00OOOO00OOO000O0 [OOOOOO00O0O0000O0 ].str .contains (OOO00OOOO000O0O00 ,na =False )]#line:2779
    O00OO0O0OOOO0OOO0 =(len (OO0O000OOOO0OOOOO ),(len (O0O0O0OOO0O0OO00O )-len (OO0O000OOOO0OOOOO )),len (OO0O000O0000OOOOO ),(len (O00OOOO00OOO000O0 )-len (OO0O000O0000OOOOO )))#line:2780
    if len (OO0O000OOOO0OOOOO )>0 :#line:2781
        O0O0OOO0OOOO000OO =STAT_PPR_ROR_0 (len (OO0O000OOOO0OOOOO ),(len (O0O0O0OOO0O0OO00O )-len (OO0O000OOOO0OOOOO )),len (OO0O000O0000OOOOO ),(len (O00OOOO00OOO000O0 )-len (OO0O000O0000OOOOO )))#line:2782
    else :#line:2783
        O0O0OOO0OOOO000OO =(0 ,0 ,0 ,0 ,0 )#line:2784
    O0000O00000O0O0OO =len (O0O0O0OOO0O0OO00O )#line:2787
    if O0000O00000O0O0OO ==0 :#line:2788
        O0000O00000O0O0OO =0.5 #line:2789
    return (OOO00OOOO000O0O00 ,len (OO0O000OOOO0OOOOO ),round (len (OO0O000OOOO0OOOOO )/O0000O00000O0O0OO *100 ,2 ),round (O0O0OOO0OOOO000OO [0 ],2 ),round (O0O0OOO0OOOO000OO [1 ],2 ),round (O0O0OOO0OOOO000OO [2 ],2 ),round (O0O0OOO0OOOO000OO [3 ],2 ),round (O0O0OOO0OOOO000OO [4 ],2 ),str (O00OO0O0OOOO0OOO0 ),)#line:2800
def STAT_basic_risk (OO00O00O00OOOOOO0 ,OO000OOOO0O0000O0 ,O0O0OO0O0O0000O0O ,O000OO0OO0OOOOO0O ,OOOOO0OOOOOO0O0O0 ):#line:2804
	""#line:2805
	OO00O00O00OOOOOO0 ["风险评分"]=0 #line:2806
	OO00O00O00OOOOOO0 .loc [((OO00O00O00OOOOOO0 [OO000OOOO0O0000O0 ]>=3 )&(OO00O00O00OOOOOO0 [O0O0OO0O0O0000O0O ]>=1 ))|(OO00O00O00OOOOOO0 [OO000OOOO0O0000O0 ]>=5 ),"风险评分"]=OO00O00O00OOOOOO0 ["风险评分"]+5 #line:2807
	OO00O00O00OOOOOO0 .loc [(OO00O00O00OOOOOO0 [O0O0OO0O0O0000O0O ]>=3 ),"风险评分"]=OO00O00O00OOOOOO0 ["风险评分"]+1 #line:2808
	OO00O00O00OOOOOO0 .loc [(OO00O00O00OOOOOO0 [O000OO0OO0OOOOO0O ]>=1 ),"风险评分"]=OO00O00O00OOOOOO0 ["风险评分"]+10 #line:2809
	OO00O00O00OOOOOO0 ["风险评分"]=OO00O00O00OOOOOO0 ["风险评分"]+OO00O00O00OOOOOO0 [OOOOO0OOOOOO0O0O0 ]/100 #line:2810
	return OO00O00O00OOOOOO0 #line:2811
def STAT_PPR_ROR_0 (O0OO0OOOOO000O000 ,OO00O0O0O00OOOOO0 ,O0OOOOO0O0O00OOOO ,O00OOOO0OOO0O0OOO ):#line:2814
    ""#line:2815
    if O0OO0OOOOO000O000 *OO00O0O0O00OOOOO0 *O0OOOOO0O0O00OOOO *O00OOOO0OOO0O0OOO ==0 :#line:2820
        O0OO0OOOOO000O000 =O0OO0OOOOO000O000 +1 #line:2821
        OO00O0O0O00OOOOO0 =OO00O0O0O00OOOOO0 +1 #line:2822
        O0OOOOO0O0O00OOOO =O0OOOOO0O0O00OOOO +1 #line:2823
        O00OOOO0OOO0O0OOO =O00OOOO0OOO0O0OOO +1 #line:2824
    OOOO00OOO00OOOO00 =(O0OO0OOOOO000O000 /(O0OO0OOOOO000O000 +OO00O0O0O00OOOOO0 ))/(O0OOOOO0O0O00OOOO /(O0OOOOO0O0O00OOOO +O00OOOO0OOO0O0OOO ))#line:2825
    O00OO0OOO0OO00OO0 =math .sqrt (1 /O0OO0OOOOO000O000 -1 /(O0OO0OOOOO000O000 +OO00O0O0O00OOOOO0 )+1 /O0OOOOO0O0O00OOOO -1 /(O0OOOOO0O0O00OOOO +O00OOOO0OOO0O0OOO ))#line:2826
    O0O000OOO000000OO =(math .exp (math .log (OOOO00OOO00OOOO00 )-1.96 *O00OO0OOO0OO00OO0 ),math .exp (math .log (OOOO00OOO00OOOO00 )+1.96 *O00OO0OOO0OO00OO0 ),)#line:2830
    O00OOOOO00OOO00O0 =(O0OO0OOOOO000O000 /O0OOOOO0O0O00OOOO )/(OO00O0O0O00OOOOO0 /O00OOOO0OOO0O0OOO )#line:2831
    O0O000O0OO00O00O0 =math .sqrt (1 /O0OO0OOOOO000O000 +1 /OO00O0O0O00OOOOO0 +1 /O0OOOOO0O0O00OOOO +1 /O00OOOO0OOO0O0OOO )#line:2832
    OOO0OOO0OOO0OOOOO =(math .exp (math .log (O00OOOOO00OOO00O0 )-1.96 *O0O000O0OO00O00O0 ),math .exp (math .log (O00OOOOO00OOO00O0 )+1.96 *O0O000O0OO00O00O0 ),)#line:2836
    OO0OO0OOOOOOOOO0O =((O0OO0OOOOO000O000 *OO00O0O0O00OOOOO0 -OO00O0O0O00OOOOO0 *O0OOOOO0O0O00OOOO )*(O0OO0OOOOO000O000 *OO00O0O0O00OOOOO0 -OO00O0O0O00OOOOO0 *O0OOOOO0O0O00OOOO )*(O0OO0OOOOO000O000 +OO00O0O0O00OOOOO0 +O0OOOOO0O0O00OOOO +O00OOOO0OOO0O0OOO ))/((O0OO0OOOOO000O000 +OO00O0O0O00OOOOO0 )*(O0OOOOO0O0O00OOOO +O00OOOO0OOO0O0OOO )*(O0OO0OOOOO000O000 +O0OOOOO0O0O00OOOO )*(OO00O0O0O00OOOOO0 +O00OOOO0OOO0O0OOO ))#line:2839
    return O00OOOOO00OOO00O0 ,OOO0OOO0OOO0OOOOO [0 ],OOOO00OOO00OOOO00 ,O0O000OOO000000OO [0 ],OO0OO0OOOOOOOOO0O #line:2840
def STAT_find_keyword_risk (OO00O0O00OO0OO000 ,O0OO00OO0O00O000O ,OOOO0OO00O00OOOOO ,OO000OO0OOOO00O00 ,O00OOOO0000O00OOO ):#line:2842
		""#line:2843
		OO0000000OO0O0OO0 =OO00O0O00OO0OO000 .groupby (O0OO00OO0O00O000O ).agg (证号关键字总数量 =(OOOO0OO00O00OOOOO ,"count"),包含元素个数 =(OO000OO0OOOO00O00 ,"nunique"),包含元素 =(OO000OO0OOOO00O00 ,STAT_countx ),).reset_index ()#line:2848
		O0OOO00OOO0O0OOO0 =O0OO00OO0O00O000O .copy ()#line:2850
		O0OOO00OOO0O0OOO0 .append (OO000OO0OOOO00O00 )#line:2851
		OOO00OO00O00OOO00 =OO00O0O00OO0OO000 .groupby (O0OOO00OOO0O0OOO0 ).agg (计数 =(OO000OO0OOOO00O00 ,"count"),严重伤害数 =("伤害",lambda OO0O0O00O0O00O0O0 :STAT_countpx (OO0O0O00O0O00O0O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda O0O0000O00O0O0OOO :STAT_countpx (O0O0000O00O0O0OOO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:2858
		OOO00O0000OOO000O =O0OOO00OOO0O0OOO0 .copy ()#line:2861
		OOO00O0000OOO000O .remove ("关键字")#line:2862
		OO00O0O0OO0O000OO =OO00O0O00OO0OO000 .groupby (OOO00O0000OOO000O ).agg (该元素总数 =(OO000OO0OOOO00O00 ,"count"),).reset_index ()#line:2865
		OOO00OO00O00OOO00 ["证号总数"]=O00OOOO0000O00OOO #line:2867
		OO0O0OOOO0OO0O0OO =pd .merge (OOO00OO00O00OOO00 ,OO0000000OO0O0OO0 ,on =O0OO00OO0O00O000O ,how ="left")#line:2868
		if len (OO0O0OOOO0OO0O0OO )>0 :#line:2873
			OO0O0OOOO0OO0O0OO [['数量均值','数量标准差','数量CI']]=OO0O0OOOO0OO0O0OO .包含元素 .apply (lambda O00000O00O0O0OOO0 :STAT_get_mean_std_ci (O00000O00O0O0OOO0 ,1 ))#line:2874
		return OO0O0OOOO0OO0O0OO #line:2877
def STAT_find_risk (OOO00OOOO00000OO0 ,OO00O0OOO00O0O000 ,O0OOOO00O00O000O0 ,O0OO000O00O0O00O0 ):#line:2883
		""#line:2884
		O0OOO000O0OO0OO00 =OOO00OOOO00000OO0 .groupby (OO00O0OOO00O0O000 ).agg (证号总数量 =(O0OOOO00O00O000O0 ,"count"),包含元素个数 =(O0OO000O00O0O00O0 ,"nunique"),包含元素 =(O0OO000O00O0O00O0 ,STAT_countx ),均值 =(O0OO000O00O0O00O0 ,STAT_get_mean ),标准差 =(O0OO000O00O0O00O0 ,STAT_get_std ),CI上限 =(O0OO000O00O0O00O0 ,STAT_get_95ci ),).reset_index ()#line:2892
		OO000O000O000O00O =OO00O0OOO00O0O000 .copy ()#line:2894
		OO000O000O000O00O .append (O0OO000O00O0O00O0 )#line:2895
		O0OOO0O0000000OOO =OOO00OOOO00000OO0 .groupby (OO000O000O000O00O ).agg (计数 =(O0OO000O00O0O00O0 ,"count"),严重伤害数 =("伤害",lambda O0O0O00OOOOOOO0OO :STAT_countpx (O0O0O00OOOOOOO0OO .values ,"严重伤害")),死亡数量 =("伤害",lambda O0OO0OO0OOOO000OO :STAT_countpx (O0OO0OO0OOOO000OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:2902
		OO0OO000000O0O000 =pd .merge (O0OOO0O0000000OOO ,O0OOO000O0OO0OO00 ,on =OO00O0OOO00O0O000 ,how ="left")#line:2904
		OO0OO000000O0O000 ["风险评分"]=0 #line:2906
		OO0OO000000O0O000 ["报表类型"]="dfx_findrisk"+O0OO000O00O0O00O0 #line:2907
		OO0OO000000O0O000 .loc [((OO0OO000000O0O000 ["计数"]>=3 )&(OO0OO000000O0O000 ["严重伤害数"]>=1 )|(OO0OO000000O0O000 ["计数"]>=5 )),"风险评分"]=OO0OO000000O0O000 ["风险评分"]+5 #line:2908
		OO0OO000000O0O000 .loc [(OO0OO000000O0O000 ["计数"]>=(OO0OO000000O0O000 ["均值"]+OO0OO000000O0O000 ["标准差"])),"风险评分"]=OO0OO000000O0O000 ["风险评分"]+1 #line:2909
		OO0OO000000O0O000 .loc [(OO0OO000000O0O000 ["计数"]>=OO0OO000000O0O000 ["CI上限"]),"风险评分"]=OO0OO000000O0O000 ["风险评分"]+1 #line:2910
		OO0OO000000O0O000 .loc [(OO0OO000000O0O000 ["严重伤害数"]>=3 )&(OO0OO000000O0O000 ["风险评分"]>=7 ),"风险评分"]=OO0OO000000O0O000 ["风险评分"]+1 #line:2911
		OO0OO000000O0O000 .loc [(OO0OO000000O0O000 ["死亡数量"]>=1 ),"风险评分"]=OO0OO000000O0O000 ["风险评分"]+10 #line:2912
		OO0OO000000O0O000 ["风险评分"]=OO0OO000000O0O000 ["风险评分"]+OO0OO000000O0O000 ["单位个数"]/100 #line:2913
		OO0OO000000O0O000 =OO0OO000000O0O000 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:2914
		return OO0OO000000O0O000 #line:2916
def TABLE_tree_Level_2 (OO0OO00O0O000000O ,OO000OOO0OO00OOOO ,O0O0O00OOOOOOO00O ,*O0O00000O000O0O0O ):#line:2923
    ""#line:2924
    try :#line:2926
        O00O0OO0O00OOO00O =OO0OO00O0O000000O .columns #line:2927
    except :#line:2928
        return 0 #line:2929
    if "报告编码"in OO0OO00O0O000000O .columns :#line:2931
        OO000OOO0OO00OOOO =0 #line:2932
    try :#line:2933
        OO000O00OO0OO0OO0 =len (np .unique (OO0OO00O0O000000O ["注册证编号/曾用注册证编号"].values ))#line:2934
    except :#line:2935
        OO000O00OO0OO0OO0 =10 #line:2936
    OO0OOOO0OO00OO00O =Toplevel ()#line:2939
    OO0OOOO0OO00OO00O .title ("报表查看器")#line:2940
    OOOOOOO0OO0OOOO0O =OO0OOOO0OO00OO00O .winfo_screenwidth ()#line:2941
    O0O0O0OOOOOO0OO00 =OO0OOOO0OO00OO00O .winfo_screenheight ()#line:2943
    OO00O0O0OO00OOO0O =1310 #line:2945
    O00OOO0O0000O0OO0 =600 #line:2946
    OOO000000OOOO0OOO =(OOOOOOO0OO0OOOO0O -OO00O0O0OO00OOO0O )/2 #line:2948
    O00OOOOOO0OOOOOOO =(O0O0O0OOOOOO0OO00 -O00OOO0O0000O0OO0 )/2 #line:2949
    OO0OOOO0OO00OO00O .geometry ("%dx%d+%d+%d"%(OO00O0O0OO00OOO0O ,O00OOO0O0000O0OO0 ,OOO000000OOOO0OOO ,O00OOOOOO0OOOOOOO ))#line:2950
    OO0O00OOOOOOO00O0 =ttk .Frame (OO0OOOO0OO00OO00O ,width =1310 ,height =20 )#line:2953
    OO0O00OOOOOOO00O0 .pack (side =TOP )#line:2954
    OO00OOO00OO00OO00 =ttk .Frame (OO0OOOO0OO00OO00O ,width =1310 ,height =20 )#line:2955
    OO00OOO00OO00OO00 .pack (side =BOTTOM )#line:2956
    OOOO00O0O0O0O0000 =ttk .Frame (OO0OOOO0OO00OO00O ,width =1310 ,height =600 )#line:2957
    OOOO00O0O0O0O0000 .pack (fill ="both",expand ="false")#line:2958
    if OO000OOO0OO00OOOO ==0 :#line:2962
        PROGRAM_Menubar (OO0OOOO0OO00OO00O ,OO0OO00O0O000000O ,OO000OOO0OO00OOOO ,O0O0O00OOOOOOO00O )#line:2963
    try :#line:2966
        OO00O000OO000OOOO =StringVar ()#line:2967
        OO00O000OO000OOOO .set ("产品类别")#line:2968
        def O0OOO0OOO00OO000O (*OO00O0OO0OO000O0O ):#line:2969
            OO00O000OO000OOOO .set (O0OOO0OO0O0OO0000 .get ())#line:2970
        OOOOO00OOOO000000 =StringVar ()#line:2971
        OOOOO00OOOO000000 .set ("无源|诊断试剂")#line:2972
        OOOOO0O0OOOOO0OOO =Label (OO0O00OOOOOOO00O0 ,text ="")#line:2973
        OOOOO0O0OOOOO0OOO .pack (side =LEFT )#line:2974
        OOOOO0O0OOOOO0OOO =Label (OO0O00OOOOOOO00O0 ,text ="位置：")#line:2975
        OOOOO0O0OOOOO0OOO .pack (side =LEFT )#line:2976
        O0OO0OOO0OO0OO00O =StringVar ()#line:2977
        O0OOO0OO0O0OO0000 =ttk .Combobox (OO0O00OOOOOOO00O0 ,width =12 ,height =30 ,state ="readonly",textvariable =O0OO0OOO0OO0OO00O )#line:2980
        O0OOO0OO0O0OO0000 ["values"]=OO0OO00O0O000000O .columns .tolist ()#line:2981
        O0OOO0OO0O0OO0000 .current (0 )#line:2982
        O0OOO0OO0O0OO0000 .bind ("<<ComboboxSelected>>",O0OOO0OOO00OO000O )#line:2983
        O0OOO0OO0O0OO0000 .pack (side =LEFT )#line:2984
        OOO0OO00OO0OOOOO0 =Label (OO0O00OOOOOOO00O0 ,text ="检索：")#line:2985
        OOO0OO00OO0OOOOO0 .pack (side =LEFT )#line:2986
        OO0OOOOOO000OO00O =Entry (OO0O00OOOOOOO00O0 ,width =12 ,textvariable =OOOOO00OOOO000000 ).pack (side =LEFT )#line:2987
        def OO000000OO0OO0O00 ():#line:2989
            pass #line:2990
        OO00OOOOOO0O0OO0O =Button (OO0O00OOOOOOO00O0 ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (OO0OO00O0O000000O ),)#line:3004
        OO00OOOOOO0O0OO0O .pack (side =LEFT )#line:3005
        O0OOOOOOOOOOOOOOO =Button (OO0O00OOOOOOO00O0 ,text ="视图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_easyreadT (OO0OO00O0O000000O ),1 ,O0O0O00OOOOOOO00O ),)#line:3014
        if "详细描述T"not in OO0OO00O0O000000O .columns :#line:3015
            O0OOOOOOOOOOOOOOO .pack (side =LEFT )#line:3016
        O0OOOOOOOOOOOOOOO =Button (OO0O00OOOOOOO00O0 ,text ="网",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_web_view (OO0OO00O0O000000O ),)#line:3026
        if "详细描述T"not in OO0OO00O0O000000O .columns :#line:3027
            O0OOOOOOOOOOOOOOO .pack (side =LEFT )#line:3028
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="含",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .loc [OO0OO00O0O000000O [OO00O000OO000OOOO .get ()].astype (str ).str .contains (str (OOOOO00OOOO000000 .get ()),na =False )],1 ,O0O0O00OOOOOOO00O ,),)#line:3046
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3047
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="无",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .loc [~OO0OO00O0O000000O [OO00O000OO000OOOO .get ()].astype (str ).str .contains (str (OOOOO00OOOO000000 .get ()),na =False )],1 ,O0O0O00OOOOOOO00O ,),)#line:3064
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3065
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="大",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .loc [OO0OO00O0O000000O [OO00O000OO000OOOO .get ()].astype (float )>float (OOOOO00OOOO000000 .get ())],1 ,O0O0O00OOOOOOO00O ,),)#line:3080
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3081
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="小",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .loc [OO0OO00O0O000000O [OO00O000OO000OOOO .get ()].astype (float )<float (OOOOO00OOOO000000 .get ())],1 ,O0O0O00OOOOOOO00O ,),)#line:3096
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3097
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="等",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .loc [OO0OO00O0O000000O [OO00O000OO000OOOO .get ()].astype (float )==float (OOOOO00OOOO000000 .get ())],1 ,O0O0O00OOOOOOO00O ,),)#line:3112
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3113
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="式",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_findin (OO0OO00O0O000000O ,O0O0O00OOOOOOO00O ))#line:3122
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3123
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="前",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .head (int (OOOOO00OOOO000000 .get ())),1 ,O0O0O00OOOOOOO00O ,),)#line:3138
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3139
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="升",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .sort_values (by =(OO00O000OO000OOOO .get ()),ascending =[True ],na_position ="last"),1 ,O0O0O00OOOOOOO00O ,),)#line:3154
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3155
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="降",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O .sort_values (by =(OO00O000OO000OOOO .get ()),ascending =[False ],na_position ="last"),1 ,O0O0O00OOOOOOO00O ,),)#line:3170
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3171
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="SQL",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_sql (OO0OO00O0O000000O ),)#line:3181
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3182
    except :#line:3185
        pass #line:3186
    if ini ["模式"]!="其他":#line:3189
        O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="近月",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O [(OO0OO00O0O000000O ["最近30天报告单位个数"]>=1 )],1 ,O0O0O00OOOOOOO00O ,),)#line:3202
        if "最近30天报告数"in OO0OO00O0O000000O .columns :#line:3203
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3204
        OO0000000O0O0O0O0 =Button (OO0O00OOOOOOO00O0 ,text ="图表",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (OO0OO00O0O000000O ),)#line:3216
        if OO000OOO0OO00OOOO !=0 :#line:3217
            OO0000000O0O0O0O0 .pack (side =LEFT )#line:3218
        def OO0000OOO000OO00O ():#line:3223
            pass #line:3224
        if OO000OOO0OO00OOOO ==0 :#line:3227
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="精简",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_easyread2 (OO0OO00O0O000000O ),1 ,O0O0O00OOOOOOO00O ,),)#line:3241
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3242
        if OO000OOO0OO00OOOO ==0 :#line:3245
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="证号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_zhenghao (),1 ,O0O0O00OOOOOOO00O ,),)#line:3259
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3260
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO00O0O000000O ).df_zhenghao ()))#line:3269
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3270
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="批号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_pihao (),1 ,O0O0O00OOOOOOO00O ,),)#line:3285
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3286
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO00O0O000000O ).df_pihao ()))#line:3295
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3296
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="型号",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_xinghao (),1 ,O0O0O00OOOOOOO00O ,),)#line:3311
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3312
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO00O0O000000O ).df_xinghao ()))#line:3321
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3322
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="规格",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_guige (),1 ,O0O0O00OOOOOOO00O ,),)#line:3337
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3338
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_pre (Countall (OO0OO00O0O000000O ).df_guige ()))#line:3347
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3348
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="企业",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_chiyouren (),1 ,O0O0O00OOOOOOO00O ,),)#line:3363
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3364
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="县区",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_org ("监测机构"),1 ,O0O0O00OOOOOOO00O ,),)#line:3380
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3381
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="单位",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_user (),1 ,O0O0O00OOOOOOO00O ,),)#line:3394
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3395
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="年龄",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_age (),1 ,O0O0O00OOOOOOO00O ,),)#line:3409
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3410
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="时隔",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_deep_view (OO0OO00O0O000000O ,["时隔"],["报告编码","nunique"],0 ),1 ,O0O0O00OOOOOOO00O ,),)#line:3424
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3425
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="表现",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (Countall (OO0OO00O0O000000O ).df_psur (),1 ,O0O0O00OOOOOOO00O ,),)#line:3439
            if "UDI"not in OO0OO00O0O000000O .columns :#line:3440
                O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3441
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="表现",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (TOOLS_get_guize2 (OO0OO00O0O000000O ),1 ,O0O0O00OOOOOOO00O ,),)#line:3454
            if "UDI"in OO0OO00O0O000000O .columns :#line:3455
                O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3456
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="发生时间",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_time (OO0OO00O0O000000O ,"事件发生日期",0 ),)#line:3465
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3466
            O000O0OOOOOO0O0OO =Button (OO0O00OOOOOOO00O0 ,text ="报告时间",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :DRAW_make_one (TOOLS_time (OO0OO00O0O000000O ,"报告日期",1 ),"时间托帕斯图","time","报告总数","超级托帕斯图(严重伤害数)"),)#line:3476
            O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3477
    try :#line:3483
        OO00O0OO0O000O0O0 =ttk .Label (OO00OOO00OO00OO00 ,text ="方法：")#line:3485
        OO00O0OO0O000O0O0 .pack (side =LEFT )#line:3486
        OOOO000OO0O000O00 =StringVar ()#line:3487
        OO0O0O0OOOO0OOOO0 =ttk .Combobox (OO00OOO00OO00OO00 ,width =15 ,textvariable =OOOO000OO0O000O00 ,state ='readonly')#line:3488
        OO0O0O0OOOO0OOOO0 ['values']=("分组统计","数据透视","描述性统计","饼图(XY)","柱状图(XY)","折线图(XY)","托帕斯图(XY)","堆叠柱状图（X-YZ）","追加外部表格信息","添加到外部表格")#line:3489
        OO0O0O0OOOO0OOOO0 .pack (side =LEFT )#line:3493
        OO0O0O0OOOO0OOOO0 .current (0 )#line:3494
        OO0OOO00OO0OOOOOO =ttk .Label (OO00OOO00OO00OO00 ,text ="分组列（X-Y-Z）:")#line:3495
        OO0OOO00OO0OOOOOO .pack (side =LEFT )#line:3496
        OO0O0000OO000OOOO =StringVar ()#line:3499
        OO00O0O0000OOOO00 =ttk .Combobox (OO00OOO00OO00OO00 ,width =15 ,textvariable =OO0O0000OO000OOOO ,state ='readonly')#line:3500
        OO00O0O0000OOOO00 ['values']=OO0OO00O0O000000O .columns .tolist ()#line:3501
        OO00O0O0000OOOO00 .pack (side =LEFT )#line:3502
        OO0O00O000O000O0O =StringVar ()#line:3503
        OO00OOOOOOO00OOO0 =ttk .Combobox (OO00OOO00OO00OO00 ,width =15 ,textvariable =OO0O00O000O000O0O ,state ='readonly')#line:3504
        OO00OOOOOOO00OOO0 ['values']=OO0OO00O0O000000O .columns .tolist ()#line:3505
        OO00OOOOOOO00OOO0 .pack (side =LEFT )#line:3506
        OOOOO00OO000OO0O0 =StringVar ()#line:3507
        OOOO000O0000000O0 =ttk .Combobox (OO00OOO00OO00OO00 ,width =15 ,textvariable =OOOOO00OO000OO0O0 ,state ='readonly')#line:3508
        OOOO000O0000000O0 ['values']=OO0OO00O0O000000O .columns .tolist ()#line:3509
        OOOO000O0000000O0 .pack (side =LEFT )#line:3510
        OO00O0O00OOOOOOOO =StringVar ()#line:3511
        OO00OOO00000O00O0 =StringVar ()#line:3512
        OO0OOO00OO0OOOOOO =ttk .Label (OO00OOO00OO00OO00 ,text ="计算列（V-M）:")#line:3513
        OO0OOO00OO0OOOOOO .pack (side =LEFT )#line:3514
        OO0O00O00OO0OOOO0 =ttk .Combobox (OO00OOO00OO00OO00 ,width =10 ,textvariable =OO00O0O00OOOOOOOO ,state ='readonly')#line:3516
        OO0O00O00OO0OOOO0 ['values']=OO0OO00O0O000000O .columns .tolist ()#line:3517
        OO0O00O00OO0OOOO0 .pack (side =LEFT )#line:3518
        O00OOO00O00000OOO =ttk .Combobox (OO00OOO00OO00OO00 ,width =10 ,textvariable =OO00OOO00000O00O0 ,state ='readonly')#line:3519
        O00OOO00O00000OOO ['values']=["计数","求和","唯一值计数"]#line:3520
        O00OOO00O00000OOO .pack (side =LEFT )#line:3521
        OO0OO000OO0O00OO0 =Button (OO00OOO00OO00OO00 ,text ="自助报表",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_Autotable_0 (OO0OO00O0O000000O ,OO0O0O0OOOO0OOOO0 .get (),OO0O0000OO000OOOO .get (),OO0O00O000O000O0O .get (),OOOOO00OO000OO0O0 .get (),OO00O0O00OOOOOOOO .get (),OO00OOO00000O00O0 .get (),OO0OO00O0O000000O ))#line:3523
        OO0OO000OO0O00OO0 .pack (side =LEFT )#line:3524
        OO0000000O0O0O0O0 =Button (OO00OOO00OO00OO00 ,text ="去首行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O [1 :],1 ,O0O0O00OOOOOOO00O ,))#line:3541
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3542
        OO0000000O0O0O0O0 =Button (OO00OOO00OO00OO00 ,text ="去尾行",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TABLE_tree_Level_2 (OO0OO00O0O000000O [:-1 ],1 ,O0O0O00OOOOOOO00O ,),)#line:3557
        OO0000000O0O0O0O0 .pack (side =LEFT )#line:3558
        O000O0OOOOOO0O0OO =Button (OO00OOO00OO00OO00 ,text ="行数:"+str (len (OO0OO00O0O000000O )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:3568
        O000O0OOOOOO0O0OO .pack (side =LEFT )#line:3569
    except :#line:3572
        showinfo (title ="提示信息",message ="界面初始化失败。")#line:3573
    OOOO0O0OO0OOO00O0 =OO0OO00O0O000000O .values .tolist ()#line:3579
    O000OOOOOOO0OO00O =OO0OO00O0O000000O .columns .values .tolist ()#line:3580
    O0O0O00000O000000 =ttk .Treeview (OOOO00O0O0O0O0000 ,columns =O000OOOOOOO0OO00O ,show ="headings",height =45 )#line:3581
    for OO000OOO00OO0000O in O000OOOOOOO0OO00O :#line:3584
        O0O0O00000O000000 .heading (OO000OOO00OO0000O ,text =OO000OOO00OO0000O )#line:3585
    for OO0O0O0OOOO0O000O in OOOO0O0OO0OOO00O0 :#line:3586
        O0O0O00000O000000 .insert ("","end",values =OO0O0O0OOOO0O000O )#line:3587
    for O00OOO0O0OOO0O000 in O000OOOOOOO0OO00O :#line:3589
        try :#line:3590
            O0O0O00000O000000 .column (O00OOO0O0OOO0O000 ,minwidth =0 ,width =80 ,stretch =NO )#line:3591
            if "只剩"in O00OOO0O0OOO0O000 :#line:3592
                O0O0O00000O000000 .column (O00OOO0O0OOO0O000 ,minwidth =0 ,width =150 ,stretch =NO )#line:3593
        except :#line:3594
            pass #line:3595
    OO0000OOO0OOOO00O =["评分说明"]#line:3599
    OOOOOO00000OO000O =["该单位喜好上报的品种统计","报告编码","产品名称","上报机构描述","持有人处理描述","该注册证编号/曾用注册证编号报告数量","通用名称","该批准文号报告数量","上市许可持有人名称",]#line:3612
    O0OO0OO0O000O00O0 =["注册证编号/曾用注册证编号","监测机构","报告月份","报告季度","单位列表","单位名称",]#line:3620
    O00O0O0O00OO0O0O0 =["管理类别",]#line:3624
    for O00OOO0O0OOO0O000 in OOOOOO00000OO000O :#line:3627
        try :#line:3628
            O0O0O00000O000000 .column (O00OOO0O0OOO0O000 ,minwidth =0 ,width =200 ,stretch =NO )#line:3629
        except :#line:3630
            pass #line:3631
    for O00OOO0O0OOO0O000 in O0OO0OO0O000O00O0 :#line:3634
        try :#line:3635
            O0O0O00000O000000 .column (O00OOO0O0OOO0O000 ,minwidth =0 ,width =140 ,stretch =NO )#line:3636
        except :#line:3637
            pass #line:3638
    for O00OOO0O0OOO0O000 in O00O0O0O00OO0O0O0 :#line:3639
        try :#line:3640
            O0O0O00000O000000 .column (O00OOO0O0OOO0O000 ,minwidth =0 ,width =40 ,stretch =NO )#line:3641
        except :#line:3642
            pass #line:3643
    for O00OOO0O0OOO0O000 in OO0000OOO0OOOO00O :#line:3644
        try :#line:3645
            O0O0O00000O000000 .column (O00OOO0O0OOO0O000 ,minwidth =0 ,width =800 ,stretch =NO )#line:3646
        except :#line:3647
            pass #line:3648
    try :#line:3650
        O0O0O00000O000000 .column ("请选择需要查看的表格",minwidth =1 ,width =300 ,stretch =NO )#line:3653
    except :#line:3654
        pass #line:3655
    try :#line:3657
        O0O0O00000O000000 .column ("详细描述T",minwidth =1 ,width =2300 ,stretch =NO )#line:3660
    except :#line:3661
        pass #line:3662
    O0OO000OO0OOOOOOO =Scrollbar (OOOO00O0O0O0O0000 ,orient ="vertical")#line:3664
    O0OO000OO0OOOOOOO .pack (side =RIGHT ,fill =Y )#line:3665
    O0OO000OO0OOOOOOO .config (command =O0O0O00000O000000 .yview )#line:3666
    O0O0O00000O000000 .config (yscrollcommand =O0OO000OO0OOOOOOO .set )#line:3667
    OO0OOOOOO00OOOO0O =Scrollbar (OOOO00O0O0O0O0000 ,orient ="horizontal")#line:3669
    OO0OOOOOO00OOOO0O .pack (side =BOTTOM ,fill =X )#line:3670
    OO0OOOOOO00OOOO0O .config (command =O0O0O00000O000000 .xview )#line:3671
    O0O0O00000O000000 .config (yscrollcommand =O0OO000OO0OOOOOOO .set )#line:3672
    def OO0OO0OO0000000OO (OOO0O0OOOO000O0O0 ,O0O00OO0OO00O0O00 ,O00OO0OOOOO0000OO ):#line:3675
        for O0000O0O0000OO0OO in O0O0O00000O000000 .selection ():#line:3677
            O00000OOOOO00O0O0 =O0O0O00000O000000 .item (O0000O0O0000OO0OO ,"values")#line:3678
        OOOOO0O0OO0OOOO00 =dict (zip (O0O00OO0OO00O0O00 ,O00000OOOOO00O0O0 ))#line:3679
        if "详细描述T"in O0O00OO0OO00O0O00 and "{"in OOOOO0O0OO0OOOO00 ["详细描述T"]:#line:3683
            O000OOO000000O0O0 =eval (OOOOO0O0OO0OOOO00 ["详细描述T"])#line:3684
            O000OOO000000O0O0 =pd .DataFrame .from_dict (O000OOO000000O0O0 ,orient ="index",columns =["content"]).reset_index ()#line:3685
            O000OOO000000O0O0 =O000OOO000000O0O0 .sort_values (by ="content",ascending =[False ],na_position ="last")#line:3686
            DRAW_make_one (O000OOO000000O0O0 ,OOOOO0O0OO0OOOO00 ["条目"],"index","content","饼图")#line:3687
            return 0 #line:3688
        if "dfx_deepview"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3693
            O000OOOO000000000 =eval (OOOOO0O0OO0OOOO00 ["报表类型"][13 :])#line:3694
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO .copy ()#line:3695
            for O0O0OO0O00000O0O0 in O000OOOO000000000 :#line:3696
                O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO [(O0OO0O0O00O0OOOOO [O0O0OO0O00000O0O0 ]==O00000OOOOO00O0O0 [O000OOOO000000000 .index (O0O0OO0O00000O0O0 )])].copy ()#line:3697
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_deepview"#line:3698
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3699
            return 0 #line:3700
        if "dfx_deepvie2"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3703
            O000OOOO000000000 =eval (OOOOO0O0OO0OOOO00 ["报表类型"][13 :])#line:3704
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO .copy ()#line:3705
            for O0O0OO0O00000O0O0 in O000OOOO000000000 :#line:3706
                O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO [O0OO0O0O00O0OOOOO [O0O0OO0O00000O0O0 ].str .contains (O00000OOOOO00O0O0 [O000OOOO000000000 .index (O0O0OO0O00000O0O0 )],na =False )].copy ()#line:3707
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_deepview"#line:3708
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3709
            return 0 #line:3710
        if "dfx_zhenghao"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3714
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["注册证编号/曾用注册证编号"]==OOOOO0O0OO0OOOO00 ["注册证编号/曾用注册证编号"])].copy ()#line:3715
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_zhenghao"#line:3716
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3717
            return 0 #line:3718
        if ("dfx_pihao"in OOOOO0O0OO0OOOO00 ["报表类型"]or "dfx_findrisk"in OOOOO0O0OO0OOOO00 ["报表类型"]or "dfx_xinghao"in OOOOO0O0OO0OOOO00 ["报表类型"]or "dfx_guige"in OOOOO0O0OO0OOOO00 ["报表类型"])and OO000O00OO0OO0OO0 ==1 :#line:3722
            O0O0OO00OO0O00OO0 ="CLT"#line:3723
            if "pihao"in OOOOO0O0OO0OOOO00 ["报表类型"]or "产品批号"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3724
                O0O0OO00OO0O00OO0 ="产品批号"#line:3725
            if "xinghao"in OOOOO0O0OO0OOOO00 ["报表类型"]or "型号"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3726
                O0O0OO00OO0O00OO0 ="型号"#line:3727
            if "guige"in OOOOO0O0OO0OOOO00 ["报表类型"]or "规格"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3728
                O0O0OO00OO0O00OO0 ="规格"#line:3729
            if "事件发生季度"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3730
                O0O0OO00OO0O00OO0 ="事件发生季度"#line:3731
            if "事件发生月份"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3732
                O0O0OO00OO0O00OO0 ="事件发生月份"#line:3733
            if "性别"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3734
                O0O0OO00OO0O00OO0 ="性别"#line:3735
            if "年龄段"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3736
                O0O0OO00OO0O00OO0 ="年龄段"#line:3737
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["注册证编号/曾用注册证编号"]==OOOOO0O0OO0OOOO00 ["注册证编号/曾用注册证编号"])&(O00OO0OOOOO0000OO [O0O0OO00OO0O00OO0 ]==OOOOO0O0OO0OOOO00 [O0O0OO00OO0O00OO0 ])].copy ()#line:3738
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_pihao"#line:3739
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3740
            return 0 #line:3741
        if ("findrisk"in OOOOO0O0OO0OOOO00 ["报表类型"]or "dfx_pihao"in OOOOO0O0OO0OOOO00 ["报表类型"]or "dfx_xinghao"in OOOOO0O0OO0OOOO00 ["报表类型"]or "dfx_guige"in OOOOO0O0OO0OOOO00 ["报表类型"])and OO000O00OO0OO0OO0 !=1 :#line:3745
            O0OO0O0O00O0OOOOO =OO0OO00O0O000000O [(OO0OO00O0O000000O ["注册证编号/曾用注册证编号"]==OOOOO0O0OO0OOOO00 ["注册证编号/曾用注册证编号"])].copy ()#line:3746
            O0OO0O0O00O0OOOOO ["报表类型"]=OOOOO0O0OO0OOOO00 ["报表类型"]+"1"#line:3747
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,1 ,O00OO0OOOOO0000OO )#line:3748
            return 0 #line:3750
        if "dfx_org监测机构"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3753
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["监测机构"]==OOOOO0O0OO0OOOO00 ["监测机构"])].copy ()#line:3754
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_org"#line:3755
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3756
            return 0 #line:3757
        if "dfx_org市级监测机构"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3759
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["市级监测机构"]==OOOOO0O0OO0OOOO00 ["市级监测机构"])].copy ()#line:3760
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_org"#line:3761
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3762
            return 0 #line:3763
        if "dfx_user"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3766
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["单位名称"]==OOOOO0O0OO0OOOO00 ["单位名称"])].copy ()#line:3767
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_user"#line:3768
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3769
            return 0 #line:3770
        if "dfx_chiyouren"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3774
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["上市许可持有人名称"]==OOOOO0O0OO0OOOO00 ["上市许可持有人名称"])].copy ()#line:3775
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_chiyouren"#line:3776
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3777
            return 0 #line:3778
        if "dfx_chanpin"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3780
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["产品名称"]==OOOOO0O0OO0OOOO00 ["产品名称"])].copy ()#line:3781
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_chanpin"#line:3782
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3783
            return 0 #line:3784
        if "dfx_findrisk事件发生季度1"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3789
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["注册证编号/曾用注册证编号"]==OOOOO0O0OO0OOOO00 ["注册证编号/曾用注册证编号"])&(O00OO0OOOOO0000OO ["事件发生季度"]==OOOOO0O0OO0OOOO00 ["事件发生季度"])].copy ()#line:3790
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_findrisk事件发生季度"#line:3791
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3792
            return 0 #line:3793
        if "dfx_findrisk事件发生月份1"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3796
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["注册证编号/曾用注册证编号"]==OOOOO0O0OO0OOOO00 ["注册证编号/曾用注册证编号"])&(O00OO0OOOOO0000OO ["事件发生月份"]==OOOOO0O0OO0OOOO00 ["事件发生月份"])].copy ()#line:3797
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_dfx_findrisk事件发生月份"#line:3798
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3799
            return 0 #line:3800
        if ("keyword_findrisk"in OOOOO0O0OO0OOOO00 ["报表类型"])and OO000O00OO0OO0OO0 ==1 :#line:3803
            O0O0OO00OO0O00OO0 ="CLT"#line:3804
            if "批号"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3805
                O0O0OO00OO0O00OO0 ="产品批号"#line:3806
            if "事件发生季度"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3807
                O0O0OO00OO0O00OO0 ="事件发生季度"#line:3808
            if "事件发生月份"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3809
                O0O0OO00OO0O00OO0 ="事件发生月份"#line:3810
            if "性别"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3811
                O0O0OO00OO0O00OO0 ="性别"#line:3812
            if "年龄段"in OOOOO0O0OO0OOOO00 ["报表类型"]:#line:3813
                O0O0OO00OO0O00OO0 ="年龄段"#line:3814
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO [(O00OO0OOOOO0000OO ["注册证编号/曾用注册证编号"]==OOOOO0O0OO0OOOO00 ["注册证编号/曾用注册证编号"])&(O00OO0OOOOO0000OO [O0O0OO00OO0O00OO0 ]==OOOOO0O0OO0OOOO00 [O0O0OO00OO0O00OO0 ])].copy ()#line:3815
            O0OO0O0O00O0OOOOO ["关键字查找列"]=""#line:3816
            for OO00O0OO000O0OO00 in TOOLS_get_list (OOOOO0O0OO0OOOO00 ["关键字查找列"]):#line:3817
                O0OO0O0O00O0OOOOO ["关键字查找列"]=O0OO0O0O00O0OOOOO ["关键字查找列"]+O0OO0O0O00O0OOOOO [OO00O0OO000O0OO00 ].astype ("str")#line:3818
            O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO [(O0OO0O0O00O0OOOOO ["关键字查找列"].str .contains (OOOOO0O0OO0OOOO00 ["关键字组合"],na =False ))]#line:3819
            if str (OOOOO0O0OO0OOOO00 ["排除值"])!="nan":#line:3821
                O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO .loc [~O0OO0O0O00O0OOOOO ["关键字查找列"].str .contains (OOOOO0O0OO0OOOO00 ["排除值"],na =False )]#line:3822
            O0OO0O0O00O0OOOOO ["报表类型"]="ori_"+OOOOO0O0OO0OOOO00 ["报表类型"]#line:3824
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3825
            return 0 #line:3826
        if ("PSUR"in OOOOO0O0OO0OOOO00 ["报表类型"]):#line:3831
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO .copy ()#line:3832
            if ini ["模式"]=="器械":#line:3833
                O0OO0O0O00O0OOOOO ["关键字查找列"]=O0OO0O0O00O0OOOOO ["器械故障表现"].astype (str )+O0OO0O0O00O0OOOOO ["伤害表现"].astype (str )+O0OO0O0O00O0OOOOO ["使用过程"].astype (str )+O0OO0O0O00O0OOOOO ["事件原因分析描述"].astype (str )+O0OO0O0O00O0OOOOO ["初步处置情况"].astype (str )#line:3834
            else :#line:3835
                O0OO0O0O00O0OOOOO ["关键字查找列"]=O0OO0O0O00O0OOOOO ["器械故障表现"]#line:3836
            if "-其他关键字-"in str (OOOOO0O0OO0OOOO00 ["关键字标记"]):#line:3838
                O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO .loc [~O0OO0O0O00O0OOOOO ["关键字查找列"].str .contains (OOOOO0O0OO0OOOO00 ["关键字标记"],na =False )].copy ()#line:3839
                TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3840
                return 0 #line:3841
            O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO [(O0OO0O0O00O0OOOOO ["关键字查找列"].str .contains (OOOOO0O0OO0OOOO00 ["关键字标记"],na =False ))]#line:3844
            if str (OOOOO0O0OO0OOOO00 ["排除值"])!="没有排除值":#line:3845
                O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO .loc [~O0OO0O0O00O0OOOOO ["关键字查找列"].str .contains (OOOOO0O0OO0OOOO00 ["排除值"],na =False )]#line:3846
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3850
            return 0 #line:3851
        if ("ROR"in OOOOO0O0OO0OOOO00 ["报表类型"]):#line:3854
            O00OO00O0000O0O00 ={'nan':"-未定义-"}#line:3855
            O0O00OO0OO0OO0O0O =eval (OOOOO0O0OO0OOOO00 ["报表定位"],O00OO00O0000O0O00 )#line:3856
            O0OO0O0O00O0OOOOO =O00OO0OOOOO0000OO .copy ()#line:3857
            for OOO000OOOO00O0O0O ,O000O0O0OO00OO0OO in O0O00OO0OO0OO0O0O .items ():#line:3859
                if OOO000OOOO00O0O0O =="合并列"and O000O0O0OO00OO0OO !={}:#line:3861
                    for OOO0OO000000O0000 ,OOOOO0OO00OO000OO in O000O0O0OO00OO0OO .items ():#line:3862
                        if OOOOO0OO00OO000OO !="-未定义-":#line:3863
                            OOO0O00O0OOOO0O0O =TOOLS_get_list (OOOOO0OO00OO000OO )#line:3864
                            O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ]=""#line:3865
                            for O0O00O0OO0000O0O0 in OOO0O00O0OOOO0O0O :#line:3866
                                O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ]=O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ]+O0OO0O0O00O0OOOOO [O0O00O0OO0000O0O0 ].astype ("str")#line:3867
                if OOO000OOOO00O0O0O =="等于"and O000O0O0OO00OO0OO !={}:#line:3869
                    for OOO0OO000000O0000 ,OOOOO0OO00OO000OO in O000O0O0OO00OO0OO .items ():#line:3870
                        O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO [(O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ]==OOOOO0OO00OO000OO )]#line:3871
                if OOO000OOOO00O0O0O =="不等于"and O000O0O0OO00OO0OO !={}:#line:3873
                    for OOO0OO000000O0000 ,OOOOO0OO00OO000OO in O000O0O0OO00OO0OO .items ():#line:3874
                        if OOOOO0OO00OO000OO !="-未定义-":#line:3875
                            O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO [(O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ]!=OOOOO0OO00OO000OO )]#line:3876
                if OOO000OOOO00O0O0O =="包含"and O000O0O0OO00OO0OO !={}:#line:3878
                    for OOO0OO000000O0000 ,OOOOO0OO00OO000OO in O000O0O0OO00OO0OO .items ():#line:3879
                        if OOOOO0OO00OO000OO !="-未定义-":#line:3880
                            O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO .loc [O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ].str .contains (OOOOO0OO00OO000OO ,na =False )]#line:3881
                if OOO000OOOO00O0O0O =="不包含"and O000O0O0OO00OO0OO !={}:#line:3883
                    for OOO0OO000000O0000 ,OOOOO0OO00OO000OO in O000O0O0OO00OO0OO .items ():#line:3884
                        if OOOOO0OO00OO000OO !="-未定义-":#line:3885
                            O0OO0O0O00O0OOOOO =O0OO0O0O00O0OOOOO .loc [~O0OO0O0O00O0OOOOO [OOO0OO000000O0000 ].str .contains (OOOOO0OO00OO000OO ,na =False )]#line:3886
            TABLE_tree_Level_2 (O0OO0O0O00O0OOOOO ,0 ,O0OO0O0O00O0OOOOO )#line:3888
            return 0 #line:3889
    try :#line:3893
        if O0O00000O000O0O0O [1 ]=="dfx_zhenghao":#line:3894
            OOO00O0OO0000O000 ="dfx_zhenghao"#line:3895
            OOOOOO0000O0OOO00 =""#line:3896
    except :#line:3897
            OOO00O0OO0000O000 =""#line:3898
            OOOOOO0000O0OOO00 ="近一年"#line:3899
    if (("总体评分"in O0OOO0OO0O0OO0000 ["values"])and ("高峰批号均值"in O0OOO0OO0O0OO0000 ["values"])and ("月份均值"in O0OOO0OO0O0OO0000 ["values"]))or OOO00O0OO0000O000 =="dfx_zhenghao":#line:3900
            def O000O0OO0OO000OO0 (event =None ):#line:3903
                for O000O0000O0000OOO in O0O0O00000O000000 .selection ():#line:3904
                    O0OOOOOOOOOOO0000 =O0O0O00000O000000 .item (O000O0000O0000OOO ,"values")#line:3905
                OOOOO00O00OO0OO0O =dict (zip (O000OOOOOOO0OO00O ,O0OOOOOOOOOOO0000 ))#line:3906
                OOOOO000O00O0OO00 =O0O0O00OOOOOOO00O [(O0O0O00OOOOOOO00O ["注册证编号/曾用注册证编号"]==OOOOO00O00OO0OO0O ["注册证编号/曾用注册证编号"])].copy ()#line:3907
                OOOOO000O00O0OO00 ["报表类型"]=OOOOO00O00OO0OO0O ["报表类型"]+"1"#line:3908
                TABLE_tree_Level_2 (OOOOO000O00O0OO00 ,1 ,O0O0O00OOOOOOO00O )#line:3909
            def O0O000O0O00000000 (event =None ):#line:3910
                for O0OO0OO0O00OO00OO in O0O0O00000O000000 .selection ():#line:3911
                    O0OOO0OO0OO0O0OOO =O0O0O00000O000000 .item (O0OO0OO0O00OO00OO ,"values")#line:3912
                O0OOO0O000O000000 =dict (zip (O000OOOOOOO0OO00O ,O0OOO0OO0OO0O0OOO ))#line:3913
                O0O0000OOOO0O0O00 =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==O0OOO0O000O000000 ["注册证编号/曾用注册证编号"])].copy ()#line:3914
                O0O0000OOOO0O0O00 ["报表类型"]=O0OOO0O000O000000 ["报表类型"]+"1"#line:3915
                TABLE_tree_Level_2 (O0O0000OOOO0O0O00 ,1 ,O0O00000O000O0O0O [0 ])#line:3916
            def O00OO0OOOO00OO00O (OOO00OO000OOO00O0 ):#line:3917
                for OOO000000OOOOOO00 in O0O0O00000O000000 .selection ():#line:3918
                    OOO000O0O0OOOO00O =O0O0O00000O000000 .item (OOO000000OOOOOO00 ,"values")#line:3919
                O00O00OOOO00OOOO0 =dict (zip (O000OOOOOOO0OO00O ,OOO000O0O0OOOO00O ))#line:3920
                OOO0OOO00O0OOO0O0 =O0O0O00OOOOOOO00O [(O0O0O00OOOOOOO00O ["注册证编号/曾用注册证编号"]==O00O00OOOO00OOOO0 ["注册证编号/曾用注册证编号"])].copy ()#line:3923
                OOO0OOO00O0OOO0O0 ["报表类型"]=O00O00OOOO00OOOO0 ["报表类型"]+"1"#line:3924
                O0OOOO0000000000O =Countall (OOO0OOO00O0OOO0O0 ).df_psur (OOO00OO000OOO00O0 ,O00O00OOOO00OOOO0 ["规整后品类"])[["关键字标记","总数量","严重比"]]#line:3925
                O0OOOO0000000000O =O0OOOO0000000000O .rename (columns ={"总数量":"最近30天总数量"})#line:3926
                O0OOOO0000000000O =O0OOOO0000000000O .rename (columns ={"严重比":"最近30天严重比"})#line:3927
                OOO0OOO00O0OOO0O0 =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==O00O00OOOO00OOOO0 ["注册证编号/曾用注册证编号"])].copy ()#line:3929
                OOO0OOO00O0OOO0O0 ["报表类型"]=O00O00OOOO00OOOO0 ["报表类型"]+"1"#line:3930
                OO0O000OO0O0O0OO0 =Countall (OOO0OOO00O0OOO0O0 ).df_psur (OOO00OO000OOO00O0 ,O00O00OOOO00OOOO0 ["规整后品类"])#line:3931
                O00OOO0OOO000OO00 =pd .merge (OO0O000OO0O0O0OO0 ,O0OOOO0000000000O ,on ="关键字标记",how ="left")#line:3933
                del O00OOO0OOO000OO00 ["报表类型"]#line:3934
                O00OOO0OOO000OO00 ["报表类型"]="PSUR"#line:3935
                TABLE_tree_Level_2 (O00OOO0OOO000OO00 ,1 ,OOO0OOO00O0OOO0O0 )#line:3937
            def O00OO000000OO0000 (O000OO0OOO00OOO0O ):#line:3940
                for OOOOOO0OOO00O0000 in O0O0O00000O000000 .selection ():#line:3941
                    OOO0OOOO0OO0OOO00 =O0O0O00000O000000 .item (OOOOOO0OOO00O0000 ,"values")#line:3942
                O0OO0000000000OOO =dict (zip (O000OOOOOOO0OO00O ,OOO0OOOO0OO0OOO00 ))#line:3943
                OOO0O000O0000O000 =O0O00000O000O0O0O [0 ]#line:3944
                if O0OO0000000000OOO ["规整后品类"]=="N":#line:3945
                    if O000OO0OOO00OOO0O =="特定品种":#line:3946
                        showinfo (title ="关于",message ="未能适配该品种规则，可能未制定或者数据规整不完善。")#line:3947
                        return 0 #line:3948
                    OOO0O000O0000O000 =OOO0O000O0000O000 .loc [OOO0O000O0000O000 ["产品名称"].str .contains (O0OO0000000000OOO ["产品名称"],na =False )].copy ()#line:3949
                else :#line:3950
                    OOO0O000O0000O000 =OOO0O000O0000O000 .loc [OOO0O000O0000O000 ["规整后品类"].str .contains (O0OO0000000000OOO ["规整后品类"],na =False )].copy ()#line:3951
                OOO0O000O0000O000 =OOO0O000O0000O000 .loc [OOO0O000O0000O000 ["产品类别"].str .contains (O0OO0000000000OOO ["产品类别"],na =False )].copy ()#line:3952
                OOO0O000O0000O000 ["报表类型"]=O0OO0000000000OOO ["报表类型"]+"1"#line:3954
                if O000OO0OOO00OOO0O =="特定品种":#line:3955
                    TABLE_tree_Level_2 (Countall (OOO0O000O0000O000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],O0OO0000000000OOO ["规整后品类"],O0OO0000000000OOO ["注册证编号/曾用注册证编号"]),1 ,OOO0O000O0000O000 )#line:3956
                else :#line:3957
                    TABLE_tree_Level_2 (Countall (OOO0O000O0000O000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"],O000OO0OOO00OOO0O ,O0OO0000000000OOO ["注册证编号/曾用注册证编号"]),1 ,OOO0O000O0000O000 )#line:3958
            def OOOOOOO00O0O00O0O (event =None ):#line:3960
                for OO0O0O0000OOO0OO0 in O0O0O00000O000000 .selection ():#line:3961
                    OO0O00O00O00O00O0 =O0O0O00000O000000 .item (OO0O0O0000OOO0OO0 ,"values")#line:3962
                O0000OOOO000O0OOO =dict (zip (O000OOOOOOO0OO00O ,OO0O00O00O00O00O0 ))#line:3963
                O0O00OO0O00O00OOO =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==O0000OOOO000O0OOO ["注册证编号/曾用注册证编号"])].copy ()#line:3964
                O0O00OO0O00O00OOO ["报表类型"]=O0000OOOO000O0OOO ["报表类型"]+"1"#line:3965
                TABLE_tree_Level_2 (Countall (O0O00OO0O00O00OOO ).df_pihao (),1 ,O0O00OO0O00O00OOO ,)#line:3970
            def O00O0OO00O000O0OO (event =None ):#line:3972
                for OOO0O0O00O0OOO0O0 in O0O0O00000O000000 .selection ():#line:3973
                    OO00000000OOOOOO0 =O0O0O00000O000000 .item (OOO0O0O00O0OOO0O0 ,"values")#line:3974
                OOOO00O00OO0O00O0 =dict (zip (O000OOOOOOO0OO00O ,OO00000000OOOOOO0 ))#line:3975
                O0O00O00OO0O00O0O =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==OOOO00O00OO0O00O0 ["注册证编号/曾用注册证编号"])].copy ()#line:3976
                O0O00O00OO0O00O0O ["报表类型"]=OOOO00O00OO0O00O0 ["报表类型"]+"1"#line:3977
                TABLE_tree_Level_2 (Countall (O0O00O00OO0O00O0O ).df_xinghao (),1 ,O0O00O00OO0O00O0O ,)#line:3982
            def O00OOOO00OO0O0OOO (event =None ):#line:3984
                for OO0OO0O00OOO0O0O0 in O0O0O00000O000000 .selection ():#line:3985
                    OOOO00OO0OOOO000O =O0O0O00000O000000 .item (OO0OO0O00OOO0O0O0 ,"values")#line:3986
                OOOOOOOOOOO0O0O0O =dict (zip (O000OOOOOOO0OO00O ,OOOO00OO0OOOO000O ))#line:3987
                O0OO0O00OOO00O0OO =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==OOOOOOOOOOO0O0O0O ["注册证编号/曾用注册证编号"])].copy ()#line:3988
                O0OO0O00OOO00O0OO ["报表类型"]=OOOOOOOOOOO0O0O0O ["报表类型"]+"1"#line:3989
                TABLE_tree_Level_2 (Countall (O0OO0O00OOO00O0OO ).df_user (),1 ,O0OO0O00OOO00O0OO ,)#line:3994
            def OO0OOO0O0O00O0OO0 (event =None ):#line:3996
                for OOOO0OOO0OOO0O0O0 in O0O0O00000O000000 .selection ():#line:3998
                    O0OO0O00OOO0O0OOO =O0O0O00000O000000 .item (OOOO0OOO0OOO0O0O0 ,"values")#line:3999
                O00O0OO0OO0OO00O0 =dict (zip (O000OOOOOOO0OO00O ,O0OO0O00OOO0O0OOO ))#line:4000
                OOO0O00OOO00OOO0O =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==O00O0OO0OO0OO00O0 ["注册证编号/曾用注册证编号"])].copy ()#line:4001
                OOO0O00OOO00OOO0O ["报表类型"]=O00O0OO0OO0OO00O0 ["报表类型"]+"1"#line:4002
                O0OOOO0O0000O000O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name =0 ).reset_index (drop =True )#line:4003
                if ini ["模式"]=="药品":#line:4004
                    O0OOOO0O0000O000O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name ="药品").reset_index (drop =True )#line:4005
                if ini ["模式"]=="器械":#line:4006
                    O0OOOO0O0000O000O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name ="器械").reset_index (drop =True )#line:4007
                if ini ["模式"]=="化妆品":#line:4008
                    O0OOOO0O0000O000O =pd .read_excel ("配置表/0（范例）预警参数.xlsx",header =0 ,sheet_name ="化妆品").reset_index (drop =True )#line:4009
                OOOO0O0O0OO0O0O0O =O0OOOO0O0000O000O ["值"][3 ]+"|"+O0OOOO0O0000O000O ["值"][4 ]#line:4010
                if ini ["模式"]=="器械":#line:4011
                    OOO0O00OOO00OOO0O ["关键字查找列"]=OOO0O00OOO00OOO0O ["器械故障表现"].astype (str )+OOO0O00OOO00OOO0O ["伤害表现"].astype (str )+OOO0O00OOO00OOO0O ["使用过程"].astype (str )+OOO0O00OOO00OOO0O ["事件原因分析描述"].astype (str )+OOO0O00OOO00OOO0O ["初步处置情况"].astype (str )#line:4012
                else :#line:4013
                    OOO0O00OOO00OOO0O ["关键字查找列"]=OOO0O00OOO00OOO0O ["器械故障表现"].astype (str )#line:4014
                OOO0O00OOO00OOO0O =OOO0O00OOO00OOO0O .loc [OOO0O00OOO00OOO0O ["关键字查找列"].str .contains (OOOO0O0O0OO0O0O0O ,na =False )].copy ().reset_index (drop =True )#line:4015
                TABLE_tree_Level_2 (OOO0O00OOO00OOO0O ,0 ,OOO0O00OOO00OOO0O ,)#line:4021
            def OO0O000OO0O0OO000 (event =None ):#line:4024
                for O00O00OO00OOO00O0 in O0O0O00000O000000 .selection ():#line:4025
                    OO0OO0O0O0OOO000O =O0O0O00000O000000 .item (O00O00OO00OOO00O0 ,"values")#line:4026
                O0OO0O000OOOOO00O =dict (zip (O000OOOOOOO0OO00O ,OO0OO0O0O0OOO000O ))#line:4027
                O00OO000O00OO00O0 =O0O00000O000O0O0O [0 ][(O0O00000O000O0O0O [0 ]["注册证编号/曾用注册证编号"]==O0OO0O000OOOOO00O ["注册证编号/曾用注册证编号"])].copy ()#line:4028
                O00OO000O00OO00O0 ["报表类型"]=O0OO0O000OOOOO00O ["报表类型"]+"1"#line:4029
                TOOLS_time (O00OO000O00OO00O0 ,"事件发生日期",0 )#line:4030
            def OOO000O00OO00000O (OOOO00O00O0OO0OO0 ,OO00OO0OO00OOOO0O ):#line:4032
                for OOOO0OO00OOO00OOO in O0O0O00000O000000 .selection ():#line:4034
                    OOOO0000OOOO0OO0O =O0O0O00000O000000 .item (OOOO0OO00OOO00OOO ,"values")#line:4035
                O00O0OO000OO0OO00 =dict (zip (O000OOOOOOO0OO00O ,OOOO0000OOOO0OO0O ))#line:4036
                OO0OOOOO00OOOOOO0 =O0O00000O000O0O0O [0 ]#line:4037
                if O00O0OO000OO0OO00 ["规整后品类"]=="N":#line:4038
                    if OOOO00O00O0OO0OO0 =="特定品种":#line:4039
                        showinfo (title ="关于",message ="未能适配该品种规则，可能未制定或者数据规整不完善。")#line:4040
                        return 0 #line:4041
                OO0OOOOO00OOOOOO0 =OO0OOOOO00OOOOOO0 .loc [OO0OOOOO00OOOOOO0 ["注册证编号/曾用注册证编号"].str .contains (O00O0OO000OO0OO00 ["注册证编号/曾用注册证编号"],na =False )].copy ()#line:4042
                OO0OOOOO00OOOOOO0 ["报表类型"]=O00O0OO000OO0OO00 ["报表类型"]+"1"#line:4043
                if OOOO00O00O0OO0OO0 =="特定品种":#line:4044
                    TABLE_tree_Level_2 (Countall (OO0OOOOO00OOOOOO0 ).df_find_all_keword_risk (OO00OO0OO00OOOO0O ,O00O0OO000OO0OO00 ["规整后品类"]),1 ,OO0OOOOO00OOOOOO0 )#line:4045
                else :#line:4046
                    TABLE_tree_Level_2 (Countall (OO0OOOOO00OOOOOO0 ).df_find_all_keword_risk (OO00OO0OO00OOOO0O ,OOOO00O00O0OO0OO0 ),1 ,OO0OOOOO00OOOOOO0 )#line:4047
            O000O0OO00OOO00O0 =Menu (OO0OOOO0OO00OO00O ,tearoff =False ,)#line:4051
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"故障表现分类（无源）",command =lambda :O00OO0OOOO00OO00O ("通用无源"))#line:4052
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"故障表现分类（有源）",command =lambda :O00OO0OOOO00OO00O ("通用有源"))#line:4053
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"故障表现分类（特定品种）",command =lambda :O00OO0OOOO00OO00O ("特定品种"))#line:4054
            O000O0OO00OOO00O0 .add_separator ()#line:4056
            if OOO00O0OO0000O000 =="":#line:4057
                O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"同类比较(ROR-无源)",command =lambda :O00OO000000OO0000 ("无源"))#line:4058
                O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"同类比较(ROR-有源)",command =lambda :O00OO000000OO0000 ("有源"))#line:4059
                O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"同类比较(ROR-特定品种)",command =lambda :O00OO000000OO0000 ("特定品种"))#line:4060
            O000O0OO00OOO00O0 .add_separator ()#line:4062
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(批号-无源)",command =lambda :OOO000O00OO00000O ("无源","产品批号"))#line:4063
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(批号-特定品种)",command =lambda :OOO000O00OO00000O ("特定品种","产品批号"))#line:4064
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(月份-无源)",command =lambda :OOO000O00OO00000O ("无源","事件发生月份"))#line:4065
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(月份-有源)",command =lambda :OOO000O00OO00000O ("有源","事件发生月份"))#line:4066
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(月份-特定品种)",command =lambda :OOO000O00OO00000O ("特定品种","事件发生月份"))#line:4067
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(季度-无源)",command =lambda :OOO000O00OO00000O ("无源","事件发生季度"))#line:4068
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(季度-有源)",command =lambda :OOO000O00OO00000O ("有源","事件发生季度"))#line:4069
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"关键字趋势(季度-特定品种)",command =lambda :OOO000O00OO00000O ("特定品种","事件发生季度"))#line:4070
            O000O0OO00OOO00O0 .add_separator ()#line:4072
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"各批号报送情况",command =OOOOOOO00O0O00O0O )#line:4073
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"各型号报送情况",command =O00O0OO00O000O0OO )#line:4074
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"报告单位情况",command =O00OOOO00OO0O0OOO )#line:4075
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"事件发生时间曲线",command =OO0O000OO0O0OO000 )#line:4076
            O000O0OO00OOO00O0 .add_separator ()#line:4077
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"原始数据",command =O0O000O0O00000000 )#line:4078
            if OOO00O0OO0000O000 =="":#line:4079
                O000O0OO00OOO00O0 .add_command (label ="近30天原始数据",command =O000O0OO0OO000OO0 )#line:4080
            O000O0OO00OOO00O0 .add_command (label =OOOOOO0000O0OOO00 +"高度关注(一级和二级)",command =OO0OOO0O0O00O0OO0 )#line:4081
            def OO0O0000OO000OO0O (OOO000O0OOO00OO0O ):#line:4083
                O000O0OO00OOO00O0 .post (OOO000O0OOO00OO0O .x_root ,OOO000O0OOO00OO0O .y_root )#line:4084
            OO0OOOO0OO00OO00O .bind ("<Button-3>",OO0O0000OO000OO0O )#line:4085
    if OO000OOO0OO00OOOO ==0 or "规整编码"in OO0OO00O0O000000O .columns :#line:4088
        O0O0O00000O000000 .bind ("<Double-1>",lambda O00OOO000O0OO0000 :OO0OOOO0OO00OOOO0 (O00OOO000O0OO0000 ,OO0OO00O0O000000O ))#line:4089
    if OO000OOO0OO00OOOO ==1 and "规整编码"not in OO0OO00O0O000000O .columns :#line:4090
        O0O0O00000O000000 .bind ("<Double-1>",lambda OO0OOO0O0000O00OO :OO0OO0OO0000000OO (OO0OOO0O0000O00OO ,O000OOOOOOO0OO00O ,O0O0O00OOOOOOO00O ))#line:4091
    def OOOO00000O0O0O0OO (OOOOO0OOOO0O0O0OO ,O00O00OO00000OOO0 ,OO0OOOOO00O0O00OO ):#line:4094
        OO00OO0000O0OO000 =[(OOOOO0OOOO0O0O0OO .set (O0O0OOOOO0OOO000O ,O00O00OO00000OOO0 ),O0O0OOOOO0OOO000O )for O0O0OOOOO0OOO000O in OOOOO0OOOO0O0O0OO .get_children ("")]#line:4095
        OO00OO0000O0OO000 .sort (reverse =OO0OOOOO00O0O00OO )#line:4096
        for O00O0OOO0000O000O ,(OO0OOOOOO0OO0OOOO ,O0O0O0O00O000OOOO )in enumerate (OO00OO0000O0OO000 ):#line:4098
            OOOOO0OOOO0O0O0OO .move (O0O0O0O00O000OOOO ,"",O00O0OOO0000O000O )#line:4099
        OOOOO0OOOO0O0O0OO .heading (O00O00OO00000OOO0 ,command =lambda :OOOO00000O0O0O0OO (OOOOO0OOOO0O0O0OO ,O00O00OO00000OOO0 ,not OO0OOOOO00O0O00OO ))#line:4102
    for OOO0O0OOO0OO0OOO0 in O000OOOOOOO0OO00O :#line:4104
        O0O0O00000O000000 .heading (OOO0O0OOO0OO0OOO0 ,text =OOO0O0OOO0OO0OOO0 ,command =lambda _col =OOO0O0OOO0OO0OOO0 :OOOO00000O0O0O0OO (O0O0O00000O000000 ,_col ,False ),)#line:4109
    def OO0OOOO0OO00OOOO0 (OOO0OOO00OOOO00OO ,OOOO00O0OOO000O00 ):#line:4113
        if "规整编码"in OOOO00O0OOO000O00 .columns :#line:4115
            OOOO00O0OOO000O00 =OOOO00O0OOO000O00 .rename (columns ={"规整编码":"报告编码"})#line:4116
        for O0O000O0OO0O0000O in O0O0O00000O000000 .selection ():#line:4118
            O0O00OOOOO0O0OO00 =O0O0O00000O000000 .item (O0O000O0OO0O0000O ,"values")#line:4119
            OO00OO0OO0O000000 =Toplevel ()#line:4122
            O00O00OOO0O0000O0 =OO00OO0OO0O000000 .winfo_screenwidth ()#line:4124
            OOO000O0O0OOO00O0 =OO00OO0OO0O000000 .winfo_screenheight ()#line:4126
            O0OOOO00OO0O0OO0O =800 #line:4128
            O00OO0O0O0O00O00O =600 #line:4129
            OO0000000OO00OOOO =(O00O00OOO0O0000O0 -O0OOOO00OO0O0OO0O )/2 #line:4131
            O00000O00OO00000O =(OOO000O0O0OOO00O0 -O00OO0O0O0O00O00O )/2 #line:4132
            OO00OO0OO0O000000 .geometry ("%dx%d+%d+%d"%(O0OOOO00OO0O0OO0O ,O00OO0O0O0O00O00O ,OO0000000OO00OOOO ,O00000O00OO00000O ))#line:4133
            O0O000OO00000O00O =ScrolledText (OO00OO0OO0O000000 ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:4137
            O0O000OO00000O00O .pack (padx =10 ,pady =10 )#line:4138
            def O000O0OO0OO0OO00O (event =None ):#line:4139
                O0O000OO00000O00O .event_generate ('<<Copy>>')#line:4140
            def O0000O00O0O0000O0 (O0O0OOO0OOO00OO00 ,O0OOO0O000O0OOO00 ):#line:4141
                TOOLS_savetxt (O0O0OOO0OOO00OO00 ,O0OOO0O000O0OOO00 ,1 )#line:4142
            OO00000O0OO00O0O0 =Menu (O0O000OO00000O00O ,tearoff =False ,)#line:4143
            OO00000O0OO00O0O0 .add_command (label ="复制",command =O000O0OO0OO0OO00O )#line:4144
            OO00000O0OO00O0O0 .add_command (label ="导出",command =lambda :PROGRAM_thread_it (O0000O00O0O0000O0 ,O0O000OO00000O00O .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =OOOO00O0OOO000O00 .iloc [0 ,0 ],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:4145
            def OO00OO00OOO00OOO0 (OO0O000O00O000OOO ):#line:4147
                OO00000O0OO00O0O0 .post (OO0O000O00O000OOO .x_root ,OO0O000O00O000OOO .y_root )#line:4148
            O0O000OO00000O00O .bind ("<Button-3>",OO00OO00OOO00OOO0 )#line:4149
            try :#line:4151
                OO00OO0OO0O000000 .title (str (O0O00OOOOO0O0OO00 [0 ]))#line:4152
                OOOO00O0OOO000O00 ["报告编码"]=OOOO00O0OOO000O00 ["报告编码"].astype ("str")#line:4153
                OO0OOO000OOOOOOO0 =OOOO00O0OOO000O00 [(OOOO00O0OOO000O00 ["报告编码"]==str (O0O00OOOOO0O0OO00 [0 ]))]#line:4154
            except :#line:4155
                pass #line:4156
            OOOO00O0O00OO00OO =OOOO00O0OOO000O00 .columns .values .tolist ()#line:4158
            for O0OO000000OO0O000 in range (len (OOOO00O0O00OO00OO )):#line:4159
                try :#line:4161
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="报告编码.1":#line:4162
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4163
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="产品名称":#line:4164
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4165
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="事件发生日期":#line:4166
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4167
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="是否开展了调查":#line:4168
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4169
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="市级监测机构":#line:4170
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4171
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="上报机构描述":#line:4172
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4173
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]=="持有人处理描述":#line:4174
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4175
                    if O0OO000000OO0O000 >1 and OOOO00O0O00OO00OO [O0OO000000OO0O000 -1 ]=="持有人处理描述":#line:4176
                        O0O000OO00000O00O .insert (END ,"\n\n")#line:4177
                except :#line:4179
                    pass #line:4180
                try :#line:4181
                    if OOOO00O0O00OO00OO [O0OO000000OO0O000 ]in ["单位名称","产品名称ori","上报机构描述","持有人处理描述","产品名称","注册证编号/曾用注册证编号","型号","规格","产品批号","上市许可持有人名称ori","上市许可持有人名称","伤害","伤害表现","器械故障表现","使用过程","事件原因分析描述","初步处置情况","调查情况","关联性评价","事件原因分析.1","具体控制措施"]:#line:4182
                        O0O000OO00000O00O .insert (END ,"●")#line:4183
                except :#line:4184
                    pass #line:4185
                O0O000OO00000O00O .insert (END ,OOOO00O0O00OO00OO [O0OO000000OO0O000 ])#line:4186
                O0O000OO00000O00O .insert (END ,"：")#line:4187
                try :#line:4188
                    O0O000OO00000O00O .insert (END ,OO0OOO000OOOOOOO0 .iloc [0 ,O0OO000000OO0O000 ])#line:4189
                except :#line:4190
                    O0O000OO00000O00O .insert (END ,O0O00OOOOO0O0OO00 [O0OO000000OO0O000 ])#line:4191
                O0O000OO00000O00O .insert (END ,"\n")#line:4192
            O0O000OO00000O00O .config (state =DISABLED )#line:4193
    O0O0O00000O000000 .pack ()#line:4195
def TOOLS_get_guize2 (O0OOOOO00O0OO00OO ):#line:4198
	""#line:4199
	O0OOOOO00O00OOOOO ="配置表/0（范例）比例失衡关键字库.xls"#line:4200
	O00OOOOOO0OOO0O0O =pd .read_excel (O0OOOOO00O00OOOOO ,header =0 ,sheet_name ="器械")#line:4201
	OO00OOO0000OO0O0O =O00OOOOOO0OOO0O0O [["适用范围列","适用范围"]].drop_duplicates ("适用范围")#line:4202
	text .insert (END ,OO00OOO0000OO0O0O )#line:4203
	text .see (END )#line:4204
	O000O00OOOOOO00OO =Toplevel ()#line:4205
	O000O00OOOOOO00OO .title ('切换通用规则')#line:4206
	O0O000OO0O0O0O000 =O000O00OOOOOO00OO .winfo_screenwidth ()#line:4207
	O0O000O00OOOO000O =O000O00OOOOOO00OO .winfo_screenheight ()#line:4209
	OOOOO0O0OOOOOOO00 =450 #line:4211
	O0000OOO0000OOO00 =100 #line:4212
	O0O0O00O0OOOO0OO0 =(O0O000OO0O0O0O000 -OOOOO0O0OOOOOOO00 )/2 #line:4214
	O00O00OOOOOOOOO0O =(O0O000O00OOOO000O -O0000OOO0000OOO00 )/2 #line:4215
	O000O00OOOOOO00OO .geometry ("%dx%d+%d+%d"%(OOOOO0O0OOOOOOO00 ,O0000OOO0000OOO00 ,O0O0O00O0OOOO0OO0 ,O00O00OOOOOOOOO0O ))#line:4216
	O0O00OOO00O0O000O =Label (O000O00OOOOOO00OO ,text ="查找位置：器械故障表现+伤害表现+使用过程+事件原因分析描述+初步处置情况")#line:4217
	O0O00OOO00O0O000O .pack ()#line:4218
	O0OO00OOO00O0O000 =Label (O000O00OOOOOO00OO ,text ="请选择您所需要的通用规则关键字：")#line:4219
	O0OO00OOO00O0O000 .pack ()#line:4220
	def O000O000000O00O00 (*O00O0O0000O00OOOO ):#line:4221
		OO00O0O00OOO00O0O .set (OOOO00OOO0OOOO0OO .get ())#line:4222
	OO00O0O00OOO00O0O =StringVar ()#line:4223
	OOOO00OOO0OOOO0OO =ttk .Combobox (O000O00OOOOOO00OO ,width =14 ,height =30 ,state ="readonly",textvariable =OO00O0O00OOO00O0O )#line:4224
	OOOO00OOO0OOOO0OO ["values"]=OO00OOO0000OO0O0O ["适用范围"].to_list ()#line:4225
	OOOO00OOO0OOOO0OO .current (0 )#line:4226
	OOOO00OOO0OOOO0OO .bind ("<<ComboboxSelected>>",O000O000000O00O00 )#line:4227
	OOOO00OOO0OOOO0OO .pack ()#line:4228
	OOOOOOOOOOO0OOOO0 =LabelFrame (O000O00OOOOOO00OO )#line:4231
	O0O0O0O0OOO0OOO00 =Button (OOOOOOOOOOO0OOOO0 ,text ="确定",width =10 ,command =lambda :O0O00OO0O000O0O00 (O00OOOOOO0OOO0O0O ,OO00O0O00OOO00O0O .get ()))#line:4232
	O0O0O0O0OOO0OOO00 .pack (side =LEFT ,padx =1 ,pady =1 )#line:4233
	OOOOOOOOOOO0OOOO0 .pack ()#line:4234
	def O0O00OO0O000O0O00 (OO0OO0000OO00OOOO ,O0OOO0OOO000O0O0O ):#line:4236
		O0OOOOOO0O0O0O0O0 =OO0OO0000OO00OOOO .loc [OO0OO0000OO00OOOO ["适用范围"].str .contains (O0OOO0OOO000O0O0O ,na =False )].copy ().reset_index (drop =True )#line:4237
		TABLE_tree_Level_2 (Countall (O0OOOOO00O0OO00OO ).df_psur ("特定品种作为通用关键字",O0OOOOOO0O0O0O0O0 ),1 ,O0OOOOO00O0OO00OO )#line:4238
def TOOLS_findin (O000OO0OO0O00000O ,OO0O000OO0OOOO0O0 ):#line:4239
	""#line:4240
	OOOO0OOOOO000OOOO =Toplevel ()#line:4241
	OOOO0OOOOO000OOOO .title ('高级查找')#line:4242
	OO000OOOOO00O000O =OOOO0OOOOO000OOOO .winfo_screenwidth ()#line:4243
	O0OOOO000OOO0O0O0 =OOOO0OOOOO000OOOO .winfo_screenheight ()#line:4245
	OO00O000OO00O0O0O =400 #line:4247
	OOOO00O0O00O0OO00 =120 #line:4248
	O00OO0OOO000O0O00 =(OO000OOOOO00O000O -OO00O000OO00O0O0O )/2 #line:4250
	O000000O000OO00OO =(O0OOOO000OOO0O0O0 -OOOO00O0O00O0OO00 )/2 #line:4251
	OOOO0OOOOO000OOOO .geometry ("%dx%d+%d+%d"%(OO00O000OO00O0O0O ,OOOO00O0O00O0OO00 ,O00OO0OOO000O0O00 ,O000000O000OO00OO ))#line:4252
	OOOO00OOO00OO00OO =Label (OOOO0OOOOO000OOOO ,text ="需要查找的关键字（用|隔开）：")#line:4253
	OOOO00OOO00OO00OO .pack ()#line:4254
	O0OOO0OOO0OOOOO0O =Label (OOOO0OOOOO000OOOO ,text ="在哪些列查找（用|隔开）：")#line:4255
	O0OO0O000OOO0OOO0 =Entry (OOOO0OOOOO000OOOO ,width =80 )#line:4257
	O0OO0O000OOO0OOO0 .insert (0 ,"破裂|断裂")#line:4258
	O00O0O0O0OO0OOO00 =Entry (OOOO0OOOOO000OOOO ,width =80 )#line:4259
	O00O0O0O0OO0OOO00 .insert (0 ,"器械故障表现|伤害表现")#line:4260
	O0OO0O000OOO0OOO0 .pack ()#line:4261
	O0OOO0OOO0OOOOO0O .pack ()#line:4262
	O00O0O0O0OO0OOO00 .pack ()#line:4263
	OO000OOOO00OO00O0 =LabelFrame (OOOO0OOOOO000OOOO )#line:4264
	OOOOOO0OO0O000O00 =Button (OO000OOOO00OO00O0 ,text ="确定",width =10 ,command =lambda :PROGRAM_thread_it (TABLE_tree_Level_2 ,O0OOO0O0O0OOO0O0O (O0OO0O000OOO0OOO0 .get (),O00O0O0O0OO0OOO00 .get (),O000OO0OO0O00000O ),1 ,OO0O000OO0OOOO0O0 ))#line:4265
	OOOOOO0OO0O000O00 .pack (side =LEFT ,padx =1 ,pady =1 )#line:4266
	OO000OOOO00OO00O0 .pack ()#line:4267
	def O0OOO0O0O0OOO0O0O (OO000O000O000000O ,O0O000000O00000O0 ,OO0O000O0OO0O0OO0 ):#line:4270
		OO0O000O0OO0O0OO0 ["关键字查找列10"]="######"#line:4271
		for O0000OO00OOOO0O00 in TOOLS_get_list (O0O000000O00000O0 ):#line:4272
			OO0O000O0OO0O0OO0 ["关键字查找列10"]=OO0O000O0OO0O0OO0 ["关键字查找列10"].astype (str )+OO0O000O0OO0O0OO0 [O0000OO00OOOO0O00 ].astype (str )#line:4273
		OO0O000O0OO0O0OO0 =OO0O000O0OO0O0OO0 .loc [OO0O000O0OO0O0OO0 ["关键字查找列10"].str .contains (OO000O000O000000O ,na =False )]#line:4274
		del OO0O000O0OO0O0OO0 ["关键字查找列10"]#line:4275
		return OO0O000O0OO0O0OO0 #line:4276
def PROGRAM_about ():#line:4278
    ""#line:4279
    OOO0000O00OO0O0OO =" 佛山市食品药品检验检测中心 \n(佛山市药品不良反应监测中心)\n蔡权周（QQ或微信411703730）\n仅供政府设立的不良反应监测机构使用。"#line:4280
    showinfo (title ="关于",message =OOO0000O00OO0O0OO )#line:4281
def PROGRAM_thread_it (OO0O00000OOOOOO00 ,*O0OO0OOOO000000OO ):#line:4284
    ""#line:4285
    O000O0O0OOOO0000O =threading .Thread (target =OO0O00000OOOOOO00 ,args =O0OO0OOOO000000OO )#line:4287
    O000O0O0OOOO0000O .setDaemon (True )#line:4289
    O000O0O0OOOO0000O .start ()#line:4291
def PROGRAM_Menubar (O0000O0OOOO0O00OO ,OO0OOOOO000000000 ,O0OO0OOO0OOOO0OO0 ,O000O0OO0O000OO00 ):#line:4292
	""#line:4293
	if ini ["模式"]=="其他":#line:4294
		return 0 #line:4295
	OOOO00O0OO0000O0O =Menu (O0000O0OOOO0O00OO )#line:4296
	O0000O0OOOO0O00OO .config (menu =OOOO00O0OO0000O0O )#line:4298
	OO0OOOO0OO0O00OOO =Menu (OOOO00O0OO0000O0O ,tearoff =0 )#line:4302
	OOOO00O0OO0000O0O .add_cascade (label ="信号检测",menu =OO0OOOO0OO0O00OOO )#line:4303
	OO0OOOO0OO0O00OOO .add_command (label ="数量比例失衡监测-证号内批号",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_findrisk ("产品批号"),1 ,O000O0OO0O000OO00 ))#line:4306
	OO0OOOO0OO0O00OOO .add_command (label ="数量比例失衡监测-证号内季度",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_findrisk ("事件发生季度"),1 ,O000O0OO0O000OO00 ))#line:4308
	OO0OOOO0OO0O00OOO .add_command (label ="数量比例失衡监测-证号内月份",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_findrisk ("事件发生月份"),1 ,O000O0OO0O000OO00 ))#line:4310
	OO0OOOO0OO0O00OOO .add_command (label ="数量比例失衡监测-证号内性别",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_findrisk ("性别"),1 ,O000O0OO0O000OO00 ))#line:4312
	OO0OOOO0OO0O00OOO .add_command (label ="数量比例失衡监测-证号内年龄段",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_findrisk ("年龄段"),1 ,O000O0OO0O000OO00 ))#line:4314
	OO0OOOO0OO0O00OOO .add_separator ()#line:4316
	OO0OOOO0OO0O00OOO .add_command (label ="关键字检测（同证号内不同批号比对）",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_find_all_keword_risk ("产品批号"),1 ,O000O0OO0O000OO00 ))#line:4318
	OO0OOOO0OO0O00OOO .add_command (label ="关键字检测（同证号内不同月份比对）",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_find_all_keword_risk ("事件发生月份"),1 ,O000O0OO0O000OO00 ))#line:4320
	OO0OOOO0OO0O00OOO .add_command (label ="关键字检测（同证号内不同季度比对）",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_find_all_keword_risk ("事件发生季度"),1 ,O000O0OO0O000OO00 ))#line:4322
	OO0OOOO0OO0O00OOO .add_command (label ="关键字检测（同证号内不同性别比对）",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_find_all_keword_risk ("性别"),1 ,O000O0OO0O000OO00 ))#line:4324
	OO0OOOO0OO0O00OOO .add_command (label ="关键字检测（同证号内不同年龄段比对）",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_find_all_keword_risk ("年龄段"),1 ,O000O0OO0O000OO00 ))#line:4326
	OO0OOOO0OO0O00OOO .add_separator ()#line:4328
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同证号的批号间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","产品批号"]),1 ,O000O0OO0O000OO00 ))#line:4330
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同证号的月份间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","事件发生月份"]),1 ,O000O0OO0O000OO00 ))#line:4332
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同证号的季度间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","事件发生季度"]),1 ,O000O0OO0O000OO00 ))#line:4334
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同证号的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","年龄段"]),1 ,O000O0OO0O000OO00 ))#line:4336
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同证号的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号","性别"]),1 ,O000O0OO0O000OO00 ))#line:4338
	OO0OOOO0OO0O00OOO .add_separator ()#line:4340
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同品名的证号间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]),1 ,O000O0OO0O000OO00 ))#line:4342
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同品名的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["产品类别","规整后品类","产品名称","年龄段"]),1 ,O000O0OO0O000OO00 ))#line:4344
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同品名的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["产品类别","规整后品类","产品名称","性别"]),1 ,O000O0OO0O000OO00 ))#line:4346
	OO0OOOO0OO0O00OOO .add_separator ()#line:4348
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同类别的名称间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["产品类别","产品名称"]),1 ,O000O0OO0O000OO00 ))#line:4350
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同类别的年龄段间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["产品类别","年龄段"]),1 ,O000O0OO0O000OO00 ))#line:4352
	OO0OOOO0OO0O00OOO .add_command (label ="关键字ROR-页面内同类别的性别间比对",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_ror (["产品类别","性别"]),1 ,O000O0OO0O000OO00 ))#line:4354
	OO0OOOO0OO0O00OOO .add_separator ()#line:4365
	if ini ["模式"]=="药品":#line:4366
		OO0OOOO0OO0O00OOO .add_command (label ="新的不良反应检测(证号)",command =lambda :PROGRAM_thread_it (TOOLS_get_new ,O000O0OO0O000OO00 ,"证号"))#line:4369
		OO0OOOO0OO0O00OOO .add_command (label ="新的不良反应检测(品种)",command =lambda :PROGRAM_thread_it (TOOLS_get_new ,O000O0OO0O000OO00 ,"品种"))#line:4372
	O000O00OOO0OO0OO0 =Menu (OOOO00O0OO0000O0O ,tearoff =0 )#line:4375
	OOOO00O0OO0000O0O .add_cascade (label ="简报制作",menu =O000O00OOO0OO0OO0 )#line:4376
	O000O00OOO0OO0OO0 .add_command (label ="药品简报",command =lambda :TOOLS_autocount (OO0OOOOO000000000 ,"药品"))#line:4379
	O000O00OOO0OO0OO0 .add_command (label ="器械简报",command =lambda :TOOLS_autocount (OO0OOOOO000000000 ,"器械"))#line:4381
	O000O00OOO0OO0OO0 .add_command (label ="化妆品简报",command =lambda :TOOLS_autocount (OO0OOOOO000000000 ,"化妆品"))#line:4383
	OOO0OOO0O0O0O0000 =Menu (OOOO00O0OO0000O0O ,tearoff =0 )#line:4387
	OOOO00O0OO0000O0O .add_cascade (label ="品种评价",menu =OOO0OOO0O0O0O0000 )#line:4388
	OOO0OOO0O0O0O0000 .add_command (label ="报告年份",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"报告年份",-1 ))#line:4390
	OOO0OOO0O0O0O0000 .add_command (label ="发生年份",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"事件发生年份",-1 ))#line:4392
	OOO0OOO0O0O0O0000 .add_separator ()#line:4393
	OOO0OOO0O0O0O0000 .add_command (label ="怀疑/并用",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"怀疑/并用",1 ))#line:4395
	OOO0OOO0O0O0O0000 .add_command (label ="涉及企业",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"上市许可持有人名称",1 ))#line:4397
	OOO0OOO0O0O0O0000 .add_command (label ="产品名称",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"产品名称",1 ))#line:4399
	OOO0OOO0O0O0O0000 .add_command (label ="注册证号",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_zhenghao (),1 ,O000O0OO0O000OO00 ))#line:4401
	OOO0OOO0O0O0O0000 .add_separator ()#line:4402
	OOO0OOO0O0O0O0000 .add_command (label ="年龄段分布",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"年龄段",1 ))#line:4404
	OOO0OOO0O0O0O0000 .add_command (label ="性别分布",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"性别",1 ))#line:4406
	OOO0OOO0O0O0O0000 .add_command (label ="年龄性别分布",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_age (),1 ,O000O0OO0O000OO00 ,))#line:4408
	OOO0OOO0O0O0O0000 .add_separator ()#line:4409
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应发生时间",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"时隔",1 ))#line:4411
	OOO0OOO0O0O0O0000 .add_command (label ="报告类型-严重程度",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"报告类型-严重程度",1 ))#line:4414
	OOO0OOO0O0O0O0000 .add_command (label ="停药减药后反应是否减轻或消失",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"停药减药后反应是否减轻或消失",1 ))#line:4416
	OOO0OOO0O0O0O0000 .add_command (label ="再次使用可疑药是否出现同样反应",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"再次使用可疑药是否出现同样反应",1 ))#line:4418
	OOO0OOO0O0O0O0000 .add_command (label ="对原患疾病影响",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"对原患疾病影响",1 ))#line:4420
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应结果",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"不良反应结果",1 ))#line:4422
	OOO0OOO0O0O0O0000 .add_command (label ="报告单位关联性评价",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"关联性评价",1 ))#line:4424
	OOO0OOO0O0O0O0000 .add_separator ()#line:4425
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应转归情况",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"不良反应结果2",4 ))#line:4427
	OOO0OOO0O0O0O0000 .add_command (label ="关联性评价汇总",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"关联性评价汇总",5 ))#line:4429
	OOO0OOO0O0O0O0000 .add_separator ()#line:4433
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应-术语",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"器械故障表现",0 ))#line:4435
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应器官系统-术语",command =lambda :TABLE_tree_Level_2 (Countall (OO0OOOOO000000000 ).df_psur (),1 ,O000O0OO0O000OO00 ))#line:4437
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应-由code转化",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"不良反应-code",2 ))#line:4439
	OOO0OOO0O0O0O0000 .add_command (label ="不良反应器官系统-由code转化",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"不良反应-code",3 ))#line:4441
	OOO0OOO0O0O0O0000 .add_separator ()#line:4443
	OOO0OOO0O0O0O0000 .add_command (label ="疾病名称-术语",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"相关疾病信息[疾病名称]-术语",0 ))#line:4445
	OOO0OOO0O0O0O0000 .add_command (label ="疾病名称-由code转化",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"相关疾病信息[疾病名称]-code",2 ))#line:4447
	OOO0OOO0O0O0O0000 .add_command (label ="疾病器官系统-由code转化",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"相关疾病信息[疾病名称]-code",3 ))#line:4449
	OOO0OOO0O0O0O0000 .add_separator ()#line:4450
	OOO0OOO0O0O0O0000 .add_command (label ="适应症-术语",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"治疗适应症-术语",0 ))#line:4452
	OOO0OOO0O0O0O0000 .add_command (label ="适应症-由code转化",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"治疗适应症-code",2 ))#line:4454
	OOO0OOO0O0O0O0000 .add_command (label ="适应症器官系统-由code转化",command =lambda :STAT_pinzhong (OO0OOOOO000000000 ,"治疗适应症-code",3 ))#line:4456
	O0OOOO0O000O00000 =Menu (OOOO00O0OO0000O0O ,tearoff =0 )#line:4458
	OOOO00O0OO0000O0O .add_cascade (label ="基础研究",menu =O0OOOO0O000O00000 )#line:4459
	O0OOOO0O000O00000 .add_command (label ="基础信息批量操作（品名）",command =lambda :TOOLS_ror_mode1 (OO0OOOOO000000000 ,"产品名称"))#line:4461
	O0OOOO0O000O00000 .add_command (label ="器官系统ROR批量操作（品名）",command =lambda :TOOLS_ror_mode2 (OO0OOOOO000000000 ,"产品名称"))#line:4463
	O0OOOO0O000O00000 .add_command (label ="ADR-ROR批量操作（品名）",command =lambda :TOOLS_ror_mode3 (OO0OOOOO000000000 ,"产品名称"))#line:4465
	OOOOO0O00000OO0O0 =Menu (OOOO00O0OO0000O0O ,tearoff =0 )#line:4466
	OOOO00O0OO0000O0O .add_cascade (label ="风险预警",menu =OOOOO0O00000OO0O0 )#line:4467
	OOOOO0O00000OO0O0 .add_command (label ="预警（单日）",command =lambda :TOOLS_keti (OO0OOOOO000000000 ))#line:4469
	OOOOO0O00000OO0O0 .add_command (label ="事件分布（器械）",command =lambda :TOOLS_get_guize2 (OO0OOOOO000000000 ))#line:4472
	O0000O0OOOOOOO000 =Menu (OOOO00O0OO0000O0O ,tearoff =0 )#line:4479
	OOOO00O0OO0000O0O .add_cascade (label ="实用工具",menu =O0000O0OOOOOOO000 )#line:4480
	O0000O0OOOOOOO000 .add_command (label ="数据规整（报告单位）",command =lambda :TOOL_guizheng (OO0OOOOO000000000 ,2 ,False ))#line:4484
	O0000O0OOOOOOO000 .add_command (label ="数据规整（产品名称）",command =lambda :TOOL_guizheng (OO0OOOOO000000000 ,3 ,False ))#line:4486
	O0000O0OOOOOOO000 .add_command (label ="数据规整（自定义）",command =lambda :TOOL_guizheng (OO0OOOOO000000000 ,0 ,False ))#line:4488
	O0000O0OOOOOOO000 .add_separator ()#line:4490
	O0000O0OOOOOOO000 .add_command (label ="原始导入",command =TOOLS_fileopen )#line:4492
	O0000O0OOOOOOO000 .add_command (label ="脱敏保存",command =lambda :TOOLS_data_masking (OO0OOOOO000000000 ))#line:4494
	O0000O0OOOOOOO000 .add_separator ()#line:4495
	O0000O0OOOOOOO000 .add_command (label ="批量筛选（默认）",command =lambda :TOOLS_xuanze (OO0OOOOO000000000 ,1 ))#line:4497
	O0000O0OOOOOOO000 .add_command (label ="批量筛选（自定义）",command =lambda :TOOLS_xuanze (OO0OOOOO000000000 ,0 ))#line:4499
	O0000O0OOOOOOO000 .add_separator ()#line:4500
	O0000O0OOOOOOO000 .add_command (label ="评价人员（广东化妆品）",command =lambda :TOOL_person (OO0OOOOO000000000 ))#line:4502
	O0000O0OOOOOOO000 .add_separator ()#line:4503
	O0000O0OOOOOOO000 .add_command (label ="意见反馈",command =lambda :PROGRAM_helper (["","  药械妆不良反应报表统计分析工作站","  开发者：蔡权周","  邮箱：411703730@qq.com","  微信号：sysucai","  手机号：18575757461"]))#line:4507
	O0000O0OOOOOOO000 .add_command (label ="更改用户组",command =lambda :PROGRAM_thread_it (display_random_number ))#line:4509
def PROGRAM_helper (OO0O0OO0000O0O0OO ):#line:4513
    ""#line:4514
    OOOOO00OO0000O0O0 =Toplevel ()#line:4515
    OOOOO00OO0000O0O0 .title ("信息查看")#line:4516
    OOOOO00OO0000O0O0 .geometry ("700x500")#line:4517
    O0OO0O0OO0O000000 =Scrollbar (OOOOO00OO0000O0O0 )#line:4519
    O00O0OO0O0O0O00OO =Text (OOOOO00OO0000O0O0 ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:4520
    O0OO0O0OO0O000000 .pack (side =RIGHT ,fill =Y )#line:4521
    O00O0OO0O0O0O00OO .pack ()#line:4522
    O0OO0O0OO0O000000 .config (command =O00O0OO0O0O0O00OO .yview )#line:4523
    O00O0OO0O0O0O00OO .config (yscrollcommand =O0OO0O0OO0O000000 .set )#line:4524
    for OO0O000OO0O0O0000 in OO0O0OO0000O0O0OO :#line:4526
        O00O0OO0O0O0O00OO .insert (END ,OO0O000OO0O0O0000 )#line:4527
        O00O0OO0O0O0O00OO .insert (END ,"\n")#line:4528
    def OOOOOO0O00O0O0000 (event =None ):#line:4531
        O00O0OO0O0O0O00OO .event_generate ('<<Copy>>')#line:4532
    OO0O00O000OO00OOO =Menu (O00O0OO0O0O0O00OO ,tearoff =False ,)#line:4535
    OO0O00O000OO00OOO .add_command (label ="复制",command =OOOOOO0O00O0O0000 )#line:4536
    def OOOOO0O0OO00OO0O0 (O0O00OOO00OO0OO00 ):#line:4537
         OO0O00O000OO00OOO .post (O0O00OOO00OO0OO00 .x_root ,O0O00OOO00OO0OO00 .y_root )#line:4538
    O00O0OO0O0O0O00OO .bind ("<Button-3>",OOOOO0O0OO00OO0O0 )#line:4539
    O00O0OO0O0O0O00OO .config (state =DISABLED )#line:4541
def PROGRAM_change_schedule (O00OO0O0OOO000OOO ,O0O0OO0OOO0O0O0O0 ):#line:4543
    ""#line:4544
    canvas .coords (fill_rec ,(5 ,5 ,(O00OO0O0OOO000OOO /O0O0OO0OOO0O0O0O0 )*680 ,25 ))#line:4546
    root .update ()#line:4547
    x .set (str (round (O00OO0O0OOO000OOO /O0O0OO0OOO0O0O0O0 *100 ,2 ))+"%")#line:4548
    if round (O00OO0O0OOO000OOO /O0O0OO0OOO0O0O0O0 *100 ,2 )==100.00 :#line:4549
        x .set ("完成")#line:4550
def PROGRAM_showWelcome ():#line:4553
    ""#line:4554
    OO000O0OO00O0OO0O =roox .winfo_screenwidth ()#line:4555
    O0OOO0O0OOO00OO00 =roox .winfo_screenheight ()#line:4557
    roox .overrideredirect (True )#line:4559
    roox .attributes ("-alpha",1 )#line:4560
    O0OOO00000OO0OO0O =(OO000O0OO00O0OO0O -475 )/2 #line:4561
    O00O0O000OOOO0OO0 =(O0OOO0O0OOO00OO00 -200 )/2 #line:4562
    roox .geometry ("675x130+%d+%d"%(O0OOO00000OO0OO0O ,O00O0O000OOOO0OO0 ))#line:4564
    roox ["bg"]="green"#line:4565
    O0O0000O0OO0OOOO0 =Label (roox ,text =title_all2 ,fg ="white",bg ="green",font =("微软雅黑",20 ))#line:4568
    O0O0000O0OO0OOOO0 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:4569
    OOOOO0O00O000000O =Label (roox ,text ="仅供监测机构使用 ",fg ="white",bg ="black",font =("微软雅黑",15 ))#line:4572
    OOOOO0O00O000000O .place (x =0 ,y =90 ,width =675 ,height =40 )#line:4573
def PROGRAM_closeWelcome ():#line:4576
    ""#line:4577
    for OO0OO0OOOO000O0OO in range (2 ):#line:4578
        root .attributes ("-alpha",0 )#line:4579
        time .sleep (1 )#line:4580
    root .attributes ("-alpha",1 )#line:4581
    roox .destroy ()#line:4582
class Countall ():#line:4597
	""#line:4598
	def __init__ (OO0O0OOOOO0OOO000 ,OO00O00OOOO0OOO0O ):#line:4599
		""#line:4600
		OO0O0OOOOO0OOO000 .df =OO00O00OOOO0OOO0O #line:4601
		OO0O0OOOOO0OOO000 .mode =ini ["模式"]#line:4602
	def df_org (O0OO0OOO00OO0O0O0 ,O00OOOO00OO00OOO0 ):#line:4604
		""#line:4605
		OOOOO000OO0OOO0O0 =O0OO0OOO00OO0O0O0 .df .drop_duplicates (["报告编码"]).groupby ([O00OOOO00OO00OOO0 ]).agg (报告数量 =("注册证编号/曾用注册证编号","count"),审核通过数 =("有效报告","sum"),严重伤害数 =("伤害",lambda O0000O0O00OO0O00O :STAT_countpx (O0000O0O00OO0O00O .values ,"严重伤害")),死亡数量 =("伤害",lambda O00OO00O00000O0OO :STAT_countpx (O00OO00O00000O0OO .values ,"死亡")),超时报告数 =("超时标记",lambda OOOOO0OOO0OOOOOO0 :STAT_countpx (OOOOO0OOO0OOOOOO0 .values ,1 )),有源 =("产品类别",lambda O0O0OOO0O0OO00000 :STAT_countpx (O0O0OOO0O0OO00000 .values ,"有源")),无源 =("产品类别",lambda OOO0OO0OO00O0O00O :STAT_countpx (OOO0OO0OO00O0O00O .values ,"无源")),体外诊断试剂 =("产品类别",lambda OO00OOO0O0OO0O000 :STAT_countpx (OO00OOO0O0OO0O000 .values ,"体外诊断试剂")),三类数量 =("管理类别",lambda O00OO00OOO0000OOO :STAT_countpx (O00OO00OOO0000OOO .values ,"Ⅲ类")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),报告季度 =("报告季度",STAT_countx ),报告月份 =("报告月份",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:4620
		O000O0OOO0OO0O0O0 =["报告数量","审核通过数","严重伤害数","死亡数量","超时报告数","有源","无源","体外诊断试剂","三类数量","单位个数"]#line:4622
		OOOOO000OO0OOO0O0 .loc ["合计"]=OOOOO000OO0OOO0O0 [O000O0OOO0OO0O0O0 ].apply (lambda OOO0O0OO000O00000 :OOO0O0OO000O00000 .sum ())#line:4623
		OOOOO000OO0OOO0O0 [O000O0OOO0OO0O0O0 ]=OOOOO000OO0OOO0O0 [O000O0OOO0OO0O0O0 ].apply (lambda O0000O0OO000O0OOO :O0000O0OO000O0OOO .astype (int ))#line:4624
		OOOOO000OO0OOO0O0 .iloc [-1 ,0 ]="合计"#line:4625
		OOOOO000OO0OOO0O0 ["严重比"]=round ((OOOOO000OO0OOO0O0 ["严重伤害数"]+OOOOO000OO0OOO0O0 ["死亡数量"])/OOOOO000OO0OOO0O0 ["报告数量"]*100 ,2 )#line:4627
		OOOOO000OO0OOO0O0 ["Ⅲ类比"]=round ((OOOOO000OO0OOO0O0 ["三类数量"])/OOOOO000OO0OOO0O0 ["报告数量"]*100 ,2 )#line:4628
		OOOOO000OO0OOO0O0 ["超时比"]=round ((OOOOO000OO0OOO0O0 ["超时报告数"])/OOOOO000OO0OOO0O0 ["报告数量"]*100 ,2 )#line:4629
		OOOOO000OO0OOO0O0 ["报表类型"]="dfx_org"+O00OOOO00OO00OOO0 #line:4630
		if ini ["模式"]=="药品":#line:4633
			del OOOOO000OO0OOO0O0 ["有源"]#line:4635
			del OOOOO000OO0OOO0O0 ["无源"]#line:4636
			del OOOOO000OO0OOO0O0 ["体外诊断试剂"]#line:4637
			OOOOO000OO0OOO0O0 =OOOOO000OO0OOO0O0 .rename (columns ={"三类数量":"新的和严重的数量"})#line:4638
			OOOOO000OO0OOO0O0 =OOOOO000OO0OOO0O0 .rename (columns ={"Ⅲ类比":"新严比"})#line:4639
		return OOOOO000OO0OOO0O0 #line:4641
	def df_user (O0O000O00000O0O0O ):#line:4645
		""#line:4646
		O0O000O00000O0O0O .df ["医疗机构类别"]=O0O000O00000O0O0O .df ["医疗机构类别"].fillna ("未填写")#line:4647
		OO00O000OOO000O00 =O0O000O00000O0O0O .df .drop_duplicates (["报告编码"]).groupby (["监测机构","单位名称","医疗机构类别"]).agg (报告数量 =("注册证编号/曾用注册证编号","count"),审核通过数 =("有效报告","sum"),严重伤害数 =("伤害",lambda OOOO0O0OOOO0O0O0O :STAT_countpx (OOOO0O0OOOO0O0O0O .values ,"严重伤害")),死亡数量 =("伤害",lambda OO00O00OOO00000OO :STAT_countpx (OO00O00OOO00000OO .values ,"死亡")),超时报告数 =("超时标记",lambda O0OO0O0O0O0O0OO0O :STAT_countpx (O0OO0O0O0O0O0OO0O .values ,1 )),有源 =("产品类别",lambda OO00O000OOOOO0O00 :STAT_countpx (OO00O000OOOOO0O00 .values ,"有源")),无源 =("产品类别",lambda O000000O0OO00OO00 :STAT_countpx (O000000O0OO00OO00 .values ,"无源")),体外诊断试剂 =("产品类别",lambda OO0O00OO00OOO0O0O :STAT_countpx (OO0O00OO00OOO0O0O .values ,"体外诊断试剂")),三类数量 =("管理类别",lambda OOO0OO0OO0O0O00OO :STAT_countpx (OOO0OO0OO0O0O00OO .values ,"Ⅲ类")),产品数量 =("产品名称","nunique"),产品清单 =("产品名称",STAT_countx ),报告季度 =("报告季度",STAT_countx ),报告月份 =("报告月份",STAT_countx ),).sort_values (by ="报告数量",ascending =[False ],na_position ="last").reset_index ()#line:4662
		OO0OOO000O00OOOOO =["报告数量","审核通过数","严重伤害数","死亡数量","超时报告数","有源","无源","体外诊断试剂","三类数量"]#line:4665
		OO00O000OOO000O00 .loc ["合计"]=OO00O000OOO000O00 [OO0OOO000O00OOOOO ].apply (lambda O0O0O0OO0OOO00OO0 :O0O0O0OO0OOO00OO0 .sum ())#line:4666
		OO00O000OOO000O00 [OO0OOO000O00OOOOO ]=OO00O000OOO000O00 [OO0OOO000O00OOOOO ].apply (lambda OOOO0O0OO0OOO0OO0 :OOOO0O0OO0OOO0OO0 .astype (int ))#line:4667
		OO00O000OOO000O00 .iloc [-1 ,0 ]="合计"#line:4668
		OO00O000OOO000O00 ["严重比"]=round ((OO00O000OOO000O00 ["严重伤害数"]+OO00O000OOO000O00 ["死亡数量"])/OO00O000OOO000O00 ["报告数量"]*100 ,2 )#line:4670
		OO00O000OOO000O00 ["Ⅲ类比"]=round ((OO00O000OOO000O00 ["三类数量"])/OO00O000OOO000O00 ["报告数量"]*100 ,2 )#line:4671
		OO00O000OOO000O00 ["超时比"]=round ((OO00O000OOO000O00 ["超时报告数"])/OO00O000OOO000O00 ["报告数量"]*100 ,2 )#line:4672
		OO00O000OOO000O00 ["报表类型"]="dfx_user"#line:4673
		if ini ["模式"]=="药品":#line:4675
			del OO00O000OOO000O00 ["有源"]#line:4677
			del OO00O000OOO000O00 ["无源"]#line:4678
			del OO00O000OOO000O00 ["体外诊断试剂"]#line:4679
			OO00O000OOO000O00 =OO00O000OOO000O00 .rename (columns ={"三类数量":"新的和严重的数量"})#line:4680
			OO00O000OOO000O00 =OO00O000OOO000O00 .rename (columns ={"Ⅲ类比":"新严比"})#line:4681
		return OO00O000OOO000O00 #line:4683
	def df_zhenghao (O00OOOO00OO0O0O00 ):#line:4688
		""#line:4689
		O00O0OOO0O0OO00OO =O00OOOO00OO0O0O00 .df .groupby (["上市许可持有人名称","产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (证号计数 =("注册证编号/曾用注册证编号","count"),严重伤害数 =("伤害",lambda OOO000000OOOO000O :STAT_countpx (OOO000000OOOO000O .values ,"严重伤害")),死亡数量 =("伤害",lambda O000000O00OO0OO00 :STAT_countpx (O000000O00OO0OO00 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda OOO00O00OO0OOO0OO :STAT_countpx (OOO00O00OO0OOO0OO .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OO0O000O0OOOOOO00 :STAT_countpx (OO0O000O0OOOOOO00 .values ,"严重伤害待评价")),).sort_values (by ="证号计数",ascending =[False ],na_position ="last").reset_index ()#line:4704
		O00O0OOO0O0OO00OO =STAT_basic_risk (O00O0OOO0O0OO00OO ,"证号计数","严重伤害数","死亡数量","单位个数")#line:4705
		O00O0OOO0O0OO00OO =pd .merge (O00O0OOO0O0OO00OO ,STAT_recent30 (O00OOOO00OO0O0O00 .df ,["注册证编号/曾用注册证编号"]),on =["注册证编号/曾用注册证编号"],how ="left")#line:4707
		O00O0OOO0O0OO00OO ["最近30天报告数"]=O00O0OOO0O0OO00OO ["最近30天报告数"].fillna (0 ).astype (int )#line:4708
		O00O0OOO0O0OO00OO ["最近30天报告严重伤害数"]=O00O0OOO0O0OO00OO ["最近30天报告严重伤害数"].fillna (0 ).astype (int )#line:4709
		O00O0OOO0O0OO00OO ["最近30天报告死亡数量"]=O00O0OOO0O0OO00OO ["最近30天报告死亡数量"].fillna (0 ).astype (int )#line:4710
		O00O0OOO0O0OO00OO ["最近30天报告单位个数"]=O00O0OOO0O0OO00OO ["最近30天报告单位个数"].fillna (0 ).astype (int )#line:4711
		O00O0OOO0O0OO00OO ["最近30天风险评分"]=O00O0OOO0O0OO00OO ["最近30天风险评分"].fillna (0 ).astype (int )#line:4712
		O00O0OOO0O0OO00OO ["报表类型"]="dfx_zhenghao"#line:4714
		if ini ["模式"]=="药品":#line:4716
			O00O0OOO0O0OO00OO =O00O0OOO0O0OO00OO .rename (columns ={"待评价数":"新的数量"})#line:4717
			O00O0OOO0O0OO00OO =O00O0OOO0O0OO00OO .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4718
		return O00O0OOO0O0OO00OO #line:4720
	def df_pihao (O0O0O000OO0O0O00O ):#line:4722
		""#line:4723
		O0O0OO0OOO0OOOO00 =O0O0O000OO0O0O00O .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","产品批号"]).agg (批号计数 =("产品批号","count"),严重伤害数 =("伤害",lambda O00O0O0OO00O000OO :STAT_countpx (O00O0O0OO00O000OO .values ,"严重伤害")),死亡数量 =("伤害",lambda O00OO0OO00O00000O :STAT_countpx (O00OO0OO00O00000O .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda O000000000000O0O0 :STAT_countpx (O000000000000O0O0 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda OOOO000OOOO0O000O :STAT_countpx (OOOO000OOOO0O000O .values ,"严重伤害待评价")),).sort_values (by ="批号计数",ascending =[False ],na_position ="last").reset_index ()#line:4736
		O0O0OO0OOO0OOOO00 =STAT_basic_risk (O0O0OO0OOO0OOOO00 ,"批号计数","严重伤害数","死亡数量","单位个数")#line:4739
		O0O0OO0OOO0OOOO00 =pd .merge (O0O0OO0OOO0OOOO00 ,STAT_recent30 (O0O0O000OO0O0O00O .df ,["注册证编号/曾用注册证编号","产品批号"]),on =["注册证编号/曾用注册证编号","产品批号"],how ="left")#line:4741
		O0O0OO0OOO0OOOO00 ["最近30天报告数"]=O0O0OO0OOO0OOOO00 ["最近30天报告数"].fillna (0 ).astype (int )#line:4742
		O0O0OO0OOO0OOOO00 ["最近30天报告严重伤害数"]=O0O0OO0OOO0OOOO00 ["最近30天报告严重伤害数"].fillna (0 ).astype (int )#line:4743
		O0O0OO0OOO0OOOO00 ["最近30天报告死亡数量"]=O0O0OO0OOO0OOOO00 ["最近30天报告死亡数量"].fillna (0 ).astype (int )#line:4744
		O0O0OO0OOO0OOOO00 ["最近30天报告单位个数"]=O0O0OO0OOO0OOOO00 ["最近30天报告单位个数"].fillna (0 ).astype (int )#line:4745
		O0O0OO0OOO0OOOO00 ["最近30天风险评分"]=O0O0OO0OOO0OOOO00 ["最近30天风险评分"].fillna (0 ).astype (int )#line:4746
		O0O0OO0OOO0OOOO00 ["报表类型"]="dfx_pihao"#line:4748
		if ini ["模式"]=="药品":#line:4749
			O0O0OO0OOO0OOOO00 =O0O0OO0OOO0OOOO00 .rename (columns ={"待评价数":"新的数量"})#line:4750
			O0O0OO0OOO0OOOO00 =O0O0OO0OOO0OOOO00 .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4751
		return O0O0OO0OOO0OOOO00 #line:4752
	def df_xinghao (OO00OO0OO0O00OOOO ):#line:4754
		""#line:4755
		OO0O0OOO0OOOO0O0O =OO00OO0OO0O00OOOO .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","型号"]).agg (型号计数 =("型号","count"),严重伤害数 =("伤害",lambda OO000O00O00O0O000 :STAT_countpx (OO000O00O00O0O000 .values ,"严重伤害")),死亡数量 =("伤害",lambda OOOO0O00OO00OO0OO :STAT_countpx (OOOO0O00OO00OO0OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),规格个数 =("规格","nunique"),规格列表 =("规格",STAT_countx ),待评价数 =("持有人报告状态",lambda OOO0O00000OO0OO00 :STAT_countpx (OOO0O00000OO0OO00 .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O000O0OO0O00OOO00 :STAT_countpx (O000O0OO0O00OOO00 .values ,"严重伤害待评价")),).sort_values (by ="型号计数",ascending =[False ],na_position ="last").reset_index ()#line:4768
		OO0O0OOO0OOOO0O0O ["报表类型"]="dfx_xinghao"#line:4769
		if ini ["模式"]=="药品":#line:4770
			OO0O0OOO0OOOO0O0O =OO0O0OOO0OOOO0O0O .rename (columns ={"待评价数":"新的数量"})#line:4771
			OO0O0OOO0OOOO0O0O =OO0O0OOO0OOOO0O0O .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4772
		return OO0O0OOO0OOOO0O0O #line:4774
	def df_guige (O0O00OO0OOO00OOOO ):#line:4776
		""#line:4777
		O00OO0O0OO0OOOOO0 =O0O00OO0OOO00OOOO .df .groupby (["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","规格"]).agg (规格计数 =("规格","count"),严重伤害数 =("伤害",lambda O00O0O0OO0OOO0000 :STAT_countpx (O00O0O0OO0OOO0000 .values ,"严重伤害")),死亡数量 =("伤害",lambda OO0O0O0OOO0000O00 :STAT_countpx (OO0O0O0OOO0000O00 .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),批号个数 =("产品批号","nunique"),批号列表 =("产品批号",STAT_countx ),型号个数 =("型号","nunique"),型号列表 =("型号",STAT_countx ),待评价数 =("持有人报告状态",lambda OO000OOO0OO0O00OO :STAT_countpx (OO000OOO0OO0O00OO .values ,"待评价")),严重伤害待评价数 =("伤害与评价",lambda O0OO0OOOO0O000O0O :STAT_countpx (O0OO0OOOO0O000O0O .values ,"严重伤害待评价")),).sort_values (by ="规格计数",ascending =[False ],na_position ="last").reset_index ()#line:4790
		O00OO0O0OO0OOOOO0 ["报表类型"]="dfx_guige"#line:4791
		if ini ["模式"]=="药品":#line:4792
			O00OO0O0OO0OOOOO0 =O00OO0O0OO0OOOOO0 .rename (columns ={"待评价数":"新的数量"})#line:4793
			O00OO0O0OO0OOOOO0 =O00OO0O0OO0OOOOO0 .rename (columns ={"严重伤害待评价数":"新的严重的数量"})#line:4794
		return O00OO0O0OO0OOOOO0 #line:4796
	def df_findrisk (OO0O0O000O0OO0OOO ,O00OO0O0000O0O0OO ):#line:4798
		""#line:4799
		if O00OO0O0000O0O0OO =="产品批号":#line:4800
			return STAT_find_risk (OO0O0O000O0OO0OOO .df [(OO0O0O000O0OO0OOO .df ["产品类别"]!="有源")],["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],"注册证编号/曾用注册证编号",O00OO0O0000O0O0OO )#line:4801
		else :#line:4802
			return STAT_find_risk (OO0O0O000O0OO0OOO .df ,["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"],"注册证编号/曾用注册证编号",O00OO0O0000O0O0OO )#line:4803
	def df_find_all_keword_risk (OOOO00OOO0O00OOO0 ,O00OOO00O0OOOO000 ,*OOO000OOOOOO0OO00 ):#line:4805
		""#line:4806
		OO0O000OO00OOOO0O =OOOO00OOO0O00OOO0 .df .copy ()#line:4808
		OOOOOOO00OO00O0OO =time .time ()#line:4809
		OOO00OOOOOO0OO0O0 ="配置表/0（范例）比例失衡关键字库.xls"#line:4810
		if "报告类型-新的"in OO0O000OO00OOOO0O .columns :#line:4811
			OO0OO0000000O0OOO ="药品"#line:4812
		else :#line:4813
			OO0OO0000000O0OOO ="器械"#line:4814
		OOO00O000O0OOO0O0 =pd .read_excel (OOO00OOOOOO0OO0O0 ,header =0 ,sheet_name =OO0OO0000000O0OOO ).reset_index (drop =True )#line:4815
		try :#line:4818
			if len (OOO000OOOOOO0OO00 [0 ])>0 :#line:4819
				OOO00O000O0OOO0O0 =OOO00O000O0OOO0O0 .loc [OOO00O000O0OOO0O0 ["适用范围"].str .contains (OOO000OOOOOO0OO00 [0 ],na =False )].copy ().reset_index (drop =True )#line:4820
		except :#line:4821
			pass #line:4822
		O00OOO0000000OOO0 =["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号"]#line:4824
		OOO000O00OOO0O0O0 =O00OOO0000000OOO0 [-1 ]#line:4825
		O00O0O00O000O0O0O =OO0O000OO00OOOO0O .groupby (O00OOO0000000OOO0 ).agg (总数量 =(OOO000O00OOO0O0O0 ,"count"),严重伤害数 =("伤害",lambda OO0O0O0OOOOO0O0O0 :STAT_countpx (OO0O0O0OOOOO0O0O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda OOO00O0O00000O0OO :STAT_countpx (OOO00O0O00000O0OO .values ,"死亡")),)#line:4830
		OOO000O00OOO0O0O0 =O00OOO0000000OOO0 [-1 ]#line:4831
		OOO0OOOOOO0OOOOOO =O00OOO0000000OOO0 .copy ()#line:4833
		OOO0OOOOOO0OOOOOO .append (O00OOO00O0OOOO000 )#line:4834
		O0OOO00OOOO0O0O00 =OO0O000OO00OOOO0O .groupby (OOO0OOOOOO0OOOOOO ).agg (该元素总数量 =(OOO000O00OOO0O0O0 ,"count"),).reset_index ()#line:4837
		O00O0O00O000O0O0O =O00O0O00O000O0O0O [(O00O0O00O000O0O0O ["总数量"]>=3 )].reset_index ()#line:4840
		OO0O0OOO0OOOO0OO0 =[]#line:4841
		OOO000O0O00OOOOOO =0 #line:4845
		O0O0OOO0000OO00O0 =int (len (O00O0O00O000O0O0O ))#line:4846
		for OO00OO0000O0OO00O ,OOO000O0OO000OO0O ,OOO000000O00O00O0 ,O00OOO0OOO00OO0OO in zip (O00O0O00O000O0O0O ["产品名称"].values ,O00O0O00O000O0O0O ["产品类别"].values ,O00O0O00O000O0O0O [OOO000O00OOO0O0O0 ].values ,O00O0O00O000O0O0O ["总数量"].values ):#line:4847
			OOO000O0O00OOOOOO +=1 #line:4848
			if (time .time ()-OOOOOOO00OO00O0OO )>3 :#line:4850
				root .attributes ("-topmost",True )#line:4851
				PROGRAM_change_schedule (OOO000O0O00OOOOOO ,O0O0OOO0000OO00O0 )#line:4852
				root .attributes ("-topmost",False )#line:4853
			OO000OO000OO0OO00 =OO0O000OO00OOOO0O [(OO0O000OO00OOOO0O [OOO000O00OOO0O0O0 ]==OOO000000O00O00O0 )].copy ()#line:4854
			OOO00O000O0OOO0O0 ["SELECT"]=OOO00O000O0OOO0O0 .apply (lambda O0O000O0000000O00 :(O0O000O0000000O00 ["适用范围"]in OO00OO0000O0OO00O )or (O0O000O0000000O00 ["适用范围"]in OOO000O0OO000OO0O )or (O0O000O0000000O00 ["适用范围"]=="通用"),axis =1 )#line:4855
			OOOOO00O0O0OO0000 =OOO00O000O0OOO0O0 [(OOO00O000O0OOO0O0 ["SELECT"]==True )].reset_index ()#line:4856
			if len (OOOOO00O0O0OO0000 )>0 :#line:4857
				for O0OO0O000OO0O0OOO ,O0OOO0O000000O00O ,OOO00O0O0O0OO0O00 in zip (OOOOO00O0O0OO0000 ["值"].values ,OOOOO00O0O0OO0000 ["查找位置"].values ,OOOOO00O0O0OO0000 ["排除值"].values ):#line:4859
					O00000OOOOO00O00O =OO000OO000OO0OO00 .copy ()#line:4860
					O0OO00O0O0O0O0O0O =TOOLS_get_list (O0OO0O000OO0O0OOO )[0 ]#line:4861
					O00000OOOOO00O00O ["关键字查找列"]=""#line:4863
					for O00O0000OOOOO0OOO in TOOLS_get_list (O0OOO0O000000O00O ):#line:4864
						O00000OOOOO00O00O ["关键字查找列"]=O00000OOOOO00O00O ["关键字查找列"]+O00000OOOOO00O00O [O00O0000OOOOO0OOO ].astype ("str")#line:4865
					O00000OOOOO00O00O .loc [O00000OOOOO00O00O ["关键字查找列"].str .contains (O0OO0O000OO0O0OOO ,na =False ),"关键字"]=O0OO00O0O0O0O0O0O #line:4867
					if str (OOO00O0O0O0OO0O00 )!="nan":#line:4870
						O00000OOOOO00O00O =O00000OOOOO00O00O .loc [~O00000OOOOO00O00O ["关键字查找列"].str .contains (OOO00O0O0O0OO0O00 ,na =False )].copy ()#line:4871
					if (len (O00000OOOOO00O00O ))<1 :#line:4873
						continue #line:4874
					O0OOOOO0OOO000O00 =STAT_find_keyword_risk (O00000OOOOO00O00O ,["上市许可持有人名称","产品类别","产品名称","注册证编号/曾用注册证编号","关键字"],"关键字",O00OOO00O0OOOO000 ,int (O00OOO0OOO00OO0OO ))#line:4876
					if len (O0OOOOO0OOO000O00 )>0 :#line:4877
						O0OOOOO0OOO000O00 ["关键字组合"]=O0OO0O000OO0O0OOO #line:4878
						O0OOOOO0OOO000O00 ["排除值"]=OOO00O0O0O0OO0O00 #line:4879
						O0OOOOO0OOO000O00 ["关键字查找列"]=O0OOO0O000000O00O #line:4880
						OO0O0OOO0OOOO0OO0 .append (O0OOOOO0OOO000O00 )#line:4881
		O0OO00OOOO00000O0 =pd .concat (OO0O0OOO0OOOO0OO0 )#line:4885
		O0OO00OOOO00000O0 =pd .merge (O0OO00OOOO00000O0 ,O0OOO00OOOO0O0O00 ,on =OOO0OOOOOO0OOOOOO ,how ="left")#line:4888
		O0OO00OOOO00000O0 ["关键字数量比例"]=round (O0OO00OOOO00000O0 ["计数"]/O0OO00OOOO00000O0 ["该元素总数量"],2 )#line:4889
		O0OO00OOOO00000O0 =O0OO00OOOO00000O0 .reset_index (drop =True )#line:4891
		if len (O0OO00OOOO00000O0 )>0 :#line:4892
			O0OO00OOOO00000O0 ["风险评分"]=0 #line:4893
			O0OO00OOOO00000O0 ["报表类型"]="keyword_findrisk"+O00OOO00O0OOOO000 #line:4894
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["计数"]>=3 ),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+3 #line:4895
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["计数"]>=(O0OO00OOOO00000O0 ["数量均值"]+O0OO00OOOO00000O0 ["数量标准差"])),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+1 #line:4896
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["计数"]>=O0OO00OOOO00000O0 ["数量CI"]),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+1 #line:4897
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["关键字数量比例"]>0.5 )&(O0OO00OOOO00000O0 ["计数"]>=3 ),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+1 #line:4898
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["严重伤害数"]>=3 ),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+1 #line:4899
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["单位个数"]>=3 ),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+1 #line:4900
			O0OO00OOOO00000O0 .loc [(O0OO00OOOO00000O0 ["死亡数量"]>=1 ),"风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+10 #line:4901
			O0OO00OOOO00000O0 ["风险评分"]=O0OO00OOOO00000O0 ["风险评分"]+O0OO00OOOO00000O0 ["单位个数"]/100 #line:4902
			O0OO00OOOO00000O0 =O0OO00OOOO00000O0 .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:4903
		print ("耗时：",(time .time ()-OOOOOOO00OO00O0OO ))#line:4909
		return O0OO00OOOO00000O0 #line:4910
	def df_ror (OO00O000O0O000OOO ,OO00OOO0OO0OO00O0 ,*OO0OOOO0O0O0O00O0 ):#line:4913
		""#line:4914
		OOOO00000OOO0OO0O =OO00O000O0O000OOO .df .copy ()#line:4916
		O00OO00OO0O0O00O0 =time .time ()#line:4917
		O0O0O0O000OOO00O0 ="配置表/0（范例）比例失衡关键字库.xls"#line:4918
		if "报告类型-新的"in OOOO00000OOO0OO0O .columns :#line:4919
			OO0OO0OO00OO00O0O ="药品"#line:4920
		else :#line:4922
			OO0OO0OO00OO00O0O ="器械"#line:4923
		OOOOO0O00OOO0OOO0 =pd .read_excel (O0O0O0O000OOO00O0 ,header =0 ,sheet_name =OO0OO0OO00OO00O0O ).reset_index (drop =True )#line:4924
		if "css"in OOOO00000OOO0OO0O .columns :#line:4927
			O0OOO00OO00OOOO0O =OOOO00000OOO0OO0O .copy ()#line:4928
			O0OOO00OO00OOOO0O ["器械故障表现"]=O0OOO00OO00OOOO0O ["器械故障表现"].fillna ("未填写")#line:4929
			O0OOO00OO00OOOO0O ["器械故障表现"]=O0OOO00OO00OOOO0O ["器械故障表现"].str .replace ("*","",regex =False )#line:4930
			OOO0OOO00000OOO0O ="use("+str ("器械故障表现")+").file"#line:4931
			O0000OO00O0000000 =str (Counter (TOOLS_get_list0 (OOO0OOO00000OOO0O ,O0OOO00OO00OOOO0O ,1000 ))).replace ("Counter({","{")#line:4932
			O0000OO00O0000000 =O0000OO00O0000000 .replace ("})","}")#line:4933
			O0000OO00O0000000 =ast .literal_eval (O0000OO00O0000000 )#line:4934
			OOOOO0O00OOO0OOO0 =pd .DataFrame .from_dict (O0000OO00O0000000 ,orient ="index",columns =["计数"]).reset_index ()#line:4935
			OOOOO0O00OOO0OOO0 ["适用范围列"]="产品类别"#line:4936
			OOOOO0O00OOO0OOO0 ["适用范围"]="无源"#line:4937
			OOOOO0O00OOO0OOO0 ["查找位置"]="伤害表现"#line:4938
			OOOOO0O00OOO0OOO0 ["值"]=OOOOO0O00OOO0OOO0 ["index"]#line:4939
			OOOOO0O00OOO0OOO0 ["排除值"]="-没有排除值-"#line:4940
			del OOOOO0O00OOO0OOO0 ["index"]#line:4941
		O0O00O0O0OOO0OO0O =OO00OOO0OO0OO00O0 [-2 ]#line:4944
		OOOO0OO00O0000OO0 =OO00OOO0OO0OO00O0 [-1 ]#line:4945
		O0O000O0OO0OO00OO =OO00OOO0OO0OO00O0 [:-1 ]#line:4946
		try :#line:4949
			if len (OO0OOOO0O0O0O00O0 [0 ])>0 :#line:4950
				O0O00O0O0OOO0OO0O =OO00OOO0OO0OO00O0 [-3 ]#line:4951
				OOOOO0O00OOO0OOO0 =OOOOO0O00OOO0OOO0 .loc [OOOOO0O00OOO0OOO0 ["适用范围"].str .contains (OO0OOOO0O0O0O00O0 [0 ],na =False )].copy ().reset_index (drop =True )#line:4952
				O0OO000O00000000O =OOOO00000OOO0OO0O .groupby (["产品类别","规整后品类","产品名称","注册证编号/曾用注册证编号"]).agg (该元素总数量 =(OOOO0OO00O0000OO0 ,"count"),该元素严重伤害数 =("伤害",lambda OOO0O00OOO00O0OO0 :STAT_countpx (OOO0O00OOO00O0OO0 .values ,"严重伤害")),该元素死亡数量 =("伤害",lambda O00O000O0000OO00O :STAT_countpx (O00O000O0000OO00O .values ,"死亡")),该元素单位个数 =("单位名称","nunique"),该元素单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:4959
				OOOO000OO0O0OO0O0 =OOOO00000OOO0OO0O .groupby (["产品类别","规整后品类"]).agg (所有元素总数量 =(O0O00O0O0OOO0OO0O ,"count"),所有元素严重伤害数 =("伤害",lambda O0OOOO0O0OOOOOO0O :STAT_countpx (O0OOOO0O0OOOOOO0O .values ,"严重伤害")),所有元素死亡数量 =("伤害",lambda OO0OOOO0O0OO0OO00 :STAT_countpx (OO0OOOO0O0OO0OO00 .values ,"死亡")),)#line:4964
				if len (OOOO000OO0O0OO0O0 )>1 :#line:4965
					text .insert (END ,"注意，产品类别有两种，产品名称规整疑似不正确！")#line:4966
				O0OO000O00000000O =pd .merge (O0OO000O00000000O ,OOOO000OO0O0OO0O0 ,on =["产品类别","规整后品类"],how ="left").reset_index ()#line:4968
		except :#line:4970
			text .insert (END ,"\n目前结果为未进行名称规整的结果！\n")#line:4971
			O0OO000O00000000O =OOOO00000OOO0OO0O .groupby (OO00OOO0OO0OO00O0 ).agg (该元素总数量 =(OOOO0OO00O0000OO0 ,"count"),该元素严重伤害数 =("伤害",lambda O00OOO0OO000OO000 :STAT_countpx (O00OOO0OO000OO000 .values ,"严重伤害")),该元素死亡数量 =("伤害",lambda O0OO00O000OO0OOOO :STAT_countpx (O0OO00O000OO0OOOO .values ,"死亡")),该元素单位个数 =("单位名称","nunique"),该元素单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:4978
			OOOO000OO0O0OO0O0 =OOOO00000OOO0OO0O .groupby (O0O000O0OO0OO00OO ).agg (所有元素总数量 =(O0O00O0O0OOO0OO0O ,"count"),所有元素严重伤害数 =("伤害",lambda O00000O0OOO0O0O0O :STAT_countpx (O00000O0OOO0O0O0O .values ,"严重伤害")),所有元素死亡数量 =("伤害",lambda O0O00OO00OO000O0O :STAT_countpx (O0O00OO00OO000O0O .values ,"死亡")),)#line:4984
			O0OO000O00000000O =pd .merge (O0OO000O00000000O ,OOOO000OO0O0OO0O0 ,on =O0O000O0OO0OO00OO ,how ="left").reset_index ()#line:4988
		OOOO000OO0O0OO0O0 =OOOO000OO0O0OO0O0 [(OOOO000OO0O0OO0O0 ["所有元素总数量"]>=3 )].reset_index ()#line:4990
		O0O0000000O000OO0 =[]#line:4991
		if ("产品名称"not in OOOO000OO0O0OO0O0 .columns )and ("规整后品类"not in OOOO000OO0O0OO0O0 .columns ):#line:4993
			OOOO000OO0O0OO0O0 ["产品名称"]=OOOO000OO0O0OO0O0 ["产品类别"]#line:4994
		if "规整后品类"not in OOOO000OO0O0OO0O0 .columns :#line:5000
			OOOO000OO0O0OO0O0 ["规整后品类"]="不适用"#line:5001
		O0O0O000OOO000O00 =0 #line:5004
		O0000O0OOO00OOOO0 =int (len (OOOO000OO0O0OO0O0 ))#line:5005
		for O0O00O0O0OO000000 ,OO0OO0OOO0O0O0O00 ,OO0OO0OOOO000O000 ,OO0OOOO0OO000O00O in zip (OOOO000OO0O0OO0O0 ["规整后品类"],OOOO000OO0O0OO0O0 ["产品类别"],OOOO000OO0O0OO0O0 [O0O00O0O0OOO0OO0O ],OOOO000OO0O0OO0O0 ["所有元素总数量"]):#line:5006
			O0O0O000OOO000O00 +=1 #line:5007
			if (time .time ()-O00OO00OO0O0O00O0 )>3 :#line:5008
				root .attributes ("-topmost",True )#line:5009
				PROGRAM_change_schedule (O0O0O000OOO000O00 ,O0000O0OOO00OOOO0 )#line:5010
				root .attributes ("-topmost",False )#line:5011
			OO000OOOO00OO0OOO =OOOO00000OOO0OO0O [(OOOO00000OOO0OO0O [O0O00O0O0OOO0OO0O ]==OO0OO0OOOO000O000 )].copy ()#line:5012
			OOOOO0O00OOO0OOO0 ["SELECT"]=OOOOO0O00OOO0OOO0 .apply (lambda OOOOOO00O00OOOO00 :((O0O00O0O0OO000000 in OOOOOO00O00OOOO00 ["适用范围"])or (OOOOOO00O00OOOO00 ["适用范围"]in OO0OO0OOO0O0O0O00 )),axis =1 )#line:5013
			O0OO0OOO0O00OOO00 =OOOOO0O00OOO0OOO0 [(OOOOO0O00OOO0OOO0 ["SELECT"]==True )].reset_index ()#line:5014
			if len (O0OO0OOO0O00OOO00 )>0 :#line:5015
				for O0OO0O0O000OOO00O ,OO00OO0000OOOO000 ,O00O0O00O00000000 in zip (O0OO0OOO0O00OOO00 ["值"].values ,O0OO0OOO0O00OOO00 ["查找位置"].values ,O0OO0OOO0O00OOO00 ["排除值"].values ):#line:5017
					O000OO0O00O0O0OO0 =OO000OOOO00OO0OOO .copy ()#line:5018
					OOO000O000O00O0OO =TOOLS_get_list (O0OO0O0O000OOO00O )[0 ]#line:5019
					OOOO0O0OOO00OOOOO ="关键字查找列"#line:5020
					O000OO0O00O0O0OO0 [OOOO0O0OOO00OOOOO ]=""#line:5021
					for O000OOO00O0O0OO0O in TOOLS_get_list (OO00OO0000OOOO000 ):#line:5022
						O000OO0O00O0O0OO0 [OOOO0O0OOO00OOOOO ]=O000OO0O00O0O0OO0 [OOOO0O0OOO00OOOOO ]+O000OO0O00O0O0OO0 [O000OOO00O0O0OO0O ].astype ("str")#line:5023
					O000OO0O00O0O0OO0 .loc [O000OO0O00O0O0OO0 [OOOO0O0OOO00OOOOO ].str .contains (O0OO0O0O000OOO00O ,na =False ),"关键字"]=OOO000O000O00O0OO #line:5025
					if str (O00O0O00O00000000 )!="nan":#line:5028
						O000OO0O00O0O0OO0 =O000OO0O00O0O0OO0 .loc [~O000OO0O00O0O0OO0 ["关键字查找列"].str .contains (O00O0O00O00000000 ,na =False )].copy ()#line:5029
					if (len (O000OO0O00O0O0OO0 ))<1 :#line:5032
						continue #line:5033
					for O00O00O0O0OO0O00O in zip (O000OO0O00O0O0OO0 [OOOO0OO00O0000OO0 ].drop_duplicates ()):#line:5035
						try :#line:5038
							if O00O00O0O0OO0O00O [0 ]!=OO0OOOO0O0O0O00O0 [1 ]:#line:5039
								continue #line:5040
						except :#line:5041
							pass #line:5042
						OO0OO00OOOO0O0O0O ={"合并列":{OOOO0O0OOO00OOOOO :OO00OO0000OOOO000 },"等于":{O0O00O0O0OOO0OO0O :OO0OO0OOOO000O000 ,OOOO0OO00O0000OO0 :O00O00O0O0OO0O00O [0 ]},"不等于":{},"包含":{OOOO0O0OOO00OOOOO :O0OO0O0O000OOO00O },"不包含":{OOOO0O0OOO00OOOOO :O00O0O00O00000000 }}#line:5050
						OOO0OOOOO00OO0OO0 =STAT_PPR_ROR_1 (OOOO0OO00O0000OO0 ,str (O00O00O0O0OO0O00O [0 ]),"关键字查找列",O0OO0O0O000OOO00O ,O000OO0O00O0O0OO0 )+(O0OO0O0O000OOO00O ,O00O0O00O00000000 ,OO00OO0000OOOO000 ,OO0OO0OOOO000O000 ,O00O00O0O0OO0O00O [0 ],str (OO0OO00OOOO0O0O0O ))#line:5052
						if OOO0OOOOO00OO0OO0 [1 ]>0 :#line:5054
							OOOO00O00OOOO0O0O =pd .DataFrame (columns =["特定关键字","出现频次","占比","ROR值","ROR值的95%CI下限","PRR值","PRR值的95%CI下限","卡方值","四分表","关键字组合","排除值","关键字查找列",O0O00O0O0OOO0OO0O ,OOOO0OO00O0000OO0 ,"报表定位"])#line:5056
							OOOO00O00OOOO0O0O .loc [0 ]=OOO0OOOOO00OO0OO0 #line:5057
							O0O0000000O000OO0 .append (OOOO00O00OOOO0O0O )#line:5058
		O0O00OOOO00O0OOOO =pd .concat (O0O0000000O000OO0 )#line:5062
		O0O00OOOO00O0OOOO =pd .merge (O0OO000O00000000O ,O0O00OOOO00O0OOOO ,on =[O0O00O0O0OOO0OO0O ,OOOO0OO00O0000OO0 ],how ="right")#line:5066
		O0O00OOOO00O0OOOO =O0O00OOOO00O0OOOO .reset_index (drop =True )#line:5067
		del O0O00OOOO00O0OOOO ["index"]#line:5068
		if len (O0O00OOOO00O0OOOO )>0 :#line:5069
			O0O00OOOO00O0OOOO ["风险评分"]=0 #line:5070
			O0O00OOOO00O0OOOO ["报表类型"]="ROR"#line:5071
			O0O00OOOO00O0OOOO .loc [(O0O00OOOO00O0OOOO ["出现频次"]>=3 ),"风险评分"]=O0O00OOOO00O0OOOO ["风险评分"]+3 #line:5072
			O0O00OOOO00O0OOOO .loc [(O0O00OOOO00O0OOOO ["ROR值的95%CI下限"]>1 ),"风险评分"]=O0O00OOOO00O0OOOO ["风险评分"]+1 #line:5073
			O0O00OOOO00O0OOOO .loc [(O0O00OOOO00O0OOOO ["PRR值的95%CI下限"]>1 ),"风险评分"]=O0O00OOOO00O0OOOO ["风险评分"]+1 #line:5074
			O0O00OOOO00O0OOOO ["风险评分"]=O0O00OOOO00O0OOOO ["风险评分"]+O0O00OOOO00O0OOOO ["该元素单位个数"]/100 #line:5075
			O0O00OOOO00O0OOOO =O0O00OOOO00O0OOOO .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:5076
		print ("耗时：",(time .time ()-O00OO00OO0O0O00O0 ))#line:5082
		return O0O00OOOO00O0OOOO #line:5083
	def df_chiyouren (O0O0O0O00O00OOO0O ):#line:5089
		""#line:5090
		OOO0000OOO0000O00 =O0O0O0O00O00OOO0O .df .copy ().reset_index (drop =True )#line:5091
		OOO0000OOO0000O00 ["总报告数"]=data ["报告编码"].copy ()#line:5092
		OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"总待评价数量"]=data ["报告编码"]#line:5093
		OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["伤害"]=="严重伤害"),"严重伤害报告数"]=data ["报告编码"]#line:5094
		OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价")&(OOO0000OOO0000O00 ["伤害"]=="严重伤害"),"严重伤害待评价数量"]=data ["报告编码"]#line:5095
		OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价")&(OOO0000OOO0000O00 ["伤害"]=="其他"),"其他待评价数量"]=data ["报告编码"]#line:5096
		O00OOOOO0O00O0OO0 =OOO0000OOO0000O00 .groupby (["上市许可持有人名称"]).aggregate ({"总报告数":"nunique","总待评价数量":"nunique","严重伤害报告数":"nunique","严重伤害待评价数量":"nunique","其他待评价数量":"nunique"})#line:5099
		O00OOOOO0O00O0OO0 ["严重伤害待评价比例"]=round (O00OOOOO0O00O0OO0 ["严重伤害待评价数量"]/O00OOOOO0O00O0OO0 ["严重伤害报告数"]*100 ,2 )#line:5104
		O00OOOOO0O00O0OO0 ["总待评价比例"]=round (O00OOOOO0O00O0OO0 ["总待评价数量"]/O00OOOOO0O00O0OO0 ["总报告数"]*100 ,2 )#line:5107
		O00OOOOO0O00O0OO0 ["总报告数"]=O00OOOOO0O00O0OO0 ["总报告数"].fillna (0 )#line:5108
		O00OOOOO0O00O0OO0 ["总待评价比例"]=O00OOOOO0O00O0OO0 ["总待评价比例"].fillna (0 )#line:5109
		O00OOOOO0O00O0OO0 ["严重伤害报告数"]=O00OOOOO0O00O0OO0 ["严重伤害报告数"].fillna (0 )#line:5110
		O00OOOOO0O00O0OO0 ["严重伤害待评价比例"]=O00OOOOO0O00O0OO0 ["严重伤害待评价比例"].fillna (0 )#line:5111
		O00OOOOO0O00O0OO0 ["总报告数"]=O00OOOOO0O00O0OO0 ["总报告数"].astype (int )#line:5112
		O00OOOOO0O00O0OO0 ["总待评价比例"]=O00OOOOO0O00O0OO0 ["总待评价比例"].astype (int )#line:5113
		O00OOOOO0O00O0OO0 ["严重伤害报告数"]=O00OOOOO0O00O0OO0 ["严重伤害报告数"].astype (int )#line:5114
		O00OOOOO0O00O0OO0 ["严重伤害待评价比例"]=O00OOOOO0O00O0OO0 ["严重伤害待评价比例"].astype (int )#line:5115
		O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .sort_values (by =["总报告数","总待评价比例"],ascending =[False ,False ],na_position ="last")#line:5118
		if "场所名称"in OOO0000OOO0000O00 .columns :#line:5120
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["审核日期"]=="未填写"),"审核日期"]=3000 -12 -12 #line:5121
			OOO0000OOO0000O00 ["报告时限"]=pd .Timestamp .today ()-pd .to_datetime (OOO0000OOO0000O00 ["审核日期"])#line:5122
			OOO0000OOO0000O00 ["报告时限2"]=45 -(pd .Timestamp .today ()-pd .to_datetime (OOO0000OOO0000O00 ["审核日期"])).dt .days #line:5123
			OOO0000OOO0000O00 ["报告时限"]=OOO0000OOO0000O00 ["报告时限"].dt .days #line:5124
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限"]>45 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"待评价且超出当前日期45天（严重）"]=1 #line:5125
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限"]>45 )&(OOO0000OOO0000O00 ["伤害"]=="其他")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"待评价且超出当前日期45天（其他）"]=1 #line:5126
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限"]>30 )&(OOO0000OOO0000O00 ["伤害"]=="死亡")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"待评价且超出当前日期30天（死亡）"]=1 #line:5127
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]<=1 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["报告时限2"]>0 )&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩1天"]=1 #line:5129
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]>1 )&(OOO0000OOO0000O00 ["报告时限2"]<=3 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩1-3天"]=1 #line:5130
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]>3 )&(OOO0000OOO0000O00 ["报告时限2"]<=5 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩3-5天"]=1 #line:5131
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]>5 )&(OOO0000OOO0000O00 ["报告时限2"]<=10 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩5-10天"]=1 #line:5132
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]>10 )&(OOO0000OOO0000O00 ["报告时限2"]<=20 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩10-20天"]=1 #line:5133
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]>20 )&(OOO0000OOO0000O00 ["报告时限2"]<=30 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩20-30天"]=1 #line:5134
			OOO0000OOO0000O00 .loc [(OOO0000OOO0000O00 ["报告时限2"]>30 )&(OOO0000OOO0000O00 ["报告时限2"]<=45 )&(OOO0000OOO0000O00 ["伤害"]=="严重伤害")&(OOO0000OOO0000O00 ["持有人报告状态"]=="待评价"),"严重待评价且只剩30-45天"]=1 #line:5135
			del OOO0000OOO0000O00 ["报告时限2"]#line:5136
			O0OO000000OO0OO00 =(OOO0000OOO0000O00 .groupby (["上市许可持有人名称"]).aggregate ({"待评价且超出当前日期45天（严重）":"sum","待评价且超出当前日期45天（其他）":"sum","待评价且超出当前日期30天（死亡）":"sum","严重待评价且只剩1天":"sum","严重待评价且只剩1-3天":"sum","严重待评价且只剩3-5天":"sum","严重待评价且只剩5-10天":"sum","严重待评价且只剩10-20天":"sum","严重待评价且只剩20-30天":"sum","严重待评价且只剩30-45天":"sum"}).reset_index ())#line:5138
			O00OOOOO0O00O0OO0 =pd .merge (O00OOOOO0O00O0OO0 ,O0OO000000OO0OO00 ,on =["上市许可持有人名称"],how ="outer",)#line:5139
			O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（严重）"]=O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（严重）"].fillna (0 )#line:5140
			O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（严重）"]=O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（严重）"].astype (int )#line:5141
			O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（其他）"]=O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（其他）"].fillna (0 )#line:5142
			O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（其他）"]=O00OOOOO0O00O0OO0 ["待评价且超出当前日期45天（其他）"].astype (int )#line:5143
			O00OOOOO0O00O0OO0 ["待评价且超出当前日期30天（死亡）"]=O00OOOOO0O00O0OO0 ["待评价且超出当前日期30天（死亡）"].fillna (0 )#line:5144
			O00OOOOO0O00O0OO0 ["待评价且超出当前日期30天（死亡）"]=O00OOOOO0O00O0OO0 ["待评价且超出当前日期30天（死亡）"].astype (int )#line:5145
			O00OOOOO0O00O0OO0 ["严重待评价且只剩1天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩1天"].fillna (0 )#line:5147
			O00OOOOO0O00O0OO0 ["严重待评价且只剩1天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩1天"].astype (int )#line:5148
			O00OOOOO0O00O0OO0 ["严重待评价且只剩1-3天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩1-3天"].fillna (0 )#line:5149
			O00OOOOO0O00O0OO0 ["严重待评价且只剩1-3天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩1-3天"].astype (int )#line:5150
			O00OOOOO0O00O0OO0 ["严重待评价且只剩3-5天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩3-5天"].fillna (0 )#line:5151
			O00OOOOO0O00O0OO0 ["严重待评价且只剩3-5天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩3-5天"].astype (int )#line:5152
			O00OOOOO0O00O0OO0 ["严重待评价且只剩5-10天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩5-10天"].fillna (0 )#line:5153
			O00OOOOO0O00O0OO0 ["严重待评价且只剩5-10天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩5-10天"].astype (int )#line:5154
			O00OOOOO0O00O0OO0 ["严重待评价且只剩10-20天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩10-20天"].fillna (0 )#line:5155
			O00OOOOO0O00O0OO0 ["严重待评价且只剩10-20天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩10-20天"].astype (int )#line:5156
			O00OOOOO0O00O0OO0 ["严重待评价且只剩20-30天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩20-30天"].fillna (0 )#line:5157
			O00OOOOO0O00O0OO0 ["严重待评价且只剩20-30天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩20-30天"].astype (int )#line:5158
			O00OOOOO0O00O0OO0 ["严重待评价且只剩30-45天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩30-45天"].fillna (0 )#line:5159
			O00OOOOO0O00O0OO0 ["严重待评价且只剩30-45天"]=O00OOOOO0O00O0OO0 ["严重待评价且只剩30-45天"].astype (int )#line:5160
		O00OOOOO0O00O0OO0 ["总待评价数量"]=O00OOOOO0O00O0OO0 ["总待评价数量"].fillna (0 )#line:5162
		O00OOOOO0O00O0OO0 ["总待评价数量"]=O00OOOOO0O00O0OO0 ["总待评价数量"].astype (int )#line:5163
		O00OOOOO0O00O0OO0 ["严重伤害待评价数量"]=O00OOOOO0O00O0OO0 ["严重伤害待评价数量"].fillna (0 )#line:5164
		O00OOOOO0O00O0OO0 ["严重伤害待评价数量"]=O00OOOOO0O00O0OO0 ["严重伤害待评价数量"].astype (int )#line:5165
		O00OOOOO0O00O0OO0 ["其他待评价数量"]=O00OOOOO0O00O0OO0 ["其他待评价数量"].fillna (0 )#line:5166
		O00OOOOO0O00O0OO0 ["其他待评价数量"]=O00OOOOO0O00O0OO0 ["其他待评价数量"].astype (int )#line:5167
		O0O0O0000O0OOO0OO =["总报告数","总待评价数量","严重伤害报告数","严重伤害待评价数量","其他待评价数量"]#line:5170
		O00OOOOO0O00O0OO0 .loc ["合计"]=O00OOOOO0O00O0OO0 [O0O0O0000O0OOO0OO ].apply (lambda O0OOOOOO000O00OOO :O0OOOOOO000O00OOO .sum ())#line:5171
		O00OOOOO0O00O0OO0 [O0O0O0000O0OOO0OO ]=O00OOOOO0O00O0OO0 [O0O0O0000O0OOO0OO ].apply (lambda OO0000O0000OOO0O0 :OO0000O0000OOO0O0 .astype (int ))#line:5172
		O00OOOOO0O00O0OO0 .iloc [-1 ,0 ]="合计"#line:5173
		if "场所名称"in OOO0000OOO0000O00 .columns :#line:5175
			O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .reset_index (drop =True )#line:5176
		else :#line:5177
			O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .reset_index ()#line:5178
		if ini ["模式"]=="药品":#line:5180
			O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .rename (columns ={"总待评价数量":"新的数量"})#line:5181
			O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .rename (columns ={"严重伤害待评价数量":"新的严重的数量"})#line:5182
			O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .rename (columns ={"严重伤害待评价比例":"新的严重的比例"})#line:5183
			O00OOOOO0O00O0OO0 =O00OOOOO0O00O0OO0 .rename (columns ={"总待评价比例":"新的比例"})#line:5184
			del O00OOOOO0O00O0OO0 ["其他待评价数量"]#line:5186
		O00OOOOO0O00O0OO0 ["报表类型"]="dfx_chiyouren"#line:5187
		return O00OOOOO0O00O0OO0 #line:5188
	def df_age (OOOO0O0O00OO0O000 ):#line:5190
		""#line:5191
		OO000O00O0OO00000 =OOOO0O0O00OO0O000 .df .copy ()#line:5192
		OO000O00O0OO00000 =OO000O00O0OO00000 .drop_duplicates ("报告编码").copy ()#line:5193
		O0O000OOOOO0O000O =pd .pivot_table (OO000O00O0OO00000 .drop_duplicates ("报告编码"),values =["报告编码"],index ="年龄段",columns ="性别",aggfunc ={"报告编码":"nunique"},fill_value ="0",margins =True ,dropna =False ,).rename (columns ={"报告编码":"数量"}).reset_index ()#line:5194
		O0O000OOOOO0O000O .columns =O0O000OOOOO0O000O .columns .droplevel (0 )#line:5195
		O0O000OOOOO0O000O ["构成比(%)"]=round (100 *O0O000OOOOO0O000O ["All"]/len (OO000O00O0OO00000 ),2 )#line:5196
		O0O000OOOOO0O000O ["累计构成比(%)"]=O0O000OOOOO0O000O ["构成比(%)"].cumsum ()#line:5197
		O0O000OOOOO0O000O ["报表类型"]="年龄性别表"#line:5198
		return O0O000OOOOO0O000O #line:5199
	def df_psur (O0O00000000O00O0O ,*OO000O00000OOOOO0 ):#line:5201
		""#line:5202
		O0O0O000O0O000OO0 =O0O00000000O00O0O .df .copy ()#line:5203
		O00O0O0000O00O0O0 ="配置表/0（范例）比例失衡关键字库.xls"#line:5204
		O000O0OO00OO00000 =len (O0O0O000O0O000OO0 .drop_duplicates ("报告编码"))#line:5205
		if "报告类型-新的"in O0O0O000O0O000OO0 .columns :#line:5209
			OO0O000OOOO00O0OO ="药品"#line:5210
		elif "皮损形态"in O0O0O000O0O000OO0 .columns :#line:5211
			OO0O000OOOO00O0OO ="化妆品"#line:5212
		else :#line:5213
			OO0O000OOOO00O0OO ="器械"#line:5214
		O0O00OO0O0O0OO000 =pd .read_excel (O00O0O0000O00O0O0 ,header =0 ,sheet_name =OO0O000OOOO00O0OO )#line:5217
		OOO000O00O00OOO0O =(O0O00OO0O0O0OO000 .loc [O0O00OO0O0O0OO000 ["适用范围"].str .contains ("通用监测关键字|无源|有源",na =False )].copy ().reset_index (drop =True ))#line:5220
		try :#line:5223
			if OO000O00000OOOOO0 [0 ]in ["特定品种","通用无源","通用有源"]:#line:5224
				OOO0000O00OO000O0 =""#line:5225
				if OO000O00000OOOOO0 [0 ]=="特定品种":#line:5226
					OOO0000O00OO000O0 =O0O00OO0O0O0OO000 .loc [O0O00OO0O0O0OO000 ["适用范围"].str .contains (OO000O00000OOOOO0 [1 ],na =False )].copy ().reset_index (drop =True )#line:5227
				if OO000O00000OOOOO0 [0 ]=="通用无源":#line:5229
					OOO0000O00OO000O0 =O0O00OO0O0O0OO000 .loc [O0O00OO0O0O0OO000 ["适用范围"].str .contains ("通用监测关键字|无源",na =False )].copy ().reset_index (drop =True )#line:5230
				if OO000O00000OOOOO0 [0 ]=="通用有源":#line:5231
					OOO0000O00OO000O0 =O0O00OO0O0O0OO000 .loc [O0O00OO0O0O0OO000 ["适用范围"].str .contains ("通用监测关键字|有源",na =False )].copy ().reset_index (drop =True )#line:5232
				if OO000O00000OOOOO0 [0 ]=="体外诊断试剂":#line:5233
					OOO0000O00OO000O0 =O0O00OO0O0O0OO000 .loc [O0O00OO0O0O0OO000 ["适用范围"].str .contains ("体外诊断试剂",na =False )].copy ().reset_index (drop =True )#line:5234
				if len (OOO0000O00OO000O0 )<1 :#line:5235
					showinfo (title ="提示",message ="未找到相应的自定义规则，任务结束。")#line:5236
					return 0 #line:5237
				else :#line:5238
					OOO000O00O00OOO0O =OOO0000O00OO000O0 #line:5239
		except :#line:5241
			pass #line:5242
		try :#line:5246
			if OO0O000OOOO00O0OO =="器械"and OO000O00000OOOOO0 [0 ]=="特定品种作为通用关键字":#line:5247
				OOO000O00O00OOO0O =OO000O00000OOOOO0 [1 ]#line:5248
		except dddd :#line:5250
			pass #line:5251
		O0000O0O0OO0OOOO0 =""#line:5254
		O0O0O0O00O0OOOO0O ="-其他关键字-不含："#line:5255
		for O0OOO0O00O0000O00 ,OO00O00O000O0000O in OOO000O00O00OOO0O .iterrows ():#line:5256
			O0O0O0O00O0OOOO0O =O0O0O0O00O0OOOO0O +"|"+str (OO00O00O000O0000O ["值"])#line:5257
			O0OO0O0OOOOO0OOOO =OO00O00O000O0000O #line:5258
		O0OO0O0OOOOO0OOOO [2 ]="通用监测关键字"#line:5259
		O0OO0O0OOOOO0OOOO [4 ]=O0O0O0O00O0OOOO0O #line:5260
		OOO000O00O00OOO0O .loc [len (OOO000O00O00OOO0O )]=O0OO0O0OOOOO0OOOO #line:5261
		OOO000O00O00OOO0O =OOO000O00O00OOO0O .reset_index (drop =True )#line:5262
		if ini ["模式"]=="器械":#line:5266
			O0O0O000O0O000OO0 ["关键字查找列"]=O0O0O000O0O000OO0 ["器械故障表现"].astype (str )+O0O0O000O0O000OO0 ["伤害表现"].astype (str )+O0O0O000O0O000OO0 ["使用过程"].astype (str )+O0O0O000O0O000OO0 ["事件原因分析描述"].astype (str )+O0O0O000O0O000OO0 ["初步处置情况"].astype (str )#line:5267
		else :#line:5268
			O0O0O000O0O000OO0 ["关键字查找列"]=O0O0O000O0O000OO0 ["器械故障表现"]#line:5269
		text .insert (END ,"\n药品查找列默认为不良反应表现,药品规则默认为通用规则。\n器械默认查找列为器械故障表现+伤害表现+使用过程+事件原因分析描述+初步处置情况，器械默认规则为无源通用规则+有源通用规则。\n")#line:5270
		O0O00OOOO0OOOO00O =[]#line:5272
		for O0OOO0O00O0000O00 ,OO00O00O000O0000O in OOO000O00O00OOO0O .iterrows ():#line:5274
			OO0OOO00OOOO0O0OO =OO00O00O000O0000O ["值"]#line:5275
			if "-其他关键字-"not in OO0OOO00OOOO0O0OO :#line:5277
				O0OO0OOO00OOOO00O =O0O0O000O0O000OO0 .loc [O0O0O000O0O000OO0 ["关键字查找列"].str .contains (OO0OOO00OOOO0O0OO ,na =False )].copy ()#line:5280
				if str (OO00O00O000O0000O ["排除值"])!="nan":#line:5281
					O0OO0OOO00OOOO00O =O0OO0OOO00OOOO00O .loc [~O0OO0OOO00OOOO00O ["关键字查找列"].str .contains (str (OO00O00O000O0000O ["排除值"]),na =False )].copy ()#line:5283
			else :#line:5285
				O0OO0OOO00OOOO00O =O0O0O000O0O000OO0 .loc [~O0O0O000O0O000OO0 ["关键字查找列"].str .contains (OO0OOO00OOOO0O0OO ,na =False )].copy ()#line:5288
			O0OO0OOO00OOOO00O ["关键字标记"]=str (OO0OOO00OOOO0O0OO )#line:5289
			O0OO0OOO00OOOO00O ["关键字计数"]=1 #line:5290
			if len (O0OO0OOO00OOOO00O )>0 :#line:5296
				try :#line:5297
					OO0O000000OO0OOOO =pd .pivot_table (O0OO0OOO00OOOO00O .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns ="伤害PSUR",aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5307
				except :#line:5309
					OO0O000000OO0OOOO =pd .pivot_table (O0OO0OOO00OOOO00O .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns ="伤害",aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:5319
				OO0O000000OO0OOOO =OO0O000000OO0OOOO [:-1 ]#line:5320
				OO0O000000OO0OOOO .columns =OO0O000000OO0OOOO .columns .droplevel (0 )#line:5321
				OO0O000000OO0OOOO =OO0O000000OO0OOOO .reset_index ()#line:5322
				if len (OO0O000000OO0OOOO )>0 :#line:5325
					OOO000OO0OOO0OOO0 =str (Counter (TOOLS_get_list0 ("use(器械故障表现).file",O0OO0OOO00OOOO00O ,1000 ))).replace ("Counter({","{")#line:5326
					OOO000OO0OOO0OOO0 =OOO000OO0OOO0OOO0 .replace ("})","}")#line:5327
					OOO000OO0OOO0OOO0 =ast .literal_eval (OOO000OO0OOO0OOO0 )#line:5328
					OO0O000000OO0OOOO .loc [0 ,"事件分类"]=str (TOOLS_get_list (OO0O000000OO0OOOO .loc [0 ,"关键字标记"])[0 ])#line:5330
					OO0O000000OO0OOOO .loc [0 ,"不良事件名称1"]=str ({OOO000O0O00O0OO00 :OO0OOO000OO0000OO for OOO000O0O00O0OO00 ,OO0OOO000OO0000OO in OOO000OO0OOO0OOO0 .items ()if STAT_judge_x (str (OOO000O0O00O0OO00 ),TOOLS_get_list (OO0OOO00OOOO0O0OO ))==1 })#line:5331
					OO0O000000OO0OOOO .loc [0 ,"不良事件名称2"]=str ({O0O00O000OO000OOO :OO0OOO0O0O0OO00O0 for O0O00O000OO000OOO ,OO0OOO0O0O0OO00O0 in OOO000OO0OOO0OOO0 .items ()if STAT_judge_x (str (O0O00O000OO000OOO ),TOOLS_get_list (OO0OOO00OOOO0O0OO ))!=1 })#line:5332
					if ini ["模式"]=="药品":#line:5343
						for OO00OO0O00000O0O0 in ["SOC","HLGT","HLT","PT"]:#line:5344
							OO0O000000OO0OOOO [OO00OO0O00000O0O0 ]=OO00O00O000O0000O [OO00OO0O00000O0O0 ]#line:5345
					if ini ["模式"]=="器械":#line:5346
						for OO00OO0O00000O0O0 in ["国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]:#line:5347
							OO0O000000OO0OOOO [OO00OO0O00000O0O0 ]=OO00O00O000O0000O [OO00OO0O00000O0O0 ]#line:5348
					O0O00OOOO0OOOO00O .append (OO0O000000OO0OOOO )#line:5351
		O0000O0O0OO0OOOO0 =pd .concat (O0O00OOOO0OOOO00O )#line:5352
		O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:5357
		O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .reset_index ()#line:5358
		O0000O0O0OO0OOOO0 ["All占比"]=round (O0000O0O0OO0OOOO0 ["All"]/O000O0OO00OO00000 *100 ,2 )#line:5360
		O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:5361
		try :#line:5362
			O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .rename (columns ={"其他":"一般"})#line:5363
		except :#line:5364
			pass #line:5365
		try :#line:5367
			O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .rename (columns ={" 一般":"一般"})#line:5368
		except :#line:5369
			pass #line:5370
		try :#line:5371
			O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .rename (columns ={" 严重":"严重"})#line:5372
		except :#line:5373
			pass #line:5374
		try :#line:5375
			O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .rename (columns ={"严重伤害":"严重"})#line:5376
		except :#line:5377
			pass #line:5378
		try :#line:5379
			O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 .rename (columns ={"死亡":"死亡(仅支持器械)"})#line:5380
		except :#line:5381
			pass #line:5382
		for OOO00O0000OO0O0O0 in ["一般","新的一般","严重","新的严重"]:#line:5385
			if OOO00O0000OO0O0O0 not in O0000O0O0OO0OOOO0 .columns :#line:5386
				O0000O0O0OO0OOOO0 [OOO00O0000OO0O0O0 ]=0 #line:5387
		try :#line:5389
			O0000O0O0OO0OOOO0 ["严重比"]=round ((O0000O0O0OO0OOOO0 ["严重"].fillna (0 )+O0000O0O0OO0OOOO0 ["死亡(仅支持器械)"].fillna (0 ))/O0000O0O0OO0OOOO0 ["总数量"]*100 ,2 )#line:5390
		except :#line:5391
			O0000O0O0OO0OOOO0 ["严重比"]=round ((O0000O0O0OO0OOOO0 ["严重"].fillna (0 )+O0000O0O0OO0OOOO0 ["新的严重"].fillna (0 ))/O0000O0O0OO0OOOO0 ["总数量"]*100 ,2 )#line:5392
		O0000O0O0OO0OOOO0 ["构成比"]=round ((O0000O0O0OO0OOOO0 ["总数量"].fillna (0 ))/O0000O0O0OO0OOOO0 ["总数量"].sum ()*100 ,2 )#line:5394
		if ini ["模式"]=="药品":#line:5396
			try :#line:5397
				O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)","SOC","HLGT","HLT","PT"]]#line:5398
			except :#line:5399
				O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","SOC","HLGT","HLT","PT"]]#line:5400
		elif ini ["模式"]=="器械":#line:5401
			try :#line:5402
				O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)","国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]]#line:5403
			except :#line:5404
				O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","国家故障术语集（大类）","国家故障术语集（小类）","IMDRF有关术语（故障）","国家伤害术语集（大类）","国家伤害术语集（小类）","IMDRF有关术语（伤害）"]]#line:5405
		else :#line:5407
			try :#line:5408
				O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2","死亡(仅支持器械)"]]#line:5409
			except :#line:5410
				O0000O0O0OO0OOOO0 =O0000O0O0OO0OOOO0 [["关键字标记","一般","新的一般","严重","新的严重","总数量","总数量占比","构成比","严重比","事件分类","不良事件名称1","不良事件名称2"]]#line:5411
		for OO0O0OO0O00OOO0O0 ,OO0OO0OO0O0OO00OO in OOO000O00O00OOO0O .iterrows ():#line:5413
			O0000O0O0OO0OOOO0 .loc [(O0000O0O0OO0OOOO0 ["关键字标记"].astype (str )==str (OO0OO0OO0O0OO00OO ["值"])),"排除值"]=OO0OO0OO0O0OO00OO ["排除值"]#line:5414
		O0000O0O0OO0OOOO0 ["排除值"]=O0000O0O0OO0OOOO0 ["排除值"].fillna ("没有排除值")#line:5416
		for OO0OOO0O0OO000O0O in ["一般","新的一般","严重","新的严重","总数量","总数量占比","严重比"]:#line:5420
			O0000O0O0OO0OOOO0 [OO0OOO0O0OO000O0O ]=O0000O0O0OO0OOOO0 [OO0OOO0O0OO000O0O ].fillna (0 )#line:5421
		for OO0OOO0O0OO000O0O in ["一般","新的一般","严重","新的严重","总数量"]:#line:5423
			O0000O0O0OO0OOOO0 [OO0OOO0O0OO000O0O ]=O0000O0O0OO0OOOO0 [OO0OOO0O0OO000O0O ].astype (int )#line:5424
		O0000O0O0OO0OOOO0 ["RPN"]="未定义"#line:5427
		O0000O0O0OO0OOOO0 ["故障原因"]="未定义"#line:5428
		O0000O0O0OO0OOOO0 ["可造成的伤害"]="未定义"#line:5429
		O0000O0O0OO0OOOO0 ["应采取的措施"]="未定义"#line:5430
		O0000O0O0OO0OOOO0 ["发生率"]="未定义"#line:5431
		O0000O0O0OO0OOOO0 ["报表类型"]="PSUR"#line:5433
		return O0000O0O0OO0OOOO0 #line:5434
def A0000_Main ():#line:5444
	print ("")#line:5445
if __name__ =='__main__':#line:5447
	root =Tk .Tk ()#line:5450
	root .title (title_all )#line:5451
	try :#line:5452
		root .iconphoto (True ,PhotoImage (file ="配置表/0（范例）ico.png"))#line:5453
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
