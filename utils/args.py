import torch
import os
class Args:

    def __init__(self):
        self.tr_batch_size = 8
        self.vd_batch_size = 8
        self.num_workers = 8
        self.inplanes = 4

        self.model_name = 'resunet'
        self.backbone = 'resnet50'
        self.epochs = 80
        self.lr = 0.1

        self.gpu_ids = [0, 1]
        self.gpu_id = '0, 1'
        os.environ['CUDA_VISIBLE_DEVICES'] = self.gpu_id
        self.cuda = torch.cuda.is_available()
        self.apex = True

        self.no_val = False