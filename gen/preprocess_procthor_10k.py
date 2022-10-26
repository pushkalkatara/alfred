import gzip

from tqdm import tqdm

import prior

try:
    from prior import LazyJsonDataset
except:
    raise ImportError("Please update the prior package (pip install --upgrade prior).")

def load_dataset_constrained() -> prior.DatasetDict:

    dataset = prior.load_dataset("procthor-10k")
    train = dataset['train']
    val = dataset['val']
    test = dataset['test']

    supported_scene_types = ["kitchen", "living-room", "bathroom", "bedroom"]

    data = {"train" : None, "test": None, "val" : None}

    print(dir(train[0]))
    train_houses = []
    for house_idx in range(len(train)):
        specId = train[house_idx]['metadata']['roomSpecId']
        if specId in supported_scene_types:
            train_houses.append(train[house_idx])
    data['train'] = LazyJsonDataset(
            data=train_houses, dataset="procthor-dataset", split='train'
        )

    val_houses = []
    for house_idx in range(len(val)):
        specId = val[house_idx]['metadata']['roomSpecId']
        if specId in supported_scene_types:
            val_houses.append(val[house_idx])
    data['val'] = LazyJsonDataset(
            data=val_houses, dataset="procthor-dataset", split='val'
        )

    test_houses = []
    for house_idx in range(len(test)):
        specId = test[house_idx]['metadata']['roomSpecId']
        if specId in supported_scene_types:
            test_houses.append(test[house_idx])
    data['test'] = LazyJsonDataset(
            data=test_houses, dataset="procthor-dataset", split='test'
        )

    return prior.DatasetDict(**data)