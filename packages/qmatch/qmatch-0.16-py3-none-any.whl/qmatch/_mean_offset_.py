"""
mean_offset
Dr Zheng & Dr Jiang, 2023-09-20

Find the rough offset of two astronomical photometric images of the same sky area with dither.

In preparation, compute the axis mean as mean_x and mean_y, as the feature of the image.
Fit the mean_x|y with an order 2 polynomial, then use it to normalize the mean_x|y,
in order to remove the background slope and the value difference.

Then compare mean from two images, one axis by one axis. 
We try to pan the data, divide one by another, we use the std of the result as the similarity index.
If the offset is the best, the result should be the  constant 1, but this happens only when comparing the same image.
The similarity index will drop sharply at the matched offset.
But a global trend will bring some trouble, with bigger offset, the common pixel will be fewer, and the std will decrease.
So we perform a moving average normalization on the std curve.
"""


import numpy as np
from astropy.modeling import models,fitting
from astropy import modeling


def mean_xy(img):
    """
    Compute the row/col mean of the image and normalize with a order-2 polynomial.
    :param img: 2-d image
    :returns: mean_x, mean_y
    """
    # size
    ny, nx = img.shape
    xrange = np.arange(nx)
    yrange = np.arange(ny)
    # get the raw mean
    mean_x0 = img.mean(axis=0)
    mean_y0 = img.mean(axis=1)
    # poly fit
    xc = np.polyfit(xrange, mean_x0, 2)
    yc = np.polyfit(yrange, mean_y0, 2)
    # residual
    xres = mean_x0 - np.polyval(xc, xrange)
    yres = mean_y0 - np.polyval(yc, yrange)
    xresmed, xresstd = np.median(xres), np.std(xres)
    yresmed, yresstd = np.median(yres), np.std(yres)
    # 3-sigma clip, only one side, assume no negative outlier
    xsky = np.where(xres < xresmed + 3 * xresstd)[0]
    ysky = np.where(yres < yresmed + 3 * yresstd)[0]
    # second poly fit
    xc2 = np.polyfit(xrange[xsky], mean_x0[xsky], 2)
    yc2 = np.polyfit(yrange[ysky], mean_y0[ysky], 2)
    # normalize
    mean_x = mean_x0 / np.polyval(xc2, xrange)
    mean_y = mean_y0 / np.polyval(yc2, yrange)
    # end
    return mean_x, mean_y


def mean_offset1d(m1, m2, max_d=250, con_w=25, with_std=False):
    """
    Find the best offset
    :param m1, m2: mean of one axis (x or y) of image 1&2
    :param max_d: the max trial offset distance
    :param con_w: the width of the mean smooth width
    :param with_std: if true, return std curve and the best offset
    :returns: the best offset found, and std curve
    """
    # a function do offset divide and return the std
    def offset_div(i):
        if i > 0:
            d = m1[i:] / m2[:-i]
        elif i < 0:
            d = m1[:i] / m2[-i:]
        else:
            d = m1 / m2
        dm = np.mean(d)
        ds = np.std(d / dm)
        return ds
    
    con_w2 = con_w // 2
    # compute the std of each offset
    # -w~+w only used here, in following, all in 0~2w
    divstd = np.array([offset_div(i) for i in range(-max_d, max_d+1)])
    # a mean smooth is used as the normalize factor
    # to remove the global trend
    core = np.ones(con_w)/con_w
    smoothed = np.convolve(divstd, core, mode="same")
    # the border was removed
    smoothed[:con_w2] = np.nan
    smoothed[-con_w2:] = np.nan
    divstd1 = divstd / smoothed
    # the minumum is the best offset
    p = np.nanargmin(divstd1)
    # perform a gauss fit around the peak
    g_init = models.Gaussian1D(amplitude=-0.1, mean=p, stddev=1.0)
    fit_g = fitting.LevMarLSQFitter()
    l = max(1, p - 3 * con_w)
    r = min(2*max_d, p + 3 * con_w)
    s0 = (divstd[l] + divstd[r-1]) / 2
    g = fit_g(g_init, np.arange(l, r), divstd[l:r]-s0)
    p2 = g.mean.value - max_d
    return (p2, divstd, divstd1) if with_std else p2


def simu_mean(nu, nv, cu, cm, sig=3):
    """
    Simulate a mean of one side with stars found
    :param nu, nv: size of image, u is the axis to construct, v is the other
    :param cu: star positions on u axis
    :param cm: mag of stars, if use instrumental mag, the suggested zeropoint is 25
    :param sig: the rough sigma of the star psf
    :return: simulated mean
    """
    # a gauss function
    gau = lambda x, a, u, s: a * np.exp(- (x - u)**2 / (2 * s * s)) / s / np.sqrt(2 * np.pi)
    # initial simulated means
    sm = np.ones(nu)
    # add stars
    for u, m in zip(cu, cm):
        # related range, only 5-sigma covered
        t = np.array(np.arange(-5*sig, 5*sig+1) + u, dtype=int)
        # remove pixels outside the range
        if t[0] < 0:
            t = t[-t[0]:]
        if t[-1] >= nu:
            t = t[:nu-t[-1]-1]
        # add simulated flux
        sm[t] += gau(t, 2.5**(-m), u, sig) / nv
    return sm
