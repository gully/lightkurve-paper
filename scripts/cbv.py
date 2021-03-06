import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc
import matplotlib
matplotlib.rcParams['text.latex.unicode'] = True
rc('text', usetex=True)
font = {'family' : 'serif',
        'size'   : 14,
        'serif'  : 'New Century Schoolbook'}
rc('font', **font)

from pyke import KeplerCBVCorrector, KeplerLightCurveFile

fn = ("https://archive.stsci.edu/missions/kepler/lightcurves/"
      "0084/008462852/kplr008462852-2011073133259_llc.fits")
cbv = KeplerCBVCorrector(fn)
cbv_lc = cbv.correct(cbvs=list(range(1, 11)))
sap_lc = KeplerLightCurveFile(fn).SAP_FLUX
pdcsap_lc = KeplerLightCurveFile(fn).PDCSAP_FLUX
plt.plot(sap_lc.time, sap_lc.flux/1e4, 'ko', markersize=1.5)
plt.plot(sap_lc.time, sap_lc.flux/1e4, 'o',color='#369acd', markersize=.75)
plt.plot(pdcsap_lc.time, pdcsap_lc.flux/1e4, 'ko', markersize=1.5)
plt.plot(pdcsap_lc.time, pdcsap_lc.flux/1e4, 'o', color='#89DA59', markersize=.75)
plt.plot(cbv_lc.time, cbv_lc.flux/1e4, 'ko', markersize=1.5)
plt.plot(cbv_lc.time, cbv_lc.flux/1e4, 'o', color='#ff3366', markersize=.75)

plt.plot(np.nan, np.nan, 'o', color='#369acd', markersize=3, label='SAP')
plt.plot(np.nan, np.nan, 'o', color='#89DA59', markersize=3, label='PDCSAP')
plt.plot(np.nan, np.nan, 'o', color='#ff3366', markersize=3, label='CBV')

plt.ylabel(r"Flux $(10^{4}e^{-}s^{-1})$")
plt.xlabel(r"Time $(\mathrm{BJD}-2454833)$")
plt.legend(frameon=False, numpoints=3)

plt.savefig('cbv.eps', bbox_inches='tight', pad_inches=.1)
