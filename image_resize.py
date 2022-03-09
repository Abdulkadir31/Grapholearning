import cv2

def reduce_size(path):
    img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
    print("Original Dimensions : '",img.shape)
    scale_percent = 30
    width = int(img.shape[1] * scale_percent/100)
    height = int(img.shape[0] * scale_percent/100)
    dim = (width,height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite("Images\Rescaled.jpg",resized)
    print("Reduced Dimensions : '",resized.shape)
    return "images\Rescaled.jpg"