data=['apple','carrot','mango']
fruits=['apple','mango','orange','watermelon']
veggies=['tomamto','beans','carrot','onoin']
for i in data:
    if i not in fruits:
        print(i)
    if i in veggies:
        print(i)