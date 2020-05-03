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

### 将本地仓库与远程仓库关联（以Github为例）

我们可以首先在Github上新建一个代码仓库（repository），比如就叫做“Crossin”。完成之后，利用下面的命令将本地的一个仓库（也叫“Crossin”）推送到远程仓库：

```shell
git remote add origin git@github.com:Endlare/Crossin.git
```

其中origin是给远程仓库的命名，一般来说都叫这个名儿，Endare是我在Github的账户名，Crossin就是远程仓库的名字。

下一步，就可以将本地库的所有内容推送到远程库上：

```shell
git push -u origin master
```

`-u`参数是把本地的`master`分支内容推送的远程新的`master`分支，而且把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。但是，在这一步，我的电脑出现了错误：

```shell
To github.com:Endlare/Crossin.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:Endlare/Crossin.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

这是因为我的本地仓库与远程仓库各自都有不同的文件所导致的，提示我应该首先把远程仓库的文件给pull下来。所以我搜索了一下，使用了下面的命令：

```shell
git pull --rebase origin master
```

之后再push发现又报错：

```shell
! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:Endlare/Crossin.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

我的理解是远程与本地的分支冲突，又搜索了一下，用下面这个命令push:

```shell
git push -u origin master -f 
```

终于成功。所以下次对本地仓库远程化一定要同步操作，不能东一榔头西一棒槌:joy:

通过上面的一通操作，已经实现了一个远程仓库，这之后，每次在本地做出修改，只需要利用下面的命令：

```shell
git push origin master
```

就可以将本地的修改同步到远程仓库了。

### 远程仓库克隆

最最最最标准的做法应该是将Github的一个开源仓库拷贝到本地，然后我们在本地进行代码的编辑等等，最后再push到远程，这一系列的操作不仅仅适合于初始化我们自己的仓库，也适合对别人的代码做贡献。从远程拷贝（克隆）一份的方式如下：

```shell
git clone git@github.com:<用户名>/<仓库名>.git
```

然后切换到这个目录下面就可以一顿操作啦:clap:

### 分支（Branch）与主线（Master）的概念

正常情况下只有一个分支，叫做master，指针（HEAD）指在master上，每次commit都在往前延长master，同时改变HEAD的位置，如下图所示：

![git-br-initial](https://www.liaoxuefeng.com/files/attachments/919022325462368/0)

然后，我们也可以创建一个新的分支，比如dev，然后都在这个dev上开发，HEAD就可以移到dev上，如下图所示：

![git-br-create](https://www.liaoxuefeng.com/files/attachments/919022363210080/l)

后面的提交都在dev这条分支上进行：

![git-br-dev-fd](https://www.liaoxuefeng.com/files/attachments/919022387118368/l)

等我们在dev上开发完了，只需要将其与master合并（其实就是HEAD指向换一下），就大功告成：

![git-br-ff-merge](https://www.liaoxuefeng.com/files/attachments/919022412005504/0)

所以Git全是在借助指针实现这些小任务，速度非常快，实在:cow::beer:



