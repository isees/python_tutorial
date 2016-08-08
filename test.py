cache = []

url = "http://66.media.tumblr.com/50934c3343bb039175194bc6fbf27753/tumblr_o75bpk6iXu1r2xjmjo1_1280.jpg;http://66.media.tumblr.com/daf12a1d2fa3210d25794ce638d85deb/tumblr_o6zmu0MGku1r2xjmjo1_1280.jpg;http://65.media.tumblr.com/1c32beb1a6f2695af6e459a397121d4e/tumblr_o6zkyew96T1r2xjmjo1_1280.jpg;http://66.media.tumblr.com/dd735a962e8e4fb61c587ad7317b1eae/tumblr_o6zkruEgdO1r2xjmjo1_1280.jpg;http://66.media.tumblr.com/dd735a962e8e4fb61c587ad7317b1eae/tumblr_o6zkruEgdO1r2xjmjo1_1280.jpg;http://66.media.tumblr.com/4344c81ffd32df3276a70f9bb9aaaa37/tumblr_o6zkruEgdO1r2xjmjo2_1280.jpg;http://66.media.tumblr.com/4344c81ffd32df3276a70f9bb9aaaa37/tumblr_o6zkruEgdO1r2xjmjo2_1280.jpg;http://67.media.tumblr.com/09805f06aef8ae23b7cd394dc0c4092a/tumblr_o6yupn2o7s1r2xjmjo1_1280.jpg;http://67.media.tumblr.com/f05d219bef656c3e7ad42bb1973036e5/tumblr_o6yu1vAbEG1r2xjmjo1_1280.jpg;http://67.media.tumblr.com/8a4584891810498430c60bc8f60e588c/tumblr_o6yt7bfqQU1r2xjmjo1_1280.jpg;http://67.media.tumblr.com/c64065ac349de09cfd05eedd8fe8639f/tumblr_o6vvqo4g9k1r2xjmjo1_1280.jpg;http://65.media.tumblr.com/0e82d79eb70a5a183bf8a9927d73480e/tumblr_o6v7fiSDlh1r2xjmjo1_1280.jpg;http://66.media.tumblr.com/1579f6d25f467d19e9d4dce46c0da8cf/tumblr_o6v6vvvoG31r2xjmjo1_1280.jpg;http://66.media.tumblr.com/2669c644395b0fb243a672fd95c47d8f/tumblr_o6v6dp0py71r2xjmjo1_1280.jpg;http://65.media.tumblr.com/4daaf4d39ccdfcdbddb92214dd176330/tumblr_o6uf4iSpPR1r2xjmjo1_1280.jpg;http://65.media.tumblr.com/4daaf4d39ccdfcdbddb92214dd176330/tumblr_o6uf4iSpPR1r2xjmjo1_1280.jpg;http://65.media.tumblr.com/23893dd591ba0ca8df918e79d7807bac/tumblr_o6uf4iSpPR1r2xjmjo2_1280.jpg;http://65.media.tumblr.com/23893dd591ba0ca8df918e79d7807bac/tumblr_o6uf4iSpPR1r2xjmjo2_1280.jpg;http://67.media.tumblr.com/8363ef6e9c94e5180f9856580a0f8def/tumblr_o6u91iHLRo1r2xjmjo1_r1_1280.jpg;http://65.media.tumblr.com/b611ed9b330b4afbdaefd01a873d315b/tumblr_o6u7g1JG2X1r2xjmjo1_r1_1280.jpg;http://65.media.tumblr.com/b611ed9b330b4afbdaefd01a873d315b/tumblr_o6u7g1JG2X1r2xjmjo1_r1_1280.jpg;http://67.media.tumblr.com/c7204ed1d7df41f880e110eda39fd9b8/tumblr_o6u7g1JG2X1r2xjmjo2_r1_1280.jpg;http://67.media.tumblr.com/c7204ed1d7df41f880e110eda39fd9b8/tumblr_o6u7g1JG2X1r2xjmjo2_r1_1280.jpg"

imageUrlList = url.split(";")
print imageUrlList.__len__()

cacheList = []
for m in imageUrlList:
    if m not in cacheList:
        cacheList.append(m)

print cacheList.__len__()

