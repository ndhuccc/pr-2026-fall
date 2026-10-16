"""Recreate the seven KP14--KP18 figures. Requires numpy, scipy, matplotlib.
Run compute_examples.py first; numerical results retain the source point sets.
"""
from pathlib import Path
import sys,json,base64,itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle
from scipy.spatial import ConvexHull
from jbd_figure import use_jbd_style,check_not_clipped,check_svg
R=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R))
from compute_examples import SQUARE,Y4,SOFT,YS,POS,NEG,SEP,CODE,RECEIVED
E=json.loads((R/'examples.json').read_text(encoding='utf-8'))
use_jbd_style(22)
def colors(dark):return {'text':'#f2ede4' if dark else '#252521','muted':'#b7b0a5' if dark else '#66665f','pos':'#6a9fd6' if dark else '#286da6','neg':'#d97757' if dark else '#b85337','line':'#5fb8a8' if dark else '#007d70','warn':'#e07a70' if dark else '#b63743'}
def style(ax,c,equal=False):
 ax.tick_params(colors=c['muted'],labelsize=11)
 for sp in ax.spines.values():sp.set_color(c['muted'])
 ax.xaxis.label.set_color(c['text']);ax.yaxis.label.set_color(c['text']);ax.set_facecolor('none');ax.grid(alpha=.10)
 if equal:ax.set_aspect('equal',adjustable='box')
def base(two=False):
 fig,ax=plt.subplots(1,2 if two else 1,figsize=(6.2,4.4));fig.subplots_adjust(left=.13,right=.97,bottom=.18,top=.80,wspace=.35);return fig,ax
def classes(ax,A,B,c):
 ax.scatter(A[:,0],A[:,1],s=32,c=c['pos'],marker='o',zorder=4);ax.scatter(B[:,0],B[:,1],s=38,c=c['neg'],marker='^',zorder=4)
def scorelines(ax,w,b,c,bounds,band=True):
 xx=np.linspace(bounds[0],bounds[1],500);yy=np.linspace(bounds[2],bounds[3],500);X,Y=np.meshgrid(xx,yy);Z=w[0]*X+w[1]*Y+b
 if band:ax.contourf(X,Y,Z,levels=[-1,1],colors=[c['line']],alpha=.10)
 ax.contour(X,Y,Z,levels=[0],colors=[c['line']],linewidths=2)
 if band:ax.contour(X,Y,Z,levels=[-1,1],colors=[c['line']],linewidths=1.2,linestyles='--')
def square(dark):
 c=colors(dark);fig,axs=base(True)
 for ax,w,title in zip(axs,[np.array([1.,0]),np.array([2.,1])],['optimal: width 2','tilted: width 0.8944']):
  scorelines(ax,w,0,c,[-1.65,1.65,-1.65,1.65]);classes(ax,SQUARE[:2],SQUARE[2:],c);ax.set(xlim=(-1.65,1.65),ylim=(-1.65,1.65),xlabel=r'$x_1$');ax.set_title(title,fontsize=12,color=c['text']);style(ax,c,True)
 axs[0].set_ylabel(r'$x_2$');axs[0].annotate('',(-1,0),(1,0),arrowprops={'arrowstyle':'<->','color':c['warn']});axs[0].plot([0,.13,.13],[.13,.13,0],c=c['warn'],lw=1)
 fig.text(.54,.94,'Same source square; full width vs half width',ha='center',fontsize=12,color=c['text']);return fig
def hinge(dark):
 c=colors(dark);fig,ax=base();q=np.linspace(-1.1,2,500);ax.plot(q,np.maximum(0,1-q),c=c['line'],lw=2.8)
 for a,b,tx,ty in [(-.5,1.5,-.95,1.9),(.4,.6,.65,1.1),(1.4,0,1.15,.4)]:
  ax.scatter([a],[b],s=55,c=c['warn'],zorder=5);ax.annotate(f'({a:g}, {b:g})',(a,b),xytext=(tx,ty),fontsize=12,color=c['text'],arrowprops={'arrowstyle':'->','color':c['muted']})
 ax.axvline(0,c=c['muted'],ls=':',lw=1);ax.axvline(1,c=c['muted'],ls='--',lw=1);ax.set(xlim=(-1.1,2),ylim=(-.13,2.2),xlabel=r'labeled score $q=yg$',ylabel=r'slack $\max(0,1-q)$');style(ax,c);fig.text(.53,.94,'Tie at q=0; zero hinge loss begins at q=1',ha='center',fontsize=12,color=c['text']);return fig
def ccompare(dark):
 c=colors(dark);fig,axs=base(True)
 for ax,v in zip(axs,E['soft']):
  scorelines(ax,np.array(v['w']),v['b'],c,[-2.1,2.1,-1.75,1.95]);classes(ax,SOFT[:5],SOFT[5:],c)
  idx=np.where(np.array(v['alpha'])>1e-7)[0];ax.scatter(SOFT[idx,0],SOFT[idx,1],s=95,facecolors='none',edgecolors=c['line'],lw=1,zorder=6)
  ax.set(xlim=(-2.1,2.1),ylim=(-1.75,1.95),xlabel=r'$x_1$');ax.set_title(f"C={v['C']:g}\nwidth={v['width']:.4f}; SV={v['sv']}",color=c['text'],fontsize=12);style(ax,c,True)
 axs[0].set_ylabel(r'$x_2$');fig.text(.54,.96,'Source demo points: separable, n=10',ha='center',fontsize=12,color=c['text']);return fig
def ecoc(dark):
 c=colors(dark);fig,axs=plt.subplots(1,2,figsize=(6.2,4.4),gridspec_kw={'width_ratios':[1.35,1]});fig.subplots_adjust(left=.08,right=.97,bottom=.17,top=.81,wspace=.42)
 ax,bar=axs;mat=np.vstack([CODE,RECEIVED]);ax.imshow(mat,cmap=matplotlib.colors.ListedColormap([c['neg'],c['pos']]),vmin=-1,vmax=1,alpha=.32,aspect='equal')
 for i in range(5):
  for j in range(6):ax.text(j,i,'+' if mat[i,j]>0 else '−',ha='center',va='center',fontsize=15,color=c['text'])
 ax.add_patch(Rectangle((.5,3.5),1,1,fill=False,ec=c['warn'],lw=2.3));ax.axhline(3.5,c=c['muted'],lw=1.5);ax.set_xticks(range(6),range(1,7));ax.set_yticks(range(5),['c1','c2','c3','c4','s']);ax.set_xlabel('binary task');ax.set_title('Source code + received bits',fontsize=11,color=c['text']);style(ax,c)
 ds=E['ecoc']['received_distances'];bar.barh(np.arange(4),ds,color=[c['line'],c['muted'],c['muted'],c['muted']],alpha=.85);bar.invert_yaxis();bar.set_yticks(range(4),['c1','c2','c3','c4']);bar.set(xlim=(0,4.8),xlabel='Hamming distance');bar.set_xticks([0,2,4])
 for j,v in enumerate(ds):bar.text(v+.12,j,str(v),va='center',fontsize=13,color=c['text'])
 style(bar,c);fig.text(.52,.95,'One wrong bit; nearest codeword is still c1',ha='center',fontsize=12,color=c['text']);return fig
def nubounds(dark):
 c=colors(dark);fig,ax=base();t=np.linspace(0,1,500);ax.fill_between(t,0,t,color=c['warn'],alpha=.06);ax.fill_between(t,t,1,color=c['pos'],alpha=.05);ax.plot(t,t,c=c['muted'],ls='--',lw=1.2,label='nu bound')
 vs=[v for v in E['nu'] if v['rho']>1e-7];xx=[v['nu'] for v in vs];ax.plot(xx,[v['margin_errors']/14 for v in vs],'o-',c=c['warn'],label='margin errors / 14');ax.plot(xx,[v['sv']/14 for v in vs],'s-',c=c['pos'],label='SV / 14')
 ax.set(xlim=(0,1),ylim=(0,1.05),xlabel='nu',ylabel='training fraction');style(ax,c)
 lg=fig.legend(*ax.get_legend_handles_labels(),loc='upper center',bbox_to_anchor=(.55,.99),ncol=1,fontsize=11,frameon=False)
 for txt in lg.get_texts():txt.set_color(c['text'])
 ax.text(.055,.94,'nu=0.15: rho=0\nexcluded from bound test',fontsize=11,color=c['text'],va='top');return fig
def intervals(dark):
 c=colors(dark);fig,ax=base();ax.plot([0,2],[.6,.6],c=c['pos'],lw=8,solid_capstyle='round');ax.plot([4,6],[.6,.6],c=c['neg'],lw=8,solid_capstyle='round');ax.scatter([0,2],[.6,.6],c=c['pos'],s=50);ax.scatter([4,6],[.6,.6],c=c['neg'],marker='^',s=65)
 ax.annotate('',(2,.6),(4,.6),arrowprops={'arrowstyle':'<->','color':c['warn'],'lw':1.8});ax.text(3,.75,'D=2',ha='center',fontsize=14,color=c['text']);ax.axvline(3,c=c['line'],lw=2);ax.text(3,1.12,'boundary x=3',ha='center',fontsize=12,color=c['text']);ax.text(1,.3,'positive hull',ha='center',fontsize=12,color=c['pos']);ax.text(5,.3,'negative hull',ha='center',fontsize=12,color=c['neg'])
 ax.annotate('normal points to +',(1.3,.08),(4.6,.08),fontsize=12,color=c['text'],arrowprops={'arrowstyle':'->','color':c['line']});ax.set(xlim=(-.5,6.5),ylim=(-.15,1.4),xlabel='input x');ax.set_xticks(range(7));ax.set_yticks([]);style(ax,c);fig.text(.54,.94,'Source 1-D example: score g(x)=3-x',ha='center',fontsize=13,color=c['text']);return fig
def vertices(A,mu):
 n=len(A)
 if mu>=1:return A[ConvexHull(A).vertices]
 k=int(np.floor(1/mu+1e-10));r=1-k*mu;points=[]
 for inds in itertools.combinations(range(n),k):
  if r<1e-10:points.append(mu*A[list(inds)].sum(0));continue
  for j in set(range(n))-set(inds):points.append(mu*A[list(inds)].sum(0)+r*A[j])
 pts=np.unique(np.round(points,12),axis=0)
 return pts[ConvexHull(pts).vertices] if len(pts)>2 else pts
def hull(ax,A,mu,col,dashed=False):
 V=vertices(A,mu);ax.add_patch(Polygon(V,closed=True,facecolor=col,alpha=.10,edgecolor='none'));ax.plot(*np.vstack([V,V[:1]]).T,c=col,ls='--' if dashed else '-',lw=1.6)
def closest(ax,r,c,bounds):
 p=np.array(r['xp']);q=np.array(r['xm']);m=(p+q)/2;d=p-q;u=d/np.linalg.norm(d);v=np.array([-u[1],u[0]])
 ax.plot(*np.stack([p,q]).T,c=c['warn'],lw=2,zorder=6);ax.scatter([p[0],q[0]],[p[1],q[1]],c=c['warn'],s=40,zorder=7)
 scorelines(ax,d,-d@m,c,bounds,band=False)
 h=.15;rect=np.array([m+h*u,m+h*u+h*v,m+h*v]);ax.plot(*rect.T,c=c['warn'],lw=1)
def hullcompare(dark):
 c=colors(dark);fig,axs=base(True)
 for ax,A,B,key,title,lim in [(axs[0],SEP,-SEP,'separable','disjoint source hulls',4.1),(axs[1],POS,NEG,'0.4','overlap -> capped hulls',3.1)]:
  hull(ax,A,1,c['pos']);hull(ax,B,1,c['neg']);classes(ax,A,B,c)
  if key!='separable':hull(ax,A,.4,c['pos'],True);hull(ax,B,.4,c['neg'],True)
  closest(ax,E['hulls'][key],c,[-lim,lim,-lim,lim]);ax.set(xlim=(-lim,lim),ylim=(-lim,lim),xlabel=r'$x_1$');style(ax,c,True);ax.set_title(title,fontsize=11,color=c['text'])
 axs[0].set_ylabel(r'$x_2$');fig.text(.53,.95,'Nearest segment + perpendicular bisector',ha='center',fontsize=12,color=c['text']);return fig
FUN={'lec03-kp14-square-margin':square,'lec03-kp15-hinge-loss':hinge,'lec03-kp15-c-comparison':ccompare,'lec03-kp16-ecoc-distance':ecoc,'lec03-kp17-nu-bounds':nubounds,'lec03-kp18-interval-hulls':intervals,'lec03-kp18-reduced-hulls':hullcompare}
ALT={'lec03-kp14-square-margin':'The source four-corner square with optimal full margin 2 and tilted full margin 0.894427, equal coordinate scales and a right-angle marker.','lec03-kp15-hinge-loss':'Hinge loss against labeled score q, with markers at minus 0.5, 0.4, and 1.4 giving slacks 1.5, 0.6, and zero.','lec03-kp15-c-comparison':'The same ten source demo points fitted with C 0.2 and 1000; full widths 2.653529 and 0.914766, and six versus three positive multipliers.','lec03-kp16-ecoc-distance':'Source four by six code matrix and received vector with its second bit highlighted; Hamming distances one, two, four, and four identify class one.','lec03-kp17-nu-bounds':'Source fourteen-point solutions at nu 0.3, 0.6, and 0.9, with measured margin-error and support-vector fractions versus the nu diagonal; zero-rho nu 0.15 excluded.','lec03-kp18-interval-hulls':'Source positive interval zero to two and negative interval four to six, nearest endpoints two and four, midpoint boundary three, and normal pointing left.','lec03-kp18-reduced-hulls':'Source separable convex hulls and intersecting original hulls with exact cap 0.4 reduced hulls, nearest connecting segments, perpendicular bisectors and right-angle markers.'}
if __name__=='__main__':
 OUT.mkdir(exist_ok=True,parents=True);figs={}
 for name,fn in FUN.items():
  for dark in [False,True]:
   fig=fn(dark);assert not check_not_clipped(fig),(name,check_not_clipped(fig))
   if dark:fig.savefig(OUT/(name+'.svg'),transparent=True);fig.savefig(OUT/(name+'-dark.png'),dpi=150,facecolor='#151513')
   else:fig.savefig(OUT/(name+'.png'),dpi=200,facecolor='white')
   plt.close(fig)
  data=(OUT/(name+'.svg')).read_bytes();assert not check_svg(data.decode()),name
  figs[name]={'w':620,'h':440,'uri':'data:image/svg+xml;base64,'+base64.b64encode(data).decode(),'alt':ALT[name]};print(name,len(data),flush=True)
 (R/'figs.json').write_text(json.dumps(figs,ensure_ascii=False),encoding='utf-8')
