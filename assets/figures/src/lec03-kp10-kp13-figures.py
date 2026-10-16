"""Reproducible PR Chapter 3 figures, KP10--KP13.
Run in Python with numpy, matplotlib, and the bundled jbd_figure.py.
Draws white PNGs and dark SVGs using identical numerical models.
Supplemental randomness: regression seed 42; repeated fits seed 20261016.
"""
from pathlib import Path
import json,base64,sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from jbd_figure import use_jbd_style,check_not_clipped,check_svg
OUT=Path(__file__).resolve().parents[1]
use_jbd_style(22)
sigmoid=lambda z:np.exp(-np.logaddexp(0.,-np.asarray(z)))
def pal(dark):return {'text':'#f2ede4' if dark else '#252521','muted':'#b7b0a5' if dark else '#66665f','main':'#d97757' if dark else '#b85337','ref':'#6a9fd6' if dark else '#286da6','vec':'#5fb8a8' if dark else '#007d70','edge':'#e0995f' if dark else '#996725','warn':'#e07a70' if dark else '#b63743'}
def style(ax,c):
 ax.tick_params(colors=c['muted'],labelsize=12)
 for sp in ax.spines.values():sp.set_color(c['muted'])
 ax.xaxis.label.set_color(c['text']);ax.yaxis.label.set_color(c['text']);ax.set_facecolor('none');ax.grid(alpha=.12)
def blank():
 fig,ax=plt.subplots(figsize=(6.2,4.4));fig.subplots_adjust(left=.15,right=.96,bottom=.18,top=.83);return fig,ax
def legend(fig,ax,c,cols=2):
 lg=fig.legend(*ax.get_legend_handles_labels(),loc='upper center',bbox_to_anchor=(.55,.995),ncol=cols,frameon=False,fontsize=12)
 for t in lg.get_texts():t.set_color(c['text'])
def regression(dark):
 c=pal(dark);fig,ax=blank();rng=np.random.default_rng(42);x=rng.uniform(0,6,120);y=np.sin(x)+.3*x+rng.normal(0,.5,120);g=np.linspace(0,6,500);mean=np.sin(g)+.3*g
 ax.scatter(x,y,s=9,alpha=.32,c=c['muted']);ax.plot(g,mean,color=c['ref'],lw=2.6,label='Mean')
 x0=3.2;m=np.sin(x0)+.3*x0;yy=np.linspace(m-1.5,m+1.5,500);pdf=np.exp(-.5*((yy-m)/.5)**2)/(.5*np.sqrt(2*np.pi))
 ax.axvspan(x0-.08,x0+.08,color=c['edge'],alpha=.13)
 ax.plot(x0+.85*pdf,yy,color=c['main'],lw=2,label='Density slice')
 ax.scatter([x0],[m],color=c['warn'],marker='*',s=150,zorder=4)
 ax.annotate(r'$m(x_0)$',(x0,m),xytext=(1.3,m-.7),fontsize=15,color=c['text'],arrowprops={'arrowstyle':'->','color':c['warn']})
 ax.text(x0+.16,-1.08,r'$x_0=3.2$',color=c['text'],fontsize=12)
 ax.set(xlim=(0,6),ylim=(-1.2,3),xlabel='input x',ylabel='target y');style(ax,c);legend(fig,ax,c);return fig
def posterior(dark):
 c=pal(dark);fig,ax=blank();xx=np.linspace(-3,7,500);p=sigmoid(np.log(4)+xx-2);xt=np.arange(-2.,7.);pt=sigmoid(np.log(4)+xt-2);w=np.linalg.lstsq(np.c_[xt,np.ones(9)],pt,rcond=None)[0];line=w[0]*xx+w[1]
 ax.plot(xx,p,color=c['main'],lw=2.7,label='Posterior');ax.plot(xx,line,color=c['ref'],lw=2.3,label='Linear fit');ax.fill_between(xx,p,line,color=c['edge'],alpha=.16)
 ax.axhline(0,color=c['muted'],lw=1);ax.axhline(1,color=c['muted'],lw=1);ax.axhline(.5,color=c['muted'],ls=':',lw=1)
 ax.scatter([2],[.8],color=c['main'],s=60,zorder=4);ax.annotate('(2, 0.8)',(2,.8),xytext=(-1.9,.85),color=c['text'],fontsize=13,arrowprops={'arrowstyle':'->','color':c['main']})
 ax.set(xlim=(-3,7),ylim=(-.16,1.4),xlabel='input x',ylabel='probability / score');style(ax,c);legend(fig,ax,c);return fig
def bv_models():
 x=np.linspace(0,1,11);t=np.linspace(0,1,101);f=np.sin(2*np.pi*x);truth=np.sin(2*np.pi*t);Hs={};means={};rows=[]
 for d in range(1,10):
  V=np.vander(x,d+1,increasing=True);B=np.vander(t,d+1,increasing=True);U,s,QT=np.linalg.svd(V,full_matrices=False);H=B@(QT.T*(s/(s*s+1e-9)))@U.T;mu=H@f;b2=np.mean((mu-truth)**2);var=.09*np.mean(np.sum(H*H,axis=1));Hs[d]=H;means[d]=mu;rows.append([d,b2,var,b2+var+.09])
 return x,t,f,truth,Hs,means,np.array(rows)
def risk_curves(dark):
 c=pal(dark);fig,ax=blank();_,_,_,_,_,_,a=bv_models()
 for j,label,color in [(1,'Bias squared',c['ref']),(2,'Variance',c['warn']),(3,'Total risk',c['vec'])]:ax.plot(a[:,0],a[:,j],'-o',c=color,lw=2,ms=4,label=label)
 ax.axhline(.09,c=c['muted'],ls='--',lw=1.2,label='Noise')
 best=a[np.argmin(a[:,3])];ax.scatter([best[0]],[best[3]],s=95,marker='*',c=c['vec'],zorder=5);ax.annotate('d = 3',(best[0],best[3]),xytext=(4.1,.24),color=c['text'],fontsize=13,arrowprops={'arrowstyle':'->','color':c['vec']})
 ax.set(xlim=(.8,9.2),ylim=(0,.39),xlabel='polynomial degree',ylabel='grid-averaged squared error');ax.set_xticks([1,3,5,7,9]);style(ax,c);legend(fig,ax,c,2);return fig
def fits(dark):
 c=pal(dark);fig,axs=plt.subplots(1,2,figsize=(6.2,4.4),sharey=True);fig.subplots_adjust(left=.13,right=.97,bottom=.18,top=.81,wspace=.25)
 x,t,f,truth,Hs,means,_=bv_models();rng=np.random.default_rng(20261016);targets=f+rng.normal(0,.3,(200,11))
 for ax,d,col in zip(axs,[1,9],[c['ref'],c['main']]):
  for y in targets[:10]@Hs[d].T:ax.plot(t,y,c=col,alpha=.27,lw=1.1)
  ax.plot(t,truth,c=c['text'],ls='--',lw=2);ax.plot(t,means[d],c=col,lw=2.3);ax.set(xlim=(0,1),ylim=(-1.8,1.8),xlabel='input x');ax.set_title(f'degree {d}',color=c['text'],fontsize=15);ax.set_xticks([0,.5,1]);style(ax,c)
 axs[0].set_ylabel('prediction');fig.text(.52,.955,'10 fits / truth -- / mean fit',ha='center',color=c['text'],fontsize=12);return fig
def sigmoid_plot(dark):
 c=pal(dark);fig,ax=blank();z=np.linspace(-7,7,500);p=sigmoid(z);ax.plot(z,p,c=c['vec'],lw=2.8)
 ax.axhline(0,c=c['muted'],ls='--',lw=1);ax.axhline(1,c=c['muted'],ls='--',lw=1);ax.axhline(.5,c=c['muted'],ls=':',lw=1)
 zz=np.array([-3.,0,3.]);pp=sigmoid(zz);ax.scatter(zz,pp,c=[c['ref'],c['edge'],c['main']],s=55,zorder=4)
 for z0,p0,tx,ty in [(-3,pp[0],-6.5,.22),(0,.5,.7,.38),(3,pp[2],1.8,1.07)]:ax.annotate(f'({z0:g}, {p0:.4f})',(z0,p0),xytext=(tx,ty),fontsize=12,color=c['text'],arrowprops={'arrowstyle':'->','color':c['muted']})
 ax.set(xlim=(-7,7),ylim=(-.12,1.23),xlabel='score z = b + w x',ylabel='model probability');style(ax,c);fig.text(.54,.945,r'$p=1/(1+\exp(-z))$',ha='center',fontsize=18,color=c['text']);return fig
FUN={'lec03-kp10-regression-slice':regression,'lec03-kp11-posterior-fit':posterior,'lec03-kp12-risk-curves':risk_curves,'lec03-kp12-retrained-fits':fits,'lec03-kp13-sigmoid':sigmoid_plot}
ALT={'lec03-kp10-regression-slice':'Nonlinear conditional mean sin(x)+0.3x, 120 seeded noisy observations, x=3.2 slice and sideways Gaussian density centered on the star.','lec03-kp11-posterior-fit':'Posterior sigmoid(log(4)+x-2), its nine-input least-squares line, shaded approximation gaps, bounds zero and one, and source point (2,0.8).','lec03-kp12-risk-curves':'Exact fixed-design bias squared, variance, noise 0.09, and total risk for polynomial degrees one through nine; minimum at degree three.','lec03-kp12-retrained-fits':'The same first ten of 200 seeded noise realizations fitted by degree one and degree nine, with sine truth and exact mean predictions.','lec03-kp13-sigmoid':'Sigmoid probability against the affine score z, limits at zero and one, and markers at scores minus three, zero and three.'}
if __name__=='__main__':
 OUT.mkdir(parents=True,exist_ok=True);figs={}
 for name,fn in FUN.items():
  fig=fn(False);err=check_not_clipped(fig);assert not err,(name,err);fig.savefig(OUT/(name+'.png'),dpi=200,facecolor='white');plt.close(fig)
  fig=fn(True);assert not check_not_clipped(fig),(name,check_not_clipped(fig));fig.savefig(OUT/(name+'.svg'),transparent=True);fig.savefig(OUT/(name+'-dark.png'),dpi=150,facecolor='#151513');plt.close(fig)
  b=(OUT/(name+'.svg')).read_bytes();assert not check_svg(b.decode()),name;figs[name]={'w':620,'h':440,'uri':'data:image/svg+xml;base64,'+base64.b64encode(b).decode(),'alt':ALT[name]};print(name,len(b))
 dest=Path(sys.argv[1]) if len(sys.argv)>1 else OUT;(dest/'figs.json').write_text(json.dumps(figs,ensure_ascii=False),encoding='utf-8')
