#!/usr/bin/python

# Parellel lists for each new release entry
name_list = list()
mfg_list = list()
link_list = list()
category_list = list()
# Dictionary containing all new releases
new_release_dict = dict()

with open('release.tsv') as f:
    for line in f: 
        name, mfg, link, category = line.split('\t')
        # Remove white space, title case everything, remove quotations
        name_list.append(name.strip().title().replace('"','').replace('\'',''))
        mfg_list.append(mfg.strip().title().replace('"','').replace('\'',''))
        link_list.append(link.strip())
        category_list.append(category.strip().title().replace('"','').replace('\'',''))

for i in range(0, len(name_list) - 1):
    # if there is more than one release per mfg, I want to only have the mfg
    # listed once. So, I'm modeling my data structure after this idea.
    
    dict_key = mfg_list[i]
    dict_values = {
                    "link": link_list[i],
                    "name": name_list[i],
                    "category": category_list[i]
                    }
    if dict_key in new_release_dict:
        new_release_dict[dict_key].append(dict_values)    
    else:
        new_release_dict[dict_key] = [(dict_values)]    
with open('formatted-reddit-post.txt', "w") as f:
    f.write("What up mini people?! Got some more new releases, teasers, and kickstarters for ya!\n\n\n")
    for mfg, values in new_release_dict.iteritems():
        if len(values) == 1:
            release_dict = values[0]
            f.write("[{0}: {1} - {2}]({3})\n\n\n".format(mfg, release_dict['name'], release_dict['category'], release_dict['link']))
        else:
            f.write("{0}\n".format(mfg))
            f.write("\n")
            for value in values:
                f.write("* [{0} - {1}]({2})\n".format(value['name'], value['category'], value['link']))
            f.write("\n\n")

    f.write("If I missed any releases in the last two weeks don't hesitate to "
            "list them and I will update the post.If you see any mistakes/broken " 
            "links or have any questions, feel free to message me or comment on the thread. PAINT MORE MINIS!\n\n")
    f.write("[archive of older posts](https://www.reddit.com/r/minipainting/wiki/newreleasesarchive)")
