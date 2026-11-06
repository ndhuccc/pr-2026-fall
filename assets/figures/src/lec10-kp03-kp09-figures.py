"""Rebuild original Feature Generation I figures. Run from any directory.

Requires numpy, scipy, matplotlib. English labels; no external images or data.
Every toy dataset is explicitly constructed, not an empirical benchmark.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import eigh

OUT = Path(__file__).resolve().parent.parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'figure.dpi':150,'savefig.dpi':180})
BLUE, ORANGE, GREEN = '#236485', '#c36831', '#407858'
def save(fig, name):
    fig.tight_layout(pad=1.5)
    fig.savefig(OUT/f'lec10-{name}.png', facecolor='white')
    plt.close(fig)
def matrix(ax, A, title, lim=None):
    if lim is None: lim=max(1,float(np.abs(A).max()))
    ax.imshow(A,cmap='RdBu_r',vmin=-lim,vmax=lim,aspect='equal')
    for (i,j),v in np.ndenumerate(A):
        ax.text(j,i,f'{v:.2g}',ha='center',va='center',
                color='white' if abs(v)>.65*lim else '#202020')
    ax.set_title(title); ax.set_xticks([]); ax.set_yticks([])

X=np.array([[1.,3.],[5.,7.],[3.,1.],[7.,5.]])
mu=X.mean(0); Xc=X-mu
V=np.array([[1.,-1.],[1.,1.]])/np.sqrt(2)
Z=Xc@V
fig,axs=plt.subplots(1,2,figsize=(10,4.2))
for i in range(4):
    c=BLUE if i<2 else ORANGE
    axs[0].scatter(*X[i],color=c,s=65)
    axs[0].annotate(str(i+1),X[i]+[.12,.12])
    axs[1].scatter(Z[i,0],Z[i,1],color=c,s=65)
    axs[1].annotate(str(i+1),Z[i]+[.1,.1])
for j,c in [(0,GREEN),(1,'#777777')]:
    a=mu-4*V[:,j]; b=mu+4*V[:,j]
    axs[0].plot([a[0],b[0]],[a[1],b[1]],color=c,ls='--',label=f'PC{j+1}')
axs[0].set(xlabel='$x_1$',ylabel='$x_2$',title='Same four observations; mean = (4, 4)',aspect='equal')
axs[0].legend(); axs[1].set(xlabel='$z_1$',ylabel='$z_2$',title='PC1 overlaps the constructed classes')
axs[1].axhline(0,color='#aaaaaa',lw=1); axs[1].grid(alpha=.15)
save(fig,'kp03-pca-axes')
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
axs[0].bar(['PC1','PC2'],[8,2],color=[BLUE,ORANGE]); axs[0].set(ylabel='Variance (1/n convention)',title='Total variance = 10')
axs[1].plot([0,1,2],[10,2,0],'o-',color=BLUE)
axs[1].set(xticks=[0,1,2],xlabel='Retained components',ylabel='Mean squared reconstruction error',title='Discarded variance = average error')
axs[1].grid(alpha=.2); save(fig,'kp03-variance-error')

left=np.array([[-1,1],[1,1],[-1,-1],[1,-1]])/2
s=np.array([4*np.sqrt(2),2*np.sqrt(2)])
terms=[s[j]*np.outer(left[:,j],V[:,j]) for j in range(2)]
fig,axs=plt.subplots(1,3,figsize=(9,4))
for ax,A,title in zip(axs,[Xc,*terms],['Centered X (4 x 2)','First rank-one term','Second rank-one term']):matrix(ax,A,title,3)
save(fig,'kp04-rank-one-terms')
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
axs[0].bar(['1','2'],s,color=[BLUE,ORANGE]); axs[0].set(xlabel='Component',ylabel='Singular value',title=r'$s_1=4\sqrt{2},\ s_2=2\sqrt{2}$')
axs[1].bar(['Total SSE','Mean SSE'],[8,2],color=[BLUE,GREEN]); axs[1].set(ylabel='Squared error',title='Rank-one approximation; n = 4')
save(fig,'kp04-singular-error')

W=np.array([[1.,0],[0,1],[1,1]]); H=np.array([[2.,0,1],[0,3,1]]); A=W@H
fig,axs=plt.subplots(1,3,figsize=(9,3.5))
for ax,B,title in zip(axs,[W,H,A],['Parts W (3 x 2)','Coefficients H (2 x 3)','Observations X = WH']):matrix(ax,B,title,3)
save(fig,'kp05-nonnegative-parts')
Wi=np.array([[1.,.2],[.2,1],[.8,.8]]); Hi=np.array([[1.5,.2,.8],[.2,2,.8]])
loss=[.5*np.sum((A-Wi@Hi)**2)]
for _ in range(80):
    Hi *= (Wi.T@A)/np.maximum(Wi.T@Wi@Hi,1e-12)
    Wi *= (A@Hi.T)/np.maximum(Wi@Hi@Hi.T,1e-12)
    loss.append(.5*np.sum((A-Wi@Hi)**2))
fig,ax=plt.subplots(figsize=(7.5,3.6))
ax.semilogy(np.arange(81),loss,color=BLUE); ax.set(xlabel='Completed update pairs',ylabel=r'$\frac{1}{2}\|X-WH\|_F^2$',title='One specified positive initialization; no global-optimum claim'); ax.grid(alpha=.2)
save(fig,'kp05-update-loss')

t=np.arange(-2,3,dtype=float); P=np.c_[t,t*t]
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
tt=np.linspace(-2,2,200); axs[0].plot(tt,tt*tt,color='#999999')
axs[0].scatter(*P.T,c=t,cmap='viridis',s=75); axs[0].axvline(0,color=ORANGE,ls='--',label='PC1 direction')
for i in range(5):axs[0].annotate(f't={t[i]:g}',P[i]+[.08,.08])
axs[0].set(xlim=(-2.55,2.6),ylim=(-.4,4.65),xlabel='$x_1=t$',ylabel='$x_2=t^2$',title='One parameter, curved in two dimensions'); axs[0].legend()
axs[1].scatter(t,t*t-2,c=t,cmap='viridis',s=75); axs[1].set(xlabel='Known parameter t',ylabel='PC1 coordinate = $t^2-2$',title='Opposite parameters share a projection')
save(fig,'kp06-parabola-projection')
fig,ax=plt.subplots(figsize=(7.5,4))
th=np.linspace(0,np.pi,200); a=np.linspace(0,np.pi,5)
ax.plot(np.cos(th),np.sin(th),color=BLUE,label='Semicircle arc length = pi')
ax.plot(np.cos(a),np.sin(a),'o--',color=ORANGE,label='Four short chords')
ax.plot([-1,1],[0,0],color='#777777',label='Endpoint chord length = 2')
ax.set(aspect='equal',xlabel='$x_1$',ylabel='$x_2$',title='Local chords approximate a path, not a shortcut'); ax.legend(loc='upper right',fontsize=9)
save(fig,'kp06-local-versus-global')

Q=np.array([[1.,0],[-1,0],[0,1],[0,-1]])
K=(Q@Q.T)**2; J=np.eye(4)-np.ones((4,4))/4; Kc=J@K@J
fig,axs=plt.subplots(1,2,figsize=(8,3.8)); matrix(axs[0],K,'Raw Gram K',1); matrix(axs[1],Kc,'Centered Gram Kc',1)
save(fig,'kp07-centered-gram')
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
axs[0].scatter(*Q.T,c=[BLUE,BLUE,ORANGE,ORANGE],s=75)
for i,p in enumerate(Q):axs[0].annotate(str(i+1),p+[.08,.08])
axs[0].set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),aspect='equal',xlabel='$x_1$',ylabel='$x_2$',title='Input observations')
zs=np.array([1,1,-1,-1])/np.sqrt(2)
axs[1].scatter(zs,[.08,-.08,.08,-.08],c=[BLUE,BLUE,ORANGE,ORANGE],s=75)
for i,z in enumerate(zs):axs[1].annotate(str(i+1),(z+.04,[.08,-.08,.08,-.08][i]))
axs[1].set(xlabel='Kernel PC coordinate',yticks=[],ylim=(-.4,.4),title='Vertical offsets only separate labels')
save(fig,'kp07-kernel-coordinates')

R=np.array([[-1.,0],[0,1],[1,0]])
G=np.array([[0.,1,0],[1,0,1],[0,1,0]])
D=np.diag(G.sum(1)); L=D-G; z=np.array([-1.,0,1])/np.sqrt(2)
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
axs[0].plot(*R.T,'o-',color=BLUE)
for i,p in enumerate(R):axs[0].annotate(str(i+1),p+[.06,.06])
axs[0].plot([-1,1],[0,0],ls=':',color='#aaaaaa',label='No endpoint edge')
axs[0].set(xlabel='$x_1$',ylabel='$x_2$',title='Radius 1.5; unit edge weights'); axs[0].legend(fontsize=9)
axs[1].plot(z,np.zeros(3),'o-',color=GREEN)
for i,zi in enumerate(z):axs[1].annotate(str(i+1),(zi,.04))
axs[1].set(xlabel='Embedding coordinate z',yticks=[],ylim=(-.2,.2),title=r'$z^TDz=1$; generalized eigenvalue = 1')
save(fig,'kp08-graph-embedding')
fig,axs=plt.subplots(1,3,figsize=(10,3.4))
for ax,A,title in zip(axs,[G,D,L],['Adjacency W','Degree D','Laplacian L = D - W']):matrix(ax,A,title,2)
save(fig,'kp08-graph-matrices')

LW=np.array([[0.,2,-1],[.5,0,.5],[-1,2,0]])
fig,axs=plt.subplots(1,2,figsize=(9,3.8))
xx=np.arange(3); axs[0].scatter(xx,[0,0,0],s=70,color=BLUE)
for i,v in enumerate(xx):axs[0].annotate(f'x{i+1} = {v}',(v,.04),ha='center')
axs[0].annotate('',xy=(0,0),xytext=(1,0),arrowprops={'arrowstyle':'->','color':ORANGE,'lw':2})
axs[0].text(1,-.12,r'$x_1=2x_2-x_3$',ha='center'); axs[0].set(xlim=(-.3,2.4),ylim=(-.25,.25),yticks=[],xlabel='Input coordinate',title='Endpoint reconstruction needs a negative weight')
matrix(axs[1],LW,'Fixed LLE weights W',2)
save(fig,'kp09-lle-reconstruction')
dg=np.array([[0,1,2],[1,0,1],[2,1,0]])*np.sqrt(2)
fig,axs=plt.subplots(1,2,figsize=(9,3.8)); axs[0].plot(*R.T,'o-',color=BLUE)
axs[0].text(-.95,.65,r'$\sqrt{2}$'); axs[0].text(.6,.65,r'$\sqrt{2}$')
axs[0].plot([-1,1],[0,0],ls=':',color='#aaaaaa'); axs[0].text(0,-.18,'Direct distance = 2',ha='center')
axs[0].set(ylim=(-.42,1.2),xlabel='$x_1$',ylabel='$x_2$',title=r'Graph endpoint distance = $2\sqrt{2}$')
iso=np.array([-np.sqrt(2),0,np.sqrt(2)])
axs[1].plot(iso,np.zeros(3),'o-',color=GREEN)
for i,v in enumerate(iso):axs[1].annotate(str(i+1),(v,.04))
axs[1].set(yticks=[],ylim=(-.2,.2),xlabel='Classical MDS coordinate',title='All three graph distances are reproduced')
save(fig,'kp09-isomap-distances')

if __name__=='__main__':
    print(json.dumps({'figures':14,'nmf_initial_loss':loss[0],
        'nmf_final_loss':loss[-1],'nmf_max_loss_increase':float(np.diff(loss).max()),
        'pca_covariance':(Xc.T@Xc/4).tolist(),
        'laplacian_eigenvalues':eigh(L,D,eigvals_only=True).tolist()},indent=2))
