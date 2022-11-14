import tarfile


def extract(tar_path, target_path):
    try:
        tar = tarfile.open(tar_path, "r:gz")
        filenames = tar.getnames()
        for filename in filenames:
            tar.extract(filename, target_path)
        tar.close()
    except Exception as e:
        print('extract error %s' %e)


extract('/tmp/tarball.tar.gz', '/tmp/x')
