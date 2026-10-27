"""Insert a native 'entry ticket' diagram page after page 1 of KP17 (zh/en)."""
import json, re
BLUE,RED,PUR,GOLD,GREEN,GREY,TXT="#6aa8ff","#ef6b6b","#a98bf0","#e8c85a","#5fd08a","rgba(245,241,233,0.62)","#f2ede4"
ORG="#f0a050"
T={"zh":dict(
 title="入場券:通用近似是「資格」,不是「勝負」", sub="核心問題:哪一種新座標最後能逼近任何函數?誰逼近最快?",
 l1="通用近似定理", l2="節點夠多(或階數夠高),就能把緊緻集上的任何連續函數逼近到任意小的誤差。",
 leg="虛線:目標 g(x);實線:近似 φ(x),差 < ε", cap="示範(概念示意)", c1="緊緻集", c2="= 有界、又含邊界的範圍", c3="區間 [0, 1](兩端實心 = 含邊界)",
 allq="三者\n皆成立", head="三種近似器都拿到「入場券」",
 cards=[("多項式",BLUE,"任何連續函數","(Weierstrass 定理)",r"$\sim r^{-2/l}$","r:階數;l:輸入維度","維度 l 越大,下降越慢",RED),
        ("一層 sigmoid 網路",RED,"任何連續函數","(擠壓函數 + 節點夠多)",r"$\sim 1/k$","k:隱藏節點數","維度 l 不出現在式子裡",GREEN),
        ("RBF 網路",PUR,"任何連續函數","",None,"本節未給出速率式",None,None)],
 rbf="同樣是通用近似器", what="能逼近什麼", rate="誤差下降速度", worst="(最壞情況的漸近速率)", band="能逼近任何連續函數 = 入場券(三者相同)",
 b1="通用近似是入場券,不是競爭優勢", b2="真正的差別在:① 誤差下降的速度  與  ② 最佳化難不難", b3="來源:KP17 通用近似定理 §1 入場券(圖型識別 第四章 §4.16);顏色加形狀對應:藍方塊 = 多項式、紅圓 = sigmoid、紫三角 = RBF",
 label="入場券圖解", notes="承接上一頁的「入場券」。這一頁用一張圖把同一件事再看一次：左邊是通用近似定理——節點（或階數）夠多，就能把緊緻集（有界又含邊界，例如區間 0 到 1）上的任何連續函數逼近到任意小的誤差。右邊三種近似器都拿到這張入場券：多項式（Weierstrass 定理，誤差約 r 的負 2/l 次方，r 是階數、l 是輸入維度，維度越大下降越慢）、一層 sigmoid 網路（誤差約 1/k，k 是隱藏節點數，式子裡沒有維度 l）、RBF 網路（同樣是通用近似器，本節沒有給出速率式）。結論：通用近似是入場券，不是競爭優勢；真正的差別是誤差下降的速度與最佳化難不難。",
 old="「入場券」", new="「入場券圖解」"),
 "en":dict(
 title="Entry ticket: universal approximation is qualification, not victory", sub="Core question: which new coordinates can finally approximate any function, and which is fastest?",
 l1="Universal approximation", l2="Enough nodes (or degree): any continuous function on a compact set is approximated to any small error.",
 leg="dashed: g(x); solid: φ(x), gap < ε", cap="Example (concept sketch)", c1="Compact set", c2="= bounded and includes its boundary", c3="[0, 1]: filled ends = included",
 allq="All three\nhold", head="All three approximators get the entry ticket",
 cards=[("Polynomial",BLUE,"any continuous function","(Weierstrass theorem)",r"$\sim r^{-2/l}$","r: degree; l: input dimension","larger l, slower decrease",RED),
        ("1-layer sigmoid net",RED,"any continuous function","(squashing fn + enough nodes)",r"$\sim 1/k$","k: hidden nodes","l does not appear",GREEN),
        ("RBF network",PUR,"any continuous function","",None,"no rate formula in this section",None,None)],
 rbf="also universal", what="Can approximate", rate="Error decrease rate", worst="(worst-case asymptotic rate)", band="Approximates any continuous function = entry ticket (same for all three)",
 b1="Universal approximation is the entry ticket, not an edge", b2="The real differences: ① speed of error decrease  and  ② how hard to optimize", b3="Source: KP17 universal approximation §1 (Pattern Recognition ch. 4, §4.16); colour + shape: blue square = polynomial, red circle = sigmoid, purple triangle = RBF",
 label="Entry ticket diagram", notes="Following the previous page on the entry ticket. This page shows the same idea in one diagram. Left: the universal approximation theorem: with enough nodes (or degree), any continuous function on a compact set (bounded and including its boundary, for example the interval 0 to 1) can be approximated to any small error. Right: all three approximators hold this ticket: polynomials (Weierstrass theorem, error about r to the power minus 2 over l, r the degree and l the input dimension, so higher dimension means slower decrease), one-layer sigmoid networks (error about 1 over k, k the hidden nodes, with no l in the formula), and RBF networks (also universal approximators; no rate formula given here). Conclusion: universal approximation is the entry ticket, not an edge; the real differences are the speed of error decrease and how hard optimization is.",
 old="the entry ticket", new="the entry ticket diagram")}
def build(lang,x0,sid,pre):
    t=T[lang]; nodes=[]
    def add(typ,x,y,w,h,style,text="",kind=None,z=2):
        nid=f"{pre}-{len(nodes)+1}"
        n={"id":nid,"type":typ,"name":f"ticket#{len(nodes)+1}","sceneId":sid,"transform":{"x":x0+x,"y":y,"scaleX":1,"scaleY":1,"rotation":0},"width":max(w,1),"height":max(h,1),"zIndex":z,"locked":False,"style":style,"text":text}
        if kind:n["shapeKind"]=kind
        nodes.append(n); return n
    base=lambda **k:dict({"fill":"transparent","stroke":"transparent","textColor":TXT,"fontSize":16,"radius":0,"borderWidth":0},**k)
    def box(x,y,w,h,stroke,fill="rgba(245,241,233,0.05)",r=14,sw=2): add("shape",x,y,w,h,base(fill=fill,stroke=stroke,radius=r,borderWidth=sw,borderStyle="solid"),"","rectangle",z=1)
    def tx(x,y,w,h,s,size,color=TXT,bold=False,al="center"): add("text",x,y,w,h,base(textColor=color,fontSize=size,fontWeight=700 if bold else 400,textAlign=al,lineHeight=1.3),s,"rectangle",z=3)
    def pl(pts,color,sw=3,smooth=False,dash=False):
        xs=[p[0] for p in pts];ys=[p[1] for p in pts];bx,by=min(xs),min(ys);bw=max(max(xs)-bx,1);bh=max(max(ys)-by,1)
        n=add("shape",bx,by,bw,bh,base(stroke=color,borderWidth=sw,**({"borderStyle":"dashed"} if dash else {})),"","polyline",z=3)
        n["polygonPoints"]=[dict({"x":round((p[0]-bx)/bw*100,2),"y":round((p[1]-by)/bh*100,2)},**({"smooth":True} if smooth else {})) for p in pts]
    def poly(pts,fill,z=3):
        xs=[p[0] for p in pts];ys=[p[1] for p in pts];bx,by=min(xs),min(ys);bw=max(max(xs)-bx,1);bh=max(max(ys)-by,1)
        n=add("shape",bx,by,bw,bh,base(fill=fill),"","polygon",z=z)
        n["polygonPoints"]=[{"x":round((p[0]-bx)/bw*100,2),"y":round((p[1]-by)/bh*100,2)} for p in pts]
    tx(40,8,1200,46,t["title"],32,TXT,True); tx(40,56,1200,32,t["sub"],18,GREY)
    # left panel
    box(32,104,352,448,"rgba(245,241,233,0.35)")
    tx(48,112,320,30,t["l1"],22,TXT,True,"left"); tx(48,146,320,66,t["l2"],16,TXT,False,"left")
    box(48,222,320,128,"rgba(245,241,233,0.25)",fill="rgba(245,241,233,0.04)",r=8,sw=1)
    cur=[(64,332),(90,290),(122,272),(150,282),(176,318),(205,336),(236,322),(262,290),(300,254)]
    pl(cur,TXT,3,True,True); pl([(x,y+3) for x,y in cur],RED,2,True)
    pl([(60,346),(340,346)],GREY,2); poly([(340,340),(352,346),(340,352)],GREY)
    tx(56,226,300,20,t["leg"],14,GREY,False,"left"); tx(56,356,300,18,t["cap"],14,GREY,False,"left")
    tx(48,380,320,28,t["c1"],21,TXT,True,"left"); tx(48,410,320,26,t["c2"],16,TXT,False,"left"); tx(48,448,320,24,t["c3"],16,"#5fb8ff")
    pl([(90,494),(310,494)],GREY,3)
    for cx in (110,290): add("shape",x=cx-7,y=487,w=14,h=14,style=base(fill="#5fb8ff"),text="",kind="ellipse") if False else add("shape",cx-7,487,14,14,base(fill="#5fb8ff"),"","ellipse")
    tx(96,504,30,22,"0",18); tx(276,504,30,22,"1",18)
    # arrow
    pl([(392,330),(424,330)],TXT,4); poly([(422,320),(440,330),(422,340)],TXT); tx(388,340,56,40,t["allq"],14,GREY)
    # right panel
    box(448,104,800,448,ORG); tx(448,112,800,30,t["head"],21,ORG,True)
    for i,(nm,acc,wh,wh2,rt,n1,n2,c2) in enumerate(t["cards"]):
        x=466+i*262; w=246
        box(x,152,w,330,acc,fill="rgba(245,241,233,0.05)",sw=3)
        mx=x+22
        if i==0: add("shape",mx-9,172,18,18,base(fill=acc),"","rectangle")
        elif i==1: add("shape",mx-9,172,18,18,base(fill=acc),"","ellipse")
        else: poly([(mx-10,190),(mx,171),(mx+10,190)],acc)
        tx(x+40,164,w-48,32,nm,19,acc,True,"left")
        tx(x+14,204,w-28,20,t["what"],14,GREY,False,"left"); tx(x+14,226,w-28,26,wh,18,TXT,False,"left"); tx(x+14,254,w-28,22,wh2,14,GREY,False,"left")
        pl([(x+14,288),(x+w-14,288)],"rgba(245,241,233,0.3)",2)
        tx(x+14,296,w-28,20,t["rate"],14,GREY,False,"left")
        if rt:
            tx(x+14,320,w-28,50,rt,30,acc,True,"left")
            tx(x+14,386,w-28,22,n1,15,TXT,False,"left"); tx(x+14,410,w-28,22,n2,15,c2,False,"left"); tx(x+14,440,w-28,22,t["worst"],14,GREY,False,"left")
        else:
            tx(x+14,324,w-28,36,t["rbf"],21,acc,True,"left"); tx(x+14,386,w-28,22,n1,15,TXT,False,"left")
    for i in range(3): pl([(466+i*262+123,484),(466+i*262+123,506)],ORG,3)
    box(466,506,764,34,"rgba(232,200,90,0.5)",fill="rgba(232,200,90,0.2)",r=8,sw=1); tx(466,510,764,26,t["band"],17,GOLD,True)
    # bottom banner
    box(32,572,1216,128,"rgba(245,241,233,0.35)",fill="rgba(11,18,38,0.85)",r=16)
    tx(48,580,1184,36,t["b1"],24,TXT,True); tx(48,622,1184,32,t["b2"],21,GOLD,True); tx(48,662,1184,28,t["b3"],14,GREY)
    return nodes
def apply(f,lang):
    t=T[lang]; d=json.load(open(f)); N=d["nodes"]; sc=d["scenes"]["lec05kp17-scene-u01"]; st=d["steps"]
    pat=re.compile(r"lec05kp17-u01-p(\d+)-")
    for k,v in N.items():
        m=pat.match(k)
        if m and int(m.group(1))>=2: v["transform"]["x"]+=1440
    for s in st[2:]: s["target"]["point"]["x"]+=1440
    nodes=build(lang,1440,"lec05kp17-scene-u01","lec05kp17-u01-p1b")
    ids=sc["nodeIds"]; i=max(j for j,k in enumerate(ids) if k.startswith("lec05kp17-u01-p1-"))+1
    for j,n in enumerate(nodes): N[n["id"]]=n; ids.insert(i+j,n["id"])
    ns=json.loads(json.dumps(st[1])); ns["id"]="lec05kp17-u01-step1b"; ns["label"]=t["label"]; ns["speakerNotes"]=t["notes"]; ns["target"]["point"]["x"]=1440+640
    st.insert(2,ns)
    for j,s in enumerate(st): s["order"]=j
    st[3]["speakerNotes"]=st[3]["speakerNotes"].replace(t["old"],t["new"],1)
    json.dump(d,open(f,"w"),ensure_ascii=False,indent=2); print(f,len(nodes))
if __name__=="__main__":
    apply("slides/lec05-kp17-universal-approx.jbd.json","zh"); apply("slides/lec05-kp17-universal-approx-en.jbd.json","en")
