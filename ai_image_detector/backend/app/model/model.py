import torch
import torch.nn as nn
import timm


#  Defines a dual-branch neural network that analyzes images 
# using both a Convolutional Neural Network (ConvNeXt) and 
#  a Vision Transformer (ViT) to detect AI-generated features.
 
class HybridModel(nn.Module):
    
     # Initializes the model by setting up the two specialized branches,
     # the fusion layer to combine their insights, and the final 
     # classification head.
     
    def __init__(self):
        super().__init__()

        # Spatial branch: Uses ConvNeXt to look at textures and shapes
        self.spatial_branch = timm.create_model(
            "convnext_small",
            pretrained=False,
            num_classes=0
        )

        # Frequency branch: Uses a Vision Transformer to look at mathematical patterns
        self.freq_branch = timm.create_model(
            "vit_base_patch16_224",
            pretrained=False,
            num_classes=0
        )

        embed_dim = 768
        # Fusion layer: Merges the data from both branches into a single report
        self.fusion = nn.Linear(embed_dim * 2, embed_dim)
        # Decision head: Outputs a single score representing the AI likelihood
        self.head = nn.Linear(embed_dim, 1)

    
     # Defines the "forward pass" of the model: how data travels from 
     # the input images to the final prediction score.
     
    def forward(self, spatial, freq):
        # Pass inputs through their respective specialized branches
        spatial_emb = self.spatial_branch(spatial)
        freq_emb = self.freq_branch(freq)

        # Concatenate (glue) the two reports together
        fused = torch.cat([spatial_emb, freq_emb], dim=1)
        
        # Shrink the combined data and produce the final output value
        fused = self.fusion(fused)
        out = self.head(fused).squeeze()

        return out