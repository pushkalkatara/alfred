import prior

dataset = prior.load_dataset("procthor-10k")

print(str(dataset['train'][0]['objects']))

if 'knife' in str(dataset['train'][0]['objects']):
    print("yes")