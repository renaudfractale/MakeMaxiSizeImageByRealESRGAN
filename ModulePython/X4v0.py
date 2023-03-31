def X4Size(im,imF,step,factor,V,model,Image,ImageChops):
    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size
    print(height)
    print(width)
    #Image de fond
    imM1 = Image.new(mode="RGBA", size=(height*factor, width*factor),color=(0, 0, 0, 255))
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

            imM1.alpha_composite(sr_image.convert("RGBA"), dest=(left*factor, top*factor))
    imM1 = imM1.convert("RGB")
    return imM1
