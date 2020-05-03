### 创建版本库

```
git init
```

### 把文件添加到仓库

```
git add <name of file>
```



###把改动提交

```shell
git commit -m "name of this submit"
```

### 查看日志

```shell
git log
```

### 以清爽的形式展示日志

```shell
git log --pretty=oneline
```

### 回退到上一个版本

```shell
git reset --hard HEAD^ # 回退一个版本
git reset --hard HEAD^^ # 回退到上上一个版本
git reset --hard HEAD~100 # 回退到100个版本之前
git reset --hard <commit ID> # 回退到指定版本，commit ID可以通过git log 查看
```

### 回到未来

```shell
git reflog # 查看所有commit的ID
git reset --hard <commit ID> # 回到指定ID的commit
```

### Git的工作区、缓存区（stage/index）与分支的概念

![git-repo](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)

add命令是把文件提交到缓存区，也就是stage，commit再把stage里的文件合并到具体的分支，HEAD的指针指向提交后的文件。

### 查看工作区与版本库的区别

```shell
git diff HEAD -- <文件名>
```

### 撤销在工作区的修改

```shell
git checkout -- <readme.txt>
```

命令`git checkout -- readme.txt`意思就是，把`readme.txt`文件在工作区的修改全部撤销，这里有两种情况：

一种是`readme.txt`自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是`readme.txt`已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。

### 撤销在缓存区的修改

与上一个命令不同，这个命令主要是撤回已经提交到缓存区的修改：

```shell
git reset HEAD <文件名>
```

这个命令既可以做之前的版本回退与回到未来，也可以做撤销缓存区的修改，HEAD参数表示最新的版本。这样做完之后再利用`git checkout -- <文件名>`就又可以把从缓存区撤销到工作区的修改也清楚。世界彻底清净:coffee:

### 删除文件

对于一个已经删除了的文件来说，有两种情况：一是确实是要删除，那么就需要用以下两个命令：

```shell
git rm <文件名> # 将这个文件从缓存区删除，在这一步还可以用git reset HEAD <文件名> 来撤回到工作区
git commit -m "delete" # 将这个文件从版本库删除，这一步就彻底删没了
```

二是删错了，就可以利用前面的checkout命令来撤回：

```shell
git checkout -- <文件名> # 由于版本库里的文件还在，所以还可以用版本库的文件来撤回这一步的操作
```

### Github的ssh设置

具体可直接参考廖雪峰的博文https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416，很简单。



