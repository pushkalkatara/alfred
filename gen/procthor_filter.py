

# alfred only supports ["kitchen", "living-room", "bathroom", "bedroom"]
# alfred requires kitchen in a knife
# alfred requires interactable microwave in kitchen

supported_scene_types = ["kitchen", "living-room", "bathroom", "bedroom"]

def filter_alfred_scenes(dataset):
    all_scene_numbers = []
    for house_idx in range(len(dataset['train'])):
        specId = dataset['train'][house_idx]['metadata']['roomSpecId']
        objs = str(dataset['train'][house_idx]['objects'])
        if specId in supported_scene_types and 'Microwave' in objs and 'knife' in objs:
            all_scene_numbers.append(house_idx)
    print("total number of scenes after filtering :", len(all_scene_numbers))
    return all_scene_numbers