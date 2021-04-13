def clouds_single_axis(cloud_no=2, n=1200, stretch=0.5, split_dist=10):
    # generate n random points
    x = np.random.randn(n)
    # divide into number of arrays representing each cloud
    x = [x[i:i + int(n/cloud_no)] for i in range(0, n, int(n/cloud_no))]
    # transform arrays so that clouds are distinct
    x = np.matmul(np.diag(((np.random.randint(2, size=cloud_no)*2)-1)*stretch), x)
    x = np.array([x[i] + ((np.repeat(np.random.rand(1), int(n/cloud_no))*2)-1)*split_dist for i in range(0, cloud_no)])
    return(np.squeeze(x.reshape((1,n))))

def clouds_multi_axis(cloud_no=2, naxs=3, n=1200, stretch_par=[1, 1, 1], dist_par=[5, 5, 5]):
    # define a permutation for the generated axis
    arr = np.random.permutation(range(0, n))
    # extract each axis and apply permutation
    output = []
    for i in range(0, naxs):
        gen = clouds_single_axis(cloud_no=cloud_no, n=n,
                                        stretch=stretch_par[i],
                                        split_dist=dist_par[i])
        output.append(gen[arr])
    return(np.array(output))