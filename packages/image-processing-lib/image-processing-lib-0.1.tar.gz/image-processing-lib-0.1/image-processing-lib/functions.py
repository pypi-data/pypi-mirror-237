
import cv2
import numpy as np
import matplotlib.pyplot as plt

def open_img(img, color_space=None, array32=True, uint8=False):
    '''
        convert the image to the specified color space
        ====
        inputs:
        img: ndarray or path to image
        color_space: string, one of the following: RGB, HSV, LUV, HLS, YUV, YCbCr, GRAY
        array32: boolean, if True, the image is converted to float32
        uint8: boolean, if True, the image is converted to uint8

        outputs:
        img: ndarray, the image converted to the specified color space
    '''
    conversion = {
        "RGB" : cv2.COLOR_BGR2RGB,
        "HSV" : cv2.COLOR_BGR2HSV,
        "LUV" : cv2.COLOR_BGR2LUV,
        "HLS" : cv2.COLOR_BGR2HLS,
        "YUV" : cv2.COLOR_BGR2YUV,
        "YCbCr" : cv2.COLOR_BGR2YCrCb,
        "GRAY" : cv2.COLOR_BGR2GRAY,
    }


    # is the image a path or cv2 image
    if isinstance(img, str):
        img = cv2.imread(img)


    # if the color space is None, return the image
    if color_space == None and array32:
        return img.astype(np.float32)
    
    #raise an error if the color space is not valid
    if color_space not in conversion:
        raise ValueError("Invalid color space, choose from RGB, HSV, LUV, HLS, YUV, GRAY")
    
    # convert the image to the color space as a float32
    if array32 :
        return cv2.cvtColor(img, conversion[color_space]).astype(np.float32)
    
    # convert the image to the color space as a uint8
    elif uint8:
        return cv2.cvtColor(img, conversion[color_space]).astype(np.uint8)
    
    else:
        return cv2.cvtColor(img, conversion[color_space])


def display( *args, figsize=(10,10), nb_cols=3):
    '''
    input : 
    images (ndarray) and labels (string) in the order you want them to be displayed
    figsize : size of the figure (width, height)
    nb_cols : number of columns
    
    Outpu : Display the images and labels
    '''

    images = []
    labels = []

    #Check for the type of the arguments
    for arg in args:
        if isinstance(arg, np.ndarray):
            images.append(arg)
        elif isinstance(arg, str):
            labels.append(arg)
        
        else:
            raise TypeError("The arguments must be numpy arrays (images) or strings")
    

    #concatenate the images and labels into a list of tuples [(img, 'title'), ...)]
    nb_images = len(images)
    nb_labels = len(labels)

    difference = nb_images - nb_labels

    list_img_label = []

    #chek for the difference between the number of images and labels

    if difference > 0:
        for i in range(nb_labels):
            list_img_label.append((images[i], labels[i]))
        for i in range(nb_labels, nb_images):
            list_img_label.append((images[i], ''))
    
    elif difference < 0:
        raise  ValueError("The number of images and labels must be the same")
    
    else:
        for i in range(nb_images):
            list_img_label.append((images[i], labels[i]))

    #display the images
    plt.figure(figsize=figsize)
    n = len(images)
    nb_ligns = (n - 1)//nb_cols + 1  # use (n - 1) to avoid extra row when n is a multiple of nb_cols
    
    for i, (img, title) in enumerate(list_img_label):
        if title == None:
            title = ' '
        
        plt.subplot(nb_ligns, nb_cols, i+1)
        
        
        # Check image dimensions to determine if it's grayscale or color
        if len(img.shape) == 2 or img.shape[2] == 1:
            plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        else:
            plt.imshow(img, cmap='Accent',vmin=0, vmax=255)
            
        plt.axis('off')
        plt.title(title)
        
    plt.tight_layout()  # Adjust the spacing between subplots
    plt.show()

def normalize_img(img):
    '''
    input : 
    img : image to normalize
    
    return : normalized image
    '''
    image = np.copy(img)
    return (image - np.min(image))/(np.max(image) - np.min(image))

def flatten_unflatten(img, flatten=True, shape=None):
    '''
    input :
    img : image to flatten
    flatten : if True, flatten the image is Fase, un flatten the image to shape
    '''
    image = np.copy(img)

    if flatten:
        return image.reshape(-1)

    else :
        return image.reshape(shape)

def binary(img, threshold=125, upto255=True):
    '''
    input :
    img : image to binarize
    threshold : threshold value
    upto255 : if True, the image is binarized to 255 else to 1
    
    return : binarized image
    '''

    image = np.copy(img)
    image[image < threshold] = 0
    if upto255:
        image[image >= threshold] = 255
    else:
        image[image >= threshold] = 1
    return image

def img2blocs(img, bloc_size, padding_type='reflect'):
    '''
    input : 
    
    img : image to split into blocs
    bloc_size : size of the blocs
    padding_type : type of padding to apply to the image
    where the padding types are : 'edge', 'linear_ramp', 'maximum', 'mean', 'median', 'minimum', 'reflect', 'symmetric', 'wrap'
    does not work with 'constant'

    output : 
    
    list of blocs

    If the image is not square, it is cropped to the smallest side
    '''
    #si l'image possede plus de 1 cannal (elle est en couleur) =>  on ne considere que h et w
    if len(img.shape)>2:
        h, w = img.shape[:2]

        blocs=[]

        #l'image est carrée
        if h==w:
            #l'image est divisible par la taille des blocs
            if h % bloc_size == 0:
                #calcul du nombre de blocs
                nb_blocs = h // bloc_size
                for i in range(nb_blocs):
                    for j in range(nb_blocs):
                        bloc = img[i*bloc_size:(i+1)*bloc_size, j*bloc_size:(j+1)*bloc_size]
                        blocs.append(bloc)
                return blocs
            
            else:
                rest = h % bloc_size #Calcul de combien l'image est trop grande
                agrandir = bloc_size - rest #calcul du nombre de pixels
                if agrandir % 2 == 0: # si il est pair, on peut agrandir l'image de la même taille de chaque côté
                    image = np.pad(img, ((agrandir//2, agrandir//2), (agrandir//2, agrandir//2), (0,0)), padding_type)
                    return img2blocs(image, bloc_size, padding_type)
                else: #sinon on agrandit de 1 de plus à droite
                    image = np.pad(img, ((agrandir//2, agrandir//2 + 1), (agrandir//2, agrandir//2 + 1), (0,0)), padding_type)
                    return img2blocs(image, bloc_size, padding_type)
        
        else: #l'image n'est pas carrée 
            #on calcule la taille du plus petit côté
            min_size = min(h, w)
            #on calcule le nombre de blocs
            nb_blocs = min_size // bloc_size
            #on recadre l'image
            image = img[:min_size, :min_size]
            #Recursivement, on applique la fonction à l'image recadrée
            return img2blocs(image, bloc_size, padding_type)
    
    else: #si l'image est en niveau de gris

        h, w = img.shape
        blocs=[]

        #the image is square
        if h==w:
            #the image is divisible by the bloc size 
            if h % bloc_size == 0:
                #calcul du nombre de blocs
                nb_blocs = h // bloc_size
                for i in range(nb_blocs):
                    for j in range(nb_blocs):
                        bloc = img[i*bloc_size:(i+1)*bloc_size, j*bloc_size:(j+1)*bloc_size]
                        blocs.append(bloc)
                return blocs
            
            else:
                rest = h % bloc_size #Calcul de combien l'image est trop grande
                agrandir = bloc_size - rest #calcul du nombre de pixels
                if agrandir % 2 == 0: # si il est pair, on peut agrandir l'image de la même taille de chaque côté
                    image = np.pad(img, ((agrandir//2, agrandir//2), (agrandir//2, agrandir//2)), padding_type)
                    return img2blocs(image, bloc_size, padding_type)
                else: #sinon on agrandit de 1 de plus à droite
                    image = np.pad(img, ((agrandir//2, agrandir//2 + 1), (agrandir//2, agrandir//2 + 1)), padding_type)
                    return img2blocs(image, bloc_size, padding_type)
        
        else: #l'image n'est pas carrée 
            #on calcule la taille du plus petit côté
            min_size = min(h, w)
            #on calcule le nombre de blocs
            nb_blocs = min_size // bloc_size
            #on recadre l'image
            image = img[:min_size, :min_size]
            #Recursivement, on applique la fonction à l'image recadrée
            return img2blocs(image, bloc_size, padding_type)

def resize_img(img, width=None, height=None):
    """
    Resize the image to the specified width and height.
    """
    original_height, original_width = img.shape[:2]

    if height < original_height or width < original_width:

        if width and not height:
            ratio = width / img.shape[1]
            dim = (width, int(img.shape[0] * ratio))
        elif height and not width:
            ratio = height / img.shape[0]
            dim = (int(img.shape[1] * ratio), height)
        else:
            dim = (width, height)

        return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    
    else:

        if width and not height:
            ratio = width / img.shape[1]
            dim = (width, int(img.shape[0] * ratio))
        elif height and not width:
            ratio = height / img.shape[0]
            dim = (int(img.shape[1] * ratio), height)
        else:
            dim = (width, height)

        return cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)


def rotate_img(img, angle):
    """
    Rotate the given image by the specified angle.
    """
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0) #create the rotation matrix
    return cv2.warpAffine(img, M, (w, h))


def enhance_img(img, 
                  add_noise=False, noise_intensity='medium', custom_noise_value=None,
                  add_blur=False, blur_intensity='medium', custom_blur_value=None,
                  change_contrast=False, contrast_intensity='medium', custom_contrast_alpha=None, custom_contrast_beta=None):
    """
    Enhance the image by adding noise, applying blur, and adjusting contrast.

    Parameters:
    - img: input image (ndarray).
    
    - add_noise: Boolean indicating whether to add noise or not.
    - noise_intensity: level of noise to add. Choices are ['low', 'medium', 'high'].
    - custom_noise_value: Custom noise level.
    
    - add_blur: Boolean indicating whether to apply blur or not.
    - blur_intensity: Intensity of blur. Choices are ['low', 'medium', 'high'].
    - custom_blur_value: Custom kernel size for blur.
    
    - change_contrast: Boolean indicating whether to adjust contrast or not.
    - contrast_intensity: Intensity of contrast change. Choices are ['low', 'medium', 'high'].
    - custom_contrast_alpha: Custom contrast scaling factor.
    - custom_contrast_beta: Custom contrast delta value.

    Returns:
    - Enhanced image.
    """

    noise_levels = {
        'low': 0.02,
        'medium': 0.05,
        'high': 0.1
    }

    blur_values = {
        'low': 3,
        'medium': 5,
        'high': 9
    }

    contrast_values = {
        'low': (1.1, 10),
        'medium': (1.3, 20),
        'high': (1.5, 30)
    }

    result_img = img.copy()

    # Handle noise
    if add_noise:
        noise_val = custom_noise_value if custom_noise_value is not None else noise_levels[noise_intensity]
        gauss = np.random.normal(0, noise_val, img.shape)
        result_img = np.clip(result_img + gauss * 255, 0, 255).astype(np.float32)

    # Handle blur
    if add_blur:
        blur_val = custom_blur_value if custom_blur_value is not None else blur_values[blur_intensity]
        result_img = cv2.GaussianBlur(result_img, (blur_val, blur_val), 0)

    # Handle contrast
    if change_contrast:
        alpha, beta = contrast_values[contrast_intensity]
        alpha = custom_contrast_alpha if custom_contrast_alpha is not None else alpha
        beta = custom_contrast_beta if custom_contrast_beta is not None else beta
        result_img = cv2.convertScaleAbs(result_img, alpha=alpha, beta=beta)

    return result_img



