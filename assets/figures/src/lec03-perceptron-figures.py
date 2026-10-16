"""Reproduce source-data figures in white and dark styles. Run from the course root."""
from pathlib import Path
import sys,json,base64
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'.agents/skills/view-from-text'))
from jbd_figure import use_jbd_style,new_figure,svg_data_uri,check_not_clipped

OUT=ROOT/'assets/figures'; OUT.mkdir(parents=True,exist_ok=True)
X2=np.array([[.4,.05],[.8,.6],[.5,.9],[.9,.2],[-.2,.75],[-.6,.2],[-.3,-.4],[.1,-.5]])
y2=np.array([1]*4+[-1]*4)
X4=np.array([[-1,0],[0,1],[0,-1],[1,0]]); y4=np.array([1,1,-1,-1])
X5=np.array([[1.8,1.8],[1.2,1],[-1.8,-1.4],[-1,-1.8],[.45,.35],[-1.8,1.7],[-1.2,1],[1.8,-1.5],[1.1,-1.8],[.2,-.45],[-.35,.5]])
y5=np.array([1]*5+[-1]*6)
def A(X):return np.c_[X,np.ones(len(X))]
def boundary(ax,v,xlim,color,ls,label):
    xs=np.linspace(*xlim,600)
    if abs(v[1])>1e-12:ax.plot(xs,-(v[0]*xs+v[2])/v[1],color=color,ls=ls,lw=2.2,label=label)
    else:ax.plot([-v[2]/v[0]]*2,[-10,10],color=color,ls=ls,lw=2.2,label=label)
def points(ax,X,y,c):
    for lab,mark,col in [(1,'o',c['pos']),(-1,'^',c['neg'])]:
        ax.scatter(*X[y==lab].T,c=col,marker=mark,s=65,zorder=4,edgecolors=c['text'],linewidths=.4,label=f'y = {lab:+d}')
def style(dark):
    use_jbd_style(22)
    if dark:return dict(pos='#d97757',neg='#6a9fd6',edge='#e0995f',aux='#5fb8a8',text='#f2ede4',muted='#b7b0a5',ok='#7dbb8c')
    plt.rcParams.update({'text.color':'#242424','axes.labelcolor':'#242424','axes.edgecolor':'#555555','xtick.color':'#555555','ytick.color':'#555555','grid.color':'#aaaaaa','figure.facecolor':'white','savefig.transparent':False})
    return dict(pos='#aa4a27',neg='#1b66a4',edge='#99601e',aux='#087969',text='#242424',muted='#555555',ok='#237438')
FIGS={}
def make(kind,dark):
    c=style(dark); fig,ax=new_figure(620,420,margins_px=(96,76,26,70))
    ax.tick_params(labelsize=12); ax.set_xlabel(r'$x_1$'); ax.set_ylabel(r'$x_2$')
    if kind=='kp02-boundaries':
        points(ax,X2,y2,c)
        boundary(ax,[1,1,-.5],(-.85,1.1),c['muted'],'--','before')
        boundary(ax,[1.42,.51,-.5],(-.85,1.1),c['edge'],'-','after')
        ax.annotate('A',X2[0],xytext=(8,-20),textcoords='offset points',color=c['text'])
        ax.annotate('B',X2[4],xytext=(-19,8),textcoords='offset points',color=c['text'])
        ax.set(xlim=(-.85,1.1),ylim=(-.7,1.15));ax.set_aspect('equal')
        alt='來源8點資料；虛線為初始邊界，實線為1.42x1+0.51x2-0.5=0。A、B更新後分數為0.0935與-0.4015，8點均嚴格分對。'
    elif kind=='kp04-online':
        points(ax,X4,y4,c);boundary(ax,[-1,1,0],(-1.4,1.4),c['edge'],'-','final')
        for p,label,off in zip(X4,'ABCD',[(-20,-3),(8,5),(8,-4),(8,5)]):ax.annotate(label,p,xytext=off,textcoords='offset points',color=c['text'])
        ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4));ax.set_aspect('equal')
        alt='原例3.2四點A=(-1,0)、B=(0,1)、C=(0,-1)、D=(1,0)，最終邊界x1=x2。圓點正類、三角形負類，四點均嚴格分對。'
    elif kind=='kp05-boundaries':
        points(ax,X5,y5,c);boundary(ax,[.3,-.4,.2],(-2.2,2.2),c['muted'],'--','initial / pocket')
        boundary(ax,[-.785,.9125,-.85],(-2.2,2.2),c['edge'],'-','after one update')
        ax.set(xlim=(-2.2,2.2),ylim=(-2.2,2.2));ax.set_aspect('equal')
        alt='來源11點資料，共5正類圓點與6負類三角形；初始虛線分對8點，第一次批次更新後實線只分對4點，因此口袋保留初始線。'
    elif kind=='kp03-bound':
        t=np.arange(301); r=1/(t+1); u=8+2*(np.cumsum(r*r)-np.cumsum(r))
        ax.plot(t,u,color=c['aux'],label='hypothetical bound')
        ax.plot([0,300],[0,0],color=c['edge'],ls='--',label='zero')
        ax.scatter([2,20,80],u[[2,20,80]],s=35,color=c['edge'],zorder=4)
        ax.set(xlim=(0,300),ylim=(-1.6,8.5),xlabel='update index t',ylabel=r'$U_t$')
        alt='來源純量示例D0=8、B平方=2，步長1/(t+1)；假設無窮更新的上界越過零線，負值只代表假設矛盾，不是真實負距離。'
    elif kind=='kp05-errors':
        v=np.array([.3,-.4,.2]); best=int(np.sum(y5*(A(X5)@v)>0)); err=[11-best]; be=[11-best]
        for _ in range(80):
            bad=y5*(A(X5)@v)<=0;v+=.35*(y5[bad,None]*A(X5)[bad]).sum(axis=0)
            cor=int(np.sum(y5*(A(X5)@v)>0));best=max(best,cor);err.append(11-cor);be.append(11-best)
        ax.plot(range(81),err,color=c['edge'],lw=2,label='current mistakes')
        ax.step(range(81),be,color=c['ok'],lw=3,where='post',label='pocket mistakes')
        ax.set(xlim=(0,80),ylim=(-.2,11.2),xlabel='updates',ylabel='mistakes / 11');ax.set_yticks([0,3,6,9,11])
        alt='同一11點、初值(0.3,-0.4,0.2)與步長0.35的80次批次更新。當前錯誤可增加，口袋歷史最佳錯誤數保持不增加。'
    ax.legend(loc='lower center',bbox_to_anchor=(.5,1.015),ncol=2,frameon=False,fontsize=11)
    ax.grid(alpha=.15)
    clipped=check_not_clipped(fig)
    if clipped:raise RuntimeError((kind,clipped))
    stem='lec03-'+kind
    if dark:
        fig.savefig(OUT/(stem+'-dark.png'),dpi=150,transparent=False,facecolor='#151513')
        uri=svg_data_uri(fig)
        (OUT/(stem+'.svg')).write_bytes(base64.b64decode(uri.split(',',1)[1]))
        FIGS[stem]={'uri':uri,'w':620,'h':420,'alt':alt}
    else:
        fig.savefig(OUT/(stem+'.png'),dpi=200,facecolor='white');plt.close(fig)
for k in ['kp02-boundaries','kp03-bound','kp04-online','kp05-boundaries','kp05-errors']:
    for d in [False,True]:make(k,d)
(ROOT/'figs.json').write_text(json.dumps(FIGS,ensure_ascii=False),encoding='utf-8')
print('5 figures, white PNG + dark SVG, clipping checks passed')
