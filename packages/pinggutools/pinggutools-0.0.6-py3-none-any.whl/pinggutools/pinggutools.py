#!/usr/bin/env python
# coding: utf-8
# 阅易评
# 开发人：蔡权周，张博涵
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
version_now ="0.0.6"#line:57
usergroup ="用户组=0"#line:58
setting_cfg =""#line:59
csdir =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:60
def extract_zip_file (O0O0O00O0OO00O0OO ,O00O00OOO00O000O0 ):#line:68
    import zipfile #line:70
    if O00O00OOO00O000O0 =="":#line:71
        return 0 #line:72
    with zipfile .ZipFile (O0O0O00O0OO00O0OO ,'r')as O0OO0OOOO000000OO :#line:73
        for OO0OOOOOO0O0O0O00 in O0OO0OOOO000000OO .infolist ():#line:74
            OO0OOOOOO0O0O0O00 .filename =OO0OOOOOO0O0O0O00 .filename .encode ('cp437').decode ('gbk')#line:76
            O0OO0OOOO000000OO .extract (OO0OOOOOO0O0O0O00 ,O00O00OOO00O000O0 )#line:77
def get_directory_path (O0O00OOOO0000OOO0 ):#line:83
    global csdir #line:85
    if not (os .path .isfile (os .path .join (O0O00OOOO0000OOO0 ,'0（范例）质量评估.xls'))):#line:87
        extract_zip_file (csdir +"def.py",O0O00OOOO0000OOO0 )#line:92
    if O0O00OOOO0000OOO0 =="":#line:94
        quit ()#line:95
    return O0O00OOOO0000OOO0 #line:96
def convert_and_compare_dates (O0O0O00O00000O0OO ):#line:100
    import datetime #line:101
    O000O00000OO00000 =datetime .datetime .now ()#line:102
    try :#line:104
       OOOO00OO0OO0O00OO =datetime .datetime .strptime (str (int (int (O0O0O00O00000O0OO )/4 )),"%Y%m%d")#line:105
    except :#line:106
        print ("fail")#line:107
        return "已过期"#line:108
    if OOOO00OO0OO0O00OO >O000O00000OO00000 :#line:110
        return "未过期"#line:112
    else :#line:113
        return "已过期"#line:114
def read_setting_cfg ():#line:116
    global csdir #line:117
    if os .path .exists (csdir +'setting.cfg'):#line:119
        text .insert (END ,"已完成初始化\n")#line:120
        with open (csdir +'setting.cfg','r')as O000O0OOOO00000O0 :#line:121
            OO0O0OOOOOOO0OO0O =eval (O000O0OOOO00000O0 .read ())#line:122
    else :#line:123
        O0OOOO00O00O00OO0 =csdir +'setting.cfg'#line:125
        with open (O0OOOO00O00O00OO0 ,'w')as O000O0OOOO00000O0 :#line:126
            O000O0OOOO00000O0 .write ('{"settingdir": 0, "sidori": 0, "sidfinal": "11111180000808"}')#line:127
        text .insert (END ,"未初始化，正在初始化...\n")#line:128
        OO0O0OOOOOOO0OO0O =read_setting_cfg ()#line:129
    return OO0O0OOOOOOO0OO0O #line:130
def open_setting_cfg ():#line:133
    global csdir #line:134
    with open (csdir +"setting.cfg","r")as OOO00000000O00O00 :#line:136
        O00O0O00OO0O00000 =eval (OOO00000000O00O00 .read ())#line:138
    return O00O0O00OO0O00000 #line:139
def update_setting_cfg (OO0O0O0OOO00OOOO0 ,O00O0000OO0O00000 ):#line:141
    global csdir #line:142
    with open (csdir +"setting.cfg","r")as O00OO0O0OOO00O00O :#line:144
        O00OO000OOO0OO00O =eval (O00OO0O0OOO00O00O .read ())#line:146
    if O00OO000OOO0OO00O [OO0O0O0OOO00OOOO0 ]==0 or O00OO000OOO0OO00O [OO0O0O0OOO00OOOO0 ]=="11111180000808":#line:148
        O00OO000OOO0OO00O [OO0O0O0OOO00OOOO0 ]=O00O0000OO0O00000 #line:149
        with open (csdir +"setting.cfg","w")as O00OO0O0OOO00O00O :#line:151
            O00OO0O0OOO00O00O .write (str (O00OO000OOO0OO00O ))#line:152
def generate_random_file ():#line:155
    O0O000O00OO00OOO0 =random .randint (200000 ,299999 )#line:157
    update_setting_cfg ("sidori",O0O000O00OO00OOO0 )#line:159
def display_random_number ():#line:161
    global csdir #line:162
    OO0OO0O0OOO00O00O =Toplevel ()#line:163
    OO0OO0O0OOO00O00O .title ("ID")#line:164
    O000OO000O00OO000 =OO0OO0O0OOO00O00O .winfo_screenwidth ()#line:166
    OO00O00000OO0OOO0 =OO0OO0O0OOO00O00O .winfo_screenheight ()#line:167
    OO00OOOOO00O0OOOO =80 #line:169
    O000O0000O00000OO =70 #line:170
    O00OOOOOOOOOO0O0O =(O000OO000O00OO000 -OO00OOOOO00O0OOOO )/2 #line:172
    O0OO0000OOO00O0OO =(OO00O00000OO0OOO0 -O000O0000O00000OO )/2 #line:173
    OO0OO0O0OOO00O00O .geometry ("%dx%d+%d+%d"%(OO00OOOOO00O0OOOO ,O000O0000O00000OO ,O00OOOOOOOOOO0O0O ,O0OO0000OOO00O0OO ))#line:174
    with open (csdir +"setting.cfg","r")as OO00O00O0OO00OO0O :#line:177
        O0000O0O0O0OO0000 =eval (OO00O00O0OO00OO0O .read ())#line:179
    OO0O00O0O0O0OOO00 =int (O0000O0O0O0OO0000 ["sidori"])#line:180
    OOOOO000O0O00000O =OO0O00O0O0O0OOO00 *2 +183576 #line:181
    print (OOOOO000O0O00000O )#line:183
    OOO000OO0OO0O0000 =ttk .Label (OO0OO0O0OOO00O00O ,text =f"机器码: {OO0O00O0O0O0OOO00}")#line:185
    O0000O00000OO0OOO =ttk .Entry (OO0OO0O0OOO00O00O )#line:186
    OOO000OO0OO0O0000 .pack ()#line:189
    O0000O00000OO0OOO .pack ()#line:190
    ttk .Button (OO0OO0O0OOO00O00O ,text ="验证",command =lambda :check_input (O0000O00000OO0OOO .get (),OOOOO000O0O00000O )).pack ()#line:194
def check_input (O0OOO0000O000O0OO ,O000O0O00O0OOO0O0 ):#line:196
    try :#line:200
        OO000000OOOO0O00O =int (str (O0OOO0000O000O0OO )[0 :6 ])#line:201
        O00O000O000OO0O00 =convert_and_compare_dates (str (O0OOO0000O000O0OO )[6 :14 ])#line:202
    except :#line:203
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:204
        return 0 #line:205
    if OO000000OOOO0O00O ==O000O0O00O0OOO0O0 and O00O000O000OO0O00 =="未过期":#line:207
        update_setting_cfg ("sidfinal",O0OOO0000O000O0OO )#line:208
        showinfo (title ="提示",message ="注册成功,请重新启动程序。")#line:209
        quit ()#line:210
    else :#line:211
        showinfo (title ="提示",message ="不匹配，注册失败。")#line:212
def update_software (O0O00O00OOO0O000O ):#line:217
    global version_now #line:219
    text .insert (END ,"当前版本为："+version_now +",正在检查更新...(您可以同时执行分析任务)")#line:220
    try :#line:221
        OO00OO00O0O00000O =requests .get (f"https://pypi.org/pypi/{O0O00O00OOO0O000O}/json",timeout =2 ).json ()["info"]["version"]#line:222
    except :#line:223
        return "...更新失败。"#line:224
    if OO00OO00O0O00000O >version_now :#line:225
        text .insert (END ,"\n最新版本为："+OO00OO00O0O00000O +",正在尝试自动更新....")#line:226
        pip .main (['install',O0O00O00OOO0O000O ,'--upgrade'])#line:228
        text .insert (END ,"\n您可以开展工作。")#line:229
        return "...更新成功。"#line:230
def Topentable (OOO00O000O000OO00 ):#line:233
    ""#line:234
    global ori #line:235
    global biaozhun #line:236
    global dishi #line:237
    O0OOO0O000OO0OO0O =[]#line:238
    OOO0O00O00O00O0OO =[]#line:239
    OO0OOOOOO0O0000O0 =1 #line:240
    if OOO00O000O000OO00 ==123 :#line:243
        try :#line:244
            O0000O0000O00000O =filedialog .askopenfilename (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:247
            biaozhun =pd .read_excel (O0000O0000O00000O ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:250
        except :#line:251
            showinfo (title ="提示",message ="配置表文件有误或您没有选择。")#line:252
            return 0 #line:253
        try :#line:254
            dishi =pd .read_excel (O0000O0000O00000O ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:257
        except :#line:258
            showinfo (title ="提示",message ="您选择的配置文件没有地市列表或您没有选择。")#line:259
            return 0 #line:260
        if ("评分项"in biaozhun .columns and "打分标准"in biaozhun .columns and "专家序号"not in biaozhun .columns ):#line:265
            text .insert (END ,"\n您使用自定义的配置表。")#line:266
            text .see (END )#line:267
            showinfo (title ="提示",message ="您将使用自定义的配置表。")#line:268
            return 0 #line:269
        else :#line:270
            showinfo (title ="提示",message ="配置表文件有误，请正确选择。")#line:271
            biaozhun =""#line:272
            return 0 #line:273
    try :#line:276
        if OOO00O000O000OO00 !=1 :#line:277
            O0000O0OO0OO00O0O =filedialog .askopenfilenames (filetypes =[("XLS",".xls"),("XLSX",".xlsx")])#line:280
        if OOO00O000O000OO00 ==1 :#line:281
            O0000O0OO0OO00O0O =filedialog .askopenfilenames (filetypes =[("XLSX",".xlsx"),("XLS",".xls")])#line:284
            for OO0OOOO0O000OO0OO in O0000O0OO0OO00O0O :#line:285
                if ("●专家评分表"in OO0OOOO0O000OO0OO )and ("●(最终评分需导入)被抽出的所有数据.xls"not in OO0OOOO0O000OO0OO ):#line:286
                    O0OOO0O000OO0OO0O .append (OO0OOOO0O000OO0OO )#line:287
                elif "●(最终评分需导入)被抽出的所有数据.xls"in OO0OOOO0O000OO0OO :#line:288
                    OOO0O00O00O00O0OO .append (OO0OOOO0O000OO0OO )#line:289
                    O0O00000OOO0O000O =OO0OOOO0O000OO0OO .replace ("●(最终评分需导入)被抽出的所有数据","分数错误信息")#line:290
                    OO0OOOOOO0O0000O0 =0 #line:291
            if OO0OOOOOO0O0000O0 ==1 :#line:292
                showinfo (title ="提示",message ="请一并导入以下文件：●(最终评分需导入)被抽出的所有数据.xls")#line:294
                return 0 #line:295
            O0000O0OO0OO00O0O =O0OOO0O000OO0OO0O #line:296
        OO0000OOOOO00000O =[pd .read_excel (O00OOO0O00O0OOO0O ,header =0 ,sheet_name =0 )for O00OOO0O00O0OOO0O in O0000O0OO0OO00O0O ]#line:299
        ori =pd .concat (OO0000OOOOO00000O ,ignore_index =True ).drop_duplicates ().reset_index (drop =True )#line:300
        if "报告编码"in ori .columns or "报告表编码"in ori .columns :#line:302
            ori =ori .fillna ("-未填写-")#line:303
        if "报告类型-新的"in ori .columns :#line:306
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:309
            ori ["报告编码"]=ori ["报告表编码"]#line:310
            text .insert (END ,"检测到导入的文件为药品报告，正在进行兼容性数据规整，请稍后...")#line:311
            ori =ori .rename (columns ={"医院名称":"单位名称"})#line:312
            ori =ori .rename (columns ={"报告地区名称":"使用单位、经营企业所属监测机构"})#line:313
            ori =ori .rename (columns ={"报告类型-严重程度":"伤害"})#line:314
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:315
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:316
            ori .loc [(ori ["不良反应结果"]=="死亡"),"伤害"]="死亡"#line:317
            ori ["上报单位所属地区"]=ori ["使用单位、经营企业所属监测机构"]#line:318
            try :#line:319
                ori ["报告编码"]=ori ["唯一标识"]#line:320
            except :#line:321
                pass #line:322
            ori ["药品信息"]=""#line:326
            OOOOO00O00O0OO0OO =0 #line:327
            OOOO0O0O00O00O000 =len (ori ["报告编码"].drop_duplicates ())#line:328
            for O000OO0000000OO00 in ori ["报告编码"].drop_duplicates ():#line:329
                OOOOO00O00O0OO0OO =OOOOO00O00O0OO0OO +1 #line:330
                O0OOO0O00O000O0OO =round (OOOOO00O00O0OO0OO /OOOO0O0O00O00O000 ,2 )#line:331
                try :#line:332
                    change_schedule (OOOOO00O00O0OO0OO ,OOOO0O0O00O00O000 )#line:333
                except :#line:334
                    if O0OOO0O00O000O0OO in [0.10 ,0.20 ,0.30 ,0.40 ,0.50 ,0.60 ,0.70 ,0.80 ,0.90 ,0.99 ]:#line:335
                        text .insert (END ,O0OOO0O00O000O0OO )#line:336
                        text .insert (END ,"...")#line:337
                O0O0OOO00OO00OO0O =ori [(ori ["报告编码"]==O000OO0000000OO00 )].sort_values (by =["药品序号"]).reset_index ()#line:339
                for O0O0O00OO00OOO00O ,O00O0OOO00OO00OO0 in O0O0OOO00OO00OO0O .iterrows ():#line:340
                    ori .loc [(ori ["报告编码"]==O00O0OOO00OO00OO0 ["报告编码"]),"药品信息"]=ori ["药品信息"]+"●药品序号："+str (O00O0OOO00OO00OO0 ["药品序号"])+" 性质："+str (O00O0OOO00OO00OO0 ["怀疑/并用"])+"\n批准文号:"+str (O00O0OOO00OO00OO0 ["批准文号"])+"\n商品名称："+str (O00O0OOO00OO00OO0 ["商品名称"])+"\n通用名称："+str (O00O0OOO00OO00OO0 ["通用名称"])+"\n剂型："+str (O00O0OOO00OO00OO0 ["剂型"])+"\n生产厂家："+str (O00O0OOO00OO00OO0 ["生产厂家"])+"\n生产批号："+str (O00O0OOO00OO00OO0 ["生产批号"])+"\n用量："+str (O00O0OOO00OO00OO0 ["用量"])+str (O00O0OOO00OO00OO0 ["用量单位"])+"，"+str (O00O0OOO00OO00OO0 ["用法-日"])+"日"+str (O00O0OOO00OO00OO0 ["用法-次"])+"次\n给药途径:"+str (O00O0OOO00OO00OO0 ["给药途径"])+"\n用药开始时间："+str (O00O0OOO00OO00OO0 ["用药开始时间"])+"\n用药终止时间："+str (O00O0OOO00OO00OO0 ["用药终止时间"])+"\n用药原因："+str (O00O0OOO00OO00OO0 ["用药原因"])+"\n"#line:341
            ori =ori .drop_duplicates ("报告编码")#line:342
        if "皮损部位"in ori .columns :#line:349
            biaozhun =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:352
            ori ["报告编码"]=ori ["报告表编号"]#line:353
            text .insert (END ,"检测到导入的文件为化妆品报告，正在进行兼容性数据规整，请稍后...")#line:354
            ori ["报告地区名称"]=ori ["报告单位名称"].astype (str )#line:356
            ori ["单位名称"]=ori ["报告单位名称"].astype (str )#line:358
            ori ["伤害"]=ori ["报告类型"].astype (str )#line:359
            ori ["伤害"]=ori ["伤害"].str .replace ("一般","其他",regex =False )#line:360
            ori ["伤害"]=ori ["伤害"].str .replace ("严重","严重伤害",regex =False )#line:361
            ori ["上报单位所属地区"]=ori ["报告地区名称"]#line:363
            try :#line:364
                ori ["报告编码"]=ori ["唯一标识"]#line:365
            except :#line:366
                pass #line:367
            text .insert (END ,"\n正在开展化妆品注册单位规整...")#line:368
            OO0O0000O00O0O000 =pd .read_excel (peizhidir +"0（范例）注册单位.xlsx",sheet_name ="机构列表",header =0 ,index_col =0 ,).reset_index ()#line:369
            for O0O0O00OO00OOO00O ,O00O0OOO00OO00OO0 in OO0O0000O00O0O000 .iterrows ():#line:371
                ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["中文全称"]),"监测机构"]=O00O0OOO00OO00OO0 ["归属地区"]#line:372
                ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["中文全称"]),"市级监测机构"]=O00O0OOO00OO00OO0 ["地市"]#line:373
            ori ["监测机构"]=ori ["监测机构"].fillna ("未规整")#line:374
            ori ["市级监测机构"]=ori ["市级监测机构"].fillna ("未规整")#line:375
        try :#line:378
                text .insert (END ,"\n开展报告单位和监测机构名称规整...")#line:379
                O00OOOOOO0O0OOO00 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="报告单位",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:380
                OO0O0000O00O0O000 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="监测机构",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:381
                OO0OOOOO000000000 =pd .read_excel (peizhidir +"0（范例）上报单位.xls",sheet_name ="地市清单",header =0 ,index_col =0 ,).fillna ("没有定义好X").reset_index ()#line:382
                for O0O0O00OO00OOO00O ,O00O0OOO00OO00OO0 in O00OOOOOO0O0OOO00 .iterrows ():#line:383
                        ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["曾用名1"]),"单位名称"]=O00O0OOO00OO00OO0 ["单位名称"]#line:384
                        ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["曾用名2"]),"单位名称"]=O00O0OOO00OO00OO0 ["单位名称"]#line:385
                        ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["曾用名3"]),"单位名称"]=O00O0OOO00OO00OO0 ["单位名称"]#line:386
                        ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["曾用名4"]),"单位名称"]=O00O0OOO00OO00OO0 ["单位名称"]#line:387
                        ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["曾用名5"]),"单位名称"]=O00O0OOO00OO00OO0 ["单位名称"]#line:388
                        ori .loc [(ori ["单位名称"]==O00O0OOO00OO00OO0 ["单位名称"]),"使用单位、经营企业所属监测机构"]=O00O0OOO00OO00OO0 ["监测机构"]#line:391
                for O0O0O00OO00OOO00O ,O00O0OOO00OO00OO0 in OO0O0000O00O0O000 .iterrows ():#line:393
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==O00O0OOO00OO00OO0 ["曾用名1"]),"使用单位、经营企业所属监测机构"]=O00O0OOO00OO00OO0 ["监测机构"]#line:394
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==O00O0OOO00OO00OO0 ["曾用名2"]),"使用单位、经营企业所属监测机构"]=O00O0OOO00OO00OO0 ["监测机构"]#line:395
                        ori .loc [(ori ["使用单位、经营企业所属监测机构"]==O00O0OOO00OO00OO0 ["曾用名3"]),"使用单位、经营企业所属监测机构"]=O00O0OOO00OO00OO0 ["监测机构"]#line:396
                for OO0O0000000O0O000 in OO0OOOOO000000000 ["地市列表"]:#line:398
                        ori .loc [(ori ["上报单位所属地区"].str .contains (OO0O0000000O0O000 ,na =False )),"市级监测机构"]=OO0O0000000O0O000 #line:399
                ori .loc [(ori ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构"]="佛山"#line:400
        except :#line:402
                text .insert (END ,"\n报告单位和监测机构名称规整失败.")#line:403
    except :#line:405
        showinfo (title ="提示",message ="导入文件错误,请重试。")#line:406
        return 0 #line:407
    try :#line:410
        ori =ori .loc [:,~ori .columns .str .contains ("Unnamed")]#line:411
    except :#line:412
        pass #line:413
    try :#line:414
        ori ["报告编码"]=ori ["报告编码"].astype (str )#line:415
    except :#line:416
        pass #line:417
    ori =ori .sample (frac =1 ).copy ()#line:420
    ori .reset_index (inplace =True )#line:421
    text .insert (END ,"\n数据读取成功，行数："+str (len (ori )))#line:422
    text .see (END )#line:423
    if OOO00O000O000OO00 ==0 :#line:426
        if "报告编码"not in ori .columns :#line:427
            showinfo (title ="提示信息",message ="\n在校验过程中，发现您导入的并非原始报告数据，请重新导入。")#line:428
        else :#line:429
            showinfo (title ="提示信息",message ="\n数据读取成功。")#line:430
        return 0 #line:431
    O00O00OO0O00OOOO0 =ori .copy ()#line:434
    OO00000OO00O0O000 ={}#line:435
    OOOO0O0O00OOOO000 =0 #line:436
    if "专家序号"not in O00O00OO0O00OOOO0 .columns :#line:437
        showinfo (title ="提示信息",message ="您导入的并非专家评分文件，请重新导入。")#line:438
        return 0 #line:439
    for O0O0O00OO00OOO00O ,O00O0OOO00OO00OO0 in O00O00OO0O00OOOO0 .iterrows ():#line:440
        OOOOO000O0O00OOOO ="专家打分-"+str (O00O0OOO00OO00OO0 ["条目"])#line:441
        try :#line:442
            float (O00O0OOO00OO00OO0 ["评分"])#line:443
            float (O00O0OOO00OO00OO0 ["满分"])#line:444
        except :#line:445
            showinfo (title ="错误提示",message ="因专家评分或满分值输入的不是数字，导致了程序中止，请修正："+"专家序号："+str (int (O00O0OOO00OO00OO0 ["专家序号"]))+"，报告序号："+str (int (O00O0OOO00OO00OO0 ["序号"]))+O00O0OOO00OO00OO0 ["条目"],)#line:454
            ori =0 #line:455
        if float (O00O0OOO00OO00OO0 ["评分"])>float (O00O0OOO00OO00OO0 ["满分"])or float (O00O0OOO00OO00OO0 ["评分"])<0 :#line:456
            OO00000OO00O0O000 [str (O0O0O00OO00OOO00O )]=("专家序号："+str (int (O00O0OOO00OO00OO0 ["专家序号"]))+"；  报告序号："+str (int (O00O0OOO00OO00OO0 ["序号"]))+O00O0OOO00OO00OO0 ["条目"])#line:463
            OOOO0O0O00OOOO000 =1 #line:464
    if OOOO0O0O00OOOO000 ==1 :#line:466
        OO00O0OO0O000O0O0 =pd .DataFrame (list (OO00000OO00O0O000 .items ()),columns =["错误编号","错误信息"])#line:467
        del OO00O0OO0O000O0O0 ["错误编号"]#line:468
        OO00OO00OO000000O =O0O00000OOO0O000O #line:469
        OO00O0OO0O000O0O0 =OO00O0OO0O000O0O0 .sort_values (by =["错误信息"],ascending =True ,na_position ="last")#line:470
        OOO0O0OOOOOO00OOO =pd .ExcelWriter (OO00OO00OO000000O )#line:471
        OO00O0OO0O000O0O0 .to_excel (OOO0O0OOOOOO00OOO ,sheet_name ="字典数据")#line:472
        OOO0O0OOOOOO00OOO .close ()#line:473
        showinfo (title ="警告",message ="经检查，部分专家的打分存在错误。请您修正错误的打分文件再重新导入全部的专家打分文件。详见:分数错误信息.xls",)#line:477
        text .insert (END ,"\n经检查，部分专家的打分存在错误。详见:分数错误信息.xls。请您修正错误的打分文件再重新导入全部的专家打分文件。")#line:478
        text .insert (END ,"\n以下是错误信息概况：\n")#line:479
        text .insert (END ,OO00O0OO0O000O0O0 )#line:480
        text .see (END )#line:481
        return 0 #line:482
    if OOO00O000O000OO00 ==1 :#line:485
        return ori ,OOO0O00O00O00O0OO #line:486
def Tchouyang (OOO000000OO00OOO0 ):#line:489
    ""#line:490
    try :#line:492
        if OOO000000OO00OOO0 ==0 :#line:493
            showinfo (title ="提示",message ="您尚未导入原始数据。")#line:494
            return 0 #line:495
    except :#line:496
        pass #line:497
    if "详细描述"in OOO000000OO00OOO0 .columns :#line:498
        showinfo (title ="提示",message ="目前工作文件为专家评分文件，请导入原始数据进行抽样。")#line:499
        return 0 #line:500
    O00O0OO0O000OOOOO =Toplevel ()#line:503
    O00O0OO0O000OOOOO .title ("随机抽样及随机分组")#line:504
    O00OOOO0O00O000O0 =O00O0OO0O000OOOOO .winfo_screenwidth ()#line:505
    O0O0O0O0OO0OO0000 =O00O0OO0O000OOOOO .winfo_screenheight ()#line:507
    OOOOOOO00OO00OO00 =300 #line:509
    O0OOO0000OOO00O00 =220 #line:510
    O00OOO00OO00OOO0O =(O00OOOO0O00O000O0 -OOOOOOO00OO00OO00 )/1.7 #line:512
    OOOO00OO0OOOOOO0O =(O0O0O0O0OO0OO0000 -O0OOO0000OOO00O00 )/2 #line:513
    O00O0OO0O000OOOOO .geometry ("%dx%d+%d+%d"%(OOOOOOO00OO00OO00 ,O0OOO0000OOO00O00 ,O00OOO00OO00OOO0O ,OOOO00OO0OOOOOO0O ))#line:514
    O0OO000O0O00OO0O0 =Label (O00O0OO0O000OOOOO ,text ="评估对象：")#line:516
    O0OO000O0O00OO0O0 .grid (row =1 ,column =0 ,sticky ="w")#line:517
    O0O00OO0OO00000OO =StringVar ()#line:518
    OO0O0O0OOOOO00OO0 =ttk .Combobox (O00O0OO0O000OOOOO ,width =25 ,height =10 ,state ="readonly",textvariable =O0O00OO0OO00000OO )#line:521
    OO0O0O0OOOOO00OO0 ["values"]=["上报单位","县区","地市","省级审核人","上市许可持有人"]#line:522
    OO0O0O0OOOOO00OO0 .current (0 )#line:523
    OO0O0O0OOOOO00OO0 .grid (row =2 ,column =0 )#line:524
    OO00000000O0O00O0 =Label (O00O0OO0O000OOOOO ,text ="-----------------------------------------")#line:526
    OO00000000O0O00O0 .grid (row =3 ,column =0 ,sticky ="w")#line:527
    O0O0OO0OOO00OO000 =Label (O00O0OO0O000OOOOO ,text ="死亡报告抽样数量（>1)或比例(<=1)：")#line:529
    O0O0OO0OOO00OO000 .grid (row =4 ,column =0 ,sticky ="w")#line:530
    OOO0OOOOOOOOOOOOO =Entry (O00O0OO0O000OOOOO ,width =10 )#line:531
    OOO0OOOOOOOOOOOOO .grid (row =4 ,column =1 ,sticky ="w")#line:532
    O00O0O0O0O000OO0O =Label (O00O0OO0O000OOOOO ,text ="严重报告抽样数量（>1)或比例(<=1)：")#line:534
    O00O0O0O0O000OO0O .grid (row =6 ,column =0 ,sticky ="w")#line:535
    OO00OO00O000O0000 =Entry (O00O0OO0O000OOOOO ,width =10 )#line:536
    OO00OO00O000O0000 .grid (row =6 ,column =1 ,sticky ="w")#line:537
    O0O0O0OOO0O00000O =Label (O00O0OO0O000OOOOO ,text ="一般报告抽样数量（>1)或比例(<=1)：")#line:539
    O0O0O0OOO0O00000O .grid (row =8 ,column =0 ,sticky ="w")#line:540
    OOO00000OOO0OO0O0 =Entry (O00O0OO0O000OOOOO ,width =10 )#line:541
    OOO00000OOO0OO0O0 .grid (row =8 ,column =1 ,sticky ="w")#line:542
    OO00000000O0O00O0 =Label (O00O0OO0O000OOOOO ,text ="-----------------------------------------")#line:544
    OO00000000O0O00O0 .grid (row =9 ,column =0 ,sticky ="w")#line:545
    OOOOOO000O0OOOO0O =Label (O00O0OO0O000OOOOO ,text ="抽样后随机分组数（专家数量）：")#line:547
    O0OOOO00OO0O00OO0 =Entry (O00O0OO0O000OOOOO ,width =10 )#line:548
    OOOOOO000O0OOOO0O .grid (row =10 ,column =0 ,sticky ="w")#line:549
    O0OOOO00OO0O00OO0 .grid (row =10 ,column =1 ,sticky ="w")#line:550
    O0000OOO0000OOO0O =Button (O00O0OO0O000OOOOO ,text ="最大覆盖",width =12 ,command =lambda :thread_it (Tdoing0 ,OOO000000OO00OOO0 ,OOO00000OOO0OO0O0 .get (),OO00OO00O000O0000 .get (),OOO0OOOOOOOOOOOOO .get (),O0OOOO00OO0O00OO0 .get (),OO0O0O0OOOOO00OO0 .get (),"最大覆盖",1 ,),)#line:567
    O0000OOO0000OOO0O .grid (row =13 ,column =1 ,sticky ="w")#line:568
    OO00OO0O0OO00OO0O =Button (O00O0OO0O000OOOOO ,text ="总体随机",width =12 ,command =lambda :thread_it (Tdoing0 ,OOO000000OO00OOO0 ,OOO00000OOO0OO0O0 .get (),OO00OO00O000O0000 .get (),OOO0OOOOOOOOOOOOO .get (),O0OOOO00OO0O00OO0 .get (),OO0O0O0OOOOO00OO0 .get (),"总体随机",1 ))#line:569
    OO00OO0O0OO00OO0O .grid (row =13 ,column =0 ,sticky ='w')#line:570
def Tdoing0 (OOO00OO0O0000OO00 ,O00OOOOOO0000000O ,OO0OO0O0000O0O00O ,O0O0O0O00000OO000 ,O0OOOO0OO00O0O000 ,OO0OOO0O0OOO00O0O ,OOOO000OO0O00O00O ,OOO0OOO0O00O0O00O ):#line:576
    ""#line:577
    global dishi #line:578
    global biaozhun #line:579
    if (O00OOOOOO0000000O ==""or OO0OO0O0000O0O00O ==""or O0O0O0O00000OO000 ==""or O0OOOO0OO00O0O000 ==""or OO0OOO0O0OOO00O0O ==""or OOOO000OO0O00O00O ==""):#line:589
        showinfo (title ="提示信息",message ="参数设置不完整。")#line:590
        return 0 #line:591
    if OO0OOO0O0OOO00O0O =="上报单位":#line:592
        OO0OOO0O0OOO00O0O ="单位名称"#line:593
    if OO0OOO0O0OOO00O0O =="县区":#line:594
        OO0OOO0O0OOO00O0O ="使用单位、经营企业所属监测机构"#line:595
    if OO0OOO0O0OOO00O0O =="地市":#line:596
        OO0OOO0O0OOO00O0O ="市级监测机构"#line:597
    if OO0OOO0O0OOO00O0O =="省级审核人":#line:598
        OO0OOO0O0OOO00O0O ="审核人.1"#line:599
        OOO00OO0O0000OO00 ["modex"]=1 #line:600
        OOO00OO0O0000OO00 ["审核人.1"]=OOO00OO0O0000OO00 ["审核人.1"].fillna ("未填写")#line:601
    if OO0OOO0O0OOO00O0O =="上市许可持有人":#line:602
        OO0OOO0O0OOO00O0O ="上市许可持有人名称"#line:603
        OOO00OO0O0000OO00 ["modex"]=1 #line:604
        OOO00OO0O0000OO00 ["上市许可持有人名称"]=OOO00OO0O0000OO00 ["上市许可持有人名称"].fillna ("未填写")#line:605
    if OOO0OOO0O00O0O00O ==1 :#line:607
        if len (biaozhun )==0 :#line:608
            OO00OO000000000OO =peizhidir +"0（范例）质量评估.xls"#line:609
            try :#line:610
                if "modex"in OOO00OO0O0000OO00 .columns :#line:611
                    OOO0OO0OOO00O00O0 =pd .read_excel (OO00OO000000000OO ,sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:612
                else :#line:613
                    OOO0OO0OOO00O00O0 =pd .read_excel (OO00OO000000000OO ,sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:614
                text .insert (END ,"\n您使用配置表文件夹中的“0（范例）质量评估.xls“作为评分标准。")#line:615
                text .see (END )#line:616
            except :#line:619
                OOO0OO0OOO00O00O0 =pd .DataFrame ({"评分项":{0 :"识别代码",1 :"报告人",2 :"联系人",3 :"联系电话",4 :"注册证编号/曾用注册证编号",5 :"产品名称",6 :"型号和规格",7 :"产品批号和产品编号",8 :"生产日期",9 :"有效期至",10 :"事件发生日期",11 :"发现或获知日期",12 :"伤害",13 :"伤害表现",14 :"器械故障表现",15 :"年龄和年龄类型",16 :"性别",17 :"预期治疗疾病或作用",18 :"器械使用日期",19 :"使用场所和场所名称",20 :"使用过程",21 :"合并用药/械情况说明",22 :"事件原因分析和事件原因分析描述",23 :"初步处置情况",},"打分标准":{0 :"",1 :"填写人名或XX科室，得1分",2 :"填写报告填报人员姓名或XX科X医生，得1分",3 :"填写报告填报人员移动电话或所在科室固定电话，得1分",4 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得8分",5 :"可利用国家局数据库检索，注册证号与产品名称及事件描述相匹配的，得4分",6 :"规格和型号任填其一，且内容正确，得4分",7 :"产品批号和编号任填其一，且内容正确，,得4分。\n注意：（1）如果该器械使用年限久远，或在院外用械，批号或编号无法查询追溯的，报告表“使用过程”中给予说明的，得4分；（2）出现YZB格式、YY格式、GB格式等产品标准格式，或“XX生产许XX”等许可证号，得0分；（3）出现和注册证号一样的数字，得0分。",8 :"确保“生产日期”和“有效期至”逻辑正确，“有效期至”晚于“生产日期”，且两者时间间隔应为整月或整年，得2分。",9 :"确保生产日期和有效期逻辑正确。\n注意：如果该器械是使用年限久远的（2014年之前生产产品），或在院外用械，生产日期和有效期无法查询追溯的，并在报告表“使用过程”中给予说明的，该项得4分",10 :"指发生医疗器械不良事件的日期，应与使用过程描述一致，如仅知道事件发生年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。填写正确得2分。\n注意：“事件发生日期”早于“器械使用日期”的，得0分。",11 :"指报告单位发现或知悉该不良事件的日期，填写正确得5分。\n注意：“发现或获知日期”早于“事件发生日期”的，或者早于使用日期的，得0分。",12 :"分为“死亡”、“严重伤害”“其他”，判断正确，得8分。",13 :"描述准确且简明，或者勾选的术语贴切的，得6分；描述较为准确且简明，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成器械故障表现的，得0分。\n注意：对于“严重伤害”事件，需写明实际导致的严重伤害，填写不恰当的或填写“无”的，得0分。伤害表现描述与使用过程中关于伤害的描述不一致的，得0分。对于“其他”未对患者造成伤害的，该项可填“无”或未填写，默认得6分。",14 :"描述准确而简明，或者勾选的术语贴切的，得6分；描述较为准确，或选择术语较为贴切，或描述准确但不够简洁，得3分；描述冗长、填成伤害表现的，得0分。故障表现与使用过程中关于器械故障的描述不一致的，得0分。\n注意：对于不存在器械故障但仍然对患者造成了伤害的，在伤害表现处填写了对应伤害，该项填“无”，默认得6分。",15 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",16 :"医疗器械若未用于患者或者未造成患者伤害的，患者信息非必填项，默认得1分。",17 :"指涉及医疗器械的用途或适用范围，如治疗类医疗器械的预期治疗疾病，检验检查类、辅助治疗类医疗器械的预期作用等。填写完整准确，得4分；未填写、填写不完整或填写错误，得0分。",18 :"需与使用过程描述的日期一致，若器械使用日期和不良事件发生日期不是同一天，填成“不良事件发生日期”的，得0分；填成“有源设备启用日期”的，得0分。如仅知道事件使用年份，填写当年的1月1日；如仅知道年份和月份，填写当月的第1日；如年月日均未知，填写事件获知日期，并在“使用过程”给予说明。",19 :"使用场所为“医疗机构”的，场所名称可以为空，默认得2分；使用场所为“家庭”或“其他”，但勾选为医疗机构的，得0分；如使用场所为“其他”，没有填写实际使用场所或填写错误的，得0分。",20 :"按照以下四个要素进行评分：\n（1）具体操作使用情况（5分）\n详细描述具体操作人员资质、操作使用过程等信息，对于体外诊断医疗器械应填写患者诊疗信息（如疾病情况、用药情况）、样品检测过程与结果等信息。该要素描述准确完整的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（2）不良事件情况（5分）\n详细描述使用过程中出现的非预期结果等信息，对于体外诊断医疗器械应填写发现的异常检测情况，该要素描述完整准确的，得5分；较完整准确的，得2.5分；要素缺失的，得0分。\n（3）对受害者的影响（4分）\n详细描述该事件（可能）对患者造成的伤害，（可能）对临床诊疗造成的影响。有实际伤害的事件，需写明对受害者的伤害情况，包括必要的体征（如体温、脉搏、血压、皮损程度、失血情况等）和相关检查结果（如血小板检查结果）；对于可能造成严重伤害的事件，需写明可能对患者或其他人员造成的伤害。该要素描述完整准确的，得4分；较完整准确的，得2分；要素缺失的，得0分。\n（4）采取的治疗措施及结果（4分）\n有实际伤害的情况，须写明对伤者采取的治疗措施（包括用药、用械、或手术治疗等，及采取各个治疗的时间），以及采取治疗措施后的转归情况。该要素描述完整准确得4分，较完整准确得2分，描述过于笼统简单，如描述为“对症治疗”、“报告医生”、“转院”等，或者要素缺失的，得0分；无实际伤害的，该要素默认得4分。",21 :"有合并用药/械情况但没有填写此项的，得0分；填写不完整的，得2分；评估认为该不良事件过程中不存在合并用药/械情况的，该项不填写可得4分。\n如：输液泵泵速不准，合并用药/械情况应写明输注的药液、并用的输液器信息等。",22 :"原因分析不正确，如对于产品原因（包括说明书等）、操作原因 、患者自身原因 、无法确定的勾选与原因分析的描述的内容不匹配的，得0分，例如勾选了产品原因，但描述中说明该事件可能是未按照说明书要求进行操作导致（操作原因）；原因分析正确，但原因分析描述填成使用过程或者处置方式的，得2分。",23 :"包含产品的初步处置措施和对患者的救治措施等，填写完整得2分，部分完整得1分，填写过于简单得0分。",},"满分分值":{0 :0 ,1 :1 ,2 :1 ,3 :1 ,4 :8 ,5 :4 ,6 :4 ,7 :4 ,8 :2 ,9 :2 ,10 :2 ,11 :5 ,12 :8 ,13 :6 ,14 :6 ,15 :1 ,16 :1 ,17 :4 ,18 :2 ,19 :2 ,20 :18 ,21 :4 ,22 :4 ,23 :2 ,},})#line:701
                text .insert (END ,"\n您使用软件内置的评分标准。")#line:702
                text .see (END )#line:703
            try :#line:705
                dishi =pd .read_excel (OO00OO000000000OO ,sheet_name ="地市清单",header =0 ,index_col =0 ).reset_index ()#line:708
                text .insert (END ,"\n找到地市清单，将规整地市名称。")#line:709
                for OO0OOO0OOOOOO0000 in dishi ["地市列表"]:#line:710
                    OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["上报单位所属地区"].str .contains (OO0OOO0OOOOOO0000 ,na =False )),"市级监测机构",]=OO0OOO0OOOOOO0000 #line:714
                    OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:718
                    OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["市级监测机构"].str .contains ("北海",na =False )),"市级监测机构",]="北海"#line:725
                    OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["联系地址"].str .contains ("北海市",na =False )),"市级监测机构",]="北海"#line:729
                text .see (END )#line:730
            except :#line:731
                text .insert (END ,"\n未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。")#line:732
                text .see (END )#line:733
        else :#line:734
            OOO0OO0OOO00O00O0 =biaozhun .copy ()#line:735
            if len (dishi )!=0 :#line:736
                try :#line:737
                    text .insert (END ,"\n找到自定义的地市清单，将规整地市名称。")#line:738
                    for OO0OOO0OOOOOO0000 in dishi ["地市列表"]:#line:739
                        OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["使用单位、经营企业所属监测机构"].str .contains (OO0OOO0OOOOOO0000 ,na =False )),"市级监测机构",]=OO0OOO0OOOOOO0000 #line:743
                    OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["上报单位所属地区"].str .contains ("顺德",na =False )),"市级监测机构",]="佛山"#line:747
                    text .see (END )#line:748
                except TRD :#line:749
                    text .insert (END ,"\n导入的自定义配置表中，未找到地市清单或清单有误，不对地市名称进行规整，未维护产品的报表的地市名称将以“未填写”的形式展现。",)#line:753
                    text .see (END )#line:754
            text .insert (END ,"\n您使用了自己导入的配置表作为评分标准。")#line:755
            text .see (END )#line:756
    text .insert (END ,"\n正在抽样，请稍候...已完成30%")#line:757
    OOO00OO0O0000OO00 =OOO00OO0O0000OO00 .reset_index (drop =True )#line:758
    OOO00OO0O0000OO00 ["质量评估模式"]=OOO00OO0O0000OO00 [OO0OOO0O0OOO00O0O ]#line:761
    OOO00OO0O0000OO00 ["报告时限"]=""#line:762
    OOO00OO0O0000OO00 ["报告时限情况"]="超时报告"#line:763
    OOO00OO0O0000OO00 ["识别代码"]=range (0 ,len (OOO00OO0O0000OO00 ))#line:764
    try :#line:765
        OOO00OO0O0000OO00 ["报告时限"]=pd .to_datetime (OOO00OO0O0000OO00 ["报告日期"])-pd .to_datetime (OOO00OO0O0000OO00 ["发现或获知日期"])#line:768
        OOO00OO0O0000OO00 ["报告时限"]=OOO00OO0O0000OO00 ["报告时限"].dt .days #line:769
        OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["伤害"]=="死亡")&(OOO00OO0O0000OO00 ["报告时限"]<=7 ),"报告时限情况"]="死亡未超时，报告时限："+OOO00OO0O0000OO00 ["报告时限"].astype (str )#line:772
        OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["伤害"]=="严重伤害")&(OOO00OO0O0000OO00 ["报告时限"]<=20 ),"报告时限情况"]="严重伤害未超时，报告时限："+OOO00OO0O0000OO00 ["报告时限"].astype (str )#line:775
        OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["伤害"]=="其他")&(OOO00OO0O0000OO00 ["报告时限"]<=30 ),"报告时限情况"]="其他未超时，报告时限："+OOO00OO0O0000OO00 ["报告时限"].astype (str )#line:778
        OOO00OO0O0000OO00 .loc [(OOO00OO0O0000OO00 ["报告时限情况"]=="超时报告"),"报告时限情况"]="！疑似超时报告，报告时限："+OOO00OO0O0000OO00 ["报告时限"].astype (str )#line:781
        OOO00OO0O0000OO00 ["型号和规格"]=("型号："+OOO00OO0O0000OO00 ["型号"].astype (str )+"   \n规格："+OOO00OO0O0000OO00 ["规格"].astype (str ))#line:784
        OOO00OO0O0000OO00 ["产品批号和产品编号"]=("产品批号："+OOO00OO0O0000OO00 ["产品批号"].astype (str )+"   \n产品编号："+OOO00OO0O0000OO00 ["产品编号"].astype (str ))#line:790
        OOO00OO0O0000OO00 ["使用场所和场所名称"]=("使用场所："+OOO00OO0O0000OO00 ["使用场所"].astype (str )+"   \n场所名称："+OOO00OO0O0000OO00 ["场所名称"].astype (str ))#line:796
        OOO00OO0O0000OO00 ["年龄和年龄类型"]=("年龄："+OOO00OO0O0000OO00 ["年龄"].astype (str )+"   \n年龄类型："+OOO00OO0O0000OO00 ["年龄类型"].astype (str ))#line:802
        OOO00OO0O0000OO00 ["事件原因分析和事件原因分析描述"]=("事件原因分析："+OOO00OO0O0000OO00 ["事件原因分析"].astype (str )+"   \n事件原因分析描述："+OOO00OO0O0000OO00 ["事件原因分析描述"].astype (str ))#line:808
        OOO00OO0O0000OO00 ["是否开展了调查及调查情况"]=("是否开展了调查："+OOO00OO0O0000OO00 ["是否开展了调查"].astype (str )+"   \n调查情况："+OOO00OO0O0000OO00 ["调查情况"].astype (str ))#line:817
        OOO00OO0O0000OO00 ["控制措施情况"]=("是否已采取控制措施："+OOO00OO0O0000OO00 ["是否已采取控制措施"].astype (str )+"   \n具体控制措施："+OOO00OO0O0000OO00 ["具体控制措施"].astype (str )+"   \n未采取控制措施原因："+OOO00OO0O0000OO00 ["未采取控制措施原因"].astype (str ))#line:826
        OOO00OO0O0000OO00 ["是否为错报误报报告及错报误报说明"]=("是否为错报误报报告："+OOO00OO0O0000OO00 ["是否为错报误报报告"].astype (str )+"   \n错报误报说明："+OOO00OO0O0000OO00 ["错报误报说明"].astype (str ))#line:833
        OOO00OO0O0000OO00 ["是否合并报告及合并报告编码"]=("是否合并报告："+OOO00OO0O0000OO00 ["是否合并报告"].astype (str )+"   \n合并报告编码："+OOO00OO0O0000OO00 ["合并报告编码"].astype (str ))#line:840
    except :#line:841
        pass #line:842
    if "报告类型-新的"in OOO00OO0O0000OO00 .columns :#line:843
        OOO00OO0O0000OO00 ["报告时限"]=pd .to_datetime (OOO00OO0O0000OO00 ["报告日期"].astype (str ))-pd .to_datetime (OOO00OO0O0000OO00 ["不良反应发生时间"].astype (str ))#line:845
        OOO00OO0O0000OO00 ["报告类型"]=OOO00OO0O0000OO00 ["报告类型-新的"].astype (str )+OOO00OO0O0000OO00 ["伤害"].astype (str )+"    "+OOO00OO0O0000OO00 ["严重药品不良反应"].astype (str )#line:846
        OOO00OO0O0000OO00 ["报告类型"]=OOO00OO0O0000OO00 ["报告类型"].str .replace ("-未填写-","",regex =False )#line:847
        OOO00OO0O0000OO00 ["报告类型"]=OOO00OO0O0000OO00 ["报告类型"].str .replace ("其他","一般",regex =False )#line:848
        OOO00OO0O0000OO00 ["报告类型"]=OOO00OO0O0000OO00 ["报告类型"].str .replace ("严重伤害","严重",regex =False )#line:849
        OOO00OO0O0000OO00 ["关联性评价和ADR分析"]="停药减药后反应是否减轻或消失："+OOO00OO0O0000OO00 ["停药减药后反应是否减轻或消失"].astype (str )+"\n再次使用可疑药是否出现同样反应："+OOO00OO0O0000OO00 ["再次使用可疑药是否出现同样反应"].astype (str )+"\n报告人评价："+OOO00OO0O0000OO00 ["报告人评价"].astype (str )#line:850
        OOO00OO0O0000OO00 ["ADR过程描述以及处理情况"]="不良反应发生时间："+OOO00OO0O0000OO00 ["不良反应发生时间"].astype (str )+"\n不良反应过程描述："+OOO00OO0O0000OO00 ["不良反应过程描述"].astype (str )+"\n不良反应结果:"+OOO00OO0O0000OO00 ["不良反应结果"].astype (str )+"\n对原患疾病影响:"+OOO00OO0O0000OO00 ["对原患疾病影响"].astype (str )+"\n后遗症表现："+OOO00OO0O0000OO00 ["后遗症表现"].astype (str )+"\n死亡时间:"+OOO00OO0O0000OO00 ["死亡时间"].astype (str )+"\n直接死因:"+OOO00OO0O0000OO00 ["直接死因"].astype (str )#line:851
        OOO00OO0O0000OO00 ["报告者及患者有关情况"]="患者姓名："+OOO00OO0O0000OO00 ["患者姓名"].astype (str )+"\n性别："+OOO00OO0O0000OO00 ["性别"].astype (str )+"\n出生日期:"+OOO00OO0O0000OO00 ["出生日期"].astype (str )+"\n年龄:"+OOO00OO0O0000OO00 ["年龄"].astype (str )+OOO00OO0O0000OO00 ["年龄单位"].astype (str )+"\n民族："+OOO00OO0O0000OO00 ["民族"].astype (str )+"\n体重:"+OOO00OO0O0000OO00 ["体重"].astype (str )+"\n原患疾病:"+OOO00OO0O0000OO00 ["原患疾病"].astype (str )+"\n病历号/门诊号:"+OOO00OO0O0000OO00 ["病历号/门诊号"].astype (str )+"\n既往药品不良反应/事件:"+OOO00OO0O0000OO00 ["既往药品不良反应/事件"].astype (str )+"\n家族药品不良反应/事件:"+OOO00OO0O0000OO00 ["家族药品不良反应/事件"].astype (str )#line:852
    O00OO0OO0O0OOO000 =filedialog .askdirectory ()#!!!!!!!#line:856
    O0O00O000O0OO0O00 =1 #line:859
    for O0O00O00OOOOO0OO0 in OOO00OO0O0000OO00 ["伤害"].drop_duplicates ():#line:860
        if O0O00O00OOOOO0OO0 =="其他":#line:861
            OOOOOOO000OO0O0O0 =1 #line:862
            OOOOO0O0OOOO0O00O =OOO00OO0O0000OO00 [(OOO00OO0O0000OO00 ["伤害"]=="其他")]#line:863
            OO00OOO00OOO0OOO0 =Tdoing (OOOOO0O0OOOO0O00O ,O00OOOOOO0000000O ,O0OOOO0OO00O0O000 ,OO0OOO0O0OOO00O0O ,OOOO000OO0O00O00O ,OOO0OOO0O00O0O00O )#line:864
            if O0O00O000O0OO0O00 ==1 :#line:865
                OO00OO0O00O00O000 =OO00OOO00OOO0OOO0 [0 ]#line:866
                O0O00O000O0OO0O00 =O0O00O000O0OO0O00 +1 #line:867
            else :#line:868
                OO00OO0O00O00O000 =pd .concat ([OO00OO0O00O00O000 ,OO00OOO00OOO0OOO0 [0 ]],axis =0 )#line:869
        if O0O00O00OOOOO0OO0 =="严重伤害":#line:871
            O0O0O000000OO0OO0 =1 #line:872
            O0O0O0OO0OO0OO00O =OOO00OO0O0000OO00 [(OOO00OO0O0000OO00 ["伤害"]=="严重伤害")]#line:873
            OO0OOO00O0O0OO0OO =Tdoing (O0O0O0OO0OO0OO00O ,OO0OO0O0000O0O00O ,O0OOOO0OO00O0O000 ,OO0OOO0O0OOO00O0O ,OOOO000OO0O00O00O ,OOO0OOO0O00O0O00O )#line:874
            if O0O00O000O0OO0O00 ==1 :#line:875
                OO00OO0O00O00O000 =OO0OOO00O0O0OO0OO [0 ]#line:876
                O0O00O000O0OO0O00 =O0O00O000O0OO0O00 +1 #line:877
            else :#line:878
                OO00OO0O00O00O000 =pd .concat ([OO00OO0O00O00O000 ,OO0OOO00O0O0OO0OO [0 ]],axis =0 )#line:879
        if O0O00O00OOOOO0OO0 =="死亡":#line:881
            OO0OO000O00O00OO0 =1 #line:882
            O00OOO0OO0000OO0O =OOO00OO0O0000OO00 [(OOO00OO0O0000OO00 ["伤害"]=="死亡")]#line:883
            OO0OOO0O0OOOOOO0O =Tdoing (O00OOO0OO0000OO0O ,O0O0O0O00000OO000 ,O0OOOO0OO00O0O000 ,OO0OOO0O0OOO00O0O ,OOOO000OO0O00O00O ,OOO0OOO0O00O0O00O )#line:884
            if O0O00O000O0OO0O00 ==1 :#line:885
                OO00OO0O00O00O000 =OO0OOO0O0OOOOOO0O [0 ]#line:886
                O0O00O000O0OO0O00 =O0O00O000O0OO0O00 +1 #line:887
            else :#line:888
                OO00OO0O00O00O000 =pd .concat ([OO00OO0O00O00O000 ,OO0OOO0O0OOOOOO0O [0 ]],axis =0 )#line:889
    text .insert (END ,"\n正在抽样，请稍候...已完成50%")#line:893
    OOOO0000OO000OO0O =pd .ExcelWriter (str (O00OO0OO0O0OOO000 )+"/●(最终评分需导入)被抽出的所有数据"+".xlsx")#line:894
    OO00OO0O00O00O000 .to_excel (OOOO0000OO000OO0O ,sheet_name ="被抽出的所有数据")#line:895
    OOOO0000OO000OO0O .close ()#line:896
    if OOO0OOO0O00O0O00O ==1 :#line:899
        O0O0OOO00O0O00O00 =OOO00OO0O0000OO00 .copy ()#line:900
        O0O0OOO00O0O00O00 ["原始数量"]=1 #line:901
        O000OO00O00O000O0 =OO00OO0O00O00O000 .copy ()#line:902
        O000OO00O00O000O0 ["抽取数量"]=1 #line:903
        O0OOOOOO00O0OO000 =O0O0OOO00O0O00O00 .groupby ([OO0OOO0O0OOO00O0O ]).aggregate ({"原始数量":"count"})#line:906
        O0OOOOOO00O0OO000 =O0OOOOOO00O0OO000 .sort_values (by =["原始数量"],ascending =False ,na_position ="last")#line:909
        O0OOOOOO00O0OO000 =O0OOOOOO00O0OO000 .reset_index ()#line:910
        O00OO0OO0OO0O0O0O =pd .pivot_table (O000OO00O00O000O0 ,values =["抽取数量"],index =OO0OOO0O0OOO00O0O ,columns ="伤害",aggfunc ={"抽取数量":"count"},fill_value ="0",margins =True ,dropna =False ,)#line:921
        O00OO0OO0OO0O0O0O .columns =O00OO0OO0OO0O0O0O .columns .droplevel (0 )#line:922
        O00OO0OO0OO0O0O0O =O00OO0OO0OO0O0O0O .sort_values (by =["All"],ascending =[False ],na_position ="last")#line:925
        O00OO0OO0OO0O0O0O =O00OO0OO0OO0O0O0O .reset_index ()#line:926
        O00OO0OO0OO0O0O0O =O00OO0OO0OO0O0O0O .rename (columns ={"All":"抽取总数量"})#line:927
        try :#line:928
            O00OO0OO0OO0O0O0O =O00OO0OO0OO0O0O0O .rename (columns ={"一般":"抽取数量(一般)"})#line:929
        except :#line:930
            pass #line:931
        try :#line:932
            O00OO0OO0OO0O0O0O =O00OO0OO0OO0O0O0O .rename (columns ={"严重伤害":"抽取数量(严重)"})#line:933
        except :#line:934
            pass #line:935
        try :#line:936
            O00OO0OO0OO0O0O0O =O00OO0OO0OO0O0O0O .rename (columns ={"死亡":"抽取数量-死亡"})#line:937
        except :#line:938
            pass #line:939
        O0OO00OO0O00O0O00 =pd .merge (O0OOOOOO00O0OO000 ,O00OO0OO0OO0O0O0O ,on =[OO0OOO0O0OOO00O0O ],how ="left")#line:940
        O0OO00OO0O00O0O00 ["抽取比例"]=round (O0OO00OO0O00O0O00 ["抽取总数量"]/O0OO00OO0O00O0O00 ["原始数量"],2 )#line:941
        OO0O0O00OO0O0O00O =pd .ExcelWriter (str (O00OO0OO0O0OOO000 )+"/抽样情况分布"+".xlsx")#line:942
        O0OO00OO0O00O0O00 .to_excel (OO0O0O00OO0O0O00O ,sheet_name ="抽样情况分布")#line:943
        OO0O0O00OO0O0O00O .close ()#line:944
    OO00OO0O00O00O000 =OO00OO0O00O00O000 [OOO0OO0OOO00O00O0 ["评分项"].tolist ()]#line:950
    O0OOOOO00O0OOOO00 =int (O0OOOO0OO00O0O000 )#line:952
    text .insert (END ,"\n正在抽样，请稍候...已完成70%")#line:954
    for O0O00O00OOOOO0OO0 in range (O0OOOOO00O0OOOO00 ):#line:955
        if O0O00O00OOOOO0OO0 ==0 :#line:956
            O0O000OO000O00000 =OO00OO0O00O00O000 [(OO00OO0O00O00O000 ["伤害"]=="其他")].sample (frac =1 /(O0OOOOO00O0OOOO00 -O0O00O00OOOOO0OO0 ),replace =False )#line:960
            O0O0OO0OOOO00OOOO =OO00OO0O00O00O000 [(OO00OO0O00O00O000 ["伤害"]=="严重伤害")].sample (frac =1 /(O0OOOOO00O0OOOO00 -O0O00O00OOOOO0OO0 ),replace =False )#line:963
            O0OOO00OOOO0OOO0O =OO00OO0O00O00O000 [(OO00OO0O00O00O000 ["伤害"]=="死亡")].sample (frac =1 /(O0OOOOO00O0OOOO00 -O0O00O00OOOOO0OO0 ),replace =False )#line:966
            O0OO0O0000O00OOO0 =pd .concat ([O0O000OO000O00000 ,O0O0OO0OOOO00OOOO ,O0OOO00OOOO0OOO0O ],axis =0 )#line:968
        else :#line:970
            OO00OO0O00O00O000 =pd .concat ([OO00OO0O00O00O000 ,O0OO0O0000O00OOO0 ],axis =0 )#line:971
            OO00OO0O00O00O000 .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:972
            O0O000OO000O00000 =OO00OO0O00O00O000 [(OO00OO0O00O00O000 ["伤害"]=="其他")].sample (frac =1 /(O0OOOOO00O0OOOO00 -O0O00O00OOOOO0OO0 ),replace =False )#line:975
            O0O0OO0OOOO00OOOO =OO00OO0O00O00O000 [(OO00OO0O00O00O000 ["伤害"]=="严重伤害")].sample (frac =1 /(O0OOOOO00O0OOOO00 -O0O00O00OOOOO0OO0 ),replace =False )#line:978
            O0OOO00OOOO0OOO0O =OO00OO0O00O00O000 [(OO00OO0O00O00O000 ["伤害"]=="死亡")].sample (frac =1 /(O0OOOOO00O0OOOO00 -O0O00O00OOOOO0OO0 ),replace =False )#line:981
            O0OO0O0000O00OOO0 =pd .concat ([O0O000OO000O00000 ,O0O0OO0OOOO00OOOO ,O0OOO00OOOO0OOO0O ],axis =0 )#line:982
        try :#line:983
            O0OO0O0000O00OOO0 ["报告编码"]=O0OO0O0000O00OOO0 ["报告编码"].astype (str )#line:984
        except :#line:985
            pass #line:986
        OO0000000000OO0OO =str (O00OO0OO0O0OOO000 )+"/"+str (O0O00O00OOOOO0OO0 +1 )+".xlsx"#line:987
        if OOO0OOO0O00O0O00O ==1 :#line:990
            OOOO0OO0OO000OO0O =TeasyreadT (O0OO0O0000O00OOO0 .copy ())#line:991
            del OOOO0OO0OO000OO0O ["逐条查看"]#line:992
            OOOO0OO0OO000OO0O ["评分"]=""#line:993
            if len (OOOO0OO0OO000OO0O )>0 :#line:994
                for OO0O00O0OOOOOO000 ,O0OOO0OOO0O0000OO in OOO0OO0OOO00O00O0 .iterrows ():#line:995
                    OOOO0OO0OO000OO0O .loc [(OOOO0OO0OO000OO0O ["条目"]==O0OOO0OOO0O0000OO ["评分项"]),"满分"]=O0OOO0OOO0O0000OO ["满分分值"]#line:996
                    OOOO0OO0OO000OO0O .loc [(OOOO0OO0OO000OO0O ["条目"]==O0OOO0OOO0O0000OO ["评分项"]),"打分标准"]=O0OOO0OOO0O0000OO ["打分标准"]#line:999
            OOOO0OO0OO000OO0O ["专家序号"]=O0O00O00OOOOO0OO0 +1 #line:1001
            OOOO00OOO0000OOOO =str (O00OO0OO0O0OOO000 )+"/"+"●专家评分表"+str (O0O00O00OOOOO0OO0 +1 )+".xlsx"#line:1002
            O0OO00OO0OO0OO00O =pd .ExcelWriter (OOOO00OOO0000OOOO )#line:1003
            OOOO0OO0OO000OO0O .to_excel (O0OO00OO0OO0OO00O ,sheet_name ="字典数据")#line:1004
            O0OO00OO0OO0OO00O .close ()#line:1005
    text .insert (END ,"\n正在抽样，请稍候...已完成100%")#line:1008
    showinfo (title ="提示信息",message ="抽样和分组成功，请查看以下文件夹："+str (O00OO0OO0O0OOO000 ))#line:1009
    text .insert (END ,"\n抽样和分组成功，请查看以下文件夹："+str (O00OO0OO0O0OOO000 ))#line:1010
    text .insert (END ,"\n抽样概况:\n")#line:1011
    text .insert (END ,O0OO00OO0O00O0O00 [[OO0OOO0O0OOO00O0O ,"原始数量","抽取总数量"]])#line:1012
    text .see (END )#line:1013
def Tdoing (O00O0OO00O0000OOO ,O0OO0O0O0OO00O0OO ,O0O00OO00OOO0OOOO ,OOOO00O00OOOOOO0O ,OO00O0O00OO0O000O ,O0OOO0OO00000OOOO ):#line:1016
    ""#line:1017
    def O0O000O0O0OOOOO0O (OO0OOO0OOOO0O0O0O ,O0O0O00O0O000OO00 ,OOO00OOO0O0000000 ):#line:1019
        if float (O0O0O00O0O000OO00 )>1 :#line:1020
            try :#line:1021
                OO000OO00O0OOO00O =OO0OOO0OOOO0O0O0O .sample (int (O0O0O00O0O000OO00 ),replace =False )#line:1022
            except ValueError :#line:1024
                OO000OO00O0OOO00O =OO0OOO0OOOO0O0O0O #line:1026
        else :#line:1027
            OO000OO00O0OOO00O =OO0OOO0OOOO0O0O0O .sample (frac =float (O0O0O00O0O000OO00 ),replace =False )#line:1028
            if len (OO0OOO0OOOO0O0O0O )*float (O0O0O00O0O000OO00 )>len (OO000OO00O0OOO00O )and OOO00OOO0O0000000 =="最大覆盖":#line:1030
                OO0O00OOOO00O00O0 =pd .concat ([OO0OOO0OOOO0O0O0O ,OO000OO00O0OOO00O ],axis =0 )#line:1031
                OO0O00OOOO00O00O0 .drop_duplicates (subset =["识别代码"],keep =False ,inplace =True )#line:1032
                OOOOO00O0000O00O0 =OO0O00OOOO00O00O0 .sample (1 ,replace =False )#line:1033
                OO000OO00O0OOO00O =pd .concat ([OO000OO00O0OOO00O ,OOOOO00O0000O00O0 ],axis =0 )#line:1034
        return OO000OO00O0OOO00O #line:1035
    if OO00O0O00OO0O000O =="总体随机":#line:1038
        O0OO000000OO0OO00 =O0O000O0O0OOOOO0O (O00O0OO00O0000OOO ,O0OO0O0O0OO00O0OO ,OO00O0O00OO0O000O )#line:1039
    else :#line:1041
        O00OO0000OOO0O00O =1 #line:1042
        for OO000O000O0O000OO in O00O0OO00O0000OOO [OOOO00O00OOOOOO0O ].drop_duplicates ():#line:1043
            O00O00OOO0OOO0OOO =O00O0OO00O0000OOO [(O00O0OO00O0000OOO [OOOO00O00OOOOOO0O ]==OO000O000O0O000OO )].copy ()#line:1044
            if O00OO0000OOO0O00O ==1 :#line:1045
                O0OO000000OO0OO00 =O0O000O0O0OOOOO0O (O00O00OOO0OOO0OOO ,O0OO0O0O0OO00O0OO ,OO00O0O00OO0O000O )#line:1046
                O00OO0000OOO0O00O =O00OO0000OOO0O00O +1 #line:1047
            else :#line:1048
                OOO0000O0O0OOO0OO =O0O000O0O0OOOOO0O (O00O00OOO0OOO0OOO ,O0OO0O0O0OO00O0OO ,OO00O0O00OO0O000O )#line:1049
                O0OO000000OO0OO00 =pd .concat ([O0OO000000OO0OO00 ,OOO0000O0O0OOO0OO ])#line:1050
    O0OO000000OO0OO00 =O0OO000000OO0OO00 .drop_duplicates ()#line:1051
    return O0OO000000OO0OO00 ,1 #line:1052
def Tpinggu ():#line:1055
    ""#line:1056
    O00O00O0OOOO00O0O =Topentable (1 )#line:1057
    OO0OO0OO00OOO00OO =O00O00O0OOOO00O0O [0 ]#line:1058
    O00000O00000O0O0O =O00O00O0OOOO00O0O [1 ]#line:1059
    try :#line:1062
        OOOOOO00OO0O000O0 =[pd .read_excel (O00OOO000O0OOO0O0 ,header =0 ,sheet_name =0 )for O00OOO000O0OOO0O0 in O00000O00000O0O0O ]#line:1066
        OOO0OO0O0000O0O0O =pd .concat (OOOOOO00OO0O000O0 ,ignore_index =True ).drop_duplicates ()#line:1067
        try :#line:1068
            OOO0OO0O0000O0O0O =OOO0OO0O0000O0O0O .loc [:,~OOO0OO0O0000O0O0O .columns .str .contains ("^Unnamed")]#line:1069
        except :#line:1070
            pass #line:1071
    except :#line:1072
        showinfo (title ="提示信息",message ="载入文件出错，任务终止。")#line:1073
        return 0 #line:1074
    try :#line:1077
        OO0OO0OO00OOO00OO =OO0OO0OO00OOO00OO .reset_index ()#line:1078
    except :#line:1079
        showinfo (title ="提示信息",message ="专家评分文件存在错误，程序中止。")#line:1080
        return 0 #line:1081
    OOO0OO0O0000O0O0O ["质量评估专用表"]=""#line:1083
    text .insert (END ,"\n打分表导入成功，正在统计，请耐心等待...")#line:1086
    text .insert (END ,"\n正在计算总分，请稍候，已完成20%")#line:1087
    text .see (END )#line:1088
    OOOO0O0O0O0OOO0OO =OO0OO0OO00OOO00OO [["序号","条目","详细描述","评分","满分","打分标准","专家序号"]].copy ()#line:1091
    OOOOO0OO00O0O0O00 =OOO0OO0O0000O0O0O [["质量评估模式","识别代码"]].copy ()#line:1092
    OOOO0O0O0O0OOO0OO .reset_index (inplace =True )#line:1093
    OOOOO0OO00O0O0O00 .reset_index (inplace =True )#line:1094
    OOOOO0OO00O0O0O00 =OOOOO0OO00O0O0O00 .rename (columns ={"识别代码":"序号"})#line:1095
    OOOO0O0O0O0OOO0OO =pd .merge (OOOO0O0O0O0OOO0OO ,OOOOO0OO00O0O0O00 ,on =["序号"])#line:1096
    OOOO0O0O0O0OOO0OO =OOOO0O0O0O0OOO0OO .sort_values (by =["序号","条目"],ascending =True ,na_position ="last")#line:1097
    OOOO0O0O0O0OOO0OO =OOOO0O0O0O0OOO0OO [["质量评估模式","序号","条目","详细描述","评分","满分","打分标准","专家序号"]]#line:1098
    for O00OOOOOO000O0000 ,O0OO00OOO0O0OOOOO in OO0OO0OO00OOO00OO .iterrows ():#line:1100
        OO0O0OO0000OOO000 ="专家打分-"+str (O0OO00OOO0O0OOOOO ["条目"])#line:1101
        OOO0OO0O0000O0O0O .loc [(OOO0OO0O0000O0O0O ["识别代码"]==O0OO00OOO0O0OOOOO ["序号"]),OO0O0OO0000OOO000 ]=O0OO00OOO0O0OOOOO ["评分"]#line:1102
    del OOO0OO0O0000O0O0O ["专家打分-识别代码"]#line:1103
    del OOO0OO0O0000O0O0O ["专家打分-#####分隔符#########"]#line:1104
    try :#line:1105
        OOO0OO0O0000O0O0O =OOO0OO0O0000O0O0O .loc [:,~OOO0OO0O0000O0O0O .columns .str .contains ("^Unnamed")]#line:1106
    except :#line:1107
        pass #line:1108
    text .insert (END ,"\n正在计算总分，请稍候，已完成60%")#line:1109
    text .see (END )#line:1110
    O0OO0OO0O000OOO00 =O00000O00000O0O0O [0 ]#line:1113
    try :#line:1114
        OO0OOO00O0O0O0OO0 =str (O0OO0OO0O000OOO00 ).replace ("●(最终评分需导入)被抽出的所有数据.xls","")#line:1115
    except :#line:1116
        OO0OOO00O0O0O0OO0 =str (O0OO0OO0O000OOO00 )#line:1117
    O0O00O0OOOOOO0OOO =pd .ExcelWriter (str (OO0OOO00O0O0O0OO0 )+"各评估对象打分核对文件"+".xlsx")#line:1125
    OOOO0O0O0O0OOO0OO .to_excel (O0O00O0OOOOOO0OOO ,sheet_name ="原始打分")#line:1126
    O0O00O0OOOOOO0OOO .close ()#line:1127
    OO0OO000O0OO0O0OO =Tpinggu2 (OOO0OO0O0000O0O0O )#line:1131
    text .insert (END ,"\n正在计算总分，请稍候，已完成100%")#line:1133
    text .see (END )#line:1134
    showinfo (title ="提示信息",message ="打分计算成功，请查看文件："+str (OO0OOO00O0O0O0OO0 )+"最终打分"+".xlsx")#line:1135
    text .insert (END ,"\n打分计算成功，请查看文件："+str (O0OO0OO0O000OOO00 )+"最终打分"+".xls\n")#line:1136
    OO0OO000O0OO0O0OO .reset_index (inplace =True )#line:1137
    text .insert (END ,"\n以下是结果概况：\n")#line:1138
    text .insert (END ,OO0OO000O0OO0O0OO [["评估对象","总分"]])#line:1139
    text .see (END )#line:1140
    OO00OO00O0OO0O0OO =["评估对象","总分"]#line:1144
    for OOOO00OOOOO0OO0OO in OO0OO000O0OO0O0OO .columns :#line:1145
        if "专家打分"in OOOO00OOOOO0OO0OO :#line:1146
            OO00OO00O0OO0O0OO .append (OOOO00OOOOO0OO0OO )#line:1147
    O00OO0OOO00OOOOO0 =OO0OO000O0OO0O0OO [OO00OO00O0OO0O0OO ]#line:1148
    OOOOO0OO00O00OO00 =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name =0 ,header =0 ,index_col =0 ).reset_index ()#line:1152
    if "专家打分-不良反应名称"in OO00OO00O0OO0O0OO :#line:1154
        OOOOO0OO00O00OO00 =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="药品",header =0 ,index_col =0 ).reset_index ()#line:1155
    if "专家打分-化妆品名称"in OO00OO00O0OO0O0OO :#line:1157
        OOOOO0OO00O00OO00 =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="化妆品",header =0 ,index_col =0 ).reset_index ()#line:1158
    if "专家打分-是否需要开展产品风险评价"in OO00OO00O0OO0O0OO :#line:1159
        OOOOO0OO00O00OO00 =pd .read_excel (peizhidir +"0（范例）质量评估.xls",sheet_name ="器械持有人",header =0 ,index_col =0 ).reset_index ()#line:1160
    for O00OOOOOO000O0000 ,O0OO00OOO0O0OOOOO in OOOOO0OO00O00OO00 .iterrows ():#line:1161
        O00O0OOO0OOOO0O0O ="专家打分-"+str (O0OO00OOO0O0OOOOO ["评分项"])#line:1162
        try :#line:1163
            warnings .filterwarnings ('ignore')#line:1164
            O00OO0OOO00OOOOO0 .loc [-1 ,O00O0OOO0OOOO0O0O ]=O0OO00OOO0O0OOOOO ["满分分值"]#line:1165
        except :#line:1166
            pass #line:1167
    del O00OO0OOO00OOOOO0 ["专家打分-识别代码"]#line:1168
    O00OO0OOO00OOOOO0 .iloc [-1 ,0 ]="满分分值"#line:1169
    O00OO0OOO00OOOOO0 .loc [-1 ,"总分"]=100 #line:1170
    if "专家打分-事件原因分析.1"not in OO00OO00O0OO0O0OO :#line:1172
        O00OO0OOO00OOOOO0 .loc [-1 ,"专家打分-报告时限"]=5 #line:1173
    if "专家打分-事件原因分析.1"in OO00OO00O0OO0O0OO :#line:1175
        O00OO0OOO00OOOOO0 .loc [-1 ,"专家打分-报告时限"]=10 #line:1176
    O00OO0OOO00OOOOO0 .columns =O00OO0OOO00OOOOO0 .columns .str .replace ("专家打分-","",regex =False )#line:1179
    if ("专家打分-器械故障表现"in OO00OO00O0OO0O0OO )and ("modex"not in OOO0OO0O0000O0O0O .columns ):#line:1181
        O00OO0OOO00OOOOO0 .loc [-1 ,"姓名和既往病史"]=2 #line:1182
        O00OO0OOO00OOOOO0 .loc [-1 ,"报告日期"]=1 #line:1183
    else :#line:1184
        del O00OO0OOO00OOOOO0 ["伤害"]#line:1185
    if "专家打分-化妆品名称"in OO00OO00O0OO0O0OO :#line:1187
        del O00OO0OOO00OOOOO0 ["报告时限"]#line:1188
    try :#line:1191
        O00OO0OOO00OOOOO0 =O00OO0OOO00OOOOO0 [["评估对象","总分","伤害.1","是否开展了调查及调查情况","关联性评价","事件原因分析.1","是否需要开展产品风险评价","控制措施情况","是否为错报误报报告及错报误报说明","是否合并报告及合并报告编码","报告时限"]]#line:1192
    except :#line:1193
        pass #line:1194
    try :#line:1195
        O00OO0OOO00OOOOO0 =O00OO0OOO00OOOOO0 [["评估对象","总分","报告日期","报告人","联系人","联系电话","注册证编号/曾用注册证编号","产品名称","型号和规格","产品批号和产品编号","生产日期","有效期至","事件发生日期","发现或获知日期","伤害","伤害表现","器械故障表现","姓名和既往病史","年龄和年龄类型","性别","预期治疗疾病或作用","器械使用日期","使用场所和场所名称","使用过程","合并用药/械情况说明","事件原因分析和事件原因分析描述","初步处置情况","报告时限"]]#line:1196
    except :#line:1197
        pass #line:1198
    try :#line:1199
        O00OO0OOO00OOOOO0 =O00OO0OOO00OOOOO0 [["评估对象","总分","报告类型","报告时限","报告者及患者有关情况","原患疾病","药品信息","不良反应名称","ADR过程描述以及处理情况","关联性评价和ADR分析"]]#line:1200
    except :#line:1201
        pass #line:1202
    O0OOO000OOOO0OO0O =pd .ExcelWriter (str (OO0OOO00O0O0O0OO0 )+"最终打分"+".xlsx")#line:1204
    O00OO0OOO00OOOOO0 .to_excel (O0OOO000OOOO0OO0O ,sheet_name ="最终打分")#line:1205
    O0OOO000OOOO0OO0O .close ()#line:1206
    Ttree_Level_2 (O00OO0OOO00OOOOO0 ,0 ,OO0OO000O0OO0O0OO )#line:1208
def Tpinggu2 (O000O0OOO000O0000 ):#line:1211
    ""#line:1212
    O000O0OOO000O0000 ["报告数量小计"]=1 #line:1213
    if ("器械故障表现"in O000O0OOO000O0000 .columns )and ("modex"not in O000O0OOO000O0000 .columns ):#line:1216
        O000O0OOO000O0000 ["专家打分-姓名和既往病史"]=2 #line:1217
        O000O0OOO000O0000 ["专家打分-报告日期"]=1 #line:1218
        if "专家打分-报告时限情况"not in O000O0OOO000O0000 .columns :#line:1219
            O000O0OOO000O0000 ["报告时限"]=O000O0OOO000O0000 ["报告时限"].astype (float )#line:1220
            O000O0OOO000O0000 ["专家打分-报告时限"]=0 #line:1221
            O000O0OOO000O0000 .loc [(O000O0OOO000O0000 ["伤害"]=="死亡")&(O000O0OOO000O0000 ["报告时限"]<=7 ),"专家打分-报告时限"]=5 #line:1222
            O000O0OOO000O0000 .loc [(O000O0OOO000O0000 ["伤害"]=="严重伤害")&(O000O0OOO000O0000 ["报告时限"]<=20 ),"专家打分-报告时限"]=5 #line:1223
            O000O0OOO000O0000 .loc [(O000O0OOO000O0000 ["伤害"]=="其他")&(O000O0OOO000O0000 ["报告时限"]<=30 ),"专家打分-报告时限"]=5 #line:1224
    if "专家打分-事件原因分析.1"in O000O0OOO000O0000 .columns :#line:1228
       O000O0OOO000O0000 ["专家打分-报告时限"]=10 #line:1229
    OO0000O0OOOO0OO0O =[]#line:1232
    for OO0OO00OO0O0OO00O in O000O0OOO000O0000 .columns :#line:1233
        if "专家打分-"in OO0OO00OO0O0OO00O :#line:1234
            OO0000O0OOOO0OO0O .append (OO0OO00OO0O0OO00O )#line:1235
    OO000O0000OOOOOO0 =1 #line:1239
    for OO0OO00OO0O0OO00O in OO0000O0OOOO0OO0O :#line:1240
        O0O00OO000OO00000 =O000O0OOO000O0000 .groupby (["质量评估模式"]).aggregate ({OO0OO00OO0O0OO00O :"sum"}).reset_index ()#line:1241
        if OO000O0000OOOOOO0 ==1 :#line:1242
            O000O0OO00OOO00O0 =O0O00OO000OO00000 #line:1243
            OO000O0000OOOOOO0 =OO000O0000OOOOOO0 +1 #line:1244
        else :#line:1245
            O000O0OO00OOO00O0 =pd .merge (O000O0OO00OOO00O0 ,O0O00OO000OO00000 ,on ="质量评估模式",how ="left")#line:1246
    O0O000O0OO00OOO00 =O000O0OOO000O0000 .groupby (["质量评估模式"]).aggregate ({"报告数量小计":"sum"}).reset_index ()#line:1248
    O000O0OO00OOO00O0 =pd .merge (O000O0OO00OOO00O0 ,O0O000O0OO00OOO00 ,on ="质量评估模式",how ="left")#line:1249
    for OO0OO00OO0O0OO00O in OO0000O0OOOO0OO0O :#line:1252
        O000O0OO00OOO00O0 [OO0OO00OO0O0OO00O ]=round (O000O0OO00OOO00O0 [OO0OO00OO0O0OO00O ]/O000O0OO00OOO00O0 ["报告数量小计"],2 )#line:1253
    O000O0OO00OOO00O0 ["总分"]=round (O000O0OO00OOO00O0 [OO0000O0OOOO0OO0O ].sum (axis =1 ),2 )#line:1254
    O000O0OO00OOO00O0 =O000O0OO00OOO00O0 .sort_values (by =["总分"],ascending =False ,na_position ="last")#line:1255
    print (O000O0OO00OOO00O0 )#line:1256
    warnings .filterwarnings ('ignore')#line:1257
    O000O0OO00OOO00O0 .loc ["平均分(非加权)"]=round (O000O0OO00OOO00O0 .mean (axis =0 ,numeric_only =True ),2 )#line:1258
    O000O0OO00OOO00O0 .loc ["标准差(非加权)"]=round (O000O0OO00OOO00O0 .std (axis =0 ,numeric_only =True ),2 )#line:1259
    O000O0OO00OOO00O0 =O000O0OO00OOO00O0 .rename (columns ={"质量评估模式":"评估对象"})#line:1260
    O000O0OO00OOO00O0 .iloc [-2 ,0 ]="平均分(非加权)"#line:1261
    O000O0OO00OOO00O0 .iloc [-1 ,0 ]="标准差(非加权)"#line:1262
    return O000O0OO00OOO00O0 #line:1264
def Ttree_Level_2 (OOO000O0OO0O0O000 ,O0OOOO00OOO0OO0O0 ,O0OOOO000O000O0O0 ,*OOOOOO0OOO0OO0O00 ):#line:1267
    ""#line:1268
    OO0000OO0000O0OO0 =OOO000O0OO0O0O000 .columns .values .tolist ()#line:1270
    O0OOOO00OOO0OO0O0 =0 #line:1271
    OO0O000O000OOO0OO =OOO000O0OO0O0O000 .loc [:]#line:1272
    O000000OOOO0OOOO0 =Toplevel ()#line:1275
    O000000OOOO0OOOO0 .title ("报表查看器")#line:1276
    O00O000OO000OOOO0 =O000000OOOO0OOOO0 .winfo_screenwidth ()#line:1277
    O0OOOO00O0000O000 =O000000OOOO0OOOO0 .winfo_screenheight ()#line:1279
    OO0OOO0O0000OO0OO =1300 #line:1281
    OO0OOOO0000OO00OO =600 #line:1282
    O0OO00O00OOOOOO00 =(O00O000OO000OOOO0 -OO0OOO0O0000OO0OO )/2 #line:1284
    OO00O0OO000OO000O =(O0OOOO00O0000O000 -OO0OOOO0000OO00OO )/2 #line:1285
    O000000OOOO0OOOO0 .geometry ("%dx%d+%d+%d"%(OO0OOO0O0000OO0OO ,OO0OOOO0000OO00OO ,O0OO00O00OOOOOO00 ,OO00O0OO000OO000O ))#line:1286
    OO00000O0000OO000 =ttk .Frame (O000000OOOO0OOOO0 ,width =1300 ,height =20 )#line:1287
    OO00000O0000OO000 .pack (side =TOP )#line:1288
    O00000OOOO00O00OO =OO0O000O000OOO0OO .values .tolist ()#line:1291
    O00OOOOOO000O0O0O =OO0O000O000OOO0OO .columns .values .tolist ()#line:1292
    O0O0OO0O0000OO00O =ttk .Treeview (OO00000O0000OO000 ,columns =O00OOOOOO000O0O0O ,show ="headings",height =45 )#line:1293
    for OOO0OOOO00OO0OOO0 in O00OOOOOO000O0O0O :#line:1295
        O0O0OO0O0000OO00O .heading (OOO0OOOO00OO0OOO0 ,text =OOO0OOOO00OO0OOO0 )#line:1296
    for O0000O000O0O0O0OO in O00000OOOO00O00OO :#line:1297
        O0O0OO0O0000OO00O .insert ("","end",values =O0000O000O0O0O0OO )#line:1298
    for O000O00OOO0000O00 in O00OOOOOO000O0O0O :#line:1299
        O0O0OO0O0000OO00O .column (O000O00OOO0000O00 ,minwidth =0 ,width =120 ,stretch =NO )#line:1300
    OOO000O0OOOO0O0O0 =Scrollbar (OO00000O0000OO000 ,orient ="vertical")#line:1302
    OOO000O0OOOO0O0O0 .pack (side =RIGHT ,fill =Y )#line:1303
    OOO000O0OOOO0O0O0 .config (command =O0O0OO0O0000OO00O .yview )#line:1304
    O0O0OO0O0000OO00O .config (yscrollcommand =OOO000O0OOOO0O0O0 .set )#line:1305
    OOOOO000O0000000O =Scrollbar (OO00000O0000OO000 ,orient ="horizontal")#line:1307
    OOOOO000O0000000O .pack (side =BOTTOM ,fill =X )#line:1308
    OOOOO000O0000000O .config (command =O0O0OO0O0000OO00O .xview )#line:1309
    O0O0OO0O0000OO00O .config (yscrollcommand =OOO000O0OOOO0O0O0 .set )#line:1310
    def O0OO0O000000OOO00 (O00OO00O0000OOOO0 ,OO000O0O0O00OO0O0 ,OO0OO0OOOO000O0OO ):#line:1312
        for O00OOOO0O0O00000O in O0O0OO0O0000OO00O .selection ():#line:1315
            O0OO0OO0OOOOOOOOO =O0O0OO0O0000OO00O .item (O00OOOO0O0O00000O ,"values")#line:1316
        OO0O0000000OOO0OO =O0OO0OO0OOOOOOOOO [2 :]#line:1318
        OOO000OOO00000000 =OO0OO0OOOO000O0OO .iloc [-1 ,:][2 :]#line:1321
        O00O000OOOOO00000 =OO0OO0OOOO000O0OO .columns #line:1322
        O00O000OOOOO00000 =O00O000OOOOO00000 [2 :]#line:1323
        Tpo (OOO000OOO00000000 ,OO0O0000000OOO0OO ,O00O000OOOOO00000 ,"失分","得分",O0OO0OO0OOOOOOOOO [0 ])#line:1325
        return 0 #line:1326
    O0O0OO0O0000OO00O .bind ("<Double-1>",lambda OOO000OO0OOO0000O :O0OO0O000000OOO00 (OOO000OO0OOO0000O ,O00OOOOOO000O0O0O ,OO0O000O000OOO0OO ),)#line:1332
    def OOO0O00OOO0OO0000 (OO00O0OO000OOOOOO ,OOOOOO0O00O0O0OOO ,O00OO00O0OOO000OO ):#line:1334
        O0OO00000O0000OO0 =[(OO00O0OO000OOOOOO .set (OOO0OOO0OO000OOO0 ,OOOOOO0O00O0O0OOO ),OOO0OOO0OO000OOO0 )for OOO0OOO0OO000OOO0 in OO00O0OO000OOOOOO .get_children ("")]#line:1335
        O0OO00000O0000OO0 .sort (reverse =O00OO00O0OOO000OO )#line:1336
        for O0O00OOO00OO0OO00 ,(OOO0OOOOO000O0O0O ,O0O0O00OOOOOO0OOO )in enumerate (O0OO00000O0000OO0 ):#line:1338
            OO00O0OO000OOOOOO .move (O0O0O00OOOOOO0OOO ,"",O0O00OOO00OO0OO00 )#line:1339
        OO00O0OO000OOOOOO .heading (OOOOOO0O00O0O0OOO ,command =lambda :OOO0O00OOO0OO0000 (OO00O0OO000OOOOOO ,OOOOOO0O00O0O0OOO ,not O00OO00O0OOO000OO ))#line:1342
    for O00OOOOOOO0OOO0O0 in O00OOOOOO000O0O0O :#line:1344
        O0O0OO0O0000OO00O .heading (O00OOOOOOO0OOO0O0 ,text =O00OOOOOOO0OOO0O0 ,command =lambda _col =O00OOOOOOO0OOO0O0 :OOO0O00OOO0OO0000 (O0O0OO0O0000OO00O ,_col ,False ),)#line:1349
    O0O0OO0O0000OO00O .pack ()#line:1351
def Txuanze ():#line:1353
    ""#line:1354
    global ori #line:1355
    O00OOOOO00OO0O000 =pd .read_excel (peizhidir +"0（范例）批量筛选.xls",sheet_name =0 ,header =0 ,index_col =0 ,).reset_index ()#line:1356
    text .insert (END ,"\n正在执行内部数据规整...\n")#line:1357
    text .insert (END ,O00OOOOO00OO0O000 )#line:1358
    ori ["temppr"]=""#line:1359
    for OOO0O000O0OOO00O0 in O00OOOOO00OO0O000 .columns .tolist ():#line:1360
        ori ["temppr"]=ori ["temppr"]+"----"+ori [OOO0O000O0OOO00O0 ]#line:1361
    O0O0000OO0OO0O0O0 ="测试字段MMMMM"#line:1362
    for OOO0O000O0OOO00O0 in O00OOOOO00OO0O000 .columns .tolist ():#line:1363
        for OOO0OO0O00OO0OOOO in O00OOOOO00OO0O000 [OOO0O000O0OOO00O0 ].drop_duplicates ():#line:1364
            if OOO0OO0O00OO0OOOO :#line:1365
                O0O0000OO0OO0O0O0 =O0O0000OO0OO0O0O0 +"|"+str (OOO0OO0O00OO0OOOO )#line:1366
    ori =ori .loc [ori ["temppr"].str .contains (O0O0000OO0OO0O0O0 ,na =False )].copy ()#line:1367
    del ori ["temppr"]#line:1368
    ori =ori .reset_index (drop =True )#line:1370
    text .insert (END ,"\n内部数据规整完毕。\n")#line:1371
def Tpo (OOOO0OOO0000O00O0 ,OOOOO0OOOO0OOO0O0 ,O00000OOO00O000OO ,O0O0OO0OOO0O0O00O ,O00OOOO00OO00O000 ,O0OOOO0OOOO000OOO ):#line:1374
    ""#line:1375
    OOOO0OOO0000O00O0 =OOOO0OOO0000O00O0 .astype (float )#line:1376
    OOOOO0OOOO0OOO0O0 =tuple (float (O0OO000OOO00OO000 )for O0OO000OOO00OO000 in OOOOO0OOOO0OOO0O0 )#line:1377
    OOO0OOOO0OO0OO000 =Toplevel ()#line:1378
    OOO0OOOO0OO0OO000 .title (O0OOOO0OOOO000OOO )#line:1379
    O0O0OOOO0OO00O000 =ttk .Frame (OOO0OOOO0OO0OO000 ,height =20 )#line:1380
    O0O0OOOO0OO00O000 .pack (side =TOP )#line:1381
    OO0O0000O000OOO00 =0.2 #line:1383
    OO0O0O0OO0O0O0O00 =Figure (figsize =(12 ,6 ),dpi =100 )#line:1384
    OO000OOO00O0000OO =FigureCanvasTkAgg (OO0O0O0OO0O0O0O00 ,master =OOO0OOOO0OO0OO000 )#line:1385
    OO000OOO00O0000OO .draw ()#line:1386
    OO000OOO00O0000OO .get_tk_widget ().pack (expand =1 )#line:1387
    OO0000O0OO0O000OO =OO0O0O0OO0O0O0O00 .add_subplot (111 )#line:1388
    plt .rcParams ["font.sans-serif"]=["SimHei"]#line:1390
    OO0000O0O0OOOOOOO =NavigationToolbar2Tk (OO000OOO00O0000OO ,OOO0OOOO0OO0OO000 )#line:1392
    OO0000O0O0OOOOOOO .update ()#line:1393
    OO000OOO00O0000OO .get_tk_widget ().pack ()#line:1395
    O000O00OO00OOOO0O =range (0 ,len (O00000OOO00O000OO ),1 )#line:1396
    OO0000O0OO0O000OO .set_xticklabels (O00000OOO00O000OO ,rotation =-90 ,fontsize =8 )#line:1399
    OO0000O0OO0O000OO .bar (O000O00OO00OOOO0O ,OOOO0OOO0000O00O0 ,align ="center",tick_label =O00000OOO00O000OO ,label =O0O0OO0OOO0O0O00O )#line:1403
    OO0000O0OO0O000OO .bar (O000O00OO00OOOO0O ,OOOOO0OOOO0OOO0O0 ,align ="center",label =O00OOOO00OO00O000 )#line:1404
    OO0000O0OO0O000OO .set_title (O0OOOO0OOOO000OOO )#line:1405
    OO0000O0OO0O000OO .set_xlabel ("项")#line:1406
    OO0000O0OO0O000OO .set_ylabel ("数量")#line:1407
    OO0O0O0OO0O0O0O00 .tight_layout (pad =0.4 ,w_pad =3.0 ,h_pad =3.0 )#line:1410
    O0O000O0OO000OOO0 =OO0000O0OO0O000OO .get_position ()#line:1411
    OO0000O0OO0O000OO .set_position ([O0O000O0OO000OOO0 .x0 ,O0O000O0OO000OOO0 .y0 ,O0O000O0OO000OOO0 .width *0.7 ,O0O000O0OO000OOO0 .height ])#line:1412
    OO0000O0OO0O000OO .legend (loc =2 ,bbox_to_anchor =(1.05 ,1.0 ),fontsize =10 ,borderaxespad =0.0 )#line:1413
    OO000OOO00O0000OO .draw ()#line:1415
def helper ():#line:1418
    ""#line:1419
    OOO0000O000OOO000 =Toplevel ()#line:1420
    OOO0000O000OOO000 .title ("程序使用帮助")#line:1421
    OOO0000O000OOO000 .geometry ("700x500")#line:1422
    O0OOO0000O0OOOOO0 =Scrollbar (OOO0000O000OOO000 )#line:1424
    O000OO0O000OOO0OO =Text (OOO0000O000OOO000 ,height =80 ,width =150 ,bg ="#FFFFFF",font ="微软雅黑")#line:1425
    O0OOO0000O0OOOOO0 .pack (side =RIGHT ,fill =Y )#line:1426
    O000OO0O000OOO0OO .pack ()#line:1427
    O0OOO0000O0OOOOO0 .config (command =O000OO0O000OOO0OO .yview )#line:1428
    O000OO0O000OOO0OO .config (yscrollcommand =O0OOO0000O0OOOOO0 .set )#line:1429
    O000OO0O000OOO0OO .insert (END ,"\n                                             帮助文件\n\n\n为帮助用户快速熟悉“阅易评”使用方法，现以医疗器械不良事件报告表为例，对使用步骤作以下说明：\n\n第一步：原始数据准备\n用户登录国家医疗器械不良事件监测信息系统（https://maers.adrs.org.cn/），在“个例不良事件管理—报告浏览”页面，选择本次评估的报告范围（时间、报告状态、事发地监测机构等）后进行查询和导出。\n●注意：国家医疗器械不良事件监测信息系统设置每次导出数据上限为5000份报告，如查询发现需导出报告数量超限，需分次导出；如导出数据为压缩包，需先行解压。如原始数据在多个文件夹内，需先行整理到统一文件夹中，方便下一步操作。\n\n第二步：原始数据导入\n用户点击“导入原始数据”按钮，在弹出数据导入框中找到原始数据存储位置，本程序支持导入多个原始数据文件，可在长按键盘“Ctrl”按键的同时分别点击相关文件，选择完毕后点击“打开”按钮，程序会提示“数据读取成功”或“导入文件错误”。\n●注意：基于当前评估工作需要，仅针对使用单位报告进行评估，故导入数据时仅选择“使用单位、经营企业医疗器械不良事件报告”，不支持与“上市许可持有人医疗器械不良事件报告”混选。如提示“导入文件错误，请重试”，请重启程序并重新操作，如仍提示错误可与开发者联系（联系方式见文末）。\n\n第三步：报告抽样分组\n用户点击“随机抽样分组”按钮，在“随机抽样及随机分组”弹窗中：\n1、根据评估目的，在“评估对象”处勾选相应选项，可根据选项对上报单位（医疗机构）、县（区）、地市实施评估。注意：如果您是省级用户，被评估对象是各地市，您要关闭本软件，修改好配置表文件夹“0（范例）质量评估.xls”中的“地市列表”单元表，将本省地市参照范例填好再运行本软件。如果被评估对象不是选择“地市”，则无需该项操作。\n2、根据报告伤害类型依次输入需抽取的比例或报告数量。程序默认此处输入数值小于1（含1）为抽取比例，输入数值大于1为抽取报告数量，用户根据实际情况任选一种方式即可。本程序支持不同伤害类型报告选用不同抽样方式。\n3、根据参与评估专家数量，在“抽样后随机分组数”输入对应数字。\n4、抽样方法有2种，一种是最大覆盖，即对每个评估对象按抽样数量/比例进行单独抽样，如遇到不足则多抽（所以总体实际抽样数量可能会比设置的多一点），每个评估对象都会被抽到；另外一种是总体随机，即按照设定的参数从总体中随机抽取（有可能部分评估对象没有被抽到）。\n用户在确定抽样分组内容全部正确录入后，点击“最大覆盖”或者“总体随机”按钮，根据程序提示选择保存地址。程序将按照专家数量将抽取的报告进行随即分配，生成对应份数的“专家评分表”，专家评分表包含评分项、详细描述、评分、满分、打分标准等。专家评分表自动隐藏报告单位等信息，用户可随机将评分表派发给专家进行评分。\n●注意：为保护数据同时便于专家查看，需对专家评分表进行格式设置，具体操作如下（或者直接使用格式刷一键完成，模板详见配置表-专家模板）：全选表格，右键-设置单元格格式-对齐，勾选自动换行，之后设置好列间距。此外，请勿修改“专家评分表“和“（最终评分需导入）被抽出的所有数据”两类工作文件的文件名。\n\n第四步：评估得分统计\n用户在全部专家完成评分后，将所有专家评分表放置在同一文件夹中，点击“评估得分统计”按钮，全选所有专家评分表和“（最终评分需导入）被抽出的所有数据”这个文件，后点击“打开”，程序将首先进行评分内容校验，对于打分错误报告给与提示并生成错误定位文件，需根据提示修正错误再全部导入。如打分项无误，程序将提示“打分表导入成功，正在统计请耐心等待”，并生成最终的评分结果。\n\n本程序由广东省药品不良反应监测中心和佛山市药品不良反应监测中心共同制作，其他贡献单位包括广州市药品不良反应监测中心、深圳市药物警戒和风险管理研究院等。如有疑问，请联系我们：\n评估标准相关问题：广东省药品不良反应监测中心 张博涵 020-37886057\n程序运行相关问题：佛山市药品不良反应监测中心 蔡权周 0757-82580815 \n\n",)#line:1433
    O000OO0O000OOO0OO .config (state =DISABLED )#line:1435
def TeasyreadT (OOOOO000OO0O0O0OO ):#line:1438
    ""#line:1439
    OOOOO000OO0O0O0OO ["#####分隔符#########"]="######################################################################"#line:1442
    O000O0O00OO000OO0 =OOOOO000OO0O0O0OO .stack (dropna =False )#line:1443
    O000O0O00OO000OO0 =pd .DataFrame (O000O0O00OO000OO0 ).reset_index ()#line:1444
    O000O0O00OO000OO0 .columns =["序号","条目","详细描述"]#line:1445
    O000O0O00OO000OO0 ["逐条查看"]="逐条查看"#line:1446
    return O000O0O00OO000OO0 #line:1447
def Tget_list (OO0O0O0OO00000O00 ):#line:1452
    ""#line:1453
    OO0O0O0OO00000O00 =str (OO0O0O0OO00000O00 )#line:1454
    O000O0000000000OO =[]#line:1455
    O000O0000000000OO .append (OO0O0O0OO00000O00 )#line:1456
    O000O0000000000OO =",".join (O000O0000000000OO )#line:1457
    O000O0000000000OO =O000O0000000000OO .split (",")#line:1458
    O000O0000000000OO =",".join (O000O0000000000OO )#line:1459
    O000O0000000000OO =O000O0000000000OO .split ("，")#line:1460
    O0O00O00OO00000O0 =O000O0000000000OO [:]#line:1461
    O000O0000000000OO =list (set (O000O0000000000OO ))#line:1462
    O000O0000000000OO .sort (key =O0O00O00OO00000O0 .index )#line:1463
    return O000O0000000000OO #line:1464
def thread_it (OOOOOO0OO0OO0O00O ,*O00OOOO000000O0O0 ):#line:1467
    ""#line:1468
    OO0O0OO00OO00OOO0 =threading .Thread (target =OOOOOO0OO0OO0O00O ,args =O00OOOO000000O0O0 )#line:1470
    OO0O0OO00OO00OOO0 .setDaemon (True )#line:1472
    OO0O0OO00OO00OOO0 .start ()#line:1474
def showWelcome ():#line:1477
    ""#line:1478
    OO0OO00O0O0O00000 =roox .winfo_screenwidth ()#line:1479
    OO00O0OO000000OOO =roox .winfo_screenheight ()#line:1481
    roox .overrideredirect (True )#line:1483
    roox .attributes ("-alpha",1 )#line:1484
    O0OOO000O00OO0O00 =(OO0OO00O0O0O00000 -475 )/2 #line:1485
    OO0OOO0OOOOO0O00O =(OO00O0OO000000OOO -200 )/2 #line:1486
    roox .geometry ("675x140+%d+%d"%(O0OOO000O00OO0O00 ,OO0OOO0OOOOO0O00O ))#line:1488
    roox ["bg"]="royalblue"#line:1489
    O0OO0OO0O00OO0OO0 =Label (roox ,text ="阅易评",fg ="white",bg ="royalblue",font =("微软雅黑",35 ))#line:1492
    O0OO0OO0O00OO0OO0 .place (x =0 ,y =15 ,width =675 ,height =90 )#line:1493
    O00OOOO00OOO0OO00 =Label (roox ,text ="                                 广东省药品不良反应监测中心                         V"+version_now ,fg ="white",bg ="cornflowerblue",font =("微软雅黑",15 ),)#line:1500
    O00OOOO00OOO0OO00 .place (x =0 ,y =90 ,width =675 ,height =50 )#line:1501
def closeWelcome ():#line:1504
    ""#line:1505
    for O0O00000O000O00OO in range (2 ):#line:1506
        root .attributes ("-alpha",0 )#line:1507
        time .sleep (1 )#line:1508
    root .attributes ("-alpha",1 )#line:1509
    roox .destroy ()#line:1510
root =Tk ()#line:1514
root .title ("阅易评 V"+version_now )#line:1515
try :#line:1516
    root .iconphoto (True ,PhotoImage (file =peizhidir +"0（范例）ico.png"))#line:1517
except :#line:1518
    pass #line:1519
sw_root =root .winfo_screenwidth ()#line:1520
sh_root =root .winfo_screenheight ()#line:1522
ww_root =700 #line:1524
wh_root =620 #line:1525
x_root =(sw_root -ww_root )/2 #line:1527
y_root =(sh_root -wh_root )/2 #line:1528
root .geometry ("%dx%d+%d+%d"%(ww_root ,wh_root ,x_root ,y_root ))#line:1529
root .configure (bg ="steelblue")#line:1530
try :#line:1533
    frame0 =ttk .Frame (root ,width =100 ,height =20 )#line:1534
    frame0 .pack (side =LEFT )#line:1535
    B_open_files1 =Button (frame0 ,text ="导入原始数据",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,0 ),)#line:1548
    B_open_files1 .pack ()#line:1549
    B_open_files3 =Button (frame0 ,text ="随机抽样分组",bg ="steelblue",height =2 ,fg ="snow",width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tchouyang ,ori ),)#line:1562
    B_open_files3 .pack ()#line:1563
    B_open_files3 =Button (frame0 ,text ="评估得分统计",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Tpinggu ),)#line:1576
    B_open_files3 .pack ()#line:1577
    B_open_files3 =Button (frame0 ,text ="查看帮助文件",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (helper ),)#line:1590
    B_open_files3 .pack ()#line:1591
    B_open_files1 =Button (frame0 ,text ="更改评分标准",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Topentable ,123 ),)#line:1603
    B_open_files1 =Button (frame0 ,text ="内置数据清洗",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (Txuanze ),)#line:1617
    if usergroup =="用户组=1":#line:1618
        B_open_files1 .pack ()#line:1619
    B_open_files1 =Button (frame0 ,text ="更改用户分组",bg ="steelblue",fg ="snow",height =2 ,width =12 ,font =("微软雅黑",12 ),relief =GROOVE ,activebackground ="lightsteelblue",command =lambda :thread_it (display_random_number ))#line:1631
    if usergroup =="用户组=0":#line:1632
        B_open_files1 .pack ()#line:1633
except :#line:1635
    pass #line:1636
text =ScrolledText (root ,height =400 ,width =400 ,bg ="#FFFFFF",font ="微软雅黑")#line:1640
text .pack ()#line:1641
text .insert (END ,"\n    欢迎使用“阅易评”，本程序由广东省药品不良反应监测中心联合佛山市药品不良反应监测中心开发，主要功能包括：\n    1、根据报告伤害类型和用户自定义抽样比例对报告表随机抽样；\n    2、根据评估专家数量对抽出报告表随机分组，生成专家评分表；\n    3、根据专家最终评分实现自动汇总统计。\n    本程序供各监测机构免费使用，使用前请先查看帮助文件。\n  \n版本功能更新日志：\n2022年6月1日  支持医疗器械不良事件报告表质量评估(上报部分)。\n2022年10月31日  支持药品不良反应报告表质量评估。  \n2023年4月6日  支持化妆品不良反应报告表质量评估。\n2023年6月9日  支持医疗器械不良事件报告表质量评估(调查评价部分)。\n\n缺陷修正：20230609 修正结果列排序（按评分项目排序）。\n\n注：化妆品质量评估仅支持第一怀疑化妆品。",)#line:1646
text .insert (END ,"\n\n")#line:1647
setting_cfg =read_setting_cfg ()#line:1653
generate_random_file ()#line:1654
setting_cfg =open_setting_cfg ()#line:1655
if setting_cfg ["settingdir"]==0 :#line:1656
    showinfo (title ="提示",message ="未发现默认配置文件夹，请选择一个。如该配置文件夹中并无配置文件，将生成默认配置文件。")#line:1657
    filepathu =filedialog .askdirectory ()#line:1658
    path =get_directory_path (filepathu )#line:1659
    update_setting_cfg ("settingdir",path )#line:1660
setting_cfg =open_setting_cfg ()#line:1661
random_number =int (setting_cfg ["sidori"])#line:1662
input_number =int (str (setting_cfg ["sidfinal"])[0 :6 ])#line:1663
day_end =convert_and_compare_dates (str (setting_cfg ["sidfinal"])[6 :14 ])#line:1664
sid =random_number *2 +183576 #line:1665
if input_number ==sid and day_end =="未过期":#line:1666
    usergroup ="用户组=1"#line:1667
    text .insert (END ,usergroup +"   有效期至：")#line:1668
    text .insert (END ,datetime .strptime (str (int (int (str (setting_cfg ["sidfinal"])[6 :14 ])/4 )),"%Y%m%d"))#line:1669
else :#line:1670
    text .insert (END ,usergroup )#line:1671
text .insert (END ,"\n配置文件路径："+setting_cfg ["settingdir"]+"\n")#line:1672
peizhidir =str (setting_cfg ["settingdir"])+csdir .split ("pinggutools")[0 ][-1 ]#line:1673
roox =Toplevel ()#line:1677
tMain =threading .Thread (target =showWelcome )#line:1678
tMain .start ()#line:1679
t1 =threading .Thread (target =closeWelcome )#line:1680
t1 .start ()#line:1681
root .lift ()#line:1682
root .attributes ("-topmost",True )#line:1683
root .attributes ("-topmost",False )#line:1684
root .mainloop ()#line:1685
