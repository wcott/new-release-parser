#!/usr/bin/python
from datetime import date

# Parellel lists for each new release entry
name_list = list()
mfg_list = list()
link_list = list()
category_list = list()
# Dictionary containing all new releases
new_release_dict = dict()
crowd_funding_formatted_list = list()

with open('release.tsv') as f:
    lines = f.readlines()[1:]
    for line in lines:
        name, mfg, link, category, nsfw = line.split('\t')
        # Remove white space, title case everything, remove quotations
        if "Yes" in nsfw:
            name_list.append(name.strip().title().replace('"','').replace('\'','') + " NSFW")
        else:
            name_list.append(name.strip().title().replace('"','').replace('\'',''))
        mfg_list.append(mfg.strip().title().replace('"','').replace('\'',''))
        link_list.append(link.strip())
        category_list.append(category.strip().title().replace('"','').replace('\'',''))

for i in range(0, len(name_list) - 1):
    # if there is more than one release per mfg, I want to only have the mfg
    # listed once. So, I'm modeling my data structure after this idea.

    if "Crowd Funding" in category_list[i]:
        crowd_funding_formatted_list.append("* [{0}]({1})\n".format(name_list[i], link_list[i]))
    else:
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

date = date.today().isoformat()
with open('archive/{0}'.format(date), "w") as f:
    f.write("What up mini people?! Got some more new releases, teasers, and kickstarters for ya!\n\n\n")
    f.write("**New Releases and Teasers**\n\n\n")
    for mfg, values in new_release_dict.iteritems():
        if len(values) == 1:
            release_dict = values[0]
            if "Teaser" in release_dict['category']:
                f.write("[{0}: {1} - {2}]({3})\n\n\n".format(mfg, release_dict['name'], release_dict['category'], release_dict['link']))
            else:
                f.write("[{0}: {1}]({2})\n\n\n".format(mfg, release_dict['name'], release_dict['link']))
        else:
            f.write("{0}\n".format(mfg))
            f.write("\n")
            for value in values:
                if "Teaser" in value['category']:
                    f.write("* [{0} - {1}]({2})\n".format(value['name'], value['category'], value['link']))
                else:
                    f.write("* [{0}]({1})\n".format(value['name'], value['link']))
            f.write("\n\n")
    f.write("\n**Crowd Funding Campaigns**\n\n")
    for item in crowd_funding_formatted_list:
        f.write(item)

    f.write("\n\n\n")
    f.write("If I missed any releases in the last two weeks don't hesitate to "
            "list them and I will update the post.If you see any mistakes/broken "
            "links or have any questions, feel free to message me or comment on the thread. PAINT MORE MINIS!\n\n")
    f.write("[archive of older posts](https://www.reddit.com/r/minipainting/wiki/newreleasesarchive)\n\n")
    f.write("Would you like to help find the new releases that go into this post? Private message /u/SDuby!")
