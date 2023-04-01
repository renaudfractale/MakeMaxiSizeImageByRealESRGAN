
def X4Size(im,imF,step,factor,V,model,Image,ImageChops):
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    print(height)
    print(width)
    #Image de fond
    imM1 = Image.new(mode="RGBA", size=(height*factor, width*factor),color=(0, 0, 0, 0))
    #B1
    for i_height in range(0, height-1, step):
        for i_width in range(0, width-1, step):
            print("B1 : " + str(i_height)+"x"+str(i_width))  
            left = i_width
            top = i_height
            right = i_width+step
            bottom = i_height+step
    
            im1 = im.crop((left, top, right, bottom))
            sr_image  = model.predict(im1)
            sr_image.putalpha(255)
            imM1.alpha_composite(sr_image, dest=(left*factor, top*factor))
    if step!=width :
        imM2 = Image.new(mode="RGBA", size=(height*factor, width*factor),color=(0, 0, 0,0))
        #B2
        for i_height in range(int(-step/2), height-1, step):
            for i_width in range(int(-step/2), width-1, step):
                print("B2 : " + str(i_height)+"x"+str(i_width)) 
                left = i_width
                top = i_height
                right = i_width+step
                bottom = i_height+step

                im1 = im.crop((left, top, right, bottom))
                sr_image  = model.predict(im1)
                sr_image.putalpha(0)
                sr_imageF=ImageChops.add(sr_image,imF)
                imM2.alpha_composite(sr_imageF, dest=(left*factor, top*factor))
 
        #Merge
        imM1.alpha_composite(imM2)
    imM1 = imM1.convert("RGB")
    return imM1
