count = 0
theparagraph = open(theparapath, 'rb')
while 1:
    buffer = thefile.read(8192*1024)
    if not buffer: break
    count += buffer.count('\n')
thepara.close(  )
