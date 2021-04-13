def gen_sine_wave(n=1000, s=1, amp=1, wl=1, ns_mean=0, ns_var=1, x_range=(0,1), r_rad=0, swap_axis=False):
    # n - number of points to generate
    # s - slope gradient of wave
    # amp - amplitude of wave
    # wl - wavelength equivalent parameter
    # ns_mean, ns_var - noise mean and variance
    x = np.random.rand(n)
    x = np.interp(x, (x.min(), x.max()), x_range)
    epsilon = ns_mean + ns_var * np.random.randn(n)
    # apply to formula [y = s*x + mag*sin(wl*x)]
    y = s*x + amp*np.sin(wl*x) + epsilon
    # create rotation matrix
    rM = np.array((np.cos(r_rad), -np.sin(r_rad), np.sin(r_rad), np.cos(r_rad))).reshape((-1, 2))
    t = (x, y)
    output = np.matmul(rM, t)
    if (swap_axis==True):
        output = output[[1, 0],:]
    return(output)