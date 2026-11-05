# 建國啤酒廠兩筆紀錄合併：移除 2006 歷史建築那筆，保留市定古蹟並加 extraLinks（可重複執行）
import json,glob,os
D='/tmp/newcity/taipei-city'; OFF='/home/user/Cultural_Heritage2/taipei-city/data/sites-official.json'
DUP='zhongshan-jianguopijiuchang2'; KEEP='zhongshan-jianguopijiuchang'
def rw(p,fn):
    d=json.load(open(p)); d2=fn(d); json.dump(d2,open(p,'w'),ensure_ascii=False,indent=1 if p==OFF else None)
def base(d):
    dup=[x for x in d if x['id']==DUP]
    for x in d:
        if x['id']==KEEP and dup:
            x['mergedNote']='同一處另有 2006 年登錄為歷史建築的官方紀錄（caseId 20061123000003），已合併為一處，類別用市定古蹟；下面 texts2 是那筆紀錄的官方說明。'
            x['texts2']=dup[0].get('texts')
    return [x for x in d if x['id']!=DUP]
rw(D+'/sites_base.json',base)
for f in glob.glob(D+'/part*.json'): rw(f,base)
def off(d):
    dup=[x for x in d if x['id']==DUP]
    for x in d:
        if x['id']==KEEP:
            x['extraLinks']=[{"title":"文資局官方資料（2006 年登錄為歷史建築的「建國啤酒廠」）","url":"https://nchdb.boch.gov.tw/assets/advanceSearch/historicalBuilding/20061123000003"}]
    return [x for x in d if x['id']!=DUP]
rw(OFF,off)
for f in glob.glob(D+'/part*.json')+[D+'/sites_base.json']:
    for x in json.load(open(f)):
        if x['id'] in ('datong-dihuajieduanhaoji','daan-diguodaxuexiaoshe',KEEP): print(os.path.basename(f),x['id'])
print(len(json.load(open(OFF))))
