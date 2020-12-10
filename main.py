import os
if __name__ == "__main__":
    with open('dir.txt', 'r', encoding='utf8') as f:
        cache_dir = f.readline().strip()
        output_dir = f.readline().strip()
    cache_list = os.listdir(cache_dir)
    cache_list = [w for w in cache_list if w[-3:] == '.uc']
    cnt = 0
    for uc in cache_list:
        with open(cache_dir + '/' + uc, 'rb') as f1, open(output_dir + '/' + uc[:-3] + '.mp3', 'wb') as f2:
            for line in f1.readlines():
                line = bytes([w ^ b'\xa3'[0] for w in line])
                f2.write(line)
            f1.close()
            f2.close()
        cnt += 1
        print('Finished {} out of {}'.format(cnt, len(cache_list)))
    os.system('pause')
