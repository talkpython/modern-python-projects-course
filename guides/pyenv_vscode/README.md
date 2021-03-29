# Making `pyenv-win` work with VS Code in Windows

At the time of recording this course, VS Code has some problems with discovering Python versions installed with `pyenv-win`. However, there is an experimental feature that solves this issues, so maybe if you are watching it in the future, you won't have this problem.
 
So, if you are a Windows user and you don't see Python versions installed with `pyenv-win` when you run the "Python: Select Interpreter" command, follow the instruction from [this GitHub issue](https://github.com/microsoft/vscode-python/issues/15304):

1. Open the VS Code settings
Search for *Python > Experiments: Opt Into* option and click *Edit in settings.json*:

![]()

