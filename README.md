# Color Isolation
Code snippet to isolate **a** desired color using HSV trackbars in OpenCV

Works better on images with small color gradients (flat colors) such as cartoon images. For noiser images, especially real life images, further image augmentation such as contrast balancing should be done prior.

It is possible to extract more than one colour using the snippet, but doing it manually is tedious.

Note that trackbar values do not update and you will need to note down the desired values.
