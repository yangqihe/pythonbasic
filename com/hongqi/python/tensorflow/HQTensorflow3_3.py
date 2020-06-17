import struct
import numpy as np
import PIL.Image

def read_image(filename):
    f = open(filename,'rb')
    index = 0
    buf = f.read()
    f.close()

    magic,numImages,rows,columns = struct.unpack_from('>IIII',buf,index)
    index += struct.calcsize('>IIII')

    print('numImages',numImages)

    for i in range(0,numImages):
        image = PIL.Image.new('L',(columns,rows))

        for x in range(rows):
            for y in range(columns):
                image.putpixel((y,x),int(struct.unpack_from('B',buf,index)[0]))
                index += struct.calcsize('B')
        print('save '+str(i)+'image')
        image.save('/Users/yangchiher/Desktop/test_/'+str(i)+'.png')

def read_label(filename,saveFilename):
    f = open(filename,'rb')
    index = 0
    buf = f.read()
    f.close()
    magic,labels = struct.unpack_from('>II',buf,index)
    index += struct.calcsize('>II')
    labelArr = [0] * labels
    for x in range(labels):
        labelArr[x] = int(struct.unpack_from('>B',buf,index)[0])
        index +=struct.calcsize('>B')

    save = open(saveFilename,'w')
    save.write(','.join(map(lambda  x:str(x),labelArr)))
    save.write('\n')
    save.close()
    print('save labels success')

if __name__ == '__main__':
    #read_image('/Users/yangchiher/Desktop/test_/train-images-idx3-ubyte')
    read_label("/Users/yangchiher/Desktop/test_/train-labels-idx1-ubyte","/Users/yangchiher/Desktop/test_/save.txt")