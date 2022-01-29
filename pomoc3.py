from PIL import Image, ImageFilter

im = Image.open("obraz.png")
im.show()

im1 = im.filter(ImageFilter.BLUR) # rozmywa obraz
im1.save("image1.jpg")
im2 = im.filter(ImageFilter.CONTOUR) # tworzy kontur obrazu
im2.save("image2.jpg")
im3 = im.filter(ImageFilter.DETAIL) #
im3.save("image3.jpg")
im4 = im.filter(ImageFilter.EDGE_ENHANCE)
im4.save("image4.jpg")
im5 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im5.save("image5.jpg")
im6 = im.filter(ImageFilter.EMBOSS)
im6.save("image6.jpg")
im7 = im.filter(ImageFilter.FIND_EDGES) # też znajdowanie krawędzi
im7.save("image7.jpg")
im8 = im.filter(ImageFilter.SMOOTH) # wygładzanie
im8.save("image8.jpg")
im9 = im.filter(ImageFilter.SMOOTH_MORE) # mocniejsze wygładzanie
im9.save("image9.jpg")
im10 = im.filter(ImageFilter.SHARPEN) # wyostrzanie
im10.save("image10.jpg")