project_name = input("Enter project name: ")
desc = input("Enter a brief description of your repository: ")
dependencies = input("Enter any packages which your code peruses: ").split()
run = input("Describe how one should run your code: ")
readme = """
# {}

## Description
    {}

## Requirements 
```{}```

### To Run
```{}```

""".format(project_name,desc,dependencies,run)
print(readme)

with open('README.md','w') as file:
    file.write(readme)