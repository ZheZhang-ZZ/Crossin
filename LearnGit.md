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

### 分支与主线涉及的命令

创建一个叫做`dev`的分支，并切换到该分支:

```shell
git checkout -b dev
git switch -c dev #与上一行命令实现一样的效果，而且更加“顾名思义”
```

相当于:

```shell
git branch dev #创建分支
git checkout dev #切换到该分支
git switch dev #也是切换到某分支
```

查看当前分支:

```shell
git branch
```

合并分支:

```shell
git merge dev #相当于合并dev分支到当前分支
```

删除分支:

```
git branch -d dev
```

常规情况下，git使用fast-forward的方式合并分支，但是这会丢失支线的信息，但是速度较快。如果不想用fast-forward的方式合并分支，可以采用下面的方式:

```shell
git merge -no-ff -m "merge with no-ff" dev
```

此时的合并方式如下图所示：

![git-no-ff-mode](https://www.liaoxuefeng.com/files/attachments/919023225142304/0)

可以看出与前面fast-forward的合并方式的差异。

正常开发时，master通常不动，各个开发人员都向dev提交，等开发完毕再讲master与dev合并：

![git-br-policy](https://www.liaoxuefeng.com/files/attachments/919023260793600/0)



### 查看远程仓库信息

```shell
git remote # 显示远程仓库名称，默认是origin
git remote -v #显示更详细的信息
```

### 往远程仓库推送子分支

```shell
git clone <远程仓库地址> #克隆一份
git checkout -b dev origin/dev #创建远程origin的dev分支到本地
git push origin dev
```

### 推送冲突

上面代码块第三行的推送如果与他人的推送冲突，可以先用`git pull`把远程仓库给拉下来，然后手动解决冲突之后提交。如果`git pull`也失败，则可能是没有指定本地`dev`与远程`origin/dev`的链接，可以利用下面的命令：

```shell
git branch --set-upstream-to=origin/dev dev
```

再重新`git pull`，解决掉冲突合并即可。

### rebase

将错综复杂的提交变成一条直线，命令为：

```shell
git rebase
git log --graph --pretty=oneline --abbrev-commit #查看log
```

### 打标签

打标签感觉是给想要保存的分支在某一时间点一个保存，并用标签进行命名

```shell
git checkout master # 切换到需要打标签的分支
git tag v1.0 # 打标签
git tag # 查看所有标签
git show <标签名> #查看标签信息
git tag -a <标签名> -m 'infomation' # 利用-a 与 -m参数来进行标签名与信息的添加
```

标签的一些操作

```shell
git tag -d <标签名> # 删除标签
git push origin <标签名> # 将指定标签推送到远程仓库
git push origin --tags # 一次性推送所有标签到远程

# 如果要删除一个已经推送到远程的标签，需要以下两步
git tag -d <标签名> # 删除本地标签
git push origin :refs/tags/<标签名> # 删除远程标签
```

### 忽略文件

如果不想让git追踪一些文件（比如隐私文件、数据、编译后文件等等）可以在`.gitignore`中添加这些文件的名称，github已经提供了一些`.gitignore`文件的模板，可以在https://github.com/github/gitignore查询。写完该文件后需要将其提交，如果不想让该文件忽略某一个文件，可以强制提交`git add -f <文件名> `

![ignore](https://cdn.py2china.cn/upload-by-code/lesson/8d78c9b4gy1fj7j6p62mdj20bm09v0te.jpg)

### 配置别名

配置一个`last`命令，让其显示上一条提交：

```shell
 git config --global alias.last 'log -1' # --global是全局参数，即该命令对这台电脑里所有Git仓库都适用
```

还有更丧心病狂的:open_mouth:

```shell
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

### 配置文件

每个仓库的配置文件都放在了`.git/config`文件中，里面有`[alias]`的项，是我们定义的别名，所以可通过直接修改它们来进行别名的修改。而整个用户的所有配置文件是放在用户主目录下的`.gitconfig`中的（也就是`config`命令加了`--global`参数时修改的文件），也可以修改这个文件，从而对这台电脑所有git仓库的配置进行修改。

