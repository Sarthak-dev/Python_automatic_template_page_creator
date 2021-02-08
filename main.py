import os.path
save_path = 'C:/Users/acer/Desktop/Work'
name_of_file = input("What is the name of the file: ")
completeName = os.path.join(save_path, name_of_file +".html")
file1 = open(completeName, "w")
message = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600&display=swap" rel="stylesheet">
    <title>Q & A</title>
</head>
<style>
    body{
        background-color:rgb(247, 41, 41);
    }
    #q{
        background-color: white;
        text-align: center;
        font-family: 'Ubuntu', sans-serif;
        margin: 10px;
        font-size: 28px;
        border-radius: 10px;
    }
    .q{
        padding: 10px;
    }
    .a{
        padding: 10px;
    }
    #a{
        background-color: white;
        text-align: center;
        margin: 20px;
        border-radius: 10px;
        font-family: 'Cairo', sans-serif;
        font-size: 26px;
    }
</style>
<body>
    <form id="q">
    <p class="q">'''
file1.write(message)
g=input("What is your Question: ")
file1.write(g)
h='''</p>
    </form>
    <form id="a">
    <p class="a">'''
file1.write(h)
i=input("What is your Answer: ")
file1.write(i)
s='''</p>
    </form>
</body>
</html>'''
file1.write(s)
file1.close()
