"""Replace the image on KP13's comparison page with native nodes (zh/en)."""
import json, sys
BLUE,GREEN,ORG,RED,TXT="#6aa8ff","#5fd08a","#f0a050","#ef6b6b","#f2ede4"
T={"zh":dict(
 h1="廣義線性分類器",h2="投影追蹤",
 fa=r"$g(\boldsymbol{x})=\sum_i w_i f_i(\boldsymbol{x})$", fb=r"$g(\boldsymbol{x})=\sum_i f_i(\boldsymbol{w}_i^{T}\boldsymbol{x})$",
 inp="輸入向量\n$\\boldsymbol{x}$", out="輸出\n$g(\\boldsymbol{x})$",
 a_top=("固定的非線性映射","fᵢ 事先決定,不可學習"), a_bot=("可學習的線性權重","wᵢ 可用正規方程直接求解"),
 b_top=("可學習的投影方向","尋找最佳投影角度 wᵢ"), b_bot=("需配適的非線性函數 fᵢ","隨投影方向調整,如 Sigmoid"),
 a_lin="對參數 w 呈線性", b_lin="對參數 w 呈非線性",
 a_dbl=r"加倍測試 $g(2\boldsymbol{w})=2g(\boldsymbol{w})$", b_dbl=r"加倍測試 $f(2\boldsymbol{w}_i^{T}\boldsymbol{x})\neq 2f(\boldsymbol{w}_i^{T}\boldsymbol{x})$",
 a_ok="✓ 權重加倍,輸出剛好加倍",b_ex="例如 f(2) = 0.881 ≠ 2f(1)"),
 "en":dict(
 h1="Generalized linear classifier",h2="Projection pursuit",
 fa=r"$g(\boldsymbol{x})=\sum_i w_i f_i(\boldsymbol{x})$", fb=r"$g(\boldsymbol{x})=\sum_i f_i(\boldsymbol{w}_i^{T}\boldsymbol{x})$",
 inp="Input\n$\\boldsymbol{x}$", out="Output\n$g(\\boldsymbol{x})$",
 a_top=("Fixed nonlinear map","f_i chosen in advance, not learned"), a_bot=("Linear weights","w_i by normal equations"),
 b_top=("Projection direction","learnable: find the best direction w_i"), b_bot=("Nonlinear function","f_i is fitted, e.g. sigmoid"),
 a_lin="Linear in the parameters w", b_lin="Nonlinear in the parameters w",
 a_dbl=r"Doubling test $g(2\boldsymbol{w})=2g(\boldsymbol{w})$", b_dbl=r"Doubling test $f(2\boldsymbol{w}_i^{T}\boldsymbol{x})\neq 2f(\boldsymbol{w}_i^{T}\boldsymbol{x})$",
 a_ok="✓ Double w and g doubles",b_ex="e.g. f(2) = 0.881 ≠ 2f(1)")}
def build(lang,x0,sid,pre):
    t=T[lang]; nodes=[]; ids=[]
    def add(typ,x,y,w,h,style,text="",kind=None,z=2,rot=0):
        nid=f"{pre}-{len(nodes)+1}"
        n={"id":nid,"type":typ,"name":f"gl-vs-pp#{len(nodes)+1}","sceneId":sid,"transform":{"x":x0+x,"y":y,"scaleX":1,"scaleY":1,"rotation":rot},"width":max(w,1),"height":max(h,1),"zIndex":z,"locked":False,"style":style,"text":text}
        if kind:n["shapeKind"]=kind
        nodes.append(n); return n
    base=lambda **k:dict({"fill":"transparent","stroke":"transparent","textColor":TXT,"fontSize":16,"radius":0,"borderWidth":0},**k)
    def box(x,y,w,h,stroke,fill="rgba(245,241,233,0.05)",r=14,sw=3): add("shape",x,y,w,h,base(fill=fill,stroke=stroke,radius=r,borderWidth=sw,borderStyle="solid"),"","rectangle",z=1)
    def tx(x,y,w,h,s,size,color=TXT,bold=False,al="center"): add("text",x,y,w,h,base(textColor=color,fontSize=size,fontWeight=700 if bold else 400,textAlign=al,lineHeight=1.3),s,"rectangle",z=3)
    def pl(pts,color,sw=4,smooth=False,dash=False):
        xs=[p[0] for p in pts];ys=[p[1] for p in pts];bx,by=min(xs),min(ys);bw=max(max(xs)-bx,1);bh=max(max(ys)-by,1)
        n=add("shape",bx,by,bw,bh,base(stroke=color,borderWidth=sw,**({"borderStyle":"dashed"} if dash else {})),"","polyline")
        n["polygonPoints"]=[dict({"x":round((p[0]-bx)/bw*100,2),"y":round((p[1]-by)/bh*100,2)},**({"smooth":True} if smooth else {})) for p in pts]
    def head(x,y,color,d=14): # right-pointing arrowhead
        add("shape",x-d,y-d/2,d,d,base(fill=color),"","polygon").__setitem__("polygonPoints",[{"x":0,"y":0},{"x":100,"y":50},{"x":0,"y":100}])
    for side,ox,acc,ttl,form,top,bot,lin,dbl,okc in (("a",30,BLUE,t["h1"],t["fa"],t["a_top"],t["a_bot"],t["a_lin"],t["a_dbl"],GREEN),("b",650,ORG,t["h2"],t["fb"],t["b_top"],t["b_bot"],t["b_lin"],t["b_dbl"],RED)):
        X=lambda v:ox+v
        box(ox,14,600,692,acc,r=18,sw=2)
        box(X(60),28,480,62,acc,fill="rgba(245,241,233,0.07)")
        tx(X(60),36,480,46,ttl,32,acc,True)
        tx(X(40),104,520,52,form,28)
        # flow
        box(X(20),322,120,90,acc,fill="rgba(245,241,233,0.08)",r=12); tx(X(20),328,120,78,t["inp"],20,TXT,True)
        for ty in (262,452):
            pl([(X(140),367),(X(172),367),(X(172),ty),(X(214),ty)],acc,4,smooth=False); head(X(224),ty,acc)
        box(X(224),190,200,150,acc); tx(X(230),200,188,34,top[0],19,acc,True); tx(X(230),284,188,52,top[1],16,TXT)
        box(X(224),380,200,150,acc); tx(X(230),390,188,34,bot[0],19,acc,True); tx(X(230),474,188,52,bot[1],16,TXT)
        for ty in (262,452):
            pl([(X(424),ty),(X(446),ty),(X(446),367),(X(474),367)],GREEN,4)
        head(X(486),367,GREEN)
        tx(X(488),326,106,82,t["out"],20,TXT,True)
        # small icons
        if side=="a": # padlock-ish: body + shackle
            add("shape",X(300),248,40,30,base(fill=acc),"","rectangle"); pl([(X(306),248),(X(306),232),(X(334),232),(X(334),248)],acc,5)
            for k,hh in enumerate((20,36,28)): add("shape",X(278+k*40),452-hh,24,hh,base(fill=acc),"","rectangle")
        else:
            pl([(X(262),262),(X(290),232),(X(318),262),(X(346),236),(X(380),262)],acc,4,smooth=True)
            pl([(X(262),446),(X(288),420),(X(314),446),(X(340),420),(X(366),446),(X(386),430)],acc,4,smooth=True)
        # bottom
        tx(X(20),556,560,34,lin,24,TXT,True)
        box(X(20),600,560,92,okc,fill="rgba(245,241,233,0.05)",r=12,sw=2)
        tx(X(30),608,540,40,dbl,24,okc,True)
        tx(X(30),652,540,32,t["b_ex"] if side=="b" else t["a_ok"],20,okc if side=="a" else TXT)
    return nodes
def apply(f,lang):
    d=json.load(open(f)); N=d["nodes"]; sc=d["scenes"]["lec05kp13-scene-u01"]
    old=N.pop("lec05kp13-u01-p8b-fig"); x0=old["transform"]["x"]
    ids=sc["nodeIds"]; i=ids.index("lec05kp13-u01-p8b-fig"); ids.pop(i)
    nodes=build(lang,x0,"lec05kp13-scene-u01","lec05kp13-u01-p8b")
    for j,n in enumerate(nodes): N[n["id"]]=n; ids.insert(i+j,n["id"])
    json.dump(d,open(f,"w"),ensure_ascii=False,indent=2); print(f,len(nodes))
if __name__=="__main__":
    apply("slides/lec05-kp13-generalized-linear.jbd.json","zh"); apply("slides/lec05-kp13-generalized-linear-en.jbd.json","en")
