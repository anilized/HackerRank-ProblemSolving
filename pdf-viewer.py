def designerPdfViewer(h, word):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pos = []
    height = []
    i = 0
    while i < len(letter):
        pos.append([letter[i], h[i]])
        i+=1
    #print (pos)
    for k in  word:
        for p in range(len(pos)):
            if pos[p][0] == k:
                height.append(pos[p][1])
    #print (height)
    area = len(word)*max(height)
    return area