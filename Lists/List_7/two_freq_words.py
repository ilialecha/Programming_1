from easyinput import read, read_many

def find_freq_words(n):
    ws = 0
    w = {}
    for word in read_many(str):
        if not word in w: w[word]=1
        else:
            w[word]+=1
            if w[word] ==n:
                ws +=1
                if ws == 2:
                    return f"There are two words that appear {n} or more times."
    return f"Less than two words appear {n} or more times."

print(find_freq_words(read(int)))