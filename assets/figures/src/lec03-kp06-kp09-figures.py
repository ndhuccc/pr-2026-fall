"""Reproduce PR Chapter 3 KP06--KP09 figures. Run from any directory.
Requires numpy and matplotlib. Source coordinates and weights are embedded.
LMS reproduces the source Mulberry32 / Box-Muller stream, seed 0x3a7f21.
Produces white PNGs and dark SVGs from identical numerical data.
"""
from pathlib import Path
import json,math,sys,base64
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
OUT=Path(__file__).resolve().parents[1];OUT.mkdir(exist_ok=True,parents=True)
plt.rcParams.update({'mathtext.fontset':'cm','svg.fonttype':'path','font.family':'DejaVu Sans','font.size':15.84})
W=np.array([[5.13,3.60,1.00],[-.05,-3.16,-.41],[-3.84,1.28,.69]])
A=np.array([[1,1],[2,2],[2,1],[1,-1],[1,-2],[2,-2],[-1,1],[-1,2],[-2,1]],float)
D=np.array([[.2,.7],[.3,.3],[.4,.5],[.6,.5],[.1,.4],[.4,.6],[.6,.2],[.7,.4],[.8,.6],[.7,.5]])
X=np.c_[D,np.ones(10)];Y=np.r_[np.ones(5),-np.ones(5)];wl=np.linalg.lstsq(X,Y,rcond=None)[0]
def sample_stream():
 state=0x3a7f21
 def rng():
  nonlocal state
  state=(state+0x6D2B79F5)&0xffffffff;v=((state^(state>>15))*(1|state))&0xffffffff
  v^=(v+(((v^(v>>7))*(61|v))&0xffffffff))&0xffffffff
  return ((v^(v>>14))&0xffffffff)/4294967296
 def normal():return math.sqrt(-2*math.log(max(5e-324,1-rng())))*math.cos(2*math.pi*(1-rng()))
 samples=[]
 for _ in range(260):
  x=normal();samples.append((x,1.8*x+.28*normal()))
 return samples
def lms(rho):
 w=0.;h=[w]
 for x,y in sample_stream():w+=rho*x*(y-x*w);h.append(w)
 return np.array(h)
def palette(dark):
 return dict(text='#f2ede4' if dark else '#252521',muted='#b7b0a5' if dark else '#686860',
  colors=['#d97757','#6a9fd6','#b49acb'] if dark else ['#be6244','#327bb6','#805aad'],
  edge='#e0995f' if dark else '#936621',vec='#5fb8a8' if dark else '#007c72',warn='#e07a70' if dark else '#bc3949')
def style(ax,c):
 ax.tick_params(colors=c['muted'],labelsize=12)
 for sp in ax.spines.values():sp.set_color(c['muted'])
 ax.xaxis.label.set_color(c['text']);ax.yaxis.label.set_color(c['text']);ax.grid(alpha=.12)
 ax.set_facecolor('none')
def regions(dark):
 c=palette(dark);fig,ax=plt.subplots(figsize=(6.2,4.4));fig.subplots_adjust(left=.13,right=.97,bottom=.15,top=.86)
 xx=np.linspace(-3,3,440);gx,gy=np.meshgrid(xx,xx);G=np.c_[gx.ravel(),gy.ravel(),np.ones(gx.size)]@W.T
 cls=G.argmax(1).reshape(gx.shape);ax.contourf(gx,gy,cls,levels=[-.5,.5,1.5,2.5],colors=c['colors'],alpha=.15)
 for i in range(3):
  ax.scatter(A[i*3:i*3+3,0],A[i*3:i*3+3,1],c=c['colors'][i],marker=['o','^','s'][i],s=68,label=f'Class {i+1}',zorder=4)
 for i,j in [(0,1),(0,2),(1,2)]:
  diff=(G[:,i]-G[:,j]).reshape(gx.shape);ax.contour(gx,gy,diff,levels=[0],colors=[c['muted']],linewidths=1,linestyles='--',alpha=.7)
 
 for i,j in [(0,1),(0,2),(1,2)]:
  h=3-i-j;diff=(G[:,i]-G[:,j]).reshape(gx.shape);active=(np.maximum(G[:,i],G[:,j])>=G[:,h]-.03).reshape(gx.shape)
  ax.contour(gx,gy,np.ma.masked_where(~active,diff),levels=[0],colors=[c['edge']],linewidths=2)
 ax.set(xlim=(-3,3),ylim=(-3,3),xlabel=r'$x_1$',ylabel=r'$x_2$');ax.set_aspect('equal');style(ax,c)
 leg=fig.legend(*ax.get_legend_handles_labels(),loc='upper center',bbox_to_anchor=(.53,.99),ncol=3,frameon=False,fontsize=13)
 for t in leg.get_texts():t.set_color(c['text'])
 return fig
def projection(dark):
 c=palette(dark);fig=plt.figure(figsize=(6.2,4.4));ax=fig.add_subplot(111,projection='3d');fig.subplots_adjust(left=0,right=1,bottom=0,top=.93)
 b1=np.array([1.,0,0]);b2=np.array([.5,np.sqrt(3)/2,0]);y=np.array([1.35,.85,1.25]);p=y.copy();p[2]=0
 verts=[[(0,0,0),(2.1,0,0),(2.1,1.65,0),(0,1.65,0)]]
 plane=Poly3DCollection(verts,facecolors=c['vec'],alpha=.13,edgecolors=c['muted'],linewidths=.6);ax.add_collection3d(plane)
 for b,txt in [(b1,r'$b_1$'),(b2,r'$b_2$')]:
  ax.quiver(0,0,0,*b,color=c['vec'],arrow_length_ratio=.12,linewidth=2.2);ax.text(*(b+np.array([.02,.03,.03])),txt,color=c['text'],fontsize=15)
 ax.quiver(0,0,0,*p,color=c['colors'][1],arrow_length_ratio=.07,linewidth=2)
 ax.plot([p[0],y[0]],[p[1],y[1]],[p[2],y[2]],'--',color=c['warn'],linewidth=2)
 ax.scatter(*y,color=c['text'],s=42);ax.scatter(*p,color=c['colors'][1],s=40)
 ax.text(*(y+np.array([.04,.04,.04])),r'$y$',color=c['text'],fontsize=16);ax.text(*(p+np.array([.08,-.05,.07])),r'$\hat y$',color=c['colors'][1],fontsize=16)
 a=p+np.array([.15,0,0]);b=a+np.array([0,0,.15]);d=p+np.array([0,0,.15]);ax.plot(*np.array([a,b,d]).T,color=c['warn'],linewidth=1.8)
 ax.text(1.43,.88,.65,r'$e$',color=c['warn'],fontsize=16)
 ax.set(xlim=(0,2.1),ylim=(0,1.65),zlim=(0,1.6),xlabel='axis 1',ylabel='axis 2',zlabel='axis 3');ax.set_box_aspect((2.1,1.65,1.6));ax.view_init(elev=24,azim=-60)
 ax.tick_params(colors=c['muted'],labelsize=10,pad=0)
 for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.label.set_color(c['muted']);axis.pane.set_alpha(0);axis._axinfo['grid']['color']=(.5,.5,.5,.13)
 ax.set_facecolor('none');return fig
def trajectory(dark):
 c=palette(dark);fig,axs=plt.subplots(2,1,figsize=(6.2,4.4),sharex=True,gridspec_kw={'height_ratios':[2,1]});fig.subplots_adjust(left=.13,right=.97,bottom=.13,top=.86,hspace=.22)
 for rho,col in zip([.005,.08,.25],c['colors']):axs[0].plot(lms(rho),color=col,lw=1.5,label=f'{rho:.3f}')
 axs[0].axhline(1.8,color=c['muted'],ls='--',lw=1.2);axs[0].set(ylim=(-.1,2.45),ylabel=r'$\hat w_k$');axs[0].text(180,1.9,r'$w^*=1.8$',color=c['muted'],fontsize=13)
 axs[1].plot(np.arange(1,261),np.diff(lms(.08)),color=c['vec'],lw=1);axs[1].axhline(0,color=c['muted'],lw=.7);axs[1].set(xlim=(0,260),ylim=(-.17,.34),ylabel=r'$\Delta w$',xlabel='sample k')
 for ax in axs:style(ax,c)
 leg=fig.legend(*axs[0].get_legend_handles_labels(),title='step size',loc='upper center',bbox_to_anchor=(.54,1.01),ncol=3,frameon=False,fontsize=12,title_fontsize=12)
 for t in leg.get_texts()+[leg.get_title()]:t.set_color(c['text'])
 return fig
def boundary(dark):
 c=palette(dark);fig,ax=plt.subplots(figsize=(6.2,4.4));fig.subplots_adjust(left=.13,right=.97,bottom=.15,top=.85)
 xx=np.linspace(0,1,440);gx,gy=np.meshgrid(xx,xx);g=wl[0]*gx+wl[1]*gy+wl[2]
 ax.contourf(gx,gy,g,levels=[-10,0,10],colors=[c['colors'][1],c['colors'][0]],alpha=.12)
 ax.contour(gx,gy,g,levels=[0],colors=[c['edge']],linewidths=2)
 for i in range(2):ax.scatter(D[i*5:i*5+5,0],D[i*5:i*5+5,1],c=c['colors'][i],marker=['o','^'][i],s=65,label=f'Class {i+1}',zorder=4)
 bad=(X@wl)*Y<=0;ax.scatter(D[bad,0],D[bad,1],facecolors='none',edgecolors=c['warn'],s=250,linewidth=1.8,label='Misclassified',zorder=5)
 for i in [3,5]:
  ax.annotate(f'({D[i,0]:.1f}, {D[i,1]:.1f})',D[i],xytext=(D[i,0]+(.12 if i==3 else -.27),D[i,1]+(.12 if i==3 else .15)),color=c['text'],fontsize=13,arrowprops=dict(arrowstyle='->',color=c['warn']))
 ax.set(xlim=(0,1),ylim=(0,1),xlabel=r'$x_1$',ylabel=r'$x_2$');ax.set_aspect('equal');style(ax,c)
 leg=fig.legend(*ax.get_legend_handles_labels(),loc='upper center',bbox_to_anchor=(.53,.99),ncol=3,frameon=False,fontsize=12)
 for t in leg.get_texts():t.set_color(c['text'])
 return fig
FUNCTIONS={'lec03-kp06-regions':regions,'lec03-kp07-projection':projection,'lec03-kp08-trajectory':trajectory,'lec03-kp09-boundary':boundary}
ALTS={'lec03-kp06-regions':'Example 3.3 nine exact data points, maximum of three source scores, dashed pairwise equality lines and final classification borders.','lec03-kp07-projection':'Two bases in the z=0 plane, target (1.35,0.85,1.25), projection (1.35,0.85,0), vertical residual and right-angle marker.','lec03-kp08-trajectory':'LMS weight paths at steps 0.005, 0.08 and 0.25 for the same 260 seeded samples, true weight 1.8, and signed corrections at step 0.08.','lec03-kp09-boundary':'Example 3.4 ten exact samples with the full-precision least-squares decision line and rings at the two errors (0.6,0.5) and (0.4,0.6).'}
if __name__=='__main__':
 figs={}
 for key,fn in FUNCTIONS.items():
  fig=fn(False);fig.savefig(OUT/(key+'.png'),dpi=200,facecolor='white');plt.close(fig)
  fig=fn(True);fig.savefig(OUT/(key+'.svg'),transparent=True);fig.savefig(OUT/(key+'-dark.png'),dpi=150,facecolor='#151513');plt.close(fig)
  b=(OUT/(key+'.svg')).read_bytes();figs[key]={'w':620,'h':440,'uri':'data:image/svg+xml;base64,'+base64.b64encode(b).decode(),'alt':ALTS[key]};print(key,len(b))
 work=Path(sys.argv[1]) if len(sys.argv)>1 else OUT
 (work/'figs.json').write_text(json.dumps(figs,ensure_ascii=False),encoding='utf-8')
