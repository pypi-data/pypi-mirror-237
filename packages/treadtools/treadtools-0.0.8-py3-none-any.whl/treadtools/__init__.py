#!/usr/bin/env python
# coding: utf-8
import warnings #line:7
import traceback #line:8
import ast #line:9
import re #line:10
import xlrd #line:11
import xlwt #line:12
import openpyxl #line:13
import pandas as pd #line:14
import numpy as np #line:15
import math #line:16
import tkinter as Tk #line:17
from tkinter import ttk #line:18
from tkinter import *#line:19
import tkinter .font as tkFont #line:20
from tkinter import filedialog ,dialog ,PhotoImage #line:21
from tkinter .messagebox import showinfo #line:22
from tkinter .scrolledtext import ScrolledText #line:23
import collections #line:24
from collections import Counter #line:25
import datetime #line:26
from datetime import datetime ,timedelta #line:27
from tkinter import END #line:28
import xlsxwriter #line:29
import os #line:30
import time #line:31
import threading #line:32
import pip #line:33
import matplotlib as plt #line:34
import requests #line:35
import random #line:36
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:38
from matplotlib .figure import Figure #line:39
from matplotlib .backends .backend_tkagg import NavigationToolbar2Tk #line:40
from matplotlib .ticker import PercentFormatter #line:41
from tkinter import ttk ,Menu ,Frame ,Canvas ,StringVar ,LEFT ,RIGHT ,TOP ,BOTTOM ,BOTH ,Y ,X ,YES ,NO ,DISABLED ,END ,Button ,LabelFrame ,GROOVE ,Toplevel ,Label ,Entry ,Scrollbar ,Text ,filedialog ,dialog ,PhotoImage #line:42
global TT_ori #line:45
global TT_biaozhun #line:46
global TT_modex #line:47
global TT_ori_backup #line:48
global version_now #line:49
global usergroup #line:50
global setting_cfg #line:51
global csdir #line:52
TT_biaozhun ={}#line:53
TT_ori =""#line:54
TT_modex =0 #line:55
TT_ori_backup =""#line:56
version_now ="0.0.8"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
try :#line:60
    csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:61
    csdir =csdir +csdir .split ("pinggutools")[0 ][-1 ]#line:62
except :#line:63
    csdir =str (os .path .dirname (__file__ ))#line:64
    csdir =csdir +csdir .split ("treadtools")[0 ][-1 ]#line:65
def extract_zip_file (O0000OOO000O00OOO ,OO00O0O0O0OOOO0O0 ):#line:73
    import zipfile #line:75
    if OO00O0O0O0OOOO0O0 =="":#line:76
        return 0 #line:77
    with zipfile .ZipFile (O0000OOO000O00OOO ,'r')as O00OOO0O00OOO00O0 :#line:78
        for O0O0O00OOOOO000O0 in O00OOO0O00OOO00O0 .infolist ():#line:79
            O0O0O00OOOOO000O0 .filename =O0O0O00OOOOO000O0 .filename .encode ('cp437').decode ('gbk')#line:81
            O00OOO0O00OOO00O0 .extract (O0O0O00OOOOO000O0 ,OO00O0O0O0OOOO0O0 )#line:82
def get_directory_path (OO0O00O0O000O0OOO ):#line:88
    global csdir #line:90
    if not (os .path .isfile (os .path .join (OO0O00O0O000O0OOO ,'规则文件.xls'))):#line:92
        extract_zip_file (csdir +"def.py",OO0O00O0O000O0OOO )#line:97
    if OO0O00O0O000O0OOO =="":#line:99
        quit ()#line:100
    return OO0O00O0O000O0OOO #line:101
def convert_and_compare_dates (OO000O0O000OOO0OO ):#line:105
    import datetime #line:106
    O000OOO0OO0O00OOO =datetime .datetime .now ()#line:107
    try :#line:109
       OO0O00O0000O0O00O =datetime .datetime .strptime (str (int (int (OO000O0O000OOO0OO )/4 )),"%Y%m%d")#line:110
    except :#line:111
        print ("fail")#line:112
        return "已过期"#line:113
    if OO0O00O0000O0O00O >O000OOO0OO0O00OOO :#line:115
        return "未过期"#line:117
    else :#line:118
        return "已过期"#line:119
def read_setting_cfg ():#line:121
    global csdir #line:122
    if os .path .exists (csdir +'setting.cfg'):#line:124
        text .insert (END ,"已完成初始化\n")#line:125
        with open (csdir +'setting.cfg','r')as OO00OO0O000OO0OOO :#line:126
            OOO00OO0OOO0OO000 =eval (OO00OO0O000OO0OOO .read ())#line:127
    else :#line:128
        O0O0OO0OO00000000 =csdir +'setting.cfg'#line:130
        with open (O0O0OO0OO00000000 ,'w')as OO00OO0O000OO0OOO :#line:131
            OO00OO0O000OO0OOO .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:132
        text .insert (END ,"未初始化，正在初始化...\n")#line:133
        OOO00OO0OOO0OO000 =read_setting_cfg ()#line:134
    return OOO00OO0OOO0OO000 #line:135
def open_setting_cfg ():#line:138
    global csdir #line:139
    with open (csdir +"setting.cfg","r")as OO000000OO00O00OO :#line:141
        O00OOOOOOOOO00O0O =eval (OO000000OO00O00OO .read ())#line:143
    return O00OOOOOOOOO00O0O #line:144
def update_setting_cfg (O0OO0OOO0000OO0O0 ,O0O00OO0O000O00O0 ):#line:146
    global csdir #line:147
    with open (csdir +"setting.cfg","r")as OOO000OOOOO000OO0 :#line:149
        O0000O0OOO0OOO0O0 =eval (OOO000OOOOO000OO0 .read ())#line:151
    if O0000O0OOO0OOO0O0 [O0OO0OOO0000OO0O0 ]==0 or O0000O0OOO0OOO0O0 [O0OO0OOO0000OO0O0 ]=="11111180000808":#line:153
        O0000O0OOO0OOO0O0 [O0OO0OOO0000OO0O0 ]=O0O00OO0O000O00O0 #line:154
        with open (csdir +"setting.cfg","w")as OOO000OOOOO000OO0 :#line:156
            OOO000OOOOO000OO0 .write (str (O0000O0OOO0OOO0O0 ))#line:157
def generate_random_file ():#line:160
    O00O00OO0O000OO0O =random .randint (200000 ,299999 )#line:162
    update_setting_cfg ("sidori",O00O00OO0O000OO0O )#line:164
def display_random_number ():#line:166
    global csdir #line:167
    OO00O0O0OOOO000O0 =Toplevel ()#line:168
    OO00O0O0OOOO000O0 .title ("ID")#line:169
    O0OO00O0OO00000O0 =OO00O0O0OOOO000O0 .winfo_screenwidth ()#line:171
    OO00O0O000OO0O0O0 =OO00O0O0OOOO000O0 .winfo_screenheight ()#line:172
    O0OOOOOOO00OOOOOO =80 #line:174
    O0OOO000O00OOO0OO =70 #line:175
    OOO000OO0OOO00OOO =(O0OO00O0OO00000O0 -O0OOOOOOO00OOOOOO )/2 #line:177
    OOO00O00OOO0000OO =(OO00O0O000OO0O0O0 -O0OOO000O00OOO0OO )/2 #line:178
    OO00O0O0OOOO000O0 .geometry ("%dx%d+%d+%d"%(O0OOOOOOO00OOOOOO ,O0OOO000O00OOO0OO ,OOO000OO0OOO00OOO ,OOO00O00OOO0000OO ))#line:179
    with open (csdir +"setting.cfg","r")as OO0OO000OO00OO0O0 :#line:182
        OOOO000000O00OO00 =eval (OO0OO000OO00OO0O0 .read ())#line:184
    OOOO00OOOO00O0000 =int (OOOO000000O00OO00 ["sidori"])#line:185
    OO0OOOO0O0O0O0O0O =OOOO00OOOO00O0000 *2 +183576 #line:186
    print (OO0OOOO0O0O0O0O0O )#line:188
    OOOO0O0O00OO0OO0O =ttk .Label (OO00O0O0OOOO000O0 ,text =f"机器码: {OOOO00OOOO00O0000}")#line:190
    OO00O0O00OOOOOO0O =ttk .Entry (OO00O0O0OOOO000O0 )#line:191
    OOOO0O0O00OO0OO0O .pack ()#line:194
    OO00O0O00OOOOOO0O .pack ()#line:195
    ttk .Button (OO00O0O0OOOO000O0 ,text ="验证",command =lambda :check_input (OO00O0O00OOOOOO0O .get (),OO0OOOO0O0O0O0O0O )).pack ()#line:199
def check_input (OOO0OOO000000OO00 ,O00O00O0O00OOOO0O ):#line:201
    try :#line:205
        O000000OO0OOO0OOO =int (str (OOO0OOO000000OO00 )[0 :6 ])#line:206
        OO00OO0O0O000O00O =convert_and_compare_dates (str (OOO0OOO000000OO00 )[6 :14 ])#line:207
    except :#line:208
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:209
        return 0 #line:210
    if O000000OO0OOO0OOO ==O00O00O0O00OOOO0O and OO00OO0O0O000O00O =="未过期":#line:212
        update_setting_cfg ("sidfinal",OOO0OOO000000OO00 )#line:213
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:214
        quit ()#line:215
    else :#line:216
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:217
def update_software (OO0O0O00OO0OO00OO ):#line:221
    global version_now #line:223
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:224
    try :#line:225
        OOOOOO0O00O00O00O =requests .get (f"https://pypi.org/pypi/{OO0O0O00OO0OO00OO}/json",timeout =2 ).json ()["info"]["version"]#line:226
    except :#line:227
        return "...更新失败。"#line:228
    if OOOOOO0O00O00O00O >version_now :#line:229
        text .insert (END ,"\n最新版本为："+OOOOOO0O00O00O00O +",正在尝试自动更新....")#line:230
        pip .main (['install',OO0O0O00OO0OO00OO ,'--upgrade'])#line:232
        text .insert (END ,"\n您可以开展工作。")#line:233
        return "...更新成功。"#line:234
def Tread_TOOLS_fileopen (OOOOOOOO00O0O0O0O ):#line:238
    ""#line:239
    global TT_ori #line:240
    global TT_ori_backup #line:241
    global TT_biaozhun #line:242
    warnings .filterwarnings ('ignore')#line:243
    if OOOOOOOO00O0O0O0O ==0 :#line:245
        O0OOOO00OO00000OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:246
        OOO000OO000OOOO0O =[pd .read_excel (O0O0O00O0O0O00O00 ,header =0 ,sheet_name =0 )for O0O0O00O0O0O00O00 in O0OOOO00OO00000OO ]#line:247
        OOO0O0000O0OOO0O0 =pd .concat (OOO000OO000OOOO0O ,ignore_index =True ).drop_duplicates ()#line:248
        try :#line:249
            OOO0O0000O0OOO0O0 =OOO0O0000O0OOO0O0 .loc [:,~TT_ori .columns .str .contains ("^Unnamed")]#line:250
        except :#line:251
            pass #line:252
        TT_ori_backup =OOO0O0000O0OOO0O0 .copy ()#line:253
        TT_ori =Tread_TOOLS_CLEAN (OOO0O0000O0OOO0O0 ).copy ()#line:254
        text .insert (END ,"\n原始数据导入成功，行数："+str (len (TT_ori )))#line:256
        text .insert (END ,"\n数据校验：\n")#line:257
        text .insert (END ,TT_ori )#line:258
        text .see (END )#line:259
    if OOOOOOOO00O0O0O0O ==1 :#line:261
        OOOOO000OOOOO0OO0 =filedialog .askopenfilename (filetypes =[("XLS",".xls")])#line:262
        TT_biaozhun ["关键字表"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:263
        TT_biaozhun ["产品批号"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name ="产品批号",header =0 ,index_col =0 ,).reset_index ()#line:264
        TT_biaozhun ["事件发生月份"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name ="事件发生月份",header =0 ,index_col =0 ,).reset_index ()#line:265
        TT_biaozhun ["事件发生季度"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name ="事件发生季度",header =0 ,index_col =0 ,).reset_index ()#line:266
        TT_biaozhun ["规格"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name ="规格",header =0 ,index_col =0 ,).reset_index ()#line:267
        TT_biaozhun ["型号"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name ="型号",header =0 ,index_col =0 ,).reset_index ()#line:268
        TT_biaozhun ["设置"]=pd .read_excel (OOOOO000OOOOO0OO0 ,sheet_name ="设置",header =0 ,index_col =0 ,).reset_index ()#line:269
        Tread_TOOLS_check (TT_ori ,TT_biaozhun ["关键字表"],0 )#line:270
        text .insert (END ,"\n标准导入成功，行数："+str (len (TT_biaozhun )))#line:271
        text .see (END )#line:272
def Tread_TOOLS_check (OOO0OOO0OO0OO0O0O ,OO000O0OO0O00O0OO ,OOOOOO0O00O00OO0O ):#line:274
        ""#line:275
        global TT_ori #line:276
        OO000OO0O0OO0000O =Tread_TOOLS_Countall (OOO0OOO0OO0OO0O0O ).df_psur (OO000O0OO0O00O0OO )#line:277
        if OOOOOO0O00O00OO0O ==0 :#line:279
            Tread_TOOLS_tree_Level_2 (OO000OO0O0OO0000O ,0 ,TT_ori .copy ())#line:281
        OO000OO0O0OO0000O ["核验"]=0 #line:284
        OO000OO0O0OO0000O .loc [(OO000OO0O0OO0000O ["关键字标记"].str .contains ("-其他关键字-",na =False )),"核验"]=OO000OO0O0OO0000O .loc [(OO000OO0O0OO0000O ["关键字标记"].str .contains ("-其他关键字-",na =False )),"总数量"]#line:285
        if OO000OO0O0OO0000O ["核验"].sum ()>0 :#line:286
            showinfo (title ="温馨提示",message ="存在未定义类型的报告"+str (OO000OO0O0OO0000O ["核验"].sum ())+"条，趋势分析可能会存在遗漏，建议修正该错误再进行下一步。")#line:287
def Tread_TOOLS_tree_Level_2 (OOO00OOOO00OO0O00 ,OO0O00O0O0OOO0000 ,OOO00O0OO0O0O0OOO ,*OOOO0O0O0O0OO0000 ):#line:289
    ""#line:290
    global TT_ori_backup #line:292
    O00O0OO00000O0OO0 =OOO00OOOO00OO0O00 .columns .values .tolist ()#line:294
    OO0O00O0O0OOO0000 =0 #line:295
    O00000O0000OOOO0O =OOO00OOOO00OO0O00 .loc [:]#line:296
    O0O0O0OOOOOOO00O0 =0 #line:300
    try :#line:301
        OOOO0O0OO0O0OOO0O =OOOO0O0O0O0OO0000 [0 ]#line:302
        O0O0O0OOOOOOO00O0 =1 #line:303
    except :#line:304
        pass #line:305
    OO0O000O0000O00OO =Toplevel ()#line:308
    OO0O000O0000O00OO .title ("报表查看器")#line:309
    OOOO0O0OOOOOO000O =OO0O000O0000O00OO .winfo_screenwidth ()#line:310
    OOO0OO0O0O0OOO000 =OO0O000O0000O00OO .winfo_screenheight ()#line:312
    OOOO00O00O0OOO000 =1300 #line:314
    O000O0000O0O000OO =600 #line:315
    O00OOO0O00O000O00 =(OOOO0O0OOOOOO000O -OOOO00O00O0OOO000 )/2 #line:317
    O000O0OO0000OO0O0 =(OOO0OO0O0O0OOO000 -O000O0000O0O000OO )/2 #line:318
    OO0O000O0000O00OO .geometry ("%dx%d+%d+%d"%(OOOO00O00O0OOO000 ,O000O0000O0O000OO ,O00OOO0O00O000O00 ,O000O0OO0000OO0O0 ))#line:319
    O000O00O0O0O0OOOO =ttk .Frame (OO0O000O0000O00OO ,width =1300 ,height =20 )#line:320
    O000O00O0O0O0OOOO .pack (side =BOTTOM )#line:321
    O00O00OO000O00O00 =ttk .Frame (OO0O000O0000O00OO ,width =1300 ,height =20 )#line:323
    O00O00OO000O00O00 .pack (side =TOP )#line:324
    if 1 >0 :#line:328
        OO0OOOOO0O0000O0O =Button (O000O00O0O0O0OOOO ,text ="控制图(所有)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00000O0000OOOO0O [:-1 ],OOOO0O0OO0O0OOO0O ,[OO0OOO0O000O00OO0 for OO0OOO0O000O00OO0 in O00000O0000OOOO0O .columns if (OO0OOO0O000O00OO0 not in [OOOO0O0OO0O0OOO0O ])],"关键字趋势图",100 ),)#line:338
        if O0O0O0OOOOOOO00O0 ==1 :#line:339
            OO0OOOOO0O0000O0O .pack (side =LEFT )#line:340
        OO0OOOOO0O0000O0O =Button (O000O00O0O0O0OOOO ,text ="控制图(总数量)",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (O00000O0000OOOO0O [:-1 ],OOOO0O0OO0O0OOO0O ,[OOOO0OO0O0O000O00 for OOOO0OO0O0O000O00 in O00000O0000OOOO0O .columns if (OOOO0OO0O0O000O00 in ["该元素总数量"])],"关键字趋势图",100 ),)#line:350
        if O0O0O0OOOOOOO00O0 ==1 :#line:351
            OO0OOOOO0O0000O0O .pack (side =LEFT )#line:352
        O00O0000O0O000OOO =Button (O000O00O0O0O0OOOO ,text ="导出",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :TOOLS_save_dict (O00000O0000OOOO0O ),)#line:362
        O00O0000O0O000OOO .pack (side =LEFT )#line:363
        O00O0000O0O000OOO =Button (O000O00O0O0O0OOOO ,text ="发生率测算",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_fashenglv (O00000O0000OOOO0O ,OOOO0O0OO0O0OOO0O ),)#line:373
        if "关键字标记"not in O00000O0000OOOO0O .columns and "报告编码"not in O00000O0000OOOO0O .columns :#line:374
            if "对象"not in O00000O0000OOOO0O .columns :#line:375
                O00O0000O0O000OOO .pack (side =LEFT )#line:376
        O00O0000O0O000OOO =Button (O000O00O0O0O0OOOO ,text ="直方图",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_histbar (O00000O0000OOOO0O .copy ()),)#line:386
        if "对象"in O00000O0000OOOO0O .columns :#line:387
            O00O0000O0O000OOO .pack (side =LEFT )#line:388
        OO0O0O00OO000O00O =Button (O000O00O0O0O0OOOO ,text ="行数:"+str (len (O00000O0000OOOO0O )),bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",)#line:398
        OO0O0O00OO000O00O .pack (side =LEFT )#line:399
    OO0OOOOO00O0O0OOO =O00000O0000OOOO0O .values .tolist ()#line:402
    O0O0000OO0OO00000 =O00000O0000OOOO0O .columns .values .tolist ()#line:403
    OO0OO0O0000O0000O =ttk .Treeview (O00O00OO000O00O00 ,columns =O0O0000OO0OO00000 ,show ="headings",height =45 )#line:404
    for O0O000OOO0OO00O00 in O0O0000OO0OO00000 :#line:406
        OO0OO0O0000O0000O .heading (O0O000OOO0OO00O00 ,text =O0O000OOO0OO00O00 )#line:407
    for O0OO0OO000OOO00OO in OO0OOOOO00O0O0OOO :#line:408
        OO0OO0O0000O0000O .insert ("","end",values =O0OO0OO000OOO00OO )#line:409
    for O0OO00OO0000OO0O0 in O0O0000OO0OO00000 :#line:410
        OO0OO0O0000O0000O .column (O0OO00OO0000OO0O0 ,minwidth =0 ,width =120 ,stretch =NO )#line:411
    OOOOO0O0OO0OOO0OO =Scrollbar (O00O00OO000O00O00 ,orient ="vertical")#line:413
    OOOOO0O0OO0OOO0OO .pack (side =RIGHT ,fill =Y )#line:414
    OOOOO0O0OO0OOO0OO .config (command =OO0OO0O0000O0000O .yview )#line:415
    OO0OO0O0000O0000O .config (yscrollcommand =OOOOO0O0OO0OOO0OO .set )#line:416
    OOOO00OOO00OOO0OO =Scrollbar (O00O00OO000O00O00 ,orient ="horizontal")#line:418
    OOOO00OOO00OOO0OO .pack (side =BOTTOM ,fill =X )#line:419
    OOOO00OOO00OOO0OO .config (command =OO0OO0O0000O0000O .xview )#line:420
    OO0OO0O0000O0000O .config (yscrollcommand =OOOOO0O0OO0OOO0OO .set )#line:421
    def O0O0OO0O00OOOO0OO (OOO00OOOO0O0000OO ,OOO0000O0O00OO00O ,OO000OO0O0O00O0OO ):#line:423
        for O0O0OOOOOO0O0O0O0 in OO0OO0O0000O0000O .selection ():#line:426
            OO0OOOOOOO00000OO =OO0OO0O0000O0000O .item (O0O0OOOOOO0O0O0O0 ,"values")#line:427
            O0OO0OOO00OO0OOO0 =dict (zip (OOO0000O0O00OO00O ,OO0OOOOOOO00000OO ))#line:428
        if "该分类下各项计数"in OOO0000O0O00OO00O :#line:430
            OO000O0OO0000OOOO =OOO00O0OO0O0O0OOO .copy ()#line:431
            OO000O0OO0000OOOO ["关键字查找列"]=""#line:432
            for O0OO0OO0OOOO00OOO in TOOLS_get_list (O0OO0OOO00OO0OOO0 ["查找位置"]):#line:433
                OO000O0OO0000OOOO ["关键字查找列"]=OO000O0OO0000OOOO ["关键字查找列"]+OO000O0OO0000OOOO [O0OO0OO0OOOO00OOO ].astype ("str")#line:434
            O0OO00OOOOOOO0OOO =OO000O0OO0000OOOO .loc [OO000O0OO0000OOOO ["关键字查找列"].str .contains (O0OO0OOO00OO0OOO0 ["关键字标记"],na =False )].copy ()#line:435
            O0OO00OOOOOOO0OOO =O0OO00OOOOOOO0OOO .loc [~O0OO00OOOOOOO0OOO ["关键字查找列"].str .contains (O0OO0OOO00OO0OOO0 ["排除值"],na =False )].copy ()#line:436
            Tread_TOOLS_tree_Level_2 (O0OO00OOOOOOO0OOO ,0 ,O0OO00OOOOOOO0OOO )#line:442
            return 0 #line:443
        if "报告编码"in OOO0000O0O00OO00O :#line:445
            OOOOO000OO000O0OO =Toplevel ()#line:446
            OO0OO0O00OO00O00O =OOOOO000OO000O0OO .winfo_screenwidth ()#line:447
            O00OO000OOOOOO00O =OOOOO000OO000O0OO .winfo_screenheight ()#line:449
            O0OO000OOO000OOOO =800 #line:451
            O0000OOOO0OOOOO0O =600 #line:452
            O0OO0OO0OOOO00OOO =(OO0OO0O00OO00O00O -O0OO000OOO000OOOO )/2 #line:454
            OOO00OO0O00000O00 =(O00OO000OOOOOO00O -O0000OOOO0OOOOO0O )/2 #line:455
            OOOOO000OO000O0OO .geometry ("%dx%d+%d+%d"%(O0OO000OOO000OOOO ,O0000OOOO0OOOOO0O ,O0OO0OO0OOOO00OOO ,OOO00OO0O00000O00 ))#line:456
            OOOO0OOOOO0OO0OOO =ScrolledText (OOOOO000OO000O0OO ,height =1100 ,width =1100 ,bg ="#FFFFFF")#line:460
            OOOO0OOOOO0OO0OOO .pack (padx =10 ,pady =10 )#line:461
            def O00OOO0000OO000O0 (event =None ):#line:462
                OOOO0OOOOO0OO0OOO .event_generate ('<<Copy>>')#line:463
            def OOO0O00OO00O00O0O (OOOO0000OOO000OO0 ,O0O00OOOO00000OO0 ):#line:464
                OOO000O00OOOOOO0O =open (O0O00OOOO00000OO0 ,"w",encoding ='utf-8')#line:465
                OOO000O00OOOOOO0O .write (OOOO0000OOO000OO0 )#line:466
                OOO000O00OOOOOO0O .flush ()#line:468
                showinfo (title ="提示信息",message ="保存成功。")#line:469
            OOO00OO000O0OO000 =Menu (OOOO0OOOOO0OO0OOO ,tearoff =False ,)#line:471
            OOO00OO000O0OO000 .add_command (label ="复制",command =O00OOO0000OO000O0 )#line:472
            OOO00OO000O0OO000 .add_command (label ="导出",command =lambda :thread_it (OOO0O00OO00O00O0O ,OOOO0OOOOO0OO0OOO .get (1.0 ,'end'),filedialog .asksaveasfilename (title =u"保存文件",initialfile =O0OO0OOO00OO0OOO0 ["报告编码"],defaultextension ="txt",filetypes =[("txt","*.txt")])))#line:473
            def OO00OO0000O000O00 (OO0O000OOOO0O00OO ):#line:475
                OOO00OO000O0OO000 .post (OO0O000OOOO0O00OO .x_root ,OO0O000OOOO0O00OO .y_root )#line:476
            OOOO0OOOOO0OO0OOO .bind ("<Button-3>",OO00OO0000O000O00 )#line:477
            OOOOO000OO000O0OO .title (O0OO0OOO00OO0OOO0 ["报告编码"])#line:479
            for O0O0O0OO00OOO00OO in range (len (OOO0000O0O00OO00O )):#line:480
                OOOO0OOOOO0OO0OOO .insert (END ,OOO0000O0O00OO00O [O0O0O0OO00OOO00OO ])#line:482
                OOOO0OOOOO0OO0OOO .insert (END ,"：")#line:483
                OOOO0OOOOO0OO0OOO .insert (END ,O0OO0OOO00OO0OOO0 [OOO0000O0O00OO00O [O0O0O0OO00OOO00OO ]])#line:484
                OOOO0OOOOO0OO0OOO .insert (END ,"\n")#line:485
            OOOO0OOOOO0OO0OOO .config (state =DISABLED )#line:486
            return 0 #line:487
        OOO00OO0O00000O00 =OO0OOOOOOO00000OO [1 :-1 ]#line:490
        O0OO0OO0OOOO00OOO =OO000OO0O0O00O0OO .columns .tolist ()#line:492
        O0OO0OO0OOOO00OOO =O0OO0OO0OOOO00OOO [1 :-1 ]#line:493
        O0000000OO0000OO0 ={'关键词':O0OO0OO0OOOO00OOO ,'数量':OOO00OO0O00000O00 }#line:495
        O0000000OO0000OO0 =pd .DataFrame .from_dict (O0000000OO0000OO0 )#line:496
        O0000000OO0000OO0 ["数量"]=O0000000OO0000OO0 ["数量"].astype (float )#line:497
        Tread_TOOLS_draw (O0000000OO0000OO0 ,"帕累托图",'关键词','数量',"帕累托图")#line:498
        return 0 #line:499
    OO0OO0O0000O0000O .bind ("<Double-1>",lambda OOO0O00OO0O0OOO00 :O0O0OO0O00OOOO0OO (OOO0O00OO0O0OOO00 ,O0O0000OO0OO00000 ,O00000O0000OOOO0O ),)#line:507
    OO0OO0O0000O0000O .pack ()#line:508
class Tread_TOOLS_Countall ():#line:510
    ""#line:511
    def __init__ (O00O0000OO0000OO0 ,O000O0OO00000O0O0 ):#line:512
        ""#line:513
        O00O0000OO0000OO0 .df =O000O0OO00000O0O0 #line:514
    def df_psur (OOO0OO000O0O000OO ,O0OOO0O0OO00OO0O0 ,*O0O000000OO0O0O0O ):#line:516
        ""#line:517
        global TT_biaozhun #line:518
        O00O0OO0OOOO0OOOO =OOO0OO000O0O000OO .df .copy ()#line:519
        O0O0O00000OO00000 =len (O00O0OO0OOOO0OOOO .drop_duplicates ("报告编码"))#line:521
        O00O0OOOO000O0OOO =O0OOO0O0OO00OO0O0 .copy ()#line:524
        O0OOOOO00O0O0000O =TT_biaozhun ["设置"]#line:527
        if O0OOOOO00O0O0000O .loc [1 ,"值"]:#line:528
            OOO0000O00OO000O0 =O0OOOOO00O0O0000O .loc [1 ,"值"]#line:529
        else :#line:530
            OOO0000O00OO000O0 ="透视列"#line:531
            O00O0OO0OOOO0OOOO [OOO0000O00OO000O0 ]="未正确设置"#line:532
        OOOOO00000O0O000O =""#line:534
        OOOOOOOOOOOOOO000 ="-其他关键字-"#line:535
        for OO0OOO0OOOO00O0OO ,O0OOO0000OO0O0O00 in O00O0OOOO000O0OOO .iterrows ():#line:536
            OOOOOOOOOOOOOO000 =OOOOOOOOOOOOOO000 +"|"+str (O0OOO0000OO0O0O00 ["值"])#line:537
            O0O00OO0000OO0O0O =O0OOO0000OO0O0O00 #line:538
        O0O00OO0000OO0O0O [3 ]=OOOOOOOOOOOOOO000 #line:539
        O0O00OO0000OO0O0O [2 ]="-其他关键字-|"#line:540
        O00O0OOOO000O0OOO .loc [len (O00O0OOOO000O0OOO )]=O0O00OO0000OO0O0O #line:541
        O00O0OOOO000O0OOO =O00O0OOOO000O0OOO .reset_index (drop =True )#line:542
        O00O0OO0OOOO0OOOO ["关键字查找列"]=""#line:546
        for O0000000000OOO0OO in TOOLS_get_list (O00O0OOOO000O0OOO .loc [0 ,"查找位置"]):#line:547
            O00O0OO0OOOO0OOOO ["关键字查找列"]=O00O0OO0OOOO0OOOO ["关键字查找列"]+O00O0OO0OOOO0OOOO [O0000000000OOO0OO ].astype ("str")#line:548
        OOOOOO000OOOO000O =[]#line:551
        for OO0OOO0OOOO00O0OO ,O0OOO0000OO0O0O00 in O00O0OOOO000O0OOO .iterrows ():#line:552
            OO00000OO00O0O0OO =O0OOO0000OO0O0O00 ["值"]#line:553
            O00OOO00OO0000O0O =O00O0OO0OOOO0OOOO .loc [O00O0OO0OOOO0OOOO ["关键字查找列"].str .contains (OO00000OO00O0O0OO ,na =False )].copy ()#line:554
            if str (O0OOO0000OO0O0O00 ["排除值"])!="nan":#line:555
                O00OOO00OO0000O0O =O00OOO00OO0000O0O .loc [~O00OOO00OO0000O0O ["关键字查找列"].str .contains (str (O0OOO0000OO0O0O00 ["排除值"]),na =False )].copy ()#line:556
            O00OOO00OO0000O0O ["关键字标记"]=str (OO00000OO00O0O0OO )#line:558
            O00OOO00OO0000O0O ["关键字计数"]=1 #line:559
            if len (O00OOO00OO0000O0O )>0 :#line:561
                O0O0OO0OO00O0O00O =pd .pivot_table (O00OOO00OO0000O0O .drop_duplicates ("报告编码"),values =["关键字计数"],index ="关键字标记",columns =OOO0000O00OO000O0 ,aggfunc ={"关键字计数":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:571
                O0O0OO0OO00O0O00O =O0O0OO0OO00O0O00O [:-1 ]#line:572
                O0O0OO0OO00O0O00O .columns =O0O0OO0OO00O0O00O .columns .droplevel (0 )#line:573
                O0O0OO0OO00O0O00O =O0O0OO0OO00O0O00O .reset_index ()#line:574
                if len (O0O0OO0OO00O0O00O )>0 :#line:577
                    OOOOOOOO0O0OO0O0O =str (Counter (TOOLS_get_list0 ("use(关键字查找列).file",O00OOO00OO0000O0O ,1000 ))).replace ("Counter({","{")#line:578
                    OOOOOOOO0O0OO0O0O =OOOOOOOO0O0OO0O0O .replace ("})","}")#line:579
                    OOOOOOOO0O0OO0O0O =ast .literal_eval (OOOOOOOO0O0OO0O0O )#line:580
                    O0O0OO0OO00O0O00O .loc [0 ,"事件分类"]=str (TOOLS_get_list (O0O0OO0OO00O0O00O .loc [0 ,"关键字标记"])[0 ])#line:582
                    O0O0OO0OO00O0O00O .loc [0 ,"该分类下各项计数"]=str ({O00000OOO0OO000OO :OOOOO000OOO0O0000 for O00000OOO0OO000OO ,OOOOO000OOO0O0000 in OOOOOOOO0O0OO0O0O .items ()if STAT_judge_x (str (O00000OOO0OO000OO ),TOOLS_get_list (OO00000OO00O0O0OO ))==1 })#line:583
                    O0O0OO0OO00O0O00O .loc [0 ,"其他分类各项计数"]=str ({O000000000O00OOOO :O00OO00OO0000OOOO for O000000000O00OOOO ,O00OO00OO0000OOOO in OOOOOOOO0O0OO0O0O .items ()if STAT_judge_x (str (O000000000O00OOOO ),TOOLS_get_list (OO00000OO00O0O0OO ))!=1 })#line:584
                    O0O0OO0OO00O0O00O ["查找位置"]=O0OOO0000OO0O0O00 ["查找位置"]#line:585
                    OOOOOO000OOOO000O .append (O0O0OO0OO00O0O00O )#line:588
        OOOOO00000O0O000O =pd .concat (OOOOOO000OOOO000O )#line:589
        OOOOO00000O0O000O =OOOOO00000O0O000O .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:594
        OOOOO00000O0O000O =OOOOO00000O0O000O .reset_index ()#line:595
        OOOOO00000O0O000O ["All占比"]=round (OOOOO00000O0O000O ["All"]/O0O0O00000OO00000 *100 ,2 )#line:597
        OOOOO00000O0O000O =OOOOO00000O0O000O .rename (columns ={"All":"总数量","All占比":"总数量占比"})#line:598
        for OOO0OOOO00OOO00OO ,O000O000000OO0OO0 in O00O0OOOO000O0OOO .iterrows ():#line:601
            OOOOO00000O0O000O .loc [(OOOOO00000O0O000O ["关键字标记"].astype (str )==str (O000O000000OO0OO0 ["值"])),"排除值"]=O000O000000OO0OO0 ["排除值"]#line:602
            OOOOO00000O0O000O .loc [(OOOOO00000O0O000O ["关键字标记"].astype (str )==str (O000O000000OO0OO0 ["值"])),"查找位置"]=O000O000000OO0OO0 ["查找位置"]#line:603
        OOOOO00000O0O000O ["排除值"]=OOOOO00000O0O000O ["排除值"].fillna ("-没有排除值-")#line:605
        OOOOO00000O0O000O ["报表类型"]="PSUR"#line:608
        del OOOOO00000O0O000O ["index"]#line:609
        try :#line:610
            del OOOOO00000O0O000O ["未正确设置"]#line:611
        except :#line:612
            pass #line:613
        return OOOOO00000O0O000O #line:614
    def df_find_all_keword_risk (O0OOO0O00O0000000 ,OOO0OO0O0O0OO0OO0 ,*O0OO0O00O0O0OOO0O ):#line:617
        ""#line:618
        global TT_biaozhun #line:619
        O0000OO00O0000000 =O0OOO0O00O0000000 .df .copy ()#line:621
        OOO0000000OO0O00O =time .time ()#line:622
        O000000O00O0O0O0O =TT_biaozhun ["关键字表"].copy ()#line:624
        OOOO0O000O000000O ="作用对象"#line:626
        O00OO00OOO0O000OO ="报告编码"#line:628
        O0000O0OO000O0O00 =O0000OO00O0000000 .groupby ([OOOO0O000O000000O ]).agg (总数量 =(O00OO00OOO0O000OO ,"nunique"),).reset_index ()#line:631
        OO0OOO00O0OOO00O0 =[OOOO0O000O000000O ,OOO0OO0O0O0OO0OO0 ]#line:633
        O0O00O0O000O0O00O =O0000OO00O0000000 .groupby (OO0OOO00O0OOO00O0 ).agg (该元素总数量 =(OOOO0O000O000000O ,"count"),).reset_index ()#line:637
        OO0OOOO0O000O0O00 =[]#line:639
        O0O00O0O0OO0OO0O0 =0 #line:643
        OO00O0O00O00OOOOO =int (len (O0000O0OO000O0O00 ))#line:644
        for O0O0O000OOO00000O ,O000OO0O0000000OO in zip (O0000O0OO000O0O00 [OOOO0O000O000000O ].values ,O0000O0OO000O0O00 ["总数量"].values ):#line:645
            O0O00O0O0OO0OO0O0 +=1 #line:646
            O0OOOO0OO0O00O0O0 =O0000OO00O0000000 [(O0000OO00O0000000 [OOOO0O000O000000O ]==O0O0O000OOO00000O )].copy ()#line:647
            for O0O0O0000O0000OO0 ,O0O0000O000O00OO0 ,OO000O00OO000OOO0 in zip (O000000O00O0O0O0O ["值"].values ,O000000O00O0O0O0O ["查找位置"].values ,O000000O00O0O0O0O ["排除值"].values ):#line:649
                    OO00OO0000OO00000 =O0OOOO0OO0O00O0O0 .copy ()#line:650
                    OOOO000OO0OO00000 =TOOLS_get_list (O0O0O0000O0000OO0 )[0 ]#line:651
                    OO00OO0000OO00000 ["关键字查找列"]=""#line:653
                    for O0OOO0O0OOO00O0O0 in TOOLS_get_list (O0O0000O000O00OO0 ):#line:654
                        OO00OO0000OO00000 ["关键字查找列"]=OO00OO0000OO00000 ["关键字查找列"]+OO00OO0000OO00000 [O0OOO0O0OOO00O0O0 ].astype ("str")#line:655
                    OO00OO0000OO00000 .loc [OO00OO0000OO00000 ["关键字查找列"].str .contains (O0O0O0000O0000OO0 ,na =False ),"关键字"]=OOOO000OO0OO00000 #line:657
                    if str (OO000O00OO000OOO0 )!="nan":#line:662
                        OO00OO0000OO00000 =OO00OO0000OO00000 .loc [~OO00OO0000OO00000 ["关键字查找列"].str .contains (OO000O00OO000OOO0 ,na =False )].copy ()#line:663
                    if (len (OO00OO0000OO00000 ))<1 :#line:665
                        continue #line:667
                    OOO00OO0O000OOOO0 =STAT_find_keyword_risk (OO00OO0000OO00000 ,[OOOO0O000O000000O ,"关键字"],"关键字",OOO0OO0O0O0OO0OO0 ,int (O000OO0O0000000OO ))#line:669
                    if len (OOO00OO0O000OOOO0 )>0 :#line:670
                        OOO00OO0O000OOOO0 ["关键字组合"]=O0O0O0000O0000OO0 #line:671
                        OOO00OO0O000OOOO0 ["排除值"]=OO000O00OO000OOO0 #line:672
                        OOO00OO0O000OOOO0 ["关键字查找列"]=O0O0000O000O00OO0 #line:673
                        OO0OOOO0O000O0O00 .append (OOO00OO0O000OOOO0 )#line:674
        if len (OO0OOOO0O000O0O00 )<1 :#line:677
            showinfo (title ="错误信息",message ="该注册证号未检索到任何关键字，规则制定存在缺陷。")#line:678
            return 0 #line:679
        O00O000O000000OOO =pd .concat (OO0OOOO0O000O0O00 )#line:680
        O00O000O000000OOO =pd .merge (O00O000O000000OOO ,O0O00O0O000O0O00O ,on =OO0OOO00O0OOO00O0 ,how ="left")#line:683
        O00O000O000000OOO ["关键字数量比例"]=round (O00O000O000000OOO ["计数"]/O00O000O000000OOO ["该元素总数量"],2 )#line:684
        O00O000O000000OOO =O00O000O000000OOO .reset_index (drop =True )#line:686
        if len (O00O000O000000OOO )>0 :#line:689
            O00O000O000000OOO ["风险评分"]=0 #line:690
            O00O000O000000OOO ["报表类型"]="keyword_findrisk"+OOO0OO0O0O0OO0OO0 #line:691
            O00O000O000000OOO .loc [(O00O000O000000OOO ["计数"]>=3 ),"风险评分"]=O00O000O000000OOO ["风险评分"]+3 #line:692
            O00O000O000000OOO .loc [(O00O000O000000OOO ["计数"]>=(O00O000O000000OOO ["数量均值"]+O00O000O000000OOO ["数量标准差"])),"风险评分"]=O00O000O000000OOO ["风险评分"]+1 #line:693
            O00O000O000000OOO .loc [(O00O000O000000OOO ["计数"]>=O00O000O000000OOO ["数量CI"]),"风险评分"]=O00O000O000000OOO ["风险评分"]+1 #line:694
            O00O000O000000OOO .loc [(O00O000O000000OOO ["关键字数量比例"]>0.5 )&(O00O000O000000OOO ["计数"]>=3 ),"风险评分"]=O00O000O000000OOO ["风险评分"]+1 #line:695
            O00O000O000000OOO =O00O000O000000OOO .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:697
        O0OOOOO00O0OO00O0 =O00O000O000000OOO .columns .to_list ()#line:707
        O000OO0OO0O000OOO =O0OOOOO00O0OO00O0 [O0OOOOO00O0OO00O0 .index ("关键字")+1 ]#line:708
        O0OO0000O0OOOOO0O =pd .pivot_table (O00O000O000000OOO ,index =O000OO0OO0O000OOO ,columns ="关键字",values =["计数"],aggfunc ={"计数":"sum"},fill_value ="0",margins =True ,dropna =False ,)#line:719
        O0OO0000O0OOOOO0O .columns =O0OO0000O0OOOOO0O .columns .droplevel (0 )#line:720
        O0OO0000O0OOOOO0O =pd .merge (O0OO0000O0OOOOO0O ,O00O000O000000OOO [[O000OO0OO0O000OOO ,"该元素总数量"]].drop_duplicates (O000OO0OO0O000OOO ),on =[O000OO0OO0O000OOO ],how ="left")#line:723
        del O0OO0000O0OOOOO0O ["All"]#line:725
        O0OO0000O0OOOOO0O .iloc [-1 ,-1 ]=O0OO0000O0OOOOO0O ["该元素总数量"].sum (axis =0 )#line:726
        print ("耗时：",(time .time ()-OOO0000000OO0O00O ))#line:728
        return O0OO0000O0OOOOO0O #line:731
def Tread_TOOLS_bar (O000O0000O0O00OOO ):#line:739
         ""#line:740
         O00000O0O00O0O0OO =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:741
         O0OO000OO00O0O00O =[pd .read_excel (OO00O0O0O000OO0OO ,header =0 ,sheet_name =0 )for OO00O0O0O000OO0OO in O00000O0O00O0O0OO ]#line:742
         OO0OO0O00O0OO0O00 =pd .concat (O0OO000OO00O0O00O ,ignore_index =True )#line:743
         O0OOOOO0000OOO00O =pd .pivot_table (OO0OO0O00O0OO0O00 ,index ="对象",columns ="关键词",values =O000O0000O0O00OOO ,aggfunc ="sum",fill_value ="0",margins =True ,dropna =False ,).reset_index ()#line:753
         del O0OOOOO0000OOO00O ["All"]#line:755
         O0OOOOO0000OOO00O =O0OOOOO0000OOO00O [:-1 ]#line:756
         Tread_TOOLS_tree_Level_2 (O0OOOOO0000OOO00O ,0 ,0 )#line:758
def Tread_TOOLS_analysis (OOO000OO00OO0O00O ):#line:763
    ""#line:764
    import datetime #line:765
    global TT_ori #line:766
    global TT_biaozhun #line:767
    if len (TT_ori )==0 :#line:769
       showinfo (title ="提示",message ="您尚未导入原始数据。")#line:770
       return 0 #line:771
    if len (TT_biaozhun )==0 :#line:772
       showinfo (title ="提示",message ="您尚未导入规则。")#line:773
       return 0 #line:774
    OO000OOOO0OO000OO =TT_biaozhun ["设置"]#line:776
    TT_ori ["作用对象"]=""#line:777
    for O000O00OOOOOOO0OO in TOOLS_get_list (OO000OOOO0OO000OO .loc [0 ,"值"]):#line:778
        TT_ori ["作用对象"]=TT_ori ["作用对象"]+"-"+TT_ori [O000O00OOOOOOO0OO ].fillna ("未填写").astype ("str")#line:779
    O00OOOO00000O000O =Toplevel ()#line:782
    O00OOOO00000O000O .title ("单品分析")#line:783
    O00O000O00OO000OO =O00OOOO00000O000O .winfo_screenwidth ()#line:784
    O00OO00OO0OOO0OOO =O00OOOO00000O000O .winfo_screenheight ()#line:786
    O00OO00OO000OOO00 =580 #line:788
    OOO0000000OO00OO0 =80 #line:789
    OOOOOOOOOO000O0O0 =(O00O000O00OO000OO -O00OO00OO000OOO00 )/1.7 #line:791
    O00O0O0O0OO0O0O00 =(O00OO00OO0OOO0OOO -OOO0000000OO00OO0 )/2 #line:792
    O00OOOO00000O000O .geometry ("%dx%d+%d+%d"%(O00OO00OO000OOO00 ,OOO0000000OO00OO0 ,OOOOOOOOOO000O0O0 ,O00O0O0O0OO0O0O00 ))#line:793
    OO0O0OOO0O00O000O =Label (O00OOOO00000O000O ,text ="作用对象：")#line:796
    OO0O0OOO0O00O000O .grid (row =1 ,column =0 ,sticky ="w")#line:797
    OOO00OO0O00OO0OO0 =StringVar ()#line:798
    OOOOO000O0O0OO0O0 =ttk .Combobox (O00OOOO00000O000O ,width =25 ,height =10 ,state ="readonly",textvariable =OOO00OO0O00OO0OO0 )#line:801
    OOOOO000O0O0OO0O0 ["values"]=list (set (TT_ori ["作用对象"].to_list ()))#line:802
    OOOOO000O0O0OO0O0 .current (0 )#line:803
    OOOOO000O0O0OO0O0 .grid (row =1 ,column =1 )#line:804
    O0O0OO000O000000O =Label (O00OOOO00000O000O ,text ="分析对象：")#line:806
    O0O0OO000O000000O .grid (row =1 ,column =2 ,sticky ="w")#line:807
    OOOOOO000000O0000 =StringVar ()#line:810
    O000000O0OO000O00 =ttk .Combobox (O00OOOO00000O000O ,width =15 ,height =10 ,state ="readonly",textvariable =OOOOOO000000O0000 )#line:813
    O000000O0OO000O00 ["values"]=["事件发生月份","事件发生季度","产品批号","型号","规格"]#line:814
    O000000O0OO000O00 .current (0 )#line:816
    O000000O0OO000O00 .grid (row =1 ,column =3 )#line:817
    OOO00000OOOOOO000 =Label (O00OOOO00000O000O ,text ="事件发生起止时间：")#line:822
    OOO00000OOOOOO000 .grid (row =2 ,column =0 ,sticky ="w")#line:823
    OO000OO0O0OOO0O0O =Entry (O00OOOO00000O000O ,width =10 )#line:825
    OO000OO0O0OOO0O0O .insert (0 ,min (TT_ori ["事件发生日期"].dt .date ))#line:826
    OO000OO0O0OOO0O0O .grid (row =2 ,column =1 ,sticky ="w")#line:827
    O0O0O0O0OO00000OO =Entry (O00OOOO00000O000O ,width =10 )#line:829
    O0O0O0O0OO00000OO .insert (0 ,max (TT_ori ["事件发生日期"].dt .date ))#line:830
    O0O0O0O0OO00000OO .grid (row =2 ,column =2 ,sticky ="w")#line:831
    O000OOO0000OO0O00 =Button (O00OOOO00000O000O ,text ="原始查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,OOOOO000O0O0OO0O0 .get (),O000000O0OO000O00 .get (),OO000OO0O0OOO0O0O .get (),O0O0O0O0OO00000OO .get (),1 ))#line:841
    O000OOO0000OO0O00 .grid (row =3 ,column =2 ,sticky ="w")#line:842
    O000OOO0000OO0O00 =Button (O00OOOO00000O000O ,text ="分类查看",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,OOOOO000O0O0OO0O0 .get (),O000000O0OO000O00 .get (),OO000OO0O0OOO0O0O .get (),O0O0O0O0OO00000OO .get (),0 ))#line:852
    O000OOO0000OO0O00 .grid (row =3 ,column =3 ,sticky ="w")#line:853
    O000OOO0000OO0O00 =Button (O00OOOO00000O000O ,text ="趋势分析",width =10 ,bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :thread_it (Tread_TOOLS_doing ,TT_ori ,OOOOO000O0O0OO0O0 .get (),O000000O0OO000O00 .get (),OO000OO0O0OOO0O0O .get (),O0O0O0O0OO00000OO .get (),2 ))#line:863
    O000OOO0000OO0O00 .grid (row =3 ,column =1 ,sticky ="w")#line:864
def Tread_TOOLS_doing (OO0OOOO0OO0O0O0OO ,O0000O000000O0000 ,O0OOOOO000OOO000O ,OOO0OOOO0OOO000OO ,OOOOOO000OO00O0OO ,O0OOOOOOOOOOOO0OO ):#line:866
    ""#line:867
    global TT_biaozhun #line:868
    OO0OOOO0OO0O0O0OO =OO0OOOO0OO0O0O0OO [(OO0OOOO0OO0O0O0OO ["作用对象"]==O0000O000000O0000 )].copy ()#line:869
    OOO0OOOO0OOO000OO =pd .to_datetime (OOO0OOOO0OOO000OO )#line:871
    OOOOOO000OO00O0OO =pd .to_datetime (OOOOOO000OO00O0OO )#line:872
    OO0OOOO0OO0O0O0OO =OO0OOOO0OO0O0O0OO [((OO0OOOO0OO0O0O0OO ["事件发生日期"]>=OOO0OOOO0OOO000OO )&(OO0OOOO0OO0O0O0OO ["事件发生日期"]<=OOOOOO000OO00O0OO ))]#line:873
    text .insert (END ,"\n数据数量："+str (len (OO0OOOO0OO0O0O0OO )))#line:874
    text .see (END )#line:875
    if O0OOOOOOOOOOOO0OO ==0 :#line:877
        Tread_TOOLS_check (OO0OOOO0OO0O0O0OO ,TT_biaozhun ["关键字表"],0 )#line:878
        return 0 #line:879
    if O0OOOOOOOOOOOO0OO ==1 :#line:880
        Tread_TOOLS_tree_Level_2 (OO0OOOO0OO0O0O0OO ,1 ,OO0OOOO0OO0O0O0OO )#line:881
        return 0 #line:882
    if len (OO0OOOO0OO0O0O0OO )<1 :#line:883
        showinfo (title ="错误信息",message ="没有符合筛选条件的报告。")#line:884
        return 0 #line:885
    Tread_TOOLS_check (OO0OOOO0OO0O0O0OO ,TT_biaozhun ["关键字表"],1 )#line:886
    Tread_TOOLS_tree_Level_2 (Tread_TOOLS_Countall (OO0OOOO0OO0O0O0OO ).df_find_all_keword_risk (O0OOOOO000OOO000O ),1 ,0 ,O0OOOOO000OOO000O )#line:889
def STAT_countx (O0O0O0OO0OOOO0OOO ):#line:899
    ""#line:900
    return O0O0O0OO0OOOO0OOO .value_counts ().to_dict ()#line:901
def STAT_countpx (O0O00OO000OOOOO0O ,O000OOOOO0000O000 ):#line:903
    ""#line:904
    return len (O0O00OO000OOOOO0O [(O0O00OO000OOOOO0O ==O000OOOOO0000O000 )])#line:905
def STAT_countnpx (OOO0OOOO00O0O00O0 ,OO0OOOO0OO0OOOO0O ):#line:907
    ""#line:908
    return len (OOO0OOOO00O0O00O0 [(OOO0OOOO00O0O00O0 not in OO0OOOO0OO0OOOO0O )])#line:909
def STAT_get_max (OO0OOOO0OOOO00000 ):#line:911
    ""#line:912
    return OO0OOOO0OOOO00000 .value_counts ().max ()#line:913
def STAT_get_mean (O0O0000O0O00O0000 ):#line:915
    ""#line:916
    return round (O0O0000O0O00O0000 .value_counts ().mean (),2 )#line:917
def STAT_get_std (OO0OO0O0O000OO00O ):#line:919
    ""#line:920
    return round (OO0OO0O0O000OO00O .value_counts ().std (ddof =1 ),2 )#line:921
def STAT_get_95ci (O00OOOO000OO000OO ):#line:923
    ""#line:924
    return round (np .percentile (O00OOOO000OO000OO .value_counts (),97.5 ),2 )#line:925
def STAT_get_mean_std_ci (OO00OOO0OO00OO0OO ,OO00O0O00O000OOOO ):#line:927
    ""#line:928
    warnings .filterwarnings ("ignore")#line:929
    O000O0OOO0O0OOOO0 =TOOLS_strdict_to_pd (str (OO00OOO0OO00OO0OO ))["content"].values /OO00O0O00O000OOOO #line:930
    O0OO00O0O00O00000 =round (O000O0OOO0O0OOOO0 .mean (),2 )#line:931
    OOOOO00OOO0OOOOOO =round (O000O0OOO0O0OOOO0 .std (ddof =1 ),2 )#line:932
    OO0OOOO00O000O0O0 =round (np .percentile (O000O0OOO0O0OOOO0 ,97.5 ),2 )#line:933
    return pd .Series ((O0OO00O0O00O00000 ,OOOOO00OOO0OOOOOO ,OO0OOOO00O000O0O0 ))#line:934
def STAT_findx_value (OOOO0O000000O00OO ,O00O00O0OO0OO000O ):#line:936
    ""#line:937
    warnings .filterwarnings ("ignore")#line:938
    OOO0O000O0O000OOO =TOOLS_strdict_to_pd (str (OOOO0O000000O00OO ))#line:939
    OOO0OO00000OOOO0O =OOO0O000O0O000OOO .where (OOO0O000O0O000OOO ["index"]==str (O00O00O0OO0OO000O ))#line:941
    print (OOO0OO00000OOOO0O )#line:942
    return OOO0OO00000OOOO0O #line:943
def STAT_judge_x (OO000000O0OOOOOO0 ,OOOOO0O000OO0OOOO ):#line:945
    ""#line:946
    for O00OOO0OOO0OOO00O in OOOOO0O000OO0OOOO :#line:947
        if OO000000O0OOOOOO0 .find (O00OOO0OOO0OOO00O )>-1 :#line:948
            return 1 #line:949
def STAT_basic_risk (O000OO0000OO0OO00 ,OOO0000000O0OOOO0 ,OO0O0OOO0OOOOO00O ,OOO00O0OO0OOO000O ,OOOO00O0OOO00OO0O ):#line:952
    ""#line:953
    O000OO0000OO0OO00 ["风险评分"]=0 #line:954
    O000OO0000OO0OO00 .loc [((O000OO0000OO0OO00 [OOO0000000O0OOOO0 ]>=3 )&(O000OO0000OO0OO00 [OO0O0OOO0OOOOO00O ]>=1 ))|(O000OO0000OO0OO00 [OOO0000000O0OOOO0 ]>=5 ),"风险评分"]=O000OO0000OO0OO00 ["风险评分"]+5 #line:955
    O000OO0000OO0OO00 .loc [(O000OO0000OO0OO00 [OO0O0OOO0OOOOO00O ]>=3 ),"风险评分"]=O000OO0000OO0OO00 ["风险评分"]+1 #line:956
    O000OO0000OO0OO00 .loc [(O000OO0000OO0OO00 [OOO00O0OO0OOO000O ]>=1 ),"风险评分"]=O000OO0000OO0OO00 ["风险评分"]+10 #line:957
    O000OO0000OO0OO00 ["风险评分"]=O000OO0000OO0OO00 ["风险评分"]+O000OO0000OO0OO00 [OOOO00O0OOO00OO0O ]/100 #line:958
    return O000OO0000OO0OO00 #line:959
def STAT_find_keyword_risk (OO00OOO0O0OOO0O00 ,OO0O0OOOO0OO00OO0 ,O0O0O0OO0O000O00O ,O0OO0OOOO000OO0O0 ,OOO0000O0OOOOO0O0 ):#line:963
        ""#line:964
        O00O0O00O0OO000O0 =OO00OOO0O0OOO0O00 .groupby (OO0O0OOOO0OO00OO0 ).agg (证号关键字总数量 =(O0O0O0OO0O000O00O ,"count"),包含元素个数 =(O0OO0OOOO000OO0O0 ,"nunique"),包含元素 =(O0OO0OOOO000OO0O0 ,STAT_countx ),).reset_index ()#line:969
        OOO00O0O0000OOOO0 =OO0O0OOOO0OO00OO0 .copy ()#line:971
        OOO00O0O0000OOOO0 .append (O0OO0OOOO000OO0O0 )#line:972
        O0OOOO00O000O0OO0 =OO00OOO0O0OOO0O00 .groupby (OOO00O0O0000OOOO0 ).agg (计数 =(O0OO0OOOO000OO0O0 ,"count"),).reset_index ()#line:975
        O00000OOO00O000O0 =OOO00O0O0000OOOO0 .copy ()#line:978
        O00000OOO00O000O0 .remove ("关键字")#line:979
        OO0OOO0O00O0O0O0O =OO00OOO0O0OOO0O00 .groupby (O00000OOO00O000O0 ).agg (该元素总数 =(O0OO0OOOO000OO0O0 ,"count"),).reset_index ()#line:982
        O0OOOO00O000O0OO0 ["证号总数"]=OOO0000O0OOOOO0O0 #line:984
        OOOO0O00OO0OOOO0O =pd .merge (O0OOOO00O000O0OO0 ,O00O0O00O0OO000O0 ,on =OO0O0OOOO0OO00OO0 ,how ="left")#line:985
        if len (OOOO0O00OO0OOOO0O )>0 :#line:987
            OOOO0O00OO0OOOO0O [['数量均值','数量标准差','数量CI']]=OOOO0O00OO0OOOO0O .包含元素 .apply (lambda OO0OOOO0OO000O00O :STAT_get_mean_std_ci (OO0OOOO0OO000O00O ,1 ))#line:988
        return OOOO0O00OO0OOOO0O #line:989
def STAT_find_risk (OOO0OO0OOOO000O0O ,OO0O00O0O0OO0O0O0 ,O0O000O0O0OOO0OO0 ,OO0OO0O0OO0000000 ):#line:995
        ""#line:996
        O0OOOO0OOO0O0O00O =OOO0OO0OOOO000O0O .groupby (OO0O00O0O0OO0O0O0 ).agg (证号总数量 =(O0O000O0O0OOO0OO0 ,"count"),包含元素个数 =(OO0OO0O0OO0000000 ,"nunique"),包含元素 =(OO0OO0O0OO0000000 ,STAT_countx ),均值 =(OO0OO0O0OO0000000 ,STAT_get_mean ),标准差 =(OO0OO0O0OO0000000 ,STAT_get_std ),CI上限 =(OO0OO0O0OO0000000 ,STAT_get_95ci ),).reset_index ()#line:1004
        O000000OO00OO0O0O =OO0O00O0O0OO0O0O0 .copy ()#line:1006
        O000000OO00OO0O0O .append (OO0OO0O0OO0000000 )#line:1007
        OOOOOO0O0000O000O =OOO0OO0OOOO000O0O .groupby (O000000OO00OO0O0O ).agg (计数 =(OO0OO0O0OO0000000 ,"count"),严重伤害数 =("伤害",lambda OO0O0OO0O00O000O0 :STAT_countpx (OO0O0OO0O00O000O0 .values ,"严重伤害")),死亡数量 =("伤害",lambda OO00O0O0O0OO000OO :STAT_countpx (OO00O0O0O0OO000OO .values ,"死亡")),单位个数 =("单位名称","nunique"),单位列表 =("单位名称",STAT_countx ),).reset_index ()#line:1014
        O00O0OOOO0000000O =pd .merge (OOOOOO0O0000O000O ,O0OOOO0OOO0O0O00O ,on =OO0O00O0O0OO0O0O0 ,how ="left")#line:1016
        O00O0OOOO0000000O ["风险评分"]=0 #line:1018
        O00O0OOOO0000000O ["报表类型"]="dfx_findrisk"+OO0OO0O0OO0000000 #line:1019
        O00O0OOOO0000000O .loc [((O00O0OOOO0000000O ["计数"]>=3 )&(O00O0OOOO0000000O ["严重伤害数"]>=1 )|(O00O0OOOO0000000O ["计数"]>=5 )),"风险评分"]=O00O0OOOO0000000O ["风险评分"]+5 #line:1020
        O00O0OOOO0000000O .loc [(O00O0OOOO0000000O ["计数"]>=(O00O0OOOO0000000O ["均值"]+O00O0OOOO0000000O ["标准差"])),"风险评分"]=O00O0OOOO0000000O ["风险评分"]+1 #line:1021
        O00O0OOOO0000000O .loc [(O00O0OOOO0000000O ["计数"]>=O00O0OOOO0000000O ["CI上限"]),"风险评分"]=O00O0OOOO0000000O ["风险评分"]+1 #line:1022
        O00O0OOOO0000000O .loc [(O00O0OOOO0000000O ["严重伤害数"]>=3 )&(O00O0OOOO0000000O ["风险评分"]>=7 ),"风险评分"]=O00O0OOOO0000000O ["风险评分"]+1 #line:1023
        O00O0OOOO0000000O .loc [(O00O0OOOO0000000O ["死亡数量"]>=1 ),"风险评分"]=O00O0OOOO0000000O ["风险评分"]+10 #line:1024
        O00O0OOOO0000000O ["风险评分"]=O00O0OOOO0000000O ["风险评分"]+O00O0OOOO0000000O ["单位个数"]/100 #line:1025
        O00O0OOOO0000000O =O00O0OOOO0000000O .sort_values (by ="风险评分",ascending =[False ],na_position ="last").reset_index (drop =True )#line:1026
        return O00O0OOOO0000000O #line:1028
def TOOLS_get_list (OOOOO000000O0O0OO ):#line:1030
    ""#line:1031
    OOOOO000000O0O0OO =str (OOOOO000000O0O0OO )#line:1032
    O00O0O0O0OO0O0O0O =[]#line:1033
    O00O0O0O0OO0O0O0O .append (OOOOO000000O0O0OO )#line:1034
    O00O0O0O0OO0O0O0O =",".join (O00O0O0O0OO0O0O0O )#line:1035
    O00O0O0O0OO0O0O0O =O00O0O0O0OO0O0O0O .split ("|")#line:1036
    OOO0OOO00O000000O =O00O0O0O0OO0O0O0O [:]#line:1037
    O00O0O0O0OO0O0O0O =list (set (O00O0O0O0OO0O0O0O ))#line:1038
    O00O0O0O0OO0O0O0O .sort (key =OOO0OOO00O000000O .index )#line:1039
    return O00O0O0O0OO0O0O0O #line:1040
def TOOLS_get_list0 (O00OOOO000000OOO0 ,OOOOOO0O0OO0O0O0O ,*O0O0000O0OOO0O0O0 ):#line:1042
    ""#line:1043
    O00OOOO000000OOO0 =str (O00OOOO000000OOO0 )#line:1044
    if pd .notnull (O00OOOO000000OOO0 ):#line:1046
        try :#line:1047
            if "use("in str (O00OOOO000000OOO0 ):#line:1048
                O0OO0OO0OOOO0O0O0 =O00OOOO000000OOO0 #line:1049
                OOO0000O00O0OO0OO =re .compile (r"[(](.*?)[)]",re .S )#line:1050
                OOOO0O0O0000OO0OO =re .findall (OOO0000O00O0OO0OO ,O0OO0OO0OOOO0O0O0 )#line:1051
                O0O0OO0OOOO00OOOO =[]#line:1052
                if ").list"in O00OOOO000000OOO0 :#line:1053
                    O0O0O0O0OOOOO00O0 ="配置表/"+str (OOOO0O0O0000OO0OO [0 ])+".xls"#line:1054
                    O00O0OO00O0O0OOO0 =pd .read_excel (O0O0O0O0OOOOO00O0 ,sheet_name =OOOO0O0O0000OO0OO [0 ],header =0 ,index_col =0 ).reset_index ()#line:1057
                    O00O0OO00O0O0OOO0 ["检索关键字"]=O00O0OO00O0O0OOO0 ["检索关键字"].astype (str )#line:1058
                    O0O0OO0OOOO00OOOO =O00O0OO00O0O0OOO0 ["检索关键字"].tolist ()+O0O0OO0OOOO00OOOO #line:1059
                if ").file"in O00OOOO000000OOO0 :#line:1060
                    O0O0OO0OOOO00OOOO =OOOOOO0O0OO0O0O0O [OOOO0O0O0000OO0OO [0 ]].astype (str ).tolist ()+O0O0OO0OOOO00OOOO #line:1062
                try :#line:1065
                    if "报告类型-新的"in OOOOOO0O0OO0O0O0O .columns :#line:1066
                        O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1067
                        O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split (";")#line:1068
                        O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1069
                        O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split ("；")#line:1070
                        O0O0OO0OOOO00OOOO =[O00000O0OO0O00OOO .replace ("（严重）","")for O00000O0OO0O00OOO in O0O0OO0OOOO00OOOO ]#line:1071
                        O0O0OO0OOOO00OOOO =[O000OOOOOO0000O0O .replace ("（一般）","")for O000OOOOOO0000O0O in O0O0OO0OOOO00OOOO ]#line:1072
                except :#line:1073
                    pass #line:1074
                O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1077
                O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split ("、")#line:1078
                O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1079
                O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split ("，")#line:1080
                O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1081
                O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split (",")#line:1082
                O000O000O0O0OO00O =O0O0OO0OOOO00OOOO [:]#line:1084
                try :#line:1085
                    if O0O0000O0OOO0O0O0 [0 ]==1000 :#line:1086
                      pass #line:1087
                except :#line:1088
                      O0O0OO0OOOO00OOOO =list (set (O0O0OO0OOOO00OOOO ))#line:1089
                O0O0OO0OOOO00OOOO .sort (key =O000O000O0O0OO00O .index )#line:1090
            else :#line:1092
                O00OOOO000000OOO0 =str (O00OOOO000000OOO0 )#line:1093
                O0O0OO0OOOO00OOOO =[]#line:1094
                O0O0OO0OOOO00OOOO .append (O00OOOO000000OOO0 )#line:1095
                O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1096
                O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split ("、")#line:1097
                O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1098
                O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split ("，")#line:1099
                O0O0OO0OOOO00OOOO =",".join (O0O0OO0OOOO00OOOO )#line:1100
                O0O0OO0OOOO00OOOO =O0O0OO0OOOO00OOOO .split (",")#line:1101
                O000O000O0O0OO00O =O0O0OO0OOOO00OOOO [:]#line:1103
                try :#line:1104
                    if O0O0000O0OOO0O0O0 [0 ]==1000 :#line:1105
                      O0O0OO0OOOO00OOOO =list (set (O0O0OO0OOOO00OOOO ))#line:1106
                except :#line:1107
                      pass #line:1108
                O0O0OO0OOOO00OOOO .sort (key =O000O000O0O0OO00O .index )#line:1109
                O0O0OO0OOOO00OOOO .sort (key =O000O000O0O0OO00O .index )#line:1110
        except ValueError2 :#line:1112
            showinfo (title ="提示信息",message ="创建单元格支持多个甚至表单（文件）传入的方法，返回一个经过整理的清单出错，任务终止。")#line:1113
            return False #line:1114
    return O0O0OO0OOOO00OOOO #line:1116
def TOOLS_strdict_to_pd (O0OOO000O0O00OOO0 ):#line:1117
    ""#line:1118
    return pd .DataFrame .from_dict (eval (O0OOO000O0O00OOO0 ),orient ="index",columns =["content"]).reset_index ()#line:1119
def Tread_TOOLS_view_dict (OO0OOOOO0O0O0OO00 ,OOOO000OO0OO0000O ):#line:1121
    ""#line:1122
    O00O000O00O000OO0 =Toplevel ()#line:1123
    O00O000O00O000OO0 .title ("查看数据")#line:1124
    O00O000O00O000OO0 .geometry ("700x500")#line:1125
    OO000O00000O00OO0 =Scrollbar (O00O000O00O000OO0 )#line:1127
    OOO00000OO00OO0OO =Text (O00O000O00O000OO0 ,height =100 ,width =150 )#line:1128
    OO000O00000O00OO0 .pack (side =RIGHT ,fill =Y )#line:1129
    OOO00000OO00OO0OO .pack ()#line:1130
    OO000O00000O00OO0 .config (command =OOO00000OO00OO0OO .yview )#line:1131
    OOO00000OO00OO0OO .config (yscrollcommand =OO000O00000O00OO0 .set )#line:1132
    if OOOO000OO0OO0000O ==1 :#line:1133
        OOO00000OO00OO0OO .insert (END ,OO0OOOOO0O0O0OO00 )#line:1135
        OOO00000OO00OO0OO .insert (END ,"\n\n")#line:1136
        return 0 #line:1137
    for O00OOO0OOO000O0OO in range (len (OO0OOOOO0O0O0OO00 )):#line:1138
        OOO00000OO00OO0OO .insert (END ,OO0OOOOO0O0O0OO00 .iloc [O00OOO0OOO000O0OO ,0 ])#line:1139
        OOO00000OO00OO0OO .insert (END ,":")#line:1140
        OOO00000OO00OO0OO .insert (END ,OO0OOOOO0O0O0OO00 .iloc [O00OOO0OOO000O0OO ,1 ])#line:1141
        OOO00000OO00OO0OO .insert (END ,"\n\n")#line:1142
def Tread_TOOLS_fashenglv (OO00O0O0OO00O0O0O ,O0O0O0OOO00OO000O ):#line:1145
    global TT_biaozhun #line:1146
    OO00O0O0OO00O0O0O =pd .merge (OO00O0O0OO00O0O0O ,TT_biaozhun [O0O0O0OOO00OO000O ],on =[O0O0O0OOO00OO000O ],how ="left").reset_index (drop =True )#line:1147
    OOOO0OO0O00O0OO00 =OO00O0O0OO00O0O0O ["使用次数"].mean ()#line:1149
    OO00O0O0OO00O0O0O ["使用次数"]=OO00O0O0OO00O0O0O ["使用次数"].fillna (int (OOOO0OO0O00O0OO00 ))#line:1150
    OOOOO0O0000000O0O =OO00O0O0OO00O0O0O ["使用次数"][:-1 ].sum ()#line:1151
    OO00O0O0OO00O0O0O .iloc [-1 ,-1 ]=OOOOO0O0000000O0O #line:1152
    OO0OO0000OO0000OO =[O0OOOOO000O0OO0OO for O0OOOOO000O0OO0OO in OO00O0O0OO00O0O0O .columns if (O0OOOOO000O0OO0OO not in ["使用次数",O0O0O0OOO00OO000O ])]#line:1153
    for OO0OO000O0O00OO00 ,O000O0000O0O0O00O in OO00O0O0OO00O0O0O .iterrows ():#line:1154
        for O000OOOO000000OOO in OO0OO0000OO0000OO :#line:1155
            OO00O0O0OO00O0O0O .loc [OO0OO000O0O00OO00 ,O000OOOO000000OOO ]=int (O000O0000O0O0O00O [O000OOOO000000OOO ])/int (O000O0000O0O0O00O ["使用次数"])#line:1156
    del OO00O0O0OO00O0O0O ["使用次数"]#line:1157
    Tread_TOOLS_tree_Level_2 (OO00O0O0OO00O0O0O ,1 ,1 ,O0O0O0OOO00OO000O )#line:1158
def TOOLS_save_dict (OOOOO000O000OO0OO ):#line:1160
    ""#line:1161
    OOOO000OOO0OO0O00 =filedialog .asksaveasfilename (title =u"保存文件",initialfile ="【排序后的原始数据】.xls",defaultextension ="xls",filetypes =[("Excel 97-2003 工作簿","*.xls")],)#line:1167
    try :#line:1168
        OOOOO000O000OO0OO ["详细描述T"]=OOOOO000O000OO0OO ["详细描述T"].astype (str )#line:1169
    except :#line:1170
        pass #line:1171
    try :#line:1172
        OOOOO000O000OO0OO ["报告编码"]=OOOOO000O000OO0OO ["报告编码"].astype (str )#line:1173
    except :#line:1174
        pass #line:1175
    try :#line:1176
        O0OO0000OO00OO0O0 =re .search ("\【(.*?)\】",OOOO000OOO0OO0O00 )#line:1177
        OOOOO000O000OO0OO ["对象"]=O0OO0000OO00OO0O0 .group (1 )#line:1178
    except :#line:1179
        pass #line:1180
    O0OO00OO0O00OO00O =pd .ExcelWriter (OOOO000OOO0OO0O00 ,engine ="xlsxwriter")#line:1181
    OOOOO000O000OO0OO .to_excel (O0OO00OO0O00OO00O ,sheet_name ="字典数据")#line:1182
    O0OO00OO0O00OO00O .close ()#line:1183
    showinfo (title ="提示",message ="文件写入成功。")#line:1184
def Tread_TOOLS_DRAW_histbar (OO0000O0OO0OO00O0 ):#line:1188
    ""#line:1189
    OO0O000O00O0000OO =Toplevel ()#line:1192
    OO0O000O00O0000OO .title ("直方图")#line:1193
    OOO000O0O0OO0000O =ttk .Frame (OO0O000O00O0000OO ,height =20 )#line:1194
    OOO000O0O0OO0000O .pack (side =TOP )#line:1195
    OO0000O000OO0OOO0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:1197
    OOOOO00OO0000O00O =FigureCanvasTkAgg (OO0000O000OO0OOO0 ,master =OO0O000O00O0000OO )#line:1198
    OOOOO00OO0000O00O .draw ()#line:1199
    OOOOO00OO0000O00O .get_tk_widget ().pack (expand =1 )#line:1200
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1202
    plt .rcParams ['axes.unicode_minus']=False #line:1203
    OO00OO0O0000O0OOO =NavigationToolbar2Tk (OOOOO00OO0000O00O ,OO0O000O00O0000OO )#line:1205
    OO00OO0O0000O0OOO .update ()#line:1206
    OOOOO00OO0000O00O .get_tk_widget ().pack ()#line:1207
    OO00OO00OO0OO0OO0 =OO0000O000OO0OOO0 .add_subplot (111 )#line:1209
    OO00OO00OO0OO0OO0 .set_title ("直方图")#line:1211
    O000O0OO000O00OOO =OO0000O0OO0OO00O0 .columns .to_list ()#line:1213
    O000O0OO000O00OOO .remove ("对象")#line:1214
    OO00O00OOO00OOO00 =np .arange (len (O000O0OO000O00OOO ))#line:1215
    for OO00O000OO0OO0O0O in O000O0OO000O00OOO :#line:1219
        OO0000O0OO0OO00O0 [OO00O000OO0OO0O0O ]=OO0000O0OO0OO00O0 [OO00O000OO0OO0O0O ].astype (float )#line:1220
    OO0000O0OO0OO00O0 ['数据']=OO0000O0OO0OO00O0 [O000O0OO000O00OOO ].values .tolist ()#line:1222
    O0OO00OOO00OO0OO0 =0 #line:1223
    for O0O0O00OOOO000O0O ,OO0000O00O00OOO00 in OO0000O0OO0OO00O0 .iterrows ():#line:1224
        OO00OO00OO0OO0OO0 .bar ([OOO0O0O00OOOOOO00 +O0OO00OOO00OO0OO0 for OOO0O0O00OOOOOO00 in OO00O00OOO00OOO00 ],OO0000O0OO0OO00O0 .loc [O0O0O00OOOO000O0O ,'数据'],label =O000O0OO000O00OOO ,width =0.1 )#line:1225
        for O00O00O00OOOOOO0O ,O00OO0O0O0OO00OOO in zip ([O0O00O00OO0OOO0OO +O0OO00OOO00OO0OO0 for O0O00O00OO0OOO0OO in OO00O00OOO00OOO00 ],OO0000O0OO0OO00O0 .loc [O0O0O00OOOO000O0O ,'数据']):#line:1228
           OO00OO00OO0OO0OO0 .text (O00O00O00OOOOOO0O -0.015 ,O00OO0O0O0OO00OOO +0.07 ,str (int (O00OO0O0O0OO00OOO )),color ='black',size =8 )#line:1229
        O0OO00OOO00OO0OO0 =O0OO00OOO00OO0OO0 +0.1 #line:1231
    OO00OO00OO0OO0OO0 .set_xticklabels (OO0000O0OO0OO00O0 .columns .to_list (),rotation =-90 ,fontsize =8 )#line:1233
    OO00OO00OO0OO0OO0 .legend (OO0000O0OO0OO00O0 ["对象"])#line:1237
    OOOOO00OO0000O00O .draw ()#line:1240
def Tread_TOOLS_DRAW_make_risk_plot (OO000OO0OO0OO00O0 ,O00OOOOO0O0OOO00O ,O0O0O0OO000O000O0 ,O0O00O00O00O00000 ,OO000000OO00OO0OO ):#line:1242
    ""#line:1243
    OO000OOOOO0OO00O0 =Toplevel ()#line:1246
    OO000OOOOO0OO00O0 .title (O0O00O00O00O00000 )#line:1247
    O000O0OOOOO0O0O0O =ttk .Frame (OO000OOOOO0OO00O0 ,height =20 )#line:1248
    O000O0OOOOO0O0O0O .pack (side =TOP )#line:1249
    O0000OO0O0OOO0OOO =Figure (figsize =(12 ,6 ),dpi =100 )#line:1251
    O0OO0OOO0OO000000 =FigureCanvasTkAgg (O0000OO0O0OOO0OOO ,master =OO000OOOOO0OO00O0 )#line:1252
    O0OO0OOO0OO000000 .draw ()#line:1253
    O0OO0OOO0OO000000 .get_tk_widget ().pack (expand =1 )#line:1254
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1256
    plt .rcParams ['axes.unicode_minus']=False #line:1257
    O00O0O00O000OOO0O =NavigationToolbar2Tk (O0OO0OOO0OO000000 ,OO000OOOOO0OO00O0 )#line:1259
    O00O0O00O000OOO0O .update ()#line:1260
    O0OO0OOO0OO000000 .get_tk_widget ().pack ()#line:1261
    O0O00O00O00O00O00 =O0000OO0O0OOO0OOO .add_subplot (111 )#line:1263
    O0O00O00O00O00O00 .set_title (O0O00O00O00O00000 )#line:1265
    OO0OO0O0O00O000O0 =OO000OO0OO0OO00O0 [O00OOOOO0O0OOO00O ]#line:1266
    if OO000000OO00OO0OO !=999 :#line:1269
        O0O00O00O00O00O00 .set_xticklabels (OO0OO0O0O00O000O0 ,rotation =-90 ,fontsize =8 )#line:1270
    OO0OOO000O0OO0OOO =range (0 ,len (OO0OO0O0O00O000O0 ),1 )#line:1273
    for OOOO0000OO0O0OOO0 in O0O0O0OO000O000O0 :#line:1278
        OO0OOOOOO0OOO000O =OO000OO0OO0OO00O0 [OOOO0000OO0O0OOO0 ].astype (float )#line:1279
        if OOOO0000OO0O0OOO0 =="关注区域":#line:1281
            O0O00O00O00O00O00 .plot (list (OO0OO0O0O00O000O0 ),list (OO0OOOOOO0OOO000O ),label =str (OOOO0000OO0O0OOO0 ),color ="red")#line:1282
        else :#line:1283
            O0O00O00O00O00O00 .plot (list (OO0OO0O0O00O000O0 ),list (OO0OOOOOO0OOO000O ),label =str (OOOO0000OO0O0OOO0 ))#line:1284
        if OO000000OO00OO0OO ==100 :#line:1287
            for O000000OOOOO00O00 ,O00OOO0O0OOOO00OO in zip (OO0OO0O0O00O000O0 ,OO0OOOOOO0OOO000O ):#line:1288
                if O00OOO0O0OOOO00OO ==max (OO0OOOOOO0OOO000O )and O00OOO0O0OOOO00OO >=3 and len (O0O0O0OO000O000O0 )!=1 :#line:1289
                     O0O00O00O00O00O00 .text (O000000OOOOO00O00 ,O00OOO0O0OOOO00OO ,(str (OOOO0000OO0O0OOO0 )+":"+str (int (O00OOO0O0OOOO00OO ))),color ='black',size =8 )#line:1290
                if len (O0O0O0OO000O000O0 )==1 and O00OOO0O0OOOO00OO >=0.01 :#line:1291
                     O0O00O00O00O00O00 .text (O000000OOOOO00O00 ,O00OOO0O0OOOO00OO ,str (int (O00OOO0O0OOOO00OO )),color ='black',size =8 )#line:1292
    if len (O0O0O0OO000O000O0 )==1 :#line:1302
        O00O0O0O0O0OO000O =OO000OO0OO0OO00O0 [O0O0O0OO000O000O0 ].astype (float ).values #line:1303
        OO0OOOOO0000O000O =O00O0O0O0O0OO000O .mean ()#line:1304
        O00O0O00O000OOOOO =O00O0O0O0O0OO000O .std ()#line:1305
        OOO0O000O0O00O0O0 =OO0OOOOO0000O000O +3 *O00O0O00O000OOOOO #line:1306
        OO00000000OO0OOO0 =O00O0O00O000OOOOO -3 *O00O0O00O000OOOOO #line:1307
        O0O00O00O00O00O00 .axhline (OO0OOOOO0000O000O ,color ='r',linestyle ='--',label ='Mean')#line:1309
        O0O00O00O00O00O00 .axhline (OOO0O000O0O00O0O0 ,color ='g',linestyle ='--',label ='UCL(μ+3σ)')#line:1310
        O0O00O00O00O00O00 .axhline (OO00000000OO0OOO0 ,color ='g',linestyle ='--',label ='LCL(μ-3σ)')#line:1311
    O0O00O00O00O00O00 .set_title ("控制图")#line:1313
    O0O00O00O00O00O00 .set_xlabel ("项")#line:1314
    O0000OO0O0OOO0OOO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1315
    O0OO0O00000OOOO0O =O0O00O00O00O00O00 .get_position ()#line:1316
    O0O00O00O00O00O00 .set_position ([O0OO0O00000OOOO0O .x0 ,O0OO0O00000OOOO0O .y0 ,O0OO0O00000OOOO0O .width *0.7 ,O0OO0O00000OOOO0O .height ])#line:1317
    O0O00O00O00O00O00 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1318
    OO000O0OOO0O00000 =StringVar ()#line:1321
    OO0OOOO0O0OO00O00 =ttk .Combobox (O000O0OOOOO0O0O0O ,width =15 ,textvariable =OO000O0OOO0O00000 ,state ='readonly')#line:1322
    OO0OOOO0O0OO00O00 ['values']=O0O0O0OO000O000O0 #line:1323
    OO0OOOO0O0OO00O00 .pack (side =LEFT )#line:1324
    OO0OOOO0O0OO00O00 .current (0 )#line:1325
    OO0O0OO0OO0OOOOO0 =Button (O000O0OOOOO0O0O0O ,text ="控制图（单项）",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OO000OO0OO0OO00O0 ,O00OOOOO0O0OOO00O ,[O000OOOO0OO0OO000 for O000OOOO0OO0OO000 in O0O0O0OO000O000O0 if OO000O0OOO0O00000 .get ()in O000OOOO0OO0OO000 ],O0O00O00O00O00000 ,OO000000OO00OO0OO ))#line:1335
    OO0O0OO0OO0OOOOO0 .pack (side =LEFT ,anchor ="ne")#line:1336
    O0OO0O0OOOOOO0OOO =Button (O000O0OOOOO0O0O0O ,text ="去除标记",bg ="white",font =("微软雅黑",10 ),relief =GROOVE ,activebackground ="green",command =lambda :Tread_TOOLS_DRAW_make_risk_plot (OO000OO0OO0OO00O0 ,O00OOOOO0O0OOO00O ,O0O0O0OO000O000O0 ,O0O00O00O00O00000 ,0 ))#line:1344
    O0OO0O0OOOOOO0OOO .pack (side =LEFT ,anchor ="ne")#line:1346
    O0OO0OOO0OO000000 .draw ()#line:1347
def Tread_TOOLS_draw (OO0OO00O0OO000000 ,OOO0000OOO0OOO0O0 ,O00000O0O00OOO0OO ,O0000OO000O0O0OO0 ,O00OOOO0O0000O00O ):#line:1349
    ""#line:1350
    warnings .filterwarnings ("ignore")#line:1351
    OOO00OOOO0OO0O0OO =Toplevel ()#line:1352
    OOO00OOOO0OO0O0OO .title (OOO0000OOO0OOO0O0 )#line:1353
    OO00O0000000OO00O =ttk .Frame (OOO00OOOO0OO0O0OO ,height =20 )#line:1354
    OO00O0000000OO00O .pack (side =TOP )#line:1355
    O00OOOOO0O00O0OOO =Figure (figsize =(12 ,6 ),dpi =100 )#line:1357
    OOO0OO0OOOO0OOOOO =FigureCanvasTkAgg (O00OOOOO0O00O0OOO ,master =OOO00OOOO0OO0O0OO )#line:1358
    OOO0OO0OOOO0OOOOO .draw ()#line:1359
    OOO0OO0OOOO0OOOOO .get_tk_widget ().pack (expand =1 )#line:1360
    O00OOOOOOO0000OO0 =O00OOOOO0O00O0OOO .add_subplot (111 )#line:1361
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1363
    plt .rcParams ['axes.unicode_minus']=False #line:1364
    O0OO00OO00O0OO0OO =NavigationToolbar2Tk (OOO0OO0OOOO0OOOOO ,OOO00OOOO0OO0O0OO )#line:1366
    O0OO00OO00O0OO0OO .update ()#line:1367
    OOO0OO0OOOO0OOOOO .get_tk_widget ().pack ()#line:1369
    try :#line:1372
        O0O0OO000OOOO0000 =OO0OO00O0OO000000 .columns #line:1373
        OO0OO00O0OO000000 =OO0OO00O0OO000000 .sort_values (by =O0000OO000O0O0OO0 ,ascending =[False ],na_position ="last")#line:1374
    except :#line:1375
        OO000OO0O0O00O00O =eval (OO0OO00O0OO000000 )#line:1376
        OO000OO0O0O00O00O =pd .DataFrame .from_dict (OO000OO0O0O00O00O ,TT_orient =O00000O0O00OOO0OO ,columns =[O0000OO000O0O0OO0 ]).reset_index ()#line:1379
        OO0OO00O0OO000000 =OO000OO0O0O00O00O .sort_values (by =O0000OO000O0O0OO0 ,ascending =[False ],na_position ="last")#line:1380
    if ("日期"in OOO0000OOO0OOO0O0 or "时间"in OOO0000OOO0OOO0O0 or "季度"in OOO0000OOO0OOO0O0 )and "饼图"not in O00OOOO0O0000O00O :#line:1384
        OO0OO00O0OO000000 [O00000O0O00OOO0OO ]=pd .to_datetime (OO0OO00O0OO000000 [O00000O0O00OOO0OO ],format ="%Y/%m/%d").dt .date #line:1385
        OO0OO00O0OO000000 =OO0OO00O0OO000000 .sort_values (by =O00000O0O00OOO0OO ,ascending =[True ],na_position ="last")#line:1386
    elif "批号"in OOO0000OOO0OOO0O0 :#line:1387
        OO0OO00O0OO000000 [O00000O0O00OOO0OO ]=OO0OO00O0OO000000 [O00000O0O00OOO0OO ].astype (str )#line:1388
        OO0OO00O0OO000000 =OO0OO00O0OO000000 .sort_values (by =O00000O0O00OOO0OO ,ascending =[True ],na_position ="last")#line:1389
        O00OOOOOOO0000OO0 .set_xticklabels (OO0OO00O0OO000000 [O00000O0O00OOO0OO ],rotation =-90 ,fontsize =8 )#line:1390
    else :#line:1391
        OO0OO00O0OO000000 [O00000O0O00OOO0OO ]=OO0OO00O0OO000000 [O00000O0O00OOO0OO ].astype (str )#line:1392
        O00OOOOOOO0000OO0 .set_xticklabels (OO0OO00O0OO000000 [O00000O0O00OOO0OO ],rotation =-90 ,fontsize =8 )#line:1393
    O0OOOOO0O0OO0O000 =OO0OO00O0OO000000 [O0000OO000O0O0OO0 ]#line:1395
    OO00000000O00OO00 =range (0 ,len (O0OOOOO0O0OO0O000 ),1 )#line:1396
    O00OOOOOOO0000OO0 .set_title (OOO0000OOO0OOO0O0 )#line:1398
    if O00OOOO0O0000O00O =="柱状图":#line:1402
        O00OOOOOOO0000OO0 .bar (x =OO0OO00O0OO000000 [O00000O0O00OOO0OO ],height =O0OOOOO0O0OO0O000 ,width =0.2 ,color ="#87CEFA")#line:1403
    elif O00OOOO0O0000O00O =="饼图":#line:1404
        O00OOOOOOO0000OO0 .pie (x =O0OOOOO0O0OO0O000 ,labels =OO0OO00O0OO000000 [O00000O0O00OOO0OO ],autopct ="%0.2f%%")#line:1405
    elif O00OOOO0O0000O00O =="折线图":#line:1406
        O00OOOOOOO0000OO0 .plot (OO0OO00O0OO000000 [O00000O0O00OOO0OO ],O0OOOOO0O0OO0O000 ,lw =0.5 ,ls ='-',c ="r",alpha =0.5 )#line:1407
    elif "帕累托图"in str (O00OOOO0O0000O00O ):#line:1409
        OO0000O0O0000OO00 =OO0OO00O0OO000000 [O0000OO000O0O0OO0 ].fillna (0 )#line:1410
        O000000O0OO00OO00 =OO0000O0O0000OO00 .cumsum ()/OO0000O0O0000OO00 .sum ()*100 #line:1414
        OO0OO00O0OO000000 ["百分比"]=round (OO0OO00O0OO000000 ["数量"]/OO0000O0O0000OO00 .sum ()*100 ,2 )#line:1415
        OO0OO00O0OO000000 ["累计百分比"]=round (O000000O0OO00OO00 ,2 )#line:1416
        OO00OO00OO0O000O0 =O000000O0OO00OO00 [O000000O0OO00OO00 >0.8 ].index [0 ]#line:1417
        O0OOO00OO00O0O0OO =OO0000O0O0000OO00 .index .tolist ().index (OO00OO00OO0O000O0 )#line:1418
        O00OOOOOOO0000OO0 .bar (x =OO0OO00O0OO000000 [O00000O0O00OOO0OO ],height =OO0000O0O0000OO00 ,color ="C0",label =O0000OO000O0O0OO0 )#line:1422
        O0O00000O00OOO0OO =O00OOOOOOO0000OO0 .twinx ()#line:1423
        O0O00000O00OOO0OO .plot (OO0OO00O0OO000000 [O00000O0O00OOO0OO ],O000000O0OO00OO00 ,color ="C1",alpha =0.6 ,label ="累计比例")#line:1424
        O0O00000O00OOO0OO .yaxis .set_major_formatter (PercentFormatter ())#line:1425
        O00OOOOOOO0000OO0 .tick_params (axis ="y",colors ="C0")#line:1430
        O0O00000O00OOO0OO .tick_params (axis ="y",colors ="C1")#line:1431
        for OOO00O00O0OOO00OO ,OOOOO0000OO0O000O ,OOOO0OO0000O0000O ,O00OO0O0O0O0OOO0O in zip (OO0OO00O0OO000000 [O00000O0O00OOO0OO ],OO0000O0O0000OO00 ,OO0OO00O0OO000000 ["百分比"],OO0OO00O0OO000000 ["累计百分比"]):#line:1433
            O00OOOOOOO0000OO0 .text (OOO00O00O0OOO00OO ,OOOOO0000OO0O000O +0.1 ,str (int (OOOOO0000OO0O000O ))+", "+str (int (OOOO0OO0000O0000O ))+"%,"+str (int (O00OO0O0O0O0OOO0O ))+"%",color ='black',size =8 )#line:1434
        if "超级帕累托图"in str (O00OOOO0O0000O00O ):#line:1437
            OO00000000OO00000 =re .compile (r'[(](.*?)[)]',re .S )#line:1438
            OOOO0OO0O0OO0OOOO =re .findall (OO00000000OO00000 ,O00OOOO0O0000O00O )[0 ]#line:1439
            O00OOOOOOO0000OO0 .bar (x =OO0OO00O0OO000000 [O00000O0O00OOO0OO ],height =OO0OO00O0OO000000 [OOOO0OO0O0OO0OOOO ],color ="orangered",label =OOOO0OO0O0OO0OOOO )#line:1440
    O00OOOOO0O00O0OOO .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1445
    O0O00OO0000OOOOOO =O00OOOOOOO0000OO0 .get_position ()#line:1446
    O00OOOOOOO0000OO0 .set_position ([O0O00OO0000OOOOOO .x0 ,O0O00OO0000OOOOOO .y0 ,O0O00OO0000OOOOOO .width *0.7 ,O0O00OO0000OOOOOO .height ])#line:1447
    O00OOOOOOO0000OO0 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1448
    OOO0OO0OOOO0OOOOO .draw ()#line:1451
    if len (O0OOOOO0O0OO0O000 )<=20 and O00OOOO0O0000O00O !="饼图"and O00OOOO0O0000O00O !="帕累托图":#line:1454
        for O000O000OOOOOOOOO ,OOOOO0000000OOO0O in zip (OO00000000O00OO00 ,O0OOOOO0O0OO0O000 ):#line:1455
            OO0O0O0OOOOOO0000 =str (OOOOO0000000OOO0O )#line:1456
            OOOO00O0OOO0O0OOO =(O000O000OOOOOOOOO ,OOOOO0000000OOO0O +0.3 )#line:1457
            O00OOOOOOO0000OO0 .annotate (OO0O0O0OOOOOO0000 ,xy =OOOO00O0OOO0O0OOO ,fontsize =8 ,color ="black",ha ="center",va ="baseline")#line:1458
    O000000OOO0OOO00O =Button (OO00O0000000OO00O ,relief =GROOVE ,activebackground ="green",text ="保存原始数据",command =lambda :TOOLS_save_dict (OO0OO00O0OO000000 ),)#line:1468
    O000000OOO0OOO00O .pack (side =RIGHT )#line:1469
    O0OO00000OOO0O00O =Button (OO00O0000000OO00O ,relief =GROOVE ,text ="查看原始数据",command =lambda :Tread_TOOLS_view_dict (OO0OO00O0OO000000 ,1 ))#line:1473
    O0OO00000OOO0O00O .pack (side =RIGHT )#line:1474
    O000OO00OO00O0000 =Button (OO00O0000000OO00O ,relief =GROOVE ,text ="饼图",command =lambda :Tread_TOOLS_draw (OO0OO00O0OO000000 ,OOO0000OOO0OOO0O0 ,O00000O0O00OOO0OO ,O0000OO000O0O0OO0 ,"饼图"),)#line:1482
    O000OO00OO00O0000 .pack (side =LEFT )#line:1483
    O000OO00OO00O0000 =Button (OO00O0000000OO00O ,relief =GROOVE ,text ="柱状图",command =lambda :Tread_TOOLS_draw (OO0OO00O0OO000000 ,OOO0000OOO0OOO0O0 ,O00000O0O00OOO0OO ,O0000OO000O0O0OO0 ,"柱状图"),)#line:1490
    O000OO00OO00O0000 .pack (side =LEFT )#line:1491
    O000OO00OO00O0000 =Button (OO00O0000000OO00O ,relief =GROOVE ,text ="折线图",command =lambda :Tread_TOOLS_draw (OO0OO00O0OO000000 ,OOO0000OOO0OOO0O0 ,O00000O0O00OOO0OO ,O0000OO000O0O0OO0 ,"折线图"),)#line:1497
    O000OO00OO00O0000 .pack (side =LEFT )#line:1498
    O000OO00OO00O0000 =Button (OO00O0000000OO00O ,relief =GROOVE ,text ="帕累托图",command =lambda :Tread_TOOLS_draw (OO0OO00O0OO000000 ,OOO0000OOO0OOO0O0 ,O00000O0O00OOO0OO ,O0000OO000O0O0OO0 ,"帕累托图"),)#line:1505
    O000OO00OO00O0000 .pack (side =LEFT )#line:1506
def helper ():#line:1512
    ""#line:1513
    O0O0O000O0000O00O =Toplevel ()#line:1514
    O0O0O000O0000O00O .title ("程序使用帮助")#line:1515
    O0O0O000O0000O00O .geometry ("700x500")#line:1516
    O000O0OO00OOOO000 =Scrollbar (O0O0O000O0000O00O )#line:1518
    O0OO0OO000OO0O000 =Text (O0O0O000O0000O00O ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1519
    O000O0OO00OOOO000 .pack (side =RIGHT ,fill =Y )#line:1520
    O0OO0OO000OO0O000 .pack ()#line:1521
    O000O0OO00OOOO000 .config (command =O0OO0OO000OO0O000 .yview )#line:1522
    O0OO0OO000OO0O000 .config (yscrollcommand =O000O0OO00OOOO000 .set )#line:1523
    O0OO0OO000OO0O000 .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1528
    O0OO0OO000OO0O000 .config (state =DISABLED )#line:1529
def Tread_TOOLS_CLEAN (O0O00O0O0O00OO0OO ):#line:1533
        ""#line:1534
        O0O00O0O0O00OO0OO ["报告编码"]=O0O00O0O0O00OO0OO ["报告编码"].astype ("str")#line:1536
        O0O00O0O0O00OO0OO ["产品批号"]=O0O00O0O0O00OO0OO ["产品批号"].astype ("str")#line:1538
        O0O00O0O0O00OO0OO ["型号"]=O0O00O0O0O00OO0OO ["型号"].astype ("str")#line:1539
        O0O00O0O0O00OO0OO ["规格"]=O0O00O0O0O00OO0OO ["规格"].astype ("str")#line:1540
        O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"]=O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"].str .replace ("(","（",regex =False )#line:1542
        O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"]=O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"].str .replace (")","）",regex =False )#line:1543
        O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"]=O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"].str .replace ("*","※",regex =False )#line:1544
        O0O00O0O0O00OO0OO ["产品名称"]=O0O00O0O0O00OO0OO ["产品名称"].str .replace ("*","※",regex =False )#line:1546
        O0O00O0O0O00OO0OO ["产品批号"]=O0O00O0O0O00OO0OO ["产品批号"].str .replace ("(","（",regex =False )#line:1548
        O0O00O0O0O00OO0OO ["产品批号"]=O0O00O0O0O00OO0OO ["产品批号"].str .replace (")","）",regex =False )#line:1549
        O0O00O0O0O00OO0OO ["产品批号"]=O0O00O0O0O00OO0OO ["产品批号"].str .replace ("*","※",regex =False )#line:1550
        O0O00O0O0O00OO0OO ['事件发生日期']=pd .to_datetime (O0O00O0O0O00OO0OO ['事件发生日期'],format ='%Y-%m-%d',errors ='coerce')#line:1553
        O0O00O0O0O00OO0OO ["事件发生月份"]=O0O00O0O0O00OO0OO ["事件发生日期"].dt .to_period ("M").astype (str )#line:1557
        O0O00O0O0O00OO0OO ["事件发生季度"]=O0O00O0O0O00OO0OO ["事件发生日期"].dt .to_period ("Q").astype (str )#line:1558
        O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"]=O0O00O0O0O00OO0OO ["注册证编号/曾用注册证编号"].fillna ("未填写")#line:1562
        O0O00O0O0O00OO0OO ["产品批号"]=O0O00O0O0O00OO0OO ["产品批号"].fillna ("未填写")#line:1563
        O0O00O0O0O00OO0OO ["型号"]=O0O00O0O0O00OO0OO ["型号"].fillna ("未填写")#line:1564
        O0O00O0O0O00OO0OO ["规格"]=O0O00O0O0O00OO0OO ["规格"].fillna ("未填写")#line:1565
        return O0O00O0O0O00OO0OO #line:1567
def thread_it (O00O000OOO000000O ,*O0OOO0OOO0O0OOO00 ):#line:1571
    ""#line:1572
    OOO0O0O0O00000O0O =threading .Thread (target =O00O000OOO000000O ,args =O0OOO0OOO0O0OOO00 )#line:1574
    OOO0O0O0O00000O0O .setDaemon (True )#line:1576
    OOO0O0O0O00000O0O .start ()#line:1578
def showWelcome ():#line:1581
    ""#line:1582
    OO00OOOO00OOOOO00 =roox .winfo_screenwidth ()#line:1583
    O000OO0000O0O00OO =roox .winfo_screenheight ()#line:1585
    roox .overrideredirect (True )#line:1587
    roox .attributes ("-alpha",1 )#line:1588
    OOOOOOOOO0O00O0OO =(OO00OOOO00OOOOO00 -475 )/2 #line:1589
    O000OOO00OO0OO000 =(O000OO0000O0O00OO -200 )/2 #line:1590
    roox .geometry ("675x140+%d+%d"%(OOOOOOOOO0O00O0OO ,O000OOO00OO0OO000 ))#line:1592
    roox ["bg"]="royalblue"#line:1593
    O0OOOOOO000OO000O =Label (roox ,text ="医疗器械警戒趋势分析工具",fg ="white",bg ="royalblue",font =("微软雅黑",20 ))#line:1596
    O0OOOOOO000OO000O .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1597
    OO000OOO0O0O0OO00 =Label (roox ,text ="Trend Analysis Tools V"+str (version_now ),fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1604
    OO000OOO0O0O0OO00 .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1605
def closeWelcome ():#line:1608
    ""#line:1609
    for O0OO00O0000O0O00O in range (2 ):#line:1610
        root .attributes ("-alpha",0 )#line:1611
        time .sleep (1 )#line:1612
    root .attributes ("-alpha",1 )#line:1613
    roox .destroy ()#line:1614
if __name__ =='__main__':#line:1618
    pass #line:1619
root =Tk ()#line:1620
root .title ("医疗器械警戒趋势分析工具Trend Analysis Tools V"+str (version_now ))#line:1621
sw_root =root .winfo_screenwidth ()#line:1622
sh_root =root .winfo_screenheight ()#line:1624
ww_root =700 #line:1626
wh_root =620 #line:1627
x_root =(sw_root -ww_root )/2 #line:1629
y_root =(sh_root -wh_root )/2 #line:1630
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1631
root .configure (bg ="steelblue")#line:1632
try :#line:1635
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1636
    frame0 .pack (side =LEFT )#line:1637
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,0 ),)#line:1650
    B_open_files1 .pack ()#line:1651
    B_open_files3 =Button (frame0 ,text ="导入分析规则",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_fileopen ,1 ),)#line:1664
    B_open_files3 .pack ()#line:1665
    B_open_files3 =Button (frame0 ,text ="趋势统计分析",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_analysis ,0 ),)#line:1680
    B_open_files3 .pack ()#line:1681
    B_open_files3 =Button (frame0 ,text ="直方图（数量）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"数量"))#line:1694
    B_open_files3 .pack ()#line:1695
    B_open_files3 =Button (frame0 ,text ="直方图（占比）",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tread_TOOLS_bar ,"百分比"))#line:1706
    B_open_files3 .pack ()#line:1707
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ))#line:1718
    B_open_files3 .pack ()#line:1719
    B_open_files3 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1730
    B_open_files3 .pack ()#line:1731
except :#line:1732
    pass #line:1733
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1737
text .pack ()#line:1738
text .insert (END ,"\n  本程序用于趋势分析,供广东省内参与医疗器械警戒试点的企业免费使用。如您有相关问题或改进建议，请联系以下人员：\n\n    佛山市药品不良反应监测中心\n    蔡权周 \n    微信：18575757461 \n    邮箱：411703730@qq.com")#line:1743
text .insert (END ,"\n\n")#line:1744
def A000 ():#line:1746
    pass #line:1747
setting_cfg =read_setting_cfg ()#line:1751
generate_random_file ()#line:1752
setting_cfg =open_setting_cfg ()#line:1753
if setting_cfg ["settingdir"]==0 :#line:1754
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1755
    filepathu =filedialog .askdirectory ()#line:1756
    path =get_directory_path (filepathu )#line:1757
    update_setting_cfg ("settingdir",path )#line:1758
setting_cfg =open_setting_cfg ()#line:1759
random_number =int (setting_cfg ["sidori"])#line:1760
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1761
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1762
sid =random_number *2 +183576 #line:1763
if input_number ==sid and day_end =="未过期":#line:1764
    usergroup ="用户组=1"#line:1765
    text .insert (END ,usergroup +"   有效期至：")#line:1766
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1767
else :#line:1768
    text .insert (END ,usergroup )#line:1769
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1770
aaass =update_software ("treadtools")#line:1771
text .insert (END ,aaass )#line:1772
roox =Toplevel ()#line:1775
tMain =threading .Thread (target =showWelcome )#line:1776
tMain .start ()#line:1777
t1 =threading .Thread (target =closeWelcome )#line:1778
t1 .start ()#line:1779
root .lift ()#line:1783
root .attributes ("-topmost",True )#line:1784
root .attributes ("-topmost",False )#line:1785
root .mainloop ()#line:1786
