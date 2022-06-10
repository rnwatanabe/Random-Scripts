def freq95(image, ds, scale=1, padding=0):
  '''
  Inputs:
  image - a 2d, one channel, image.
  ds - the spatial resolution of the image
  scale - the image will be scaled to this number before
   the frequency is computed. Useful if the necessary padding is
   very high. Defaults to 1.
  padding - size of the border of zeros that will be created around the image
   before the computation of the frequency. Useful if the 95 \% 
   frequency is very low.

  Outputs:
  f_95 - The frequency that respect the following equation:

  \begin{equation}
    \int_0^f E(f)df = 0.95E_tot
  \end{equation}

  f - frequency vector
  fft_image - fft of the image
  EnCum - cumulative energy at each frequency
  '''


  def fftimage(image, ds, padding=0):
    import cv2
    image_pad = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT,value=0)
    fft_image = np.abs(np.fft.fftshift(np.fft.fft2(image_pad)))
    fmax = 1/ds
    f = np.arange(-len(fft_image)//2,len(fft_image)//2)*fmax
    return f, fft_image

  def compute_frequency(fft_image_polar, f):
    f = f[len(f)//2:].reshape(1,-1)
    fft_image_polar_2 = (fft_image_polar/fft_image_polar.max()+1e-6)**2
    En_image = np.sum(f*fft_image_polar_2)
    EnCum_image = np.cumsum(np.sum(fft_image_polar_2*f, axis=0))
    f_95 = f[0,np.argwhere(EnCum_image<=0.95*En_image)[-1]]
    return f_95, EnCum_image


  from skimage.transform import warp_polar, rescale
  import numpy as np
  image = rescale(image, scale, anti_aliasing=True)
  dsscaled = ds/scale
  f, fft_image = fftimage(image, ds=dsscaled, padding=padding)
  fft_image_polar = warp_polar(fft_image,
                               output_shape=(360, 
                                             fft_image.shape[0]//2))
  f_95, EnCum = compute_frequency(fft_image_polar, f)

  return f_95, f, fft_image, EnCum
