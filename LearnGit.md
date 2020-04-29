### 创建版本库

```
git init
```

### 把文件添加到仓库

```
git add <name of file>
```



###把改动提交

```
git commit -m "name of this submit"
```

### 查看日志

```
git log
```

### 以清爽的形式展示日志

```
git log --pretty=oneline
```

### 回退到上一个版本

```
git reset --hard HEAD^ # 回退一个版本
git reset --hard HEAD^^ # 回退到上上一个版本
git reset --hard HEAD~100 # 回退到100个版本之前
git reset --hard <commit ID> # 回退到指定版本，commit ID可以通过git log 查看
```

### 回到未来

```
git reflog # 查看所有commit的ID
git reset --hard <commit ID> # 回到指定ID的commit
```

