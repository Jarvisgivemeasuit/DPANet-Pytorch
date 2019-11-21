import os

class Path:
    @staticmethod
    def db_root_dir(dataset_name):
        dataset_path_root = os.path.expanduser('~/dataset')
        if dataset_name == 'pascal_voc':
            # folder that contains VOCdevkit/.
            return os.path.join(dataset_path_root, "voc2012", "VOCdevkit")
        elif dataset_name == 'sbd':
            # folder that contains dataset/.
            return '/path/to/datasets/benchmark_RELEASE/'
        elif dataset_name == 'cityscapes':
            # foler that contains leftImg8bit/
            return '/path/to/datasets/cityscapes/'
        elif dataset_name == 'coco':
            return '/home/arron/Documents/arron/dataSet/coco'
        elif dataset_name == 'rssrai':
            return '/home/arron/dataset/rssrai2019'
        elif dataset_name == 'rssrai_grey':
            return '/home/arron/dataset/rssrai_grey/'
        else:
            print('Dataset {} not available.'.format(dataset_name))
            raise NotImplementedError

    project_root = '/home/arron/Documents/grey/paper/experiment'

# class RssraiPath:
#     def __init__(self, root_path):
#         self.root_path = root_path
#         self.path_dict = {}

#     def rssrai_path(self):
        