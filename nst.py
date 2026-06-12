import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from torchvision.utils import save_image

# Device
device = torch.device("cpu")

# Load images
image_size = 512

transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor()
])

content = transform(Image.open("content.jpg")).unsqueeze(0).to(device)
style = transform(Image.open("style.jpg")).unsqueeze(0).to(device)

# Load VGG19 (CORRECT WAY)
vgg = models.vgg19(weights=models.VGG19_Weights.DEFAULT).features.to(device).eval()

for param in vgg.parameters():
    param.requires_grad = False

# Get features function
def get_features(x):
    layers = ['0', '5', '10', '19', '28']
    features = []
    for name, layer in vgg._modules.items():
        x = layer(x)
        if name in layers:
            features.append(x)
    return features

# Target image
target = content.clone().requires_grad_(True)

optimizer = optim.Adam([target], lr=0.003)

# Training loop
for step in range(200):

    target_features = get_features(target)
    content_features = get_features(content)
    style_features = get_features(style)

    content_loss = torch.mean((target_features[3] - content_features[3]) ** 2)
    style_loss = torch.mean((target_features[0] - style_features[0]) ** 2)

    total_loss = content_loss + 100 * style_loss

    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()

    if step % 20 == 0:
        print("Step:", step, "Loss:", total_loss.item())

# Save output
save_image(target, "output.jpg")
print("Done! Saved as output.jpg")
