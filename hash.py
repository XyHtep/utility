import hashlib

def getHash(file_path):
    m = hashlib.md5()
    s = hashlib.sha1()
    ss = hashlib.sha256()
    sss = hashlib.sha512()

    with open(file_path,'rb') as f:
        line = f.read()
        m.update(line)
        s.update(line)
        ss.update(line)
        sss.update(line)
    md5code = m.hexdigest()
    sha1code = s.hexdigest()
    sha256code = ss.hexdigest()
    sha512code = sss.hexdigest()
    return f"MD5 hash: {md5code}\nSHA1 hash: {sha1code}\nSHA256 hash: {sha256code}\nSHA512 hash: {sha512code}"

if __name__ == "__main__":
    """ Be aware of tailing whitespace"""
    check_file = str(input(r"path to file: "))
    check_file.replace('"', "")
    print(getHash(check_file))