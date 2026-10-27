"""Insert a native 'CNN vs flatten-MLP' page after page 1 of KP12 (zh/en)."""
import json, re
RED,BLUE,GREEN,GOLD,ORG,GREY,TXT="#ef6b6b","#5b8def","#4fc27a","#e8c85a","#f0a050","rgba(245,241,233,0.62)","#f2ede4"
T={"zh":dict(
 title="導論:CNN 對上 flatten-MLP", sub="flatten 先把「鄰居關係」拆散;CNN 用局部核在原圖上滑,空間相關才保得住",
 bh="BEFORE · flatten → MLP", bs="二維格子被拉成一條向量,鄰居關係消失", img="影像 H×W(示例 4×4)",
 n1="左上紅格 ≈ 右下藍格", n2="在網路眼裡「同等距離」", n3="邊緣、紋理這種局部圖案學不起來",
 fl="flatten", vec="1×(H·W) 長向量(示例:1×16)", ex="示例:格數與連線為示意,非課本實際尺寸", fc="全連接:人人握手",
 ah="AFTER · CNN 局部濾波器", as_="直接在 2D 格子上滑同一顆小核,空間還在", same="同一張 4×4 影像", kern="共享核 K(3×3)", capk="實線/虛線 = 同一顆 3×3 核蓋在兩處",
 sp="稀疏:只看鄰居", sh="共享:全圖同一套", sp2="左上仍是左上的鄰居,空間還在",
 gh="三個立刻看得見的好處", g=["① 參數量大幅下降","② 自帶先驗:局部圖案到處都可能出現","③ 平移等變:輸入挪,特徵圖跟著挪"],
 mini="示例(概念示意)", rows=["輸入:原位","輸入:右移","特徵圖:原位","特徵圖:跟著右移"],
 b1="CNN = 全連接的特例:打開「稀疏連接」+「權重共享」兩個開關", b2="平移等變:輸入挪一格,特徵圖跟著挪一格(跟著走 ≠ 後面池化才講的「平移不變」)", b3="反直覺:不是「CNN 比較神」,是 flatten 先把最有用的 2D 鄰居關係丟掉了",
 label="CNN 對上 flatten", old="「局部共享規則」", new="「CNN 對上 flatten」",
 notes="承接上一頁的「局部共享規則」。這一頁用 BEFORE／AFTER 對照看為什麼要共享：左邊把 4×4 影像 flatten 成 1×16 長向量接全連接層，左上紅格與右下藍格在網路眼裡是同等距離，邊緣、紋理這種局部圖案學不起來；右邊直接在 2D 格子上滑同一顆 3×3 核，稀疏（只看鄰居）加共享（全圖同一套），空間關係還在。三個好處：參數量大幅下降、自帶局部圖案先驗、平移等變（輸入挪一格，特徵圖跟著挪一格；這不等於之後池化才講的平移不變）。結論：CNN 是全連接的特例，打開稀疏連接與權重共享兩個開關；不是 CNN 比較神，而是 flatten 先把 2D 鄰居關係丟掉了。圖中格數與連線是示意，不是課本實際尺寸。"),
 "en":dict(
 title="Intro: CNN vs flatten-MLP", sub="Flatten scatters neighbour relations; a CNN slides a local kernel over the image, so spatial correlation survives",
 bh="BEFORE · flatten → MLP", bs="The 2D grid becomes one vector; neighbours are lost", img="Image H×W (example 4×4)",
 n1="Red ≈ blue", n2="Equal distance to the network", n3="Edges and textures (local patterns) cannot be learned",
 fl="flatten", vec="1×(H·W) vector (example: 1×16)", ex="Schematic, not textbook size", fc="Fully connected",
 ah="AFTER · CNN local filter", as_="Slide one small kernel over the 2D grid; space is kept", same="Same 4×4 image", kern="Shared kernel K (3×3)", capk="Solid / dashed: same 3×3 kernel",
 sp="Sparse: neighbours", sh="Shared: one set", sp2="Top-left stays a neighbour",
 gh="Three visible benefits", g=["① Far fewer parameters","② Built-in local prior","③ Shift equivariance"],
 mini="Example (concept sketch)", rows=["input","input, shifted","feature map","map follows"],
 b1="CNN = a special case of fully connected: switch on 'sparse links' + 'weight sharing'", b2="Shift equivariance: shift the input one cell and the feature map shifts one cell (equivariant ≠ the 'shift invariance' pooling gives later)", b3="Counter-intuitive: CNN is not magic; flatten throws away the most useful 2D neighbour relation",
 label="CNN vs flatten", old="the local sharing rule", new="CNN vs flatten",
 notes="Following the previous page on the local sharing rule. This page is a BEFORE/AFTER comparison of why we share. Left: a 4×4 image flattened into a 1×16 vector feeding a fully connected layer; the top-left red cell and the bottom-right blue cell look equally far to the network, so local patterns like edges and textures cannot be learned. Right: slide one 3×3 kernel over the 2D grid: sparse (neighbours only) plus shared (one set for the whole image), so space is kept. Three benefits: far fewer parameters, a built-in local-pattern prior, and shift equivariance (shift the input one cell and the feature map shifts one cell; this is not the shift invariance that pooling gives later). Conclusion: a CNN is a special case of a fully connected layer with sparse links and weight sharing switched on; it is not magic, flatten simply throws away the 2D neighbour relation. Cells and links in the figure are schematic, not textbook size.",
 )}
def build(lang,x0,sid,pre):
    t=T[lang]; nodes=[]
    def add(typ,x,y,w,h,style,text="",kind=None,z=2):
        nid=f"{pre}-{len(nodes)+1}"
        n={"id":nid,"type":typ,"name":f"cnn#{len(nodes)+1}","sceneId":sid,"transform":{"x":x0+x,"y":y,"scaleX":1,"scaleY":1,"rotation":0},"width":max(w,1),"height":max(h,1),"zIndex":z,"locked":False,"style":style,"text":text}
        if kind:n["shapeKind"]=kind
        nodes.append(n); return n
    base=lambda **k:dict({"fill":"transparent","stroke":"transparent","textColor":TXT,"fontSize":16,"radius":0,"borderWidth":0},**k)
    def box(x,y,w,h,stroke,fill="rgba(245,241,233,0.05)",r=14,sw=2,dash=False,z=1): add("shape",x,y,w,h,base(fill=fill,stroke=stroke,radius=r,borderWidth=sw,borderStyle="dashed" if dash else "solid"),"","rectangle",z=z)
    def tx(x,y,w,h,s,size,color=TXT,bold=False,al="left"): add("text",x,y,w,h,base(textColor=color,fontSize=size,fontWeight=700 if bold else 400,textAlign=al,lineHeight=1.25),s,"rectangle",z=4)
    def pl(pts,color,sw=3,dash=False,z=3,smooth=False):
        xs=[p[0] for p in pts];ys=[p[1] for p in pts];bx,by=min(xs),min(ys);bw=max(max(xs)-bx,1);bh=max(max(ys)-by,1)
        n=add("shape",bx,by,bw,bh,base(stroke=color,borderWidth=sw,**({"borderStyle":"dashed"} if dash else {})),"","polyline",z=z)
        n["polygonPoints"]=[{"x":round((p[0]-bx)/bw*100,2),"y":round((p[1]-by)/bh*100,2)} for p in pts]
    def poly(pts,fill,z=3):
        xs=[p[0] for p in pts];ys=[p[1] for p in pts];bx,by=min(xs),min(ys);bw=max(max(xs)-bx,1);bh=max(max(ys)-by,1)
        n=add("shape",bx,by,bw,bh,base(fill=fill),"","polygon",z=z); n["polygonPoints"]=[{"x":round((p[0]-bx)/bw*100,2),"y":round((p[1]-by)/bh*100,2)} for p in pts]
    def cell(x,y,w,h,fill="#f2ede4",stroke="rgba(30,30,30,0.7)",sw=1): box(x,y,w,h,stroke,fill=fill,r=0,sw=sw,z=2)
    tx(40,8,1200,44,t["title"],32,TXT,True,"center"); tx(40,54,1200,30,t["sub"],18,GREY,False,"center")
    # BEFORE
    box(32,100,592,472,RED,fill="rgba(239,107,107,0.07)",r=16)
    tx(48,106,560,30,t["bh"],22,RED,True); tx(48,138,560,22,t["bs"],15,TXT)
    tx(60,160,260,20,t["img"],14,GREY)
    for r in range(4):
        for c in range(4): cell(72+c*38,182+r*38,38,38,RED if (r,c)==(0,0) else (BLUE if (r,c)==(3,3) else "#f2ede4"))
    box(316,190,292,124,RED,fill="transparent",r=10,sw=2,dash=True)
    tx(326,198,274,26,t["n1"],19,RED,True); tx(326,228,274,24,t["n2"],16); tx(326,262,274,44,t["n3"],15,GREY)
    pl([(145,340),(145,364)],TXT,4); poly([(137,362),(145,376),(153,362)],TXT); tx(156,346,100,22,t["fl"],16,TXT,True)
    tx(240,352,380,22,t["vec"],14,GREY)
    vx,vy,vw=72,384,32
    for i in range(16): cell(vx+i*vw if False else 72+i*31,384,31,31,RED if i==0 else (BLUE if i==15 else "#f2ede4"))
    nx=[110,230,350,470,590] if False else [120,224,328,432,536]
    for i in range(1,15,2):
        for nxx in nx: pl([(72+i*31+15,415),(nxx,498)],"rgba(245,241,233,0.14)",1,z=2)
    for nxx in nx: add("shape",nxx-10,498,20,20,base(fill=RED,stroke="rgba(30,30,30,0.7)",borderWidth=1),"","ellipse",z=3)
    pl([(87,415),(328,498)],RED,3,z=3); pl([(72+15*31+15,415),(328,498)],BLUE,3,z=3)
    tx(48,542,360,22,t["ex"],13,GREY); tx(380,538,232,26,t["fc"],17,RED,True)
    # AFTER
    box(656,100,592,472,GREEN,fill="rgba(79,194,122,0.07)",r=16)
    tx(672,106,560,30,t["ah"],22,GREEN,True); tx(672,138,560,22,t["as_"],15,TXT)
    tx(692,164,200,20,t["same"],14,GREY)
    gx,gy=692,186
    for r in range(4):
        for c in range(4): cell(gx+c*38,gy+r*38,38,38,RED if (r,c)==(0,0) else (BLUE if (r,c)==(3,3) else "#f2ede4"))
    box(gx,gy,114,114,GREEN,fill="rgba(79,194,122,0.18)",r=0,sw=3,z=3)
    box(gx+38,gy+38,114,114,GREEN,fill="transparent",r=0,sw=3,dash=True,z=3)
    pl([(gx+158,gy+34),(940,gy+40)],GREEN,3); poly([(938,gy+30),(954,gy+40),(938,gy+50)],GREEN)
    tx(965,164,260,22,t["kern"],16,TXT,True)
    kw=[["w11","w12","w13"],["w21","w22","w23"],["w31","w32","w33"]]
    for r in range(3):
        for c in range(3):
            box(966+c*38,190+r*34,38,34,GREEN,fill="rgba(79,194,122,0.28)",r=0,sw=1,z=2); tx(966+c*38,190+r*34+6,38,22,kw[r][c],13,TXT,False,"center")
    tx(676,346,360,40,t["capk"],14,GREY)
    tx(972,300,270,24,t["sp"],18,TXT,True); tx(972,326,270,24,t["sh"],18,TXT,True); tx(972,356,270,40,t["sp2"],15,GREY)
    tx(676,400,300,26,t["gh"],18,TXT,True)
    for i,s in enumerate(t["g"]): tx(688,432+i*34,300,34,s,14,TXT)
    tx(1000,404,244,20,t["mini"],13,GREY)
    cw=18
    for k,(lab,hi,col) in enumerate(((t["rows"][0],2,GREEN),(t["rows"][1],4,GREEN),(t["rows"][2],0,ORG),(t["rows"][3],3,ORG))):
        y=430+k*34
        for i in range(6): cell(1000+i*cw,y,cw,24,col if i==hi else "#f2ede4")
        tx(1112,y+2,134,20,lab,13,GREY)
    box(32,588,1216,116,"rgba(120,150,255,0.6)",fill="rgba(30,58,160,0.55)",r=16)
    tx(48,596,1184,34,t["b1"],23,TXT,True,"center"); tx(48,634,1184,26,t["b2"],15,"rgba(245,241,233,0.8)",False,"center"); tx(48,664,1184,26,t["b3"],16,GOLD,True,"center")
    return nodes
def apply(f,lang):
    t=T[lang]; d=json.load(open(f)); N=d["nodes"]; sc=d["scenes"]["lec05kp12-scene-u01"]; st=d["steps"]
    pat=re.compile(r"lec05kp12-u01-p(\d+)-")
    for k,v in N.items():
        m=pat.match(k)
        if m and int(m.group(1))>=2: v["transform"]["x"]+=1440
    for s in st[2:]: s["target"]["point"]["x"]+=1440
    nodes=build(lang,1440,"lec05kp12-scene-u01","lec05kp12-u01-p1b")
    ids=sc["nodeIds"]; i=max(j for j,k in enumerate(ids) if k.startswith("lec05kp12-u01-p1-"))+1
    for j,n in enumerate(nodes): N[n["id"]]=n; ids.insert(i+j,n["id"])
    ns=json.loads(json.dumps(st[1])); ns["id"]="lec05kp12-u01-step1b"; ns["label"]=t["label"]; ns["speakerNotes"]=t["notes"]; ns["target"]["point"]["x"]=1440+640
    st.insert(2,ns)
    for j,s in enumerate(st): s["order"]=j
    st[3]["speakerNotes"]=st[3]["speakerNotes"].replace(t["old"],t["new"],1)
    json.dump(d,open(f,"w"),ensure_ascii=False,indent=2); print(f,len(nodes))
if __name__=="__main__":
    apply("slides/lec05-kp12-weight-sharing.jbd.json","zh"); apply("slides/lec05-kp12-weight-sharing-en.jbd.json","en")
