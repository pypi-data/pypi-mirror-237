#!/usr/bin/env python
# coding: utf-8
import warnings #line:10
import traceback #line:11
import re #line:12
import xlrd #line:13
import xlwt #line:14
import openpyxl #line:15
import pandas as pd #line:16
import numpy as np #line:17
import math #line:18
import tkinter as Tk #line:19
from tkinter import ttk #line:20
from tkinter import *#line:21
import tkinter .font as tkFont #line:22
from tkinter import filedialog ,dialog ,PhotoImage #line:23
from tkinter .messagebox import showinfo #line:24
from tkinter .scrolledtext import ScrolledText #line:25
import collections #line:26
from collections import Counter #line:27
import datetime #line:28
from datetime import datetime ,timedelta #line:29
from tkinter import END #line:30
import xlsxwriter #line:31
import os #line:32
import time #line:33
import threading #line:34
import matplotlib as plt #line:35
from matplotlib .backends .backend_tkagg import FigureCanvasTkAgg #line:36
from matplotlib .figure import Figure #line:37
from matplotlib .backends .backend_tkagg import NavigationToolbar2Tk #line:38
global ori #line:41
global biaozhun #line:42
global dishi #line:43
biaozhun =""#line:44
dishi =""#line:45
ori =0 #line:46
global modex #line:47
modex =""#line:48
import random #line:50
import requests #line:51
global version_now #line:52
global usergroup #line:53
global setting_cfg #line:54
global csdir #line:55
global peizhidir #line:56
version_now ="0.0.4"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
try :#line:60
    csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:61
    csdir =csdir +csdir .split ("pinggutools")[0 ][-1 ]#line:62
except :#line:63
    csdir =str (os .path .dirname (__file__ ))#line:64
    csdir =csdir +csdir .split ("treadtools")[0 ][-1 ]#line:65
def extract_zip_file (OO0O0O000O0O00OO0 ,O00O00O0OOOOO0OO0 ):#line:73
    import zipfile #line:75
    if O00O00O0OOOOO0OO0 =="":#line:76
        return 0 #line:77
    with zipfile .ZipFile (OO0O0O000O0O00OO0 ,'r')as OOO0O0O0OO0OOOOOO :#line:78
        for O0O0O0OO000OO0O0O in OOO0O0O0OO0OOOOOO .infolist ():#line:79
            O0O0O0OO000OO0O0O .filename =O0O0O0OO000OO0O0O .filename .encode ('cp437').decode ('gbk')#line:81
            OOO0O0O0OO0OOOOOO .extract (O0O0O0OO000OO0O0O ,O00O00O0OOOOO0OO0 )#line:82
def get_directory_path (O00OO000OOO0OO000 ):#line:88
    global csdir #line:90
    if not (os .path .isfile (os .path .join (O00OO000OOO0OO000 ,'0（范例）质量评估.xls'))):#line:92
        extract_zip_file (csdir +"def.py",O00OO000OOO0OO000 )#line:97
    if O00OO000OOO0OO000 =="":#line:99
        quit ()#line:100
    return O00OO000OOO0OO000 #line:101
def convert_and_compare_dates (O0O0000O000000O00 ):#line:105
    import datetime #line:106
    O00O0OO0O0O000000 =datetime .datetime .now ()#line:107
    try :#line:109
       O0O0O0000OO00O00O =datetime .datetime .strptime (str (int (int (O0O0000O000000O00 )/4 )),"%Y%m%d")#line:110
    except :#line:111
        print ("fail")#line:112
        return "已过期"#line:113
    if O0O0O0000OO00O00O >O00O0OO0O0O000000 :#line:115
        return "未过期"#line:117
    else :#line:118
        return "已过期"#line:119
def read_setting_cfg ():#line:121
    global csdir #line:122
    if os .path .exists (csdir +'setting.cfg'):#line:124
        text .insert (END ,"已完成初始化\n")#line:125
        with open (csdir +'setting.cfg','r')as OO0O00OOO00OO0OOO :#line:126
            O0000OO00OOOOOOOO =eval (OO0O00OOO00OO0OOO .read ())#line:127
    else :#line:128
        O0OO000O0O00O000O =csdir +'setting.cfg'#line:130
        with open (O0OO000O0O00O000O ,'w')as OO0O00OOO00OO0OOO :#line:131
            OO0O00OOO00OO0OOO .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:132
        text .insert (END ,"未初始化，正在初始化...\n")#line:133
        O0000OO00OOOOOOOO =read_setting_cfg ()#line:134
    return O0000OO00OOOOOOOO #line:135
def open_setting_cfg ():#line:138
    global csdir #line:139
    with open (csdir +"setting.cfg","r")as OO0OOO00OO00O0O00 :#line:141
        O0OOO00000O0O0O0O =eval (OO0OOO00OO00O0O00 .read ())#line:143
    return O0OOO00000O0O0O0O #line:144
def update_setting_cfg (OO0OOOOO000000OOO ,O000O0OOOOO00O000 ):#line:146
    global csdir #line:147
    with open (csdir +"setting.cfg","r")as O0OOO0000OOO0000O :#line:149
        OO0OO00OOO0000OO0 =eval (O0OOO0000OOO0000O .read ())#line:151
    if OO0OO00OOO0000OO0 [OO0OOOOO000000OOO ]==0 or OO0OO00OOO0000OO0 [OO0OOOOO000000OOO ]=="11111180000808":#line:153
        OO0OO00OOO0000OO0 [OO0OOOOO000000OOO ]=O000O0OOOOO00O000 #line:154
        with open (csdir +"setting.cfg","w")as O0OOO0000OOO0000O :#line:156
            O0OOO0000OOO0000O .write (str (OO0OO00OOO0000OO0 ))#line:157
def generate_random_file ():#line:160
    OOOO0OO0O0OO0O00O =random .randint (200000 ,299999 )#line:162
    update_setting_cfg ("sidori",OOOO0OO0O0OO0O00O )#line:164
def display_random_number ():#line:166
    global csdir #line:167
    OOO0O00O0OO0O0OOO =Toplevel ()#line:168
    OOO0O00O0OO0O0OOO .title ("ID")#line:169
    OO0O000OOOOOOOO00 =OOO0O00O0OO0O0OOO .winfo_screenwidth ()#line:171
    O0OOO000O0OOOO0OO =OOO0O00O0OO0O0OOO .winfo_screenheight ()#line:172
    O0000O00O0000000O =80 #line:174
    O0OOO0OOO000O00O0 =70 #line:175
    OOOO0O0O0OOOO00OO =(OO0O000OOOOOOOO00 -O0000O00O0000000O )/2 #line:177
    OO00OOOOOOO0000OO =(O0OOO000O0OOOO0OO -O0OOO0OOO000O00O0 )/2 #line:178
    OOO0O00O0OO0O0OOO .geometry ("%dx%d+%d+%d"%(O0000O00O0000000O ,O0OOO0OOO000O00O0 ,OOOO0O0O0OOOO00OO ,OO00OOOOOOO0000OO ))#line:179
    with open (csdir +"setting.cfg","r")as O00O000OOO0O0O0O0 :#line:182
        O0OO0OO000O00OO0O =eval (O00O000OOO0O0O0O0 .read ())#line:184
    O0OOOO00O00OO0OO0 =int (O0OO0OO000O00OO0O ["sidori"])#line:185
    OO0OOOOOOOO0OO0OO =O0OOOO00O00OO0OO0 *2 +183576 #line:186
    print (OO0OOOOOOOO0OO0OO )#line:188
    O0O00O00O00O0000O =ttk .Label (OOO0O00O0OO0O0OOO ,text =f"机器码: {O0OOOO00O00OO0OO0}")#line:190
    OO0OOO0O0OOO000OO =ttk .Entry (OOO0O00O0OO0O0OOO )#line:191
    O0O00O00O00O0000O .pack ()#line:194
    OO0OOO0O0OOO000OO .pack ()#line:195
    ttk .Button (OOO0O00O0OO0O0OOO ,text ="验证",command =lambda :check_input (OO0OOO0O0OOO000OO .get (),OO0OOOOOOOO0OO0OO )).pack ()#line:199
def check_input (OO000OOOOO0OOOO0O ,OOO0O00OO00OOOOOO ):#line:201
    try :#line:205
        OOOO0O00OOOOO000O =int (str (OO000OOOOO0OOOO0O )[0 :6 ])#line:206
        O00O0OO00O00O0O0O =convert_and_compare_dates (str (OO000OOOOO0OOOO0O )[6 :14 ])#line:207
    except :#line:208
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:209
        return 0 #line:210
    if OOOO0O00OOOOO000O ==OOO0O00OO00OOOOOO and O00O0OO00O00O0O0O =="未过期":#line:212
        update_setting_cfg ("sidfinal",OO000OOOOO0OOOO0O )#line:213
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:214
        quit ()#line:215
    else :#line:216
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:217
def update_software (O0O00OOOOOOOOOO00 ):#line:222
    global version_now #line:224
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:225
    try :#line:226
        OO000O0OOOO0O0O00 =requests .get (f"https://pypi.org/pypi/{O0O00OOOOOOOOOO00}/json",timeout =2 ).json ()["info"]["version"]#line:227
    except :#line:228
        return "...更新失败。"#line:229
    if OO000O0OOOO0O0O00 >version_now :#line:230
        text .insert (END ,"\n最新版本为："+OO000O0OOOO0O0O00 +",正在尝试自动更新....")#line:231
        pip .main (['install',O0O00OOOOOOOOOO00 ,'--upgrade'])#line:233
        text .insert (END ,"\n您可以开展工作。")#line:234
        return "...更新成功。"#line:235
def Topentable (OO0OO0O00OO0O0000 ):#line:238
    ""#line:239
    global ori #line:240
    global biaozhun #line:241
    global dishi #line:242
    OO00OO0000OO0O000 =[]#line:243
    OOOO0OOOOO000O0OO =[]#line:244
    OOO0OO00O000OO0OO =1 #line:245
    if OO0OO0O00OO0O0000 ==123 :#line:248
        try :#line:249
            O000000OO0OOOOOOO =filedialog .askopenfilename (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:252
            biaozhun =pd .read_excel (O000000OO0OOOOOOO ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:255
        except :#line:256
            showinfo (title ="提示",message ="配置表文件有误或您没有选择。")#line:257
            return 0 #line:258
        try :#line:259
            dishi =pd .read_excel (O000000OO0OOOOOOO ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:262
        except :#line:263
            showinfo (title ="提示",message ="您选择的配置文件没有地市列表或您没有选择。")#line:264
            return 0 #line:265
        if ("评分项"in biaozhun .columns and "打分标准"in biaozhun .columns and "专家序号"not in biaozhun .columns ):#line:270
            text .insert (END ,"\n您使用自定义的配置表。")#line:271
            text .see (END )#line:272
            showinfo (title ="提示",message ="您将使用自定义的配置表。")#line:273
            return 0 #line:274
        else :#line:275
            showinfo (title ="提示",message ="配置表文件有误，请正确选择。")#line:276
            biaozhun =""#line:277
            return 0 #line:278
    try :#line:281
        if OO0OO0O00OO0O0000 !=1 :#line:282
            O0OO0OOOOOO0OOO0O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:285
        if OO0OO0O00OO0O0000 ==1 :#line:286
            O0OO0OOOOOO0OOO0O =filedialog .askopenfilenames (filetypes =[("XLSX",".xlsx"),("XLS",".xls")])#line:289
            for OOO0OO0O00OOOOO00 in O0OO0OOOOOO0OOO0O :#line:290
                if ("●专家评分表"in OOO0OO0O00OOOOO00 )and ("●(最终评分需导入)被抽出的所有数据.xls"not in OOO0OO0O00OOOOO00 ):#line:291
                    OO00OO0000OO0O000 .append (OOO0OO0O00OOOOO00 )#line:292
                elif "●(最终评分需导入)被抽出的所有数据.xls"in OOO0OO0O00OOOOO00 :#line:293
                    OOOO0OOOOO000O0OO .append (OOO0OO0O00OOOOO00 )#line:294
                    O000O0OOO0O000OOO =OOO0OO0O00OOOOO00 .replace ("●(最终评分需导入)被抽出的所有数据","分数错误信息")#line:295
                    OOO0OO00O000OO0OO =0 #line:296
            if OOO0OO00O000OO0OO ==1 :#line:297
                showinfo (title ="提示",message ="请一并导入以下文件：●(最终评分需导入)被抽出的所有数据.xls")#line:299
                return 0 #line:300
            O0OO0OOOOOO0OOO0O =OO00OO0000OO0O000 #line:301
        O00000000OO0OO00O =[pd .read_excel (OO00O000O0OO0O000 ,header =0 ,sheet_name =0 )for OO00O000O0OO0O000 in O0OO0OOOOOO0OOO0O ]#line:304
        ori =pd .concat (O00000000OO0OO00O ,ignore_index =True ).drop_duplicates ().reset_index (drop =True )#line:305
        if "报告编码"in ori .columns or "报告表编码"in ori .columns :#line:307
            ori =ori .fillna ("-未填写-")#line:308
        if "报告类型-新的"in ori .columns :#line:311
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:314
            ori ["报告编码"]=ori ["报告表编码"]#line:315
            text .insert (END ,"检测到导入的文件为药品报告，正在进行兼容性数据规整，请稍后...")#line:316
            ori =ori .rename (columns ={"医院名称":"单位名称"})#line:317
            ori =ori .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:318
            ori =ori .rename (columns ={"报告类型-严重程度":"伤害"})#line:319
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:320
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:321
            ori .loc [(ori ["不良反应结果"]=="死亡"),"伤害"]="死亡"#line:322
            ori ["上报单位所属地区"]=ori ["使用单位、经营企业所属监测机构"]#line:323
            try :#line:324
                ori ["报告编码"]=ori ["唯一标识"]#line:325
            except :#line:326
                pass #line:327
            ori ["药品信息"]=""#line:331
            OOOOO00000OO000O0 =0 #line:332
            O0O0OO00OOOOOOOO0 =len (ori ["报告编码"].drop_duplicates ())#line:333
            for OOOO0O00000O0O00O in ori ["报告编码"].drop_duplicates ():#line:334
                OOOOO00000OO000O0 =OOOOO00000OO000O0 +1 #line:335
                OOO0O0000OO00O0OO =round (OOOOO00000OO000O0 /O0O0OO00OOOOOOOO0 ,2 )#line:336
                try :#line:337
                    change_schedule (OOOOO00000OO000O0 ,O0O0OO00OOOOOOOO0 )#line:338
                except :#line:339
                    if OOO0O0000OO00O0OO in [0.10 ,0.20 ,0.30 ,0.40 ,0.50 ,0.60 ,0.70 ,0.80 ,0.90 ,0.99 ]:#line:340
                        text .insert (END ,OOO0O0000OO00O0OO )#line:341
                        text .insert (END ,"...")#line:342
                O0O00O0O00O00OO0O =ori [(ori ["报告编码"]==OOOO0O00000O0O00O )].sort_values (by =["药品序号"]).reset_index ()#line:344
                for O0000OOO0OOOOOOOO ,O00O0O0OOO0O000OO in O0O00O0O00O00OO0O .iterrows ():#line:345
                    ori .loc [(ori ["报告编码"]==O00O0O0OOO0O000OO ["报告编码"]),"药品信息"]=ori ["药品信息"]+"●药品序号："+str (O00O0O0OOO0O000OO ["药品序号"])+" 性质："+str (O00O0O0OOO0O000OO ["怀疑/并用"])+"\n批准文号:"+str (O00O0O0OOO0O000OO ["批准文号"])+"\n商品名称："+str (O00O0O0OOO0O000OO ["商品名称"])+"\n通用名称："+str (O00O0O0OOO0O000OO ["通用名称"])+"\n剂型："+str (O00O0O0OOO0O000OO ["剂型"])+"\n生产厂家："+str (O00O0O0OOO0O000OO ["生产厂家"])+"\n生产批号："+str (O00O0O0OOO0O000OO ["生产批号"])+"\n用量："+str (O00O0O0OOO0O000OO ["用量"])+str (O00O0O0OOO0O000OO ["用量单位"])+"，"+str (O00O0O0OOO0O000OO ["用法-日"])+"日"+str (O00O0O0OOO0O000OO ["用法-次"])+"次\n给药途径:"+str (O00O0O0OOO0O000OO ["给药途径"])+"\n用药开始时间："+str (O00O0O0OOO0O000OO ["用药开始时间"])+"\n用药终止时间："+str (O00O0O0OOO0O000OO ["用药终止时间"])+"\n用药原因："+str (O00O0O0OOO0O000OO ["用药原因"])+"\n"#line:346
            ori =ori .drop_duplicates ("报告编码")#line:347
        if "皮损部位"in ori .columns :#line:354
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:357
            ori ["报告编码"]=ori ["报告表编号"]#line:358
            text .insert (END ,"检测到导入的文件为化妆品报告，正在进行兼容性数据规整，请稍后...")#line:359
            ori ["报告地区名称"]=ori ["报告单位名称"].astype (str )#line:361
            ori ["单位名称"]=ori ["报告单位名称"].astype (str )#line:363
            ori ["伤害"]=ori ["报告类型"].astype (str )#line:364
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:365
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:366
            ori ["上报单位所属地区"]=ori ["报告地区名称"]#line:368
            try :#line:369
                ori ["报告编码"]=ori ["唯一标识"]#line:370
            except :#line:371
                pass #line:372
            text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:373
            OO0OOO000OOO0O000 =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:374
            for O0000OOO0OOOOOOOO ,O00O0O0OOO0O000OO in OO0OOO000OOO0O000 .iterrows ():#line:376
                ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["中文全称"]),"监测机构"]=O00O0O0OOO0O000OO ["归属地区"]#line:377
                ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["中文全称"]),"市级监测机构"]=O00O0O0OOO0O000OO ["地市"]#line:378
            ori ["监测机构"]=ori ["监测机构"].fillna ("未规整")#line:379
            ori ["市级监测机构"]=ori ["市级监测机构"].fillna ("未规整")#line:380
        try :#line:383
                text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:384
                O00000O00OO0O0O00 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:385
                OO0OOO000OOO0O000 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:386
                O0O000OO0OOO0OOOO =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:387
                for O0000OOO0OOOOOOOO ,O00O0O0OOO0O000OO in O00000O00OO0O0O00 .iterrows ():#line:388
                        ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["曾用名1"]),"单位名称"]=O00O0O0OOO0O000OO ["单位名称"]#line:389
                        ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["曾用名2"]),"单位名称"]=O00O0O0OOO0O000OO ["单位名称"]#line:390
                        ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["曾用名3"]),"单位名称"]=O00O0O0OOO0O000OO ["单位名称"]#line:391
                        ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["曾用名4"]),"单位名称"]=O00O0O0OOO0O000OO ["单位名称"]#line:392
                        ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["曾用名5"]),"单位名称"]=O00O0O0OOO0O000OO ["单位名称"]#line:393
                        ori .loc [(ori ["单位名称"]==O00O0O0OOO0O000OO ["单位名称"]),"使用单位、经营企业所属监测机构"]=O00O0O0OOO0O000OO ["监测机构"]#line:396
                for O0000OOO0OOOOOOOO ,O00O0O0OOO0O000OO in OO0OOO000OOO0O000 .iterrows ():#line:398
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==O00O0O0OOO0O000OO ["曾用名1"]),"使用单位、经营企业所属监测机构"]=O00O0O0OOO0O000OO ["监测机构"]#line:399
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==O00O0O0OOO0O000OO ["曾用名2"]),"使用单位、经营企业所属监测机构"]=O00O0O0OOO0O000OO ["监测机构"]#line:400
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==O00O0O0OOO0O000OO ["曾用名3"]),"使用单位、经营企业所属监测机构"]=O00O0O0OOO0O000OO ["监测机构"]#line:401
                for OO00OO0O0O0O0O00O in O0O000OO0OOO0OOOO ["地市列表"]:#line:403
                        ori .loc [(ori ["上报单位所属地区"].str .contains (OO00OO0O0O0O0O00O ,na =False )),"市级监测机构"]=OO00OO0O0O0O0O00O #line:404
                ori .loc [(ori ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:405
        except :#line:407
                text .insert (END ,"\n报告单位和监测机构名称规整失败.")#line:408
    except :#line:410
        showinfo (title ="提示",message ="导入文件错误,请重试。")#line:411
        return 0 #line:412
    try :#line:415
        ori =ori .loc [:,~ori .columns .str .contains ("Unnamed")]#line:416
    except :#line:417
        pass #line:418
    try :#line:419
        ori ["报告编码"]=ori ["报告编码"].astype (str )#line:420
    except :#line:421
        pass #line:422
    ori =ori .sample (frac =1 ).copy ()#line:425
    ori .reset_index (inplace =True )#line:426
    text .insert (END ,"\n数据读取成功，行数："+str (len (ori )))#line:427
    text .see (END )#line:428
    if OO0OO0O00OO0O0000 ==0 :#line:431
        if "报告编码"not in ori .columns :#line:432
            showinfo (title ="提示信息",message ="\n在校验过程中，发现您导入的并非原始报告数据，请重新导入。")#line:433
        else :#line:434
            showinfo (title ="提示信息",message ="\n数据读取成功。")#line:435
        return 0 #line:436
    O00OOOO00O0O00OOO =ori .copy ()#line:439
    OO000O00O00000OO0 ={}#line:440
    O0OOOO0OOOOO0OO00 =0 #line:441
    if "专家序号"not in O00OOOO00O0O00OOO .columns :#line:442
        showinfo (title ="提示信息",message ="您导入的并非专家评分文件，请重新导入。")#line:443
        return 0 #line:444
    for O0000OOO0OOOOOOOO ,O00O0O0OOO0O000OO in O00OOOO00O0O00OOO .iterrows ():#line:445
        OO0OOOOOOO00O00O0 ="专家打分-"+str (O00O0O0OOO0O000OO ["条目"])#line:446
        try :#line:447
            float (O00O0O0OOO0O000OO ["评分"])#line:448
            float (O00O0O0OOO0O000OO ["满分"])#line:449
        except :#line:450
            showinfo (title ="错误提示",message ="因专家评分或满分值输入的不是数字，导致了程序中止，请修正："+"专家序号："+str (int (O00O0O0OOO0O000OO ["专家序号"]))+"，报告序号："+str (int (O00O0O0OOO0O000OO ["序号"]))+O00O0O0OOO0O000OO ["条目"],)#line:459
            ori =0 #line:460
        if float (O00O0O0OOO0O000OO ["评分"])>float (O00O0O0OOO0O000OO ["满分"])or float (O00O0O0OOO0O000OO ["评分"])<0 :#line:461
            OO000O00O00000OO0 [str (O0000OOO0OOOOOOOO )]=("专家序号："+str (int (O00O0O0OOO0O000OO ["专家序号"]))+"；  报告序号："+str (int (O00O0O0OOO0O000OO ["序号"]))+O00O0O0OOO0O000OO ["条目"])#line:468
            O0OOOO0OOOOO0OO00 =1 #line:469
    if O0OOOO0OOOOO0OO00 ==1 :#line:471
        O00OO00O0O000OO0O =pd .DataFrame (list (OO000O00O00000OO0 .items ()),columns =["错误编号","错误信息"])#line:472
        del O00OO00O0O000OO0O ["错误编号"]#line:473
        OO0O0000O0000O000 =O000O0OOO0O000OOO #line:474
        O00OO00O0O000OO0O =O00OO00O0O000OO0O .sort_values (by =["错误信息"],ascending =True ,na_position ="last")#line:475
        O00OO0OOOOO000OO0 =pd .ExcelWriter (OO0O0000O0000O000 )#line:476
        O00OO00O0O000OO0O .to_excel (O00OO0OOOOO000OO0 ,sheet_name ="字典数据")#line:477
        O00OO0OOOOO000OO0 .close ()#line:478
        showinfo (title ="警告",message ="经检查，部分专家的打分存在错误。请您修正错误的打分文件再重新导入全部的专家打分文件。详见:分数错误信息.xls",)#line:482
        text .insert (END ,"\n经检查，部分专家的打分存在错误。详见:分数错误信息.xls。请您修正错误的打分文件再重新导入全部的专家打分文件。")#line:483
        text .insert (END ,"\n以下是错误信息概况：\n")#line:484
        text .insert (END ,O00OO00O0O000OO0O )#line:485
        text .see (END )#line:486
        return 0 #line:487
    if OO0OO0O00OO0O0000 ==1 :#line:490
        return ori ,OOOO0OOOOO000O0OO #line:491
def Tchouyang (O0OO000OO000O00OO ):#line:494
    ""#line:495
    try :#line:497
        if O0OO000OO000O00OO ==0 :#line:498
            showinfo (title ="提示",message ="您尚未导入原始数据。")#line:499
            return 0 #line:500
    except :#line:501
        pass #line:502
    if "详细描述"in O0OO000OO000O00OO .columns :#line:503
        showinfo (title ="提示",message ="目前工作文件为专家评分文件，请导入原始数据进行抽样。")#line:504
        return 0 #line:505
    O00OO0OO0OOOOO000 =Toplevel ()#line:508
    O00OO0OO0OOOOO000 .title ("随机抽样及随机分组")#line:509
    OOOO000O0O00OO0O0 =O00OO0OO0OOOOO000 .winfo_screenwidth ()#line:510
    O0O0O0OO000O0000O =O00OO0OO0OOOOO000 .winfo_screenheight ()#line:512
    OOO0O000O000OO0O0 =300 #line:514
    O0000OO0O0O0000O0 =220 #line:515
    OOO0O000OOOO0OO00 =(OOOO000O0O00OO0O0 -OOO0O000O000OO0O0 )/1.7 #line:517
    OOO0OO0OO0O00O00O =(O0O0O0OO000O0000O -O0000OO0O0O0000O0 )/2 #line:518
    O00OO0OO0OOOOO000 .geometry ("%dx%d+%d+%d"%(OOO0O000O000OO0O0 ,O0000OO0O0O0000O0 ,OOO0O000OOOO0OO00 ,OOO0OO0OO0O00O00O ))#line:519
    O0O0O0O0OOOOO000O =Label (O00OO0OO0OOOOO000 ,text ="评估对象：")#line:521
    O0O0O0O0OOOOO000O .grid (row =1 ,column =0 ,sticky ="w")#line:522
    OO0O00O00OOOOO000 =StringVar ()#line:523
    O00OOOOOOOO0000O0 =ttk .Combobox (O00OO0OO0OOOOO000 ,width =25 ,height =10 ,state ="readonly",textvariable =OO0O00O00OOOOO000 )#line:526
    O00OOOOOOOO0000O0 ["values"]=["上报单位","县区","地市","省级审核人","上市许可持有人"]#line:527
    O00OOOOOOOO0000O0 .current (0 )#line:528
    O00OOOOOOOO0000O0 .grid (row =2 ,column =0 )#line:529
    O0OOOOOO00O0OO000 =Label (O00OO0OO0OOOOO000 ,text ="-----------------------------------------")#line:531
    O0OOOOOO00O0OO000 .grid (row =3 ,column =0 ,sticky ="w")#line:532
    OOOOOO000OOOOOO0O =Label (O00OO0OO0OOOOO000 ,text ="死亡报告抽样数量（>1)或比例(<=1)：")#line:534
    OOOOOO000OOOOOO0O .grid (row =4 ,column =0 ,sticky ="w")#line:535
    O0OO00O00000O0OOO =Entry (O00OO0OO0OOOOO000 ,width =10 )#line:536
    O0OO00O00000O0OOO .grid (row =4 ,column =1 ,sticky ="w")#line:537
    OO00OOOO00OO0O000 =Label (O00OO0OO0OOOOO000 ,text ="严重报告抽样数量（>1)或比例(<=1)：")#line:539
    OO00OOOO00OO0O000 .grid (row =6 ,column =0 ,sticky ="w")#line:540
    O0OO00OO0OOO000OO =Entry (O00OO0OO0OOOOO000 ,width =10 )#line:541
    O0OO00OO0OOO000OO .grid (row =6 ,column =1 ,sticky ="w")#line:542
    OO0O0000O0OO0O00O =Label (O00OO0OO0OOOOO000 ,text ="一般报告抽样数量（>1)或比例(<=1)：")#line:544
    OO0O0000O0OO0O00O .grid (row =8 ,column =0 ,sticky ="w")#line:545
    O000OOO0O00OO0O0O =Entry (O00OO0OO0OOOOO000 ,width =10 )#line:546
    O000OOO0O00OO0O0O .grid (row =8 ,column =1 ,sticky ="w")#line:547
    O0OOOOOO00O0OO000 =Label (O00OO0OO0OOOOO000 ,text ="-----------------------------------------")#line:549
    O0OOOOOO00O0OO000 .grid (row =9 ,column =0 ,sticky ="w")#line:550
    O0O0O0OOO00OO000O =Label (O00OO0OO0OOOOO000 ,text ="抽样后随机分组数（专家数量）：")#line:552
    O000O00OO0OOO0OOO =Entry (O00OO0OO0OOOOO000 ,width =10 )#line:553
    O0O0O0OOO00OO000O .grid (row =10 ,column =0 ,sticky ="w")#line:554
    O000O00OO0OOO0OOO .grid (row =10 ,column =1 ,sticky ="w")#line:555
    OO00O0OOO0O0OO000 =Button (O00OO0OO0OOOOO000 ,text ="最大覆盖",width =12 ,command =lambda :thread_it (Tdoing0 ,O0OO000OO000O00OO ,O000OOO0O00OO0O0O .get (),O0OO00OO0OOO000OO .get (),O0OO00O00000O0OOO .get (),O000O00OO0OOO0OOO .get (),O00OOOOOOOO0000O0 .get (),"最大覆盖",1 ,),)#line:572
    OO00O0OOO0O0OO000 .grid (row =13 ,column =1 ,sticky ="w")#line:573
    O00OO0O0OO00OO00O =Button (O00OO0OO0OOOOO000 ,text ="总体随机",width =12 ,command =lambda :thread_it (Tdoing0 ,O0OO000OO000O00OO ,O000OOO0O00OO0O0O .get (),O0OO00OO0OOO000OO .get (),O0OO00O00000O0OOO .get (),O000O00OO0OOO0OOO .get (),O00OOOOOOOO0000O0 .get (),"总体随机",1 ))#line:574
    O00OO0O0OO00OO00O .grid (row =13 ,column =0 ,sticky ='w')#line:575
def Tdoing0 (O0000000OO0O0O0O0 ,O0O0OOOO0O0OOO0O0 ,O0OOOO00O0O0O0000 ,O000O0O0OOOOOO000 ,O00O00OOOOO0OO0O0 ,OOO0OOO0000O0OOOO ,OOO0OO00O0O0O0O0O ,O0O0O00O0OOO00OO0 ):#line:581
    ""#line:582
    global dishi #line:583
    global biaozhun #line:584
    if (O0O0OOOO0O0OOO0O0 ==""or O0OOOO00O0O0O0000 ==""or O000O0O0OOOOOO000 ==""or O00O00OOOOO0OO0O0 ==""or OOO0OOO0000O0OOOO ==""or OOO0OO00O0O0O0O0O ==""):#line:594
        showinfo (title ="提示信息",message ="参数设置不完整。")#line:595
        return 0 #line:596
    if OOO0OOO0000O0OOOO =="上报单位":#line:597
        OOO0OOO0000O0OOOO ="单位名称"#line:598
    if OOO0OOO0000O0OOOO =="县区":#line:599
        OOO0OOO0000O0OOOO ="使用单位、经营企业所属监测机构"#line:600
    if OOO0OOO0000O0OOOO =="地市":#line:601
        OOO0OOO0000O0OOOO ="市级监测机构"#line:602
    if OOO0OOO0000O0OOOO =="省级审核人":#line:603
        OOO0OOO0000O0OOOO ="审核人.1"#line:604
        O0000000OO0O0O0O0 ["modex"]=1 #line:605
        O0000000OO0O0O0O0 ["审核人.1"]=O0000000OO0O0O0O0 ["审核人.1"].fillna ("未填写")#line:606
    if OOO0OOO0000O0OOOO =="上市许可持有人":#line:607
        OOO0OOO0000O0OOOO ="上市许可持有人名称"#line:608
        O0000000OO0O0O0O0 ["modex"]=1 #line:609
        O0000000OO0O0O0O0 ["上市许可持有人名称"]=O0000000OO0O0O0O0 ["上市许可持有人名称"].fillna ("未填写")#line:610
    if O0O0O00O0OOO00OO0 ==1 :#line:612
        if len (biaozhun )==0 :#line:613
            O0OOOOOO00000OOOO =peizhidir +"0（范例）质量评估.xls"#line:614
            try :#line:615
                if "modex"in O0000000OO0O0O0O0 .columns :#line:616
                    O0O0OO0O00O0O0O00 =pd .read_excel (O0OOOOOO00000OOOO ,sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:617
                else :#line:618
                    O0O0OO0O00O0O0O00 =pd .read_excel (O0OOOOOO00000OOOO ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:619
                text .insert (END ,"\n您使用配置表文件夹中的“0（范例）质量评估.xls“作为评分标准。")#line:620
                text .see (END )#line:621
            except :#line:624
                O0O0OO0O00O0O0O00 =pd .DataFrame ({"评分项":{0 :"识别代码",1 :"报告人",2 :"联系人",3 :"联系电话",4 :"注册证编号/曾用注册证编号",5 :"产品名称",6 :"型号和规格",7 :"产品批号和产品编号",8 :"生产日期",9 :"有效期至",10 :"事件发生日期",11 :"发现或获知日期",12 :"伤害",13 :"伤害表现",14 :"器械故障表现",15 :"年龄和年龄类型",16 :"性别",17 :"预期治疗疾病或作用",18 :"器械使用日期",19 :"使用场所和场所名称",20 :"使用过程",21 :"合并用药/械情况说明",22 :"事件原因分析和事件原因分析描述",23 :"初步处置情况",},"打分标准":{0 :"",1 :"填写人名或XX科室，得1分",2 :"填写报告填报人员姓名或XX科X医生，得1分",3 :"填写报告填报人员移动电话或所在科室固定电话，得1分",4 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得8分",5 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得4分",6 :"规格和型号任填其一，且内容正确，得4分",7 :"产品批号和编号任填其一，且内容正确，,得4分。\n注意：（1）如果该器械使用年限久远，或在院外用械，批号或编号无法查询追溯的，报告表“使用过程”中给予说明的，得4分；（2）出现YZB格式、YY格式、GB格式等产品标准格式，或“XX生产许XX”等许可证号，得0分；（3）出现和注册证号一样的数字，得0分。",8 :"确保“生产日期”和“有效期至”逻辑正确，“有效期至”晚于“生产日期”，且两者时间间隔应为整月或整年，得2分。",9 :"确保生产日期和有效期逻辑正确。\n注意：如果该器械是使用年限久远的（2014年之前生产产品），或在院外用械，生产日期和有效期无法查询追溯的，并在报告表“使用过程”中给予说明的，该项得4分",10 :"指发生医疗器械不良事件的日期，应与使用过程描述一致，如仅知道事件发生年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。填写正确得2分。\n注意：“事件发生日期”早于“器械使用日期”的，得0分。",11 :"指报告单位发现或知悉该不良事件的日期，填写正确得5分。\n注意：“发现或获知日期”早于“事件发生日期”的，或者早于使用日期的，得0分。",12 :"分为“死亡”、“严重伤害”“其他”，判断正确，得8分。",13 :"描述准确且简明，或者勾选的术语贴切的，得6分；描述较为准确且简明，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成器械故障表现的，得0分。\n注意：对于“严重伤害”事件，需写明实际导致的严重伤害，填写不恰当的或填写“无”的，得0分。伤害表现描述与使用过程中关于伤害的描述不一致的，得0分。对于“其他”未对患者造成伤害的，该项可填“无”或未填写，默认得6分。",14 :"描述准确而简明，或者勾选的术语贴切的，得6分；描述较为准确，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成伤害表现的，得0分。故障表现与使用过程中关于器械故障的描述不一致的，得0分。\n注意：对于不存在器械故障但仍然对患者造成了伤害的，在伤害表现处填写了对应伤害，该项填“无”，默认得6分。",15 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",16 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",17 :"指涉及医疗器械的用途或适用范围，如治疗类医疗器械的预期治疗疾病，检验检查类、辅助治疗类医疗器械的预期作用等。填写完整准确，得4分；未填写、填写不完整或填写错误，得0分。",18 :"需与使用过程描述的日期一致，若器械使用日期和不良事件发生日期不是同一天，填成“不良事件发生日期”的，得0分；填成“有源设备启用日期”的，得0分。如仅知道事件使用年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。",19 :"使用场所为“医疗机构”的，场所名称可以为空，默认得2分；使用场所为“家庭”或“其他”，但勾选为医疗机构的，得0分；如使用场所为“其他”，没有填写实际使用场所或填写错误的，得0分。",20 :"按照以下四个要素进行评分：\n（1）具体操作使用情况（5分）\n详细描述具体操作人员资质、操作使用过程等信息，对于体外诊断医疗器械应填写患者诊疗信息（如疾病情况、用药情况）、样品检测过程与结果等信息。该要素描述准确完整的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（2）不良事件情况（5分）\n详细描述使用过程中出现的非预期结果等信息，对于体外诊断医疗器械应填写发现的异常检测情况，该要素描述完整准确的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（3）对受害者的影响（4分）\n详细描述该事件（可能）对患者造成的伤害，（可能）对临床诊疗造成的影响。有实际伤害的事件，需写明对受害者的伤害情况，包括必要的体征（如体温、脉搏、血压、皮损程度、失血情况等）和相关检查结果（如血小板检查结果）；对于可能造成严重伤害的事件，需写明可能对患者或其他人员造成的伤害。该要素描述完整准确的，得4分；较完整准确的，得2分；要素缺失的，得0分。\n（4）采取的治疗措施及结果（4分）\n有实际伤害的情况，须写明对伤者采取的治疗措施（包括用药、用械、或手术治疗等，及采取各个治疗的时间），以及采取治疗措施后的转归情况。该要素描述完整准确得4分，较完整准确得2分，描述过于笼统简单，如描述为“对症治疗”、“报告医生”、“转院”等，或者要素缺失的，得0分；无实际伤害的，该要素默认得4分。",21 :"有合并用药/械情况但没有填写此项的，得0分；填写不完整的，得2分；评估认为该不良事件过程中不存在合并用药/械情况的，该项不填写可得4分。\n如：输液泵泵速不准，合并用药/械情况应写明输注的药液、并用的输液器信息等。",22 :"原因分析不正确，如对于产品原因（包括说明书等）、操作原因 、患者自身原因 、无法确定的勾选与原因分析的描述的内容不匹配的，得0分，例如勾选了产品原因，但描述中说明该事件可能是未按照说明书要求进行操作导致（操作原因）；原因分析正确，但原因分析描述填成使用过程或者处置方式的，得2分。",23 :"包含产品的初步处置措施和对患者的救治措施等，填写完整得2分，部分完整得1分，填写过于简单得0分。",},"满分分值":{0 :0 ,1 :1 ,2 :1 ,3 :1 ,4 :8 ,5 :4 ,6 :4 ,7 :4 ,8 :2 ,9 :2 ,10 :2 ,11 :5 ,12 :8 ,13 :6 ,14 :6 ,15 :1 ,16 :1 ,17 :4 ,18 :2 ,19 :2 ,20 :18 ,21 :4 ,22 :4 ,23 :2 ,},})#line:706
                text .insert (END ,"\n您使用软件内置的评分标准。")#line:707
                text .see (END )#line:708
            try :#line:710
                dishi =pd .read_excel (O0OOOOOO00000OOOO ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:713
                text .insert (END ,"\n找到地市清单，将规整地市名称。")#line:714
                for OOO00OO0O0OOOO00O in dishi ["地市列表"]:#line:715
                    O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["上报单位所属地区"].str .contains (OOO00OO0O0OOOO00O ,na =False )),"市级监测机构",]=OOO00OO0O0OOOO00O #line:719
                    O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:723
                    O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["市级监测机构"].str .contains ("北海",na =False )),"市级监测机构",]="北海"#line:730
                    O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["联系地址"].str .contains ("北海市",na =False )),"市级监测机构",]="北海"#line:734
                text .see (END )#line:735
            except :#line:736
                text .insert (END ,"\n未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。")#line:737
                text .see (END )#line:738
        else :#line:739
            O0O0OO0O00O0O0O00 =biaozhun .copy ()#line:740
            if len (dishi )!=0 :#line:741
                try :#line:742
                    text .insert (END ,"\n找到自定义的地市清单，将规整地市名称。")#line:743
                    for OOO00OO0O0OOOO00O in dishi ["地市列表"]:#line:744
                        O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["使用单位、经营企业所属监测机构"].str .contains (OOO00OO0O0OOOO00O ,na =False )),"市级监测机构",]=OOO00OO0O0OOOO00O #line:748
                    O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:752
                    text .see (END )#line:753
                except TRD :#line:754
                    text .insert (END ,"\n导入的自定义配置表中，未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。",)#line:758
                    text .see (END )#line:759
            text .insert (END ,"\n您使用了自己导入的配置表作为评分标准。")#line:760
            text .see (END )#line:761
    text .insert (END ,"\n正在抽样，请稍候...已完成30%")#line:762
    O0000000OO0O0O0O0 =O0000000OO0O0O0O0 .reset_index (drop =True )#line:763
    O0000000OO0O0O0O0 ["质量评估模式"]=O0000000OO0O0O0O0 [OOO0OOO0000O0OOOO ]#line:766
    O0000000OO0O0O0O0 ["报告时限"]=""#line:767
    O0000000OO0O0O0O0 ["报告时限情况"]="超时报告"#line:768
    O0000000OO0O0O0O0 ["识别代码"]=range (0 ,len (O0000000OO0O0O0O0 ))#line:769
    try :#line:770
        O0000000OO0O0O0O0 ["报告时限"]=pd .to_datetime (O0000000OO0O0O0O0 ["报告日期"])-pd .to_datetime (O0000000OO0O0O0O0 ["发现或获知日期"])#line:773
        O0000000OO0O0O0O0 ["报告时限"]=O0000000OO0O0O0O0 ["报告时限"].dt .days #line:774
        O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["伤害"]=="死亡")&(O0000000OO0O0O0O0 ["报告时限"]<=7 ),"报告时限情况"]="死亡未超时，报告时限："+O0000000OO0O0O0O0 ["报告时限"].astype (str )#line:777
        O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["伤害"]=="严重伤害")&(O0000000OO0O0O0O0 ["报告时限"]<=20 ),"报告时限情况"]="严重伤害未超时，报告时限："+O0000000OO0O0O0O0 ["报告时限"].astype (str )#line:780
        O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["伤害"]=="其他")&(O0000000OO0O0O0O0 ["报告时限"]<=30 ),"报告时限情况"]="其他未超时，报告时限："+O0000000OO0O0O0O0 ["报告时限"].astype (str )#line:783
        O0000000OO0O0O0O0 .loc [(O0000000OO0O0O0O0 ["报告时限情况"]=="超时报告"),"报告时限情况"]="！疑似超时报告，报告时限："+O0000000OO0O0O0O0 ["报告时限"].astype (str )#line:786
        O0000000OO0O0O0O0 ["型号和规格"]=("型号："+O0000000OO0O0O0O0 ["型号"].astype (str )+"   \n规格："+O0000000OO0O0O0O0 ["规格"].astype (str ))#line:789
        O0000000OO0O0O0O0 ["产品批号和产品编号"]=("产品批号："+O0000000OO0O0O0O0 ["产品批号"].astype (str )+"   \n产品编号："+O0000000OO0O0O0O0 ["产品编号"].astype (str ))#line:795
        O0000000OO0O0O0O0 ["使用场所和场所名称"]=("使用场所："+O0000000OO0O0O0O0 ["使用场所"].astype (str )+"   \n场所名称："+O0000000OO0O0O0O0 ["场所名称"].astype (str ))#line:801
        O0000000OO0O0O0O0 ["年龄和年龄类型"]=("年龄："+O0000000OO0O0O0O0 ["年龄"].astype (str )+"   \n年龄类型："+O0000000OO0O0O0O0 ["年龄类型"].astype (str ))#line:807
        O0000000OO0O0O0O0 ["事件原因分析和事件原因分析描述"]=("事件原因分析："+O0000000OO0O0O0O0 ["事件原因分析"].astype (str )+"   \n事件原因分析描述："+O0000000OO0O0O0O0 ["事件原因分析描述"].astype (str ))#line:813
        O0000000OO0O0O0O0 ["是否开展了调查及调查情况"]=("是否开展了调查："+O0000000OO0O0O0O0 ["是否开展了调查"].astype (str )+"   \n调查情况："+O0000000OO0O0O0O0 ["调查情况"].astype (str ))#line:822
        O0000000OO0O0O0O0 ["控制措施情况"]=("是否已采取控制措施："+O0000000OO0O0O0O0 ["是否已采取控制措施"].astype (str )+"   \n具体控制措施："+O0000000OO0O0O0O0 ["具体控制措施"].astype (str )+"   \n未采取控制措施原因："+O0000000OO0O0O0O0 ["未采取控制措施原因"].astype (str ))#line:831
        O0000000OO0O0O0O0 ["是否为错报误报报告及错报误报说明"]=("是否为错报误报报告："+O0000000OO0O0O0O0 ["是否为错报误报报告"].astype (str )+"   \n错报误报说明："+O0000000OO0O0O0O0 ["错报误报说明"].astype (str ))#line:838
        O0000000OO0O0O0O0 ["是否合并报告及合并报告编码"]=("是否合并报告："+O0000000OO0O0O0O0 ["是否合并报告"].astype (str )+"   \n合并报告编码："+O0000000OO0O0O0O0 ["合并报告编码"].astype (str ))#line:845
    except :#line:846
        pass #line:847
    if "报告类型-新的"in O0000000OO0O0O0O0 .columns :#line:848
        O0000000OO0O0O0O0 ["报告时限"]=pd .to_datetime (O0000000OO0O0O0O0 ["报告日期"].astype (str ))-pd .to_datetime (O0000000OO0O0O0O0 ["不良反应发生时间"].astype (str ))#line:850
        O0000000OO0O0O0O0 ["报告类型"]=O0000000OO0O0O0O0 ["报告类型-新的"].astype (str )+O0000000OO0O0O0O0 ["伤害"].astype (str )+"    "+O0000000OO0O0O0O0 ["严重药品不良反应"].astype (str )#line:851
        O0000000OO0O0O0O0 ["报告类型"]=O0000000OO0O0O0O0 ["报告类型"].str .replace ("-未填写-","",regex =False )#line:852
        O0000000OO0O0O0O0 ["报告类型"]=O0000000OO0O0O0O0 ["报告类型"].str .replace ("其他","一般",regex =False )#line:853
        O0000000OO0O0O0O0 ["报告类型"]=O0000000OO0O0O0O0 ["报告类型"].str .replace ("严重伤害","严重",regex =False )#line:854
        O0000000OO0O0O0O0 ["关联性评价和ADR分析"]="停药减药后反应是否减轻或消失："+O0000000OO0O0O0O0 ["停药减药后反应是否减轻或消失"].astype (str )+"\n再次使用可疑药是否出现同样反应："+O0000000OO0O0O0O0 ["再次使用可疑药是否出现同样反应"].astype (str )+"\n报告人评价："+O0000000OO0O0O0O0 ["报告人评价"].astype (str )#line:855
        O0000000OO0O0O0O0 ["ADR过程描述以及处理情况"]="不良反应发生时间："+O0000000OO0O0O0O0 ["不良反应发生时间"].astype (str )+"\n不良反应过程描述："+O0000000OO0O0O0O0 ["不良反应过程描述"].astype (str )+"\n不良反应结果:"+O0000000OO0O0O0O0 ["不良反应结果"].astype (str )+"\n对原患疾病影响:"+O0000000OO0O0O0O0 ["对原患疾病影响"].astype (str )+"\n后遗症表现："+O0000000OO0O0O0O0 ["后遗症表现"].astype (str )+"\n死亡时间:"+O0000000OO0O0O0O0 ["死亡时间"].astype (str )+"\n直接死因:"+O0000000OO0O0O0O0 ["直接死因"].astype (str )#line:856
        O0000000OO0O0O0O0 ["报告者及患者有关情况"]="患者姓名："+O0000000OO0O0O0O0 ["患者姓名"].astype (str )+"\n性别："+O0000000OO0O0O0O0 ["性别"].astype (str )+"\n出生日期:"+O0000000OO0O0O0O0 ["出生日期"].astype (str )+"\n年龄:"+O0000000OO0O0O0O0 ["年龄"].astype (str )+O0000000OO0O0O0O0 ["年龄单位"].astype (str )+"\n民族："+O0000000OO0O0O0O0 ["民族"].astype (str )+"\n体重:"+O0000000OO0O0O0O0 ["体重"].astype (str )+"\n原患疾病:"+O0000000OO0O0O0O0 ["原患疾病"].astype (str )+"\n病历号/门诊号:"+O0000000OO0O0O0O0 ["病历号/门诊号"].astype (str )+"\n既往药品不良反应/事件:"+O0000000OO0O0O0O0 ["既往药品不良反应/事件"].astype (str )+"\n家族药品不良反应/事件:"+O0000000OO0O0O0O0 ["家族药品不良反应/事件"].astype (str )#line:857
    OOOOO0OOOOOOOO00O =filedialog .askdirectory ()#!!!!!!!#line:861
    O000O00OOOO0000O0 =1 #line:864
    for OO00OOO0OOOO0O00O in O0000000OO0O0O0O0 ["伤害"].drop_duplicates ():#line:865
        if OO00OOO0OOOO0O00O =="其他":#line:866
            O00O0O00O0OO0000O =1 #line:867
            OOOO0000O0OOOOO00 =O0000000OO0O0O0O0 [(O0000000OO0O0O0O0 ["伤害"]=="其他")]#line:868
            O000OO0000O0OO0OO =Tdoing (OOOO0000O0OOOOO00 ,O0O0OOOO0O0OOO0O0 ,O00O00OOOOO0OO0O0 ,OOO0OOO0000O0OOOO ,OOO0OO00O0O0O0O0O ,O0O0O00O0OOO00OO0 )#line:869
            if O000O00OOOO0000O0 ==1 :#line:870
                OO0OOO000000OO0OO =O000OO0000O0OO0OO [0 ]#line:871
                O000O00OOOO0000O0 =O000O00OOOO0000O0 +1 #line:872
            else :#line:873
                OO0OOO000000OO0OO =pd .concat ([OO0OOO000000OO0OO ,O000OO0000O0OO0OO [0 ]],axis =0 )#line:874
        if OO00OOO0OOOO0O00O =="严重伤害":#line:876
            OO0O0O00OO00O0OOO =1 #line:877
            OOOO00O000O00OO0O =O0000000OO0O0O0O0 [(O0000000OO0O0O0O0 ["伤害"]=="严重伤害")]#line:878
            O0O00OOOO00000000 =Tdoing (OOOO00O000O00OO0O ,O0OOOO00O0O0O0000 ,O00O00OOOOO0OO0O0 ,OOO0OOO0000O0OOOO ,OOO0OO00O0O0O0O0O ,O0O0O00O0OOO00OO0 )#line:879
            if O000O00OOOO0000O0 ==1 :#line:880
                OO0OOO000000OO0OO =O0O00OOOO00000000 [0 ]#line:881
                O000O00OOOO0000O0 =O000O00OOOO0000O0 +1 #line:882
            else :#line:883
                OO0OOO000000OO0OO =pd .concat ([OO0OOO000000OO0OO ,O0O00OOOO00000000 [0 ]],axis =0 )#line:884
        if OO00OOO0OOOO0O00O =="死亡":#line:886
            O0000O000O0O0O0OO =1 #line:887
            OO00000O0O0OOO0O0 =O0000000OO0O0O0O0 [(O0000000OO0O0O0O0 ["伤害"]=="死亡")]#line:888
            OOO0OO000O0OOOO00 =Tdoing (OO00000O0O0OOO0O0 ,O000O0O0OOOOOO000 ,O00O00OOOOO0OO0O0 ,OOO0OOO0000O0OOOO ,OOO0OO00O0O0O0O0O ,O0O0O00O0OOO00OO0 )#line:889
            if O000O00OOOO0000O0 ==1 :#line:890
                OO0OOO000000OO0OO =OOO0OO000O0OOOO00 [0 ]#line:891
                O000O00OOOO0000O0 =O000O00OOOO0000O0 +1 #line:892
            else :#line:893
                OO0OOO000000OO0OO =pd .concat ([OO0OOO000000OO0OO ,OOO0OO000O0OOOO00 [0 ]],axis =0 )#line:894
    text .insert (END ,"\n正在抽样，请稍候...已完成50%")#line:898
    O000OO00OO0O0OOOO =pd .ExcelWriter (str (OOOOO0OOOOOOOO00O )+"/●(最终评分需导入)被抽出的所有数据"+".xlsx")#line:899
    OO0OOO000000OO0OO .to_excel (O000OO00OO0O0OOOO ,sheet_name ="被抽出的所有数据")#line:900
    O000OO00OO0O0OOOO .close ()#line:901
    if O0O0O00O0OOO00OO0 ==1 :#line:904
        OOO000O00OO000OO0 =O0000000OO0O0O0O0 .copy ()#line:905
        OOO000O00OO000OO0 ["原始数量"]=1 #line:906
        O0000OOOO0O0OO0OO =OO0OOO000000OO0OO .copy ()#line:907
        O0000OOOO0O0OO0OO ["抽取数量"]=1 #line:908
        O000OO0O0OOO0OO00 =OOO000O00OO000OO0 .groupby ([OOO0OOO0000O0OOOO ]).aggregate ({"原始数量":"count"})#line:911
        O000OO0O0OOO0OO00 =O000OO0O0OOO0OO00 .sort_values (by =["原始数量"],ascending =False ,na_position ="last")#line:914
        O000OO0O0OOO0OO00 =O000OO0O0OOO0OO00 .reset_index ()#line:915
        O0OOO0OOOOO0000OO =pd .pivot_table (O0000OOOO0O0OO0OO ,values =["抽取数量"],index =OOO0OOO0000O0OOOO ,columns ="伤害",aggfunc ={"抽取数量":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:926
        O0OOO0OOOOO0000OO .columns =O0OOO0OOOOO0000OO .columns .droplevel (0 )#line:927
        O0OOO0OOOOO0000OO =O0OOO0OOOOO0000OO .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:930
        O0OOO0OOOOO0000OO =O0OOO0OOOOO0000OO .reset_index ()#line:931
        O0OOO0OOOOO0000OO =O0OOO0OOOOO0000OO .rename (columns ={"All":"抽取总数量"})#line:932
        try :#line:933
            O0OOO0OOOOO0000OO =O0OOO0OOOOO0000OO .rename (columns ={"一般":"抽取数量(一般)"})#line:934
        except :#line:935
            pass #line:936
        try :#line:937
            O0OOO0OOOOO0000OO =O0OOO0OOOOO0000OO .rename (columns ={"严重伤害":"抽取数量(严重)"})#line:938
        except :#line:939
            pass #line:940
        try :#line:941
            O0OOO0OOOOO0000OO =O0OOO0OOOOO0000OO .rename (columns ={"死亡":"抽取数量-死亡"})#line:942
        except :#line:943
            pass #line:944
        O000OOOO0OOO0O0O0 =pd .merge (O000OO0O0OOO0OO00 ,O0OOO0OOOOO0000OO ,on =[OOO0OOO0000O0OOOO ],how ="left")#line:945
        O000OOOO0OOO0O0O0 ["抽取比例"]=round (O000OOOO0OOO0O0O0 ["抽取总数量"]/O000OOOO0OOO0O0O0 ["原始数量"],2 )#line:946
        O00OOO00OO00O0OOO =pd .ExcelWriter (str (OOOOO0OOOOOOOO00O )+"/抽样情况分布"+".xlsx")#line:947
        O000OOOO0OOO0O0O0 .to_excel (O00OOO00OO00O0OOO ,sheet_name ="抽样情况分布")#line:948
        O00OOO00OO00O0OOO .close ()#line:949
    OO0OOO000000OO0OO =OO0OOO000000OO0OO [O0O0OO0O00O0O0O00 ["评分项"].tolist ()]#line:955
    OOO0000O0O0O0O00O =int (O00O00OOOOO0OO0O0 )#line:957
    text .insert (END ,"\n正在抽样，请稍候...已完成70%")#line:959
    for OO00OOO0OOOO0O00O in range (OOO0000O0O0O0O00O ):#line:960
        if OO00OOO0OOOO0O00O ==0 :#line:961
            O00000000000OO0O0 =OO0OOO000000OO0OO [(OO0OOO000000OO0OO ["伤害"]=="其他")].sample (frac =1 /(OOO0000O0O0O0O00O -OO00OOO0OOOO0O00O ),replace =False )#line:965
            O000000OO00O0O000 =OO0OOO000000OO0OO [(OO0OOO000000OO0OO ["伤害"]=="严重伤害")].sample (frac =1 /(OOO0000O0O0O0O00O -OO00OOO0OOOO0O00O ),replace =False )#line:968
            O0OO00000OOOOO0O0 =OO0OOO000000OO0OO [(OO0OOO000000OO0OO ["伤害"]=="死亡")].sample (frac =1 /(OOO0000O0O0O0O00O -OO00OOO0OOOO0O00O ),replace =False )#line:971
            O00OOO0OO0O000000 =pd .concat ([O00000000000OO0O0 ,O000000OO00O0O000 ,O0OO00000OOOOO0O0 ],axis =0 )#line:973
        else :#line:975
            OO0OOO000000OO0OO =pd .concat ([OO0OOO000000OO0OO ,O00OOO0OO0O000000 ],axis =0 )#line:976
            OO0OOO000000OO0OO .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:977
            O00000000000OO0O0 =OO0OOO000000OO0OO [(OO0OOO000000OO0OO ["伤害"]=="其他")].sample (frac =1 /(OOO0000O0O0O0O00O -OO00OOO0OOOO0O00O ),replace =False )#line:980
            O000000OO00O0O000 =OO0OOO000000OO0OO [(OO0OOO000000OO0OO ["伤害"]=="严重伤害")].sample (frac =1 /(OOO0000O0O0O0O00O -OO00OOO0OOOO0O00O ),replace =False )#line:983
            O0OO00000OOOOO0O0 =OO0OOO000000OO0OO [(OO0OOO000000OO0OO ["伤害"]=="死亡")].sample (frac =1 /(OOO0000O0O0O0O00O -OO00OOO0OOOO0O00O ),replace =False )#line:986
            O00OOO0OO0O000000 =pd .concat ([O00000000000OO0O0 ,O000000OO00O0O000 ,O0OO00000OOOOO0O0 ],axis =0 )#line:987
        try :#line:988
            O00OOO0OO0O000000 ["报告编码"]=O00OOO0OO0O000000 ["报告编码"].astype (str )#line:989
        except :#line:990
            pass #line:991
        OO0OO0OOO0O00O000 =str (OOOOO0OOOOOOOO00O )+"/"+str (OO00OOO0OOOO0O00O +1 )+".xlsx"#line:992
        if O0O0O00O0OOO00OO0 ==1 :#line:995
            OO000O0OO000OO0O0 =TeasyreadT (O00OOO0OO0O000000 .copy ())#line:996
            del OO000O0OO000OO0O0 ["逐条查看"]#line:997
            OO000O0OO000OO0O0 ["评分"]=""#line:998
            if len (OO000O0OO000OO0O0 )>0 :#line:999
                for OO00OO00OO00O0OOO ,OO00O0OO0OOO00O0O in O0O0OO0O00O0O0O00 .iterrows ():#line:1000
                    OO000O0OO000OO0O0 .loc [(OO000O0OO000OO0O0 ["条目"]==OO00O0OO0OOO00O0O ["评分项"]),"满分"]=OO00O0OO0OOO00O0O ["满分分值"]#line:1001
                    OO000O0OO000OO0O0 .loc [(OO000O0OO000OO0O0 ["条目"]==OO00O0OO0OOO00O0O ["评分项"]),"打分标准"]=OO00O0OO0OOO00O0O ["打分标准"]#line:1004
            OO000O0OO000OO0O0 ["专家序号"]=OO00OOO0OOOO0O00O +1 #line:1006
            OOOOOO0O00000OOOO =str (OOOOO0OOOOOOOO00O )+"/"+"●专家评分表"+str (OO00OOO0OOOO0O00O +1 )+".xlsx"#line:1007
            O0OO0OOO0000O0O00 =pd .ExcelWriter (OOOOOO0O00000OOOO )#line:1008
            OO000O0OO000OO0O0 .to_excel (O0OO0OOO0000O0O00 ,sheet_name ="字典数据")#line:1009
            O0OO0OOO0000O0O00 .close ()#line:1010
    text .insert (END ,"\n正在抽样，请稍候...已完成100%")#line:1013
    showinfo (title ="提示信息",message ="抽样和分组成功，请查看以下文件夹："+str (OOOOO0OOOOOOOO00O ))#line:1014
    text .insert (END ,"\n抽样和分组成功，请查看以下文件夹："+str (OOOOO0OOOOOOOO00O ))#line:1015
    text .insert (END ,"\n抽样概况:\n")#line:1016
    text .insert (END ,O000OOOO0OOO0O0O0 [[OOO0OOO0000O0OOOO ,"原始数量","抽取总数量"]])#line:1017
    text .see (END )#line:1018
def Tdoing (O0O0OOO0OOO0OO000 ,O000O0O00O000O0OO ,OOOOOOO0OO0OOOO00 ,OOO0O00O0O0OO00OO ,O0O000O00000OOO00 ,OO0000OO0O0000OOO ):#line:1021
    ""#line:1022
    def OO00OO0O00OOOOO0O (O0OOOOOOO0O0O0000 ,O0OOOOO000O0O00O0 ,O000OOO0000OOO0OO ):#line:1024
        if float (O0OOOOO000O0O00O0 )>1 :#line:1025
            try :#line:1026
                O00OO0OO000OO0OO0 =O0OOOOOOO0O0O0000 .sample (int (O0OOOOO000O0O00O0 ),replace =False )#line:1027
            except ValueError :#line:1029
                O00OO0OO000OO0OO0 =O0OOOOOOO0O0O0000 #line:1031
        else :#line:1032
            O00OO0OO000OO0OO0 =O0OOOOOOO0O0O0000 .sample (frac =float (O0OOOOO000O0O00O0 ),replace =False )#line:1033
            if len (O0OOOOOOO0O0O0000 )*float (O0OOOOO000O0O00O0 )>len (O00OO0OO000OO0OO0 )and O000OOO0000OOO0OO =="最大覆盖":#line:1035
                O0O00O0OO0OO00000 =pd .concat ([O0OOOOOOO0O0O0000 ,O00OO0OO000OO0OO0 ],axis =0 )#line:1036
                O0O00O0OO0OO00000 .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:1037
                O00OOOO0O0000O00O =O0O00O0OO0OO00000 .sample (1 ,replace =False )#line:1038
                O00OO0OO000OO0OO0 =pd .concat ([O00OO0OO000OO0OO0 ,O00OOOO0O0000O00O ],axis =0 )#line:1039
        return O00OO0OO000OO0OO0 #line:1040
    if O0O000O00000OOO00 =="总体随机":#line:1043
        OO0OOOO0000OO000O =OO00OO0O00OOOOO0O (O0O0OOO0OOO0OO000 ,O000O0O00O000O0OO ,O0O000O00000OOO00 )#line:1044
    else :#line:1046
        OO0OO000O000OO00O =1 #line:1047
        for O0O000OO0000OO000 in O0O0OOO0OOO0OO000 [OOO0O00O0O0OO00OO ].drop_duplicates ():#line:1048
            OOOOO00O0000O0000 =O0O0OOO0OOO0OO000 [(O0O0OOO0OOO0OO000 [OOO0O00O0O0OO00OO ]==O0O000OO0000OO000 )].copy ()#line:1049
            if OO0OO000O000OO00O ==1 :#line:1050
                OO0OOOO0000OO000O =OO00OO0O00OOOOO0O (OOOOO00O0000O0000 ,O000O0O00O000O0OO ,O0O000O00000OOO00 )#line:1051
                OO0OO000O000OO00O =OO0OO000O000OO00O +1 #line:1052
            else :#line:1053
                OOO0OOOO0OO0OO0O0 =OO00OO0O00OOOOO0O (OOOOO00O0000O0000 ,O000O0O00O000O0OO ,O0O000O00000OOO00 )#line:1054
                OO0OOOO0000OO000O =pd .concat ([OO0OOOO0000OO000O ,OOO0OOOO0OO0OO0O0 ])#line:1055
    OO0OOOO0000OO000O =OO0OOOO0000OO000O .drop_duplicates ()#line:1056
    return OO0OOOO0000OO000O ,1 #line:1057
def Tpinggu ():#line:1060
    ""#line:1061
    OOOO0OO0O00OO00OO =Topentable (1 )#line:1062
    OOOOO00O00OOOO0OO =OOOO0OO0O00OO00OO [0 ]#line:1063
    OO0O00O0000000O00 =OOOO0OO0O00OO00OO [1 ]#line:1064
    try :#line:1067
        OOOO0000O0O00OO00 =[pd .read_excel (OO0O0OO0OO00O0O00 ,header =0 ,sheet_name =0 )for OO0O0OO0OO00O0O00 in OO0O00O0000000O00 ]#line:1071
        O00O000O00OOOO000 =pd .concat (OOOO0000O0O00OO00 ,ignore_index =True ).drop_duplicates ()#line:1072
        try :#line:1073
            O00O000O00OOOO000 =O00O000O00OOOO000 .loc [:,~O00O000O00OOOO000 .columns .str .contains ("^Unnamed")]#line:1074
        except :#line:1075
            pass #line:1076
    except :#line:1077
        showinfo (title ="提示信息",message ="载入文件出错，任务终止。")#line:1078
        return 0 #line:1079
    try :#line:1082
        OOOOO00O00OOOO0OO =OOOOO00O00OOOO0OO .reset_index ()#line:1083
    except :#line:1084
        showinfo (title ="提示信息",message ="专家评分文件存在错误，程序中止。")#line:1085
        return 0 #line:1086
    O00O000O00OOOO000 ["质量评估专用表"]=""#line:1088
    text .insert (END ,"\n打分表导入成功，正在统计，请耐心等待...")#line:1091
    text .insert (END ,"\n正在计算总分，请稍候，已完成20%")#line:1092
    text .see (END )#line:1093
    O00000O0OOO0O0O00 =OOOOO00O00OOOO0OO [["序号","条目","详细描述","评分","满分","打分标准","专家序号"]].copy ()#line:1096
    O0OOOOOOOO000OOOO =O00O000O00OOOO000 [["质量评估模式","识别代码"]].copy ()#line:1097
    O00000O0OOO0O0O00 .reset_index (inplace =True )#line:1098
    O0OOOOOOOO000OOOO .reset_index (inplace =True )#line:1099
    O0OOOOOOOO000OOOO =O0OOOOOOOO000OOOO .rename (columns ={"识别代码":"序号"})#line:1100
    O00000O0OOO0O0O00 =pd .merge (O00000O0OOO0O0O00 ,O0OOOOOOOO000OOOO ,on =["序号"])#line:1101
    O00000O0OOO0O0O00 =O00000O0OOO0O0O00 .sort_values (by =["序号","条目"],ascending =True ,na_position ="last")#line:1102
    O00000O0OOO0O0O00 =O00000O0OOO0O0O00 [["质量评估模式","序号","条目","详细描述","评分","满分","打分标准","专家序号"]]#line:1103
    for OOO00000O00OO0O00 ,OOO0O0OOOO0O00OO0 in OOOOO00O00OOOO0OO .iterrows ():#line:1105
        OOOO00O0O00O0OOO0 ="专家打分-"+str (OOO0O0OOOO0O00OO0 ["条目"])#line:1106
        O00O000O00OOOO000 .loc [(O00O000O00OOOO000 ["识别代码"]==OOO0O0OOOO0O00OO0 ["序号"]),OOOO00O0O00O0OOO0 ]=OOO0O0OOOO0O00OO0 ["评分"]#line:1107
    del O00O000O00OOOO000 ["专家打分-识别代码"]#line:1108
    del O00O000O00OOOO000 ["专家打分-#####分隔符#########"]#line:1109
    try :#line:1110
        O00O000O00OOOO000 =O00O000O00OOOO000 .loc [:,~O00O000O00OOOO000 .columns .str .contains ("^Unnamed")]#line:1111
    except :#line:1112
        pass #line:1113
    text .insert (END ,"\n正在计算总分，请稍候，已完成60%")#line:1114
    text .see (END )#line:1115
    O0OO00O0OO00O0O0O =OO0O00O0000000O00 [0 ]#line:1118
    try :#line:1119
        O0O0O00OOOOO000O0 =str (O0OO00O0OO00O0O0O ).replace ("●(最终评分需导入)被抽出的所有数据.xls","")#line:1120
    except :#line:1121
        O0O0O00OOOOO000O0 =str (O0OO00O0OO00O0O0O )#line:1122
    OOO0O0O000OOO00OO =pd .ExcelWriter (str (O0O0O00OOOOO000O0 )+"各评估对象打分核对文件"+".xlsx")#line:1130
    O00000O0OOO0O0O00 .to_excel (OOO0O0O000OOO00OO ,sheet_name ="原始打分")#line:1131
    OOO0O0O000OOO00OO .close ()#line:1132
    OO0OO0000O0O0OO00 =Tpinggu2 (O00O000O00OOOO000 )#line:1136
    text .insert (END ,"\n正在计算总分，请稍候，已完成100%")#line:1138
    text .see (END )#line:1139
    showinfo (title ="提示信息",message ="打分计算成功，请查看文件："+str (O0O0O00OOOOO000O0 )+"最终打分"+".xlsx")#line:1140
    text .insert (END ,"\n打分计算成功，请查看文件："+str (O0OO00O0OO00O0O0O )+"最终打分"+".xls\n")#line:1141
    OO0OO0000O0O0OO00 .reset_index (inplace =True )#line:1142
    text .insert (END ,"\n以下是结果概况：\n")#line:1143
    text .insert (END ,OO0OO0000O0O0OO00 [["评估对象","总分"]])#line:1144
    text .see (END )#line:1145
    OOO0OO0OOO0OOO00O =["评估对象","总分"]#line:1149
    for O0OO0000000OO0000 in OO0OO0000O0O0OO00 .columns :#line:1150
        if "专家打分"in O0OO0000000OO0000 :#line:1151
            OOO0OO0OOO0OOO00O .append (O0OO0000000OO0000 )#line:1152
    O00OOO0O000000O00 =OO0OO0000O0O0OO00 [OOO0OO0OOO0OOO00O ]#line:1153
    OO00O00OO000O000O =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:1157
    if "专家打分-不良反应名称"in OOO0OO0OOO0OOO00O :#line:1159
        OO00O00OO000O000O =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:1160
    if "专家打分-化妆品名称"in OOO0OO0OOO0OOO00O :#line:1162
        OO00O00OO000O000O =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:1163
    if "专家打分-是否需要开展产品风险评价"in OOO0OO0OOO0OOO00O :#line:1164
        OO00O00OO000O000O =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:1165
    for OOO00000O00OO0O00 ,OOO0O0OOOO0O00OO0 in OO00O00OO000O000O .iterrows ():#line:1166
        OOO00OO0O0OOOOOO0 ="专家打分-"+str (OOO0O0OOOO0O00OO0 ["评分项"])#line:1167
        try :#line:1168
            warnings .filterwarnings ('ignore')#line:1169
            O00OOO0O000000O00 .loc [-1 ,OOO00OO0O0OOOOOO0 ]=OOO0O0OOOO0O00OO0 ["满分分值"]#line:1170
        except :#line:1171
            pass #line:1172
    del O00OOO0O000000O00 ["专家打分-识别代码"]#line:1173
    O00OOO0O000000O00 .iloc [-1 ,0 ]="满分分值"#line:1174
    O00OOO0O000000O00 .loc [-1 ,"总分"]=100 #line:1175
    if "专家打分-事件原因分析.1"not in OOO0OO0OOO0OOO00O :#line:1177
        O00OOO0O000000O00 .loc [-1 ,"专家打分-报告时限"]=5 #line:1178
    if "专家打分-事件原因分析.1"in OOO0OO0OOO0OOO00O :#line:1180
        O00OOO0O000000O00 .loc [-1 ,"专家打分-报告时限"]=10 #line:1181
    O00OOO0O000000O00 .columns =O00OOO0O000000O00 .columns .str .replace ("专家打分-","",regex =False )#line:1184
    if ("专家打分-器械故障表现"in OOO0OO0OOO0OOO00O )and ("modex"not in O00O000O00OOOO000 .columns ):#line:1186
        O00OOO0O000000O00 .loc [-1 ,"姓名和既往病史"]=2 #line:1187
        O00OOO0O000000O00 .loc [-1 ,"报告日期"]=1 #line:1188
    else :#line:1189
        del O00OOO0O000000O00 ["伤害"]#line:1190
    if "专家打分-化妆品名称"in OOO0OO0OOO0OOO00O :#line:1192
        del O00OOO0O000000O00 ["报告时限"]#line:1193
    try :#line:1196
        O00OOO0O000000O00 =O00OOO0O000000O00 [["评估对象","总分","伤害.1","是否开展了调查及调查情况","关联性评价","事件原因分析.1","是否需要开展产品风险评价","控制措施情况","是否为错报误报报告及错报误报说明","是否合并报告及合并报告编码","报告时限"]]#line:1197
    except :#line:1198
        pass #line:1199
    try :#line:1200
        O00OOO0O000000O00 =O00OOO0O000000O00 [["评估对象","总分","报告日期","报告人","联系人","联系电话","注册证编号/曾用注册证编号","产品名称","型号和规格","产品批号和产品编号","生产日期","有效期至","事件发生日期","发现或获知日期","伤害","伤害表现","器械故障表现","姓名和既往病史","年龄和年龄类型","性别","预期治疗疾病或作用","器械使用日期","使用场所和场所名称","使用过程","合并用药/械情况说明","事件原因分析和事件原因分析描述","初步处置情况","报告时限"]]#line:1201
    except :#line:1202
        pass #line:1203
    try :#line:1204
        O00OOO0O000000O00 =O00OOO0O000000O00 [["评估对象","总分","报告类型","报告时限","报告者及患者有关情况","原患疾病","药品信息","不良反应名称","ADR过程描述以及处理情况","关联性评价和ADR分析"]]#line:1205
    except :#line:1206
        pass #line:1207
    OO00O0O00OOO0OO0O =pd .ExcelWriter (str (O0O0O00OOOOO000O0 )+"最终打分"+".xlsx")#line:1209
    O00OOO0O000000O00 .to_excel (OO00O0O00OOO0OO0O ,sheet_name ="最终打分")#line:1210
    OO00O0O00OOO0OO0O .close ()#line:1211
    Ttree_Level_2 (O00OOO0O000000O00 ,0 ,OO0OO0000O0O0OO00 )#line:1213
def Tpinggu2 (O0O0OOO0OO00000O0 ):#line:1216
    ""#line:1217
    O0O0OOO0OO00000O0 ["报告数量小计"]=1 #line:1218
    if ("器械故障表现"in O0O0OOO0OO00000O0 .columns )and ("modex"not in O0O0OOO0OO00000O0 .columns ):#line:1221
        O0O0OOO0OO00000O0 ["专家打分-姓名和既往病史"]=2 #line:1222
        O0O0OOO0OO00000O0 ["专家打分-报告日期"]=1 #line:1223
        if "专家打分-报告时限情况"not in O0O0OOO0OO00000O0 .columns :#line:1224
            O0O0OOO0OO00000O0 ["报告时限"]=O0O0OOO0OO00000O0 ["报告时限"].astype (float )#line:1225
            O0O0OOO0OO00000O0 ["专家打分-报告时限"]=0 #line:1226
            O0O0OOO0OO00000O0 .loc [(O0O0OOO0OO00000O0 ["伤害"]=="死亡")&(O0O0OOO0OO00000O0 ["报告时限"]<=7 ),"专家打分-报告时限"]=5 #line:1227
            O0O0OOO0OO00000O0 .loc [(O0O0OOO0OO00000O0 ["伤害"]=="严重伤害")&(O0O0OOO0OO00000O0 ["报告时限"]<=20 ),"专家打分-报告时限"]=5 #line:1228
            O0O0OOO0OO00000O0 .loc [(O0O0OOO0OO00000O0 ["伤害"]=="其他")&(O0O0OOO0OO00000O0 ["报告时限"]<=30 ),"专家打分-报告时限"]=5 #line:1229
    if "专家打分-事件原因分析.1"in O0O0OOO0OO00000O0 .columns :#line:1233
       O0O0OOO0OO00000O0 ["专家打分-报告时限"]=10 #line:1234
    OOO0OOO0O0OO00O00 =[]#line:1237
    for OOO00O0O0O0000OO0 in O0O0OOO0OO00000O0 .columns :#line:1238
        if "专家打分-"in OOO00O0O0O0000OO0 :#line:1239
            OOO0OOO0O0OO00O00 .append (OOO00O0O0O0000OO0 )#line:1240
    OOO0000OOO00O0OO0 =1 #line:1244
    for OOO00O0O0O0000OO0 in OOO0OOO0O0OO00O00 :#line:1245
        O0000OO0O0OO000OO =O0O0OOO0OO00000O0 .groupby (["质量评估模式"]).aggregate ({OOO00O0O0O0000OO0 :"sum"}).reset_index ()#line:1246
        if OOO0000OOO00O0OO0 ==1 :#line:1247
            O0000O00OOOO0O0O0 =O0000OO0O0OO000OO #line:1248
            OOO0000OOO00O0OO0 =OOO0000OOO00O0OO0 +1 #line:1249
        else :#line:1250
            O0000O00OOOO0O0O0 =pd .merge (O0000O00OOOO0O0O0 ,O0000OO0O0OO000OO ,on ="质量评估模式",how ="left")#line:1251
    O0000000000000O0O =O0O0OOO0OO00000O0 .groupby (["质量评估模式"]).aggregate ({"报告数量小计":"sum"}).reset_index ()#line:1253
    O0000O00OOOO0O0O0 =pd .merge (O0000O00OOOO0O0O0 ,O0000000000000O0O ,on ="质量评估模式",how ="left")#line:1254
    for OOO00O0O0O0000OO0 in OOO0OOO0O0OO00O00 :#line:1257
        O0000O00OOOO0O0O0 [OOO00O0O0O0000OO0 ]=round (O0000O00OOOO0O0O0 [OOO00O0O0O0000OO0 ]/O0000O00OOOO0O0O0 ["报告数量小计"],2 )#line:1258
    O0000O00OOOO0O0O0 ["总分"]=round (O0000O00OOOO0O0O0 [OOO0OOO0O0OO00O00 ].sum (axis =1 ),2 )#line:1259
    O0000O00OOOO0O0O0 =O0000O00OOOO0O0O0 .sort_values (by =["总分"],ascending =False ,na_position ="last")#line:1260
    warnings .filterwarnings ('ignore')#line:1261
    O0000O00OOOO0O0O0 .loc ["平均分(非加权)"]=round (O0000O00OOOO0O0O0 .mean (axis =0 ),2 )#line:1262
    O0000O00OOOO0O0O0 .loc ["标准差(非加权)"]=round (O0000O00OOOO0O0O0 .std (axis =0 ),2 )#line:1263
    O0000O00OOOO0O0O0 =O0000O00OOOO0O0O0 .rename (columns ={"质量评估模式":"评估对象"})#line:1264
    O0000O00OOOO0O0O0 .iloc [-2 ,0 ]="平均分(非加权)"#line:1265
    O0000O00OOOO0O0O0 .iloc [-1 ,0 ]="标准差(非加权)"#line:1266
    return O0000O00OOOO0O0O0 #line:1268
def Ttree_Level_2 (O0O00O0OOOOO0O0O0 ,O00000OOO0OO00OO0 ,O00OO00O000OO00O0 ,*O000OO0OO0O0O0O00 ):#line:1271
    ""#line:1272
    O0O0O000OOOO00O00 =O0O00O0OOOOO0O0O0 .columns .values .tolist ()#line:1274
    O00000OOO0OO00OO0 =0 #line:1275
    O000OOO0OO0O0O00O =O0O00O0OOOOO0O0O0 .loc [:]#line:1276
    OO0OO0O00O00O000O =Toplevel ()#line:1279
    OO0OO0O00O00O000O .title ("报表查看器")#line:1280
    OOOO0O0O0OO0OO00O =OO0OO0O00O00O000O .winfo_screenwidth ()#line:1281
    O0OOOOO0OO00O0O0O =OO0OO0O00O00O000O .winfo_screenheight ()#line:1283
    OOOOO00O00O0OO0OO =1300 #line:1285
    O00O00OO00O00OOO0 =600 #line:1286
    O0O00OOO0000OOO00 =(OOOO0O0O0OO0OO00O -OOOOO00O00O0OO0OO )/2 #line:1288
    O00OO0OOO00O000O0 =(O0OOOOO0OO00O0O0O -O00O00OO00O00OOO0 )/2 #line:1289
    OO0OO0O00O00O000O .geometry ("%dx%d+%d+%d"%(OOOOO00O00O0OO0OO ,O00O00OO00O00OOO0 ,O0O00OOO0000OOO00 ,O00OO0OOO00O000O0 ))#line:1290
    OO00O0000OOO000OO =ttk .Frame (OO0OO0O00O00O000O ,width =1300 ,height =20 )#line:1291
    OO00O0000OOO000OO .pack (side =TOP )#line:1292
    O0OO0000O0OO00OO0 =O000OOO0OO0O0O00O .values .tolist ()#line:1295
    O0O0000000O0OOO00 =O000OOO0OO0O0O00O .columns .values .tolist ()#line:1296
    O0000O0OO000000O0 =ttk .Treeview (OO00O0000OOO000OO ,columns =O0O0000000O0OOO00 ,show ="headings",height =45 )#line:1297
    for O0OOO0000O0O0OOO0 in O0O0000000O0OOO00 :#line:1299
        O0000O0OO000000O0 .heading (O0OOO0000O0O0OOO0 ,text =O0OOO0000O0O0OOO0 )#line:1300
    for OOO00O0O0OOO000O0 in O0OO0000O0OO00OO0 :#line:1301
        O0000O0OO000000O0 .insert ("","end",values =OOO00O0O0OOO000O0 )#line:1302
    for OOOOOO00O00OO0OOO in O0O0000000O0OOO00 :#line:1303
        O0000O0OO000000O0 .column (OOOOOO00O00OO0OOO ,minwidth =0 ,width =120 ,stretch =NO )#line:1304
    OO0O0OO0O0000O0O0 =Scrollbar (OO00O0000OOO000OO ,orient ="vertical")#line:1306
    OO0O0OO0O0000O0O0 .pack (side =RIGHT ,fill =Y )#line:1307
    OO0O0OO0O0000O0O0 .config (command =O0000O0OO000000O0 .yview )#line:1308
    O0000O0OO000000O0 .config (yscrollcommand =OO0O0OO0O0000O0O0 .set )#line:1309
    OO0O00000O00O0O00 =Scrollbar (OO00O0000OOO000OO ,orient ="horizontal")#line:1311
    OO0O00000O00O0O00 .pack (side =BOTTOM ,fill =X )#line:1312
    OO0O00000O00O0O00 .config (command =O0000O0OO000000O0 .xview )#line:1313
    O0000O0OO000000O0 .config (yscrollcommand =OO0O0OO0O0000O0O0 .set )#line:1314
    def OO00OOO0OOO000OOO (OOO0O0O00OO0O0OOO ,O0O0O00OO00O0OOO0 ,O0O0O0O00O0000OO0 ):#line:1316
        for OO0000OO00OOOO000 in O0000O0OO000000O0 .selection ():#line:1319
            O0OOO00OOO0O0O00O =O0000O0OO000000O0 .item (OO0000OO00OOOO000 ,"values")#line:1320
        OO0O00O000O0OO0OO =O0OOO00OOO0O0O00O [2 :]#line:1322
        OOO0000O0000OOOO0 =O0O0O0O00O0000OO0 .iloc [-1 ,:][2 :]#line:1325
        OOOO0OO0000OOO00O =O0O0O0O00O0000OO0 .columns #line:1326
        OOOO0OO0000OOO00O =OOOO0OO0000OOO00O [2 :]#line:1327
        Tpo (OOO0000O0000OOOO0 ,OO0O00O000O0OO0OO ,OOOO0OO0000OOO00O ,"失分","得分",O0OOO00OOO0O0O00O [0 ])#line:1329
        return 0 #line:1330
    O0000O0OO000000O0 .bind ("<Double-1>",lambda O000OO0O0O000OOO0 :OO00OOO0OOO000OOO (O000OO0O0O000OOO0 ,O0O0000000O0OOO00 ,O000OOO0OO0O0O00O ),)#line:1336
    def OOOO0OO000OOO00O0 (O000O00O0OO0O0O0O ,O0O00OO0O0OOO0OOO ,OOOO0O00OO00O0O0O ):#line:1338
        O000O0000OOO00000 =[(O000O00O0OO0O0O0O .set (O00OO0O00OO0O00OO ,O0O00OO0O0OOO0OOO ),O00OO0O00OO0O00OO )for O00OO0O00OO0O00OO in O000O00O0OO0O0O0O .get_children ("")]#line:1339
        O000O0000OOO00000 .sort (reverse =OOOO0O00OO00O0O0O )#line:1340
        for OO0OOOOOOOOOOO000 ,(OO0OOO000OOOOOOO0 ,O0O0O00OOO0O00000 )in enumerate (O000O0000OOO00000 ):#line:1342
            O000O00O0OO0O0O0O .move (O0O0O00OOO0O00000 ,"",OO0OOOOOOOOOOO000 )#line:1343
        O000O00O0OO0O0O0O .heading (O0O00OO0O0OOO0OOO ,command =lambda :OOOO0OO000OOO00O0 (O000O00O0OO0O0O0O ,O0O00OO0O0OOO0OOO ,not OOOO0O00OO00O0O0O ))#line:1346
    for O0OO0O0O0OOOO0OOO in O0O0000000O0OOO00 :#line:1348
        O0000O0OO000000O0 .heading (O0OO0O0O0OOOO0OOO ,text =O0OO0O0O0OOOO0OOO ,command =lambda _col =O0OO0O0O0OOOO0OOO :OOOO0OO000OOO00O0 (O0000O0OO000000O0 ,_col ,False ),)#line:1353
    O0000O0OO000000O0 .pack ()#line:1355
def Txuanze ():#line:1357
    ""#line:1358
    global ori #line:1359
    O0OOO0000O0OO0OOO =pd .read_excel (peizhidir +"0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1360
    text .insert (END ,"\n正在执行内部数据规整...\n")#line:1361
    text .insert (END ,O0OOO0000O0OO0OOO )#line:1362
    ori ["temppr"]=""#line:1363
    for O0000000OO0O000OO in O0OOO0000O0OO0OOO .columns .tolist ():#line:1364
        ori ["temppr"]=ori ["temppr"]+"----"+ori [O0000000OO0O000OO ]#line:1365
    OO0OOO0OOO000O0OO ="测试字段MMMMM"#line:1366
    for O0000000OO0O000OO in O0OOO0000O0OO0OOO .columns .tolist ():#line:1367
        for O0O000O0O0OOO0OO0 in O0OOO0000O0OO0OOO [O0000000OO0O000OO ].drop_duplicates ():#line:1368
            if O0O000O0O0OOO0OO0 :#line:1369
                OO0OOO0OOO000O0OO =OO0OOO0OOO000O0OO +"|"+str (O0O000O0O0OOO0OO0 )#line:1370
    ori =ori .loc [ori ["temppr"].str .contains (OO0OOO0OOO000O0OO ,na =False )].copy ()#line:1371
    del ori ["temppr"]#line:1372
    ori =ori .reset_index (drop =True )#line:1374
    text .insert (END ,"\n内部数据规整完毕。\n")#line:1375
def Tpo (O000OOO00O000OO0O ,O00O00000O0O0000O ,OOOOOO000000OOOOO ,O0OOO0OO0000O00O0 ,OOO0O0O00O00000O0 ,OOO000O0OOO00O00O ):#line:1378
    ""#line:1379
    O000OOO00O000OO0O =O000OOO00O000OO0O .astype (float )#line:1380
    O00O00000O0O0000O =tuple (float (OO000000O0O0OO000 )for OO000000O0O0OO000 in O00O00000O0O0000O )#line:1381
    O0OOO0O00O0O00O0O =Toplevel ()#line:1382
    O0OOO0O00O0O00O0O .title (OOO000O0OOO00O00O )#line:1383
    OOOO0000O00OO0O0O =ttk .Frame (O0OOO0O00O0O00O0O ,height =20 )#line:1384
    OOOO0000O00OO0O0O .pack (side =TOP )#line:1385
    OOOO0O00O0OOOO0OO =0.2 #line:1387
    OOO00OO00OO0O00O0 =Figure (figsize =(12 ,6 ),dpi =100 )#line:1388
    OO0OOO0O0O0O0OO00 =FigureCanvasTkAgg (OOO00OO00OO0O00O0 ,master =O0OOO0O00O0O00O0O )#line:1389
    OO0OOO0O0O0O0OO00 .draw ()#line:1390
    OO0OOO0O0O0O0OO00 .get_tk_widget ().pack (expand =1 )#line:1391
    OO0OO0OOO0O00OO00 =OOO00OO00OO0O00O0 .add_subplot (111 )#line:1392
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1394
    O00OOOO0OO0OO0O0O =NavigationToolbar2Tk (OO0OOO0O0O0O0OO00 ,O0OOO0O00O0O00O0O )#line:1396
    O00OOOO0OO0OO0O0O .update ()#line:1397
    OO0OOO0O0O0O0OO00 .get_tk_widget ().pack ()#line:1399
    OOOO00O0OO00O00OO =range (0 ,len (OOOOOO000000OOOOO ),1 )#line:1400
    OO0OO0OOO0O00OO00 .set_xticklabels (OOOOOO000000OOOOO ,rotation =-90 ,fontsize =8 )#line:1403
    OO0OO0OOO0O00OO00 .bar (OOOO00O0OO00O00OO ,O000OOO00O000OO0O ,align ="center",tick_label =OOOOOO000000OOOOO ,label =O0OOO0OO0000O00O0 )#line:1407
    OO0OO0OOO0O00OO00 .bar (OOOO00O0OO00O00OO ,O00O00000O0O0000O ,align ="center",label =OOO0O0O00O00000O0 )#line:1408
    OO0OO0OOO0O00OO00 .set_title (OOO000O0OOO00O00O )#line:1409
    OO0OO0OOO0O00OO00 .set_xlabel ("项")#line:1410
    OO0OO0OOO0O00OO00 .set_ylabel ("数量")#line:1411
    OOO00OO00OO0O00O0 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1414
    O0O0OOO00O0O0OOO0 =OO0OO0OOO0O00OO00 .get_position ()#line:1415
    OO0OO0OOO0O00OO00 .set_position ([O0O0OOO00O0O0OOO0 .x0 ,O0O0OOO00O0O0OOO0 .y0 ,O0O0OOO00O0O0OOO0 .width *0.7 ,O0O0OOO00O0O0OOO0 .height ])#line:1416
    OO0OO0OOO0O00OO00 .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1417
    OO0OOO0O0O0O0OO00 .draw ()#line:1419
def helper ():#line:1422
    ""#line:1423
    O0OO0000O00O00OOO =Toplevel ()#line:1424
    O0OO0000O00O00OOO .title ("程序使用帮助")#line:1425
    O0OO0000O00O00OOO .geometry ("700x500")#line:1426
    O0OO0O0000OOO0000 =Scrollbar (O0OO0000O00O00OOO )#line:1428
    O0O00OOOO00OOOOOO =Text (O0OO0000O00O00OOO ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1429
    O0OO0O0000OOO0000 .pack (side =RIGHT ,fill =Y )#line:1430
    O0O00OOOO00OOOOOO .pack ()#line:1431
    O0OO0O0000OOO0000 .config (command =O0O00OOOO00OOOOOO .yview )#line:1432
    O0O00OOOO00OOOOOO .config (yscrollcommand =O0OO0O0000OOO0000 .set )#line:1433
    O0O00OOOO00OOOOOO .insert (END ,"\n                                             帮助文件\n\n\n为帮助用户快速熟悉“阅易评”使用方法，现以医疗器械不良事件报告表为例，对使用步骤作以下说明：\n\n第一步：原始数据准备\n用户登录国家医疗器械不良事件监测信息系统（https://maers.adrs.org.cn/），在“个例不良事件管理—报告浏览”页面，选择本次评估的报告范围（时间、报告状态、事发地监测机构等）后进行查询和导出。\n●注意：国家医疗器械不良事件监测信息系统设置每次导出数据上限为5000份报告，如查询发现需导出报告数量超限，需分次导出；如导出数据为压缩包，需先行解压。如原始数据在多个文件夹内，需先行整理到统一文件夹中，方便下一步操作。\n\n第二步：原始数据导入\n用户点击“导入原始数据”按钮，在弹出数据导入框中找到原始数据存储位置，本程序支持导入多个原始数据文件，可在长按键盘“Ctrl”按键的同时分别点击相关文件，选择完毕后点击“打开”按钮，程序会提示“数据读取成功”或“导入文件错误”。\n●注意：基于当前评估工作需要，仅针对使用单位报告进行评估，故导入数据时仅选择“使用单位、经营企业医疗器械不良事件报告”，不支持与“上市许可持有人医疗器械不良事件报告”混选。如提示“导入文件错误，请重试”，请重启程序并重新操作，如仍提示错误可与开发者联系（联系方式见文末）。\n\n第三步：报告抽样分组\n用户点击“随机抽样分组”按钮，在“随机抽样及随机分组”弹窗中：\n1、根据评估目的，在“评估对象”处勾选相应选项，可根据选项对上报单位（医疗机构）、县（区）、地市实施评估。注意：如果您是省级用户，被评估对象是各地市，您要关闭本软件，修改好配置表文件夹“0（范例）质量评估.xls”中的“地市列表”单元表，将本省地市参照范例填好再运行本软件。如果被评估对象不是选择“地市”，则无需该项操作。\n2、根据报告伤害类型依次输入需抽取的比例或报告数量。程序默认此处输入数值小于1（含1）为抽取比例，输入数值大于1为抽取报告数量，用户根据实际情况任选一种方式即可。本程序支持不同伤害类型报告选用不同抽样方式。\n3、根据参与评估专家数量，在“抽样后随机分组数”输入对应数字。\n4、抽样方法有2种，一种是最大覆盖，即对每个评估对象按抽样数量/比例进行单独抽样，如遇到不足则多抽（所以总体实际抽样数量可能会比设置的多一点），每个评估对象都会被抽到；另外一种是总体随机，即按照设定的参数从总体中随机抽取（有可能部分评估对象没有被抽到）。\n用户在确定抽样分组内容全部正确录入后，点击“最大覆盖”或者“总体随机”按钮，根据程序提示选择保存地址。程序将按照专家数量将抽取的报告进行随即分配，生成对应份数的“专家评分表”，专家评分表包含评分项、详细描述、评分、满分、打分标准等。专家评分表自动隐藏报告单位等信息，用户可随机将评分表派发给专家进行评分。\n●注意：为保护数据同时便于专家查看，需对专家评分表进行格式设置，具体操作如下（或者直接使用格式刷一键完成，模板详见配置表-专家模板）：全选表格，右键-设置单元格格式-对齐，勾选自动换行，之后设置好列间距。此外，请勿修改“专家评分表“和“（最终评分需导入）被抽出的所有数据”两类工作文件的文件名。\n\n第四步：评估得分统计\n用户在全部专家完成评分后，将所有专家评分表放置在同一文件夹中，点击“评估得分统计”按钮，全选所有专家评分表和“（最终评分需导入）被抽出的所有数据”这个文件，后点击“打开”，程序将首先进行评分内容校验，对于打分错误报告给与提示并生成错误定位文件，需根据提示修正错误再全部导入。如打分项无误，程序将提示“打分表导入成功，正在统计请耐心等待”，并生成最终的评分结果。\n\n本程序由广东省药品不良反应监测中心和佛山市药品不良反应监测中心共同制作，其他贡献单位包括广州市药品不良反应监测中心、深圳市药物警戒和风险管理研究院等。如有疑问，请联系我们：\n评估标准相关问题：广东省药品不良反应监测中心 张博涵 020-37886057\n程序运行相关问题：佛山市药品不良反应监测中心 蔡权周 0757-82580815 \n\n",)#line:1437
    O0O00OOOO00OOOOOO .config (state =DISABLED )#line:1439
def TeasyreadT (O00O0O00OOO0O00O0 ):#line:1442
    ""#line:1443
    O00O0O00OOO0O00O0 ["#####分隔符#########"]="######################################################################"#line:1446
    OOO0O0O000OOOOOOO =O00O0O00OOO0O00O0 .stack (dropna =False )#line:1447
    OOO0O0O000OOOOOOO =pd .DataFrame (OOO0O0O000OOOOOOO ).reset_index ()#line:1448
    OOO0O0O000OOOOOOO .columns =["序号","条目","详细描述"]#line:1449
    OOO0O0O000OOOOOOO ["逐条查看"]="逐条查看"#line:1450
    return OOO0O0O000OOOOOOO #line:1451
def Tget_list (O000OO0O000O0O0O0 ):#line:1456
    ""#line:1457
    O000OO0O000O0O0O0 =str (O000OO0O000O0O0O0 )#line:1458
    OO0O00OOOOO000OOO =[]#line:1459
    OO0O00OOOOO000OOO .append (O000OO0O000O0O0O0 )#line:1460
    OO0O00OOOOO000OOO =",".join (OO0O00OOOOO000OOO )#line:1461
    OO0O00OOOOO000OOO =OO0O00OOOOO000OOO .split (",")#line:1462
    OO0O00OOOOO000OOO =",".join (OO0O00OOOOO000OOO )#line:1463
    OO0O00OOOOO000OOO =OO0O00OOOOO000OOO .split ("，")#line:1464
    OOO00OOOO0OO00OOO =OO0O00OOOOO000OOO [:]#line:1465
    OO0O00OOOOO000OOO =list (set (OO0O00OOOOO000OOO ))#line:1466
    OO0O00OOOOO000OOO .sort (key =OOO00OOOO0OO00OOO .index )#line:1467
    return OO0O00OOOOO000OOO #line:1468
def thread_it (O0O0OOO00O00O00O0 ,*O0O00O00O00O0O00O ):#line:1471
    ""#line:1472
    O0O0O0O0OO00OO0OO =threading .Thread (target =O0O0OOO00O00O00O0 ,args =O0O00O00O00O0O00O )#line:1474
    O0O0O0O0OO00OO0OO .setDaemon (True )#line:1476
    O0O0O0O0OO00OO0OO .start ()#line:1478
def showWelcome ():#line:1481
    ""#line:1482
    O0O000O0OOO00O000 =roox .winfo_screenwidth ()#line:1483
    OO000000000000000 =roox .winfo_screenheight ()#line:1485
    roox .overrideredirect (True )#line:1487
    roox .attributes ("-alpha",1 )#line:1488
    O00000OOOO0O00O0O =(O0O000O0OOO00O000 -475 )/2 #line:1489
    O0OO00OO0O0O00OO0 =(OO000000000000000 -200 )/2 #line:1490
    roox .geometry ("675x140+%d+%d"%(O00000OOOO0O00O0O ,O0OO00OO0O0O00OO0 ))#line:1492
    roox ["bg"]="royalblue"#line:1493
    O0OO0O00OOO000O0O =Label (roox ,text ="阅易评",fg ="white",bg ="royalblue",font =("微软雅黑",35 ))#line:1496
    O0OO0O00OOO000O0O .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1497
    O00O0O0O0OOOO0O0O =Label (roox ,text ="                                 广东省药品不良反应监测中心                         V"+version_now ,fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1504
    O00O0O0O0OOOO0O0O .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1505
def closeWelcome ():#line:1508
    ""#line:1509
    for O000O0OO000OOOOOO in range (2 ):#line:1510
        root .attributes ("-alpha",0 )#line:1511
        time .sleep (1 )#line:1512
    root .attributes ("-alpha",1 )#line:1513
    roox .destroy ()#line:1514
root =Tk ()#line:1518
root .title ("阅易评 V"+version_now )#line:1519
try :#line:1520
    root .iconphoto (True ,PhotoImage (file =peizhidir +"0（范例）ico.png"))#line:1521
except :#line:1522
    pass #line:1523
sw_root =root .winfo_screenwidth ()#line:1524
sh_root =root .winfo_screenheight ()#line:1526
ww_root =700 #line:1528
wh_root =620 #line:1529
x_root =(sw_root -ww_root )/2 #line:1531
y_root =(sh_root -wh_root )/2 #line:1532
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1533
root .configure (bg ="steelblue")#line:1534
try :#line:1537
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1538
    frame0 .pack (side =LEFT )#line:1539
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,0 ),)#line:1552
    B_open_files1 .pack ()#line:1553
    B_open_files3 =Button (frame0 ,text ="随机抽样分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tchouyang ,ori ),)#line:1566
    B_open_files3 .pack ()#line:1567
    B_open_files3 =Button (frame0 ,text ="评估得分统计",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tpinggu ),)#line:1580
    B_open_files3 .pack ()#line:1581
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ),)#line:1594
    B_open_files3 .pack ()#line:1595
    B_open_files1 =Button (frame0 ,text ="更改评分标准",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,123 ),)#line:1607
    B_open_files1 =Button (frame0 ,text ="内置数据清洗",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Txuanze ),)#line:1621
    if usergroup =="用户组=1":#line:1622
        B_open_files1 .pack ()#line:1623
    B_open_files1 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1635
    if usergroup =="用户组=0":#line:1636
        B_open_files1 .pack ()#line:1637
except :#line:1639
    pass #line:1640
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1644
text .pack ()#line:1645
text .insert (END ,"\n    欢迎使用“阅易评”，本程序由广东省药品不良反应监测中心联合佛山市药品不良反应监测中心开发，主要功能包括：\n    1、根据报告伤害类型和用户自定义抽样比例对报告表随机抽样；\n    2、根据评估专家数量对抽出报告表随机分组，生成专家评分表；\n    3、根据专家最终评分实现自动汇总统计。\n    本程序供各监测机构免费使用，使用前请先查看帮助文件。\n  \n版本功能更新日志：\n2022年6月1日  支持医疗器械不良事件报告表质量评估(上报部分)。\n2022年10月31日  支持药品不良反应报告表质量评估。  \n2023年4月6日  支持化妆品不良反应报告表质量评估。\n2023年6月9日  支持医疗器械不良事件报告表质量评估(调查评价部分)。\n\n缺陷修正：20230609 修正结果列排序（按评分项目排序）。\n\n注：化妆品质量评估仅支持第一怀疑化妆品。",)#line:1650
text .insert (END ,"\n\n")#line:1651
setting_cfg =read_setting_cfg ()#line:1657
generate_random_file ()#line:1658
setting_cfg =open_setting_cfg ()#line:1659
if setting_cfg ["settingdir"]==0 :#line:1660
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1661
    filepathu =filedialog .askdirectory ()#line:1662
    path =get_directory_path (filepathu )#line:1663
    update_setting_cfg ("settingdir",path )#line:1664
setting_cfg =open_setting_cfg ()#line:1665
random_number =int (setting_cfg ["sidori"])#line:1666
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1667
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1668
sid =random_number *2 +183576 #line:1669
if input_number ==sid and day_end =="未过期":#line:1670
    usergroup ="用户组=1"#line:1671
    text .insert (END ,usergroup +"   有效期至：")#line:1672
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1673
else :#line:1674
    text .insert (END ,usergroup )#line:1675
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1676
peizhidir =str (setting_cfg ["settingdir"])+csdir .split ("pinggutools")[0 ][-1 ]#line:1677
aaass =update_software ("pinggutools")#line:1678
text .insert (END ,aaass )#line:1679
roox =Toplevel ()#line:1682
tMain =threading .Thread (target =showWelcome )#line:1683
tMain .start ()#line:1684
t1 =threading .Thread (target =closeWelcome )#line:1685
t1 .start ()#line:1686
root .lift ()#line:1687
root .attributes ("-topmost",True )#line:1688
root .attributes ("-topmost",False )#line:1689
root .mainloop ()#line:1690
