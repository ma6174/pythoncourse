# wfp, 6/15/07
# wfp, updated names, 10/11
# simple dictionaries

scores_dict={"joan":90,"bill":80,"john":75,"amy":45,"fred":60,"janice":85,"irving":10}

print("All the names")
for name_str in scores_dict:
    print(name_str)

print()
print("The name-score pairs")
for name_str,score_int in scores_dict.items():
    print("{:7s} : {:d}".format(name_str,score_int))

#update
pair_list=input("Enter a name and a score (: separated) ").split(":")
name_str,score_int=(pair_list[0].strip(),int(pair_list[1].strip()))
print("{:7s} {:d}".format(name_str,score_int))
scores_dict[name_str]=score_int
if "rich" in scores_dict:
    print("Updated dictionary has new value: ",end=' ')
    print("{:7s} : {:d}".format(name_str,scores_dict[name_str]))
