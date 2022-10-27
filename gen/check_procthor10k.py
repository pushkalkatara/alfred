import prior

dataset = prior.load_dataset("procthor-10k")

count_kitchen_with_knife = 0
count_kitchenA_with_knife = 0
for i in range(len(dataset['train'])):
    scene = dataset['train'][i]['metadata']['roomSpecId']
    foundKnife = False
    if 'knife' in str(dataset['train'][i]['objects']):
        foundKnife = True
        print("Found Knife at id: {}, scene: {}".format(str(i), str(dataset['train'][i]['metadata']['roomSpecId'])))
    
    if 'kitchen' in scene and not foundKnife:
        print("Found kitchen but no knife at id: {}, scene: {}".format(str(i), str(dataset['train'][i]['metadata']['roomSpecId'])))

    if 'kitchen' in scene and foundKnife:
        count_kitchenA_with_knife+=1
    if scene == 'kitchen' and foundKnife:
        count_kitchen_with_knife+=1

print(count_kitchen_with_knife)
print(count_kitchenA_with_knife)