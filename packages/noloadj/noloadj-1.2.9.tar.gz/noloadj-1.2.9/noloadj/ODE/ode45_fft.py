from noloadj.ODE.ode45 import *
from noloadj.ODE.ode45 import _odeint45

def odeint45_fft(f,x0,t,*P,M,T=0.,h0=1e-5,tol=1.48e-8):
    return _odeint45_fft(f,h0,tol,M,x0,t,T,*P)


@partial(custom_jvp,nondiff_argnums=(0,1,2,3))
def _odeint45_fft(f,h0,tol,M,x0,t,T,*P):
    if hasattr(f,'etat'):
        xs,ys,_=_odeint45(f,h0,tol,x0,t,T,*P)
    else:
        xs,ys=_odeint45(f,h0,tol,x0,t,T,*P)
    xfft=np.fft.fft(xs,M)*2/M # fft de x avec normalisation
    xfft=xfft.at[:,0].divide(2)
    yfft=np.fft.fft(ys,M)*2/M # fft de y avec normalisation
    yfft=yfft.at[:,0].divide(2)
    moduleX,phaseX=np.abs(xfft),np.angle(xfft) # amplitude et phase de la fft de x
    moduleY,phaseY=np.abs(yfft),np.angle(yfft) # amplitude et phase de la fft de y
    return xs,moduleX[:,0:M//2],phaseX[:,0:M//2],ys,moduleY[:,0:M//2],\
           phaseY[:,0:M//2]# on retire les frequences negatives


@_odeint45_fft.defjvp
def _odeint45_fft_jvp(f,h0,tol,M, primals, tangents):
    x0, t,T, *P = primals
    delta_x0, _,_, *dP = tangents
    nPdP = len(P)

    xs,xs_dot,modX,phX,dmodX,dphX,ys,ys_dot,modY,phY,dmodY,dphY=\
        odeint45_fft_etendu(f,nPdP, h0,tol,M, x0,delta_x0,t,T, *P, *dP)
    return (xs,modX,phX,ys,modY,phY),(xs_dot,dmodX,dphX,ys_dot,dmodY,dphY)


def odeint45_fft_etendu(f,nPdP,h0,tol,M,x0,delta_x0,t,T,*P_and_dP):
    P,dP = P_and_dP[:nPdP],P_and_dP[nPdP:]
    if hasattr(f,'etat'):
        xs,delta_xs,ys,delta_ys,_=odeint45_etendu(f,nPdP,h0,tol,x0,
                                        delta_x0,t,T, *P, *dP)
    else:
        xs,delta_xs,ys,delta_ys=odeint45_etendu(f,nPdP,h0,tol,x0,delta_x0,
                                        t,T, *P, *dP)
    xfft=np.fft.fft(xs,M)*2/M  # fft de x avec normalisation
    dxfft=np.fft.fft(delta_xs,M)*2/M
    xfft,dxfft=xfft.at[:,0].divide(2),dxfft.at[:,0].divide(2)
    yfft=np.fft.fft(ys,M)*2/M  # fft de x avec normalisation
    dyfft=np.fft.fft(delta_ys,M)*2/M
    yfft,dyfft=yfft.at[:,0].divide(2),dyfft.at[:,0].divide(2)
    moduleX,phaseX=np.abs(xfft),np.angle(xfft)  # amplitude et phase de la fft de x
    dmoduleX,dphaseX=np.abs(dxfft),np.angle(xfft)
    moduleY,phaseY=np.abs(yfft),np.angle(yfft)  # amplitude et phase de la fft de x
    dmoduleY,dphaseY=np.abs(dyfft),np.angle(yfft)
    return xs,delta_xs,moduleX[:,0:M//2],phaseX[:,0:M//2],dmoduleX[:,0:M//2],\
           dphaseX[:,0:M//2],ys,delta_ys,moduleY[:,0:M//2],phaseY[:,0:M//2],\
           dmoduleY[:,0:M//2],dphaseY[:,0:M//2]



