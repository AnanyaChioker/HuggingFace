from transformers import pipline

classifier = pipline("sentimental-analysis")

res = classifier("something")

print(res)
