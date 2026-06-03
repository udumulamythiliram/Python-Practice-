#word frequency counter

def freq():
    with open("story.txt","r") as f:
        data = f.read()
        words = data.lower().split()
        count ={}
        for word in words:
            if word not in count:
                count[word]= 1
            else:
                count[word]+=1
    sorted_asc = dict(sorted(count.items(), key=lambda item: item[1],reverse = True))

    for word , num in list(sorted_asc.items())[:10]:
        print(word , num )
freq()

