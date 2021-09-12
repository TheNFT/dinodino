try:
    from PIL import Image
except ImportError:
    import Image

count = 1
while count <= 500:

    filecount = str(count)

    im1 = Image.open(r'1/'+filecount+'.png').convert("RGB")
    im1.save(r'1/'+filecount+'.jpeg')

    count += 1