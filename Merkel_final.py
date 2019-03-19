#%%
import merkletools
import json
mt=merkletools.MerkleTools()

#%%
with open("ex.json", "r") as read_file:
        data = json.load(read_file)

#%%
data_list=[]
for x in data:
    data_list.append(data[x])

#%%
mt.add_leaf(data_list, True)
print(mt.get_leaf_count())
mt.make_tree()
print(mt.is_ready)

#%%
mt.reset_tree()

#%%
print(mt.get_merkle_root())

#%%
ans={}
for x in data:
    for i in range(len(data_list)):
        if data[x]==data_list[i]:
            value=i
    ans[x]={
        "Value" : data[x],
        "Hash": mt.get_leaf(value),
        "Proof": mt.get_proof(value)
    }
mk={"Merkel_root" : mt.get_merkle_root()}
with open("Merkle_json.json", "w") as write_file:
        json.dump([ans,mk], write_file)

#%%
for x in range(len(data_list)):
    print(data_list[x])