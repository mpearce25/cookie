
# Provide path to the original training data (all of it)
f = open("/home/yelman/Desktop/preprocess/orig/de-en/train_orig.en", "r")
lines_orig = f.readlines()
f.close()

# Provide path to the paraphrased training data (all of it)
f = open("/home/yelman/Desktop/preprocess/orig/de-en/train.en", "r")
lines_paraphrase = f.readlines()
f.close()

print(len(lines_orig), len(lines_paraphrase))

# Provide path to the original tags
f = open("/home/yelman/Desktop/preprocess/orig/de-en/train.tags.de-en_old.en", "r")
lines_tags = f.readlines()
f.close()


for i in range(len(lines_tags)):
    if i % 10000 == 0:
        print(i)
    try:
        idx = lines_orig.index(lines_tags[i])
    except:
        idx = -1
    if idx != -1:
        lines_tags[i] = lines_paraphrase[idx]


# Write lines_tags to new file for tags paraphrase. Save it inside orih/de-en as trains.tags.de-en.en to run it with bash script.
f = open('tag_para_formality', 'w')
f.writelines(lines_tags)
f.close()
