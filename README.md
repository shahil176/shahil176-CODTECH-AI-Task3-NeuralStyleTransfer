README - NEURAL STYLE TRANSFER SYSTEM

COMPANY: CODTECH IT SOLUTIONS PVT. LTD

NAME: SHAHIL MURMU

INTERN ID: [YOUR INTERN ID]

DOMAIN: ARTIFICIAL INTELLIGENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH KUMAR

Task 3 Description – Neural Style Transfer using Deep Learning

The primary objective of Task 3 is to develop a Neural Style Transfer system using Python and deep learning techniques. Neural Style Transfer (NST) is a popular application of Artificial Intelligence in the field of computer vision that allows the combination of two different images to create a new artistic image. The system takes a content image and a style image as input and generates an output image that preserves the content structure while applying the artistic style of the second image.

In this project, Python and the PyTorch deep learning framework are used to implement Neural Style Transfer. A pre-trained convolutional neural network, VGG19, is utilized to extract important features from both the content and style images. These features represent high-level patterns such as shapes, textures, and colors. The system does not require training the model from scratch; instead, it uses transfer learning to reuse the knowledge of the pre-trained model.

The process begins by loading the content and style images and preprocessing them using resizing and tensor conversion techniques. The VGG19 model is then used as a feature extractor to obtain intermediate representations of both images. A target image is initialized, usually as a copy of the content image, and is gradually optimized to match both content and style characteristics.

Two main loss functions are used in this process: content loss and style loss. The content loss ensures that the generated image retains the structure and objects of the original content image. The style loss ensures that the artistic patterns, textures, and colors of the style image are applied to the output image. The total loss is a combination of both, and the optimization process minimizes this loss using gradient descent.

As the training progresses, the target image is updated iteratively, gradually transforming into a stylized version of the content image. After several iterations, the final output image is generated and saved as a file. This output demonstrates how artificial intelligence can be used to create artistic transformations of real-world images.

Neural Style Transfer is widely used in digital art, photo editing applications, and creative AI tools. It is also used in social media filters, graphic design tools, and artistic image generation systems. This project helps in understanding important deep learning concepts such as convolutional neural networks, feature extraction, optimization, and transfer learning.

Through this task, valuable hands-on experience is gained in working with PyTorch, image processing libraries, and neural network architectures. It also demonstrates how AI models can go beyond classification tasks and be used for creative generation tasks.

In conclusion, the Neural Style Transfer System is a powerful demonstration of how artificial intelligence can combine content and artistic styles to generate visually appealing images. This project provides a strong foundation for advanced topics in computer vision and generative AI.

OUTPUT

The system successfully generates a stylized image by combining the content of one image with the artistic style of another image.

Example Output:

Content Image + Style Image → Output Stylized Image
<img width="512" height="512" alt="Image" src="https://github.com/user-attachments/assets/5a3b57c2-1f51-43a6-bade-1431cf79d0e5" />
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/36dbf2bf-7987-41ec-b910-6bcb4097bff7" />
<img width="1600" height="1333" alt="Image" src="https://github.com/user-attachments/assets/8417d6a8-b306-4397-9495-7f3153bfa5e3" />
<img width="1600" height="715" alt="Image" src="https://github.com/user-attachments/assets/b9775108-65f0-4b68-83cc-d68f1d875c1c" />
