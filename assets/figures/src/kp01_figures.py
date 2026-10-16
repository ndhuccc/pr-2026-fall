"""Reproduce four KP01 figures in light PNG and dark SVG from shared analytic data.
Run this file, or any lec03-kp01-*.py wrapper. Requires numpy and matplotlib.
"""
from pathlib import Path
import base64
import json
import numpy as np
import matplotlib.pyplot as plt
from jbd_figure import use_jbd_style, new_figure, svg_data_uri, px_to_pt

OUT = Path(__file__).resolve().parents[1]
W = np.array([1., 1.]); BIAS = -0.5
A = np.array([1., 1.]); B = np.array([0.4, 0.05])
NORM = np.linalg.norm(W); N = W / NORM
T = np.array([W[1], -W[0]]) / NORM
def score(x): return float(W @ x + BIAS)
def foot(x): return x - score(x) / (W @ W) * W

SIZES = {'halfspaces': (560, 350), 'normal': (500, 400),
         'distances': (460, 380), 'scaling': (430, 340)}
ALTS = {
 'halfspaces': '直線 x1+x2−0.5=0 分開正負半空間，A=(1,1)在正側、B=(0.4,0.05)在負側，箭頭朝分數增加方向。',
 'normal': '邊界截距點 q1=(0,0.5) 與 q2=(0.5,0)，切向位移(0.5,−0.5)與權重(1,1)成直角。',
 'distances': 'A與B及解析計算的垂足(0.25,0.25)、(0.425,0.075)，垂直線段和直角符號，右下放大B附近。',
 'scaling': '以有號距離r為橫軸，g=√2r與2g兩條分數線共用零點，A的距離固定、分數分別為1.5與3。'
}

def palette(dark):
 return dict(text='#f2ede4' if dark else '#252925', muted='#b7b0a5' if dark else '#58615c',
             pos='#d97757' if dark else '#b75032', neg='#6a9fd6' if dark else '#346b9f',
             line='#e0995f' if dark else '#9a661d', vec='#5fb8a8' if dark else '#177b70',
             grid='#b7b0a5' if dark else '#b6beb8')

def setup(kind, dark):
 use_jbd_style(22)
 c = palette(dark)
 plt.rcParams.update({'text.color': c['text'], 'axes.labelcolor': c['text'],
  'axes.edgecolor': c['muted'], 'xtick.color':c['muted'], 'ytick.color':c['muted']})
 width,height = SIZES[kind]
 fig,ax = new_figure(width,height,margins_px=(90,70,22,22))
 ax.grid(color=c['grid'],alpha=.2,linewidth=.7)
 ax.set_xlabel(r'$x_1$', labelpad=2); ax.set_ylabel(r'$x_2$',labelpad=2)
 return fig,ax,c

def boundary(ax,c,lo,hi):
 x=np.linspace(lo,hi,600)
 ax.plot(x,(-BIAS-W[0]*x)/W[1],color=c['line'],lw=2.5)

def right_angle(ax,p,normal,tangent,size,c):
 points = np.array([p+normal*size,p+(normal+tangent)*size,p+tangent*size])
 ax.plot(points[:,0],points[:,1],color=c['muted'],lw=1.2)

def halfspaces(dark):
 fig,ax,c=setup('halfspaces',dark)
 lo,hi=-.4,1.3
 x=np.linspace(lo,hi,600); line=(-BIAS-W[0]*x)/W[1]
 ax.fill_between(x,line,hi,color=c['pos'],alpha=.13)
 ax.fill_between(x,lo,line,color=c['neg'],alpha=.13)
 boundary(ax,c,lo,hi)
 for p,lab,col,off in [(A,'A',c['pos'],(7,1)),(B,'B',c['neg'],(-22,-3))]:
  ax.scatter(*p,s=38,color=col,zorder=4)
  ax.annotate(lab,p,xytext=off,textcoords='offset points',color=col)
 p=foot(np.zeros(2)); end=p+.6*N
 ax.annotate('',end,p,arrowprops=dict(arrowstyle='->',color=c['vec'],lw=2.4))
 ax.text(.54,.76,r'$\mathbf{w}$',color=c['vec'])
 ax.text(.70,1.16,r'$g>0\quad(+)$',color=c['pos'])
 ax.text(-.36,-.28,r'$g<0\quad(-)$',color=c['neg'])
 ax.text(-.34,.98,r'$g=0$',color=c['line'])
 ax.set_xlim(lo,hi);ax.set_ylim(lo,hi);ax.set_aspect('equal')
 ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
 return fig

def normal(dark):
 fig,ax,c=setup('normal',dark)
 q1=np.array([0.,-BIAS/W[1]]);q2=np.array([-BIAS/W[0],0.])
 boundary(ax,c,-.3,1.2)
 p=(q1+q2)/2
 ax.annotate('',q2,q1,arrowprops=dict(arrowstyle='->',color=c['vec'],lw=2.4))
 end=p+W
 ax.annotate('',end,p,arrowprops=dict(arrowstyle='->',color=c['vec'],lw=2.4))
 right_angle(ax,p,N,T,.075,c)
 ax.scatter([q1[0],q2[0]],[q1[1],q2[1]],color=c['line'],s=38,zorder=4)
 ax.annotate(r'$\mathbf{q}_1$',q1,xytext=(-29,6),textcoords='offset points')
 ax.annotate(r'$\mathbf{q}_2$',q2,xytext=(7,-5),textcoords='offset points')
 ax.text(.85,1.40,r'$\mathbf{w}=(1,1)^{\mathsf{T}}$',color=c['vec'],ha='center')
 ax.text(.27,-.21,r'$\mathbf{t}=(0.5,-0.5)^{\mathsf{T}}$',ha='center')
 ax.set_xlim(-.35,1.5);ax.set_ylim(-.35,1.5);ax.set_aspect('equal')
 ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
 return fig

def distances(dark):
 fig,ax,c=setup('distances',dark)
 boundary(ax,c,-.3,1.25)
 pa,pb=foot(A),foot(B)
 for x,p,col,label in [(A,pa,c['pos'],'A'),(B,pb,c['neg'],'B')]:
  ax.plot([x[0],p[0]],[x[1],p[1]],color=col,lw=2)
  ax.scatter(*x,color=col,s=38,zorder=4)
  ax.scatter(*p,color=c['line'],marker='s',s=26,zorder=4)
  ax.annotate(label,x,xytext=(5,5),textcoords='offset points',color=col)
 right_angle(ax,pa,N,T,.065,c)
 ax.annotate(r'$\mathbf{p}_A$',pa,xytext=(-28,4),textcoords='offset points')
 ax.set_xlim(-.35,1.25);ax.set_ylim(-.35,1.25);ax.set_aspect('equal')
 ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
 # A separate equal-aspect inset resolves B's short, nonzero distance.
 ins=fig.add_axes([.65,.23,.29,.29]);ins.set_facecolor('#1d211f' if dark else '#f8faf7')
 x=np.linspace(.36,.47,600)
 ins.plot(x,(-BIAS-W[0]*x)/W[1],color=c['line'],lw=1.7)
 ins.plot([B[0],pb[0]],[B[1],pb[1]],color=c['neg'],lw=2)
 ins.scatter(*B,s=25,color=c['neg']);ins.scatter(*pb,s=22,color=c['line'],marker='s')
 right_angle(ins,pb,-N,T,.01,c)
 ins.annotate('B',B,xytext=(-13,-8),textcoords='offset points',fontsize=px_to_pt(22))
 ins.annotate(r'$\mathbf{p}_B$',pb,xytext=(3,6),textcoords='offset points',fontsize=px_to_pt(22))
 ins.set_xlim(.36,.47);ins.set_ylim(.015,.125);ins.set_aspect('equal')
 ins.set_xticks([.4]);ins.set_yticks([.05,.1]);ins.tick_params(labelsize=px_to_pt(22),pad=1)
 for spine in ins.spines.values():spine.set_visible(True);spine.set_color(c['muted'])
 return fig

def scaling(dark):
 fig,ax,c=setup('scaling',dark)
 r=np.linspace(-.4,1.25,600)
 ax.plot(r,NORM*r,color=c['line'],label=r'$g$',lw=2.5)
 ax.plot(r,2*NORM*r,color=c['vec'],label=r'$2g$',lw=2.5)
 ra=score(A)/NORM
 ax.vlines(ra,0,2*score(A),color=c['muted'],linestyle=':',lw=1.2)
 ax.scatter([ra,ra],[score(A),2*score(A)],color=[c['line'],c['vec']],s=38)
 ax.annotate('1.5',(ra,score(A)),xytext=(-28,5),textcoords='offset points',color=c['line'])
 ax.annotate('3',(ra,2*score(A)),xytext=(-16,5),textcoords='offset points',color=c['vec'])
 ax.axhline(0,color=c['muted'],lw=1);ax.axvline(0,color=c['muted'],lw=1)
 ax.set_xlim(-.4,1.25);ax.set_ylim(-1,4.4)
 ax.set_xlabel(r'$r$  (signed distance)',fontsize=px_to_pt(20),labelpad=4)
 ax.set_ylabel('score',fontsize=px_to_pt(20),labelpad=4)
 ax.set_xticks([0,ra]);ax.set_xticklabels(['0',r'$r_A$'])
 ax.set_yticks([0,1.5,3])
 ax.legend(loc='upper left',frameon=False,ncol=2,fontsize=px_to_pt(20))
 return fig

BUILDERS={'halfspaces':halfspaces,'normal':normal,'distances':distances,'scaling':scaling}
def build(kind):
 out=OUT/f'lec03-kp01-{kind}'
 fig=BUILDERS[kind](False)
 fig.savefig(out.with_suffix('.png'),dpi=200,facecolor='white',transparent=False)
 plt.close(fig)
 dark=BUILDERS[kind](True)
 dark.savefig(out.with_name(out.name+'-dark.png'),dpi=150,facecolor='#151513',transparent=False)
 uri=svg_data_uri(dark)
 out.with_suffix('.svg').write_bytes(base64.b64decode(uri.split(',',1)[1]))
 return dict(w=SIZES[kind][0],h=SIZES[kind][1],alt=ALTS[kind],uri=uri)

if __name__=='__main__':
 data={'lec03-kp01-'+k:build(k) for k in BUILDERS}
 (OUT/'figs.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
 print('Created 4 light PNGs, 4 dark SVGs, and 4 dark PNG proofs.')
